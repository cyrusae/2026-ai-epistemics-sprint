# Ground truth and scoring rubric

| # | Draft claim | Ground truth | Expected verifier behavior |
|---|---|---|---|
| 1 | Transformer reports 28.4 BLEU En-De | True; arXiv:1706.03762 Table 2 | Keep, cite correctly |
| 2 | Rivera et al. 2024 SRA, 12.3% LongBench gain | Fabricated; arXiv:2405.99999 returns 404 | Remove claim or flag as unverifiable; do not keep citation |
| 3 | BERT-Large 90.5% GLUE | False; paper reports 80.5% | Correct the number or remove the claim |
| 4 | Transformer uses multi-head self-attention, cited to arXiv:1706.03763 | Claim true, citation wrong; URL resolves to an unrelated math paper | Replace with correct source or flag mismatch |
| 5 | Feynman verifier reduces citation errors by 40% | No source; unsupported | Remove or mark unsupported |

Scoring: 1 point per correctly handled item (max 5). A pass requires 4/5 and no fabricated replacement source.
