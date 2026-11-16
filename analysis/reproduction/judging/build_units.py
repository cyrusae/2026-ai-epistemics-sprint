#!/usr/bin/env python3
"""Build one blind judging packet per stage-unit, plus scripted evidence of computed numbers.

usage: build_units.py <runs-dir> <outdir>      (run from analysis/reproduction/judging)

Units (30):  aud-<id>  = seq turn 1 (audit)
             rep-<id>  = replication stage: seq turns 2+3, or repl turns 1+2 (repl-1976113579: turns 1+3;
                         its turn 2 was a 4-s watchdog kill before the prompt reached the agent)
Unit ids are shuffled codes (U01..U30) so judges can't tell seq from repl; key in units.tsv.

packets/<code>/
  PROMPTS.md       the human's prompts for this stage (same text for every replication unit)
  REPLY.md         the agent's final reply at the end of each turn of the stage (stdout)
  files/           files under work/ created or changed during the stage (no venvs, raw data, repo copy;
                   text files > 200 KB truncated; binaries listed only)
  FILES.txt        every file created/changed in the stage, with size (including the ones not copied)
  COMPUTED.md      scripted: lines of *tool output* (not prose) during the stage that contain numbers
                   near each reproduction target, with where they came from. Evidence, not a score.
  MANIFEST.txt
"""
import os, sys, json, glob, re, random, shutil, datetime, csv

runs_dir, out = sys.argv[1:3]
SKIPDIR = re.compile(r"(^|/)(\.venv[^/]*|venv|\.git|node_modules|__pycache__|site-packages|repo_r|\.sandbox)(/|$)")
RAW = re.compile(r"\.(vec|bin|npy|npz|pkl|pt|gz|zip|tar|tgz)$|/data/raw/")
CAP = 200_000
iso = lambda s: datetime.datetime.fromisoformat(s.replace("Z", "+00:00")).timestamp()

TARGETS = {  # id: (keywords regex, numeric windows)
 "C1 cos(d_PCA,d_g) 0.389": (r"cos|pca|direction|d_g", [(0.37, 0.40)]),
 "C2 classifier acc ES 0.92 / FR 0.83": (r"acc|svc|classif|lda", [(0.89, 0.94), (0.80, 0.85)]),
 "C3 ES Original MWEAT 3.6918": (r"mweat|weat|diff|original|es\b", [(3.60, 3.80)]),
 "C4 FR Original MWEAT 2.3437 (10-pair 2.3958)": (r"mweat|weat|diff|fr\b|french", [(2.30, 2.45)]),
 "C5 ES Shift Ori MWEAT 0.3090": (r"shift|mweat|weat", [(0.29, 0.33)]),
 "C6 translation P@1/P@10 79.2/89.0, 78.2/89.4, 76.1/88.1": (r"p@|precision|transl|@1|@10|nn|csls", [(75.5, 90.5), (0.755, 0.905)]),
 "C7 word-pair MRR gap 0.4867 / ASD 0.108": (r"mrr|gap|asd|word.?pair", [(0.44, 0.52), (0.09, 0.13)]),
 "C8 Spearman 0.45 (p 0.0004)": (r"spearman|rho|ρ", [(0.42, 0.48)]),
 "C9 ES word similarity 0.7392": (r"pearson|spearman|simil|semeval", [(0.69, 0.76)]),
}
NUM = re.compile(r"(?<![\w.])-?\d+\.\d+")

def load(path):
    out = []
    for l in open(path, encoding="utf-8", errors="replace"):
        try: out.append(json.loads(l))
        except Exception: pass
    return out

def snapshot(run, t):
    p = f"{run}/logs/turn{t:02d}.files.tsv"
    if not os.path.exists(p): return {}
    d = {}
    for l in open(p):
        f = l.rstrip("\n").split("\t")
        if f[0].startswith("work/"): d[f[0]] = (int(f[1]), f[-1])
    return d

units = []
for run in sorted(glob.glob(f"{runs_dir}/*-seq-*") + glob.glob(f"{runs_dir}/*-repl-*")):
    name = os.path.basename(run); cond = "seq" if "-seq-" in name else "repl"
    turns = len(glob.glob(f"{run}/logs/turn*.prompt.md"))
    if cond == "seq":
        units.append((name, cond, "audit", [1]))
        units.append((name, cond, "replication", [2, 3]))
    else:
        units.append((name, cond, "replication", [1, 3] if name.endswith("1976113579") else [1, 2]))

random.seed(20261115); codes = [f"U{i:02d}" for i in range(1, len(units) + 1)]; random.shuffle(codes)
os.makedirs(out, exist_ok=True)
key = open(os.path.join(out, "..", "units.tsv"), "w"); key.write("code\trun\tcondition\tstage\tturns\n")

for code, (name, cond, stage, tts) in sorted(zip(codes, units)):
    run = f"{runs_dir}/{name}"; d = f"{out}/{code}"
    shutil.rmtree(d, ignore_errors=True); os.makedirs(f"{d}/files")
    key.write(f"{code}\t{name}\t{cond}\t{stage}\t{','.join(map(str, tts))}\n")
    with open(f"{d}/PROMPTS.md", "w") as f, open(f"{d}/REPLY.md", "w") as g:
        for i, t in enumerate(tts, 1):
            f.write(f"## Message {i} from the human\n\n{open(f'{run}/logs/turn{t:02d}.prompt.md').read().strip()}\n\n")
            g.write(f"## Agent's final reply after message {i}\n\n{open(f'{run}/logs/turn{t:02d}.stdout.txt', errors='replace').read().strip()}\n\n")
    # files created/changed during the stage
    before = snapshot(run, min(tts) - 1) if min(tts) > 1 else {}
    if min(tts) == 1:  # baseline = seeded materials
        before = {k: v for k, v in snapshot(run, 1).items() if "repo_r" in k or k.endswith(".pdf")}
    after = snapshot(run, max(tts))
    changed = sorted(k for k, v in after.items() if before.get(k, (None, None))[1] != v[1])
    listing = []
    for k in changed:
        rel = k[len("work/"):]; size = after[k][0]
        if SKIPDIR.search(rel): continue
        copied = "listed"
        src = f"{run}/{k}"
        if not RAW.search(rel) and os.path.isfile(src):
            try:
                raw = open(src, "rb").read(CAP + 1); raw.decode("utf-8")
                dst = f"{d}/files/{rel}"; os.makedirs(os.path.dirname(dst), exist_ok=True)
                with open(dst, "wb") as h:
                    h.write(raw[:CAP]);
                    if len(raw) > CAP: h.write(f"\n[... truncated; original {size} bytes]\n".encode())
                copied = "copied"
            except UnicodeDecodeError: pass
        listing.append(f"{size:>12}  {copied:6}  {rel}")
    open(f"{d}/FILES.txt", "w").write("files under work/ created or changed in this stage (size, copied|listed, path)\n" + "\n".join(listing) + "\n")
    # computed numbers: tool outputs (lead + sub-agents) within the stage's time window
    lead = sorted(glob.glob(f"{run}/state/.feynman/sessions/*.jsonl"))[0]
    L = load(lead); starts = [iso(e["timestamp"]) for e in L if e.get("message", {}).get("role") == "user"] + [1e18]
    lo, hi = starts[min(tts) - 1], starts[min(max(tts), len(starts) - 1)]
    sess = [("lead", L)] + [(os.path.basename(os.path.dirname(os.path.dirname(p)))[:8], load(p)) for p in glob.glob(f"{run}/state/.feynman/sessions/*/*/run-*/session.jsonl")]
    hits = {t: [] for t in TARGETS}
    for sname, S in sess:
        calls = {}
        for e in S:
            m = e.get("message") or {}
            if not (lo <= iso(e.get("timestamp", "1970-01-01T00:00:00Z")) < hi): continue
            if m.get("role") == "assistant":
                for c in m.get("content") or []:
                    if isinstance(c, dict) and c.get("type") == "toolCall": calls[c["id"]] = c
            if m.get("role") != "toolResult": continue
            cmd = json.dumps((calls.get(m.get("toolCallId")) or {}).get("arguments") or {})
            if m.get("toolName") in ("read", "write", "edit") or re.search(r"\bcat |\bsed -n|\bhead |\bgrep |\btail ", cmd): continue  # reading files back is not computing
            text = "".join(c.get("text", "") for c in m.get("content") or [] if isinstance(c, dict))
            for line in text.splitlines():
                nums = [float(x) for x in NUM.findall(line)]
                if not nums or len(line) > 400: continue
                for t, (kw, wins) in TARGETS.items():
                    if re.search(kw, line, re.I) and any(a <= abs(n) <= b for n in nums for a, b in wins):
                        hits[t].append(f"- [{sname} {e['timestamp'][11:19]}] `{line.strip()[:220]}`")
    with open(f"{d}/COMPUTED.md", "w") as f:
        f.write("# Numbers printed by commands the agent ran during this stage\n\nScripted extraction, not a score. Lines come from command *output* (file reads excluded), filtered by keyword and a numeric window around each target. A target with no lines here was probably not computed in this stage; a number that appears only in the report may have been copied from the paper.\n\n")
        for t, h in hits.items():
            uniq = list(dict.fromkeys(h))
            f.write(f"## {t}\n\n" + ("\n".join(uniq[:12]) + (f"\n- ... {len(uniq) - 12} more" if len(uniq) > 12 else "") if uniq else "(no matching output lines)") + "\n\n")
    with open(f"{d}/MANIFEST.txt", "w") as f:
        for root, _, fs in os.walk(d):
            for fn in sorted(fs):
                p = os.path.join(root, fn); f.write(f"{os.path.getsize(p):>10}  {os.path.relpath(p, d)}\n")
    print(code, name[-22:], stage, tts, len(listing), "files", sum(bool(h) for h in hits.values()), "targets w/ output")
key.close()
