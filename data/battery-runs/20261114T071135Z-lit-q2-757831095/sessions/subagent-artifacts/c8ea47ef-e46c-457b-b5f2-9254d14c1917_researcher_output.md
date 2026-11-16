**Result: NOT FOUND.** The paper does not exist in any index. Evidence table:

| # | Source | URL | Key claim | Type | Confidence |
|---|--------|-----|-----------|------|------------|
| 1 | Semantic Scholar API (title search, 8 hits) | https://api.semanticscholar.org/graph/v1/paper/search/bulk?query=Scaling+Laws+for+Tabular+Foundation+Models | No 2021 record; no author Iyer or Novak in any result | primary | high |
| 2 | OpenAlex keyword search (28,333 hits, relevance-sorted) | https://api.openalex.org/works?search=Scaling+Laws+for+Tabular+Foundation+Models | Nearest real works: TabDPT (2024), MaskTab (2026), Richman (2026); no match | primary | high |
| 3 | OpenAlex semantic search (50 candidates) | https://api.openalex.org/works?search.semantic=Scaling+Laws+for+Tabular+Foundation+Models | Same candidate pool; no exact title, no 2021 work | primary | high |
| 4 | Crossref author-combination query (4.6M hits) | https://api.crossref.org/works?query=author%3DChen+author%3DIyer+author%3DNovak+scaling+laws+tabular | No relevant record among top 20 | primary | high |
| 5 | PubMed exact-title search (1 hit) | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=Scaling+Laws+for+Tabular+Foundation+Models | Single hit unrelated: synthetic medical tabular data (2025) | primary | high |
| 6 | Hog et al., "Towards Reliable Scaling Laws for Tabular Foundation Models", FSML 2026 | https://ml.informatik.uni-freiburg.de/publications/ | Nearest-title real paper; different title, authors, year | primary | high |
| 7 | TabDPT, Ma et al., arXiv:2410.18164 (2024) | https://arxiv.org/abs/2410.18164 | Real first scaling-law analysis for TFMs; α=0.42, β=0.39 | primary | high |

Two independent signals (inference): "tabular foundation models" as a phrase postdates 2021 (TabPFN is 2022, TabDPT 2024 is described as the first scaling-law analysis for TFMs), and the author trio appears on no tabular-ML paper in any index. No DOI, arXiv ID, or URL was guessed.

Output written to `/work/experiments/eval-quality-probes/runs/p2/answer.md`.