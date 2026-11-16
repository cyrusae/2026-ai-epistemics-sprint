# Script re-runs (2026-11-14)

Each run's `work/` was copied to a scratch dir; `/work/` and `/state/` literals in the copied scripts were
rewritten to the copy and to the run's saved `state/`. Scripts ran under `sandbox-exec` with network denied and
no writes under `/Users`, `python3 -I`. "Saved" = the output file the agent left in `work/`.

| run | script | result | note |
|---|---|---|---|
| lit-q1-255131788 | `experiments/score_redteam.py` (3 verifier outputs) | reproduces | 6/6, 6/6, 6/6; controls intact; run2 `D3_note_explains: false`. Matches report table (lines 164–166). |
| lit-q1-255131788 | `experiments/transcript_audit.py` on `session-snapshot.jsonl` | identical to saved | input is a snapshot the agent took mid-session |
| lit-q1-255131788 | `experiments/summarize_runs.py` | identical to saved | reads sub-agent transcripts in `state/` |
| lit-q1-61864417 | `experiments/feynman-harness-eval/grade.py` | partly | 6/7 offline; the 7th check (`url_health`) shells out to curl, so it needs network. Not compared with the original. |
| lit-q1-61864417 | `.../trace_audit.py` | differs, expected | saved: 220 msgs / 133 tool calls / $0.137; rerun on the finished session: 244 / 145 / $0.198. The script audited its own session while it was still running. |
| lit-q1-61864417 | `.../audit_committed_evals.py` | not run offline | needs the upstream repo; see the network section |
| lit-q1-73429090 | `experiments/feynman_eval_costs.py`, `feynman_eval_tools.py` | run | 12 children, $0.2009 (facts.py cost_children: 0.201). No saved output to diff. |
| lit-q1-73429090 | `experiments/probe5_analysis.py` | run | n=40, mean 72.07, 95% CI [69.25, 74.90]. No saved output to diff. |
| lit-q2-112133723 | `experiments/harness-session-audit/audit.py` | differs, expected | same in-flight self-audit pattern: saved 98 tool calls, finished session 103 |
| lit-q2-212622999 | `aggregate.py`, `check_evidence.py` | identical to saved | |
| lit-q2-212622999 | `official-eval-summarize.py` | run | 22 rows, 18 completed; no saved output to diff |
| lit-q2-212622999 | `verify_claims.py` | not run offline | needs the upstream repo; see the network section |
| lit-q2-576128396 | `canary/score.py cited.md` | identical to `score-hinted.json` | 6/6 |
| lit-q2-576128396 | `canary/score.py cited-blind.md` | **script says 5/6; `score-blind.json` says 6/6** | identical to `score-blind-raw.json`. D6 was changed by hand from `MISSED` to `FIXED_BY_CITATION` with a `manual_note`. The report headlines 6/6 and discloses the override under limitations (line 424). |
| lit-q2-757831095 | `check_probes_final.py` on pilot / wave 2 / wave 3 answers | reproduces | 7/7 each; saved files differ only in timestamp and path. The report says the score on the same wave-3 answers moved 5/7 → 6/7 → 7/7 as the checker was corrected (line 211); earlier checker versions (`check_probes_v1..v4.py`) lived in `/tmp` and are not preserved. |
| lit-q2-757831095 | `check_gate.py runs/p8/answer.md`, `make_fixtures.py` | reproduce | gate ok 133/133; fixtures and `ground_truth.json` regenerate byte-identical |

## Re-runs with network allowed (2026-11-14, evening)

Network on, writes still denied under `/Users`. Upstream cloned at tag v0.5.65 (`fe86f38`). Every copy of
`evals/run.mjs` the agents saved is byte-identical to upstream at v0.5.65, and that file is unchanged on upstream main.

| run | script | result | note |
|---|---|---|---|
| lit-q2-130306422 | upstream `evals/run.mjs --rescore` on `fixtures.jsonl` (f1-f8) | reproduces | 8/8 rows: every score field identical to saved |
| lit-q2-148479120 | upstream `evals/run.mjs --rescore` on `seed.jsonl` (c0-c12) | reproduces | 13/13 rows identical; summary row 88% valid / 63% title / 85% recall |
| lit-q2-212622999 | upstream `evals/run.mjs --rescore` on `probes/eval-scorer-blindspot/row.jsonl` | reproduces | 1/1 row identical (false claim, valid citation: scores 100%) |
| lit-q1-61864417 | `audit_committed_evals.py` on upstream `evals/results/` | identical to saved | |
| lit-q1-61864417 | `grade.py` on verifier run1, run2 | 7/7 and 7/7 | `url_health` passes with network. One of the three URLs returns HTTP 403 and still counts as healthy. |
| lit-q2-212622999 | `verify_claims.py` | 19/21 at v0.5.65; saved log says 21/21 | The two failing checks are "61 test files" (60 at v0.5.65) and "349 test declarations" (345). Upstream main has 61 files. The report says it read the repo at `1174429` (package 0.5.69), so the agent's numbers describe main, not the installed 0.5.65. Not an error in the script; a version the reader has to keep in mind. |
| lit-q2-1666411819 | `eval-scorer-probe.mjs`, `score-verifier-output.mjs` | **inconclusive** (tried 3 times) | The parts that need no arXiv lookup match the saved results: the DOI probe (P6), the no-identifier probes (P5, P8), the `done` probes and the summary-table probe. Every arXiv lookup made through these two scripts failed on re-run, so P1-P4 and P7 came back `0/1 checked, valid=null` instead of the saved values. The arXiv API answered a plain request at the same time, and the `--rescore` re-runs above resolved arXiv ids an hour earlier, so this looks like rate limiting on my side, not a fault in the agent's script. Side observation, from the upstream code: a failed lookup removes the citation from the denominator (`citations_checked`) without failing the row. |

## Still not re-run

- lit-q2-1848114517 `scorer-audit/rescored-rows.jsonl`: the scored workdirs were in `/tmp/fev`, not preserved. Only the saved rows exist.
- lit-q2-1848114517 `experiments/run_probe.py` launches fresh `feynman` sessions (costs money; not a re-score).
- lit-q2-130306422 `make_fixtures.py`, lit-q2-148479120 `make_canaries.py`: fixture builders, not scorers.
- lit-q2-757831095 `score_control.py`: inputs were in `/tmp/eval-clean-control`.

## Runs with no scorer script

lit-q1-3168526392, lit-q1-43691719, lit-q2-394425698, lit-q2-93951025: results were read off sub-agent output by the lead agent, by hand.
