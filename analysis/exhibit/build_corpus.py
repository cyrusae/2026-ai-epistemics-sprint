#!/usr/bin/env python3
"""Build a citable plain-text corpus from a Feynman session and its sub-agent sessions.

usage: build_corpus.py <lead-session.jsonl> <outdir>

Writes:
  outdir/sessions.tsv           code, agent, runId, start, file, entries
  outdir/<code>.txt             full rendering (tool results trimmed)
  outdir/chunks/<code>-NN.txt   ~CHUNK_CHARS slices, split on entry boundaries
  outdir/index.json             {entry_id: full untrimmed text} for quote verification
Entry ids: L0001 for the lead session, R1-0001 / V1-0001 / W1-0001 for researcher /
verifier / reviewer children (numbered by start time). Every entry header is
'=== <id> | <time> | <kind> ...'.
"""
import json, os, sys, glob, re, datetime

TRIM_HEAD, TRIM_TAIL, CHUNK_CHARS = 1500, 400, 120_000
PREFIX = {"researcher": "R", "verifier": "V", "reviewer": "W"}

def ts(x):
    if isinstance(x, (int, float)):
        return datetime.datetime.utcfromtimestamp(x / 1000).strftime("%H:%M:%S")
    return str(x)[11:19] if x else "--:--:--"

def text_of(c):
    if isinstance(c, str): return c
    out = []
    for p in c or []:
        if p.get("type") == "text": out.append(p.get("text", ""))
        elif p.get("type") == "image": out.append("[image]")
    return "\n".join(out)

def trim(s):
    if len(s) <= TRIM_HEAD + TRIM_TAIL + 200: return s
    return s[:TRIM_HEAD] + f"\n[... {len(s) - TRIM_HEAD - TRIM_TAIL} chars omitted by corpus builder ...]\n" + s[-TRIM_TAIL:]

def render(path, code):
    entries, full = [], {}
    n = 0
    for line in open(path):
        try: e = json.loads(line)
        except Exception: continue
        t = e.get("type")
        body_full = body = None
        if t == "message":
            m = e["message"]; role = m.get("role")
            if role == "assistant":
                u = m.get("usage") or {}; cost = (u.get("cost") or {}).get("total")
                hdr = f"assistant | {m.get('provider')}/{m.get('model')} | stop={m.get('stopReason')}" + (f" | cost=${cost:.5f}" if cost else "") + (f" | {m.get('durationMs')}ms" if m.get("durationMs") else "")
                parts = []
                for p in m.get("content") or []:
                    if p.get("type") == "thinking": parts.append("[thinking]\n" + (p.get("thinking") or ""))
                    elif p.get("type") == "text": parts.append("[reply text]\n" + p.get("text", ""))
                    elif p.get("type") == "toolCall":
                        parts.append(f"[tool call: {p.get('name')} id={p.get('id','')[-8:]}]\n" + json.dumps(p.get("arguments"), ensure_ascii=False, indent=1))
                if m.get("errorMessage"): parts.append("[error] " + str(m.get("errorMessage")))
                body = body_full = "\n".join(parts)
            elif role == "toolResult":
                hdr = f"tool result: {m.get('toolName')} id={str(m.get('toolCallId',''))[-8:]}" + (" | isError=TRUE" if m.get("isError") else "")
                d = m.get("details") or {}
                if d.get("truncated"): hdr += f" | harness-truncated (shown {d.get('shownLines')}/{d.get('totalLines')} lines)"
                body_full = text_of(m.get("content")); body = trim(body_full)
            elif role == "user":
                hdr = "USER MESSAGE"; body = body_full = text_of(m.get("content"))
            elif role == "system":
                hdr = "system"; body = body_full = text_of(m.get("content")) or "(empty in log)"
            else:
                hdr = role; body = body_full = text_of(m.get("content"))
        elif t == "custom_message":
            hdr = f"harness-injected message ({e.get('customType')}, shown-to-user={e.get('display')})"
            body_full = text_of(e.get("content")); body = trim(body_full)
        elif t == "custom":
            d = e.get("data") or {}
            hdr = f"harness record ({e.get('customType')})"
            urls = [u.get("url") for u in d.get("urlMetadata", [])] + [q.get("query") for q in d.get("queries", [])]
            body = body_full = f"{d.get('type')}: " + "; ".join(str(u) for u in urls if u)
        elif t in ("model_change", "thinking_level_change"):
            hdr = t; body = body_full = json.dumps({k: v for k, v in e.items() if k not in ("id", "parentId", "type", "timestamp")})
        elif t == "session":
            hdr = "session start"; body = body_full = json.dumps({k: e.get(k) for k in ("id", "cwd", "timestamp")})
        else:
            continue
        n += 1
        eid = f"{code}{n:04d}" if code == "L" else f"{code}-{n:04d}"
        when = ts(e.get("timestamp") or (e.get("message") or {}).get("timestamp"))
        entries.append(f"=== {eid} | {when} | {hdr} ===\n{body}\n")
        full[eid] = body_full
    return entries, full

def main():
    lead, out = sys.argv[1], sys.argv[2]
    os.makedirs(out + "/chunks", exist_ok=True)
    sess_dir = lead[:-len(".jsonl")]
    art = os.path.join(os.path.dirname(lead), "subagent-artifacts")
    kids = []
    for f in glob.glob(sess_dir + "/*/run-*/session.jsonl"):
        rid = f.split("/")[-3]
        meta = glob.glob(f"{art}/{rid}_*_meta.json")
        agent = json.load(open(meta[0]))["agent"] if meta else "child"
        start = json.loads(open(f).readline()).get("timestamp", "")
        kids.append((start, agent, rid, f))
    kids.sort()
    counters, sessions = {}, [("L", "lead", "-", json.loads(open(lead).readline()).get("timestamp", ""), lead)]
    for start, agent, rid, f in kids:
        p = PREFIX.get(agent, "C"); counters[p] = counters.get(p, 0) + 1
        sessions.append((f"{p}{counters[p]}", agent, rid, start, f))
    index, rows = {}, []
    for code, agent, rid, start, f in sessions:
        entries, full = render(f, code)
        index.update(full)
        um = next((e for e in entries if "| USER MESSAGE ===" in e), None)
        who = ("the human's only message in the entire session" if code == "L"
               else "this sub-agent's task prompt, written by the lead agent (the human did not write it)")
        ref = f"# For reference, {who}:\n#   " + (um.split("\n", 1)[1].strip().replace("\n", "\n#   ") if um else "(none)") + "\n"
        head = (f"# Session {code}: {agent} (run {rid}), started {start}\n# Entries: {len(entries)}. "
                f"Tool results over {TRIM_HEAD+TRIM_TAIL} chars are trimmed in this rendering.\n{ref}\n")
        open(f"{out}/{code}.txt", "w").write(head + "\n".join(entries))
        chunk, k = [], 1
        def flush():
            nonlocal chunk, k
            if chunk:
                open(f"{out}/chunks/{code}-{k:02d}.txt", "w").write(head + "\n".join(chunk)); k += 1; chunk = []
        size = 0
        for en in entries:
            if size + len(en) > CHUNK_CHARS and chunk: flush(); size = 0
            chunk.append(en); size += len(en)
        flush()
        rows.append(f"{code}\t{agent}\t{rid}\t{start}\t{f}\t{len(entries)}\t{k-1} chunk(s)")
    open(f"{out}/sessions.tsv", "w").write("code\tagent\trunId\tstart\tfile\tentries\tchunks\n" + "\n".join(rows) + "\n")
    json.dump(index, open(f"{out}/index.json", "w"))
    print("\n".join(rows))

main()
