# Lab notebook

## 2026-11-14 — slug: feynman-eval-quality-case-study

- Scope: audit `@companion-ai/feynman` 0.5.65 as an AI-eval subject (instrumentation,
  reproducibility, scorer validity, self-report auditability), with the harness dogfooding
  its own tooling.
- Static audit: package, prompts, `dist/`, `RELEASES.md`. Found no temperature/seed control
  and no harness-version field in the session trace; full system prompt + tool schemas are
  persisted.
- Corrected an early wrong assumption: the repo **does** ship an eval suite (`evals/`,
  12 questions, deterministic scorer); it is excluded from the npm package. Do not repeat
  the claim that Feynman has no eval layer.
- Behavioural probes (7 isolated runs, one cheap model): trace completeness 43/43 turns,
  45/45 tool calls paired; fabricated-citation trap refused 2/2; ground-truth retrieval
  5/5; identical prompt produced 2/6/3 tool calls (31.7k/76.2k/43.4k tokens) with the same
  artifact.
- Scorer audit: ran `evals/run.mjs --rescore` on 5 synthetic artifacts. A false-claims
  review scored 100/100/100; valid-but-irrelevant scored 100% valid, 0% recall; fabricated
  ID and wrong-title cases were caught. This is the central finding.
- End-to-end `/deepresearch` probe: 63.7s, 17 tool calls, 485,585 tokens, all 7 artifacts.
  Answer correct; 6/6 cited URLs actually fetched; 27.5-vs-28.4 NeurIPS metadata conflict
  reproduced independently; provenance counts do not reconcile (8 vs 7).
- Committed eval results: 6 files, only 4 of 12 questions ever run, citation validity 100%
  in all 6, cost $0.00 in all 6, `done` is the only discriminating column and it caught the
  `bg_wait` regression.
- Deliverable: `outputs/feynman-eval-quality-case-study.md` (+ `.provenance.md`).
  Experiments: `experiments/README.md`, `experiments/scorer-audit/RESULTS.md`.
- Not run: full 12-question eval; multi-model probe replication; harder fabrication trap.
- Next: if this continues, (a) add the five synthetic controls as a scorer self-test in
  `evals/`, (b) run q01/q11 3× on two models to test whether saturation survives repeats,
  (c) build the claim-support check and label ~30 claims by hand to validate it.
