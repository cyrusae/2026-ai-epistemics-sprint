# Provenance: Feynman harness AI-eval-quality case study

- **Date:** 2026-11-14
- **Harness:** Feynman 0.5.65 (`/opt/feynman/feynman-0.5.65-linux-arm64/app`), Node v24.21.0
- **Session model:** `openrouter/deepseek/deepseek-v4.1-flash-1017`
- **Workflow:** direct investigation with two bounded experiments (no full `/lit` or `/deepresearch` run)
- **Verification:** PASS WITH NOTES

## Sources consulted

| # | Source | Type | Used for |
|---|---|---|---|
| 1 | Installed harness: `.feynman/SYSTEM.md`, `.feynman/agents/*.md`, `prompts/*.md`, `package.json`, `RELEASES.md` | primary local artifact | Operating contract, verification architecture, release claims |
| 2 | `github.com/Companion-Inc/feynman` `evals/README.md`, `evals/questions.jsonl`, `evals/run.mjs` | primary public artifact | Eval design and scorer implementation |
| 3 | `evals/results/` six result pairs (2026-09-23/24) | primary public artifact | Coverage, dirty-tree, cost, model, version-label audit |
| 4 | arXiv abstracts 2408.03314, 2211.17192, 1706.03762 | primary source | Checking the verifier's replacement numbers and control citation |
| 5 | Canary experiment `experiments/feynman-eval-audit/` | raw experiment | Scorer sensitivity/specificity |
| 6 | Verifier canary `experiments/feynman-verifier-canary/` | raw experiment | Verifier contract smoke test |

## Checks performed

1. **Installed-version and package inspection.** Confirmed `0.5.65`, `evals/` absent from the installed package and from `package.json` `files`.
2. **Public eval inventory.** Parsed all six result JSONL files: 22 question rows, 6 result files, IDs only q01/q04/q07/q10 (4 of 12 = 33.3%).
3. **Dirty-tree audit.** 14/14 non-baseline rows have `git_dirty: true`; 8 baseline rows are clean.
4. **Cost audit.** All 22 rows report `cost_usd: 0` because the eval `models.json` has no cost block.
5. **Scorer canary suite.** Built 12 synthetic defect documents plus one verifier-corrected document; ran the unmodified `evals/run.mjs --rescore`. Results in `experiments/feynman-eval-audit/seed.jsonl`. Caught c1/c2/c10; missed c3/c4/c5/c6/c8/c11; false-positive c7; disclosure penalty c12.
6. **Verifier canary.** Ran the harness `verifier` agent on a six-claim draft. Five seeded defects addressed, control preserved. Run metadata: `deepseek-v4.1-flash:medium`, 59,718 input / 6,414 output / 62,464 cache-read tokens, 8 turns, 13 tool calls, 72.4s, `$0.0085`.
7. **Replacement-number check.** Confirmed against the arXiv abstract for 2408.03314: "more than 4x compared to a best-of-N baseline" and "outperform a 14x larger model" in a FLOPs-matched evaluation. Confirmed 2x–3x T5-XXL in the 2211.17192 abstract.
8. **Release-note traceability.** v0.5.3's 44/44 claim matches the committed 0.5.3 result file. The "0.5.2: 43/43, 9–14 min" claim matches the file recorded as 0.5.0 (`d926547`), not the 0.5.2-labelled pre-wait files.

## Verification status by claim class

| Claim class | Status | Note |
|---|---|---|
| Installed harness contents and architecture | verified | Direct file reads |
| Public eval design and metric implementation | verified | Read `run.mjs` and reproduced the scorer behavior |
| Result-file coverage, dirty flags, cost, versions | verified | Parsed JSONL |
| Scorer canary outcomes | verified | Reproduced with the shipped `--rescore` path |
| Verifier canary outcomes | verified for this run | n = 1; not a catch-rate estimate |
| Verifier replacement numbers | verified | arXiv abstracts |
| Real-world `/lit` hallucination rate | not measured | No labeled sample; no full workflow run |
| Authors' retained workdirs | not accessed | Not shipped; `workdir` paths are on the author's machine |
| Eval state after 2026-09-24 | unverified | Public ledger has no later result file; private runs may exist |

## Blocked / not run

- Full `/lit` and `/deepresearch` runs: not run (cost/time; not needed for the scorer audit).
- Eval `--workflow deepresearch` lane: not run.
- Reviewer canary: not run.
- Human-labeled claim-support sample: not built.
- `ScholarQA-CS2`, `DeepResearch Bench FACT`, `SciCoQA` lanes: not built upstream (README says so).

## Artifacts

- `outputs/feynman-harness-eval-quality.md` — canonical case study.
- `notes/feynman-evals/` — downloaded eval files and six result pairs.
- `experiments/feynman-eval-audit/make_canaries.py` — canary generator.
- `experiments/feynman-eval-audit/seed.jsonl` — scored canary output.
- `experiments/feynman-eval-audit/rescore-stdout.txt` — scorer console output.
- `experiments/feynman-verifier-canary/draft.md` — seeded draft.
- `experiments/feynman-verifier-canary/research-notes.md` — supplied evidence.
- `experiments/feynman-verifier-canary/cited.md` — verifier output.
- `experiments/feynman-verifier-canary/verification-log.md` — per-claim verifier log.

## Notes

- The `arXiv:2499.99999` identifier in the canaries is deliberately fabricated and is not a source. It appears in the case study only as a test fixture.
- `git_dirty` is recorded metadata, not proof that a run's content differed from a clean tree.
- The verifier canary's research notes pre-flagged two defects as unverified, which made the task easier than a real report. This is stated in the case study.
