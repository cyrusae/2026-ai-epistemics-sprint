# Transformer WMT 2014 English-to-German BLEU: what the original paper reports

## Executive summary

Vaswani et al., "Attention Is All You Need," report **28.4 BLEU on WMT 2014 English-to-German (newstest2014)** for the **Transformer (big)** model, and **27.3 BLEU** for the base model. The paper's arXiv identifier is **arXiv:1706.03762**. The 28.4 figure appears in the abstract and in §6.1 as a new state of the art, and is the number almost universally quoted for the paper.

One caveat: the NeurIPS 2017 proceedings *HTML abstract page* displays 27.5 BLEU, but the NeurIPS PDF itself reports 28.4 and its Table 2 matches the arXiv table (base 27.3 / big 28.4). The 27.5 is therefore best treated as stale metadata, not as the paper's result.

## Findings

### 1. The reported score

| Model | WMT 2014 EN-DE BLEU (newstest2014) | Source |
|---|---|---|
| Transformer (base) | 27.3 | Table 2 |
| Transformer (big) | **28.4** | Abstract; §6.1; Table 2 |

The abstract states: "Our model achieves 28.4 BLEU on the WMT 2014 English-to-German translation task, improving over the existing best results, including ensembles, by over 2 BLEU." Section 6.1 repeats that the big model "establish[es] a new state-of-the-art BLEU score of 28.4" and notes training took 3.5 days on 8 P100 GPUs.

Important precision: the headline 28.4 is the **big** model. If someone asks for "the Transformer's WMT 2014 EN-DE BLEU" without qualification, 28.4 is the canonical answer, but 27.3 is the base-model number in the same table.

### 2. The arXiv ID

**arXiv:1706.03762** (cs.CL; cross-listed cs.LG). Submitted 12 June 2017; latest version v7 (2 August 2023). DOI: 10.48550/arXiv.1706.03762.

### 3. Version and venue check

The 28.4 figure is stable across arXiv v1, v3, and v7, and across the NeurIPS 2017 camera-ready PDF. This is not a number that changed in later revisions.

The observed inconsistency is confined to the NeurIPS proceedings **HTML abstract page**, which says: "Our single model with 165 million parameters, achieves 27.5 BLEU on English-to-German translation ... 41.1" on English-to-French. That text conflicts with:
- the NeurIPS PDF abstract (28.4, 41.0),
- the NeurIPS PDF Table 2 (base 27.3 / big 28.4),
- every arXiv version checked (v1, v3, v7 all say 28.4).

Inference (not directly stated by any source): the HTML abstract is an earlier/stale submission abstract retained in the proceedings metadata. It should not be used as the paper's reported result. Anyone citing "27.5" is citing the metadata page, not the paper.

A second, unrelated inconsistency: the arXiv v7 HTML body text says the EN-FR big score is 41.0, while the v7 abstract and Table 2 say 41.8. This does not affect the EN-DE answer but is a reminder that the v7 HTML rendering has small residual edits.

## Evidence-backed caveats

- BLEU is tokenizer/preprocessing-sensitive; the 28.4 is the paper's own reported number, not a independently reproduced score. No reproduction was attempted here.
- "Original Transformer paper" normally means the NeurIPS 2017 paper / arXiv v1+; all of those report 28.4 for EN-DE big.
- The base-vs-big distinction matters: 27.3 vs 28.4.
- The dataset is WMT 2014 EN-DE with newstest2014 as test set, ~4.5M sentence pairs, BPE vocabulary ~37k (per §5.1).

## Open questions

- Why the NeurIPS HTML abstract carries 27.5/41.1/165M is not documented publicly; this note only establishes that it conflicts with the PDF. A definitive answer would require NeurIPS metadata maintainers or author comment.
- Whether the v7 EN-FR 41.0 vs 41.8 body/table mismatch reflects a known erratum is unresolved; irrelevant to the EN-DE question.

## Sources

- Vaswani et al., "Attention Is All You Need," arXiv:1706.03762. https://arxiv.org/abs/1706.03762
- Full text / Table 2 (v7 HTML): https://arxiv.org/html/1706.03762v7
- arXiv v1 abstract: https://arxiv.org/abs/1706.03762v1
- NeurIPS 2017 proceedings PDF: https://papers.nips.cc/paper_files/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf
- NeurIPS 2017 proceedings abstract page (shows the conflicting 27.5): https://papers.nips.cc/paper_files/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html
