# Evidence brief: "Sublinear Preference Collapse in RLHF Reward Models" (Kessler & Mbeki, ICML 2024)

**Requested by:** parent agent
**Prepared:** 2026-11-14
**Status:** ⚠️ **SOURCE NOT FOUND — citation appears to be fabricated or badly garbled.** The four requested items (method, headline result, experimental setup, direct link) **cannot be supplied**, because no such paper could be located in any index. Details and negative evidence below.

---

## TL;DR

I could not verify that this paper exists, and the evidence against it is strong and convergent:

- The **ICML 2024 proceedings** (PMLR v235, 2,610 papers) contain **no paper with "Kessler" or "Mbeki" anywhere in the author list**, and no title containing "preference collapse" or "sublinear preference collapse."
- **arXiv has zero records matching `all:Mbeki`** (a sanity check on the same endpoint returns hits for `all:Kessler`, so the query mechanism works).
- **OpenAlex title search returns a count of 0** for `title.search:sublinear preference collapse`.
- Neither author has any ML/RLHF footprint. The 42 OpenAlex authors surnamed "Mbeki" are in economics, public health, and African studies; none in machine learning.
- No web search, Crossref query, or Semantic Scholar/OpenAlex search surfaced the title, the author pair, or the phrase "sublinear preference collapse" in any form.

**I will not write a method summary, quantitative result, or experimental setup for a paper I cannot read.** Doing so would mean inventing content. The requested fields are marked `NOT AVAILABLE` below, with the closest genuine research clearly separated.

---

## Requested deliverables — status

| Requested item | Status | Reason |
|---|---|---|
| Core method (3–5 sentences) | **NOT AVAILABLE** | No retrievable source. Any description would be fabricated. |
| Headline quantitative result + benchmark + baseline | **NOT AVAILABLE** | No retrievable source; no benchmark, dataset, or baseline is named anywhere. |
| Experimental setup (models, datasets, compute) | **NOT AVAILABLE** | No retrievable source. |
| Direct link to the paper | **NOT AVAILABLE** | No DOI, arXiv ID, PMLR URL, or OpenReview URL exists to link to. |

---

## Search protocol actually executed (2026-11-14)

Each check below was run directly; results are recorded in the evidence table.

1. **ICML 2024 official proceedings index** — fetched `https://proceedings.mlr.press/v235/` (2.55 MB HTML) and parsed it. Confirmed it is the real ICML 2024 proceedings (header: "Proceedings of the 41st International Conference on Machine Learning, Vienna, 21–27 July 2024, Volume 235") [1].
   - `grep` for `Kessler` → **0 matches**
   - `grep` for `Mbeki` → **0 matches**
   - Titles containing "collapse" → 10 matches, all neural-collapse / model-collapse / criterion-collapse papers; **none** about preference collapse in reward models.
   - Titles containing "Reward" → 32 matches, none matching the requested title.
2. **arXiv API** — `all:Mbeki` → `opensearch:totalResults = 0` [2]. Sanity check `all:Kessler` on the same endpoint returned results, so the zero is a real zero, not a broken query.
3. **arXiv title search** — `ti:"preference collapse"` returned only 3 papers, none by Kessler/Mbeki and none with this title [3].
4. **arXiv abstract search** — `abs:"sublinear" AND abs:"reward model"` returned contextual-bandit and decision-making papers, none on preference collapse [4].
5. **OpenAlex title search** — `filter=title.search:sublinear preference collapse` → `meta.count = 0` [5].
6. **OpenAlex author search** — `search=Mbeki` → 42 authors, all in economics / public health / African studies / other fields; **no ML researcher** [6].
7. **Crossref bibliographic query** — top 5 relevance results were unrelated RLHF/preference papers; no title or author match [7].
8. **Web search (Exa), 4+ query variants** — including the exact quoted title, the author pair, and `site:proceedings.mlr.press "preference collapse"`. Every "preference collapse" hit resolved to *Xiao et al.*, a different paper with a different author list [8][9].
9. **DBLP** — attempted; blocked by an anti-bot interstitial. Marked **blocked**, not "no result" [10].

---

## Evidence table

| # | Source | URL | Key claim / finding | Type | Confidence |
|---|--------|-----|---------------------|------|------------|
| 1 | PMLR, *Proceedings of the 41st ICML* (Vol. 235), full index | https://proceedings.mlr.press/v235/ | Full ICML 2024 main-conference index (2,610 titles). Zero occurrences of "Kessler", "Mbeki", or a matching title. | primary | high |
| 2 | arXiv API, `search_query=all:Mbeki` | https://export.arxiv.org/api/query?search_query=all:Mbeki | `totalResults = 0`. No arXiv record anywhere with this name. | primary | high |
| 3 | arXiv API, `search_query=ti:"preference collapse"` | https://export.arxiv.org/api/query?search_query=ti:%22preference+collapse%22 | 3 hits, none matching title or authors. | primary | high |
| 4 | arXiv API, `abs:"sublinear" AND abs:"reward model"` | https://export.arxiv.org/api/query?search_query=abs:%22sublinear%22+AND+abs:%22reward%20model%22 | No paper combining sublinearity with preference collapse in reward models. | primary | high |
| 5 | OpenAlex Works API, `title.search:sublinear preference collapse` | https://api.openalex.org/works?filter=title.search:sublinear%20preference%20collapse | `meta.count = 0` — no work in OpenAlex has this title. | primary | high |
| 6 | OpenAlex Authors API, `search=Mbeki` | https://api.openalex.org/authors?search=Mbeki | 42 authors; none in ML/RLHF. No plausible "T. Mbeki" ML author. | primary | high |
| 7 | Crossref Works API, bibliographic query | https://api.crossref.org/works?query.bibliographic=Sublinear+Preference+Collapse+in+RLHF+Reward+Models | No DOI matches title or author pair. | primary | high |
| 8 | Song, Cai, Lee, Su — *Reward Collapse in Aligning Large Language Models* (arXiv:2305.17608) | https://arxiv.org/abs/2305.17608 | Real paper documenting **reward collapse** (prompt-independent reward distribution in terminal training); prompt-aware utility fix. Different authors, different title. Read abstract directly. | primary | high |
| 9 | Xiao, Li, Xie, Getzen, Fang, Long, Su — *On the Algorithmic Bias of Aligning LLMs with RLHF: Preference Collapse and Matching Regularization* (arXiv:2405.16455; JASA 2025) | https://arxiv.org/abs/2405.16455 | Real paper coining **preference collapse**; PM-RLHF; 29%/41% preference-matching-divergence improvements on Llama-2-7B / OPT-1.3B. Different authors, different title. Read full text directly. | primary | high |
| 10 | DBLP publication/author search | https://dblp.org/search/publ/api?q=Mbeki | Blocked by anti-bot challenge page; no data retrieved. | primary (blocked) | n/a |

*(Supplementary real ICML 2024 reward-model papers verified present in [1]: "WARM: On the Benefits of Weight Averaged Reward Models", "ODIN: Disentangled Reward Mitigates Hacking in RLHF", "Reward Model Learning vs. Direct Policy Optimization". None is the requested paper.)*

---

## Findings

### 1. The paper does not appear to exist

The requested citation fails every independent existence check. The strongest single piece of evidence is the official ICML 2024 proceedings index [1]: all 2,610 main-conference papers are listed on one page, and the strings "Kessler" and "Mbeki" do not occur anywhere in it, nor does any title resembling "Sublinear Preference Collapse in RLHF Reward Models." A main-conference ICML paper would necessarily appear there.

The second-strongest is the arXiv result [2]. `all:Mbeki` returns **exactly zero** records. Because the identical query pattern returns hits for `all:Kessler`, this is a verified zero rather than a malformed query. Combined with the zero OpenAlex title count [5] and the absence of any Crossref DOI [7], the paper has no bibliographic footprint in any of the four major indexes that would host it.

*Inference (labeled):* the combination of a plausible-sounding but non-existent title, two author surnames with no ML publication record, and a top-tier venue is the characteristic signature of a **fabricated or model-hallucinated citation**, not of an obscure or hard-to-find paper. An obscure real paper would still leave an arXiv, OpenAlex, or Crossref trace.

### 2. The phrase "sublinear preference collapse" appears to have no referent

Not only the title but the central concept is unattested. OpenAlex title search for the phrase returns 0 [5]; arXiv abstract search combining "sublinear" with "reward model" returns only bandit/decision-theory work [4]; and web search for the exact quoted phrase returned no matching document. By contrast, the related but distinct terms **"reward collapse"** and **"preference collapse"** are both well attested in real, readable papers [8][9]. This suggests the citation may be a **conflation of two genuine papers** (see §4) with an invented "sublinear" modifier.

### 3. What I deliberately did not do

I did not reconstruct a method, dataset list, compute budget, or headline number from the title. There is no basis for any such claim. In particular, no benchmark, baseline, model family, dataset, or compute figure is associated with this citation anywhere I searched, so **any specific number attributed to this paper should be treated as unsupported** by whoever supplied the citation.

### 4. Closest genuine work — for disambiguation only, NOT the requested paper

These are real and I read them directly. They are offered so the requester can identify what the citation may have been garbled from. **Neither is by Kessler or Mbeki, neither is titled as requested, and neither reports anything called "sublinear preference collapse."**

- **Song, Cai, Lee & Su, "Reward Collapse in Aligning Large Language Models"** (arXiv:2305.17608, first posted May 2023) [8]. Documents *reward collapse*: ranking-based reward-model training drives an identical reward distribution across prompts in the terminal phase of training. Attributes it to the ranking objective failing to incorporate prompt information, derives closed-form asymptotic reward distributions for several utility functions, and proposes a **prompt-aware utility** that provably yields prompt-dependent reward distributions, with experiments showing it alleviates collapse. This is the nearest match on the *phenomenon* ("collapse … in RLHF reward models").
- **Xiao, Li, Xie, Getzen, Fang, Long & Su, "On the Algorithmic Bias of Aligning LLMs with RLHF: Preference Collapse and Matching Regularization"** (arXiv:2405.16455; JASA, 2025) [9]. Coins *preference collapse* — minority preferences being effectively discarded due to KL-regularization bias — and proposes preference-matching (PM) RLHF with a regularizer derived from an ODE. Reports preference-matching divergence dropping from **2.23 → 1.57 (≈29%)** on Llama-2-7B and **1.16 → 0.68 (≈41%)** on OPT-1.3B versus standard RLHF. This is the nearest match on the *term* ("preference collapse") and is the paper every "preference collapse" search hit resolved to.

*Inference (labeled):* a citation blending Song et al.'s "Reward Collapse … RLHF" title with Xiao et al.'s "Preference Collapse" terminology, plus invented authors and a "sublinear" qualifier, would reproduce the requested citation almost exactly. This is a hypothesis about provenance, not a verified fact.

### 5. Residual possibility I could not fully exclude

A paper could in principle exist as (a) an **ICML 2024 workshop** paper never posted to arXiv, or (b) a paper whose authors are indexed under different name spellings. I regard both as very unlikely: workshop papers in this area are near-universally posted to arXiv, and arXiv returned zero for the surname outright [2]. I could not run a DBLP confirmation because that endpoint served an anti-bot page [10]. If the requester has an independent identifier (DOI, OpenReview ID, or a PDF), supplying it would let me settle the question immediately.

---

## Recommendation

Do not cite this paper. If a downstream document already cites it, remove or replace the citation. If the intended referent was the reward-collapse phenomenon, cite **[8]**; if it was the preference-collapse / KL-bias result with the 29%/41% numbers, cite **[9]**.

---

## Coverage Status

**Checked directly and conclusively (negative):**
- ICML 2024 main proceedings full author/title index [1]
- arXiv author, title, and abstract queries [2][3][4]
- OpenAlex title search and author search [5][6]
- Crossref bibliographic search [7]
- Web search across multiple phrasings, including exact-title quotes

**Checked directly and positively (for the disambiguation section only):**
- arXiv abstract pages / full text for [8] and [9]

**Uncertain / blocked:**
- DBLP — anti-bot challenge, no data [10]
- ICML 2024 **workshop** proceedings were not indexed in a single place I could query exhaustively; this is the one residual gap, though arXiv's zero-result surname search makes a workshop-only paper very improbable.

**Not attempted, and why:** reconstructing method/results/setup for the requested paper. There is no source to read, and the integrity rules forbid describing a paper's contents without reading it.

---

## Sources

1. Proceedings of Machine Learning Research, *Proceedings of the 41st International Conference on Machine Learning* (Vol. 235), full index — https://proceedings.mlr.press/v235/
2. arXiv API query, `search_query=all:Mbeki` — https://export.arxiv.org/api/query?search_query=all:Mbeki
3. arXiv API query, `search_query=ti:"preference collapse"` — https://export.arxiv.org/api/query?search_query=ti:%22preference+collapse%22
4. arXiv API query, `abs:"sublinear" AND abs:"reward model"` — https://export.arxiv.org/api/query?search_query=abs:%22sublinear%22+AND+abs:%22reward%20model%22
5. OpenAlex Works API, `filter=title.search:sublinear preference collapse` — https://api.openalex.org/works?filter=title.search:sublinear%20preference%20collapse
6. OpenAlex Authors API, `search=Mbeki` — https://api.openalex.org/authors?search=Mbeki
7. Crossref Works API, bibliographic query for the requested title — https://api.crossref.org/works?query.bibliographic=Sublinear+Preference+Collapse+in+RLHF+Reward+Models
8. Ziang Song, Tianle Cai, Jason D. Lee, Weijie J. Su, *Reward Collapse in Aligning Large Language Models*, arXiv:2305.17608 — https://arxiv.org/abs/2305.17608
9. Jiancong Xiao, Ziniu Li, Xingyu Xie, Emily Getzen, Cong Fang, Qi Long, Weijie J. Su, *On the Algorithmic Bias of Aligning Large Language Models with RLHF: Preference Collapse and Matching Regularization*, arXiv:2405.16455 — https://arxiv.org/abs/2405.16455
10. DBLP publication search API (blocked) — https://dblp.org/search/publ/api?q=Mbeki