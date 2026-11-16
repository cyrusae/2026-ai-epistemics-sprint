#!/usr/bin/env python3
"""Deterministic counts over a Feynman session + sub-agent sessions (no LLM).

usage: counts.py <lead-session.jsonl> <corpus-dir> <outdir>
Uses corpus/sessions.tsv for session codes so entry ids match the corpus.
Writes outdir/counts.md (summary) and outdir/*.tsv (candidate lists for coding).
"""
import json, sys, re, os, collections, glob

lead, corpus, out = sys.argv[1:4]
os.makedirs(out, exist_ok=True)
sessions = [l.rstrip("\n").split("\t") for l in open(f"{corpus}/sessions.tsv")][1:]
art = os.path.join(os.path.dirname(lead), "subagent-artifacts")

def load(path, code):
    rows, n = [], 0
    for line in open(path):
        try: e = json.loads(line)
        except Exception: continue
        if e.get("type") not in ("message", "custom_message", "custom", "model_change", "thinking_level_change", "session"): continue
        n += 1
        e["_id"] = f"{code}{n:04d}" if code == "L" else f"{code}-{n:04d}"
        rows.append(e)
    return rows

def text_of(c):
    if isinstance(c, str): return c
    return "\n".join(p.get("text", "") for p in c or [] if p.get("type") == "text")

R = []  # report lines
def h(s): R.append(f"\n## {s}\n")
def p(s=""): R.append(s)
def tsv(name, header, rows):
    with open(f"{out}/{name}", "w") as f:
        f.write("\t".join(header) + "\n")
        for r in rows: f.write("\t".join(str(x).replace("\t", " ").replace("\n", " ⏎ ") for x in r) + "\n")

data = {s[0]: (s, load(s[4], s[0])) for s in sessions}

# ---------- overview + cost ----------
h("Sessions, tool calls, errors, cost (from per-message usage in each session log)")
p("| code | agent | assistant msgs | tool calls | tool errors | cost (log) | cost (meta.json) | first → last |")
p("|---|---|---|---|---|---|---|---|")
tot_log = tot_meta = 0; lead_cost = 0
calls_by_tool = collections.Counter(); err_by_tool = collections.Counter()
for code, (s, rows) in data.items():
    am = [e for e in rows if e.get("type") == "message" and e["message"].get("role") == "assistant"]
    tc = sum(1 for e in am for c in e["message"].get("content") or [] if c.get("type") == "toolCall")
    te = sum(1 for e in rows if e.get("type") == "message" and e["message"].get("role") == "toolResult" and e["message"].get("isError"))
    cost = sum(((e["message"].get("usage") or {}).get("cost") or {}).get("total") or 0 for e in am)
    meta = glob.glob(f"{art}/{s[2]}_*_meta.json")
    mc = json.load(open(meta[0]))["usage"]["cost"] if meta else None
    tot_log += cost; tot_meta += mc or 0
    if code == "L": lead_cost = cost
    t = [e.get("timestamp") for e in rows if isinstance(e.get("timestamp"), str)]
    p(f"| {code} | {s[1]} | {len(am)} | {tc} | {te} | ${cost:.4f} | {'' if mc is None else f'${mc:.4f}'} | {t[0][11:19] if t else ''} → {t[-1][11:19] if t else ''} |")
p(f"\nLead session cost from its own log: **${lead_cost:.4f}**. Children (logs): ${tot_log - lead_cost:.4f}. "
  f"Lead + children: **${tot_log:.4f}**. Children per meta.json: ${tot_meta:.4f}.")
p("The exhibit compares $0.15 (agent's self-report) with $0.52 (provider records). Check which of the figures above each corresponds to.")

# ---------- tool calls: per tool, errors, result first lines ----------
h("Tool calls by tool (all sessions) and error results")
results = {}
for code, (s, rows) in data.items():
    for e in rows:
        if e.get("type") == "message" and e["message"].get("role") == "toolResult":
            results[e["message"].get("toolCallId")] = e
call_rows = []
for code, (s, rows) in data.items():
    for e in rows:
        if e.get("type") == "message" and e["message"].get("role") == "assistant":
            for c in e["message"].get("content") or []:
                if c.get("type") != "toolCall": continue
                r = results.get(c.get("id"))
                err = bool(r and r["message"].get("isError"))
                first = text_of(r["message"].get("content")).strip().split("\n")[0][:200] if r else "(no result)"
                calls_by_tool[(code[0], c.get("name"))] += 1
                if err: err_by_tool[(code[0], c.get("name"))] += 1
                call_rows.append((e["_id"], r["_id"] if r else "", code, c.get("name"), "ERROR" if err else "ok",
                                  ",".join(sorted((c.get("arguments") or {}).keys())), json.dumps(c.get("arguments"), ensure_ascii=False)[:300], first))
p("| session kind | tool | calls | error results |"); p("|---|---|---|---|")
for k, v in sorted(calls_by_tool.items(), key=lambda x: (x[0][0] != "L", -x[1])):
    p(f"| {'lead' if k[0]=='L' else k[0]+'*'} | {k[1]} | {v} | {err_by_tool.get(k, 0)} |")
tsv("tool_calls.tsv", ["call_entry", "result_entry", "session", "tool", "status", "arg_keys", "args(300)", "result_first_line"], call_rows)
p("\nFull list: `tool_calls.tsv`.")

# ---------- sub-agent launches ----------
h("Sub-agent tool calls in the lead session (item f)")
sub = [r for r in call_rows if r[2] == "L" and r[3] == "subagent"]
p(f"{len(sub)} `subagent` calls; {sum(r[4]=='ERROR' for r in sub)} returned isError.")
p("| entry | status | arg keys | result (first line) |"); p("|---|---|---|---|")
for r in sub: p(f"| {r[0]} | {r[4]} | {r[5]} | {r[7][:120].replace('|','/')} |")
launches = [r for r in sub if "task" in r[5].split(",") or "workflow" in r[5].split(",")]
p(f"\nCalls carrying a `task` or `workflow` key: {len(launches)}. Calls with neither: {len(sub) - len(launches)}.")

# ---------- fetch without url ----------
h("fetch_content calls (item f)")
fc = [r for r in call_rows if r[3] == "fetch_content"]
nourl = [r for r in fc if not ({"url", "urls"} & set(r[5].split(",")))]
p(f"{len(fc)} calls in all sessions; {len(nourl)} with neither `url` nor `urls`.")
for r in fc: p(f"- {r[0]} ({r[2]}) {r[4]} keys=[{r[5]}] → {r[7][:100]}")

# ---------- 'the user' mentions ----------
h("Mentions of 'the user' / 'user' in assistant reasoning and replies (item a)")
pat = re.compile(r"\b(the user|user's|user)\b", re.I)
mrows = []
for code, (s, rows) in data.items():
    for e in rows:
        if e.get("type") == "message" and e["message"].get("role") == "assistant":
            for c in e["message"].get("content") or []:
                field = c.get("thinking") if c.get("type") == "thinking" else c.get("text") if c.get("type") == "text" else None
                if not field: continue
                for m in pat.finditer(field):
                    a, b = max(0, m.start() - 160), min(len(field), m.end() + 160)
                    mrows.append((e["_id"], code, c["type"], field[a:b]))
by = collections.Counter((r[1][0], r[2]) for r in mrows)
p(f"{len(mrows)} matches. " + ", ".join(f"{'lead' if k[0]=='L' else k[0]+'*'} {k[1]}: {v}" for k, v in sorted(by.items())))
p("Every match with ±160 chars of context is in `user_mentions.tsv`, the candidate list for Table 4 classification. "
  "Note: the session had exactly one real user message (lead), and children's 'user' is their task prompt.")
tsv("user_mentions.tsv", ["entry", "session", "field", "context"], mrows)

# ---------- 'Feynman' / self-identification ----------
h("Mentions of 'Feynman' and self-identification phrases in assistant reasoning and replies (SELF-ID)")
fpat = re.compile(r"\bFeynman\b|\b(I am|I'm|as an?) (an? )?(AI|assistant|agent|model|language model|research agent)\b|\bmy (own )?model\b|\bwho (built|made|created) me\b", re.I)
frows = []
for code, (s_, rows) in data.items():
    for e in rows:
        if e.get("type") == "message" and e["message"].get("role") == "assistant":
            for c in e["message"].get("content") or []:
                field = c.get("thinking") if c.get("type") == "thinking" else c.get("text") if c.get("type") == "text" else None
                if not field: continue
                for m in fpat.finditer(field):
                    a, b = max(0, m.start() - 200), min(len(field), m.end() + 200)
                    near = field[max(0, m.start() - 80):m.end() + 80]
                    selfref = bool(re.search(r"\b(I am|I'm|I was|me|my|myself|acting as|you are|You are|I \(|we are)\b", near))
                    frows.append((e["_id"], code, c["type"], m.group(0), "self-ref?" if selfref else "", field[a:b]))
fb = collections.Counter((r[1][0], r[2], "Feynman" if r[3].lower() == "feynman" else "self-phrase") for r in frows)
p(f"{len(frows)} matches. " + ", ".join(f"{'lead' if k[0]=='L' else k[0]+'*'} {k[1]} {k[2]}: {v}" for k, v in sorted(fb.items())))
p("All matches with ±200 chars of context: `self_id.tsv`. Mentions of the harness name in tool arguments (paths, docs URLs) are excluded; only thinking and reply text count.")
tsv("self_id.tsv", ["entry", "session", "field", "match", "selfref_heuristic", "context"], frows)
p(f"{sum(1 for r in frows if r[4])} of these have a first-person or 'acting as'/'you are' phrase within 80 chars (column `selfref_heuristic`): the likeliest self-identifications. Most other 'Feynman' hits are the harness as research topic.")

# ---------- truncated reads followed by writes ----------
h("Truncated or partial reads followed by edit/write of the same path (item c)")
partial_rows = []
for code, (s, rows) in data.items():
    calls, partial = {}, {}
    for e in rows:
        if e.get("type") != "message": continue
        m = e["message"]
        if m.get("role") == "assistant":
            for c in m.get("content") or []:
                if c.get("type") != "toolCall": continue
                a = c.get("arguments") or {}
                calls[c.get("id")] = (c.get("name"), a, e["_id"])
                if c.get("name") in ("edit", "write") and a.get("path"):
                    base = os.path.basename(a["path"])
                    if base in partial:
                        partial_rows.append((code, partial[base][0], partial[base][1], e["_id"], c.get("name"), a["path"]))
        elif m.get("role") == "toolResult":
            name, a, cid = calls.get(m.get("toolCallId"), (None, {}, None))
            if name != "read": continue
            txt = text_of(m.get("content")); d = m.get("details") or {}
            trunc = d.get("truncated") or a.get("offset") or a.get("limit") or re.search(r"\[(?:Showing|Truncated|\d+ more lines)", txt)
            if trunc and a.get("path"):
                partial[os.path.basename(a["path"])] = (e["_id"], f"offset={a.get('offset')} limit={a.get('limit')} lines_returned={txt.count(chr(10))+1} trunc_flag={bool(d.get('truncated'))}")
p(f"{len(partial_rows)} edit/write calls after a partial read of the same file name.")
for r in partial_rows: p(f"- {r[0]}: read result {r[1]} ({r[2]}) → {r[4]} {r[3]} `{r[5]}`")
tsv("partial_read_then_write.tsv", ["session", "read_result", "read_info", "write_entry", "tool", "path"], partial_rows)

# ---------- models/providers, routing ----------
h("Models and providers per assistant message (item g)")
mc = collections.Counter(); ids = []
for code, (s, rows) in data.items():
    for e in rows:
        if e.get("type") == "model_change": p(f"- {e['_id']} model_change → {e.get('provider')}/{e.get('modelId')} at {e.get('timestamp')}")
        if e.get("type") == "message" and e["message"].get("role") == "assistant":
            m = e["message"]; mc[(code[0], m.get("provider"), m.get("model"), m.get("api"))] += 1
            ids.append((e["_id"], m.get("responseId"), m.get("model"), m.get("stopReason"), m.get("durationMs")))
for k, v in sorted(mc.items()): p(f"- {'lead' if k[0]=='L' else k[0]+'*'}: {k[1]}/{k[2]} via {k[3]}: {v} messages")
p("The log records only the OpenRouter model id, not the upstream provider. `response_ids.tsv` lists each OpenRouter generation id; "
  "OpenRouter's /api/v1/generation endpoint can resolve each to its upstream provider.")
tsv("response_ids.tsv", ["entry", "responseId", "model", "stopReason", "durationMs"], ids)
stops = collections.Counter(r[3] for r in ids); p("Stop reasons: " + ", ".join(f"{k}: {v}" for k, v in stops.items()))

# ---------- reasoning openings (restarts) ----------
h("Opening of each lead thinking block (item g: restarts / register shifts)")
orows = []
for e in data["L"][1]:
    if e.get("type") == "message" and e["message"].get("role") == "assistant":
        for c in e["message"].get("content") or []:
            if c.get("type") == "thinking" and c.get("thinking"):
                t = c["thinking"]
                orows.append((e["_id"], len(t), t[:160], t[-80:]))
tsv("thinking_openings.tsv", ["entry", "chars", "first160", "last80"], orows)
restate = [r for r in orows if re.match(r"\s*(The user|We need to|We are|I need to|Okay, (so )?the user|The task|Let me (re)?state)", r[2], re.I)]
p(f"{len(orows)} thinking blocks in the lead; {len(restate)} open with a task-framing phrase (The user / We need to / We are / I need to / The task). "
  "Cut-off endings (last char a letter, no punctuation): " + str(sum(1 for r in orows if re.search(r"[A-Za-z]$", r[3]))) + ". See `thinking_openings.tsv`.")

# ---------- harness-injected messages ----------
h("Harness-injected messages in the lead (shown to the agent as conversation turns)")
for e in data["L"][1]:
    if e.get("type") == "custom_message":
        p(f"- {e['_id']} {e.get('customType')} display={e.get('display')}: {text_of(e.get('content')).strip().split(chr(10))[0][:120]}")

# ---------- upstream providers (if providers.py has run) ----------
if os.path.exists(f"{out}/providers.tsv"):
    h("Upstream provider per assistant message (OpenRouter generation records, via providers.py)")
    prow = [l.rstrip("\n").split("\t") for l in open(f"{out}/providers.tsv")][1:]
    runs = []
    for r in prow:
        sess = r[0].split("-")[0] if "-" in r[0] else "L"
        if runs and runs[-1][0] == sess and runs[-1][1] == r[2]: runs[-1][3] = r[0]; runs[-1][4] += 1
        else: runs.append([sess, r[2], r[0], r[0], 1])
    for sess, prov, a, b, n in runs: p(f"- {sess}: **{prov}** for {n} message(s), {a} → {b}")
    p(f"\nSum of provider-reported cost over all {len(prow)} generations: **${sum(float(r[4] or 0) for r in prow):.4f}**. "
      "Model id reported by OpenRouter for all: " + ", ".join(sorted({r[3] for r in prow})))

open(f"{out}/counts.md", "w").write("# Deterministic counts\n\nGenerated by `counts.py`; entry ids match `corpus/`.\n" + "\n".join(R) + "\n")
print("\n".join(R))
