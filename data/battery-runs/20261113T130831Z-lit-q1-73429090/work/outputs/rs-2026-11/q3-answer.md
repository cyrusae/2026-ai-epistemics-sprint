# Q3 — Lookup: Kessler & Mbeki (2024), "Sublinear Preference Collapse in RLHF Reward Models," ICML 2024

## Bottom line

**I could not produce the summary, because I found no evidence that this paper exists.** I am not going to
invent a method description or numbers for it. The citation fails on all three of its identifying
attributes (author pair, title phrase, venue), and it fails in sources that would be expected to index it
if it were real.

The request assumed existence ("I know it exists"). That assumption is the one thing my checks contradict,
so the honest deliverable is the negative result plus the closest real work that the citation may have been
conflated with.

## Evidence table

| # | Source | URL | Key claim | Type | Confidence |
|---|--------|-----|-----------|------|------------|
| 1 | PMLR v235 — Proceedings of the 41st ICML (full paper index, Vienna 2024) | https://proceedings.mlr.press/v235/ | Full-text scan of the ICML 2024 proceedings index returns **no** match for "Kessler", **no** match for "Mbeki", **no** match for "Preference Collapse", and **no** match for "Reward Collapse" among titles/authors | primary | high |
| 2 | arXiv API — `all:"Sublinear Preference Collapse"` | http://export.arxiv.org/api/query?search_query=all:%22Sublinear+Preference+Collapse%22&max_results=20 | `totalResults = 0` — no arXiv paper contains this phrase anywhere in title/abstract/comments | primary | high |
| 3 | arXiv API — `au:Mbeki` (all of arXiv) | http://export.arxiv.org/api/query?search_query=au:Mbeki&max_results=50 | `totalResults = 0` — arXiv has no author surnamed Mbeki at all | primary | high |
| 4 | Semantic Scholar Graph API search | https://api.semanticscholar.org/graph/v1/paper/search/bulk?query=Sublinear+Preference+Collapse+RLHF+Reward+Models | `totalCount = 0` for the paper title | primary | high |
| 5 | Crossref works query | https://api.crossref.org/works?query=Sublinear+Preference+Collapse+in+RLHF+Reward+Models&rows=10 | No DOI record matching the title; top hits are unrelated "preference collapse / RLHF" papers by other authors | primary | high |
| 6 | OpenAlex author/work search "Mbeki" | https://openalex.org/works?search=Mbeki | Returns Thabo Mbeki / Govan Mbeki political science and South African medical authors; no ML/RLHF researcher named Mbeki | primary | high |
| 7 | Song, Cai, Lee, Su — "Reward Collapse in Aligning Large Language Models" (arXiv 2305.17608; JDS) | https://arxiv.org/abs/2305.17608 | Real paper documenting **reward collapse**; arXiv comment states acceptance at *Journal of Data Science* (JDS1201) | primary | high |
| 8 | Xiao, Li, Xie, Getzen, Fang, Long, Su — "On the Algorithmic Bias of Aligning LLMs with RLHF: Preference Collapse and Matching Regularization" (arXiv 2405.16455) | https://arxiv.org/abs/2405.16455 | Real paper introducing **preference collapse** + preference-matching (PM) RLHF; arXiv comment states acceptance at *JASA* | primary | high |
| 9 | JASA record via OpenAlex W4414274825 | https://openalex.org/W4414274825 | Bibliographic detail for [8]: *JASA* vol. 120, issue 552, pp. 2154–2164, DOI 10.1080/01621459.2025.2555067 | primary | high |
| 10 | ICML 2024 virtual papers list | https://icml.cc/virtual/2024/papers.html | Independent listing of ICML 2024 accepted papers; no title resembling "Sublinear Preference Collapse" appears in retrieved excerpts | secondary | medium |

## Findings

### The citation does not check out

The most decisive check is the ICML 2024 proceedings themselves. The PMLR volume 235 index lists every
accepted paper with authors [1]. Searching that complete index for the surname "Kessler" returns nothing,
for "Mbeki" returns nothing, for the title fragment "Preference Collapse" returns nothing, and for "Reward
Collapse" also returns nothing [1]. If a paper with these authors had appeared at ICML 2024, both surnames
would necessarily appear in that index. They do not.

This is corroborated by four independent indexes:

- arXiv contains **zero** papers matching the phrase "Sublinear Preference Collapse" [2].
- arXiv contains **zero** papers by any author named Mbeki, in any field, ever [3]. This is a strong signal:
  a 2024 ICML author with a prior publication record would normally have an arXiv presence.
- Semantic Scholar returns zero results for the title [4].
- Crossref has no DOI record for the title [5].

OpenAlex's author search for "Mbeki" surfaces only the South African political figures (Thabo, Govan) and
biomedical researchers, with no RLHF/alignment author [6]. I found no paper co-authored by anyone named
Kessler and anyone named Mbeki on any topic (inference from the four null searches above, not a single
direct "co-authorship" query).

The word "sublinear" is also unsupported: no real paper I located frames preference/reward collapse as a
*sublinear* phenomenon [2], and the actual reward-collapse analysis is framed in terms of closed-form
asymptotic reward distributions, not sublinear scaling [7].

**Inference (labeled as such):** the citation looks like a confabulated reference — a plausible-sounding
title assembled from vocabulary that is genuinely current in this literature ("preference collapse",
"reward models", "RLHF") attached to a fabricated author pair and a real venue. That is exactly the profile
of an LLM-generated hallucinated citation, and it is common enough that I would flag it to the advisor
rather than cite it.

### What the citation was probably conflating

Two real papers cover the two halves of the invented title. Both are worth citing in a related-work section
in place of the phantom reference.

**(a) "Reward collapse" — Song, Cai, Lee & Su** [7]. The paper documents *reward collapse*: with the
prevailing ranking-based (Bradley–Terry-style pairwise ranking) reward-model objective, the reward
distribution becomes essentially **identical regardless of prompt** in the terminal phase of training.
Open-ended prompts ("write a short story about your best friend") should yield a spread of rewards, while
closed-ended prompts ("what is the capital of New Zealand") should yield near-binary rewards. The authors
attribute collapse to the ranking objective's failure to incorporate prompt information, derive closed-form
reward distributions for a family of utility functions in an asymptotic regime, and propose a **prompt-aware
utility function** that provably admits a prompt-dependent reward distribution, which empirically mitigates
collapse. Venue per the arXiv comment is *Journal of Data Science* (JDS1201), **not ICML 2024** [7].

**(b) "Preference collapse" — Xiao et al.** [8]. This paper names *preference collapse*: the KL-regularized
RLHF objective carries an inherent algorithmic bias (inherited from the unaligned reference model) that, in
extreme cases, drives minority preferences to ~0% vs ~100%. They propose **preference-matching (PM) RLHF**,
deriving a PM regularizer equal to the negative log of the policy's response probability (i.e. an entropy-like
term), obtained by solving a necessary-condition ODE, plus a conditional variant for natural-language
generation. Reported result: preference-matching divergence drops from 2.23 → 1.57 (Llama-2-7B) and
1.16 → 0.68 (OPT-1.3B), described as roughly **29% and 41%** improvements over standard RLHF. Published in
*JASA* 120(552):2154–2164 [8][9]; also **not** an ICML 2024 paper.

Caveat on these two summaries: I read the arXiv abstract pages and the arXiv metadata (authors, comments,
dates) directly [7][8], plus the OpenAlex bibliographic record for the JASA version [9]. I did **not** read
either paper's full text, so the method and number descriptions above are abstract-level and should be
verified against the PDFs before being quoted as precise claims in a draft.

### Suggested action for the draft

1. Do not cite Kessler & Mbeki (2024). There is nothing to cite.
2. Replace with [7] and/or [8] depending on which phenomenon the sentence needs — reward collapse at the
   reward-model training stage, or preference collapse in the RLHF objective.
3. Check where the citation came from. If it was produced by a reference-generating tool or an LLM, audit
   the rest of that bibliography; fabricated entries rarely travel alone.

## Sources

1. PMLR, *Proceedings of the 41st International Conference on Machine Learning* (Vol. 235, ICML 2024) — https://proceedings.mlr.press/v235/
2. arXiv API, query `all:"Sublinear Preference Collapse"` — http://export.arxiv.org/api/query?search_query=all:%22Sublinear+Preference+Collapse%22&max_results=20
3. arXiv API, query `au:Mbeki` — http://export.arxiv.org/api/query?search_query=au:Mbeki&max_results=50
4. Semantic Scholar Graph API, bulk paper search — https://api.semanticscholar.org/graph/v1/paper/search/bulk?query=Sublinear+Preference+Collapse+RLHF+Reward+Models
5. Crossref REST API, works query — https://api.crossref.org/works?query=Sublinear+Preference+Collapse+in+RLHF+Reward+Models&rows=10
6. OpenAlex, work search for "Mbeki" — https://openalex.org/works?search=Mbeki
7. Ziang Song, Tianle Cai, Jason D. Lee, Weijie J. Su, "Reward Collapse in Aligning Large Language Models," arXiv:2305.17608 — https://arxiv.org/abs/2305.17608
8. Jiancong Xiao, Ziniu Li, Xingyu Xie, Emily Getzen, Cong Fang, Qi Long, Weijie J. Su, "On the Algorithmic Bias of Aligning Large Language Models with RLHF: Preference Collapse and Matching Regularization," arXiv:2405.16455 — https://arxiv.org/abs/2405.16455
9. OpenAlex record W4414274825, *Journal of the American Statistical Association* 120(552):2154–2164 — https://openalex.org/W4414274825
10. ICML 2024 virtual conference paper list — https://icml.cc/virtual/2024/papers.html

## Coverage Status

**Checked directly (primary, full inspection):**
- ICML 2024 accepted-paper index, PMLR v235 — searched for "Kessler", "Mbeki", "Preference Collapse",
  "Reward Collapse", "Sublinear" across the complete volume listing. (done)
- arXiv metadata API — exact phrase, author surname, plus `ti:"preference collapse"` and
  `ti:"reward collapse"` enumerations. (done)
- Semantic Scholar bulk search for the title. (done)
- Crossref works query for the title. (done)
- OpenAlex for "Mbeki" and for "Kessler Mbeki 2024". (done)
- arXiv abs/metadata for the two candidate real papers (authors, venue comments, dates). (done)

**Not fully verified / uncertain:**
- I did **not** read the full text of [7] or [8]; their method and headline-number descriptions here are
  abstract-level only, and the "29% / 41%" figures are quoted from the abstract rather than recomputed.
- I could not query DBLP (its API is behind an Anubis bot-challenge from this environment), so DBLP is an
  unchecked index. Given the null results in PMLR, arXiv, Semantic Scholar, Crossref and OpenAlex, a DBLP
  hit for this exact paper is implausible, but I am not claiming I checked it.
- A paper could in principle exist in a non-indexed workshop or as an unpublished manuscript. I found no
  trace of one, and a workshop paper would not be "ICML 2024" in the sense the draft cites. I did not search
  OpenReview directly for ICML 2024 submissions.
- I did not attempt to identify whether a real researcher named "Kessler" works on reward models under a
  different paper; that is irrelevant to whether *this* citation is real.

**Could not complete:** the requested summary of the named paper. It cannot be summarized because it does
not appear to exist.
