#!/usr/bin/env python3
"""Which harness capabilities did each run actually execute? No judgement.

usage: python3 -I coverage.py derived packets
reads  derived/timeline.tsv, derived/facts.tsv, packets/<run>/MANIFEST.txt
writes derived/coverage.tsv, derived/coverage.md

Definitions
- agent columns: sub-agent sessions of that type (timeline rows kind=session, agent != lead).
- tool columns: tool calls by lead + all sub-agents.
- subagent_calls: lead calls of the `subagent` tool. wf_js: *workflow*.js files left in design/
  (the pi-subagents parallel-run script, not a slash workflow).
- nested: session .jsonl files under design/ other than a snapshot of the run's own session
  (= the agent launched separate `feynman` processes).
- template: facts.py `workflows` (file signature of a shipped slash-workflow template in work/).
"""
import csv, collections, pathlib, re, sys

derived, packets = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
AGENTS = ["researcher", "verifier", "reviewer", "writer"]
TOOLS = ["feynman_science_database_search", "web_search", "fetch_content", "get_search_content",
         "document_search", "document_parse", "bash", "read", "write", "edit", "bg_wait"]
SHORT = {"feynman_science_database_search": "sci_db", "get_search_content": "search_content",
         "fetch_content": "fetch", "document_search": "doc_search", "document_parse": "doc_parse"}

sessions = collections.defaultdict(collections.Counter)
tools = collections.defaultdict(collections.Counter)
subcalls = collections.Counter()
other_tools = collections.Counter()
for r in csv.DictReader(open(derived / "timeline.tsv"), delimiter="\t"):
    if r["kind"] == "session" and r["agent"] != "lead":
        sessions[r["run"]][r["agent"]] += 1
    elif r["kind"] == "tool":
        if r["name"] == "subagent":
            subcalls[r["run"]] += 1
        elif r["name"] in TOOLS:
            tools[r["run"]][r["name"]] += 1
        else:
            other_tools[r["name"]] += 1

facts = {r["run"]: r for r in csv.DictReader(open(derived / "facts.tsv"), delimiter="\t")}
rows = []
for run in sorted(facts):
    man = (packets / run / "MANIFEST.txt").read_text().splitlines()
    files = [l.split(None, 1)[1] for l in man if len(l.split(None, 1)) == 2]
    design = [f for f in files if f.startswith("design/")]
    wf = sum(1 for f in design if re.search(r"workflow[^/]*\.js$", f))
    nested = sum(1 for f in design if re.search(r"/sessions/[^/]+\.jsonl$", f))
    row = {"run": run}
    for a in AGENTS:
        row[a] = sessions[run][a]
    row["subagent_calls"] = subcalls[run]
    row["wf_js"] = wf
    row["nested"] = nested
    row["template"] = facts[run].get("workflows", "-")
    for t in TOOLS:
        row[SHORT.get(t, t)] = tools[run][t]
    rows.append(row)

cols = list(rows[0])
with open(derived / "coverage.tsv", "w", newline="") as f:
    w = csv.DictWriter(f, cols, delimiter="\t")
    w.writeheader()
    w.writerows(rows)

n = len(rows)
out = ["# Capability coverage per run (scripted)", "", __doc__.split("Definitions")[1].strip(), "",
       "| " + " | ".join(cols) + " |", "|" + "---|" * len(cols)]
for r in rows:
    out.append("| " + " | ".join(str(r[c]) if r[c] != 0 else "·" for c in cols) + " |")
out.append("| **runs > 0** | " + " | ".join(
    str(sum(1 for r in rows if r[c] not in (0, "-", ""))) + f"/{n}" for c in cols[1:]) + " |")
if other_tools:
    out += ["", "Other tools seen: " + ", ".join(f"{k} ({v})" for k, v in other_tools.most_common())]
(derived / "coverage.md").write_text("\n".join(out) + "\n")
print("\n".join(out))
