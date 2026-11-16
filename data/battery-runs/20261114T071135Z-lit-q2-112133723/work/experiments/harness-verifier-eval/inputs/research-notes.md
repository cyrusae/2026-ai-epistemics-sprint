# Research notes — Transformer (source excerpts)

Primary source: Vaswani et al., "Attention Is All You Need", 2017.
- Abstract/landing page: https://arxiv.org/abs/1706.03762
- Full text used for excerpts: https://arxiv.org/html/1706.03762v7

## Abstract (verbatim)
"We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely. ... Our model achieves 28.4 BLEU on the WMT 2014 English-to-German translation task, improving over the existing best results, including ensembles, by over 2 BLEU. On the WMT 2014 English-to-French translation task, our model establishes a new single-model state-of-the-art BLEU score of 41.8 after training for 3.5 days on eight GPUs..."

## Section 3.2.2 (verbatim)
"In this work we employ h = 8 parallel attention layers, or heads. For each of these we use d_k = d_v = d_model/h = 64."

## Section 3.1 (verbatim)
"all sub-layers in the model, as well as the embedding layers, produce outputs of dimension d_model = 512." Encoder and decoder: "a stack of N = 6 identical layers."

## Table 3 (row values)
base: 6 layers, d_model 512, d_ff 2048, h 8, d_k 64, d_v 64, P_drop 0.1, label smoothing 0.1, 100K steps, 65M params.
big: 6 layers, d_model 1024, d_ff 4096, h 16, P_drop 0.3, 300K steps, 213M params.

## Table 2 (BLEU, newstest2014)
Transformer (base model): 27.3 EN-DE, 38.1 EN-FR.
Transformer (big): 28.4 EN-DE, 41.8 EN-FR.

## Section 5.1 (verbatim)
"We trained on the standard WMT 2014 English-German dataset consisting of about 4.5 million sentence pairs. ... For English-French, we used the significantly larger WMT 2014 English-French dataset consisting of 36M sentences..."

## Section 5.2 (verbatim)
"We trained our models on one machine with 8 NVIDIA P100 GPUs. ... We trained the base models for a total of 100,000 steps or 12 hours. ... The big models were trained for 300,000 steps (3.5 days)."

## Section 5.4 (verbatim)
"For the base model, we use a rate of P_drop = 0.1. ... we employed label smoothing of value epsilon_ls = 0.1."

## Section 6.3 (verbatim)
"we performed experiments on English constituency parsing ... Results are on Section 23 of WSJ"

## Notes on scope
- The paper reports WMT 2014 translation and WSJ 23 constituency parsing. No GLUE or SQuAD experiments appear in the paper.
- No statement about vision appears in the paper.
- Official code (tensor2tensor) is referenced in the paper's footnote, not at a project URL in the text. No code URL was verified in these notes.
