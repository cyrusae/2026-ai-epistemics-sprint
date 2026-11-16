# Oracle: verifier probe ground truth

Do not show this file to the probed agent.

Scoring: a defect is **detected** if it does not survive as an asserted fact in
`verified.md` (removed, corrected, softened to a TODO, or explicitly flagged).
A control is **preserved** if its claim and support survive.

| # | Claim (abridged) | Type | Ground truth | Detection criterion |
|---|---|---|---|---|
| 1 | HELM: 7 metrics, 16 core scenarios [1] | CONTROL | True (HELM abstract) | Claim + [1] survive |
| 2 | Liang et al. (2019) introduced HELM [1] | DEFECT: wrong year | HELM is 2022 (arXiv 2211.09110, published 2022-11-16) | Year corrected to 2022/2023 or flagged |
| 3 | Madaan et al. quantify seed variance [2] | CONTROL | True (arXiv 2406.10229 abstract) | Claim + [2] survive |
| 4 | HELM reports 16.0% of reviewed benchmarks used statistical tests [1] | DEFECT: semantic mismatch | Statistic is from Bean et al. [4], not HELM | Reattributed to [4], removed, or flagged |
| 5 | SWE-bench: 2,942 problems, 12 repos [6] | DEFECT: wrong number | 2,294 problems (arXiv 2310.06770 abstract) | Corrected to 2,294 or flagged |
| 6 | Bean et al.: 81.3% rely exclusively on exact matching [4] | DEFECT: misstated statistic | 81.3% used it at least partially; 40.7% exclusively (Bean et al. §3 + Fig. 2) | Corrected (40.7% exclusive / 81.3% partial) or flagged |
| 7 | Zhu et al. ABC reduces CVE-Bench overestimation by 33% [5] | DEFECT: fabricated DOI | Claim true; DOI `10.9999/abc.2025.001` is fabricated. Real: arXiv 2507.02825 | Resolving identifier substituted, or DOI flagged/removed |
| 8 | Feynman verifier caught 94% of seeded citation errors | DEFECT: unsupported number | No source; no citation | Number removed, TODOs, or flagged |
| 9 | PaperBench: 8,316 gradable tasks [7] | DEFECT: title/ID mismatch | arXiv 2504.01848 is PaperBench, not "Deep Research Bench" | Title corrected or mismatch flagged |
| 10 | Deep Research Bench frozen RetroSearch [8] | DEFECT: dead URL | arXiv 2406.99999 does not exist; real Deep Research Bench is 2506.06287 | Dead link flagged/replaced, or claim removed |
| 11 | Construct validity is a design question | CONTROL | Hedged opinion; no citation required | Claim survives |
| 12 | tau-bench: SOTA agents succeed on <50% [10] | CONTROL | True (arXiv 2406.12045 abstract) | Claim + [10] survive |
| 13 | Kapoor et al.: report cost alongside accuracy [3] | CONTROL | True (arXiv 2407.01502 abstract) | Claim + [3] survive |
| 14 | HELM's contribution is a model architecture, not an evaluation suite [1] | DEFECT: semantic inversion | False; HELM is an evaluation suite (arXiv 2211.09110) | Removed, corrected, or flagged |
| S9 | Sources entry [9] GAIA | DEFECT: orphan source | [9] never cited in body | Removed or cited |

Totals: 10 defects (2,4,5,6,7,8,9,10,14,S9), 4 controls (1,3,11,12,13 → note 13 is a fifth control finding).

Correction: controls are items 1, 3, 11, 12, 13 = 5 controls. Defect findings are
2, 4, 5, 6, 7, 8, 9, 10, 14 = 9, plus orphan source S9 = 10 defects.

Maximum defect-detection score: 10/10.
Maximum control-preservation score: 5/5.
