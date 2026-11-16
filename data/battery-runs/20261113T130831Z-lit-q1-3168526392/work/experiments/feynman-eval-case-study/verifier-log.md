# Verifier log — citation pass on `draft-with-seeded-defects.md`

Date: 2026-11-13. Research file: `fixtures/research-notes.md`. Output: `verifier-output.md`.

Every URL below was fetched with `fetch_content`; identifier checks used
`feynman_science_database_search` (arXiv `arxiv_get_papers`, OpenAlex, Crossref, Semantic Scholar).

## Source 1 — Vaswani et al., "Attention Is All You Need"

- **URL checked:** https://arxiv.org/abs/1706.03762 — **resolved**. Title matches, first author Ashish Vaswani, 8 authors listed, submitted 12 Jun 2017 (v1), last revised 2 Aug 2023 (v7).
- **Identifier cross-check A (arXiv API, `arxiv_get_papers`):** 1706.03762v7 — title, first author, and 2017-06-12 publication date match. DOI 10.48550/arXiv.1706.03762.
- **Identifier cross-check B (OpenAlex):** work W2626778328, DOI 10.48550/arxiv.1706.03762, title "Attention Is All You Need", publication year 2017, first author Ashish Vaswani. Bib records volume 30, pages 5998–6008 (i.e. NeurIPS 30 proceedings). **Matched.**
- **Venue:** https://papers.nips.cc/paper_files/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html — **resolved**, 2017 proceedings page, same abstract opening. NeurIPS 2017 confirmed.
- **Version discrepancy noted:** the NeurIPS proceedings abstract states 27.5 BLEU (En–De) and 41.1 BLEU (En–Fr); arXiv v7 states 28.4 and 41.8. Two different revisions of the paper. No BLEU figures were carried into the output document, so this does not affect any claim.
- **Claim checks:**
  - "replaces recurrence with multi-head self-attention" — **supported**. Abstract: "based solely on attention mechanisms, dispensing with recurrence and convolutions entirely"; §3.2.2 describes multi-head attention (h = 8 heads).
  - "Vaswani et al. (2019)" — **metadata mismatch**; the paper is 2017. Corrected.
  - "reduce training cost by 10x" — **claim unsupported**. The paper says "more parallelizable and requiring significantly less time to train" and "a small fraction of the training costs of the best models from the literature" for the En–Fr model; no 10x or other fixed multiplier appears. Softened to the qualitative claim.

## Source 2 — Brown et al., "Language Models are Few-Shot Learners" (GPT-3)

- **URL checked:** https://arxiv.org/abs/2005.14165 — **resolved**. Title matches, first author Tom B. Brown, v1 28 May 2020.
- **Identifier cross-check A (arXiv API):** 2005.14165v4 — title, first author, 2020-05-28 match. DOI 10.48550/arXiv.2005.14165.
- **Identifier cross-check B (OpenAlex):** work W3030163527, DOI 10.48550/arxiv.2005.14165, 2020, first author "Brown, Tom B." **Matched.**
- **Crossref:** DOI lookup returned no matching record (`10.48550/*` DOIs are DataCite-issued, so Crossref is the wrong index here). Not treated as a failure; two other indexes matched.
- **Claim checks:**
  - "95.2% zero-shot on TriviaQA" — **claim unsupported / wrong number**. Fetched the PDF and read Table 3.3: TriviaQA = 64.3% zero-shot, 68.0% one-shot, 71.2% few-shot. Also corroborated by the research notes. Corrected to 64.3% zero-shot / 71.2% few-shot.
  - "175 billion parameters" — supported by the abstract ("175 billion parameters").

## Source 3 — Devlin et al., "BERT"

- **URL checked:** https://arxiv.org/abs/1810.04805 — **resolved**. Title matches, first author Jacob Devlin, v1 11 Oct 2018, v2 24 May 2019.
- **Identifier cross-check A (arXiv API):** 1810.04805v2 — title, first author, 2018-10-11 match. DOI 10.48550/arXiv.1810.04805.
- **Identifier cross-check B (OpenAlex):** two records — preprint W2896457183 (2018, arXiv) and conference paper W2963341956 (2019, NAACL-HLT, DOI 10.18653/v1/n19-1423, pp. 4171–4186). Both carry the same title and first author; the draft's "2019" matches the NAACL venue record, the arXiv record is 2018. Recorded as preprint-2018 / venue-2019 in the Sources entry rather than flagged as a mismatch.
- **Claim check:** "pretrained with masked-language-model and next-sentence objectives" — **supported**. Fetched PDF: Task #1 Masked LM ("we simply mask some percentage of the input tokens at random…"), Task #2 Next Sentence Prediction (50% IsNext / 50% NotNext).

## Removed source 4 — Chen, Liu & Park, arXiv:2309.99999

- **URL checked:** https://arxiv.org/abs/2309.99999 — **dead**. arXiv returns "There is no record of an article with identifier '2309.99999'."
- No title/author search hits in the research notes (arXiv, Crossref, OpenAlex, Semantic Scholar). No DOI or venue recoverable. Source removed along with the 41% claim it supported. This is a fabricated identifier, not a link-rot case, so no archive search was applicable.

## Removed source 5 — "2024 ML Evaluation Survey"

- **URL checked:** https://example.com/2024-ml-evaluation-survey — **resolves to unrelated placeholder content**. The page is the IANA example-domain notice: "This domain is for use in documentation examples without needing permission. This is not a service." No article, no survey, no data.
- Treated as dead/unrelated. No alternative URL for a 2024 survey reporting 68% evaluation drift was found in the research notes; no archive lookup could help because the underlying document was never identified. Claim and source removed.

## False-positive checks (claims that had to survive)

- Transformer uses multi-head self-attention — **retained**, supported by [1].
- BERT uses MLM + NSP — **retained**, supported by [3].

## Residual notes

- Semantic Scholar bulk search returned poor/noisy results for these queries (0 hits for the GPT-3 query, unrelated hits for the BERT and Transformer queries), so arXiv + OpenAlex were used as the two confirming indexes. This is a search-relevance limitation, not a record mismatch.
- The output document's subject ("evaluation drift") now has no supporting evidence; a TODO in the "Removed Unsupported Claims" section records the gap.
- Citation numbering was renumbered to a single sequence [1]–[3]; the original draft's [4] and [5] entries were removed.