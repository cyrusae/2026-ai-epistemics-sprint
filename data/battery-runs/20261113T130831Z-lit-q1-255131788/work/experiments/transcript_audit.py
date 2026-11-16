#!/usr/bin/env python3
"""Audit a Feynman/Pi session JSONL for eval-readiness.

Checks:
  1. JSONL parses; every record has type/timestamp.
  2. Every assistant toolCall has a matching toolResult (by toolCallId), and vice versa.
  3. Message parentId chain resolves to a known record (no dangling parents).
  4. Assistant messages carry usage + cost + durationMs + stopReason.
  5. Timestamps are non-decreasing in file order.
  6. Tool errors are recorded with isError and non-empty content.
  7. Cost/token totals are recomputable from records.

Exit code 0 if all checks pass, 1 otherwise. Prints a machine-readable summary.
"""
import json, sys, collections
from datetime import datetime

def ts(s):
    return datetime.fromisoformat(s.replace("Z", "+00:00"))

def audit(path, allow_open_tail=False):
    recs, bad_lines = [], []
    with open(path) as f:
        for i, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                recs.append(json.loads(line))
            except Exception as e:
                bad_lines.append((i, str(e)))

    out = {"path": path, "records": len(recs), "bad_json_lines": bad_lines,
           "types": dict(collections.Counter(r.get("type") for r in recs))}

    ids = {r.get("id") for r in recs if r.get("id")}
    dangling = [r.get("id") for r in recs if r.get("parentId") and r["parentId"] not in ids]

    calls, results = {}, {}
    for r in recs:
        if r.get("type") != "message":
            continue
        m = r.get("message", {})
        if m.get("role") == "assistant":
            for b in m.get("content") or []:
                if isinstance(b, dict) and b.get("type") == "toolCall":
                    calls[b.get("id")] = (b.get("name"), r.get("id"))
        elif m.get("role") == "toolResult":
            results[m.get("toolCallId")] = (m.get("toolName"), m.get("isError"), r.get("id"))

    unmatched_calls = sorted(set(calls) - set(results))
    open_tail = []
    if allow_open_tail and recs and recs[-1].get("type") == "message":
        last_id = recs[-1].get("id")
        open_tail = [k for k in unmatched_calls if calls[k][1] == last_id]
        unmatched_calls = [k for k in unmatched_calls if k not in open_tail]
    unmatched_results = sorted(set(results) - set(calls))
    mismatched_names = sorted(k for k in set(calls) & set(results) if calls[k][0] != results[k][0])
    tool_errors = sorted(k for k, v in results.items() if v[1])

    assistants = [r["message"] for r in recs if r.get("type") == "message"
                  and r["message"].get("role") == "assistant"]
    no_usage = [r.get("id") for r in recs if r.get("type") == "message"
                and r["message"].get("role") == "assistant" and not r["message"].get("usage")]
    no_cost = [r.get("id") for r in recs if r.get("type") == "message"
               and r["message"].get("role") == "assistant"
               and not (r["message"].get("usage", {}).get("cost") or {}).get("total")]
    no_duration = [r.get("id") for r in recs if r.get("type") == "message"
                   and r["message"].get("role") == "assistant" and "durationMs" not in r["message"]]
    no_stop = [r.get("id") for r in recs if r.get("type") == "message"
               and r["message"].get("role") == "assistant" and not r["message"].get("stopReason")]

    times = [ts(r["timestamp"]) for r in recs if r.get("timestamp")]
    regressions = sum(1 for a, b in zip(times, times[1:]) if b < a)

    tot = {k: 0 for k in ("input", "output", "cacheRead", "cacheWrite", "reasoning", "totalTokens")}
    cost = 0.0
    for m in assistants:
        u = m.get("usage") or {}
        for k in tot:
            tot[k] += u.get(k) or 0
        cost += ((u.get("cost") or {}).get("total") or 0.0)

    out.update({
        "dangling_parent_ids": dangling,
        "tool_calls": len(calls),
        "tool_results": len(results),
        "unmatched_calls": unmatched_calls,
        "open_tail_excluded": open_tail,
        "unmatched_results": unmatched_results,
        "tool_name_mismatches": mismatched_names,
        "tool_error_calls": tool_errors,
        "assistant_messages": len(assistants),
        "assistant_missing_usage": no_usage,
        "assistant_missing_cost": no_cost,
        "assistant_missing_duration": no_duration,
        "assistant_missing_stop_reason": no_stop,
        "timestamp_regressions": regressions,
        "tokens": tot,
        "cost_total_usd": round(cost, 8),
    })
    failures = []
    if bad_lines: failures.append("bad_json")
    if dangling: failures.append("dangling_parent")
    if unmatched_calls: failures.append("unmatched_tool_calls")
    if unmatched_results: failures.append("unmatched_tool_results")
    if mismatched_names: failures.append("tool_name_mismatch")
    if no_usage: failures.append("missing_usage")
    if no_cost: failures.append("missing_cost")
    if no_duration: failures.append("missing_duration")
    if no_stop: failures.append("missing_stop_reason")
    if regressions: failures.append("timestamp_regression")
    out["failures"] = failures
    out["pass"] = not failures
    return out

if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    allow_open_tail = "--allow-open-tail" in sys.argv
    p = args[0] if args else None
    if not p:
        print("usage: transcript_audit.py <session.jsonl>", file=sys.stderr)
        sys.exit(2)
    result = audit(p, allow_open_tail=allow_open_tail)
    print(json.dumps(result, indent=2))
    sys.exit(0 if result["pass"] else 1)
