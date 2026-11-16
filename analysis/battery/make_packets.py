#!/usr/bin/env python3
"""Assemble one self-contained, read-only packet directory per run for the coders.

usage: make_packets.py <runs-dir> <label-glob> <corpus-dir> <ref-dir> <outdir>

packets/<run>/
  PROMPTS.md          the human's prompts to this run, in order (verbatim)
  design/             copy of the run's work/ (no venv/.git/node_modules; files > 300 KB truncated with a marker)
  transcript/         corpus rendering: L.txt (lead) + child sessions + sessions.tsv; entry ids like L0123, R1-0045
  reference/          Feynman v0.5.65 README.md and evals/README.md + evals/questions.jsonl (from the public repo)
  FACTS.md            scripted facts for this run (from derived/facts.md)
"""
import os, sys, glob, re, shutil, json

runs_dir, pat, corpus, ref, out = sys.argv[1:6]
SKIP = {".sandbox", ".venv", "venv", ".git", "node_modules", "__pycache__"}
CAP = 300_000
facts = open("derived/facts.md").read().split("\n## ")

def short(run):
    m = re.search(r"-(lit-q\d+)-(\d+)$", os.path.basename(run)); return f"{m.group(1)}-{m.group(2)}"

for run in sorted(glob.glob(os.path.join(runs_dir, f"*-{pat}-*"))):
    rid = short(run); d = os.path.join(out, rid)
    shutil.rmtree(d, ignore_errors=True); os.makedirs(d)
    prompts = sorted(glob.glob(os.path.join(run, "logs/turn*.prompt.md")))
    with open(os.path.join(d, "PROMPTS.md"), "w") as f:
        for p in prompts:
            f.write(f"## {os.path.basename(p).split('.')[0]} (from the human)\n\n{open(p).read()}\n\n")
    for root, dirs, fs in os.walk(os.path.join(run, "work")):
        dirs[:] = [x for x in dirs if x not in SKIP]
        for fn in fs:
            src = os.path.join(root, fn); rel = os.path.relpath(src, os.path.join(run, "work"))
            dst = os.path.join(d, "design", rel); os.makedirs(os.path.dirname(dst), exist_ok=True)
            if os.path.getsize(src) > CAP:
                with open(src, "rb") as a, open(dst, "wb") as b:
                    b.write(a.read(CAP)); b.write(f"\n\n[... truncated by packet builder; original {os.path.getsize(src)} bytes]\n".encode())
            else: shutil.copy2(src, dst)
    shutil.copytree(os.path.join(corpus, rid), os.path.join(d, "transcript"), ignore=shutil.ignore_patterns("chunks", "index.json"))
    os.makedirs(os.path.join(d, "reference/evals"))
    shutil.copy2(os.path.join(ref, "README.md"), os.path.join(d, "reference/README.md"))
    for fn in ("README.md", "questions.jsonl"):
        shutil.copy2(os.path.join(ref, "evals", fn), os.path.join(d, "reference/evals", fn))
    sec = next((s for s in facts if s.startswith(rid + "\n")), "")
    open(os.path.join(d, "FACTS.md"), "w").write("# Scripted facts\n\n## " + sec)
    print(rid, sum(len(fs) for _, _, fs in os.walk(d)), "files")
