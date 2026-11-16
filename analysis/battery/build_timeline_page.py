#!/usr/bin/env python3
"""Interactive timeline page: embeds derived/timeline.tsv + timing.tsv into timeline_template.html.
usage: build_timeline_page.py <corpus-dir> derived/timeline.tsv derived/timing.tsv timeline_template.html <out.html>"""
import csv, json, sys, collections, datetime, bisect
corpus, tl, tm, tpl, out = sys.argv[1:6]
iso = lambda s: datetime.datetime.fromisoformat(s.replace("Z", "+00:00")).timestamp()
ev = collections.defaultdict(list)
for r in csv.DictReader(open(tl), delimiter="\t"):
    ev[(r["run"], int(r["turn"]))].append({"s": r["session"], "a": r["agent"], "k": r["kind"][0], "n": r["name"],
        "t0": round(float(r["t0"]), 2), "t1": round(float(r["t1"]), 2), "f": r["flag"]})
cost = collections.Counter()
for run in {k[0] for k in ev}:
    sess = list(csv.DictReader(open(f"{corpus}/{run}/sessions.tsv"), delimiter="\t"))
    starts = [iso(json.loads(l)["timestamp"]) for l in open(sess[0]["file"]) if '"role":"user"' in l]
    for s in sess:
        for l in open(s["file"]):
            e = json.loads(l); m = e.get("message") or {}
            if m.get("role") == "assistant":
                c = (m.get("usage") or {}).get("cost") or {}
                t = bisect.bisect_right(starts, iso(e["timestamp"]))
                cost[(run, max(t, 1))] += c.get("total", 0) if isinstance(c, dict) else 0
multi = collections.Counter(k[0] for k in ev)
blocks = []
for r in csv.DictReader(open(tm), delimiter="\t"):
    k = (r["run"], int(r["turn"]))
    blocks.append({"id": f"{r['run']}-{r['turn']}", "label": r["run"].replace("lit-", "") + (f" · turn {r['turn']}" if multi[r["run"]] > 1 else ""),
        "wall": float(r["lead_wall_s"]), "end": float(r["last_activity_s"]), "lead_model": float(r["lead_model_s"]), "lead_tool": float(r["lead_tool_s"]),
        "nsub": int(r["subagent_sessions"]), "peak": int(r["peak_concurrent"]), "waiting": float(r["lead_waiting_s"]), "cost": round(cost[k], 4), "ev": ev[k]})
# merge multi-turn runs into one block: later turns start PAD seconds after the previous turn's last activity
PAD = 20
merged = {}
for b in blocks:
    run = b["id"].rsplit("-", 1)[0]; turn = int(b["id"].rsplit("-", 1)[1])
    for e in b["ev"]: e["u"] = turn
    if run not in merged:
        b["id"], b["label"] = run, run.replace("lit-", "") + (f" · {multi[run]} turns" if multi[run] > 1 else "")
        b["offsets"] = [0]; b["_lead_end"] = b["wall"]; merged[run] = b; continue
    m = merged[run]; off = m["offsets"][-1] + m["_lead_end"] + PAD
    for e in b["ev"]: e["t0"] = round(e["t0"] + off, 2); e["t1"] = round(e["t1"] + off, 2)
    m["ev"] += b["ev"]; m["offsets"].append(off); m["_lead_end"] = b["wall"]; m["end"] = max(m["end"], off + b["end"])
    for k in ("wall", "lead_model", "lead_tool", "nsub", "waiting", "cost"): m[k] += b[k]
    m["peak"] = max(m["peak"], b["peak"])
blocks = list(merged.values())
open(out, "w").write(open(tpl).read().replace("__DATA__", json.dumps({"blocks": blocks}, separators=(",", ":"))))
print(out, len(blocks), "blocks", sum(len(b["ev"]) for b in blocks), "events")
