#!/usr/bin/env python3
"""Re-parse Feynman's committed research-eval result files (repo evals/results/*.jsonl).

This does not re-run the scorer. It recomputes stored-field aggregates only.
"""
import glob
import json
import os
import statistics

rows = []
for f in sorted(glob.glob("/tmp/feynman-repo/evals/results/*.jsonl")):
    for line in open(f):
        if line.strip():
            r = json.loads(line)
            r["_file"] = os.path.basename(f)
            rows.append(r)

def vals(k):
    return [r[k] for r in rows if r.get(k) is not None]

out = {
    "rows": len(rows),
    "completed": sum(bool(r.get("completed")) for r in rows),
    "completion_rate": round(sum(bool(r.get("completed")) for r in rows) / len(rows), 3),
    "citation_validity": {"n": len(vals("citation_validity")),
                          "min": min(vals("citation_validity")),
                          "max": max(vals("citation_validity")),
                          "mean": round(statistics.mean(vals("citation_validity")), 3)},
    "title_match": {"n": len(vals("title_match")),
                    "min": round(min(vals("title_match")), 3),
                    "max": max(vals("title_match")),
                    "mean": round(statistics.mean(vals("title_match")), 3)},
    "key_recall": {"n": len(vals("key_recall")),
                   "min": min(vals("key_recall")),
                   "max": max(vals("key_recall")),
                   "mean": round(statistics.mean(vals("key_recall")), 3)},
    "citations": sum(r.get("citations", 0) for r in rows),
    "tokens": sum((r.get("usage") or {}).get("total_tokens", 0) for r in rows),
    "wall_seconds": sum(r.get("wall_s") or 0 for r in rows),
    "models": sorted({r.get("model") for r in rows}),
    "feynman_versions": sorted({str(r.get("feynman_version")) for r in rows}),
    "question_ids": sorted({r.get("id") for r in rows}),
    "per_file": {},
}
for f in sorted(glob.glob("/tmp/feynman-repo/evals/results/*.jsonl")):
    rs = [json.loads(l) for l in open(f) if l.strip()]
    out["per_file"][os.path.basename(f)] = {
        "rows": len(rs), "done": sum(bool(r.get("completed")) for r in rs)}
print(json.dumps(out, indent=2))
open("/work/experiments/feynman-harness-eval/committed-evals-audit.json", "w").write(json.dumps(out, indent=2))
