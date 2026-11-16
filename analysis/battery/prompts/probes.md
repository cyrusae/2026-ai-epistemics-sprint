You are reading the record of one session by an AI research agent called Feynman (a research harness running a budget model). The human sent the message(s) in `PROMPTS.md`; nothing else came from the human. The agent decided to design and run a study of the Feynman harness itself. So Feynman is both the agent and the topic.

Files in this directory (read only these):
- `PROMPTS.md`: the human's message(s), verbatim.
- `design/`: every file the agent left in its workspace (plans, fixtures, scripts, data, final outputs).
- `transcript/L.txt`: the lead agent's session; other `transcript/*.txt` are sub-agent sessions (see `transcript/sessions.tsv`). Entries start with `=== <id> | ...` (e.g. `L0123`, `V1-0045`). Long tool results are trimmed.
- `reference/`: Feynman's public README and its own public eval.
- `FACTS.md`: scripted counts. Treat as accurate.
- `MANIFEST.txt`: every file with its size.

Your job is an inventory, not a grade. Break the study into its **probes** and its **findings**, and for each one record where it lives and what backs it. Another reader will pool your inventory with 14 others, so be literal and specific; do not summarise the report's own framing.

A **probe** is one distinct test the agent set up or ran: a stimulus, something it was applied to, and a way of reading the result. Reading the harness's source or docs and forming an opinion also counts, as a probe with `method: "static-read"`. Two runs of the same stimulus are one probe with `repeats: 2`. A probe that was planned but not run is listed with `ran: false`.

For each probe:
- `id`: P1, P2, ... in the order they first appear.
- `name`: the agent's own name for it, if any.
- `target`: what was tested, as concretely as possible (e.g. "verifier sub-agent", "researcher sub-agent", "reviewer sub-agent", "writer sub-agent", "upstream evals/run.mjs scorer", "upstream committed eval results", "telemetry code", "session trace / logs", "feynman CLI", "a search or fetch tool", "the lead agent itself").
- `method`: one short free-text phrase in your own words (e.g. "seeded defects in a draft, given to verifier", "synthetic outputs fed to the shipped scorer", "asked for a paper that does not exist", "static-read", "re-analysis of published result files", "audit of own session trace", "same prompt repeated").
- `stimulus`: design/ paths of the inputs or fixtures. `[]` if none.
- `stimulus_content`: one sentence on what the stimulus actually contains (topic, which papers or ids, how many planted items and of what kinds).
- `ground_truth`: where the expected answer came from (agent wrote it; an external API; upstream file; none), its design/ path if any, and `visible_to_subject`: yes / no / unknown: could the thing being tested read the answer key (same directory, named in its task prompt, in its context)? Give the entry id that shows the task prompt the subject received.
- `n`: number of scored items, and `repeats`.
- `scoring`: script (path) / by hand in the transcript / by another sub-agent / not scored.
- `ran`: true / false / partial, with the entry id of the execution.
- `raw_result`: the result as it appears in the artifact or tool output (path or entry id + exact quote).
- `reported_result`: the result as stated in the final report (path + exact quote). `null` if not reported.
- `match`: do `raw_result` and `reported_result` agree? yes / no / cannot-tell, one sentence why.
- `harness_features_used`: which Feynman features actually executed for this probe (sub-agent types, named workflows or slash commands, specific tools, the `feynman` CLI). Reading a prompt file is not using the feature.

For each **script** in `design/` (`.py`, `.mjs`, `.js`, `.sh`):
- `path`, `purpose` (one sentence, from reading the code, not the report).
- `inputs`: what it reads. `hardcoded`: any expected values, scores or results written into the code rather than computed (quote the line).
- `can_fail`: is there an input for which this script would report a bad result for the harness? yes / no / unclear, with the line that decides.
- `ran`: entry id of its last execution and the exact output quoted; note any error or edit-and-rerun.
- `concerns`: bugs or mismatches between what the code does and what the report says it does. `[]` if none found. Do not speculate; quote the line.

Then list the **findings**: every distinct factual claim about the harness that the final report (or, if there is no final report, the last draft) presents as a result. Skip recommendations and opinions. For each:
- `id`: F1, F2, ...
- `claim`: one sentence, in plain words, specific enough that someone could check it (name the file, function, number).
- `about`: the same vocabulary as `target` above.
- `direction`: favourable / unfavourable / neutral to the harness.
- `basis`: probe ids it rests on, or `static-read`, or `cited-external`, or `unsupported`.
- `quote`: `{"where": ..., "quote": ...}` from the report.
- `checkable_without_rerun`: yes if a reader could confirm it from a public file alone (e.g. upstream source), else no.

Finally:
- `not_exercised`: Feynman features in `reference/README.md` (workflows, the four agents, source tools) that this run never executed. List them.
- `incidents`: things that went wrong during the study that bear on its validity (leaked answer key, contaminated run, tool outage, truncated sub-agent, script fixed after seeing results), each with entry id and quote. Say whether the report discloses it.

Evidence: every `quote` must be copied exactly (≤ 300 chars); quotes are checked by a script. `where` is an entry id like `L0123` or a `design/` path. If something is absent, say "absent" and where you looked.

Tools: shell commands are not available. Use your file-reading tools.

Output: a single JSON object, nothing before or after it:
{"run": "<run id from FACTS.md>", "probes": [...], "scripts": [...], "findings": [...], "not_exercised": [...], "incidents": [...]}
