#!/usr/bin/env python3
"""Check coder quotes and merge battery + rubric outputs.

usage: verify.py            (run from analysis/battery)

Reads coders/<coder>__<task>__<run>.json  (task = battery | rubric)
Quote check: `where` is an entry id (L0123, V1-0045 -> corpus/<run>/index.json) or a
design/ path (packets/<run>/design/...). Whitespace/case-normalized substring match;
an entry quote not found in its entry is searched in entries ±3 (NEARBY) and then in the
whole run (ELSEWHERE). Otherwise REJECTED.
Writes derived/battery.md, derived/rubric.md, derived/verified.json
"""
import json, os, re, glob, collections

def norm(s): return re.sub(r"\s+", " ", s.replace("⏎", " ").replace("\\n", " ")).strip().lower()

def extract(path):
    s = open(path, encoding="utf-8", errors="replace").read()
    try: j = json.loads(s)
    except Exception: j = None
    if isinstance(j, dict) and "result" in j and isinstance(j["result"], str): s = j["result"]  # agy json envelope
    elif isinstance(j, dict): return j
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

rows = collections.defaultdict(dict)  # (task, run) -> coder -> parsed
stats = collections.Counter(); out = []
for p in sorted(glob.glob("coders/*__*__*.json")):
    coder, task, run = os.path.basename(p)[:-5].split("__")
    try: j = extract(p)
    except Exception as e:
        stats[(coder, task, "UNPARSEABLE")] += 1; continue
    items = j.get("dimensions") if task == "battery" else j.get("items")
    for name, d in (items or {}).items():
        for ev in d.get("evidence") or []:
            ev["status"] = check(run, ev.get("where"), ev.get("quote")); stats[(coder, task, ev["status"])] += 1
    for n in j.get("notable") or []:
        n["status"] = check(run, n.get("where"), n.get("quote")); stats[(coder, task, n["status"])] += 1
    rows[(task, run)][coder] = j
json.dump({f"{t}|{r}": v for (t, r), v in rows.items()}, open("derived/verified.json", "w"), indent=1)

OK = ("VERIFIED", "NEARBY", "ELSEWHERE")
def ev_md(evs):
    return "".join(f"\n    - `{e.get('where')}` [{e.get('status')}]: \"{(e.get('quote') or '')[:300]}\"" for e in evs or [])

for task, key, fname in (("battery", "dimensions", "battery.md"), ("rubric", "items", "rubric.md")):
    runs = sorted({r for (t, r) in rows if t == task})
    if not runs: continue
    coders = sorted({c for (t, r), v in rows.items() if t == task for c in v})
    dims = []
    for (t, r), v in rows.items():
        if t == task:
            for c in v.values():
                for k in (c.get(key) or {}):
                    if k not in dims: dims.append(k)
    L = [f"# {task}: coder outputs with quote checks\n", "Quote status: VERIFIED (in cited place), NEARBY (±3 entries), ELSEWHERE (found elsewhere in this run), REJECTED (not found), SHORT. Interpretations whose evidence is all REJECTED are marked `!`.\n",
         "## Quote checks\n", "| coder | " + " | ".join(("VERIFIED", "NEARBY", "ELSEWHERE", "REJECTED", "SHORT", "UNPARSEABLE")) + " |", "|---" * 7 + "|"]
    for c in coders:
        L.append(f"| {c} | " + " | ".join(str(stats[(c, task, s)]) for s in ("VERIFIED", "NEARBY", "ELSEWHERE", "REJECTED", "SHORT", "UNPARSEABLE")) + " |")
    L += ["", "## Cross-run table (interpretation per coder)\n", "| run | " + " | ".join(dims) + " |", "|---" * (len(dims) + 1) + "|"]
    for r in runs:
        cells = []
        for dname in dims:
            vals = []
            for c in coders:
                d = ((rows[(task, r)].get(c) or {}).get(key) or {}).get(dname) or {}
                v = d.get("interpretation") or d.get("score") or "?"
                evs = d.get("evidence") or []
                bad = evs and not any(e.get("status") in OK for e in evs)
                vals.append(f"{v}{'!' if bad else ''}")
            cells.append(" / ".join(vals))
        L.append(f"| {r} | " + " | ".join(cells) + " |")
    L.append(f"\nCoders in each cell, in order: {', '.join(coders)}\n")
    for r in runs:
        L.append(f"\n## {r}\n")
        for dname in dims:
            L.append(f"\n### {dname}\n")
            for c in coders:
                d = ((rows[(task, r)].get(c) or {}).get(key) or {}).get(dname)
                if not d: continue
                v = d.get("interpretation") or d.get("score")
                txt = d.get("observation") or d.get("reason") or d.get("count") or ""
                L.append(f"- **{c}** — {v} ({d.get('confidence', '')}): {txt}{ev_md(d.get('evidence'))}")
        if task == "battery":
            L.append("\n### notable\n")
            for c in coders:
                for n in (rows[(task, r)].get(c) or {}).get("notable") or []:
                    L.append(f"- **{c}**: {n.get('note')}{ev_md([n])}")
    open(f"derived/{fname}", "w").write("\n".join(L) + "\n")
    print(f"derived/{fname}: {len(runs)} runs, coders {coders}")
for k, v in sorted(stats.items()): print(*k, v)
