#!/usr/bin/env python3
"""Audit the Feynman harness's own JSONL traces for this run.

Reads the parent session and every child subagent session under it, computes
tool-call/error/token counts, and writes a JSON artifact. No network calls.
"""
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path("/state/.feynman/sessions")
PARENT_ID = sys.argv[1] if len(sys.argv) > 1 else "01a1d524-f68b-71b8-9990-9d016e5a908c"


def session_files():
    parent = next(ROOT.glob(f"*_{PARENT_ID}.jsonl"), None)
    files = []
    if parent:
        files.append(("parent", parent))
    base = ROOT / f"*{PARENT_ID}"
    for p in sorted(ROOT.glob(f"*{PARENT_ID}/*/run-*/session.jsonl")):
        files.append((p.parent.parent.name[:8], p))
    return files


def parse(path: Path):
    stats = {
        "file": str(path),
        "messages": 0,
        "assistant_turns": 0,
        "tool_calls": Counter(),
        "tool_errors": Counter(),
        "search_calls": Counter(),
        "input_tokens": 0,
        "output_tokens": 0,
        "cost_usd": 0.0,
        "models": set(),
        "claim_labels": Counter(),
        "error_messages": [],
    }
    for line in path.read_text(encoding="utf-8").splitlines():
        try:
            o = json.loads(line)
        except json.JSONDecodeError:
            continue
        if o.get("type") == "model_change":
            stats["models"].add(f"{o.get('provider')}/{o.get('modelId')}")
        if o.get("type") != "message":
            continue
        stats["messages"] += 1
        m = o["message"]
        role = m.get("role")
        if role == "assistant":
            stats["assistant_turns"] += 1
            u = m.get("usage") or {}
            stats["input_tokens"] += u.get("input", 0)
            stats["output_tokens"] += u.get("output", 0)
            cost = (u.get("cost") or {}).get("total", 0)
            stats["cost_usd"] += cost if isinstance(cost, (int, float)) else 0
            for part in m.get("content", []):
                if part.get("type") == "toolCall":
                    stats["tool_calls"][part.get("name", "?")] += 1
                elif part.get("type") == "text":
                    txt = part.get("text", "")
                    for w in ("verified", "confirmed", "checked", "reproduced"):
                        stats["claim_labels"][w] += len(
                            re.findall(rf"\b{w}\b", txt, re.I))
        elif role == "toolResult":
            name = m.get("toolName", "?")
            if m.get("isError"):
                stats["tool_errors"][name] += 1
                content = m.get("content", [])
                txt = " ".join(p.get("text", "") for p in content if isinstance(p, dict))
                if txt:
                    stats["error_messages"].append(txt[:200])
            if name in ("web_search", "fetch_content", "get_search_content",
                        "feynman_science_database_search"):
                stats["search_calls"][name] += 1
    stats["models"] = sorted(stats["models"])
    stats["tool_calls"] = dict(stats["tool_calls"])
    stats["tool_errors"] = dict(stats["tool_errors"])
    stats["search_calls"] = dict(stats["search_calls"])
    stats["claim_labels"] = dict(stats["claim_labels"])
    stats["cost_usd"] = round(stats["cost_usd"], 6)
    return stats


def main():
    rows = [{"kind": k, **parse(p)} for k, p in session_files()]
    totals = {
        "sessions": len(rows),
        "messages": sum(r["messages"] for r in rows),
        "assistant_turns": sum(r["assistant_turns"] for r in rows),
        "tool_calls": sum(sum(r["tool_calls"].values()) for r in rows),
        "tool_errors": sum(sum(r["tool_errors"].values()) for r in rows),
        "input_tokens": sum(r["input_tokens"] for r in rows),
        "output_tokens": sum(r["output_tokens"] for r in rows),
        "cost_usd": round(sum(r["cost_usd"] for r in rows), 6),
    }
    all_tools = Counter()
    all_errors = Counter()
    for r in rows:
        all_tools.update(r["tool_calls"])
        all_errors.update(r["tool_errors"])
    totals["tools"] = dict(all_tools)
    totals["errors_by_tool"] = dict(all_errors)
    out = {"parent_id": PARENT_ID, "totals": totals, "sessions": rows}
    dest = Path("/work/experiments/feynman-harness-eval/trace-audit.json")
    dest.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(json.dumps({"totals": totals, "dest": str(dest)}, indent=2))


if __name__ == "__main__":
    main()