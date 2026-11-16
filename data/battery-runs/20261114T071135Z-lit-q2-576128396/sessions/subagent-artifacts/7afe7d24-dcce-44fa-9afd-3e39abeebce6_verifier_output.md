Body-only citation audit is clean: all five sources cited, no orphans in either direction.

**What I found and fixed**

The draft contained three fabricated or wrong quantitative claims and one entirely fabricated paper:

| Draft claim | Reality | Action |
|---|---|---|
| BERT GLUE 84.2% | 80.5% (7.7-pt absolute gain) | Corrected |
| CoT GSM8K 71.3% | Abstract states no percentage | Number removed |
| Zhao et al. arXiv:2405.99999 | arXiv API `not_found`; URL 404 | Paragraph + source deleted |
| `example.org/definitely-not-a-real-paper-2024` | IANA example-domain placeholder | Removed |
| RAG "+37% factual accuracy" | Not in Lewis abstract; research file marks it metadata-only | Replaced with abstract-supported claim |
| Transformer "512 GPUs" | 3.5 days on **eight** GPUs | Corrected |

All five surviving arXiv IDs were resolved through the arXiv API **and** a second index (OpenAlex or Semantic Scholar), and all five abstract URLs were fetched live. Two non-blocking metadata discrepancies are documented: the CoT paper's Semantic Scholar record adds Denny Paper P as an author, and a Crossref title search for the Transformer paper returned only 2025 `posted-content` DOIs rather than the canonical NeurIPS record.