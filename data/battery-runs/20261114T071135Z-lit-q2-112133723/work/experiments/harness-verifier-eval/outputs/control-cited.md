# The Transformer, in brief

Attention Is All You Need (Vaswani et al., 2017) [1] introduced the Transformer, an architecture based solely on attention mechanisms that dispenses with recurrence and convolutions entirely [1, 2]. The big model reached 28.4 BLEU on the WMT 2014 English-to-German translation task [1, 3], improving over the previous best results, including ensembles, by more than 2 BLEU [1, 2]. On English-to-French it established a new single-model state of the art with 41.8 BLEU [1, 3]. Training used 8 NVIDIA P100 GPUs, and the big model ran for 300,000 steps, about 3.5 days [2]. The base model has 6 encoder and decoder layers [2], d_model = 512 [2], and 8 attention heads with d_k = 64 [2], totaling 65M parameters [2]. For the base model the authors used dropout 0.1 and label smoothing 0.1 [2]; the big models used dropout 0.3, except the English-to-French big model, which used 0.1 [2]. They also evaluated the model on English constituency parsing on Section 23 of the WSJ [2]. The English-German training set contained about 4.5 million sentence pairs [2]. The paper is at https://arxiv.org/abs/1706.03762 [1].

## Sources

1. Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., & Polosukhin, I. (2017). *Attention Is All You Need*. arXiv:1706.03762, abstract page (v7). https://arxiv.org/abs/1706.03762
2. Vaswani, A., et al. (2017). *Attention Is All You Need*, full text v7: §3.1, §3.2.2, §5.1, §5.2, §5.4, §6.1, §6.3, and Tables 3–4. https://arxiv.org/html/1706.03762v7
3. Vaswani, A., et al. (2017). *Attention Is All You Need*, PDF: Table 2 (newstest2014 BLEU). https://arxiv.org/pdf/1706.03762

## Source note

The abstract [1] and Table 2 [3] both report 41.8 BLEU for the big model on English-to-French. The body text of §6.1 in the v7 HTML [2] instead says "our big model achieves a BLEU score of 41.0". The draft's 41.8 figure follows the abstract and Table 2; the internal inconsistency in the paper is recorded here rather than silently resolved.
