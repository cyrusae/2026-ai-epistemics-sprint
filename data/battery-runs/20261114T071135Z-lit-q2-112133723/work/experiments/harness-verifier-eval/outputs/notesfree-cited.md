# The Transformer, in brief

Attention Is All You Need (Vaswani et al., 2017) introduced the Transformer, an architecture based solely on attention mechanisms that dispenses with recurrence and convolutions entirely [1]. The big model reached 28.4 BLEU on the WMT 2014 English-to-German translation task, improving over the previous best results, including ensembles, by more than 2 BLEU [1]. On English-to-French it established a new single-model state of the art with 41.8 BLEU [1]. Training used 8 NVIDIA P100 GPUs, and the big model ran for 300,000 steps, about 3.5 days [2, §5.2]. The base model has 6 encoder and decoder layers, d_model = 512, and 8 attention heads with d_k = 64, totaling 65M parameters [2, §3.1, §3.2.2, Table 3]. For the base model, the authors used dropout 0.1 and label smoothing 0.1 [2, §5.4]. They also evaluated the model on English constituency parsing on Section 23 of the WSJ [2, §6.3]. The English-German training set contained about 4.5 million sentence pairs; the English-French set contained 36M sentences [2, §5.1]. The paper is at https://arxiv.org/abs/1706.03762 [1].

## Verification note

The abstract reports 41.8 BLEU for English-to-French [1], while §6.1 of the same arXiv version reports 41.0 [2]. This document states the abstract's figure and flags the discrepancy rather than resolving it.

## Removed Unsupported Claims

- The draft's statement that the authors evaluated the model on GLUE and SQuAD is not supported: the paper reports only English constituency parsing (WSJ Section 23) as an additional task [2, §6.3]. The sentence was replaced with the parsing result.
- The quoted conclusion "attention is all you need for vision as well" does not appear in the paper. The conclusion only says the authors plan to extend the Transformer to other modalities such as images, audio, and video as future work [2, §7]. The quotation was removed.
- The code/data link `https://example.com/transformer-bleu` returns HTTP 404 and is not referenced in the paper; the paper gives no project URL for code or data (tensor2tensor is mentioned only in the author-contribution footnote) [2]. The link was removed.

## Sources

[1] Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., & Polosukhin, I. (2017). *Attention Is All You Need.* arXiv:1706.03762v7. Abstract and metadata. https://arxiv.org/abs/1706.03762

[2] Vaswani, A., et al. (2017). *Attention Is All You Need.* Full text, arXiv HTML v7. Sections 3.1, 3.2.2, 5.1, 5.2, 5.4, 6.1, 6.3, 7; Table 3. https://arxiv.org/html/1706.03762v7
