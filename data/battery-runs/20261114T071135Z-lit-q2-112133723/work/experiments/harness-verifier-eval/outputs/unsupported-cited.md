# The Transformer, in brief

Attention Is All You Need (Vaswani et al., 2017) introduced the Transformer, an architecture based solely on attention mechanisms that dispenses with recurrence and convolutions entirely [1, 2]. The big model reached 28.4 BLEU on the WMT 2014 English-to-German translation task, improving over the previous best results, including ensembles, by over 2 BLEU [1, 2]. On English-to-French it established a new single-model state of the art with 41.8 BLEU [1, 2]. Training used 8 NVIDIA P100 GPUs [2], and the big model ran for 300,000 steps, about 3.5 days [2]. The base model has 6 encoder and decoder layers, d_model = 512, and 8 attention heads with d_k = 64, totaling 65M parameters [2]. For the base model the authors used dropout 0.1 and label smoothing 0.1 [2]. The English-German training set contained about 4.5 million sentence pairs, while the English-French set contained 36M sentences [2]. The paper is at https://arxiv.org/abs/1706.03762 [1].

## Removed or corrected unsupported claims

The following statements from the source draft were not supported by the research notes or by the cited paper, and were removed or corrected:

- "41.8 BLEU on the WMT 2014 English-to-German" — corrected; 41.8 is the English-to-French score, and the English-to-German score for the big model is 28.4 [1, 2].
- "improving ... by 5.1 BLEU" — corrected; the paper reports an improvement of over 2 BLEU [1, 2].
- "mixed-precision arithmetic" — removed; the supplied notes and the cited page sections do not state the training precision.
- "16 attention heads" for the base model — corrected to 8; 16 heads belongs to the big model [2].
- "BLEU scores were computed with SacreBLEU" — removed; not stated in the paper or the notes.
- "released their code under the Apache 2.0 license" — removed; the notes record no verified code or license URL.
- "evaluated the model on GLUE and SQuAD" — removed; the paper reports WMT 2014 translation and WSJ Section 23 constituency parsing, with no GLUE or SQuAD experiments [1, 2].
- The quoted conclusion "attention is all you need for vision as well" — removed; no such statement appears in the paper.
- "The English-German training set contained 36M sentence pairs" — corrected; 36M is the English-French dataset size, and English-German is about 4.5 million pairs [2].
- The link `https://arxiv.org/abs/1706.03799` — corrected to `https://arxiv.org/abs/1706.03762`; the former resolves to an unrelated paper on physical commonsense inference [1].

Note on internal inconsistency: the v7 body text of Section 6.1 states 41.0 BLEU for English-to-French, while the abstract and Table 2 state 41.8; this document follows the abstract and Table 2 [1, 2].

## Sources

1. Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., & Polosukhin, I. (2017). *Attention Is All You Need.* arXiv:1706.03762. https://arxiv.org/abs/1706.03762 (record verified at https://openalex.org/W2626778328)
2. Vaswani et al., *Attention Is All You Need*, full text v7 (HTML): https://arxiv.org/html/1706.03762v7
