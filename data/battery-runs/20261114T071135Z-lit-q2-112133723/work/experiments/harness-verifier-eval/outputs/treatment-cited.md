# The Transformer, in brief

Attention Is All You Need (Vaswani et al., 2017) introduced the Transformer, an architecture based solely on attention mechanisms that dispenses with recurrence and convolutions entirely [1]. The big model reached 28.4 BLEU on the WMT 2014 English-to-German translation task, improving over the previous best results, including ensembles, by more than 2.0 BLEU [1, 2]. On English-to-French it established a new single-model state of the art with 41.8 BLEU [1, 2]. Training used 8 NVIDIA P100 GPUs, and the big model ran for 300,000 steps, about 3.5 days [1, 2]. The base model has 6 encoder and decoder layers, d_model = 512, and 8 attention heads with d_k = 64, totaling 65M parameters [2]. The authors used dropout 0.1 and label smoothing 0.1 for the base model [2]. They also evaluated the model on English constituency parsing on Section 23 of the WSJ [2]. The English-German training set contained about 4.5 million sentence pairs [2]. The paper is at https://arxiv.org/abs/1706.03762 [1].

## Corrections Applied

- English-to-German BLEU corrected from 41.8 to 28.4; 41.8 is the English-to-French score (Table 2) [2].
- Improvement margin corrected from "5.1 BLEU" to "more than 2.0 BLEU" (§6.1; abstract says "over 2 BLEU") [1, 2].
- Base-model attention heads corrected from 16 to 8; 16 heads is the big-model configuration (Table 3) [2].
- English-German training data corrected from 36M to about 4.5M sentence pairs; 36M is the English-French set (§5.1) [2].
- Paper link corrected from arXiv:1706.03799 to arXiv:1706.03762; 1706.03799 is an unrelated paper, "Verb Physics: Relative Physical Knowledge of Actions and Objects" (Forbes & Choi, 2017) [1].

## Removed Unsupported Claims

- "They also evaluated the model on GLUE and SQuAD" — the paper reports WMT 2014 translation and WSJ Section 23 constituency parsing only; "GLUE" and "SQuAD" do not occur in the text. Replaced with the constituency-parsing result (§6.3) [2].
- Quotation "attention is all you need for vision as well" — no such sentence appears in the paper; the word "vision" occurs only in reference 36 (an unrelated cited paper on computer vision). Removed as fabricated [2].
- Code/data URL `https://example.com/transformer-bleu` — returns HTTP 404 and is an example-domain placeholder, not a project URL. Removed; the research notes contain no checked code URL.

*Note:* §6.1 of the paper gives the English-French big-model score as 41.0, while the abstract and Table 2 give 41.8. This article uses 41.8 (abstract + table) and flags the internal inconsistency [1, 2].

## Sources

1. Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., & Polosukhin, I. (2017). *Attention Is All You Need.* arXiv:1706.03762 (abstract). https://arxiv.org/abs/1706.03762
2. Vaswani, A., et al. (2017). *Attention Is All You Need.* Full text, arXiv:1706.03762v7 — §3.1, §3.2.2, §5.1, §5.2, §5.4, §6.1, §6.3, Tables 2–3. https://arxiv.org/html/1706.03762v7
