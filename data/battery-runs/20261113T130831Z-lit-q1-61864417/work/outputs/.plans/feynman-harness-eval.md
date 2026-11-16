# Plan: Feynman harness as an AI-eval instrument

**Slug:** `feynman-harness-eval`
**Started:** 2026-11-13
**Question:** What does the Feynman research harness look like when treated as an evaluation instrument, and what does dogfooding reveal about the quality of the evidence it produces?

## Key questions

1. Which of Feynman's epistemic guarantees are mechanically enforced, and which are only prompt-level conventions?
2. Does the harness's own verification stage catch injected factual/citation defects, and at what false-positive cost?
3. How does the harness behave on an unanswerable/false-premise request?
4. What observability exists for auditing a run after the fact (traces, telemetry, artifacts, version pinning)?
5. How do these properties map onto established eval-quality criteria (task validity, outcome validity, reporting, reliability)?

## Evidence needed

- Local harness source: system prompt, agent contracts, workflow prompts, runtime code, tests, CI, release notes, settings.
- External criteria: Agentic Benchmark Checklist (NeurIPS 2025), eval statistics (Miller 2024), harness/scaffold sensitivity (2026 preprints), judge bias, SWE-bench harness audits.
- Controlled probes with deterministic grading:
  - P1: verifier fixture with a corrupted number, a fabricated citation, an unsourced statistic, and two correct controls. Run twice for stability.
  - P2: researcher probe on a non-existent paper with a plausible fake DOI.
  - P3: tool-failure semantics on a 404 URL.
  - P4: post-hoc parse of this session's JSONL trace.

## Scale decision

Single lead agent plus three bounded subagent runs (verifier x2, researcher x1). No parallel literature fan-out: the reference set is small and already located.

## Task ledger

| ID | Task | Owner | Status | Output |
|----|------|-------|--------|--------|
| T1 | Local harness audit (prompts, agents, dist, tests, CI) | lead | done | notes in final artifact |
| T2 | External criteria search + URL/ID verification | lead | done | final artifact Sources |
| T3 | Build verifier fixture + grader | lead | done | `experiments/feynman-harness-eval/` |
| T4 | Verifier run 1 | verifier subagent | running | `outputs/.drafts/harness-eval-verifier-run1.md` |
| T5 | Verifier run 2 (same input) | verifier subagent | running | `outputs/.drafts/harness-eval-verifier-run2.md` |
| T6 | False-premise researcher probe | researcher subagent | running | `outputs/.drafts/harness-eval-false-premise.md` |
| T7 | Grade probes mechanically | lead | pending | `experiments/feynman-harness-eval/grade.py` output |
| T8 | Session trace audit | lead | pending | `experiments/feynman-harness-eval/trace-audit.json` |
| T9 | Write case study | lead | pending | `outputs/feynman-harness-eval.md` |
| T10 | Adversarial self-review of draft | lead | pending | `outputs/.drafts/feynman-harness-eval-review.md` |

## Verification log

| Check | Status | Evidence |
|-------|--------|----------|
| arXiv IDs resolve to claimed titles/dates | verified | `curl` metadata, 2026-11-13 |
| ABC NeurIPS page resolves | verified | HTTP 200 + title |
| Feynman version/model/session path recorded | verified | env + session header |
| Fault-injection fixture defects are unambiguous | verified | source notes quote exact values |
| Verifier catches injected defects | not run | T4/T5 |
| False-premise probe does not fabricate | not run | T6 |
| Final artifact exists on disk | not run | T9 |

## Decision log

- Use deterministic post-hoc grading rather than asking a model to grade itself.
- Treat the two verifier runs as a stability check, not a statistically powered reliability estimate (n=2).
- Do not run a full `/deepresearch` end-to-end: expensive, and its output would be graded by the same model family.