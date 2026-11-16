#!/usr/bin/env python3
"""Wall-clock timeline of every model call, tool call and sub-agent session, per run and turn.

usage: timeline.py <corpus-dir> <outdir>     (reads corpus/<run>/sessions.tsv for session files)

Writes:
  outdir/timeline.tsv   run, turn, session, agent, kind (model|tool|session), name, t0, t1, error
                        t0/t1 = seconds since that turn's human message (lead user message).
                        model: assistant message; t0 = request start (message.timestamp), t1 = t0 + durationMs.
                        tool:  toolResult; t1 = its timestamp, t0 = t1 - durationMs.
                        session: a sub-agent session, first to last entry.
  outdir/timing.tsv     per run+turn summary: wall (lead first→last entry), lead model / tool seconds,
                        sub-agent sessions, sub-agent busy seconds, peak concurrent sub-agents,
                        lead seconds waiting while sub-agents ran (bg_wait / blocking subagent calls).
"""
import json, os, sys, glob, csv, datetime, bisect

corpus, out = sys.argv[1:3]
def iso(s): return datetime.datetime.fromisoformat(s.replace("Z", "+00:00")).timestamp()

def events(path):
    for line in open(path, encoding="utf-8"):
        try: e = json.loads(line)
        except Exception: continue
        if e.get("type") != "message": continue
        yield e

rows, summ = [], []
for run in sorted(os.listdir(corpus)):
    st = os.path.join(corpus, run, "sessions.tsv")
    if not os.path.exists(st): continue
    sess = list(csv.DictReader(open(st), delimiter="\t"))
    lead = next(s for s in sess if s["code"] == "L")
    turn_starts = []
    lead_ev = list(events(lead["file"]))
    for e in lead_ev:
        if e["message"]["role"] == "user": turn_starts.append(iso(e["timestamp"]))
    def turn_of(t):
        i = bisect.bisect_right(turn_starts, t) - 1; return max(i, 0)
    for s in sess:
        evs = lead_ev if s["code"] == "L" else list(events(s["file"]))
        if not evs: continue
        if s["code"] != "L":
            a, b = iso(evs[0]["timestamp"]), iso(evs[-1]["timestamp"]); k = turn_of(a)
            rows.append([run, k + 1, s["code"], s["agent"], "session", s["agent"], a - turn_starts[k], b - turn_starts[k], ""])
        for e in evs:
            m = e["message"]
            if m["role"] == "assistant" and isinstance(m.get("timestamp"), (int, float)):
                a = m["timestamp"] / 1000; b = a + (m.get("durationMs") or 0) / 1000
                if not m.get("durationMs"): b = iso(e["timestamp"])
                k = turn_of(a)
                tools = ",".join(c.get("name", "") for c in m.get("content") or [] if isinstance(c, dict) and c.get("type") == "toolCall")
                rows.append([run, k + 1, s["code"], s["agent"], "model", tools or ("reply:" + (m.get("stopReason") or "")), a - turn_starts[k], b - turn_starts[k], m.get("stopReason") if m.get("stopReason") not in ("toolUse", "stop") else ""])
            elif m["role"] == "toolResult":
                b = iso(e["timestamp"]); a = b - (m.get("durationMs") or 0) / 1000; k = turn_of(a)
                rows.append([run, k + 1, s["code"], s["agent"], "tool", m.get("toolName", ""), a - turn_starts[k], b - turn_starts[k], "error" if m.get("isError") else ""])
    # summaries
    for k in range(len(turn_starts)):
        R = [r for r in rows if r[0] == run and r[1] == k + 1]
        L = [r for r in R if r[2] == "L"]
        S = [r for r in R if r[4] == "session"]
        wall = max((r[7] for r in L), default=0)
        pts = sorted([(r[6], 1) for r in S] + [(r[7], -1) for r in S]); cur = peak = 0
        for _, d in pts: cur += d; peak = max(peak, cur)
        waits = sum(r[7] - r[6] for r in L if r[4] == "tool" and r[5] in ("bg_wait", "subagent"))
        summ.append([run, k + 1, round(wall), round(sum(r[7] - r[6] for r in L if r[4] == "model")), round(sum(r[7] - r[6] for r in L if r[4] == "tool")),
                     len(S), round(sum(r[7] - r[6] for r in S)), peak, round(waits), round(max((r[7] for r in R), default=0))])

with open(os.path.join(out, "timeline.tsv"), "w") as f:
    f.write("run\tturn\tsession\tagent\tkind\tname\tt0\tt1\tflag\n")
    for r in rows: f.write("\t".join(str(round(x, 3)) if isinstance(x, float) else str(x) for x in r) + "\n")
with open(os.path.join(out, "timing.tsv"), "w") as f:
    f.write("run\tturn\tlead_wall_s\tlead_model_s\tlead_tool_s\tsubagent_sessions\tsubagent_busy_s\tpeak_concurrent\tlead_waiting_s\tlast_activity_s\n")
    for r in summ: f.write("\t".join(map(str, r)) + "\n")
print(len(rows), "events;", len(summ), "run-turns")
