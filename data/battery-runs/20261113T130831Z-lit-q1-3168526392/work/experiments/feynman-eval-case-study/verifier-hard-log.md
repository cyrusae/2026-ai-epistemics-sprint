# Verifier log: `draft-hard.md`

Research file: `experiments/feynman-eval-case-study/fixtures/research-notes-hard.md`
Output: `experiments/feynman-eval-case-study/verifier-hard-output.md`
Date checked: 2026-11-13

## Summary

- 5 sources in the final document (3 from the research notes, 2 canonical venue records used to substantiate conference/venue claims).
- All 5 final source URLs returned live content from `fetch_content`.
- 1 draft claim removed (10x training-cost figure, unsupported by any source).
- 1 draft number corrected (GPT-3 TriviaQA zero-shot: 95.2% → 64.3%).
- 2 draft years corrected (Vaswani 2019 → 2017; Devlin 2021 → 2019).
- No title/ID mismatches remain.

## Source-by-source checks

### [1] Vaswani et al., "Attention Is All You Need," arXiv:1706.03762

| Field | Value |
|---|---|
| URL | https://arxiv.org/abs/1706.03762 |
| Fetch result | **Live** (HTTP 200; abstract + submission history retrieved) |
| arXiv API record | `1706.03762`, v7; title "Attention Is All You Need"; authors Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, Illia Polosukhin; published 2017-06-12 |
| Publisher metadata | `https://arxiv.org/pdf/1706.03762v7` retrieved; abstract and Section 3.2.2 (Multi-Head Attention) confirmed in text |
| Title match | Yes |
| First-author match | Yes (Vaswani) |
| Year match | Yes — 2017 |
| Claims supported | (a) Introduces the Transformer; (b) built solely on attention mechanisms, dispensing with recurrence and convolutions; (c) uses multi-head self-attention (Section 3.2.2, h=8 heads); (d) "more parallelizable and requiring significantly less time to train" |
| Claims **not** supported | A 10x training-cost reduction — no such figure appears in the abstract or results. The only "10x" in the research corpus is GPT-3's parameter count relative to prior non-sparse models, which is unrelated. Removed. |
| Verdict | Keep. Cited for the introduction, the attention-only architecture, multi-head self-attention, and the qualitative efficiency claim. |

Note: `crossref` search for this title returned only low-quality `10.65215/*` "posted-content" records dated 2025, not the NeurIPS record. These were **not** used. The NeurIPS proceedings record [4] is the venue authority.

### [2] Brown et al., "Language Models are Few-Shot Learners," arXiv:2005.14165

| Field | Value |
|---|---|
| URL | https://arxiv.org/abs/2005.14165 |
| Fetch result | **Live** (HTTP 200; abstract, authors, submission history, full HTML retrieved) |
| arXiv API record | `2005.14165`, v4; published 2020-05-28; first author Tom B. Brown |
| Full-text check | arXiv HTML v4, Section 3.2 ("Closed Book Question Answering"): "On TriviaQA, we achieve 64.3% in the zero-shot setting, 68.0% in the one-shot setting, and 71.2% in the few-shot setting." |
| Title match | Yes |
| First-author match | Yes (Brown) |
| Year match | Yes — 2020 |
| Claims supported | GPT-3 achieves **64.3%** zero-shot accuracy on TriviaQA |
| Claims **not** supported | Draft's "95.2% zero-shot accuracy on TriviaQA" — contradicted by the paper (64.3%). Corrected. |
| Verdict | Keep. Number corrected to 64.3%. |

### [3] Devlin et al., "BERT," arXiv:1810.04805

| Field | Value |
|---|---|
| URL | https://arxiv.org/abs/1810.04805 |
| Fetch result | **Live** (HTTP 200; abstract, authors, submission history, full PDF text retrieved) |
| arXiv API record | `1810.04805`, v2; title "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding"; first author Jacob Devlin; published 2018-10-11, updated 2019-05-24 |
| Full-text check | PDF v2: "we also use a 'next sentence prediction' task"; Section 3.1 describes the "masked language model" (MLM) objective |
| Title match | Yes |
| First-author match | Yes (Devlin) |
| Year match | Yes — 2019 (v2; original preprint 2018) |
| Claims supported | BERT is pretrained with masked-language-model and next-sentence-prediction objectives |
| Verdict | Keep. |

### [4] Vaswani et al., NeurIPS 2017 proceedings record

| Field | Value |
|---|---|
| URL | https://proceedings.neurips.cc/paper_files/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html |
| Fetch result | **Live** (HTTP 200; title and abstract retrieved) |
| Record | "Attention is All you Need," NeurIPS 2017 proceedings; abstract matches the arXiv version's architecture and efficiency language |
| Title match | Yes |
| First-author match | Yes (Vaswani et al.) |
| Year/venue match | Yes — NeurIPS 2017 |
| Claims supported | The Transformer was presented at NeurIPS in 2017 |
| Verdict | Added as a corroborating venue record. Cited alongside [1] for the NeurIPS 2017 attribution. |

### [5] Devlin et al., NAACL-HLT 2019 (ACL Anthology)

| Field | Value |
|---|---|
| URL | https://aclanthology.org/N19-1423/ |
| Fetch result | **Live** (HTTP 200; full bibliographic record retrieved) |
| Record | Anthology ID N19-1423; "Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1"; pages 4171–4186; DOI 10.18653/v1/N19-1423; authors Jacob Devlin, Ming-Wei Chang, Kenton Lee, Kristina Toutanova |
| Title match | Yes |
| First-author match | Yes (Devlin) |
| Year/venue match | Yes — NAACL 2019 |
| Claims supported | BERT was published at NAACL in 2019 |
| Verdict | Added as a corroborating venue record. Cited alongside [3] for the NAACL 2019 attribution. |

Cross-check note: `crossref` independently returned DOI `10.18653/v1/n19-1423` with the same title, authors, and year 2019. The bare DOI URL `https://doi.org/10.18653/v1/n19-1423` returned HTTP 406 to the fetcher (publisher bot-blocking, not a dead link); the ACL Anthology page was used as the stable, fetchable URL.

## Claim-by-claim audit of the draft

| # | Draft sentence | Outcome | Citation |
|---|---|---|---|
| 1 | "Vaswani et al. (2019) introduced the Transformer at NeurIPS" | Corrected year to 2017 | [1][4] |
| 2 | "The Transformer replaces recurrence with multi-head self-attention" | Supported; reworded to match the paper's "dispensing with recurrence and convolutions" | [1] |
| 3 | "GPT-3 reaches 95.2% zero-shot accuracy on TriviaQA" | **Number wrong**; corrected to 64.3% | [2] |
| 4 | "The Transformer reduces training cost by 10x compared with recurrent networks" | **Removed**; no source states 10x. Replaced with the paper's qualitative claim | [1] |
| 5 | "BERT is pretrained with masked-language-model and next-sentence objectives" | Supported | [3] |
| 6 | "Devlin et al. (2021) released BERT at NAACL" | Corrected year to 2019 | [3][5] |

## Verification limitations

- `semanticscholar` returned HTTP 429 (anonymous rate limit); the call fell back to `openalex`, which has no API key configured and returned noisy, non-matching results for these titles.
- Metadata was therefore cross-checked via the arXiv API, the NeurIPS proceedings page, Crossref, and the ACL Anthology record — all of which agreed on title, first author, and year for the retained sources.
- No figure, table, chart, or computed result from the draft survived unverified; the only quantitative claims retained (64.3% TriviaQA; publication years) are directly quoted from the cited sources.
