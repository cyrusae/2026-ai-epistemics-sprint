# Verification log — experiments/verifier-clean-run2

Date of checks: 2026-11-13. Tools used: `fetch_content` (arXiv abstract pages, arXiv export API, PDFs, example.com) and `feynman_science_database_search` (arxiv, openalex, crossref, semanticscholar).

## Source-by-source results

| # | Source as cited in draft | Identifier checked | Exact check performed (tool + query) | Outcome |
|---|---|---|---|---|
| 1 | He et al. (2015), Deep Residual Learning for Image Recognition | arXiv:1512.03385 | `feynman_science_database_search` source=arxiv, `arxiv_get_papers:1512.03385,...` | **Live / match.** Title "Deep Residual Learning for Image Recognition"; authors Kaiming He, Xiangyu Zhang, Shaoqing Ren, Jian Sun; submitted 2015-12-10. Abstract: "An ensemble of these residual nets achieves 3.57% error on the ImageNet test set." |
| 1a | same | arXiv:1512.03385 | `fetch_content` https://arxiv.org/abs/1512.03385 (answer mode) | **Live.** Page resolves; submission history from Kaiming He, 10 Dec 2015; abstract sentence confirmed verbatim. |
| 1b | same | DOI 10.48550/arxiv.1512.03385 | `feynman_science_database_search` source=openalex, query `10.48550/arxiv.1512.03385` | **Match.** OpenAlex W2949650786, title/first author (Kaiming He)/year (2015) all match. |
| 1c | "3.57% **top-5** error" specificity | arXiv PDF | `fetch_content` https://arxiv.org/pdf/1512.03385 (answer mode) | **Supported.** Section 4.1: "This leads to 3.57% top-5 error on the test set (Table 5)." Table 5: "ResNet (ILSVRC'15) 3.57" under "top-5 err. (test)". |
| 2 | Vaswani et al. (2017), Attention Is All You Need | arXiv:1706.03762 | `feynman_science_database_search` source=arxiv, `arxiv_get_papers:...,1706.03762,...` | **Live / match.** Title "Attention Is All You Need"; first author Ashish Vaswani; submitted 2017-06-12. Abstract: "Our model achieves 28.4 BLEU on the WMT 2014 English-to-German translation task." |
| 2a | same | arXiv:1706.03762 | `fetch_content` https://arxiv.org/abs/1706.03762 (answer mode) | **Live.** Resolves; 2017; 28.4 BLEU sentence present (the extractor also surfaced the 41.8 English-to-French sentence). |
| 2b | same | DOI 10.48550/arxiv.1706.03762 | `feynman_science_database_search` source=openalex, query `10.48550/arxiv.1706.03762` | **Match.** OpenAlex W2626778328, title/first author/year match. |
| 3 | OpenAI (2023), GPT-4 Technical Report | arXiv:2303.08774 | `feynman_science_database_search` source=arxiv, `arxiv_get_papers:...,2303.08774,...` | **Live / match.** Title "GPT-4 Technical Report"; first author "OpenAI"; submitted 2023-03-15 (v6 2024-03-04). Abstract contains no MMLU number. |
| 3a | same | DOI 10.48550/arxiv.2303.08774 | `feynman_science_database_search` source=openalex, query `10.48550/arxiv.2303.08774` | **Match.** OpenAlex W4327810158, title/first author/year match. |
| 3b | "92.0% on MMLU" | arXiv PDF | `fetch_content` https://arxiv.org/pdf/2303.08774 (answer mode) | **MISMATCH — corrected.** Report states 86.4% on MMLU, Table 2 (Section 4, "Capabilities"), 5-shot. No 92.0% figure found. Draft figure replaced with 86.4% (5-shot). |
| 4 | Okafor et al. (2025), "Provenance-Gated Retrieval for Autonomous Research Agents" | arXiv:2502.14444 | `fetch_content` https://arxiv.org/abs/2502.14444 (answer mode); `fetch_content` arXiv export API id_list=...,2502.14444,... | **DEAD AS CITED.** ID resolves, but to "An Enhancement of Jiang, Z., et al.'s Compression-Based Classification Algorithm Applied to News Article Categorization" (Benavides, Masapol, Morano, Cortez; 2025-02-20). No Okafor, no provenance gates. |
| 4a | same title | title search | `feynman_science_database_search` source=openalex, query "Provenance-Gated Retrieval for Autonomous Research Agents" | **No match.** Top hits are unrelated works (e.g., "Sleeper Channels and Provenance Gates", "DualResearch", "EviGraph"); no work with the cited title or author. |
| 4b | same | research-notes caveat | manual review of research-notes.md | Notes state the source "was recorded from a search-result snippet; the URL was not opened." Consistent with failing verification. **Claim removed.** |
| 5 | Krishnamurthy et al. (2024), "Calibrated Retrieval Augmentation for Scientific Agents" | arXiv:2405.19999 | `fetch_content` arXiv export API id_list=2405.19999 | **DEAD AS CITED.** ID resolves to "The spectral radius and the distance spectral radius of complements of block graphs" (Xu Chen, Dongjun Fan, Rongxiao Shao, Guoping Wang; math.CO, 2024-05-30). |
| 5a | same title | Crossref query | `feynman_science_database_search` source=crossref, query "Calibrated Retrieval Augmentation for Scientific Agents" | **No match.** Returns phase-retrieval and RAG-query-augmentation papers; none with the cited title or authors. |
| 5b | same title | OpenAlex semantic search | `feynman_science_database_search` source=openalex, query "Calibrated Retrieval Augmentation Scientific Agents Krishnamurthy 2024" | **No match.** No work with the cited title or author. **Claim removed.** |
| 6 | BERT, cited in draft as arXiv:1706.03762 | arXiv:1810.04805 | `feynman_science_database_search` source=arxiv, `arxiv_get_papers:...,1810.04805` | **IDENTIFIER ERROR — corrected.** arXiv:1706.03762 is the Transformer paper, not BERT. Correct BERT ID is 1810.04805: title "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding"; first author Jacob Devlin; submitted 2018-10-11. |
| 6a | same | DOI 10.48550/arxiv.1810.04805 | `feynman_science_database_search` source=openalex, query `10.48550/arxiv.1810.04805` | **Match.** OpenAlex W2896457183; title/first author match; record year 2018 (preprint), consistent with 2019 NAACL publication. |
| 6b | "introduced masked-language-model pretraining" | arXiv PDF | `fetch_content` https://arxiv.org/pdf/1810.04805 (answer mode) | **Supported.** "BERT alleviates the previously mentioned unidirectionality constraint by using a 'masked language model' (MLM) pre-training objective, inspired by the Cloze task." |
| 7 | "Feynman's verifier reduces citation errors by 43% in production deployments" | none | manual review of research-notes.md | **No source exists.** Notes: "No source was found for the 43% citation-error reduction claim." **Claim removed.** |
| 8 | https://example.com/feynman-eval-report | URL | `fetch_content` https://example.com/feynman-eval-report (answer mode) | **Placeholder / no content.** Page serves only standard example-domain notices; no benchmark report. **Removed.** |

## Index cross-check summary (kept sources only)

| Source | arXiv record | Second index | Title / first author / year |
|---|---|---|---|
| ResNet | 1512.03385v1 | OpenAlex W2949650786 | match / match / 2015 |
| Transformer | 1706.03762v7 | OpenAlex W2626778328 | match / match / 2017 |
| GPT-4 | 2303.08774v6 | OpenAlex W4327810158 | match / match (OpenAI) / 2023 |
| BERT | 1810.04805v2 | OpenAlex W2896457183 | match / match / 2018 preprint (2019 venue) |

## Notes on tool behavior

- Semantic Scholar bulk search does **not** resolve bare `arXiv:<id>` strings to the paper; queries such as `arXiv:1512.03385` returned unrelated citing papers. OpenAlex DOI lookups (`filter=doi:10.48550/arxiv.<id>`) resolved exactly and were used as the second index.
- `fetch_content` in answer mode on arXiv `/abs/` pages frequently omits the title block; titles were confirmed from the arXiv API records and, where needed, the PDFs.
- arXiv title search is not supported by the `arxiv` source (it is ID-only); title searches therefore ran against OpenAlex/Crossref.

## Orphan-citation check

Inline citations in `cited-output.md`: [1], [2], [3], [4]. Sources list: 1–4. No orphan citations; no uncited sources. Every retained factual claim has at least one citation.
