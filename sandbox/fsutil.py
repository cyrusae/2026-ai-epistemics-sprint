#!/usr/bin/env python3
"""Deterministic helpers for fs (no LLM calls).

  fsutil.py snapshot <run> <tag>        list every file in work/ + state/ (size, mtime, sha256) -> logs/<tag>.files.tsv
  fsutil.py packet   <run> [turn]       evidence packet for one turn -> logs/turnNN.packet.md (also printed)
  fsutil.py ls       <runs_dir> [label] status table
"""
import hashlib, json, os, sys, glob

def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 16), b""): h.update(b)
    return h.hexdigest()[:16]

def snapshot(run, tag):
    rows = []
    for root in ("work", "state"):
        for d, _, fs in os.walk(os.path.join(run, root)):
            for f in fs:
                p = os.path.join(d, f); rel = os.path.relpath(p, run)
                if rel.startswith("work/.sandbox/"): continue
                st = os.stat(p); rows.append(f"{rel}\t{st.st_size}\t{int(st.st_mtime)}\t{sha(p)}")
    out = os.path.join(run, "logs", f"{tag}.files.tsv")
    open(out, "w").write("\n".join(sorted(rows)) + "\n")

def read_tsv(p):
    if not os.path.exists(p): return {}
    return {l.split("\t")[0]: l.split("\t")[3] for l in open(p) if l.strip()}

def session_turns(run):
    """Split the main session into turns at each user message."""
    files = sorted(glob.glob(os.path.join(run, "state/.feynman/sessions/*.jsonl")))
    turns, cur = [], None
    for f in files:
        for line in open(f):
            try: e = json.loads(line)
            except Exception: continue
            if e.get("type") != "message": continue
            m = e["message"]
            if m.get("role") == "user":
                cur = []; turns.append(cur)
            if cur is not None: cur.append(m)
    return turns

def text_of(content):
    if isinstance(content, str): return content
    return "\n".join(c.get("text", "") for c in content or [] if c.get("type") == "text")

def trunc(s, n):
    s = s if isinstance(s, str) else json.dumps(s, ensure_ascii=False)
    return s if len(s) <= n else s[:n] + f" …[+{len(s)-n} chars]"

def packet(run, turn=None):
    logs = os.path.join(run, "logs")
    n = turn or len(glob.glob(os.path.join(logs, "turn*.prompt.md")))
    tag = f"turn{n:02d}"
    turns = session_turns(run)
    msgs = turns[n - 1] if len(turns) >= n else []
    L = [f"# Evidence packet: {os.path.basename(run)} / {tag}", "",
         "Mechanically extracted from the Feynman session log and filesystem. No interpretation applied.", ""]
    L += ["## Prompt", "", "```", open(os.path.join(logs, f"{tag}.prompt.md")).read(), "```", ""]
    meta = [l for l in open(os.path.join(logs, "turns.jsonl"))] if os.path.exists(os.path.join(logs, "turns.jsonl")) else []
    if len(meta) >= n: L += ["## Run metadata", "", "`" + meta[n - 1].strip() + "`", ""]
    L += ["## Agent actions (in order)", ""]
    k = 0
    for m in msgs:
        if m.get("role") == "assistant":
            for c in m.get("content") or []:
                if c.get("type") == "toolCall":
                    k += 1; L.append(f"{k}. **{c.get('name')}** `{trunc(c.get('arguments'), 600)}`")
                elif c.get("type") == "text" and c.get("text", "").strip():
                    L.append(f"   - _said:_ {trunc(c['text'].strip(), 400)}")
        elif m.get("role") == "toolResult" and m.get("isError"):
            L.append(f"   - _tool error:_ {trunc(text_of(m.get('content')), 300)}")
    if k == 0: L.append("(no tool calls)")
    final = ""
    for m in reversed(msgs):
        if m.get("role") == "assistant" and text_of(m.get("content")).strip():
            final = text_of(m.get("content")); break
    stops = [m.get("stopReason") for m in msgs if m.get("role") == "assistant"]
    L += ["", f"Last stopReason: `{stops[-1] if stops else 'n/a'}` (assistant messages this turn: {len(stops)})"]
    L += ["", "## Final reply", "", final or "(none)", ""]
    before = read_tsv(os.path.join(logs, f"turn{n-1:02d}.files.tsv")) if n > 1 else {}
    after = read_tsv(os.path.join(logs, f"{tag}.files.tsv"))
    new = [p for p in after if p not in before]; changed = [p for p in after if p in before and before[p] != after[p]]
    skip = lambda p: p.startswith(("state/.feynman/agent/", "state/.feynman/bin/")) or p.endswith("telemetry.json")
    L += ["## Files created this turn", ""] + ([f"- {p}" for p in new if not skip(p)] or ["(none)"])
    L += ["", "## Files modified this turn", ""] + ([f"- {p}" for p in changed if not skip(p)] or ["(none)"])
    out = "\n".join(L) + "\n"
    open(os.path.join(logs, f"{tag}.packet.md"), "w").write(out)
    sys.stdout.write(out)

def ls(runs, label=None):
    rows, stats = [], {}
    for r in sorted(glob.glob(os.path.join(runs, "*"))):
        name = os.path.basename(r)
        if label and f"-{label}-" not in name: continue
        meta = [json.loads(l) for l in open(os.path.join(r, "logs/turns.jsonl"))] if os.path.exists(os.path.join(r, "logs/turns.jsonl")) else []
        dec = []
        for t in range(1, len(meta) + 1):
            p = os.path.join(r, f"logs/turn{t:02d}.decision")
            dec.append(open(p).readline().strip() if os.path.exists(p) else "-")
        cond = " > ".join(f"{m.get('prompt','?')}@{m.get('prompt_sha256','?')[:6]}" for m in meta) or "-"
        if meta:
            g = stats.setdefault(f"{meta[0].get('prompt','?')}@{meta[0].get('prompt_sha256','?')[:6]}",
                                 {"runs": 0, "verdicts": {}, "followed": 0, "failed": 0, "t1": []})
            g["runs"] += 1
            v = dec[0] if dec else "-"; g["verdicts"][v] = g["verdicts"].get(v, 0) + 1
            g["followed"] += len(meta) > 1
            g["failed"] += any(m.get("exit_code") != 0 for m in meta)
            g["t1"].append(meta[0].get("seconds", 0))
        rows.append((name, cond, str(len(meta)), ",".join(str(m["exit_code"]) for m in meta) or "-",
                     ",".join(str(m["seconds"]) + "s" for m in meta) or "-", ",".join(dec) or "-"))
    hdr = ("run", "prompts", "turns", "exit", "time", "decisions")
    w = [max(len(x[i]) for x in rows + [hdr]) for i in range(6)]
    for x in [hdr] + rows: print("  ".join(x[i].ljust(w[i]) for i in range(6)))
    if not stats: return
    print("\nby turn-1 prompt:")
    for k, g in sorted(stats.items()):
        t = sorted(g["t1"]); med = round((t[(len(t) - 1) // 2] + t[len(t) // 2]) / 2)
        vs = ", ".join(f"{n} {v if v != '-' else 'undecided'}" for v, n in sorted(g["verdicts"].items(), key=lambda x: -x[1]))
        print(f"  {k}: {g['runs']} runs | turn 1: {vs} | followed up: {g['followed']} | nonzero exit: {g['failed']} | median turn-1 time: {med}s")

if __name__ == "__main__":
    cmd, *a = sys.argv[1:]
    if cmd == "snapshot": snapshot(*a)
    elif cmd == "packet": packet(a[0], int(a[1]) if len(a) > 1 else None)
    elif cmd == "ls": ls(*a)
