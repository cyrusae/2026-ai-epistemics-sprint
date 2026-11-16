# Plan: Feynman harness as an AI-eval-quality case study

## Objective

Audit the Feynman research agent's evaluation and verification machinery, dogfood it with small behavioral probes, and produce one reproducible case study.

## Key questions

1. What eval-quality mechanisms does Feynman actually ship (prompts, agents, tests, CI, eval harness, telemetry)?
2. Does the verifier detect fabricated, contradicted, and misattributed claims?
3. Does the researcher refuse to fabricate a nonexistent paper?
4. Does the official eval measure claim support, or only citation metadata?
5. What breaks in the published artifact and in telemetry error paths?

## Scale decision

Lead-owned audit plus a small parallel subagent workflow. No broad literature survey. Four verifier runs (2 easy, 2 hard), one clean control, one researcher probe.

## Task ledger

| Task | Owner | Status | Artifact |
|---|---|---|---|
| Static audit of prompts/agents/telemetry/package | lead | done | notes in final artifact |
| Official eval harness audit | lead | done | `experiments/feynman-eval-quality/official-eval/` |
| Easy/hard/clean fixtures + rubric | lead | done | `experiments/feynman-eval-quality/fixtures/` |
| Verifier probes (4 runs) + clean control | verifier subagents | done | `experiments/feynman-eval-quality/runs/` |
| Researcher fabrication probe | researcher subagent | done | `experiments/feynman-eval-quality/runs/researcher-fake-paper.md` |
| Telemetry error-path probe | lead | done | `experiments/feynman-eval-quality/probes/telemetry-error-leak-0565.mts` |
| Eval-scorer blindspot probe | lead | done | `experiments/feynman-eval-quality/probes/eval-scorer-blindspot/` |
| Published self-check probe | lead | done | `experiments/feynman-eval-quality/logs/published-selfchecks.txt` |
| Scoring + aggregation | lead | done | `scores.json`, `aggregate.py`, `scores.md` |
| Adversarial reviewer pass | reviewer subagent | done | `experiments/feynman-eval-quality/runs/reviewer-case-study.md` |
| Final case study | lead | done | `outputs/feynman-eval-quality-case-study.md` |

## Verification log

| Check | Result | Evidence |
|---|---|---|
| Installed version | 0.5.65 | `logs/published-selfchecks.txt` |
| Source repo version | 0.5.69, HEAD 1174429 | `logs/source-inventory.txt` |
| Published `npm test` | exit 0, 0 tests | `logs/published-selfchecks.txt` |
| Published `architecture:check` | exit 1, MODULE_NOT_FOUND | `logs/published-selfchecks.txt` |
| Source prompt tests | 3/3 pass | `logs/source-tests-workflow.log` |
| Source telemetry tests | 7/7 pass | `logs/source-tests-telemetry.log` |
| Source architecture tests | 2/2 pass | `logs/source-tests-architecture.log` |
| Verifier defect detection | 24/24 | `scores.md` |
| Verifier true-claim retention | 12/12 | `scores.md` |
| Clean numeric-claim retention | 3/3 | `scores.md` |
| Researcher fabrication refusal | 1/1 | `runs/researcher-fake-paper.md` |
| Telemetry error leak | reproduced on 0.5.65 and 0.5.69 | `logs/telemetry-leak-0565.json` |
| False claim scores 100% on official eval | reproduced | `probes/eval-scorer-blindspot/rescore-output.txt` |
| Reviewer found 4 major + 16 minor issues | 4 major corrected | `runs/reviewer-case-study.md` |
| Marker-derived 24/24 and 12/12 | pass | `logs/evidence-check.txt`, `logs/verify-claims.txt` |

## Decision log

- Used the installed npm package for runtime checks and the source repo for tests/evals/CI because the npm package excludes them.
- Kept the official eval separate from the supplementary probes; the official eval uses different models and dates.
- Marked all behavioral probe results as n=1 or n=2, single-model, fixture-specific.
- Did not rerun the official eval; summarized committed results only.
