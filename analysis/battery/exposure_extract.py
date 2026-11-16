#!/usr/bin/env python3
"""Build a compact per-run extract for the answer-key exposure second coder.

usage: exposure_extract.py     (run from analysis/battery)
Writes exposure/<run>.txt: the design/ file list, then for every sub-agent session its task prompt
and every tool call (entry id, tool, arguments trimmed to 400 chars). Tool results are left out.
"""
import re, glob, os
os.makedirs("exposure", exist_ok=True)
for cdir in sorted(glob.glob("corpus/lit-*/")):
    run = os.path.basename(cdir.rstrip("/"))
    if not os.path.isdir(cdir): continue
    out = [f"# Run {run}: sub-agent tool calls (results omitted)\n", "## Files in design/ at the end of the run\n"]
    base = f"packets/{run}/design"
    for root, _, files in os.walk(base):
        for f in sorted(files):
            p = os.path.join(root, f)
            if "/node_modules/" in p or "/.git/" in p: continue
            out.append(f"{os.path.relpath(p, f'packets/{run}')}\t{os.path.getsize(p)}")
    sess = sorted(p for p in glob.glob(cdir + "*.txt") if re.match(r"[RVW]\d+\.txt", os.path.basename(p)))
    if not sess: out.append("\n(no sub-agent sessions in this run's corpus)")
    for p in sess:
        t = open(p).read()
        head = t.split("\n=== ", 1)[0]
        out.append(f"\n## Session {os.path.basename(p)[:-4]}\n{head.strip()[:2500]}\n")
        for m in re.finditer(r"^=== (\S+) \| (\S+) \| ([^\n]*?) ===\n(.*?)(?=^=== |\Z)", t, re.S | re.M):
            eid, ts, kind, body = m.groups()
            if kind.startswith("session start"): out.append(f"{eid} session start {body.strip()[:200]}")
            for c in re.finditer(r"^\[tool call: (\S+) id=\S+\]\n(.*?)(?=^\[tool call|^\[reply|^\[thinking|\Z)", body, re.S | re.M):
                args = re.sub(r"\s+", " ", c.group(2)).strip()
                out.append(f"{eid} {c.group(1)} {args[:400]}")
    open(f"exposure/{run}.txt", "w").write("\n".join(out) + "\n")
    print(len("\n".join(out)), len(sess), run)
