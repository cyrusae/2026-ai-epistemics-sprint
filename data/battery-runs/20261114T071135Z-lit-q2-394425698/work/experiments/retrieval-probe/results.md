# Retrieval probe: default `feynman_science_database_search`

- **Date:** 2026-11-14 (UTC)
- **Harness:** `@companion-ai/feynman` 0.5.65
- **Tool:** `feynman_science_database_search`, `source: "semanticscholar"`,
  default sort (`citationCount:desc`), `limit: 5`
- **Protocol:** five fixed queries, five results each, relevance judged from
  returned title + abstract. "Relevant" = the record centrally concerns LLM/AI
  evaluation, benchmarks, judges, or citation integrity. Tangential = counted
  irrelevant (strict scoring).
- **n:** 5 queries, 25 requested result slots, 20 records returned. Not a
  benchmark; a smoke test of the default evidence-gathering surface.

## Results

| Q | Query | Records returned | Relevant (strict) | Notes |
|---|-------|------------------|-------------------|-------|
| 1 | `construct validity large language model benchmarks` | 5 | 1 | Bean et al. 2025 is the only direct hit; NER, KG construction, an unrelated "Conference Papers" record, and TRAIL (agent-trace eval) fill the rest |
| 2 | `LLM-as-a-judge reliability human agreement` | 5 | 5 | **Not Semantic Scholar**: S2 returned HTTP 429 and the tool fell back to OpenAlex. Fallback preserved a `fallbackNote` and returned 5/5 on-topic |
| 3 | `benchmark contamination holdout machine learning evaluation` | 0 | 0 | Zero records, though relevant papers exist in the index |
| 4 | `variance error bars language model evaluation statistics` | 0 | 0 | Zero records, though Madaan et al. 2024 (arXiv 2406.10229) is in the index |
| 5 | `citation hallucination fabricated references large language models` | 5 | 4 | One off-topic clinical-diagnosis paper |

## Aggregate

- Semantic Scholar-only queries (1, 3, 4, 5): 15 slots requested, 10 records
  returned, **5 relevant**.
- Precision over returned records (S2 only): **5/10 = 50%**.
- Precision over requested slots (S2 only): **5/15 = 33%**.
- Queries yielding at least one relevant record (S2 only): **2/4**.
- Including the OpenAlex fallback: **3/5 queries** yielded relevant evidence;
  **10/20 returned records** were relevant.

## Observations

1. **Multi-concept natural-language queries are the failure mode.** The two
   zero-result queries each combine 3–5 concepts; the two highest-precision
   queries are shorter or single-concept. This is consistent with lexical bulk
   search behaviour, not a ranking problem.
2. **The index-fallback path worked.** When Semantic Scholar was rate-limited,
   the tool silently switched indexes but surfaced `fallbackNote` and endpoint
   provenance. That is the right behaviour for eval reproducibility: the
   instrument changed, and the change is recorded.
3. **OpenAlex returns verification primitives the prompt layer ignores.**
   Fallback records included `isRetracted`, `openAccess.status`, and ORCIDs.
   No harness agent prompt requires checking retraction status.
4. **Citation-sorted defaults surface high-citation, topically wrong records.**
   The "Conference Papers" record (161 citations, Dostoevsky Journal) appearing
   under a construct-validity query is a concrete example of citation count as a
   poor topical prior.

## Raw provenance

Endpoint template (from tool output):
`https://api.semanticscholar.org/graph/v1/paper/search/bulk?query=<q>&fields=title,year,authors,venue,citationCount,externalIds,openAccessPdf,abstract&sort=citationCount:desc`

OpenAlex fallback endpoint:
`https://api.openalex.org/works?search=LLM-as-a-judge+reliability+human+agreement&sort=relevance_score:desc&per-page=5`

Full result objects were returned in-session; the titles, years, and relevance
judgments above are transcribed from them.
