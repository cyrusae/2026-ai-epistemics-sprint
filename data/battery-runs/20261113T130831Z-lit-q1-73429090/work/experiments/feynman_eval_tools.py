#!/usr/bin/env python3
"""Count tool calls and errors per probe from Pi subagent transcripts."""
import json
import re
import sys
from collections import Counter
from pathlib import Path

art = Path(sys.argv[1] if len(sys.argv) > 1 else
           "/state/.feynman/sessions/subagent-artifacts")

rows = []
for p in sorted(art.glob("*_transcript.jsonl")):
    key = None
    tools = Counter()
    errors = Counter()
    for line in p.open(errors="ignore"):
        try:
            d = json.loads(line)
        except Exception:
            continue
        if not key:
            m = re.search(r"(?:brief-|/)([A-Za-z0-9]+)\.md", d.get("text") or "")
            if m:
                key = m.group(1)
        if d.get("recordType") == "tool_start":
            tools[d.get("toolName")] += 1
        elif d.get("recordType") == "tool_end" and d.get("isError"):
            errors[d.get("toolName")] += 1
    if key:
        rows.append((key, sum(tools.values()), dict(tools), sum(errors.values()), dict(errors)))

rows.sort()
for key, n, tools, ne, errs in rows:
    print(f"{key:4} calls={n:3} errors={ne:2}  {tools}" + (f"  ERR={errs}" if errs else ""))
