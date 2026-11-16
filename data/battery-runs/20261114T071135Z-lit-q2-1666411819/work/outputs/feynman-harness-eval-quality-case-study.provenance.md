# Provenance: Feynman 0.5.65 as an evaluation instrument

- **Date:** 2026-11-14
- **Workflow:** direct case study (no `/deepresearch` plan gate)
- **Harness:** Feynman `0.5.65` installed; repository HEAD `0.5.69` (`1174429`)
- **Rounds:** 1 synthesis round, 2 runtime verification probes (1 contaminated, discarded as a capability measurement; 1 clean), 1 meta-eval probe suite
- **Sources consulted:** 11 external sources (8 papers, 3 Feynman artifacts) plus the repository tree at `1174429`
- **Sources accepted:** 11
- **Sources rejected:** 2 — 1 dead URL in the verifier fixture (`https://feynman.is/docs/evals/research-quality`, HTTP 404) and 1 fabricated paper (`arXiv:2409.99999`) rejected by the verifier
- **Adversarial review:** `outputs/feynman-harness-eval-quality-case-study.review.md` (three MAJOR issues fixed: p-value pairing, trace-capture claim, q01 re-score disclosure)
- **Verification:** PASS WITH NOTES (post-review)
- **Plan:** none (direct case study; no long-running multi-agent plan artifact)
- **Research files:**
  - `experiments/eval-scorer-probe.mjs`
  - `experiments/eval-scorer-probe-results.json`
  - `experiments/eval-scorer-probe.log`
  - `experiments/score-verifier-output.mjs`
  - `experiments/verifier-output-score.json`
  - `experiments/verifier-output-score.log`
  - `experiments/eval-stats.log`
  - `experiments/verifier-usage.log`
  - `outputs/.probes/verifier-probe-draft.md`
  - `outputs/.probes/verifier-probe-verified.md` (contaminated negative control)
  - `/tmp/verifier-probe-clean/verified.md` (clean probe output)
- **Repository evidence:**
  - `evals/README.md`, `evals/run.mjs`, `evals/questions.jsonl`, `evals/results/*`
  - `prompts/lit.md`, `prompts/deepresearch.md`
  - `.feynman/agents/verifier.md`
  - `package.json`, `RELEASES.md`, `.github/workflows/*`

## What was checked

- **Scorer probes:** 8 synthetic citation cases; all 8 matched their expected scorer behavior. The expectations are recorded in `experiments/eval-scorer-probe-results.json`. Gaps demonstrated: P4 (negation invisible), P5 (author–year invisible), P8 (URL-only invisible).
- **Aggregate-table probe:** two rows, one with zero checkable citations; the "all" row reports 100% validity and title because nulls are skipped.
- **`done` probe:** empty provenance passes; empty final plus empty provenance passes; final without provenance fails.
- **Verifier-output scoring:** draft 66.7% valid, transparent correction 75.0%, silent deletion 100.0%.
- **Runtime verifier:** clean run passed a 10-item manual rubric (`n=1`, not blinded). The first run was contaminated by probe fixtures in `/work` and is excluded from the capability claim.
- **Committed results:** all 22 rows inspected for version, SHA, dirty flag, completion, citations, validity, title match, recall, tokens, and failures.

## Notes and caveats

- No full 12-question eval run was performed. The committed record covers only q01, q04, q07, and q10.
- The runtime verifier probe used `openrouter/deepseek/deepseek-v4.1-flash-1017` in this environment; results may not transfer to other models.
- The first verifier run's output is retained only as a contamination example. Its citation to `experiments/eval-scorer-probe.mjs` is evidence of fixture leakage, not of verification quality.
- The `$0.00` cost figures in the repository's eval tables are a missing-`cost`-block artifact, not a claim that the runs were free. The verifier cost in this study is session-reported.
- The artifact labels the committed 0.5.3 runs as "dirty" because their rows record `git_dirty: true`; the exact tested tree cannot be reconstructed from `c1e0b29`.
- The scorecard ratings are author judgment, grounded in the cited evidence, not a standardized instrument.

## Verification status by claim class

| Claim class | Status |
|---|---|
| Scorer behavior (P1–P8, table, `done`) | verified by execution |
| Committed result numbers | verified against `evals/results/*.jsonl` |
| Version/SHA/dirty provenance | verified against git |
| Verifier clean-run behavior | verified by reading its output and transcript; `n=1`, manual rubric |
| Verifier contaminated-run behavior | observed; excluded from capability claim |
| Claim-level error rate in real Feynman reports | **not measured** |
| Cost per question in real runs | **not measured** (cost block absent) |
| Human/expert correlation | **not measured** |
