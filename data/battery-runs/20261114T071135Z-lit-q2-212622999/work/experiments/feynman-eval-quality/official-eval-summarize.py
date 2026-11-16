#!/usr/bin/env python3
"""Summarize the committed Feynman /lit eval result files."""
import glob
import json
import os
from statistics import mean

ROOT = os.path.join(os.path.dirname(__file__), "official-eval", "results")

print("| Result file | Version | Dirty | Model | IDs | Done | Cites | Valid | Title | Recall | Wall (s) | Tokens | Cost |")
print("|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|")
all_rows = []
for path in sorted(glob.glob(os.path.join(ROOT, "*.jsonl"))):
    rows = [json.loads(line) for line in open(path) if line.strip()]
    all_rows.extend(rows)
    first = rows[0]
    def pct(key):
        vals = [r[key] for r in rows if isinstance(r.get(key), (int, float))]
        return f"{round(100 * mean(vals))}%" if vals else "-"
    print(
        f"| {os.path.basename(path)} | {first.get('feynman_version')} | {first.get('git_dirty')} | "
        f"{first.get('model')} | {','.join(r['id'] for r in rows)} | "
        f"{sum(1 for r in rows if r.get('completed'))}/{len(rows)} | "
        f"{sum(r.get('citations', 0) for r in rows)} | {pct('citation_validity')} | {pct('title_match')} | {pct('key_recall')} | "
        f"{sum(r.get('wall_s', 0) for r in rows)} | {sum((r.get('usage') or {}).get('total_tokens', 0) for r in rows)} | "
        f"${sum((r.get('usage') or {}).get('cost_usd', 0) for r in rows):.2f} |"
    )

completed = [r for r in all_rows if r.get("completed")]
print()
print(f"Rows: {len(all_rows)}; completed: {len(completed)}; incomplete: {len(all_rows) - len(completed)}")
print(f"Total tokens: {sum((r.get('usage') or {}).get('total_tokens', 0) for r in all_rows)}")
print(f"Total wall seconds: {sum(r.get('wall_s', 0) for r in all_rows)}")
print(f"Cost fields: {sorted({(r.get('usage') or {}).get('cost_usd') for r in all_rows})}")
print(f"Distinct question ids: {sorted({r['id'] for r in all_rows})}")
print(f"Distinct versions: {sorted({r.get('feynman_version') for r in all_rows})}")
print(f"Dirty flags: {sorted({r.get('git_dirty') for r in all_rows})}")
print("Incomplete rows:")
for r in all_rows:
    if not r.get("completed"):
        print(f"  {r['id']} version={r.get('feynman_version')} wall={r.get('wall_s')} tokens={(r.get('usage') or {}).get('total_tokens')}")
