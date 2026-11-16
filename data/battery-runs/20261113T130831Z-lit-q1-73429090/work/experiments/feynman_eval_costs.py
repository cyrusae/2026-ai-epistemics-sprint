#!/usr/bin/env python3
"""Extract per-probe wall clock, token usage, and USD cost from Pi subagent transcripts.

Usage: python3 experiments/feynman_eval_costs.py [artifacts_dir]

Reads subagent-artifacts/*_transcript.jsonl, maps each child to a probe key by
finding brief-<key>.md in the task text, then sums the `message.usage` records.
No network, no inference: arithmetic over the harness's own ledger.
"""
import json
import re
import sys
from pathlib import Path

art = Path(sys.argv[1] if len(sys.argv) > 1 else
           "/state/.feynman/sessions/subagent-artifacts")

rows = []
for p in sorted(art.glob("*_transcript.jsonl")):
    key = None
    first = last = None
    inp = out = cache_r = cache_w = reasoning = 0
    cost = 0.0
    n_msgs = 0
    for line in p.open(errors="ignore"):
        try:
            d = json.loads(line)
        except Exception:
            continue
        ts = d.get("ts")
        if isinstance(ts, (int, float)):
            first = ts if first is None else min(first, ts)
            last = ts if last is None else max(last, ts)
        text = d.get("text") or ""
        if not key:
            m = re.search(r"(?:brief-|rs-2026-11/)([A-Za-z0-9]+)\.md", text)
            if m:
                key = m.group(1)
        msg = d.get("message") or {}
        u = msg.get("usage")
        if u:
            n_msgs += 1
            inp += u.get("input", 0) or 0
            out += u.get("output", 0) or 0
            cache_r += u.get("cacheRead", 0) or 0
            cache_w += u.get("cacheWrite", 0) or 0
            reasoning += u.get("reasoning", 0) or 0
            cost += ((u.get("cost") or {}).get("total") or 0)

    if not key:
        continue
    rows.append({
        "key": key,
        "run": p.name.split("_")[0][:8],
        "agent": "verifier" if "verifier" in p.name else "researcher",
        "seconds": round((last - first) / 1000, 1) if first and last else None,
        "turns": n_msgs,
        "input": inp,
        "output": out,
        "cache_read": cache_r,
        "reasoning": reasoning,
        "usd": round(cost, 5),
    })

rows.sort(key=lambda r: r["key"])
print(json.dumps(rows, indent=1))
if rows:
    print(f"\nTOTAL usd={sum(r['usd'] for r in rows):.4f} "
          f"wall_sum_s={sum((r['seconds'] or 0) for r in rows):.1f} "
          f"children={len(rows)}")
