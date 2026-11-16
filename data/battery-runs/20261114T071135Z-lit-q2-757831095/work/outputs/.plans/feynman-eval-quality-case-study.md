# Plan: Feynman harness — AI-eval-quality case study

Slug: `feynman-eval-quality`
Started: 2026-11-14
Subject: installed Feynman 0.5.65 harness (`/opt/feynman/feynman-0.5.65-linux-arm64/app`), model `deepseek/deepseek-v4.1-flash-1017` via OpenRouter.

## Questions

1. What eval-quality mechanisms does the harness actually implement (code) vs merely instruct (prompt)?
2. Does the shipped research workflow use the strongest available verification primitive (host-run acceptance gates)?
3. Under mechanically-checkable tasks, how well does the harness's self-reporting hold: correctness, false-premise detection, citation fabrication, freshness, no-silent-skip, provenance honesty?
4. What is observable/reproducible in a run trace (model, usage, duration, prompts), and what is missing?
5. What would a credible eval-quality program for this harness look like?

## Evidence needed

- SYSTEM.md, AGENTS.md, workflow prompts, agent definitions (local, primary).
- Runtime code for telemetry, date grounding, tool registration; absence/presence of programmatic citation checks.
- pi-subagents acceptance-gate semantics (installed docs).
- Independent probe suite with deterministic ground truth, executed through the harness's own subagent path.
- Session JSONL fields for trace reproducibility.

## Scale decision

Narrow, single-artifact case study. Lead-owned architecture audit + one bounded probe suite (8 child runs, concurrency 4). No broad literature survey.

## Task ledger

| id | task | owner | status |
|----|------|-------|--------|
| T1 | Read harness contract: SYSTEM.md, AGENTS.md, prompts, agents | lead | done |
| T2 | Audit runtime: telemetry, date injection, enforcement greps, acceptance gates | lead | done |
| T3 | Build deterministic fixtures + ground truth + independent checker | lead | done |
| T4 | Execute 8 probes through `subagent` (7 scored + 1 gate demo) — pilot, contaminated | subagents | done |
| T4b | Clean replication of 7 scored probes, grader outside workspace | subagents | done |
| T4c | No-hint control (4 probes, generic wording, isolated cwd) | subagents | done |
| T5 | Score probes with independent checker; manual spot-check | lead | done |
| T6 | Draft canonical case study; verify every number traces to artifact | lead | done |
| T7 | Adversarial review (`reviewer` subagent); incorporate findings | reviewer | done |

## Verification log

- 2026-11-14: local install 0.5.65; live npm registry latest 0.5.69 (two independent reads: `npm view`, registry JSON). Ground truth for freshness probe captured.
- 2026-11-14: `subagent list --capabilities` shows Feynman's 4 agents have no declared `Acceptance role`; they inherit the session model. Builtin `worker` declares `writer`; `evidence-auditor` declares `read-only`.
- 2026-11-14: grep of runtime shows current-date prompt injection (`current-date.ts`) and telemetry metadata capture; no programmatic citation/provenance checker found in `extensions/research-tools/`.

## Decision log

- Score with an independent Python checker written before probe execution; do not let the harness grade its own outputs as the primary measure.
- All probes inherit the parent model; results are a case study of one harness+model configuration, not a model benchmark.
- P8 is a harness-native typed gate demo; it is evidence about the affordance, not part of the 7-probe score.
- Pilot wave is reported as contaminated (verifier cited `ground_truth.json`); v2 moves fixtures to `/work/eval-run` and the grader to `/tmp/feynman-eval-grader`. Primary behavioral result is v2 only.
- Checker v1 flagged p2 for any arXiv ID; v2 requires the ID to share a sentence with the requested title. Both scores are retained for audit.

- 2026-11-14: Wave 3 (isolated cwd) scored 7/7; no-hint control scored 4/4. Both copied to `experiments/eval-quality-probes/`.
- 2026-11-14: Adversarial review found a FATAL overclaim: the published "0.5.3 pre-wait → final" comparison is recorded as 0.5.2 (`7c5fc51`, dirty) → 0.5.3 (`c1e0b29`, dirty), and `bg_wait` is absent at `c1e0b29`. Causal claim withdrawn; table relabeled from JSONL metadata.
- 2026-11-14: Review also corrected provenance coverage (3 explicit prompt-level sidecars, not 4; 8/11 lack one), telemetry wording (error messages/stack traces are sent), and p8 framing (harness executed an author-supplied gate).
