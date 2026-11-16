# Provenance: Feynman as an AI-eval-quality case study

- **Date:** 2026-11-14
- **Rounds:** 1 static audit; 6 behavioral probes (4 verifier, 1 clean control, 1 researcher); 4 non-LLM probes (published self-checks, telemetry error path, eval-scorer blindspot, source test inventory); 1 adversarial reviewer pass on the case study.
- **Sources consulted:** installed `@companion-ai/feynman@0.5.65`; source repo `Companion-Inc/feynman` main `1174429` (0.5.69); `evals/` (README, runner, questions, six committed result files); `.feynman/SYSTEM.md`; four agent prompts; 11 workflow prompts; 16 skills; telemetry extension; package manifest; CI workflow; seven papers (Vaswani 2017, Devlin 2019, Brown 2020, Snell 2024, Liang 2022, Biderman 2024, THOR-MoE 2025).
- **Sources accepted:** all local artifacts listed below; arXiv metadata for the seven papers; the committed eval result files. The release-note claim "0.5.2: 43 of 43 citations" was **not** accepted as verified because the committed 43-citation run is labeled 0.5.0 and the committed 0.5.2 GPT-5.6 Terra run has 28 citations and 3/4 completion.
- **Sources rejected:** none. The 0.5.2/43-citation release-note claim is marked unresolved, not rejected.
- **Verification:** PASS WITH NOTES.
  - Local probes: marker-checked (21/21 automated checks in `experiments/feynman-eval-quality/logs/verify-claims.txt`). The 24/24 and 12/12 counts are derived by `check_evidence.py` from the raw outputs, but the marker patterns and the rubric scoring are manual and not independently scored.
  - Official eval: summarized from committed files, **not rerun**.
  - Behavioral probes: n=1 or n=2, one model (`openrouter/deepseek/deepseek-v4.1-flash-1017`), fixture-specific; not a benchmark.
  - Telemetry leak: verified at unit level on 0.5.65 and 0.5.69; not observed in a live PostHog send.
  - Version gap: installed 0.5.65 vs source 0.5.69.
- **Plan:** `outputs/.plans/feynman-eval-quality.md`
- **Research files:**
  - `experiments/feynman-eval-quality/fixtures/` — easy, hard, clean drafts; research notes; rubric.
  - `experiments/feynman-eval-quality/runs/` — six raw agent outputs plus the reviewer audit of the case study.
  - `experiments/feynman-eval-quality/scores.json`, `aggregate.py`, `scores.md` — probe scoring.
  - `experiments/feynman-eval-quality/official-eval/` — eval README, runner, questions, six result files, summary.
  - `experiments/feynman-eval-quality/probes/eval-scorer-blindspot/` — false-claim rescore probe.
  - `experiments/feynman-eval-quality/probes/telemetry-error-leak-0565.mts`, `telemetry-error-leak.mts` — telemetry probes.
  - `experiments/feynman-eval-quality/logs/` — command outputs, source-test logs, telemetry leak JSON, workflow receipts, model-status snapshot, 21-check verification log.
  - `experiments/feynman-eval-quality/verify_claims.py` — artifact-to-claim checker.

## What was actually checked

- Installed version and source version.
- Published `npm test` (0 tests, exit 0) and `npm run architecture:check` (exit 1, MODULE_NOT_FOUND).
- Three source test files (3 + 7 + 2 tests, all pass).
- Verifier detection and true-claim retention on four runs.
- Researcher refusal to fabricate a nonexistent paper.
- Telemetry error-path leakage on 0.5.65 and 0.5.69.
- Official eval scorer's verdict on a deliberately false claim (100% on done/valid/title/recall).
- 22 official eval rows: 18 completed, 4 incomplete, 137,664,710 tokens, 20,591 wall seconds, cost $0.
- Six result files, 12 questions, 4 distinct question ids, 0.5.3 dirty flags, 0.5.0/0.5.2/0.5.3 citation counts.

## What was not checked

- The official eval was not rerun; its results are from 2026-09-23/24 and different models (GPT-5.6 Terra, Claude Sonnet 5, Claude Opus 5.5).
- No live PostHog send was observed.
- No adversarial web page or prompt-injection fixture was run.
- No cross-model verifier comparison was run.
- No human labeling or inter-rater reliability study was run.
- The 0.5.3 `git_dirty` runs cannot be reconstructed from the recorded SHA alone.
