# The Transformer, in brief

Attention Is All You Need (Vaswani et al., 2017) [1] introduced the Transformer, an architecture based solely on attention mechanisms that dispenses with recurrence and convolutions entirely [1, 2]. The big model reached 28.4 BLEU on the WMT 2014 English-to-German translation task, improving over the previous best results, including ensembles, by more than 2 BLEU [1, 2]. On English-to-French it established a new single-model state of the art, with 41.8 BLEU [1, 2]. Training used 8 NVIDIA P100 GPUs, and the big model ran for 300,000 steps, about 3.5 days [2]. The base model has 6 encoder and decoder layers, d_model = 512, and 8 attention heads with d_k = 64, totaling 65M parameters [2]. For the base model, the authors used dropout 0.1 and label smoothing 0.1 [2]. They also evaluated the model on English constituency parsing, reporting results on Section 23 of the WSJ [2]. The English-German training set contained about 4.5 million sentence pairs [2]. The paper is at https://arxiv.org/abs/1706.03762 [1, 2].

*Note:* §6.1 of the paper gives the English-to-French big-model score as 41.0, while the abstract and Table 2 give 41.8. This article uses 41.8 (abstract and table) [1, 2].

## Sources

1. Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., & Polosukhin, I. (2017). *Attention Is All You Need.* arXiv:1706.03762v7; DOI 10.48550/arXiv.1706.03762. Abstract and metadata. https://arxiv.org/abs/1706.03762
2. Vaswani, A., et al. (2017). *Attention Is All You Need.* Full text, arXiv HTML v7 — §3.1, §3.2.2, §5.1, §5.2, §5.4, §6.1, §6.3, and Table 3. https://arxiv.org/html/1706.03762v7
