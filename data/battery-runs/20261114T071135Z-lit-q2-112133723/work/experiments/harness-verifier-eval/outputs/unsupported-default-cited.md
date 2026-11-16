# The Transformer, in brief

"Attention Is All You Need" (Vaswani et al., 2017) introduced the Transformer, an architecture based solely on attention mechanisms that dispenses with recurrence and convolutions entirely [1]. The big model reached 28.4 BLEU on the WMT 2014 English-to-German translation task, improving over the previous best results, including ensembles, by over 2 BLEU [1]. On WMT 2014 English-to-French, it established a new single-model state of the art with 41.8 BLEU after training for 3.5 days on eight GPUs [1]. Training used one machine with 8 NVIDIA P100 GPUs, and the big model ran for 300,000 steps, about 3.5 days [1]. The base model has 6 encoder and decoder layers, d_model = 512, and 8 attention heads with d_k = d_v = 64, totaling 65M parameters [1]. For the base model, the authors used dropout 0.1 and label smoothing 0.1 [1]. They also evaluated the model on English constituency parsing (Section 23 of the Wall Street Journal) [1]. The English-German training set contained about 4.5 million sentence pairs, while the English-French set contained 36M sentences [1]. The paper is at https://arxiv.org/abs/1706.03762 [1].

## Sources

1. Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., & Polosukhin, I. (2017). *Attention Is All You Need.* arXiv:1706.03762. https://arxiv.org/abs/1706.03762 (full text: https://arxiv.org/html/1706.03762v7; DOI: https://doi.org/10.48550/arXiv.1706.03762). Index records: arXiv:1706.03762 and OpenAlex W2626778328 (title, year 2017, and first author Vaswani match).

## Removed Unsupported Claims

- Corrected the English-to-German BLEU score from 41.8 to 28.4; 41.8 is the English-to-French score [1]. Corrected the improvement over prior results from 5.1 to "over 2" BLEU [1].
- Corrected the base model's attention heads from 16 to 8; 16 heads belongs to the big model [1]. Added d_v = 64 alongside d_k = 64 [1].
- Corrected the 36M sentence-pair figure: it describes the English-French training set, not English-German, which is about 4.5M pairs [1].
- Removed "mixed-precision arithmetic" — not supported by the research notes or the paper excerpts.
- Removed the SacreBLEU claim — not supported by the research notes or the paper excerpts.
- Removed the Apache 2.0 license claim — the research notes contain no code URL or license.
- Removed the GLUE and SQuAD evaluation claim; the paper reports English constituency parsing (WSJ Section 23), not GLUE or SQuAD.
- Removed the quotation "attention is all you need for vision as well" — it is not supported by the research notes or the paper excerpts.
- Corrected the link from https://arxiv.org/abs/1706.03799, which resolves to an unrelated ACL 2017 paper on physical commonsense knowledge, to https://arxiv.org/abs/1706.03762.
