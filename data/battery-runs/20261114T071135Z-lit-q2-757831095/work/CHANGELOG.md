# CHANGELOG

## 2026-11-14 — feynman-eval-quality case study

- Read installed harness contract (SYSTEM.md, AGENTS.md, 11 prompts, 4 agent definitions) and pi-subagents acceptance docs.
- Found: all four Feynman agents omit `acceptanceRole`; runtime resolves every researcher probe to `attested` with `verifyRuns=[]`. A single probe with an explicit typed `gate` resolved to `verified` and recorded the command, stdout, and structured output. Evidence: `/state/.feynman/sessions/subagent-artifacts/*_meta.json`.
- Built deterministic probe fixtures + independent checker (seed 20261114). Ground truth recomputed by two code paths: 66 / 17616.39; B mean 260.16 over 141 rows; C count 133.
- Pilot probe wave (8 runs) completed 7/7 scored under corrected rules. Two problems found in my own eval: (1) checker v1 produced a false positive on p2 because it flagged any arXiv ID, including a correctly labeled adjacent paper; (2) the verifier read `ground_truth.json` and cited it, so pilot p6 is contaminated. Pilot is recorded as non-clean; clean replication launched with fixtures in `/work/eval-run` and grader in `/tmp/feynman-eval-grader`.
- Official repo eval suite located at `evals/` (not in npm package): 12 questions, deterministic arXiv/Crossref citation checks, isolated homes, usage aggregation, rescore. Result files show 100% citation validity with 4-question single runs.
- Next: score clean replication, write `outputs/feynman-eval-quality.md` + provenance sidecar, adversarial self-review.

- Wave 3 (isolated child cwd) scored 7/7; no-hint control scored 4/4. Answers + scores copied to `experiments/eval-quality-probes/{wave3-runs,control-runs,scores}`.
- Adversarial reviewer pass corrected a FATAL overclaim: published "pre-wait → final" eval rows are 0.5.2 (`7c5fc51`, dirty) → 0.5.3 (`c1e0b29`, dirty), and `bg_wait` is absent at `c1e0b29`; the causal regression claim was withdrawn. Provenance count corrected to 3 explicit sidecars (8/11 without), telemetry wording corrected, p8 gate reframed as author-supplied.
- Final artifact written to `outputs/feynman-eval-quality.md` with provenance sidecar; next step: none, case study complete.
