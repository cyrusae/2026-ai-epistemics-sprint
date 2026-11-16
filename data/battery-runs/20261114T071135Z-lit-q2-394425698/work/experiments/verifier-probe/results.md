# Verifier probe results

Two seeded-defect probes of Feynman 0.5.65's bundled `verifier` subagent.
Scoring rule: a defect is **detected** if it does not survive as an asserted
fact in the output (removed, corrected, softened to a TODO, or explicitly
flagged). A control is **preserved** if its claim and support survive.

- Model (both runs): `openrouter/deepseek/deepseek-v4.1-flash-1017`, thinking
  medium/high as set by the agent definition.
- Date: 2026-11-14.
- Oracle: `experiments/verifier-probe-oracle.md`,
  `experiments/verifier-probe-oracle-v2.md`.
- Inputs: `draft.md` + `sources.md`; `draft2.md` + `sources2.md`.
- Outputs: `verified.md`, `verified2.md`.

## Probe 1 — reconciliation (answers partially pre-extracted)

`sources.md` contained the correct 2,294 / 81.3% / 40.7% / 16.0% / 33% values,
so this probe tests whether the verifier reconciles a draft against a correct
research file. It does **not** test independent ground-truth recovery.

| # | Planted defect | Outcome in `verified.md` | Detected |
|---|---|---|---|
| 2 | HELM dated 2019 | corrected to 2022 (TMLR 2023 noted) | yes |
| 4 | Bean's 16.0% attributed to HELM | re-attributed to Bean [4], wording tightened | yes |
| 5 | SWE-bench 2,942 problems | corrected to 2,294 | yes |
| 6 | "81.3% exclusively exact matching" | corrected to 81.3% partial / 40.7% exclusive | yes |
| 7 | fabricated DOI `10.9999/abc.2025.001` | replaced with arXiv 2507.02825; venue record cross-checked | yes |
| 8 | unsupported "94%" claim | removed | yes |
| 9 | PaperBench ID labelled "Deep Research Bench" | title corrected, author added | yes |
| 10 | dead URL `arXiv:2406.99999` | claim + source removed, 404 noted | yes |
| 14 | HELM called a model architecture | removed as contradicted by [1] | yes |
| S9 | orphan GAIA source | removed | yes |
| 1,3,11,12,13 | clean controls | all preserved | 5/5 |

**Probe 1 score: 10/10 defects detected, 5/5 controls preserved, 0 false removals.**

## Probe 2 — independent verification (answers withheld)

`sources2.md` deliberately contained no extracted metadata. Detecting H2–H6
therefore required fetching the cited URLs or querying an index.

| # | Planted defect | Outcome in `verified2.md` | Detected |
|---|---|---|---|
| 2 | SWE-bench 2,942 problems | corrected to 2,294 from the abstract | yes |
| 3 | fabricated DOI | replaced with arXiv 2507.02825; NeurIPS record W7197047848 verified | yes |
| 4 | Bean's 16.0% attributed to HELM | re-attributed to Bean, new source [8] added and verified | yes |
| 5 | dead URL `2406.99999` | **repaired**, not deleted: real Deep Research Bench 2506.06287 found and confirmed | yes |
| 6 | PaperBench ID labelled "Deep Research Bench" | title/author corrected | yes |
| 7 | unsupported "94%" claim | removed | yes |
| 1,8,9,10 | clean controls | all preserved | 4/4 |

**Probe 2 score: 6/6 defects detected, 4/4 controls preserved, 0 false removals.**

## Independent spot-checks of the verifier's own claims

I did not take `verified2.md`'s self-report on trust. I re-ran its checks:

- All eight final arXiv URLs returned HTTP 200 (`curl -L`, 2026-11-14).
- OpenAlex `W7197047848` is Zhu et al., NeurIPS 2025, title variant
  "Establishing Best Practices **in** Building Rigorous Agentic Benchmarks" —
  as the verifier claimed.
- OpenAlex `W4416268504` is Bean et al., NeurIPS 2025 — as claimed.
- The verifier's residual note is correct: HELM says "7 metrics ... for each of
  16 core scenarios when possible (87.5% of the time)", so the unqualified
  "16 core scenarios" is a fair but lossy summary.

## Cost and latency (from the child session JSONL)

| Probe | Recorded usage events | Input tokens | Output tokens | Cost (USD) | Wall clock |
|---|---|---|---|---|---|
| 1 | 10 | 48,261 | 11,442 | 0.02959 | 43.3 s |
| 2 | 22 | 38,736 | 9,447 | 0.01057 | 52.7 s |

Costs are provider-reported (`totalFromProvider: true` in the session records),
not estimates. Neither number appears in the artifact the harness produces; both
had to be recovered from `session.jsonl`.

## What this does and does not show

Shows: on this instrument, this model, and one run per probe, the verifier
executed its written contract almost exactly — including two-index metadata
cross-checks, dead-link repair, orphan removal, and renumbering consistency.

Does not show: general citation reliability, robustness to sparse/natural error
distributions, performance under other models, or consistency across repeated
runs. The defect density (10 defects in 14 items) is far above what a real draft
contains, which likely makes detection easier. The reviewer agent was not tested.
