#!/usr/bin/env python3
"""Summarize the three verifier red-team runs from their subagent transcripts."""
import json, glob, os, collections
from datetime import datetime

LABELS = {
    "eda2750b-53bf-42a1-8722-dd7071fd3600": "leaked_answer_key",
    "74adb1bc-43fd-4abf-a27a-16a8edb839d0": "clean_run1",
    "e8cbf99d-6e87-45fb-8102-4a1b4a3a0496": "clean_run2",
}

def ts(s): return datetime.fromisoformat(s.replace("Z", "+00:00"))

out = []
for p in sorted(glob.glob("/state/.feynman/sessions/subagent-artifacts/*_verifier_*_transcript.jsonl"), key=os.path.getmtime):
    recs = [json.loads(l) for l in open(p) if l.strip()]
    run = recs[0].get("runId")
    calls = [(r.get("toolName"), r.get("argsPayload")) for r in recs if r.get("recordType") == "tool_start"]
    reads, cost, toks, errs = [], 0.0, collections.Counter(), 0
    for r in recs:
        if r.get("recordType") == "tool_start" and r.get("toolName") == "read":
            a = r.get("argsPayload")
            if isinstance(a, str):
                try: a = json.loads(a)
                except Exception: pass
            reads.append(str(a.get("path")))
        if r.get("recordType") == "tool_end" and r.get("isError"): errs += 1
        if r.get("recordType") == "message" and r.get("usage"):
            u = r["usage"]; c = u.get("cost") or {}
            cost += c.get("total", 0) if isinstance(c, dict) else c
            for k, v in u.items():
                if isinstance(v, (int, float)) and k != "cost": toks[k] += v
    times = [ts(r["timestamp"]) for r in recs if r.get("timestamp")]
    out.append({
        "run": run, "label": LABELS.get(run, run),
        "wall_seconds": round((times[-1] - times[0]).total_seconds(), 1) if times else None,
        "tool_calls": len(calls), "tool_errors": errs,
        "tools": dict(collections.Counter(n for n, _ in calls)),
        "files_read": reads,
        "cost_usd": round(cost, 6),
        "input_tokens": toks.get("input"), "output_tokens": toks.get("output"),
        "cache_read_tokens": toks.get("cacheRead"),
        "transcript": p,
    })
print(json.dumps(out, indent=2))
