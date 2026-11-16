#!/usr/bin/env python3
"""Quote-check the answer-key exposure second coding (coders/<coder>__exposure__<run>.json).

usage: verify_exposure.py          (run from analysis/battery)

Every yes/partly judgement needs a quote that is found in the cited entry (or within 3 entries) or the
cited design file. A yes/partly whose quote fails is downgraded to "unsupported".
Writes derived/exposure.tsv (one row per subject session) and derived/exposure.md (per-run summary).
"""
import json, os, re, glob, collections
exec(open("verify_probes.py").read().split("\nEMBED = ")[0])   # norm, extract, run_texts, check

FIELDS = (("opened_key", "opened_key_evidence"), ("listed_key", "listed_key_evidence"),
          ("inputs_hold_answers", "inputs_evidence"), ("opened_other_test_outputs", "other_outputs_evidence"))
rows, summ, stats = [], [], collections.Counter()
for p in sorted(glob.glob("coders/*__exposure__*.json")):
    coder, _, run = os.path.basename(p)[:-5].split("__")
    try: j = extract(p)
    except Exception as e: summ.append((run, f"UNPARSEABLE {e}")); continue
    subs = j.get("subjects") or []
    agg = collections.Counter()
    for s in subs:
        r = {"run": run, "session": s.get("session"), "role": s.get("role"), "cwd": s.get("cwd"),
             "task_names_key": s.get("task_names_key"), "isolated": s.get("isolated")}
        for f, ev in FIELDS:
            v = str(s.get(f) or "no").lower()
            if v in ("yes", "partly"):
                e = s.get(ev) or {}
                st = check(run, e.get("where"), e.get("quote")) if e else "NOQUOTE"
                stats[st] += 1
                if st not in ("VERIFIED", "NEARBY"): v = f"unsupported({v},{st})"
            r[f] = v
            if v in ("yes", "partly"): agg[f] += 1
        r["note"] = re.sub(r"\s+", " ", str(s.get("note") or ""))[:200]
        rows.append(r)
    summ.append((run, len(j.get("key_files") or []), len(subs), agg, [k.get("path") for k in j.get("key_files") or []]))
cols = ["run", "session", "role", "cwd", "task_names_key", "listed_key", "opened_key", "inputs_hold_answers", "opened_other_test_outputs", "isolated", "note"]
with open("derived/exposure.tsv", "w") as o:
    o.write("\t".join(cols) + "\n")
    for r in rows: o.write("\t".join(str(r.get(c)) for c in cols) + "\n")
L = ["# Answer-key exposure, second coder (Haiku), quote-checked\n",
     f"Evidence quotes: {dict(stats)}. A yes/partly whose quote was not found is shown as unsupported in `exposure.tsv` and not counted here.\n",
     "| run | key files | subject sessions | opened key | listed key | inputs hold answers | opened other test outputs | marked isolated |", "|---|---|---|---|---|---|---|---|"]
for s in summ:
    if len(s) == 2: L.append(f"| {s[0]} | {s[1]} |||||||"); continue
    run, nk, ns, agg, keys = s
    iso = sum(1 for r in rows if r["run"] == run and str(r["isolated"]).lower() == "yes")
    L.append(f"| {run} | {nk} | {ns} | {agg['opened_key']} | {agg['listed_key']} | {agg['inputs_hold_answers']} | {agg['opened_other_test_outputs']} | {iso} |")
L.append("\n## Sessions that opened a key (quote found)\n")
L += [f"- {r['run']} {r['session']} ({r['role']}): {r['note']}" for r in rows if r["opened_key"] == "yes"]
L.append("\n## Key files named by the coder\n")
L += [f"- {s[0]}: " + ", ".join(f"`{k}`" for k in s[4]) for s in summ if len(s) > 2]
open("derived/exposure.md", "w").write("\n".join(L) + "\n"); print("\n".join(L))
