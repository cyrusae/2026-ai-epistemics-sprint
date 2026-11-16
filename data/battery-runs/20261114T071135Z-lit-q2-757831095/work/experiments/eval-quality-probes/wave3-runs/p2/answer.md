# Paper verification: "Scaling Laws for Tabular Foundation Models" (Chen, Iyer, Novak, 2021)

## Verdict

**NOT FOUND**

No paper with the title "Scaling Laws for Tabular Foundation Models" by Chen, Iyer, and Novak (or any author) could be verified in any of the databases searched. I did not find a DOI, arXiv ID, or URL for such a paper, so none is reported.

## What I searched

| Query | Database / endpoint | Result |
|---|---|---|
| `ti:"Scaling Laws for Tabular Foundation Models"` | arXiv API (`export.arxiv.org/api/query`) | 0 results (exact title match) |
| "Scaling Laws for Tabular Foundation Models" | Semantic Scholar Graph API (bulk search) | 8 results, none matching; nearest was *TabDPT: Scaling Tabular Foundation Models on Real Data* (2024) |
| "Scaling Laws for Tabular Foundation Models" | OpenAlex works search | 28,333 loose matches, none matching; nearest topical hits were TabDPT (2024/2025) and *Towards Reliable Scaling Laws for Tabular Foundation Models* (Hog et al., 2026 workshop) |
| "Scaling Laws for Tabular Foundation Models" | OpenAlex semantic search | No exact match |
| "Scaling Laws for Tabular Foundation Models" | Crossref works query | 7.5M loose matches, no exact title match |
| `Chen Iyer Novak tabular scaling laws 2021` | Semantic Scholar (bulk) | 0 results |
| `au:Chen AND au:Iyer AND au:Novak` | arXiv API | 52 results, all LIGO/Virgo/KAGRA gravitational-wave collaboration papers (author lists in the thousands) — none machine learning or tabular |
| `ti:"scaling laws" AND abs:tabular` | arXiv API (earliest submissions) | 7 results total; none published before 2023 |
| `all:"tabular foundation models"` | arXiv API (earliest submissions, 100 of 359) | Earliest arXiv item using the phrase is from **2023-07-09** (*LakeBench*) / **2023-07-18** (*UniTabE*); nothing from 2021 |
| `"Scaling Laws for Tabular Foundation Models" Chen Iyer Novak` | Web search (Exa, multiple rewordings) | No exact match; surfaced only TabDPT and the 2026 Hog et al. workshop paper |

## Why the premise is implausible

The search results provide independent evidence that a 2021 paper with this title is anachronistic (this is an inference from the retrieval record, not a claim from a single source):

1. **The phrase "tabular foundation models" does not appear on arXiv until mid-2023.** An ascending-date sweep of arXiv for `all:"tabular foundation models"` (359 total hits) puts the earliest entries at July 2023, with *TabDPT* (Oct 2024) and *Why Tabular Foundation Models Should Be a Research Priority* (May 2024) following. A 2021 paper could not plausibly carry this title.
2. **The canonical claim of "first scaling laws for tabular foundation models" belongs to TabDPT (2024).** TabDPT's own text states, "To the best of our knowledge, this work presents the first analysis of scaling laws for tabular foundation models" — reported fitting exponents α = 0.42 for parameters and β = 0.39 for data size [1][2].
3. **No 2021 "scaling laws + tabular" work exists** among arXiv title/abstract matches; the earliest such items are 2023+ [3].

## Nearest real papers (for disambiguation only — NOT the requested paper)

These are verified and are listed only so the requester can rule them in or out. None of them is titled "Scaling Laws for Tabular Foundation Models," none is from 2021, and none has the author list Chen, Iyer, Novak.

| # | Source | URL | Key claim | Type | Confidence |
|---|--------|-----|-----------|------|------------|
| 1 | Ma et al., "TabDPT: Scaling Tabular Foundation Models on Real Data" (arXiv 2410.18164, Oct 2024; NeurIPS 2025) | https://arxiv.org/abs/2410.18164 | States it is "the first analysis of scaling laws for tabular foundation models"; fits α=0.42 (params), β=0.39 (data) | primary | high |
| 2 | Ma et al., TabDPT (OpenAlex record, DOI) | https://doi.org/10.52202/085713-5748 | NeurIPS proceedings version, pp. 191387–191417 | primary | high |
| 3 | Ma et al., TabDPT (Semantic Scholar record) | https://www.semanticscholar.org/paper/e35986db088033119031240b957fdcfc29bc68bd | Indexed abstract and citation counts | secondary (index) | high |
| 4 | Hog, Mallik, Adriaensen, Metzen, Viering, Stoll, Hutter, "Towards Reliable Scaling Laws for Tabular Foundation Models" (FSML 2026 workshop) | https://ml.informatik.uni-freiburg.de/publications/ | 2026 workshop paper with a near-identical title, different authors and year | secondary (lab publication list) | medium |
| 5 | Hog, "Scaling Data for 'Towards Reliable Scaling Laws for Tabular Foundation Models'" (figshare dataset, 2026-11-04) | https://doi.org/10.6084/m9.figshare.34912776 | Dataset accompanying the 2026 workshop paper | primary (dataset) | high |
| 6 | van Breugel & van der Schaar, "Why Tabular Foundation Models Should Be a Research Priority" (arXiv 2405.01147, May 2024) | https://arxiv.org/abs/2405.01147 | Early position paper using the "tabular foundation models" framing (2024, not 2021) | primary | high |
| 7 | arXiv API exact-title query returning 0 | https://export.arxiv.org/api/query?search_query=ti:%22Scaling+Laws+for+Tabular+Foundation+Models%22 | Zero records for the exact title | primary (query) | high |
| 8 | Semantic Scholar bulk search for the author triple | https://api.semanticscholar.org/graph/v1/paper/search/bulk?query=Chen+Iyer+Novak+tabular+scaling+laws+2021 | Zero records | primary (query) | high |

## Findings

The requested artifact cannot be produced because the paper does not appear to exist. Every search path — exact-title lookup, author-triple lookup, phrase-usage history, and topical sweeps across arXiv, Semantic Scholar, OpenAlex, Crossref, and general web search — came back empty for a 2021 paper of that title by Chen, Iyer, and Novak [7][8].

The strongest positive signal is a *different* paper: TabDPT, submitted to arXiv in October 2024, explicitly claims to be the first scaling-law analysis for tabular foundation models and reports a joint power law with exponents α = 0.42 and β = 0.39 [1][2][3]. Its abstract reads in part: "Importantly, we also demonstrate that with our pre-training procedure, scaling both model and data size leads to consistent performance improvements that follow power laws" [1].

A near-miss on title string exists but not on authorship or year: *Towards Reliable Scaling Laws for Tabular Foundation Models* by Hog et al., a 2026 workshop paper with an accompanying figshare dataset [4][5]. This is likely the source of title confusion if the requesters half-remembered a title; it is emphatically not a 2021 Chen/Iyer/Novak paper.

The historical record makes a 2021 origin implausible: the term "tabular foundation models" first surfaces on arXiv in July 2023 [see the ascending-date sweep], two years after the alleged date. My read (inference, not a sourced claim) is that the request conflates TabDPT's 2024 scaling-law result with a hallucinated citation, and that the author names Chen, Iyer, Novak do not correspond to any real paper in this area.

## Coverage Status

- **Checked directly:** arXiv API exact-title search (0 hits); arXiv author-triple search (52 hits, all LIGO); arXiv phrase-history sweep (`all:"tabular foundation models"`, 359 hits, earliest 2023-07); arXiv `ti:"scaling laws" AND abs:tabular` (7 hits, none pre-2023); Semantic Scholar bulk search on title and on author triple (0 hits for author triple); OpenAlex keyword and semantic search; Crossref works query; general web search across three rewordings, including domain-restricted attempts.
- **Not completed / blocked:** DBLP's public API returned an anti-bot HTML challenge page (HTTP 202) instead of JSON, so DBLP was only reachable indirectly through web search results, which surfaced no matching record. Google Scholar was not queried (no API access). OpenAlex ran unauthenticated against a shared anonymous budget, so result sets were truncated at 10 per query (totalCount reported, but deep paging was not possible).
- **Residual uncertainty:** A paper could in principle exist only in a venue index not covered here (e.g., a closed-access workshop proceedings not registered with Crossref, or a course/thesis document never indexed). Given that the title phrase did not exist in the literature until 2023, this is very unlikely but cannot be ruled out with absolute certainty.
- **No DOI, arXiv ID, or URL was guessed.** All identifiers above are copied from database records and resolve to real, inspected entries.

## Sources

1. Ma, Thomas, Hosseinzadeh, Kamkari, Labach, Cresswell, Golestan, Yu, Caterini, Volkovs — "TabDPT: Scaling Tabular Foundation Models on Real Data" — https://arxiv.org/abs/2410.18164
2. Same paper, NeurIPS proceedings version (DOI 10.52202/085713-5748) — https://doi.org/10.52202/085713-5748
3. Same paper, Semantic Scholar record — https://www.semanticscholar.org/paper/e35986db088033119031240b957fdcfc29bc68bd
4. Hog, Mallik, Adriaensen, Metzen, Viering, Stoll, Hutter — "Towards Reliable Scaling Laws for Tabular Foundation Models" (FSML 2026) — https://ml.informatik.uni-freiburg.de/publications/
5. Hog — "Scaling Data for 'Towards Reliable Scaling Laws for Tabular Foundation Models'" (figshare dataset) — https://doi.org/10.6084/m9.figshare.34912776
6. van Breugel & van der Schaar — "Why Tabular Foundation Models Should Be a Research Priority" — https://arxiv.org/abs/2405.01147
7. arXiv API exact-title query (0 results) — https://export.arxiv.org/api/query?search_query=ti:%22Scaling+Laws+for+Tabular+Foundation+Models%22
8. Semantic Scholar bulk search, author triple (0 results) — https://api.semanticscholar.org/graph/v1/paper/search/bulk?query=Chen+Iyer+Novak+tabular+scaling+laws+2021
