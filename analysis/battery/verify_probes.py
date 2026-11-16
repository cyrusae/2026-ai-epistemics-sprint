#!/usr/bin/env python3
"""Quote-check the probe inventories (coders/<coder>__probes__<run>.json).

usage: verify_probes.py            (run from analysis/battery)

Checks findings[].quote {where, quote} and incidents[] {entry, quote} against the run's
corpus and design files, with the same rules as verify.py. Also pulls quoted spans out of
probes[].raw_result / reported_result (free text of the form  <where>: "<quote>") and
checks those, as a weaker signal: the coder was not required to format them that way.

Writes derived/probes_verified.json (inventories with a status on every checked quote)
and derived/probes_quotes.md (per-run counts and every quote that is not VERIFIED/NEARBY).
"""
import json, os, re, glob, collections

def norm(s): return re.sub(r"\s+", " ", s.replace("⏎", " ").replace("\\n", " ")).strip().lower()

def extract(path):
    s = open(path, encoding="utf-8", errors="replace").read()
    try: j = json.loads(s)
    except Exception: j = None
    if isinstance(j, dict): return j
    s = re.sub(r"^```(json)?|```$", "", s.strip(), flags=re.M)
    i, k = s.find("{"), s.rfind("}")
    return json.loads(s[i:k + 1])

cache = {}
def run_texts(run):
    if run in cache: return cache[run]
    idx = {k: norm(v) for k, v in json.load(open(f"corpus/{run}/index.json")).items()}
    files = {}
    for p in glob.glob(f"packets/{run}/design/**/*", recursive=True):
        if os.path.isfile(p):
            files[os.path.relpath(p, f"packets/{run}")] = norm(open(p, encoding="utf-8", errors="replace").read())
    cache[run] = (idx, files); return cache[run]

def check(run, where, quote):
    idx, files = run_texts(run)
    q = norm(quote or "")
    if len(q) < 8: return "SHORT"
    where = (where or "").strip().strip("`")
    where = re.sub(r"^(transcript/)?[A-Za-z0-9]+\.txt\s*\(?", "", where)          # "transcript/L.txt (L0118 grep ...)" -> "L0118 grep ..."
    where = re.split(r"[\s,;()]", where)[0] if where else where   # "L0073 (lead)" -> "L0073"
    if where.startswith("design/") or "/" in where:
        w = where if where.startswith("design/") else "design/" + where.lstrip("./")
        if w in files and q in files[w]: return "VERIFIED"
        return "ELSEWHERE" if any(q in t for t in files.values()) or any(q in t for t in idx.values()) else "REJECTED"
    m = re.match(r"([A-Z]+\d*-?)(\d+)$", where)
    if m and where in idx and q in idx[where]: return "VERIFIED"
    if m:
        pre, n = m.group(1), int(m.group(2)); w = len(m.group(2))
        for d in (-3, -2, -1, 1, 2, 3):
            k = f"{pre}{n + d:0{w}d}"
            if k in idx and q in idx[k]: return "NEARBY"
    return "ELSEWHERE" if any(q in t for t in idx.values()) or any(q in t for t in files.values()) else "REJECTED"

EMBED = re.compile(r"((?:design/[^\s:\"]+)|(?:[A-Z]+\d*-?\d{3,}))[^\"]{0,40}?\"((?:[^\"\\]|\\.){8,300})\"")

ORDER = ("VERIFIED", "NEARBY", "ELSEWHERE", "REJECTED", "SHORT", "NOQUOTE")
out, bad, counts = {}, [], collections.defaultdict(collections.Counter)
for p in sorted(glob.glob("coders/*__probes__*.json")):
    coder, _, run = os.path.basename(p)[:-5].split("__")
    try: j = extract(p)
    except Exception as e:
        counts[run]["UNPARSEABLE"] += 1; bad.append((run, "file", "", "UNPARSEABLE", str(e)[:120])); continue
    for f in j.get("findings") or []:
        qd = f.get("quote") if isinstance(f.get("quote"), dict) else {"where": "", "quote": f.get("quote") or ""}
        st = check(run, qd.get("where"), qd.get("quote")); f["status"] = st; counts[run]["finding:" + st] += 1
        if st not in ("VERIFIED", "NEARBY"): bad.append((run, "finding " + str(f.get("id")), qd.get("where"), st, qd.get("quote")))
    for n, inc in enumerate(j.get("incidents") or [], 1):
        w = inc.get("entry") or inc.get("entry id") or inc.get("entry_id") or inc.get("where")
        if not inc.get("quote"):
            inc["status"] = "NOQUOTE"; counts[run]["incident:NOQUOTE"] += 1
            bad.append((run, f"incident {n}", w, "NOQUOTE", inc.get("what") or inc.get("incident"))); continue
        st = check(run, w, inc.get("quote")); inc["status"] = st; counts[run]["incident:" + st] += 1
        if st not in ("VERIFIED", "NEARBY"): bad.append((run, f"incident {n}", w, st, inc.get("quote")))
    for pr in j.get("probes") or []:
        pr["embedded_quotes"] = []
        for fld in ("raw_result", "reported_result"):
            for w, q in EMBED.findall(str(pr.get(fld) or "")):
                st = check(run, w, q.replace('\\"', '"')); counts[run]["embedded:" + st] += 1
                pr["embedded_quotes"].append({"field": fld, "where": w, "quote": q, "status": st})
                if st == "REJECTED": bad.append((run, f"probe {pr.get('id')} {fld}", w, st, q))
    out[run] = j

os.makedirs("derived", exist_ok=True)
json.dump(out, open("derived/probes_verified.json", "w"), indent=1, ensure_ascii=False)
L = ["# probe inventories: quote checks\n",
     "VERIFIED = in the cited place; NEARBY = within 3 transcript entries; ELSEWHERE = in this run but not where cited; REJECTED = not found in this run.",
     "Embedded = quoted spans found inside a probe's raw_result / reported_result text (best effort; the coder was not asked for a fixed format there).\n",
     "| run | probes | scripts | findings | incidents | finding quotes V/N/E/R/S/none | incident quotes V/N/E/R/S/none | embedded V/N/E/R/S/none |", "|---|---|---|---|---|---|---|---|"]
for run in sorted(out):
    j, c = out[run], counts[run]
    cell = lambda k: "/".join(str(c[f"{k}:{s}"]) for s in ORDER)
    L.append(f"| {run} | {len(j.get('probes') or [])} | {len(j.get('scripts') or [])} | {len(j.get('findings') or [])} | {len(j.get('incidents') or [])} | {cell('finding')} | {cell('incident')} | {cell('embedded')} |")
L.append("\n## Quotes that did not check out\n")
for run, what, where, st, q in bad:
    L.append(f"- **{run}** {what} [{st}] at `{where}`: {str(q)[:300]}")
open("derived/probes_quotes.md", "w").write("\n".join(L) + "\n")
print("\n".join(L[3:5 + len(out)])); print(len(bad), "quotes not verified")
