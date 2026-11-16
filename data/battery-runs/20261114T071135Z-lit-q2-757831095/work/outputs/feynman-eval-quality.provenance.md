# Provenance: Feynman harness eval-quality case study

- **Date:** 2026-11-14
- **Subject:** Feynman 0.5.65 (`/opt/feynman/feynman-0.5.65-linux-arm64/app`), Pi 1.5.0, pi-subagents 0.86.0
- **Model under test:** `openrouter/deepseek/deepseek-v4.1-flash-1017` (thinking: high)
- **Verification:** PASS WITH NOTES
- **Plan:** `outputs/.plans/feynman-eval-quality-case-study.md`
- **Final artifact:** `outputs/feynman-eval-quality.md`

## Sources consulted vs accepted

| Type | Consulted | Accepted for claims | Notes |
|---|---|---|---|
| Local contract files | 19 (`SYSTEM.md`, `AGENTS.md`, 11 prompts, 4 agents, 2 upstream builtin agents) | 19 | Direct reads |
| Runtime code/docs | `package.json`, `current-date.ts`, `telemetry.ts`, pi-subagents `tool-reference.md`, capability listing | 5 | Direct reads; no programmatic citation checker found |
| Remote primary | `evals/README.md`, `run.mjs`, `questions.jsonl`, 6 result `.md`, 1 result `.jsonl`, repo commit, npm registry, arXiv API | 11 | Snapshotted under `experiments/eval-quality-probes/sources/` |
| Harness artifacts | 8 pilot child `*_meta.json` (7 attested, 1 verified), 7 wave-3 transcripts, 4 control transcripts, parent session JSONL | 20 | Acceptance ledgers and leak scans |
| Probe fixtures + answers | 7 fixtures, 3 waves of answers, 4 score files (including control) | 28 | Ground truth precomputed; final scorer applied uniformly |

Rejected: none. The invented paper in p2 is a deliberate negative control, not a source.

## Checks performed

- Ground truth recomputed by two code paths before any harness run (66 / 17,616.39; 260.16 / 141; 133).
- p8 typed gate: host exit 0, stdout verified, `acceptance.status=verified`, `verifyRuns=1`.
- Six ungated pilot researcher runs plus the verifier (7 children): `acceptance.status=attested`, `verifyRuns=0`.
- Capability listing: Feynman's four agents declare no acceptance role; builtin `worker`/`evidence-auditor` do.
- Grep: 0 `acceptance`/`gate`/`acceptanceRole` settings in 11 prompts + 4 agent definitions; 3 prompts require a `.provenance.md` sidecar (2 named in `AGENTS.md`); 8/11 lack a sidecar requirement.
- Upstream `reviewer` and `evidence-auditor` are read-only (`acceptanceRole: read-only`); Feynman's package-level `reviewer` shadows the former and drops its tool allowlist and role.
- Wave 3 isolation: child `cwd=/tmp/eval-clean`; zero grader/pilot references in 7/7 transcripts.
- No-hint control: 4 probes with generic wording in `/tmp/eval-clean-control`; 4/4 semantically correct, zero grader references.
- Adversarial review: independent `reviewer` pass; findings incorporated, including withdrawal of an uncontrolled 0.5.3 regression claim and correction of provenance and telemetry wording.
- Leakage audit: pilot p6 answer cites `ground_truth.json`; wave 2 p5/p7 transcripts reference the pilot tree.
- Official eval JSONL: q01 11/11, q04 11/11, q07 7/7, q10 15/15 identifiers valid.
- Checker defects: four revisions documented; score trajectory on wave 3 was 5/7 → 6/7 → 7/7, so 7/7 is in-sample.
- Artifact existence: final Markdown and this sidecar verified on disk after write.

## Notes and residual gaps

- The report's own behavioral result is n=1 per probe, one model, one day. It is a case study, not a benchmark.
- p2's secondary claims (α/β exponents; earliest arXiv phrase date) were not independently verified. Only the TabDPT title was checked.
- The reviewer's write-capable tool set is inferred from pi-subagents documentation and the capability listing; no reviewer run was exercised for that claim.
- Wave 3 leakage checks are string-based; semantic leakage cannot be excluded.
- Official eval results are from repo `main` at 0.5.69 / commit `1174429075`, not the installed 0.5.65.
- `/tmp/eval-clean` and `/tmp/feynman-eval-grader` are ephemeral; durable copies of wave 3 answers and all score files are under `experiments/eval-quality-probes/`.

## Repro anchors

- Fixtures/ground truth: `experiments/eval-quality-probes/{make_fixtures.py,ground_truth.json}`
- Final scorer: `experiments/eval-quality-probes/check_probes_final.py`
- Scores: `experiments/eval-quality-probes/scores/{pilot,wave2,wave3}.json`
- Wave 3 answers: `experiments/eval-quality-probes/wave3-runs/`
- No-hint control: `experiments/eval-quality-probes/control-runs/`, `control-scores.json`
- Workflows: `outputs/.plans/feynman-eval-quality-probes{,-v2,-v3}-workflow.js`
- Remote source snapshot: `experiments/eval-quality-probes/sources/`
- Repo commit: https://github.com/Companion-Inc/feynman/commit/1174429075
