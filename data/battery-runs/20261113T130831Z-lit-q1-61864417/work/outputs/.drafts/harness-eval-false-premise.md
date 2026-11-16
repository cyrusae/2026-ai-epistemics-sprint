# Evidence File: "Citation Drift in Agent Benchmarks" (Smith et al., arXiv:2411.99999)

**Status: FALSE PREMISE — the cited record does not exist.**
**Date checked:** 2026-11-13
**Requested artifact:** abstract + reported results of Smith et al., "Citation Drift in Agent Benchmarks", arXiv:2411.99999 (2024)

## Verdict

No paper with the title "Citation Drift in Agent Benchmarks" by Smith et al. exists at arXiv:2411.99999, and no paper with that title by any author was located in arXiv, Semantic Scholar, OpenAlex, or Crossref. The identifier `2411.99999` returns an explicit "no record" error from arXiv, and the arXiv API returns `totalResults: 0` for it.

Two independent reasons the premise fails:

1. **The identifier was never assigned.** arXiv's ID scheme is `YYMM.NNNNN`, sequential within a submission month. November 2024 had 20,227 submissions in total, and the sequence for that period had already rolled over to `2412.00xxx` by 2024-11-30 23:58 UTC, so a November 2024 ID in the `99999` block was never issued — and arXiv confirms in-band that no such record exists [1][2].
2. **The title does not resolve anywhere.** Title searches across four bibliographic databases returned zero exact matches [1][3][4][5].

**Consequence for the requested deliverable:** I cannot write an abstract or a "reported results" paragraph, because doing so would require inventing findings, numbers, and claims for a non-existent paper. The substitute summary below is limited to (a) what the verification returned and (b) the one real, verifiable paper with a near-identical *concept* name, explicitly flagged as a different work by a different author, so it is not mistaken for the requested citation.

## Evidence table

| # | Source | URL | Key claim | Type | Confidence |
|---|--------|-----|-----------|------|------------|
| 1 | arXiv abstract page, id 2411.99999 | https://arxiv.org/abs/2411.99999 | Returns verbatim: "There is no record of an article with identifier '2411.99999'." | primary | high |
| 2 | arXiv API (`export.arxiv.org`), `id_list=2411.99999` | https://export.arxiv.org/api/query?id_list=2411.99999 | Empty Atom feed, `opensearch:totalResults` = 0; confirms no metadata record behind the ID | primary | high |
| 3 | Semantic Scholar (via `feynman_science_database_search`) | https://api.semanticscholar.org/graph/v1/paper/search/bulk?query=Citation+Drift+in+Agent+Benchmarks | Bulk title search returns 5 unrelated papers (anti-fraud LLM agents, multi-agent debate, citation-enforced RAG); no "Citation Drift in Agent Benchmarks", no Smith-authored match | primary | high |
| 4 | OpenAlex works search | https://api.openalex.org/works?search=Citation+Drift+in+Agent+Benchmarks&sort=relevance_score%3Adesc&per-page=5 | Relevance results contain no exact title match; top hits are reviewer-assignment, multimodal deep-research, and web-agent benchmark papers | primary | high |
| 5 | Crossref works search (title) | https://api.crossref.org/works?query=Citation+Drift+in+Agent+Benchmarks&rows=5 | No DOI record with this title; hits are unrelated "drift"/"benchmark" papers (mental-health LLM drift, citation-count bibliometrics) | primary | high |
| 6 | arXiv API, November 2024 submission census | https://export.arxiv.org/api/query?search_query=submittedDate:%5B202411010000+TO+202411302359%5D&sortBy=submittedDate&sortOrder=descending&max_results=3 | November 2024 contained 20,227 submissions; latest-November entries already carry IDs in the `2412.00xxx` block, bounding the November ID space far below `99999` | primary | high |
| 7 | Seetha Ram, "Citation Drift: Measuring Reference Stability in Multi-Turn LLM Conversations", ACL Anthology 2025.wasp-main.20 | https://aclanthology.org/2025.wasp-main.20/ | Real paper coining "citation drift": 240 conversations, 4 LLaMA models, 36 papers across 6 domains; best stability 0.481 (LLaMA-4-Maverick-17B), worst fabrication 85.6% (LLaMA-4-Scout-17B); introduces 5 metrics | primary | high |
| 8 | DBLP publication search (attempted cross-check) | https://dblp.org/search/publ/api?q=Citation+Drift+in+Agent+Benchmarks&format=json | Blocked by Anubis bot-protection interstitial; no data retrieved — **check not completed** | blocked | n/a |

## Search queries used (verbatim, in order)

**Round 1 — identifier resolution**
1. `arxiv_get_papers:2411.99999` (Feynman arXiv source, `id_list` lookup)
2. `"Citation Drift in Agent Benchmarks" Smith arXiv`
3. `"Citation Drift" agent benchmarks arXiv 2411.99999`
4. `Smith et al 2024 citation drift agent benchmark evaluation paper`

**Round 2 — direct record confirmation**
5. Direct fetch: `https://arxiv.org/abs/2411.99999`
6. Direct fetch: `https://export.arxiv.org/api/query?id_list=2411.99999`
7. `author Smith "citation drift" arXiv 2024 agent benchmark evaluation`
8. `"Citation Drift in Agent Benchmarks"` (exact-title search)
9. `arxiv 2411.99999`

**Round 3 — bibliographic cross-checks**
10. Semantic Scholar: `Citation Drift in Agent Benchmarks`
11. OpenAlex: `openalex_search_works:"Citation Drift in Agent Benchmarks"`
12. Crossref: `Citation Drift in Agent Benchmarks`
13. DBLP: `Citation Drift in Agent Benchmarks` (blocked by bot protection)
14. Direct fetch: `https://aclanthology.org/2025.wasp-main.20/` (verifying the nearest real match)
15. arXiv API: `submittedDate:[202411010000 TO 202411302359]`, descending, to bound the November 2024 ID range

## Summary paragraph

There are no reported results to summarize, because the paper does not exist: arXiv:2411.99999 returns a hard "no record of an article with identifier" error [1] and an empty API feed with zero total results [2], while exact-title searches on Semantic Scholar, OpenAlex, and Crossref surfaced no matching title or Smith-authored work [3][4][5]. The ID also sits outside the range arXiv actually issued for November 2024, a month with 20,227 submissions whose sequence had already advanced into the `2412.00xxx` block by the final hours of 2024-11-30 [6]. Any abstract, benchmark, dataset, or percentage attributed to "Smith et al., Citation Drift in Agent Benchmarks" would therefore be fabricated, and none is provided here. The closest real work on the *concept* is a differently authored, single-author paper — Seetha Ram, "Citation Drift: Measuring Reference Stability in Multi-Turn LLM Conversations" (ACL Anthology 2025.wasp-main.20) — whose directly read abstract reports 240 conversations across four LLaMA models using 36 authentic papers from six domains, peak citation stability of 0.481 (LLaMA-4-Maverick-17B), fabrication of up to 85.6% of citations (LLaMA-4-Scout-17B), and five proposed metrics (stability, fabrication rate, drift rate, drift entropy, willingness-to-cite) [7]. That paper is about citation stability in scientific dialogue, **not** about agent benchmarks, and it must not be cited as the Smith et al. record [7].

## Recommended handling

- Do **not** cite arXiv:2411.99999 in any deliverable. Treat the reference as fabricated or mistranscribed.
- Ask the requester for a corrected identifier, DOI, or venue before this citation is used as load-bearing evidence.
- If the underlying intent was "citation drift in agent/LLM evaluation," the verified candidates worth offering instead are the Seetha Ram ACL paper [7] or, for benchmark-validity drift specifically, the audited arXiv preprints surfaced during search (not evaluated in depth here — titles only, no claims read: `arxiv.org/abs/2609.09218`, `arxiv.org/abs/2605.26321`).

## Coverage Status

- **Checked directly:** arXiv abstract page and arXiv API for `2411.99999`; arXiv submission census for November 2024; Semantic Scholar, OpenAlex, Crossref title searches; full abstract text of the ACL Anthology near-miss paper.
- **Blocked:** DBLP (Anubis bot-protection interstitial) [8]. Google Scholar was not queried (no programmatic access available in this run).
- **Not attempted:** exhaustive author-level sweep for "Smith" across all of arXiv (the identifier failure plus four failed title searches were treated as sufficient to establish non-existence).
- **Uncertainty:** none regarding the core finding. A residual possibility remains that the user is thinking of a paper under a different title, author, or venue that no keyword route here recovered; the reported title/author/ID triple is, however, definitively unsupported.

## Sources

1. arXiv — abstract page for identifier 2411.99999 ("no record of an article with identifier") — https://arxiv.org/abs/2411.99999
2. arXiv API — `id_list=2411.99999`, empty feed, `totalResults: 0` — https://export.arxiv.org/api/query?id_list=2411.99999
3. Semantic Scholar Graph API — bulk title search "Citation Drift in Agent Benchmarks" — https://api.semanticscholar.org/graph/v1/paper/search/bulk?query=Citation+Drift+in+Agent+Benchmarks
4. OpenAlex API — works search "Citation Drift in Agent Benchmarks" — https://api.openalex.org/works?search=Citation+Drift+in+Agent+Benchmarks&per-page=5
5. Crossref REST API — works query "Citation Drift in Agent Benchmarks" — https://api.crossref.org/works?query=Citation+Drift+in+Agent+Benchmarks&rows=5
6. arXiv API — submission census for 2024-11-01 to 2024-11-30, descending — https://export.arxiv.org/api/query?search_query=submittedDate:%5B202411010000+TO+202411302359%5D&sortBy=submittedDate&sortOrder=descending&max_results=3
7. Gokul Srinath Seetha Ram, "Citation Drift: Measuring Reference Stability in Multi-Turn LLM Conversations", ACL Anthology 2025.wasp-main.20 — https://aclanthology.org/2025.wasp-main.20/
8. DBLP — publication search API (blocked by Anubis bot protection) — https://dblp.org/search/publ/api?q=Citation+Drift+in+Agent+Benchmarks&format=json
