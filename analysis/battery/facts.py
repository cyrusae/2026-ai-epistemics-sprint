#!/usr/bin/env python3
"""Scripted, judgement-free facts per sandbox run.

usage: facts.py <runs-dir> <label-glob> <outdir>
  e.g. facts.py ../../sandbox/runs 'lit-q*' derived

Writes:
  outdir/facts.md            one section per run + cross-run table
  outdir/facts.tsv           cross-run table
  outdir/files.tsv           every file the agent left in work/ (run, path, bytes, kind)
  outdir/harness_reads.tsv   reads of Feynman prompt/skill files and fetches of Feynman source (GitHub)
  outdir/executions.tsv      bash commands that executed something the agent built, or Feynman itself
  outdir/keywords.tsv        keyword spot checks over thinking + replies (all sessions)
Run ids are shortened to e.g. lit-q1-73429090, matching corpus/<run>/.
"""
import json, os, sys, glob, re, collections

runs_dir, pat, out = sys.argv[1:4]
os.makedirs(out, exist_ok=True)

WORKFLOWS = {  # file signatures each prompt template leaves behind (from the shipped 0.5.65 prompts)
    "deepresearch": [r"outputs/\.drafts/[^/]+-cited\.md", r"outputs/[^/]+\.provenance\.md"],
    "lit":          [r"outputs/\.drafts/[^/]+-research-(foundations|recent)\.md"],
    "review":       [r"outputs/[^/]+-review\.md"],
    "audit":        [r"outputs/[^/]+-audit\.md"],
    "compare":      [r"outputs/[^/]+-comparison\.md"],
    "recipe":       [r"outputs/[^/]+-recipe\.md"],
    "summarize":    [r"outputs/\.notes/[^/]+-summary"],
    "autoresearch": [r"(^|/)autoresearch\.(md|jsonl|sh)$"],
}
KEYWORDS = {
    "self-feynman": r"\b(I am|I'm|as|act as|acting as|role is|role as|me \(|myself \(|we are|I, )\s*['\"`*]?Feynman\b|\b(user|me|I|myself)\s*\((as )?Feynman\)|\bFeynman \((me|myself|this agent|the agent)\)",
    "as-an-ai": r"\b(as an AI|I am an AI|I'm an AI|as a language model|I am a language model|as an (AI )?(research )?agent|I am an? (AI |research(-first)? )?agent)\b",
    "user-wants": r"\b[Tt]he user (wants|asked|asks|expects|needs|is asking|would like|requested|said|prefers|intends|is (likely|probably)|seems to|wanted|cares)\b",
    "user-other": r"\b[Tt]he user (has|is|provided|approved|built|said|already|didn't|did not)\b",
    "self-model": r"\b(this (very )?session|this run|I am running|I'm running|my own (model|session|log|harness))\b",
}
FEYN = re.compile(r"(^|[;&|(]\s*|\$\(\s*|timeout \S+\s+)(\S*/)?feynman(\.js)?\s+[^\n]*(--prompt|-p\b|--print|--new-session|--continue|--model|--thinking|audit|replicate|lit|deepresearch)")
EXEC = re.compile(r"\b(python3?|node|bash|sh|feynman|pytest|npx)\s+(?!-c\b|-m\s+json|-V|--version|-\s)[^|;&]*", re.I)

def short(run):
    m = re.search(r"-(lit-q\d+|[a-z0-9-]+?)-(\d+)$", os.path.basename(run))
    return f"{m.group(1)}-{m.group(2)}" if m else os.path.basename(run)

def load(path):
    out = []
    for line in open(path, encoding="utf-8"):
        try: out.append(json.loads(line))
        except Exception: pass
    return out

def texts(m):
    c = m.get("content")
    if isinstance(c, str): return [("text", c)]
    r = []
    for x in c or []:
        if not isinstance(x, dict): continue
        if x.get("type") == "thinking": r.append(("thinking", x.get("thinking") or ""))
        elif x.get("type") == "text": r.append(("text", x.get("text") or ""))
    return r

def tsv(name, header, rows):
    with open(os.path.join(out, name), "w") as f:
        f.write("\t".join(header) + "\n")
        for r in rows: f.write("\t".join(str(x).replace("\t", " ").replace("\n", " ⏎ ") for x in r) + "\n")

table, files_rows, reads_rows, exec_rows, kw_rows, md = [], [], [], [], [], []
for run in sorted(glob.glob(os.path.join(runs_dir, f"*-{pat}-*"))):
    if not os.path.isdir(os.path.join(run, "work")): continue
    rid = short(run)
    turns = [json.loads(l) for l in open(os.path.join(run, "logs/turns.jsonl"))] if os.path.exists(os.path.join(run, "logs/turns.jsonl")) else []
    decisions = []
    for t in range(1, len(turns) + 1):
        p = os.path.join(run, f"logs/turn{t:02d}.decision")
        decisions.append(open(p).readline().strip() if os.path.exists(p) else "-")
    sess_dir = os.path.join(run, "state/.feynman/sessions")
    lead = sorted(glob.glob(os.path.join(sess_dir, "*.jsonl")))
    children = sorted(glob.glob(os.path.join(sess_dir, "*/*/run-*/session.jsonl")))
    cost = {"lead": 0.0, "children": 0.0}; tools = collections.Counter(); errors = 0; asst = 0
    for kind, paths in (("lead", lead), ("children", children)):
        for p in paths:
            sess = "L" if kind == "lead" else "child:" + p.split("/")[-3][:8]
            for e in load(p):
                if e.get("type") != "message": continue
                m = e["message"]
                if m.get("role") == "assistant":
                    u = (m.get("usage") or {}).get("cost") or {}
                    cost[kind] += u.get("total", 0) if isinstance(u, dict) else (u or 0)
                    if kind == "lead": asst += 1
                    for x in m.get("content") or []:
                        if not isinstance(x, dict) or x.get("type") != "toolCall": continue
                        name, args = x.get("name"), x.get("arguments") or {}
                        a = json.dumps(args)
                        if kind == "lead": tools[name] += 1
                        for f in re.findall(r"(?:skills/[\w-]+/SKILL|prompts/[\w-]+)\.md", a):
                            reads_rows.append((rid, sess, name, "harness-file", f))
                        for u2 in re.findall(r"https?://[^\s\"'\\)]*(?:Companion-Inc/feynman|feynman\.is|getfeynman)[^\s\"'\\)]*", a, re.I):
                            reads_rows.append((rid, sess, name, "feynman-source-url", u2))
                        if name == "bash":
                            cmd = args.get("command", "")
                            for mm in EXEC.finditer(cmd):
                                s = mm.group(0).strip()
                                if re.search(r"\.(py|js|sh|mjs)\b", s):
                                    exec_rows.append((rid, sess, "script", s[:240]))
                            if FEYN.search(cmd):
                                exec_rows.append((rid, sess, "feynman", cmd[:240]))
                    for field, t in texts(m):
                        for k, rx in KEYWORDS.items():
                            for mm in re.finditer(rx, t):
                                i = mm.start()
                                kw_rows.append((rid, sess, field, k, mm.group(0), t[max(0, i-140):i+200]))
                elif m.get("role") == "toolResult" and m.get("isError") and kind == "lead":
                    errors += 1
    # files left in work/
    wfiles = []
    for root, dirs, fs in os.walk(os.path.join(run, "work")):
        dirs[:] = [d for d in dirs if d not in (".sandbox", "node_modules", ".git", ".venv", "venv", "__pycache__")]
        for f in fs:
            p = os.path.join(root, f); rel = os.path.relpath(p, os.path.join(run, "work"))
            ext = os.path.splitext(f)[1].lower()
            kind = ("plan" if rel.startswith("outputs/.plans") else "draft" if rel.startswith("outputs/.drafts")
                    else "output" if rel.startswith("outputs/") else
                    "script" if ext in (".py", ".js", ".mjs", ".sh", ".ts") else
                    "data" if ext in (".json", ".jsonl", ".csv", ".tsv", ".txt", ".log") else "other")
            wfiles.append((rel, os.path.getsize(p), kind))
            files_rows.append((rid, rel, os.path.getsize(p), kind))
    names = [w[0] for w in wfiles]
    wf = [k for k, rxs in WORKFLOWS.items() if all(any(re.search(rx, n) for n in names) for rx in rxs)]
    nexec = sum(1 for r in exec_rows if r[0] == rid and r[2] == "script")
    nfeyn = sum(1 for r in exec_rows if r[0] == rid and r[2] == "feynman")
    src = sum(1 for r in reads_rows if r[0] == rid and r[3] == "feynman-source-url")
    evals = sum(1 for r in reads_rows if r[0] == rid and r[3] == "feynman-source-url" and "eval" in r[4].lower())
    kinds = collections.Counter(w[2] for w in wfiles)
    kwc = collections.Counter(r[3] for r in kw_rows if r[0] == rid)
    row = dict(run=rid, turns=len(turns), exits=",".join(str(t["exit_code"]) for t in turns),
               minutes=",".join(str(round(t["seconds"]/60)) for t in turns), decisions=",".join(decisions),
               prompts=">".join(t.get("prompt", "?") for t in turns),
               cost_lead=round(cost["lead"], 3), cost_children=round(cost["children"], 3), lead_msgs=asst,
               lead_tool_calls=sum(tools.values()), lead_tool_errors=errors, subagent_calls=tools.get("subagent", 0),
               children=len(children), files=len(wfiles), scripts=kinds["script"], data=kinds["data"],
               outputs=kinds["output"] + kinds["plan"] + kinds["draft"], workflows="+".join(wf) or "-",
               script_runs=nexec, feynman_invocations=nfeyn, feynman_source_fetches=src, evals_fetches=evals,
               **{f"kw_{k}": kwc.get(k, 0) for k in KEYWORDS})
    table.append(row)
    md.append(f"## {rid}\n\n" + "\n".join(f"- **{k}**: {v}" for k, v in row.items() if k != "run")
              + "\n\nFiles in work/ (excl. venv/.git):\n" + "\n".join(f"  - `{n}` ({s} B, {k})" for n, s, k in sorted(wfiles)) + "\n")

cols = list(table[0].keys())
tsv("facts.tsv", cols, [[r[c] for c in cols] for r in table])
tsv("files.tsv", ["run", "path", "bytes", "kind"], files_rows)
tsv("harness_reads.tsv", ["run", "session", "tool", "kind", "target"], reads_rows)
tsv("executions.tsv", ["run", "session", "kind", "command"], exec_rows)
tsv("keywords.tsv", ["run", "session", "field", "keyword", "match", "context"], kw_rows)
show = ["run", "decisions", "minutes", "cost_lead", "cost_children", "files", "scripts", "workflows", "script_runs", "feynman_invocations", "feynman_source_fetches", "evals_fetches", "kw_self-feynman", "kw_as-an-ai", "kw_user-wants"]
with open(os.path.join(out, "facts.md"), "w") as f:
    f.write("# Scripted facts per run\n\nNo judgement involved; see facts.py for definitions. Keyword counts include false positives (\"Feynman\" is also the topic): read keywords.tsv.\n\n")
    f.write("| " + " | ".join(show) + " |\n|" + "---|" * len(show) + "\n")
    for r in table: f.write("| " + " | ".join(str(r[c]) for c in show) + " |\n")
    f.write("\n" + "\n".join(md))
print(f"{len(table)} runs -> {out}/facts.md")
