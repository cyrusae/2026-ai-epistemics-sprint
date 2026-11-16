# Scripted facts per run

No judgement involved; see facts.py for definitions. Keyword counts include false positives ("Feynman" is also the topic): read keywords.tsv.

| run | decisions | minutes | cost_lead | cost_children | files | scripts | workflows | script_runs | feynman_invocations | feynman_source_fetches | evals_fetches | kw_self-feynman | kw_as-an-ai | kw_user-wants |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| lit-q1-255131788 | attempted | 16 | 0.124 | 0.155 | 26 | 3 | - | 6 | 0 | 38 | 11 | 2 | 0 | 7 |
| lit-q1-3168526392 | attempted | 9 | 0.142 | 0.074 | 24 | 1 | - | 0 | 0 | 26 | 19 | 0 | 2 | 12 |
| lit-q1-43691719 | attempted | 8 | 0.047 | 0.015 | 6 | 0 | - | 0 | 1 | 24 | 10 | 0 | 1 | 8 |
| lit-q1-61864417 | attempted | 25 | 0.16 | 0.038 | 13 | 3 | - | 9 | 0 | 28 | 4 | 0 | 3 | 7 |
| lit-q1-73429090 | not-attempted,- | 1,11 | 0.225 | 0.201 | 35 | 3 | - | 10 | 0 | 0 | 0 | 3 | 1 | 12 |
| lit-q2-112133723 | attempted | 6 | 0.105 | 0.119 | 30 | 1 | audit | 6 | 0 | 4 | 0 | 0 | 0 | 4 |
| lit-q2-130306422 | no-opening | 17 | 0.192 | 0.12 | 30 | 1 | - | 12 | 2 | 34 | 18 | 0 | 0 | 10 |
| lit-q2-148479120 | attempted | 6 | 0.116 | 0.008 | 59 | 3 | - | 3 | 0 | 17 | 12 | 1 | 0 | 9 |
| lit-q2-1666411819 | attempted | 22 | 0.167 | 0.175 | 15 | 3 | - | 5 | 0 | 26 | 14 | 0 | 1 | 12 |
| lit-q2-1848114517 | attempted | 6 | 0.062 | 0.0 | 54 | 2 | deepresearch | 4 | 0 | 18 | 12 | 0 | 0 | 4 |
| lit-q2-212622999 | attempted | 21 | 0.137 | 0.141 | 63 | 5 | - | 23 | 1 | 45 | 5 | 0 | 5 | 11 |
| lit-q2-394425698 | attempted | 5 | 0.061 | 0.04 | 15 | 0 | - | 0 | 0 | 0 | 0 | 2 | 0 | 1 |
| lit-q2-576128396 | attempted | 4 | 0.079 | 0.026 | 16 | 1 | - | 5 | 0 | 2 | 0 | 1 | 2 | 8 |
| lit-q2-757831095 | attempted | 15 | 0.207 | 0.202 | 69 | 6 | - | 25 | 0 | 43 | 21 | 1 | 0 | 3 |
| lit-q2-93951025 | attempted | 8 | 0.066 | 0.051 | 9 | 0 | - | 0 | 0 | 22 | 9 | 0 | 0 | 7 |

## lit-q1-255131788

- **turns**: 1
- **exits**: 0
- **minutes**: 16
- **decisions**: attempted
- **prompts**: p1.md
- **cost_lead**: 0.124
- **cost_children**: 0.155
- **lead_msgs**: 71
- **lead_tool_calls**: 106
- **lead_tool_errors**: 3
- **subagent_calls**: 4
- **children**: 4
- **files**: 26
- **scripts**: 3
- **data**: 4
- **outputs**: 2
- **workflows**: -
- **script_runs**: 6
- **feynman_invocations**: 0
- **feynman_source_fetches**: 38
- **evals_fetches**: 11
- **kw_self-feynman**: 2
- **kw_as-an-ai**: 0
- **kw_user-wants**: 7
- **kw_user-other**: 2
- **kw_self-model**: 4

Files in work/ (excl. venv/.git):
  - `CHANGELOG.md` (2274 B, other)
  - `experiments/redteam-runs.json` (2152 B, data)
  - `experiments/reviewer-probe/cited.md` (3660 B, other)
  - `experiments/reviewer-probe/research-notes.md` (1111 B, other)
  - `experiments/reviewer-probe/review.md` (24039 B, other)
  - `experiments/reviewer-run.json` (610 B, data)
  - `experiments/score_redteam.py` (4252 B, script)
  - `experiments/session-snapshot.jsonl` (539404 B, data)
  - `experiments/summarize_runs.py` (2110 B, script)
  - `experiments/transcript-audit.json` (990 B, data)
  - `experiments/transcript_audit.py` (5583 B, script)
  - `experiments/verifier-clean-run2/cited-output.md` (3660 B, other)
  - `experiments/verifier-clean-run2/draft.md` (1163 B, other)
  - `experiments/verifier-clean-run2/research-notes.md` (1111 B, other)
  - `experiments/verifier-clean-run2/verification-log.md` (7746 B, other)
  - `experiments/verifier-clean/cited-output.md` (2898 B, other)
  - `experiments/verifier-clean/draft.md` (1163 B, other)
  - `experiments/verifier-clean/research-notes.md` (1111 B, other)
  - `experiments/verifier-clean/verification-log.md` (9555 B, other)
  - `experiments/verifier-redteam/cited-output.md` (4843 B, other)
  - `experiments/verifier-redteam/draft.md` (1163 B, other)
  - `experiments/verifier-redteam/research-notes.md` (1111 B, other)
  - `experiments/verifier-redteam/verification-log.md` (6461 B, other)
  - `notes/verifier-redteam-ground-truth.md` (1337 B, other)
  - `outputs/.plans/feynman-eval-case-study.md` (1817 B, plan)
  - `outputs/feynman-eval-case-study.md` (41274 B, output)

## lit-q1-3168526392

- **turns**: 1
- **exits**: 0
- **minutes**: 9
- **decisions**: attempted
- **prompts**: p1.md
- **cost_lead**: 0.142
- **cost_children**: 0.074
- **lead_msgs**: 66
- **lead_tool_calls**: 107
- **lead_tool_errors**: 2
- **subagent_calls**: 9
- **children**: 4
- **files**: 24
- **scripts**: 1
- **data**: 3
- **outputs**: 3
- **workflows**: -
- **script_runs**: 0
- **feynman_invocations**: 0
- **feynman_source_fetches**: 26
- **evals_fetches**: 19
- **kw_self-feynman**: 0
- **kw_as-an-ai**: 2
- **kw_user-wants**: 12
- **kw_user-other**: 4
- **kw_self-model**: 4

Files in work/ (excl. venv/.git):
  - `CHANGELOG.md` (1157 B, other)
  - `experiments/feynman-eval-case-study/fixtures/draft-hard.md` (814 B, other)
  - `experiments/feynman-eval-case-study/fixtures/draft-with-seeded-defects.md` (1200 B, other)
  - `experiments/feynman-eval-case-study/fixtures/mini-eval-paper.md` (1024 B, other)
  - `experiments/feynman-eval-case-study/fixtures/research-notes-hard.md` (1247 B, other)
  - `experiments/feynman-eval-case-study/fixtures/research-notes.md` (1783 B, other)
  - `experiments/feynman-eval-case-study/probe-outputs.md` (6395 B, other)
  - `experiments/feynman-eval-case-study/protocol.md` (3773 B, other)
  - `experiments/feynman-eval-case-study/researcher-nonexistent-output.md` (13045 B, other)
  - `experiments/feynman-eval-case-study/reviewer-eval-output.md` (18872 B, other)
  - `experiments/feynman-eval-case-study/upstream/README.md` (5020 B, other)
  - `experiments/feynman-eval-case-study/upstream/claude-opus-q01-q10.jsonl` (1768 B, data)
  - `experiments/feynman-eval-case-study/upstream/crossref-10.65215-r5bs2d54.json` (4030 B, data)
  - `experiments/feynman-eval-case-study/upstream/post-wait-gpt.md` (667 B, other)
  - `experiments/feynman-eval-case-study/upstream/pre-wait-gpt.md` (876 B, other)
  - `experiments/feynman-eval-case-study/upstream/questions.jsonl` (5353 B, data)
  - `experiments/feynman-eval-case-study/upstream/run.mjs` (15151 B, script)
  - `experiments/feynman-eval-case-study/verifier-hard-log.md` (7278 B, other)
  - `experiments/feynman-eval-case-study/verifier-hard-output.md` (2357 B, other)
  - `experiments/feynman-eval-case-study/verifier-log.md` (6026 B, other)
  - `experiments/feynman-eval-case-study/verifier-output.md` (3760 B, other)
  - `outputs/.plans/feynman-harness-eval-quality.md` (1604 B, plan)
  - `outputs/feynman-harness-eval-quality-case-study.md` (30671 B, output)
  - `outputs/feynman-harness-eval-quality-case-study.provenance.md` (4377 B, output)

## lit-q1-43691719

- **turns**: 1
- **exits**: 0
- **minutes**: 8
- **decisions**: attempted
- **prompts**: p1.md
- **cost_lead**: 0.047
- **cost_children**: 0.015
- **lead_msgs**: 38
- **lead_tool_calls**: 61
- **lead_tool_errors**: 0
- **subagent_calls**: 1
- **children**: 1
- **files**: 6
- **scripts**: 0
- **data**: 0
- **outputs**: 1
- **workflows**: -
- **script_runs**: 0
- **feynman_invocations**: 1
- **feynman_source_fetches**: 24
- **evals_fetches**: 10
- **kw_self-feynman**: 0
- **kw_as-an-ai**: 1
- **kw_user-wants**: 8
- **kw_user-other**: 2
- **kw_self-model**: 2

Files in work/ (excl. venv/.git):
  - `experiments/verifier-probe/cited.md` (1664 B, other)
  - `experiments/verifier-probe/draft.md` (394 B, other)
  - `experiments/verifier-probe/research.md` (345 B, other)
  - `experiments/verifier-probe/verification-log.md` (3650 B, other)
  - `notes/feynman-harness-eval-quality-evidence.md` (7150 B, other)
  - `outputs/feynman-harness-eval-quality-case-study.md` (31494 B, output)

## lit-q1-61864417

- **turns**: 1
- **exits**: 0
- **minutes**: 25
- **decisions**: attempted
- **prompts**: p1.md
- **cost_lead**: 0.16
- **cost_children**: 0.038
- **lead_msgs**: 58
- **lead_tool_calls**: 99
- **lead_tool_errors**: 1
- **subagent_calls**: 4
- **children**: 3
- **files**: 13
- **scripts**: 3
- **data**: 3
- **outputs**: 5
- **workflows**: -
- **script_runs**: 9
- **feynman_invocations**: 0
- **feynman_source_fetches**: 28
- **evals_fetches**: 4
- **kw_self-feynman**: 0
- **kw_as-an-ai**: 3
- **kw_user-wants**: 7
- **kw_user-other**: 6
- **kw_self-model**: 10

Files in work/ (excl. venv/.git):
  - `experiments/feynman-harness-eval/audit_committed_evals.py` (2293 B, script)
  - `experiments/feynman-harness-eval/committed-evals-audit.json` (1309 B, data)
  - `experiments/feynman-harness-eval/fixtures/research-notes.md` (2242 B, other)
  - `experiments/feynman-harness-eval/grade.py` (5192 B, script)
  - `experiments/feynman-harness-eval/trace-audit.json` (4441 B, data)
  - `experiments/feynman-harness-eval/trace_audit.py` (4507 B, script)
  - `notes/feynman-harness-eval-paper-abstracts.txt` (6636 B, data)
  - `outputs/.drafts/harness-eval-false-premise.md` (9717 B, draft)
  - `outputs/.drafts/harness-eval-fixture.md` (1229 B, draft)
  - `outputs/.drafts/harness-eval-verifier-run1.md` (3008 B, draft)
  - `outputs/.drafts/harness-eval-verifier-run2.md` (2382 B, draft)
  - `outputs/.plans/feynman-harness-eval.md` (3756 B, plan)
  - `papers/feynman-harness-eval-case-study.md` (39384 B, other)

## lit-q1-73429090

- **turns**: 2
- **exits**: 0,0
- **minutes**: 1,11
- **decisions**: not-attempted,-
- **prompts**: p1.md>p2.md
- **cost_lead**: 0.225
- **cost_children**: 0.201
- **lead_msgs**: 86
- **lead_tool_calls**: 116
- **lead_tool_errors**: 3
- **subagent_calls**: 5
- **children**: 12
- **files**: 35
- **scripts**: 3
- **data**: 1
- **outputs**: 31
- **workflows**: -
- **script_runs**: 10
- **feynman_invocations**: 0
- **feynman_source_fetches**: 0
- **evals_fetches**: 0
- **kw_self-feynman**: 3
- **kw_as-an-ai**: 1
- **kw_user-wants**: 12
- **kw_user-other**: 11
- **kw_self-model**: 2

Files in work/ (excl. venv/.git):
  - `experiments/feynman_eval_costs.py` (2337 B, script)
  - `experiments/feynman_eval_tools.py` (1156 B, script)
  - `experiments/probe5_analysis.py` (4694 B, script)
  - `experiments/probe5_scores.csv` (395 B, data)
  - `outputs/.plans/feynman-harness-eval-workflow-b.js` (1134 B, plan)
  - `outputs/.plans/feynman-harness-eval-workflow.js` (2432 B, plan)
  - `outputs/.plans/feynman-harness-eval.md` (7502 B, plan)
  - `outputs/feynman-harness-eval-groundtruth.md` (8979 B, output)
  - `outputs/feynman-harness-eval-probes/b.md` (21586 B, output)
  - `outputs/feynman-harness-eval-probes/brief-B.md` (545 B, output)
  - `outputs/feynman-harness-eval-probes/brief-p1.md` (484 B, output)
  - `outputs/feynman-harness-eval-probes/brief-p1b.md` (484 B, output)
  - `outputs/feynman-harness-eval-probes/brief-p2.md` (425 B, output)
  - `outputs/feynman-harness-eval-probes/brief-p3.md` (348 B, output)
  - `outputs/feynman-harness-eval-probes/brief-p4.md` (173 B, output)
  - `outputs/feynman-harness-eval-probes/brief-p5.md` (343 B, output)
  - `outputs/feynman-harness-eval-probes/brief-p6.md` (570 B, output)
  - `outputs/feynman-harness-eval-probes/p1.md` (9494 B, output)
  - `outputs/feynman-harness-eval-probes/p1b.md` (14824 B, output)
  - `outputs/feynman-harness-eval-probes/p2.md` (10536 B, output)
  - `outputs/feynman-harness-eval-probes/p3.md` (4889 B, output)
  - `outputs/feynman-harness-eval-probes/p4.md` (8326 B, output)
  - `outputs/feynman-harness-eval-probes/p5.md` (3211 B, output)
  - `outputs/feynman-harness-eval-probes/p6.md` (2703 B, output)
  - `outputs/feynman-harness-eval-probes/probe6-draft.md` (702 B, output)
  - `outputs/feynman-harness-eval-probes/probe6-research.md` (903 B, output)
  - `outputs/feynman-harness-eval.md` (32908 B, output)
  - `outputs/rs-2026-11/q1-answer.md` (7394 B, output)
  - `outputs/rs-2026-11/q1.md` (249 B, output)
  - `outputs/rs-2026-11/q2-answer.md` (7803 B, output)
  - `outputs/rs-2026-11/q2.md` (160 B, output)
  - `outputs/rs-2026-11/q3-answer.md` (11467 B, output)
  - `outputs/rs-2026-11/q3.md` (294 B, output)
  - `outputs/rs-2026-11/q4-answer.md` (3376 B, output)
  - `outputs/rs-2026-11/q4.md` (227 B, output)

## lit-q2-112133723

- **turns**: 1
- **exits**: 0
- **minutes**: 6
- **decisions**: attempted
- **prompts**: p1.md
- **cost_lead**: 0.105
- **cost_children**: 0.119
- **lead_msgs**: 75
- **lead_tool_calls**: 103
- **lead_tool_errors**: 8
- **subagent_calls**: 8
- **children**: 7
- **files**: 30
- **scripts**: 1
- **data**: 3
- **outputs**: 4
- **workflows**: audit
- **script_runs**: 6
- **feynman_invocations**: 0
- **feynman_source_fetches**: 4
- **evals_fetches**: 0
- **kw_self-feynman**: 0
- **kw_as-an-ai**: 0
- **kw_user-wants**: 4
- **kw_user-other**: 2
- **kw_self-model**: 5

Files in work/ (excl. venv/.git):
  - `experiments/harness-session-audit/audit.py` (4514 B, script)
  - `experiments/harness-session-audit/final.json` (1065 B, data)
  - `experiments/harness-session-audit/prelim.json` (794 B, data)
  - `experiments/harness-verifier-eval/GROUND-TRUTH.md` (3504 B, other)
  - `experiments/harness-verifier-eval/inputs/draft-control.md` (958 B, other)
  - `experiments/harness-verifier-eval/inputs/draft-treatment.md` (1011 B, other)
  - `experiments/harness-verifier-eval/inputs/draft-unsupported.md` (1087 B, other)
  - `experiments/harness-verifier-eval/inputs/research-notes.md` (2541 B, other)
  - `experiments/harness-verifier-eval/logs/abs-2405.14782.html` (45509 B, other)
  - `experiments/harness-verifier-eval/logs/abs-2411.00640.html` (39055 B, other)
  - `experiments/harness-verifier-eval/logs/arxiv-abs.html` (43071 B, other)
  - `experiments/harness-verifier-eval/logs/arxiv-html.html` (188707 B, other)
  - `experiments/harness-verifier-eval/logs/crossref-query.json` (4491 B, data)
  - `experiments/harness-verifier-eval/outputs/control-audit.md` (8272 B, other)
  - `experiments/harness-verifier-eval/outputs/control-cited.md` (2036 B, other)
  - `experiments/harness-verifier-eval/outputs/default-contract-cited.md` (3236 B, other)
  - `experiments/harness-verifier-eval/outputs/noaudit-cited.md` (1682 B, other)
  - `experiments/harness-verifier-eval/outputs/notesfree-audit.md` (7892 B, other)
  - `experiments/harness-verifier-eval/outputs/notesfree-cited.md` (2582 B, other)
  - `experiments/harness-verifier-eval/outputs/treatment-audit.md` (8902 B, other)
  - `experiments/harness-verifier-eval/outputs/treatment-cited.md` (3009 B, other)
  - `experiments/harness-verifier-eval/outputs/unsupported-audit.md` (8970 B, other)
  - `experiments/harness-verifier-eval/outputs/unsupported-cited.md` (3105 B, other)
  - `experiments/harness-verifier-eval/outputs/unsupported-default-cited.md` (2801 B, other)
  - `experiments/harness-verifier-eval/scorecard.md` (4324 B, other)
  - `notes/feynman-harness-static-analysis.md` (4056 B, other)
  - `outputs/.plans/feynman-harness-eval.md` (2290 B, plan)
  - `outputs/.plans/harness-verifier-eval-workflow.js` (1916 B, plan)
  - `outputs/feynman-harness-eval-case-study.md` (25527 B, output)
  - `outputs/feynman-harness-eval-case-study.provenance.md` (5107 B, output)

## lit-q2-130306422

- **turns**: 1
- **exits**: 0
- **minutes**: 17
- **decisions**: no-opening
- **prompts**: p1.md
- **cost_lead**: 0.192
- **cost_children**: 0.12
- **lead_msgs**: 91
- **lead_tool_calls**: 110
- **lead_tool_errors**: 0
- **subagent_calls**: 2
- **children**: 2
- **files**: 30
- **scripts**: 1
- **data**: 7
- **outputs**: 2
- **workflows**: -
- **script_runs**: 12
- **feynman_invocations**: 2
- **feynman_source_fetches**: 34
- **evals_fetches**: 18
- **kw_self-feynman**: 0
- **kw_as-an-ai**: 0
- **kw_user-wants**: 10
- **kw_user-other**: 2
- **kw_self-model**: 24

Files in work/ (excl. venv/.git):
  - `experiments/feynman-eval-audit/README.md` (3054 B, other)
  - `experiments/feynman-eval-audit/fixtures.jsonl` (4094 B, data)
  - `experiments/feynman-eval-audit/fixtures.md` (580 B, other)
  - `experiments/feynman-eval-audit/git-stats.txt` (944 B, data)
  - `experiments/feynman-eval-audit/make_fixtures.py` (3457 B, script)
  - `experiments/feynman-eval-audit/release-claim-check.txt` (643 B, data)
  - `experiments/feynman-eval-audit/rescore.log` (635 B, data)
  - `experiments/feynman-eval-audit/verification.txt` (1072 B, data)
  - `experiments/feynman-eval-audit/work/f1-control/ws/outputs/test-time-compute.md` (241 B, other)
  - `experiments/feynman-eval-audit/work/f1-control/ws/outputs/test-time-compute.provenance.md` (50 B, other)
  - `experiments/feynman-eval-audit/work/f2-fake-id/ws/outputs/test-time-compute.md` (241 B, other)
  - `experiments/feynman-eval-audit/work/f2-fake-id/ws/outputs/test-time-compute.provenance.md` (50 B, other)
  - `experiments/feynman-eval-audit/work/f3-irrelevant/ws/outputs/test-time-compute.md` (175 B, other)
  - `experiments/feynman-eval-audit/work/f3-irrelevant/ws/outputs/test-time-compute.provenance.md` (50 B, other)
  - `experiments/feynman-eval-audit/work/f4-absurd-number/ws/outputs/test-time-compute.md` (200 B, other)
  - `experiments/feynman-eval-audit/work/f4-absurd-number/ws/outputs/test-time-compute.provenance.md` (50 B, other)
  - `experiments/feynman-eval-audit/work/f5-wrong-title/ws/outputs/test-time-compute.md` (169 B, other)
  - `experiments/feynman-eval-audit/work/f5-wrong-title/ws/outputs/test-time-compute.provenance.md` (50 B, other)
  - `experiments/feynman-eval-audit/work/f6-no-provenance/ws/outputs/test-time-compute.md` (221 B, other)
  - `experiments/feynman-eval-audit/work/f7-bare-id/ws/outputs/test-time-compute.md` (74 B, other)
  - `experiments/feynman-eval-audit/work/f7-bare-id/ws/outputs/test-time-compute.provenance.md` (50 B, other)
  - `experiments/feynman-eval-audit/work/f8-rejected/ws/outputs/test-time-compute.md` (242 B, other)
  - `experiments/feynman-eval-audit/work/f8-rejected/ws/outputs/test-time-compute.provenance.md` (50 B, other)
  - `experiments/feynman-harness-probe/outputs/probe-artifact.md` (17 B, other)
  - `experiments/feynman-harness-probe/probe-result.txt` (372 B, data)
  - `experiments/feynman-harness-probe/probe.log` (5 B, data)
  - `notes/feynman-eval-quality-review-2.md` (13486 B, other)
  - `notes/feynman-eval-quality-review.md` (17239 B, other)
  - `outputs/feynman-harness-eval-quality.md` (35803 B, output)
  - `outputs/feynman-harness-eval-quality.provenance.md` (4179 B, output)

## lit-q2-148479120

- **turns**: 1
- **exits**: 0
- **minutes**: 6
- **decisions**: attempted
- **prompts**: p1.md
- **cost_lead**: 0.116
- **cost_children**: 0.008
- **lead_msgs**: 35
- **lead_tool_calls**: 50
- **lead_tool_errors**: 1
- **subagent_calls**: 1
- **children**: 1
- **files**: 59
- **scripts**: 3
- **data**: 14
- **outputs**: 2
- **workflows**: -
- **script_runs**: 3
- **feynman_invocations**: 0
- **feynman_source_fetches**: 17
- **evals_fetches**: 12
- **kw_self-feynman**: 1
- **kw_as-an-ai**: 0
- **kw_user-wants**: 9
- **kw_user-other**: 2
- **kw_self-model**: 2

Files in work/ (excl. venv/.git):
  - `experiments/feynman-eval-audit/canary-key.json` (800 B, data)
  - `experiments/feynman-eval-audit/evals/questions.jsonl` (5353 B, data)
  - `experiments/feynman-eval-audit/evals/run.mjs` (15151 B, script)
  - `experiments/feynman-eval-audit/make_canaries.py` (4796 B, script)
  - `experiments/feynman-eval-audit/rescore-stderr.txt` (0 B, data)
  - `experiments/feynman-eval-audit/rescore-stdout.txt` (792 B, data)
  - `experiments/feynman-eval-audit/rescore-stdout2.txt` (845 B, data)
  - `experiments/feynman-eval-audit/seed-input.jsonl` (2083 B, data)
  - `experiments/feynman-eval-audit/seed.jsonl` (7079 B, data)
  - `experiments/feynman-eval-audit/seed.md` (827 B, other)
  - `experiments/feynman-eval-audit/work/c0-correct/ws/outputs/test-time-compute-scaling.md` (214 B, other)
  - `experiments/feynman-eval-audit/work/c0-correct/ws/outputs/test-time-compute-scaling.provenance.md` (35 B, other)
  - `experiments/feynman-eval-audit/work/c1-wrong-title-real-id/ws/outputs/test-time-compute-scaling.md` (146 B, other)
  - `experiments/feynman-eval-audit/work/c1-wrong-title-real-id/ws/outputs/test-time-compute-scaling.provenance.md` (35 B, other)
  - `experiments/feynman-eval-audit/work/c10-doi-wrong-title/ws/outputs/crispr-base-editing.md` (142 B, other)
  - `experiments/feynman-eval-audit/work/c10-doi-wrong-title/ws/outputs/crispr-base-editing.provenance.md` (35 B, other)
  - `experiments/feynman-eval-audit/work/c11-datacite-doi/ws/outputs/crispr-base-editing.md` (107 B, other)
  - `experiments/feynman-eval-audit/work/c11-datacite-doi/ws/outputs/crispr-base-editing.provenance.md` (35 B, other)
  - `experiments/feynman-eval-audit/work/c12-verifier-output/ws/outputs/test-time-compute-scaling.md` (4297 B, other)
  - `experiments/feynman-eval-audit/work/c12-verifier-output/ws/outputs/test-time-compute-scaling.provenance.md` (35 B, other)
  - `experiments/feynman-eval-audit/work/c2-fabricated-id/ws/outputs/test-time-compute-scaling.md` (153 B, other)
  - `experiments/feynman-eval-audit/work/c2-fabricated-id/ws/outputs/test-time-compute-scaling.provenance.md` (35 B, other)
  - `experiments/feynman-eval-audit/work/c3-right-paper-false-claim/ws/outputs/test-time-compute-scaling.md` (233 B, other)
  - `experiments/feynman-eval-audit/work/c3-right-paper-false-claim/ws/outputs/test-time-compute-scaling.provenance.md` (35 B, other)
  - `experiments/feynman-eval-audit/work/c4-uncited-number/ws/outputs/test-time-compute-scaling.md` (188 B, other)
  - `experiments/feynman-eval-audit/work/c4-uncited-number/ws/outputs/test-time-compute-scaling.provenance.md` (35 B, other)
  - `experiments/feynman-eval-audit/work/c5-web-only/ws/outputs/test-time-compute-scaling.md` (202 B, other)
  - `experiments/feynman-eval-audit/work/c5-web-only/ws/outputs/test-time-compute-scaling.provenance.md` (35 B, other)
  - `experiments/feynman-eval-audit/work/c6-pmid-only/ws/outputs/crispr-base-editing.md` (143 B, other)
  - `experiments/feynman-eval-audit/work/c6-pmid-only/ws/outputs/crispr-base-editing.provenance.md` (35 B, other)
  - `experiments/feynman-eval-audit/work/c6-pmid-only/ws/outputs/test-time-compute-scaling.md` (99 B, other)
  - `experiments/feynman-eval-audit/work/c6-pmid-only/ws/outputs/test-time-compute-scaling.provenance.md` (35 B, other)
  - `experiments/feynman-eval-audit/work/c7-generic-citation-line/ws/outputs/test-time-compute-scaling.md` (68 B, other)
  - `experiments/feynman-eval-audit/work/c7-generic-citation-line/ws/outputs/test-time-compute-scaling.provenance.md` (35 B, other)
  - `experiments/feynman-eval-audit/work/c8-reference-only-contradiction/ws/outputs/test-time-compute-scaling.md` (237 B, other)
  - `experiments/feynman-eval-audit/work/c8-reference-only-contradiction/ws/outputs/test-time-compute-scaling.provenance.md` (35 B, other)
  - `experiments/feynman-eval-audit/work/c9-doi-correct/ws/outputs/crispr-base-editing.md` (173 B, other)
  - `experiments/feynman-eval-audit/work/c9-doi-correct/ws/outputs/crispr-base-editing.provenance.md` (35 B, other)
  - `experiments/feynman-verifier-canary/cited.md` (4297 B, other)
  - `experiments/feynman-verifier-canary/draft.md` (820 B, other)
  - `experiments/feynman-verifier-canary/research-notes.md` (1390 B, other)
  - `experiments/feynman-verifier-canary/verification-log.md` (4695 B, other)
  - `notes/feynman-evals/2026-09-23-lit-ferrylane-openai_claude-sonnet-5.jsonl` (2912 B, data)
  - `notes/feynman-evals/2026-09-23-lit-ferrylane-openai_claude-sonnet-5.md` (471 B, other)
  - `notes/feynman-evals/2026-09-24-lit-0.5.3-ferrylane-openai_gpt-5.6-terra.jsonl` (2578 B, data)
  - `notes/feynman-evals/2026-09-24-lit-0.5.3-ferrylane-openai_gpt-5.6-terra.md` (667 B, other)
  - `notes/feynman-evals/2026-09-24-lit-0.5.3-ferrylane_claude-opus-5-5.jsonl` (1768 B, data)
  - `notes/feynman-evals/2026-09-24-lit-0.5.3-ferrylane_claude-opus-5-5.md` (543 B, other)
  - `notes/feynman-evals/2026-09-24-lit-0.5.3-pre-wait-ferrylane-openai_gpt-5.6-terra.jsonl` (2527 B, data)
  - `notes/feynman-evals/2026-09-24-lit-0.5.3-pre-wait-ferrylane-openai_gpt-5.6-terra.md` (876 B, other)
  - `notes/feynman-evals/2026-09-24-lit-0.5.3-pre-wait-ferrylane_claude-opus-5-5.jsonl` (2442 B, data)
  - `notes/feynman-evals/2026-09-24-lit-0.5.3-pre-wait-ferrylane_claude-opus-5-5.md` (861 B, other)
  - `notes/feynman-evals/2026-09-24-lit-ferrylane-openai_gpt-5.6-terra.jsonl` (2546 B, data)
  - `notes/feynman-evals/2026-09-24-lit-ferrylane-openai_gpt-5.6-terra.md` (476 B, other)
  - `notes/feynman-evals/README.md` (5020 B, other)
  - `notes/feynman-evals/questions.jsonl` (5353 B, data)
  - `notes/feynman-evals/run.mjs` (15151 B, script)
  - `outputs/feynman-harness-eval-quality.md` (30892 B, output)
  - `outputs/feynman-harness-eval-quality.provenance.md` (5245 B, output)

## lit-q2-1666411819

- **turns**: 1
- **exits**: 0
- **minutes**: 22
- **decisions**: attempted
- **prompts**: p1.md
- **cost_lead**: 0.167
- **cost_children**: 0.175
- **lead_msgs**: 100
- **lead_tool_calls**: 134
- **lead_tool_errors**: 4
- **subagent_calls**: 17
- **children**: 6
- **files**: 15
- **scripts**: 3
- **data**: 6
- **outputs**: 5
- **workflows**: -
- **script_runs**: 5
- **feynman_invocations**: 0
- **feynman_source_fetches**: 26
- **evals_fetches**: 14
- **kw_self-feynman**: 0
- **kw_as-an-ai**: 1
- **kw_user-wants**: 12
- **kw_user-other**: 3
- **kw_self-model**: 15

Files in work/ (excl. venv/.git):
  - `experiments/.tmp-eval-scorer.generated.mjs` (15118 B, script)
  - `experiments/.tmp-verified-silent.md` (2794 B, other)
  - `experiments/eval-scorer-probe-results.json` (4408 B, data)
  - `experiments/eval-scorer-probe.log` (1219 B, data)
  - `experiments/eval-scorer-probe.mjs` (7751 B, script)
  - `experiments/eval-stats.log` (614 B, data)
  - `experiments/score-verifier-output.log` (338 B, data)
  - `experiments/score-verifier-output.mjs` (2160 B, script)
  - `experiments/verifier-output-score.json` (1044 B, data)
  - `experiments/verifier-usage.log` (131 B, data)
  - `outputs/.probes/verifier-probe-draft.md` (1600 B, output)
  - `outputs/.probes/verifier-probe-verified.md` (3695 B, output)
  - `outputs/feynman-harness-eval-quality-case-study.md` (47578 B, output)
  - `outputs/feynman-harness-eval-quality-case-study.provenance.md` (4394 B, output)
  - `outputs/feynman-harness-eval-quality-case-study.review.md` (23976 B, output)

## lit-q2-1848114517

- **turns**: 1
- **exits**: 0
- **minutes**: 6
- **decisions**: attempted
- **prompts**: p1.md
- **cost_lead**: 0.062
- **cost_children**: 0.0
- **lead_msgs**: 65
- **lead_tool_calls**: 94
- **lead_tool_errors**: 3
- **subagent_calls**: 0
- **children**: 0
- **files**: 54
- **scripts**: 2
- **data**: 37
- **outputs**: 3
- **workflows**: deepresearch
- **script_runs**: 4
- **feynman_invocations**: 0
- **feynman_source_fetches**: 18
- **evals_fetches**: 12
- **kw_self-feynman**: 0
- **kw_as-an-ai**: 0
- **kw_user-wants**: 4
- **kw_user-other**: 1
- **kw_self-model**: 4

Files in work/ (excl. venv/.git):
  - `CHANGELOG.md` (2185 B, other)
  - `experiments/README.md` (2673 B, other)
  - `experiments/probe-bg.log` (456 B, data)
  - `experiments/probe-results.json` (26086 B, data)
  - `experiments/run_probe.py` (7526 B, script)
  - `experiments/runs/det-1/meta.json` (1893 B, data)
  - `experiments/runs/det-1/sessions/2026-11-14T08-57-49-244Z_01a1d946-f7bb-70cb-a858-28f4f33689af.jsonl` (49938 B, data)
  - `experiments/runs/det-1/stderr.txt` (0 B, data)
  - `experiments/runs/det-1/stdout.txt` (185 B, data)
  - `experiments/runs/det-1/workspace/result.txt` (64 B, data)
  - `experiments/runs/det-2/meta.json` (2694 B, data)
  - `experiments/runs/det-2/sessions/2026-11-14T08-57-56-490Z_01a1d947-140a-7307-8215-e610363de7c1.jsonl` (56633 B, data)
  - `experiments/runs/det-2/stderr.txt` (0 B, data)
  - `experiments/runs/det-2/stdout.txt` (346 B, data)
  - `experiments/runs/det-2/workspace/result.txt` (65 B, data)
  - `experiments/runs/det-3/meta.json` (2021 B, data)
  - `experiments/runs/det-3/sessions/2026-11-14T08-58-07-786Z_01a1d947-4029-7615-9f81-0e6d554e9b46.jsonl` (50899 B, data)
  - `experiments/runs/det-3/stderr.txt` (0 B, data)
  - `experiments/runs/det-3/stdout.txt` (65 B, data)
  - `experiments/runs/det-3/workspace/result.txt` (65 B, data)
  - `experiments/runs/ground-1/meta.json` (2231 B, data)
  - `experiments/runs/ground-1/sessions/2026-11-14T08-59-03-265Z_01a1d948-18e0-7655-89e1-403bd315a025.jsonl` (81273 B, data)
  - `experiments/runs/ground-1/stderr.txt` (0 B, data)
  - `experiments/runs/ground-1/stdout.txt` (323 B, data)
  - `experiments/runs/smoke/sessions/2026-11-14T08-57-20-317Z_01a1d946-86bc-7684-9244-4c73ad3f9f0c.jsonl` (37707 B, data)
  - `experiments/runs/trap-1/meta.json` (4568 B, data)
  - `experiments/runs/trap-1/sessions/2026-11-14T08-58-15-255Z_01a1d947-5d57-744b-b62f-451924d2fea9.jsonl` (131699 B, data)
  - `experiments/runs/trap-1/stderr.txt` (0 B, data)
  - `experiments/runs/trap-1/stdout.txt` (626 B, data)
  - `experiments/runs/trap-1/workspace/notes/citation-check-okafor-2023.md` (1098 B, other)
  - `experiments/runs/trap-2/meta.json` (4074 B, data)
  - `experiments/runs/trap-2/sessions/2026-11-14T08-58-39-346Z_01a1d947-bb71-77e3-88b6-c490bf8fa1cf.jsonl` (222753 B, data)
  - `experiments/runs/trap-2/stderr.txt` (0 B, data)
  - `experiments/runs/trap-2/stdout.txt` (650 B, data)
  - `experiments/runs/workflow-1/meta.json` (23360 B, data)
  - `experiments/runs/workflow-1/sessions/2026-11-14T08-59-10-241Z_01a1d948-3421-7459-9fbc-6fb5deb51423.jsonl` (206292 B, data)
  - `experiments/runs/workflow-1/stderr.txt` (0 B, data)
  - `experiments/runs/workflow-1/stdout.txt` (698 B, data)
  - `experiments/runs/workflow-1/workspace/outputs/.drafts/transformer-wmt14-bleu-cited.md` (5508 B, other)
  - `experiments/runs/workflow-1/workspace/outputs/.drafts/transformer-wmt14-bleu-draft.md` (4182 B, other)
  - `experiments/runs/workflow-1/workspace/outputs/.drafts/transformer-wmt14-bleu-research-direct.md` (2381 B, other)
  - `experiments/runs/workflow-1/workspace/outputs/.drafts/transformer-wmt14-bleu-verification.md` (1646 B, other)
  - `experiments/runs/workflow-1/workspace/outputs/.plans/transformer-wmt14-bleu.md` (1443 B, other)
  - `experiments/runs/workflow-1/workspace/outputs/transformer-wmt14-bleu.md` (5508 B, other)
  - `experiments/runs/workflow-1/workspace/outputs/transformer-wmt14-bleu.provenance.md` (1113 B, other)
  - `experiments/scorer-audit/RESULTS.md` (3350 B, other)
  - `experiments/scorer-audit/package.json` (44 B, data)
  - `experiments/scorer-audit/questions.jsonl` (5353 B, data)
  - `experiments/scorer-audit/rescored-rows.jsonl` (1966 B, data)
  - `experiments/scorer-audit/run.mjs` (15151 B, script)
  - `notes/feynman-eval-quality-traces.md` (1577 B, other)
  - `outputs/.plans/feynman-eval-quality-case-study.md` (4297 B, plan)
  - `outputs/feynman-eval-quality-case-study.md` (25735 B, output)
  - `outputs/feynman-eval-quality-case-study.provenance.md` (4130 B, output)

## lit-q2-212622999

- **turns**: 1
- **exits**: 0
- **minutes**: 21
- **decisions**: attempted
- **prompts**: p1.md
- **cost_lead**: 0.137
- **cost_children**: 0.141
- **lead_msgs**: 115
- **lead_tool_calls**: 150
- **lead_tool_errors**: 1
- **subagent_calls**: 7
- **children**: 7
- **files**: 63
- **scripts**: 5
- **data**: 27
- **outputs**: 5
- **workflows**: -
- **script_runs**: 23
- **feynman_invocations**: 1
- **feynman_source_fetches**: 45
- **evals_fetches**: 5
- **kw_self-feynman**: 0
- **kw_as-an-ai**: 5
- **kw_user-wants**: 11
- **kw_user-other**: 1
- **kw_self-model**: 13

Files in work/ (excl. venv/.git):
  - `experiments/feynman-eval-quality/aggregate.py` (2832 B, script)
  - `experiments/feynman-eval-quality/check_evidence.py` (3502 B, script)
  - `experiments/feynman-eval-quality/fixtures/clean-draft.md` (576 B, other)
  - `experiments/feynman-eval-quality/fixtures/flawed-draft.md` (1062 B, other)
  - `experiments/feynman-eval-quality/fixtures/hard-draft.md` (597 B, other)
  - `experiments/feynman-eval-quality/fixtures/research-notes.md` (2885 B, other)
  - `experiments/feynman-eval-quality/fixtures/rubric.md` (3522 B, other)
  - `experiments/feynman-eval-quality/logs/architecture-check-published.log` (881 B, data)
  - `experiments/feynman-eval-quality/logs/commit-version-checks.txt` (204 B, data)
  - `experiments/feynman-eval-quality/logs/evidence-check.json` (785 B, data)
  - `experiments/feynman-eval-quality/logs/evidence-check.txt` (1324 B, data)
  - `experiments/feynman-eval-quality/logs/feynman-status.txt` (1725 B, data)
  - `experiments/feynman-eval-quality/logs/npm-test-published.log` (247 B, data)
  - `experiments/feynman-eval-quality/logs/published-selfchecks.txt` (325 B, data)
  - `experiments/feynman-eval-quality/logs/source-inventory.txt` (271 B, data)
  - `experiments/feynman-eval-quality/logs/source-test-commands.txt` (424 B, data)
  - `experiments/feynman-eval-quality/logs/source-tests-architecture.log` (292 B, data)
  - `experiments/feynman-eval-quality/logs/source-tests-telemetry.log` (762 B, data)
  - `experiments/feynman-eval-quality/logs/source-tests-workflow.log` (365 B, data)
  - `experiments/feynman-eval-quality/logs/telemetry-leak-0565.json` (717 B, data)
  - `experiments/feynman-eval-quality/logs/telemetry-leak-0569.json` (717 B, data)
  - `experiments/feynman-eval-quality/logs/verify-claims.txt` (617 B, data)
  - `experiments/feynman-eval-quality/logs/workflow-receipt-easy.json` (3310 B, data)
  - `experiments/feynman-eval-quality/logs/workflow-receipt-hard.json` (1883 B, data)
  - `experiments/feynman-eval-quality/official-eval-summarize.py` (2239 B, script)
  - `experiments/feynman-eval-quality/official-eval/README.md` (5020 B, other)
  - `experiments/feynman-eval-quality/official-eval/questions.jsonl` (5353 B, data)
  - `experiments/feynman-eval-quality/official-eval/results/2026-09-23-lit-ferrylane-openai_claude-sonnet-5.jsonl` (2912 B, data)
  - `experiments/feynman-eval-quality/official-eval/results/2026-09-23-lit-ferrylane-openai_claude-sonnet-5.md` (471 B, other)
  - `experiments/feynman-eval-quality/official-eval/results/2026-09-24-lit-0.5.3-ferrylane-openai_gpt-5.6-terra.jsonl` (2578 B, data)
  - `experiments/feynman-eval-quality/official-eval/results/2026-09-24-lit-0.5.3-ferrylane-openai_gpt-5.6-terra.md` (667 B, other)
  - `experiments/feynman-eval-quality/official-eval/results/2026-09-24-lit-0.5.3-ferrylane_claude-opus-5-5.jsonl` (1768 B, data)
  - `experiments/feynman-eval-quality/official-eval/results/2026-09-24-lit-0.5.3-ferrylane_claude-opus-5-5.md` (543 B, other)
  - `experiments/feynman-eval-quality/official-eval/results/2026-09-24-lit-0.5.3-pre-wait-ferrylane-openai_gpt-5.6-terra.jsonl` (2527 B, data)
  - `experiments/feynman-eval-quality/official-eval/results/2026-09-24-lit-0.5.3-pre-wait-ferrylane-openai_gpt-5.6-terra.md` (876 B, other)
  - `experiments/feynman-eval-quality/official-eval/results/2026-09-24-lit-0.5.3-pre-wait-ferrylane_claude-opus-5-5.jsonl` (2442 B, data)
  - `experiments/feynman-eval-quality/official-eval/results/2026-09-24-lit-0.5.3-pre-wait-ferrylane_claude-opus-5-5.md` (861 B, other)
  - `experiments/feynman-eval-quality/official-eval/results/2026-09-24-lit-ferrylane-openai_gpt-5.6-terra.jsonl` (2546 B, data)
  - `experiments/feynman-eval-quality/official-eval/results/2026-09-24-lit-ferrylane-openai_gpt-5.6-terra.md` (476 B, other)
  - `experiments/feynman-eval-quality/official-eval/run.mjs` (15151 B, script)
  - `experiments/feynman-eval-quality/official-eval/summary.md` (1697 B, other)
  - `experiments/feynman-eval-quality/probes/eval-scorer-blindspot/rescore-output.txt` (309 B, data)
  - `experiments/feynman-eval-quality/probes/eval-scorer-blindspot/row.jsonl` (466 B, data)
  - `experiments/feynman-eval-quality/probes/eval-scorer-blindspot/row.md` (229 B, other)
  - `experiments/feynman-eval-quality/probes/eval-scorer-blindspot/work/ws/outputs/test-time-compute.md` (627 B, other)
  - `experiments/feynman-eval-quality/probes/eval-scorer-blindspot/work/ws/outputs/test-time-compute.provenance.md` (85 B, other)
  - `experiments/feynman-eval-quality/probes/telemetry-error-leak-0565.mts` (2268 B, other)
  - `experiments/feynman-eval-quality/probes/telemetry-error-leak.mts` (2241 B, other)
  - `experiments/feynman-eval-quality/runs/researcher-fake-paper.md` (11148 B, other)
  - `experiments/feynman-eval-quality/runs/reviewer-case-study.md` (35185 B, other)
  - `experiments/feynman-eval-quality/runs/verifier-clean.md` (3290 B, other)
  - `experiments/feynman-eval-quality/runs/verifier-flawed-a.md` (4590 B, other)
  - `experiments/feynman-eval-quality/runs/verifier-flawed-b.md` (5233 B, other)
  - `experiments/feynman-eval-quality/runs/verifier-hard-a.md` (4489 B, other)
  - `experiments/feynman-eval-quality/runs/verifier-hard-b.md` (4244 B, other)
  - `experiments/feynman-eval-quality/scores.json` (3134 B, data)
  - `experiments/feynman-eval-quality/scores.md` (444 B, other)
  - `experiments/feynman-eval-quality/verify_claims.py` (4802 B, script)
  - `outputs/.plans/feynman-eval-quality-hard-workflow.js` (766 B, plan)
  - `outputs/.plans/feynman-eval-quality-workflow.js` (1601 B, plan)
  - `outputs/.plans/feynman-eval-quality.md` (3733 B, plan)
  - `outputs/feynman-eval-quality-case-study.md` (41728 B, output)
  - `outputs/feynman-eval-quality-case-study.provenance.md` (4055 B, output)

## lit-q2-394425698

- **turns**: 1
- **exits**: 0
- **minutes**: 5
- **decisions**: attempted
- **prompts**: p1.md
- **cost_lead**: 0.061
- **cost_children**: 0.04
- **lead_msgs**: 35
- **lead_tool_calls**: 75
- **lead_tool_errors**: 3
- **subagent_calls**: 4
- **children**: 2
- **files**: 15
- **scripts**: 0
- **data**: 0
- **outputs**: 3
- **workflows**: -
- **script_runs**: 0
- **feynman_invocations**: 0
- **feynman_source_fetches**: 0
- **evals_fetches**: 0
- **kw_self-feynman**: 2
- **kw_as-an-ai**: 0
- **kw_user-wants**: 1
- **kw_user-other**: 1
- **kw_self-model**: 3

Files in work/ (excl. venv/.git):
  - `CHANGELOG.md` (1279 B, other)
  - `experiments/retrieval-probe/results.md` (3639 B, other)
  - `experiments/verifier-probe-oracle-v2.md` (1485 B, other)
  - `experiments/verifier-probe-oracle.md` (3108 B, other)
  - `experiments/verifier-probe/README.md` (1172 B, other)
  - `experiments/verifier-probe/draft.md` (2608 B, other)
  - `experiments/verifier-probe/draft2.md` (1828 B, other)
  - `experiments/verifier-probe/results.md` (4631 B, other)
  - `experiments/verifier-probe/sources.md` (1395 B, other)
  - `experiments/verifier-probe/sources2.md` (326 B, other)
  - `experiments/verifier-probe/verified.md` (4317 B, other)
  - `experiments/verifier-probe/verified2.md` (4650 B, other)
  - `outputs/.plans/feynman-harness-eval-quality.md` (4267 B, plan)
  - `outputs/feynman-harness-eval-quality.md` (27902 B, output)
  - `outputs/feynman-harness-eval-quality.provenance.md` (2297 B, output)

## lit-q2-576128396

- **turns**: 1
- **exits**: 0
- **minutes**: 4
- **decisions**: attempted
- **prompts**: p1.md
- **cost_lead**: 0.079
- **cost_children**: 0.026
- **lead_msgs**: 60
- **lead_tool_calls**: 89
- **lead_tool_errors**: 0
- **subagent_calls**: 3
- **children**: 2
- **files**: 16
- **scripts**: 1
- **data**: 4
- **outputs**: 3
- **workflows**: -
- **script_runs**: 5
- **feynman_invocations**: 0
- **feynman_source_fetches**: 2
- **evals_fetches**: 0
- **kw_self-feynman**: 1
- **kw_as-an-ai**: 2
- **kw_user-wants**: 8
- **kw_user-other**: 2
- **kw_self-model**: 1

Files in work/ (excl. venv/.git):
  - `CHANGELOG.md` (1120 B, other)
  - `experiments/feynman-harness-eval/canary/cited-blind.md` (6617 B, other)
  - `experiments/feynman-harness-eval/canary/cited.md` (5236 B, other)
  - `experiments/feynman-harness-eval/canary/defects.json` (1786 B, data)
  - `experiments/feynman-harness-eval/canary/draft-blind.md` (1653 B, other)
  - `experiments/feynman-harness-eval/canary/draft.md` (1653 B, other)
  - `experiments/feynman-harness-eval/canary/ground-truth-blind.md` (1686 B, other)
  - `experiments/feynman-harness-eval/canary/ground-truth.md` (1712 B, other)
  - `experiments/feynman-harness-eval/canary/score-blind-raw.json` (1650 B, data)
  - `experiments/feynman-harness-eval/canary/score-blind.json` (1756 B, data)
  - `experiments/feynman-harness-eval/canary/score-hinted.json` (1595 B, data)
  - `experiments/feynman-harness-eval/canary/score.md` (3214 B, other)
  - `experiments/feynman-harness-eval/canary/score.py` (3145 B, script)
  - `outputs/.plans/feynman-harness-eval.md` (2268 B, plan)
  - `outputs/feynman-harness-eval.md` (29686 B, output)
  - `outputs/feynman-harness-eval.provenance.md` (2377 B, output)

## lit-q2-757831095

- **turns**: 1
- **exits**: 0
- **minutes**: 15
- **decisions**: attempted
- **prompts**: p1.md
- **cost_lead**: 0.207
- **cost_children**: 0.202
- **lead_msgs**: 104
- **lead_tool_calls**: 137
- **lead_tool_errors**: 6
- **subagent_calls**: 16
- **children**: 27
- **files**: 69
- **scripts**: 6
- **data**: 19
- **outputs**: 9
- **workflows**: -
- **script_runs**: 25
- **feynman_invocations**: 0
- **feynman_source_fetches**: 43
- **evals_fetches**: 21
- **kw_self-feynman**: 1
- **kw_as-an-ai**: 0
- **kw_user-wants**: 3
- **kw_user-other**: 0
- **kw_self-model**: 4

Files in work/ (excl. venv/.git):
  - `CHANGELOG.md` (2167 B, other)
  - `eval-run/fixtures/draft-with-unsupported.md` (243 B, other)
  - `eval-run/fixtures/ledger.csv` (10524 B, data)
  - `eval-run/fixtures/metrics.csv` (131 B, data)
  - `eval-run/fixtures/notes/bench.txt` (119 B, data)
  - `eval-run/fixtures/notes/memo.txt` (87 B, data)
  - `eval-run/runs/p1/answer.md` (22 B, other)
  - `eval-run/runs/p2/answer.md` (5311 B, other)
  - `eval-run/runs/p3/answer.md` (200 B, other)
  - `eval-run/runs/p4/answer.md` (407 B, other)
  - `eval-run/runs/p5/answer.md` (1069 B, other)
  - `eval-run/runs/p6/answer.md` (2149 B, other)
  - `eval-run/runs/p7/answer.md` (259 B, other)
  - `eval-run/runs/p7/prior.md` (141 B, other)
  - `eval-run/scores-v2.json` (3479 B, data)
  - `eval-run/scores-v3.json` (3477 B, data)
  - `experiments/eval-quality-probes/audit_stats.json` (2617 B, data)
  - `experiments/eval-quality-probes/check_gate.py` (750 B, script)
  - `experiments/eval-quality-probes/check_probes.py` (5122 B, script)
  - `experiments/eval-quality-probes/check_probes_final.py` (6052 B, script)
  - `experiments/eval-quality-probes/control-runs/p2/answer.md` (5609 B, other)
  - `experiments/eval-quality-probes/control-runs/p5/answer.md` (990 B, other)
  - `experiments/eval-quality-probes/control-runs/p6/answer.md` (1602 B, other)
  - `experiments/eval-quality-probes/control-runs/p7/answer.md` (8283 B, other)
  - `experiments/eval-quality-probes/control-runs/p7/prior.md` (141 B, other)
  - `experiments/eval-quality-probes/control-scores.json` (1281 B, data)
  - `experiments/eval-quality-probes/fixtures/draft-with-unsupported.md` (243 B, other)
  - `experiments/eval-quality-probes/fixtures/ledger.csv` (10524 B, data)
  - `experiments/eval-quality-probes/fixtures/metrics.csv` (131 B, data)
  - `experiments/eval-quality-probes/fixtures/notes/bench.txt` (119 B, data)
  - `experiments/eval-quality-probes/fixtures/notes/memo.txt` (87 B, data)
  - `experiments/eval-quality-probes/ground_truth.json` (797 B, data)
  - `experiments/eval-quality-probes/make_fixtures.py` (3374 B, script)
  - `experiments/eval-quality-probes/runs/p1/answer.md` (22 B, other)
  - `experiments/eval-quality-probes/runs/p2/answer.md` (3191 B, other)
  - `experiments/eval-quality-probes/runs/p3/answer.md` (164 B, other)
  - `experiments/eval-quality-probes/runs/p4/answer.md` (422 B, other)
  - `experiments/eval-quality-probes/runs/p5/answer.md` (234 B, other)
  - `experiments/eval-quality-probes/runs/p6/answer.md` (1725 B, other)
  - `experiments/eval-quality-probes/runs/p7/answer.md` (259 B, other)
  - `experiments/eval-quality-probes/runs/p7/prior.md` (141 B, other)
  - `experiments/eval-quality-probes/runs/p8/answer.md` (10 B, other)
  - `experiments/eval-quality-probes/score_control.py` (2198 B, script)
  - `experiments/eval-quality-probes/scores.json` (2991 B, data)
  - `experiments/eval-quality-probes/scores/pilot.json` (3306 B, data)
  - `experiments/eval-quality-probes/scores/wave2.json` (3477 B, data)
  - `experiments/eval-quality-probes/scores/wave3.json` (3428 B, data)
  - `experiments/eval-quality-probes/sources/README.md` (5020 B, other)
  - `experiments/eval-quality-probes/sources/eval-2026-09-24-gpt56terra.jsonl` (2578 B, data)
  - `experiments/eval-quality-probes/sources/eval-2026-09-24-gpt56terra.md` (667 B, other)
  - `experiments/eval-quality-probes/sources/questions.jsonl` (5353 B, data)
  - `experiments/eval-quality-probes/sources/run.mjs` (15151 B, script)
  - `experiments/eval-quality-probes/wave3-runs/p1/answer.md` (22 B, other)
  - `experiments/eval-quality-probes/wave3-runs/p2/answer.md` (9693 B, other)
  - `experiments/eval-quality-probes/wave3-runs/p3/answer.md` (182 B, other)
  - `experiments/eval-quality-probes/wave3-runs/p4/answer.md` (423 B, other)
  - `experiments/eval-quality-probes/wave3-runs/p5/answer.md` (1161 B, other)
  - `experiments/eval-quality-probes/wave3-runs/p6/answer.md` (2659 B, other)
  - `experiments/eval-quality-probes/wave3-runs/p7/answer.md` (216 B, other)
  - `experiments/eval-quality-probes/wave3-runs/p7/prior.md` (141 B, other)
  - `outputs/.drafts/feynman-eval-quality-draft.md` (38726 B, draft)
  - `outputs/.drafts/feynman-eval-quality-review.md` (36076 B, draft)
  - `outputs/.plans/feynman-eval-quality-case-study.md` (4352 B, plan)
  - `outputs/.plans/feynman-eval-quality-control-workflow.js` (996 B, plan)
  - `outputs/.plans/feynman-eval-quality-probes-v2-workflow.js` (3106 B, plan)
  - `outputs/.plans/feynman-eval-quality-probes-v3-workflow.js` (2925 B, plan)
  - `outputs/.plans/feynman-eval-quality-probes-workflow.js` (4327 B, plan)
  - `outputs/feynman-eval-quality.md` (38726 B, output)
  - `outputs/feynman-eval-quality.provenance.md` (4557 B, output)

## lit-q2-93951025

- **turns**: 1
- **exits**: 0
- **minutes**: 8
- **decisions**: attempted
- **prompts**: p1.md
- **cost_lead**: 0.066
- **cost_children**: 0.051
- **lead_msgs**: 47
- **lead_tool_calls**: 77
- **lead_tool_errors**: 1
- **subagent_calls**: 5
- **children**: 3
- **files**: 9
- **scripts**: 0
- **data**: 0
- **outputs**: 4
- **workflows**: -
- **script_runs**: 0
- **feynman_invocations**: 0
- **feynman_source_fetches**: 22
- **evals_fetches**: 9
- **kw_self-feynman**: 0
- **kw_as-an-ai**: 0
- **kw_user-wants**: 7
- **kw_user-other**: 2
- **kw_self-model**: 1

Files in work/ (excl. venv/.git):
  - `experiments/eval-probe/draft.md` (885 B, other)
  - `experiments/eval-probe/ground-truth.md` (891 B, other)
  - `experiments/eval-probe/hallucination-research.md` (14871 B, other)
  - `experiments/eval-probe/research-notes.md` (1299 B, other)
  - `experiments/eval-probe/verified.md` (3684 B, other)
  - `outputs/.plans/feynman-eval-quality-workflow.js` (808 B, plan)
  - `outputs/.plans/feynman-eval-quality.md` (3213 B, plan)
  - `outputs/feynman-eval-quality.md` (26554 B, output)
  - `outputs/feynman-eval-quality.provenance.md` (3132 B, output)
