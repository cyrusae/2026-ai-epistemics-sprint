# Provenance: Feynman harness case study (AI-eval-quality perspective)

- **Date:** 2026-11-14
- **Rounds:** 1 static audit of the installed package; 2 controlled canary runs of the
  `verifier` agent; 1 external eval-quality literature check.
- **Subject version:** `@companion-ai/feynman` 0.5.65, installed at
  `/opt/feynman/feynman-0.5.65-linux-arm64/app`.
- **Model for dogfood runs:** `deepseek/deepseek-v4.1-flash-1017` (OpenRouter), thinking
  level medium for the verifier.
- **Sources consulted:** local package files (`README.md`, `AGENTS.md`,
  `.feynman/SYSTEM.md`, `.feynman/agents/*.md`, `prompts/*.md`, `skills/*/SKILL.md`,
  `extensions/research-tools/telemetry.ts`, `RELEASES.md`); four arXiv records
  (1706.03762, 1810.04805, 2201.11903, 2303.08774); nine external eval-quality sources
  (arXiv 2507.02825, 2506.11763, 2511.07685, 2411.12990, 2601.09688; NeurIPS/ICLR/KDD/ACL
  proceedings URLs listed in the artifact), plus the Feynman repository/docs as a tenth
  external source.
- **Sources accepted:** all sources listed in the artifact's Sources section.
- **Sources rejected:** none removed for being dead or unverifiable. `arXiv:2405.99999`
  was checked and confirmed absent; it is a planted canary defect, not a cited source.
- **Verification:** PASS WITH NOTES. The canary is a mechanism test (n=2, one model, short
  synthetic draft), not an end-to-end benchmark. The static audit covers the installed
  package, not the public repository. The vendor's internal `/lit` eval and 9-paper search
  benchmark are self-reported and were not rerun.
- **Plan:** `outputs/.plans/feynman-harness-eval.md`
- **Research / experiment files:**
  - `experiments/feynman-harness-eval/canary/draft.md`
  - `experiments/feynman-harness-eval/canary/draft-blind.md`
  - `experiments/feynman-harness-eval/canary/ground-truth.md`
  - `experiments/feynman-harness-eval/canary/ground-truth-blind.md`
  - `experiments/feynman-harness-eval/canary/cited.md`
  - `experiments/feynman-harness-eval/canary/cited-blind.md`
  - `experiments/feynman-harness-eval/canary/defects.json`
  - `experiments/feynman-harness-eval/canary/score.py`
  - `experiments/feynman-harness-eval/canary/score.md`
  - `experiments/feynman-harness-eval/canary/score-hinted.json`
  - `experiments/feynman-harness-eval/canary/score-blind.json`
- **Final artifact:** `outputs/feynman-harness-eval.md`
