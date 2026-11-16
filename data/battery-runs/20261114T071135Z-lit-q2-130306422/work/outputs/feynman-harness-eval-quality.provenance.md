# Provenance — feynman-harness-eval-quality

- **Date:** 2026-11-14
- **Canonical output:** `outputs/feynman-harness-eval-quality.md`
- **Workflow:** ad hoc case study (not a `/lit` or `/deepresearch` run), executed inside Feynman 0.5.65.

## Sources consulted vs accepted

| Source | Role | Status |
|---|---|---|
| `Companion-Inc/feynman@1174429` (GitHub) | Primary source for eval code, questions, results, prompts, tests, history | Accepted; commit-pinned |
| `evals/README.md`, `evals/run.mjs`, `evals/questions.jsonl` | Eval design and scorer behavior | Accepted; read in full |
| `evals/results/*.jsonl` (6 files, 22 rows) | Committed eval claims, metadata, usage, failures | Accepted; recomputed |
| `RELEASES.md` v0.5.3 | Public claim under audit | Accepted; checked against rows |
| `prompts/lit.md`, `.feynman/agents/*.md`, `.feynman/SYSTEM.md` | Workflow/verifier contracts | Accepted; read |
| `tests/*.test.ts`, `.github/workflows/*` | Test/CI coverage of eval | Accepted; grep counts |
| `feynman --version`, `feynman status`, `node_modules/*/package.json` | Installed-runtime facts | Accepted; command output |
| Bean et al. 2025 (arXiv:2511.04703), Onweller et al. 2026 (arXiv:2605.06635), Coelho et al. 2025 (arXiv:2505.19253) | Evaluation-methodology context | Accepted for framing; not used for quantitative claims |
| Ferrylane gateway / GPT-5.6 Terra / Claude runs | Original model behavior | **Not reproduced**; no gateway access in this session |
| Nine-paper search benchmark | "7 of 9 vs 2 of 9" release claim | Inputs are in `evals/questions.jsonl` (q01–q06, 9 key papers); the comparison result artifact is **unverified/missing** |

## Verification status

- **Verified by command/read:** installed versions; eval file counts; question/key-paper counts; result-row counts; dirty-row count; zero-cost count; git history counts; test/CI grep counts; one-shot CLI artifact write.
- **Recomputed from committed rows:** 4/4 completion, 44 distinct identifiers, all `citation_validity` and `title_match` values, wall times, 43-citation baseline, 14/22 dirty rows, $0 cost rows.
- **Reproduced experimentally:** eight synthetic fixtures scored with the repo's actual `--rescore` path; raw output in `experiments/feynman-eval-audit/`.
- **Not run:** full `/lit` or `/deepresearch` end-to-end; human rater study; independent rescoring of the committed 0.5.3 artifacts (artifacts are not in the repo).
- **Judgment:** scorecard ratings, "construct validity" critique, contamination concern, and recommendations.
- **Adversarial review:** two independent `reviewer` subagent passes checked the draft's numbers against the pinned clone; findings are in `notes/feynman-eval-quality-review.md` and `notes/feynman-eval-quality-review-2.md`. Corrections made after review: decomposed the 110-commit count into 46 four-path + 63 package-only + 1 SYSTEM-only commit; added the network-dependent `valid` denominator caveat and the pre-wait manual re-score; isolated the bare-ID fixture from the exact-title signal; added case ids and sorted fixture rows; corrected the search-benchmark row to distinguish inputs from the missing comparison artifact; clarified six dirty 0.5.3 rows; matched the probe command to the recorded invocation.

## Intermediate artifacts

- `experiments/feynman-eval-audit/README.md`
- `experiments/feynman-eval-audit/make_fixtures.py`
- `experiments/feynman-eval-audit/fixtures.jsonl`
- `experiments/feynman-eval-audit/fixtures.md`
- `experiments/feynman-eval-audit/rescore.log`
- `experiments/feynman-eval-audit/git-stats.txt`
- `experiments/feynman-eval-audit/release-claim-check.txt`
- `experiments/feynman-harness-probe/probe.log`
- `experiments/feynman-harness-probe/probe-result.txt`
- `notes/feynman-eval-quality-review.md`
- `notes/feynman-eval-quality-review-2.md`
- `experiments/feynman-eval-audit/verification.txt`

## Notes

- The report is self-referential: the auditor is the harness under audit. Quantitative claims trace to the files above; qualitative ratings do not have an independent rater.
- No secrets, provider keys, or private research content are included. The session model string and public repository URLs only.
