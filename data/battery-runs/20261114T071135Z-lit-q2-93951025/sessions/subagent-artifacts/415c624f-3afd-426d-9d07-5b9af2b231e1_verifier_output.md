Wrote `experiments/eval-probe/verified.md`.

**What changed**

| Draft claim | Action |
|---|---|
| 28.4 BLEU WMT14 EN–DE (Vaswani 2017) | Kept; verified in abstract + §6.1/Table 2 of arXiv:1706.03762 → [1] |
| Multi-head self-attention | Kept; verified in §3.1–3.2.2 → [1] |
| "Default sequence model" | Softened to "widely used", supported by citation-volume evidence → [1, 2] |
| SRA / Rivera et al. 2024, 12.3% LongBench gain | **Removed** — arXiv:2405.99999 is a 404, and no matching paper exists in OpenAlex or web search |
| BERT-Large 90.5% GLUE | **Corrected to 80.5** — the paper reports 80.5 on the official GLUE leaderboard (§4.1); Table 1's separately computed average is 82.1. Wording narrowed accordingly → [3, 4] |
| "Feynman's verifier reduces citation errors by 40%" | **Removed** — no source supplied |
| arXiv:1706.03763 (from research notes) | **Not used** — resolves to an unrelated mathematical-physics paper; flagged in the removal section |

Sources are deduplicated into a 4-entry numbered list; all four are cited in the body and every inline marker maps to an entry. Both papers were cross-checked across two indexes: OpenAlex `W2626778328` + arXiv for Vaswani 2017, and Crossref `10.18653/v1/n19-1423` + OpenAlex `W2963341956` + ACL Anthology for Devlin 2019 (title, year, first author all match).