# Plan — Feynman harness case study (AI-eval-quality)

Slug: `feynman-harness-eval`
Started: 2026-11-14
Workspace: /work
Harness: Feynman 0.5.65, model openrouter/deepseek/deepseek-v4.1-flash-1017, reasoning high

## Question
What does Feynman's design imply for the quality of AI evaluations built on it, and does its verification layer behave as advertised under a controlled adversarial test?

## Scale decision
Direct static analysis (no researchers) + one small controlled experiment with 7 verifier arms.
Rationale: the claim under test is about the harness's own verification behavior; N=1 per arm is enough to find failure modes, not to estimate reliability.

## Task ledger
| ID | Task | Owner | Status | Output |
|---|---|---|---|---|
| T1 | Static inventory of harness rules and agent contracts | lead | done | notes/feynman-harness-static-analysis.md |
| T2 | Build planted-error corpus + ground truth | lead | done | experiments/harness-verifier-eval/GROUND-TRUTH.md |
| T3 | Run verifier arms (7 arms) | subagents | done | experiments/harness-verifier-eval/outputs/ |
| T4 | Score outputs against ground truth | lead | done | experiments/harness-verifier-eval/scorecard.md |
| T5 | Session observability audit | lead | done | experiments/harness-session-audit/final.json |
| T6 | Write case study | lead | done | outputs/feynman-harness-eval-case-study.md |
| T7 | Provenance sidecar | lead | done | outputs/feynman-harness-eval-case-study.provenance.md |

## Verification log
- 2026-11-14: arXiv abs + HTML fetched (43,071 and 188,707 bytes); key numbers extracted from HTML. `1706.03799` resolves to an unrelated paper; `example.com/transformer-bleu` returns 404. Both checked with curl.
- 2026-11-14: 7 verifier arms completed; 52/52 planted items caught; 0 unjustified removals. Disclosure varied; `no-audit` arm confounded by filename and replaced by `default-contract`.
- 2026-11-14: Crossref lookalike hazard reproduced independently (`10.65215/*`, issued 2025-11-13).
- 2026-11-14: Case study + provenance sidecar written; all cited URLs return HTTP 200.

## Decision log
- Treat the paper's 41.0 vs 41.8 EN-FR inconsistency as an unscored observation, not a planted item.
- Score detection manually from output files; do not trust the verifier's self-report alone.
