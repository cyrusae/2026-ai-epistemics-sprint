# Plan: Feynman harness eval-quality case study

Slug: `feynman-harness-eval-quality`

## Key questions
1. Does the harness's verification layer catch seeded citation/number defects?
2. Does it refuse to fabricate non-existent papers/identifiers?
3. Does its artifact contract force traceable provenance for quantitative claims?
4. What does its own evaluation infrastructure imply for eval quality?

## Task ledger
| ID | Task | Owner | Status |
|---|---|---|---|
| T1 | Pre-register protocol and fixtures | lead | done |
| T2 | Metadata + non-existent-record probes | lead | done |
| T3 | Verifier controlled-defect probe | verifier subagent | done |
| T4 | Researcher non-existent-entity probe | researcher subagent | done |
| T5 | Static audit of prompts/agents/telemetry/package + upstream evals | lead | done |
| T6 | Synthesize artifact | lead | done |

## Verification log
- 2026-11-13: protocol written before probes (`experiments/feynman-eval-case-study/protocol.md`).
- 2026-11-13: P1/P2 metadata probes done; Crossref identifier lookup is fuzzy, not exact.
- 2026-11-13: verifier 5/5 coached and 4/4 hard defects caught; researcher refused fabricated paper; reviewer caught arithmetic inconsistency.
- 2026-11-13: upstream `evals/` audited; six committed runs show `valid` at 100% on completed questions and a completion-only variance pattern.
- 2026-11-13: final artifact and provenance written; upstream eval not re-executed (not run).

## Decision log
- Keep N small; prioritize controlled fixtures over broad surveys.
- Treat subagent probes as behavioral evidence, not benchmark scores.
