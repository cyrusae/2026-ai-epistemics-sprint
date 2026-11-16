#!/usr/bin/env python3
"""Audit a Pi/Feynman JSONL session for observability + artifact evidence.

Usage: python3 audit.py <session.jsonl> [--json out.json]
Prints tool-call counts, message roles, token usage, artifact paths mentioned,
and integrity vocabulary counts. Read-only.
"""
import json, sys, re, collections, os

def texts(v):
    if isinstance(v, str):
        return [v]
    if isinstance(v, list):
        out = []
        for x in v:
            out += texts(x)
        return out
    if isinstance(v, dict):
        out = []
        for k in ("text", "content", "thinking"):
            if k in v:
                out += texts(v[k])
        return out
    return []

def main():
    path = sys.argv[1]
    outpath = None
    if "--json" in sys.argv:
        outpath = sys.argv[sys.argv.index("--json") + 1]
    rows, tools, roles, usage = [], collections.Counter(), collections.Counter(), collections.Counter()
    tool_errors = 0
    paths = set()
    all_text = []
    assistant_text = []
    first_ts = last_ts = None
    with open(path, encoding="utf-8", errors="replace") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                ev = json.loads(line)
            except json.JSONDecodeError:
                continue
            rows.append(ev)
            ts = ev.get("timestamp")
            if ts:
                first_ts = first_ts or ts
                last_ts = ts
            if ev.get("type") == "message":
                msg = ev.get("message", {})
                roles[msg.get("role", "?")] += 1
                u = msg.get("usage") or {}
                for k, v in u.items():
                    if isinstance(v, (int, float)):
                        usage[k] += v
                acc = []
                def walk(o):
                    if isinstance(o, dict):
                        for k, v in o.items():
                            if k in ("content", "text", "message", "summary", "output") and isinstance(v, (str, list, dict)):
                                acc.append(v)
                            walk(v)
                    elif isinstance(o, list):
                        for v in o:
                            walk(v)
                walk(msg)
                for v in acc:
                    all_text += texts(v)
                    if msg.get("role") == "assistant":
                        assistant_text += texts(v)
                content = msg.get("content")
                if isinstance(content, list):
                    for part in content:
                        if isinstance(part, dict) and part.get("type") in ("toolCall", "tool_call"):
                            name = part.get("name") or part.get("toolName") or "?"
                            tools[name] += 1
                            args = part.get("arguments") or {}
                            if isinstance(args, dict) and isinstance(args.get("path"), str):
                                paths.add(args["path"])
                        elif isinstance(part, dict) and part.get("type") in ("toolResult", "tool_result"):
                            if part.get("isError") or part.get("error"):
                                tool_errors += 1
    joined = "\n".join(all_text)
    aj = "\n".join(assistant_text)
    vocab = {w: len(re.findall(r"\b" + w + r"\b", aj, re.I))
             for w in ["verified", "confirmed", "reproduced", "blocked", "unverified", "inferred", "TODO"]}
    artifacts = sorted({m for m in re.findall(r"(?:outputs|experiments|notes|papers)/[A-Za-z0-9._/-]+", joined)
                        if "." in m.split("/")[-1]})
    result = {
        "session": os.path.basename(path),
        "events": len(rows),
        "roles": dict(roles),
        "tool_calls_total": sum(tools.values()),
        "tool_calls": dict(tools.most_common()),
        "tool_errors": tool_errors,
        "usage": dict(usage),
        "unique_tool_paths": len(paths),
        "distinct_urls_in_transcript": len(set(re.findall(r"https?://[^\s)\]]+", joined))),
        "integrity_vocab_assistant_only": vocab,
        "artifact_paths_mentioned": len(artifacts),
        "first_timestamp": first_ts,
        "last_timestamp": last_ts,
        "event_types": dict(collections.Counter(r.get("type") for r in rows)),
    }
    print(json.dumps(result, indent=2))
    if outpath:
        with open(outpath, "w") as f:
            json.dump(result, f, indent=2)

if __name__ == "__main__":
    main()
