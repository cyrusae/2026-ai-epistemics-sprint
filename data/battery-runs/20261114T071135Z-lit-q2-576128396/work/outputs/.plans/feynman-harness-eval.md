# Plan: Feynman harness case study (AI-eval-quality perspective)

Slug: `feynman-harness-eval`

## Objective
Assess the Feynman research-agent harness as a case study in AI evaluation quality, using
the harness itself (dogfooding) to generate evidence.

## Key questions
1. What control surfaces does the harness expose that bear on eval quality (provenance,
   verification, delegation, observability)?
2. Does the harness's own verification stage detect known citation/claim defects?
3. Where does the harness's internal evaluation fall short of published eval-quality
   standards (construct validity, contamination, statistical power, grading)?
4. What would a credible external eval of this harness look like?

## Evidence needed
- Static: SYSTEM.md, agent prompts, workflow prompts, telemetry, tool implementations.
- Empirical: canary audit of `verifier` on a draft with 6 planted defects + 1 control.
- External: eval-quality literature (DeepResearch Bench/FACT, ResearchRubrics,
  agentic benchmark best practices, construct validity).

## Scale decision
Single lead agent plus one `verifier` subagent for the canary. No researcher fan-out:
the evidence base is local plus a small set of known papers.

## Task ledger
| ID | Task | Owner | Status |
|----|------|-------|--------|
| T1 | Static audit of harness control surfaces | lead | done |
| T2 | Build canary draft + ground truth + defect manifest | lead | done |
| T3 | Run verifier on canary draft | verifier | done (hinted + blind) |
| T4 | Score detection and false positives | lead | done |
| T5 | External eval-quality grounding | lead | done |
| T6 | Write case study artifact | lead | done |

## Verification log
- arXiv metadata for 1706.03762, 1810.04805, 2201.11903, 2303.08774 checked via
  `feynman_science_database_search` (source: arxiv). Verified 2026-11-14.
- Canary scoring recorded in `experiments/feynman-harness-eval/canary/score.md`; both runs detected 6/6 planted defects and preserved the control.

## Decision log
- Chose a canary audit over a full `/lit` run: cheaper, controlled, and directly measures
  the verification claim rather than end-to-end prose quality.
- Will not claim end-to-end benchmark performance; the canary is a mechanism test, n=2 (one hinted, one blind).
