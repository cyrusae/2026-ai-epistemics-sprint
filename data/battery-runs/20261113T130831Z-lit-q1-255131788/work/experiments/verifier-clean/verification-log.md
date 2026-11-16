# Verification log

Task: add inline citations to `draft.md` from `research-notes.md`, verify every URL and identifier, and write `cited-output.md`.

Legend for outcomes: **VERIFIED** (record matches title/authors/claim), **FLAGGED** (mismatch or corrected), **REMOVED** (no traceable source; claim deleted).

## Sources checked

### [1] He et al. (2015), "Deep Residual Learning for Image Recognition", arXiv:1512.03385 — VERIFIED

- `feynman_science_database_search` source=`arxiv`, query=`arxiv_get_papers:1512.03385,...`
  - Result: title "Deep Residual Learning for Image Recognition"; authors Kaiming He, Xiangyu Zhang, Shaoqing Ren, Jian Sun; published 2015-12-10. Abstract contains: "An ensemble of these residual nets achieves 3.57% error on the ImageNet test set."
  - Outcome: title, year, first author, and the 3.57% figure all match the draft claim.
- `fetch_content` URL `https://arxiv.org/abs/1512.03385`, mode=answer
  - Result: page resolves; exact abstract sentence found: "An ensemble of these residual nets achieves 3.57% error on the ImageNet test set."
  - Outcome: live URL, content confirmed.
- `feynman_science_database_search` source=`crossref`, query=`Deep Residual Learning for Image Recognition He Zhang Ren Sun 2015`
  - Result: DOI `10.1109/cvpr.2016.90`, title matches, authors match, CVPR 2016 proceedings.
  - Outcome: second-index match confirmed. Note: arXiv preprint (2015) and CVPR venue record (2016) are the same work; the draft's year (2015) matches the arXiv record, not the venue record.

### [2] Vaswani et al. (2017), "Attention Is All You Need", arXiv:1706.03762 — VERIFIED

- `feynman_science_database_search` source=`arxiv`, query=`arxiv_get_papers:1706.03762,...`
  - Result: title "Attention Is All You Need"; first author Ashish Vaswani; published 2017-06-12. Abstract contains: "Our model achieves 28.4 BLEU on the WMT 2014 English-to-German translation task."
  - Outcome: title, year, first author, and 28.4 BLEU claim match.
- `fetch_content` URL `https://arxiv.org/abs/1706.03762`, mode=answer
  - Result: page resolves; exact 28.4 BLEU sentence found.
  - Outcome: live URL, content confirmed.
- `feynman_science_database_search` source=`crossref`, query=`Attention Is All You Need Vaswani 2017`
  - Result: only three `posted-content` records with DOI prefix `10.65215/...` and duplicate titles/authors; no authoritative NeurIPS DOI returned.
  - Outcome: arXiv record used as the authoritative identifier; Crossref surfaced only unofficial mirrors. Flagged in this log, not in the document.

### [3] OpenAI (2023), "GPT-4 Technical Report", arXiv:2303.08774 — FLAGGED (figure corrected)

- `feynman_science_database_search` source=`arxiv`, query=`arxiv_get_papers:2303.08774,...`
  - Result: title "GPT-4 Technical Report"; author "OpenAI"; published 2023-03-15. Abstract does NOT contain an MMLU number.
  - Outcome: identifier/title match; the draft's 92.0% MMLU figure is not supported by the abstract.
- `fetch_content` URL `https://arxiv.org/abs/2303.08774`, mode=answer, prompt asking for the MMLU score
  - Result: "Not found in extracted page content... contains no MMLU score, no results table, and no MMLU reference in the abstract."
  - Outcome: confirms the abstract is not the source of the number.
- `fetch_content` URL `https://arxiv.org/pdf/2303.08774v6`, mode=answer, prompt asking for the MMLU result and table
  - Result: "GPT-4's MMLU result is 86.4%, not 92.0%. It appears in Table 2 ('Performance of GPT-4 on academic benchmarks') under the 'GPT-4' column for the MMLU row (5-shot). The 92.0% value in that table is for GSM-8K, not MMLU."
  - Outcome: draft figure was wrong; corrected to 86.4% (5-shot), Table 2. The 92.0% value belongs to GSM-8K.
- `feynman_science_database_search` source=`crossref`, query=`GPT-4 Technical Report OpenAI 2023`
  - Result: no matching record returned (tech report has no DOI in Crossref).
  - Outcome: arXiv record is the only authoritative identifier; no contradiction found.

### [4] Devlin et al. (2019), "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding", arXiv:1810.04805 — VERIFIED (draft identifier corrected)

- `feynman_science_database_search` source=`arxiv`, query=`arxiv_get_papers:...,1810.04805,...`
  - Result: title "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding"; authors Jacob Devlin, Ming-Wei Chang, Kenton Lee, Kristina Toutanova; published 2018-10-11, updated 2019-05-24.
  - Outcome: title/year/first author match. The draft had cited this paper as arXiv:1706.03762, which is "Attention Is All You Need"; corrected to 1810.04805.
- `feynman_science_database_search` source=`crossref`, query=`BERT Pre-training of Deep Bidirectional Transformers for Language Understanding Devlin 2019`
  - Result: DOI `10.18653/v1/n19-1423`, title matches, authors match, NAACL 2019.
  - Outcome: second-index match confirmed.
- `fetch_content` URL `https://arxiv.org/pdf/1810.04805v2`, mode=answer, prompt asking whether masked-LM pretraining is introduced
  - Result: "Yes. The paper introduces masked language model (MLM) pretraining. Relevant sentence: 'The masked language model randomly masks some of the tokens from the input, and the objective is to predict the original vocabulary id of the masked word based only on its context.'"
  - Outcome: supporting evidence for the masked-LM claim found in the paper body (not the abstract).
- `fetch_content` URL `https://arxiv.org/abs/1810.04805`, mode=answer
  - Result: page resolves; abstract text served, but the MLM sentence is not in the abstract.
  - Outcome: live URL; body text (PDF) used for the MLM claim.

## Identifiers checked and rejected

### arXiv:2405.19999 (claimed: Krishnamurthy et al. 2024, "Calibrated Retrieval Augmentation for Scientific Agents") — REMOVED

- `feynman_science_database_search` source=`arxiv`, query=`arxiv_get_papers:...,2405.19999`
  - Result: the ID resolves to "The spectral radius and the distance spectral radius of complements of block graphs" by Xu Chen, Dongjun Fan, Rongxiao Shao, Guoping Wang (math.CO, 2024).
  - Outcome: title, authors, and subject mismatch the claimed paper.
- `feynman_science_database_search` source=`semanticscholar`, query=`Calibrated Retrieval Augmentation for Scientific Agents Krishnamurthy 2024`
  - Result: `totalCount: 0`.
  - Outcome: no record under the claimed title/authors.
- `feynman_science_database_search` source=`crossref`, query=`Calibrated Retrieval Augmentation Scientific Agents`
  - Result: no matching title among returned records.
  - Outcome: no record. The claimed paper and its 31% result have no traceable source; sentence removed.

### arXiv:2502.14444 (claimed: Okafor et al. 2025, "Provenance-Gated Retrieval for Autonomous Research Agents") — REMOVED

- `feynman_science_database_search` source=`arxiv`, query=`arxiv_get_papers:...,2502.14444`
  - Result: the ID resolves to "An Enhancement of Jiang, Z., et al.s Compression-Based Classification Algorithm Applied to News Article Categorization" by Sean Lester C. Benavides et al. (cs.CL, 2025).
  - Outcome: title, authors, and topic mismatch the claimed paper.
- `feynman_science_database_search` source=`semanticscholar`, query=`"Provenance-Gated Retrieval for Autonomous Research Agents"` (exact-title, quoted)
  - Result: `totalCount: 0`.
  - Outcome: no record.
- `feynman_science_database_search` source=`crossref`, query=`Provenance-Gated Retrieval Autonomous Research Agents`
  - Result: no matching title among returned records.
  - Outcome: no record.
- `web_search`, queries `["\"Provenance-Gated Retrieval for Autonomous Research Agents\" Okafor", ...]`
  - Result: no matching paper. Returned unrelated Okafor-authored works (a 2026 RAG provenance paper with different title and different fabricated-citation rates, 19.6%).
  - Outcome: the claimed 18%→2% result is unsupported. Research notes themselves state this source "was recorded from a search-result snippet; the URL was not opened." Sentence removed; the unrelated 2026 paper was not substituted because it does not support the claim.

## Other claims checked

### "Feynman's verifier reduces citation errors by 43% in production deployments" — REMOVED

- Check: `research-notes.md` states "No source was found for the 43% citation-error reduction claim."
- No URL, artifact, or dataset accompanies the figure.
- Outcome: unsourced quantitative claim; removed rather than guessed. No external search was run because the claim is about an internal production deployment with no public artifact path.

### `https://example.com/feynman-eval-report` — REMOVED

- `fetch_content` URL `https://example.com/feynman-eval-report`, mode=readable
  - Result: IANA example-domain boilerplate ("This domain is for use in documentation examples without needing permission. This is not a service...").
  - Outcome: placeholder, not an evaluation report. Dead as a source; pointer removed.

## Citation integrity checks

- Every `[N]` in `cited-output.md` maps to a Sources entry [1]–[4].
- Every Sources entry [1]–[4] is cited at least once in the body.
- No orphan citations, no orphan sources.
- The Open questions sentence is a hedged open question, not a factual claim; it carries no citation and asserts no result ("remains an open question" replaces the draft's stronger "remains untested").
- Total sources kept: 4. Total claims removed: 4 sentences (Krishnamurthy, Okafor, 43% figure, benchmark URL). One figure corrected (GPT-4 MMLU). One identifier corrected (BERT).
