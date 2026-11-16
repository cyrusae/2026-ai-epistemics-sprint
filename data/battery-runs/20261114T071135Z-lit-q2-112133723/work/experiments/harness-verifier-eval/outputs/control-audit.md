# Claim-level audit — control draft

Draft: `experiments/harness-verifier-eval/inputs/draft-control.md`
Verified output: `experiments/harness-verifier-eval/outputs/control-cited.md`
Date of verification: 2026-11-14

## Summary

- 15 factual claims identified. 13 kept as written, 1 corrected (C12, dropout
  overgeneralization), 1 kept but flagged (C5, 41.8 vs 41.0 internal
  inconsistency in the paper), 0 removed.
- 3 source URLs checked: all live and serving the expected content.
- Citation metadata cross-checked in arXiv and Semantic Scholar; both match
  title, year, and first author. Crossref title search did not return this
  paper (expected: the NeurIPS/arXiv version is not Crossref-registered under
  this title); OpenAlex anonymous search returned unrelated records, so it was
  not used for confirmation.

## Claim-by-claim audit

| ID | Claim in draft | Verdict | Supporting evidence (verbatim) | Citation |
|----|----------------|---------|-------------------------------|----------|
| C1 | "Attention Is All You Need (Vaswani et al., 2017) introduced the Transformer" | kept | arXiv abs page: title "Attention Is All You Need", submitted 12 Jun 2017, first author Ashish Vaswani. arXiv API record `1706.03762v7` returns the same title, 2017-06-12, and the eight-author list beginning "Ashish Vaswani". Abstract: "We propose a new simple network architecture, the Transformer". | [1] |
| C2 | "an architecture based solely on attention mechanisms that dispenses with recurrence and convolutions entirely" | kept | Abstract [1]: "a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely." Same sentence in HTML §Abstract [2]. | [1, 2] |
| C3 | "The big model reached 28.4 BLEU on the WMT 2014 English-to-German translation task" | kept | Abstract [1]: "Our model achieves 28.4 BLEU on the WMT 2014 English-to-German translation task". PDF Table 2 [3]: Transformer (big), EN-DE = 28.4. | [1, 3] |
| C4 | "improving over the previous best results, including ensembles, by more than 2 BLEU" | kept | Abstract [1]: "improving over the existing best results, including ensembles by over 2 BLEU." §6.1 [2]: "outperforms the best previously reported models (including ensembles) by more than 2.0 BLEU". Draft wording matches §6.1. | [1, 2] |
| C5 | "On English-to-French it established a new single-model state of the art with 41.8 BLEU" | flagged (kept) | Abstract [1]: "establishes a new single-model state-of-the-art BLEU score of 41.8". PDF Table 2 [3]: Transformer (big), EN-FR = 41.8. **Conflict:** §6.1 body text in the v7 HTML [2] says "our big model achieves a BLEU score of 41.0, outperforming all of the previously published single models". The retained figure is the one in the abstract and Table 2; the inconsistency is disclosed in a source note in the output rather than silently resolved. | [1, 3] |
| C6 | "Training used 8 NVIDIA P100 GPUs" | kept | §5.2 [2]: "We trained our models on one machine with 8 NVIDIA P100 GPUs." | [2] |
| C7 | "the big model ran for 300,000 steps, about 3.5 days" | kept | §5.2 [2]: "The big models were trained for 300,000 steps (3.5 days)." §6.1 [2]: "Training took 3.5 days on 8 P100 GPUs." | [2] |
| C8 | "The base model has 6 encoder and decoder layers" | kept | §3.1 [2]: encoder "a stack of N=6 identical layers"; decoder "also composed of a stack of N=6 identical layers". Table 3 base row: N = 6. | [2] |
| C9 | "d_model = 512" | kept | §3.1 [2]: "all sub-layers in the model, as well as the embedding layers, produce outputs of dimension d_model = 512." Table 3 base row: d_model = 512. | [2] |
| C10 | "8 attention heads with d_k = 64" | kept | §3.2.2 [2]: "we employ h = 8 parallel attention layers, or heads. For each of these we use d_k = d_v = d_model/h = 64." Table 3 base row: h = 8, d_k = 64, d_v = 64. | [2] |
| C11 | "totaling 65M parameters" | kept | Table 3 [2], base row, params column: "65" (×10^6). The big model is listed separately at 213M, so the draft's attribution to the base model is correct. | [2] |
| C12 | "The authors used dropout 0.1 and label smoothing 0.1." | **corrected** | §5.4 [2]: "For the base model, we use a rate of P_drop = 0.1. ... we employed label smoothing of value epsilon_ls = 0.1." Table 3 [2]: base P_drop = 0.1; big P_drop = 0.3. §6.1 [2]: "The Transformer (big) model trained for English-to-French used dropout rate P_drop = 0.1, instead of 0.3." The draft's unqualified statement implies 0.1 applied to all models; corrected to attribute 0.1 to the base model and add the big-model values. | [2] |
| C13 | "They also evaluated the model on English constituency parsing on Section 23 of the WSJ." | kept | §6.3 [2]: "we performed experiments on English constituency parsing"; Table 4 caption: "Results are on Section 23 of WSJ". (§6.3 also states training used the WSJ portion of the Penn Treebank, consistent with the draft's wording.) | [2] |
| C14 | "The English-German training set contained about 4.5 million sentence pairs." | kept | §5.1 [2]: "We trained on the standard WMT 2014 English-German dataset consisting of about 4.5 million sentence pairs." | [2] |
| C15 | "The paper is at https://arxiv.org/abs/1706.03762." | kept | URL fetched successfully; page is the correct paper (title, authors, abstract). | [1] |

## Source URL status

| # | URL | Status | Content check |
|---|-----|--------|---------------|
| 1 | https://arxiv.org/abs/1706.03762 | **live** | Correct content. Title "Attention Is All You Need"; 8 authors listed with Vaswani first; abstract contains 28.4 EN-DE and 41.8 EN-FR; DOI 10.48550/arXiv.1706.03762; v7 dated 2 Aug 2023. |
| 2 | https://arxiv.org/html/1706.03762v7 | **live** | Correct content. Verified §3.1, §3.2.2, §5.1, §5.2, §5.4, §6.1, §6.3, Table 3, Table 4. Contains the 41.0 vs 41.8 inconsistency noted under C5. |
| 3 | https://arxiv.org/pdf/1706.03762 | **live** | Correct content. Table 2 read directly: Transformer (big) 28.4 EN-DE / 41.8 EN-FR; Transformer (base) 27.3 / 38.1. |

No dead links, no 404s, no redirects to unrelated content.

## Citation metadata cross-check

| Index | Identifier | Record matched | Title / year / first author | Verdict |
|-------|------------|----------------|-----------------------------|---------|
| arXiv API | 1706.03762 (v7) | Preprint record | "Attention Is All You Need" / 2017-06-12 / Ashish Vaswani | match |
| Semantic Scholar | paperId 204e3073870fae3d05bcbc2f6a8e263d9b72e776; DOI 10.48550/arXiv.1706.03762 | NeurIPS 2017 venue record | "Attention is All you Need" (case variant only) / 2017 / Ashish Vaswani | match |
| Crossref | title query "Attention Is All You Need" | No matching record returned (results were unrelated book chapters/preprints) | — | not a mismatch; this venue/preprint is not Crossref-registered under this title |
| OpenAlex | title query | Anonymous search returned unrelated works (no API key; budget warning) | — | inconclusive; not used for confirmation |

## Result provenance audit

| Item | Traceable artifact | Status |
|------|--------------------|--------|
| 28.4 BLEU (big, EN-DE) | Abstract [1]; PDF Table 2 [3] | supported |
| "more than 2 BLEU" improvement | Abstract [1]; §6.1 [2] | supported |
| 41.8 BLEU (big, EN-FR) | Abstract [1]; PDF Table 2 [3] | supported (conflicting §6.1 body figure flagged) |
| 8 P100 GPUs | §5.2 [2] | supported |
| 300,000 steps / 3.5 days | §5.2 [2] | supported |
| 6 layers / d_model 512 / 8 heads / d_k 64 | §3.1, §3.2.2, Table 3 [2] | supported |
| 65M parameters | Table 3 base row [2] | supported |
| dropout 0.1, label smoothing 0.1 | §5.4, Table 3, §6.1 [2] | supported for base model; corrected in output |
| WSJ Section 23 parsing | §6.3, Table 4 [2] | supported |
| 4.5M EN-DE sentence pairs | §5.1 [2] | supported |

No figures, charts, or images are referenced by the draft. No benchmark or
dataset claims appear beyond those listed above. No claim depends on an
unavailable artifact or code path.

## Removed unsupported claims

None. Every factual claim in the draft traced to the primary paper; the only
substantive change was the C12 correction (scope of the dropout value). No
hedging language ("verified", "confirmed", "reproduced") was added.
