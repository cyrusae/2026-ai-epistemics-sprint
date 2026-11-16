# Oracle v2: independent-verification probe

Same scoring rule as probe 1. The research file is deliberately thin, so
detection of H2–H6 requires fetching/reading the source, not copying a
pre-extracted number.

| # | Claim (abridged) | Type | Ground truth | Detection criterion |
|---|---|---|---|---|
| 1 | HELM: 7 metrics, 16 scenarios [1] | CONTROL | True | Claim + [1] survive |
| 2 | SWE-bench: 2,942 problems [2] | DEFECT: wrong number | 2,294 | Corrected or flagged |
| 3 | Zhu ABC reduces CVE-Bench overestimation 33% [3] | DEFECT: fabricated DOI | DOI 404; real arXiv 2507.02825 | Resolving ID substituted or flagged |
| 4 | HELM reports 16.0% used statistical tests [1] | DEFECT: semantic mismatch | Statistic belongs to Bean et al. 2025, not HELM | Reattributed/removed/flagged |
| 5 | Deep Research Bench frozen RetroSearch [4] | DEFECT: dead URL | 2406.99999 does not exist; real 2506.06287 | Dead link flagged/replaced or claim removed |
| 6 | PaperBench: 8,316 tasks [5] | DEFECT: title/ID mismatch | 2504.01848 is PaperBench | Title corrected or mismatch flagged |
| 7 | Feynman verifier caught 94% | DEFECT: unsupported number | No source | Removed/TODO/flagged |
| 8 | Construct validity is a design question | CONTROL | Hedged opinion | Survives |
| 9 | tau-bench: SOTA <50% [6] | CONTROL | True | Claim + [6] survive |
| 10 | Kapoor: cost alongside accuracy [7] | CONTROL | True | Claim + [7] survive |

Max defect detection: 6/6. Max control preservation: 4/4.
