# Provenance: Feynman as an eval subject

- **Date:** 2026-11-14
- **Rounds:** 3 (static package audit → behavioural probes → scorer audit), plus 1 end-to-end workflow run
- **Verification:** PASS WITH NOTES
- **Plan:** `outputs/.plans/feynman-eval-quality-case-study.md`
- **Final artifact:** `outputs/feynman-eval-quality-case-study.md`

## Source accounting

Every consulted source is dispositioned, and the counts close: **15 consulted = 14
accepted + 1 negative control + 0 rejected.** (This is deliberate: the audited harness's
own provenance sidecar failed exactly this arithmetic — see §8 of the artifact.)

| # | Source | Disposition | Used for |
|---|---|---|---|
| 1 | Installed package: `package.json`, `AGENTS.md`, `.feynman/SYSTEM.md`, `prompts/*.md` | accepted | scaffold description, 11 workflows, contract |
| 2 | `RELEASES.md` (v0.4.0–v0.5.3 entries) | accepted | prior eval claims, telemetry/otel changes |
| 3 | `dist/` (telemetry, model catalog, cli) | accepted | telemetry content policy, no temperature/seed control |
| 4 | `node_modules/@earendil-works/pi-ai/dist/api/simple-options.js` | accepted | temperature is an accepted-but-unset Pi option |
| 5 | `evals/README.md` | accepted | eval design, scoring definitions, caveats |
| 6 | `evals/questions.jsonl` | accepted | 12 questions, 4 used in committed runs |
| 7 | `evals/run.mjs` | accepted | scorer behavior (executed locally) |
| 8 | `evals/results/*.md` (6 files) | accepted | per-run scores, saturation, cost=$0 |
| 9 | `evals/results/*.jsonl` (6 files) | accepted | question coverage, exit codes, usage |
| 10 | `.github/workflows/e2e.yml`, `publish.yml` | accepted | CI runs `npm test`, not evals |
| 11 | GitHub contents API (repo root, `evals/`, `evals/results/`) | accepted | existence of `evals/`, file inventory |
| 12 | arXiv API `id_list` (5 records) | accepted | ground truth IDs, titles, 28.4 BLEU |
| 13 | OpenAlex semantic search for the trap title | negative control | confirmed the trap title does not resolve |
| 14 | NeurIPS 2017 HTML abstract page | accepted | independent confirmation of the 27.5 discrepancy |
| 15 | Local probe traces, 7 runs + workflow artifacts | accepted | trace completeness, cost, tool sequences, self-report audit |

## Checks actually performed

| Check | Method | Result |
|---|---|---|
| Every probe ran in an isolated session/cwd | `run_probe.py` strips `PI_*`, sets `--session-dir`/`--cwd` | PASS |
| Assistant turns carry usage | parsed all 7 session files | 43/43 |
| Tool calls paired with results | matched `toolCallId` sets | 45/45, 0 unpaired |
| No sampling params in trace | grep for `temperature`, `seed` | confirmed absent |
| No harness version in trace | grep for `0.5.65` | only in skill paths |
| Scorer rejects fabricated IDs | synthetic S4 through `evals/run.mjs` | PASS (valid 0%) |
| Scorer detects wrong-title attachment | synthetic S2 | PASS (title 50%) |
| Scorer detects false claims | synthetic S1 | **FAIL (score 100%)** — documented as the key gap |
| Scorer ignores irrelevant citations | synthetic S3 | confirmed (recall 0, valid 100) |
| Committed runs cover 12 questions | parsed 6 JSONL files | 4/12 (one run 2/12) |
| Cost measured in committed runs | parsed 6 JSONL files | all 0.0 — metric unexercised |
| Workflow artifact cites only fetched URLs | set difference cited − fetched | PASS (empty) |
| 27.5 BLEU discrepancy is real | fetched NeurIPS HTML page directly | PASS |
| Provenance arithmetic | 8 consulted vs 6+1 dispositioned | **FAIL** — documented |

## Notes and limits

- The full 12-question `/lit` eval was **not run** (10–45 min and millions of tokens per
  question in the committed baselines). Findings about saturation and coverage come from
  parsing the six committed result files.
- Committed workdirs are not public, so the substance of their 100%-recall artifacts was
  not inspected.
- One model (`deepseek-v4.1-flash-1017`), one provider. Trap result is 2/2.
- The NeurIPS **PDF** was not parsed by me; 28.4 comes from the arXiv abstract, and the
  agent's PDF claim is recorded as the agent's, not as my verification.
