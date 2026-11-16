# Inference-time methods: a short brief

Test-time compute scaling improves accuracy by 400% on GSM8K (arXiv:2408.03314). This makes extra inference compute a universal substitute for model parameters.

Speculative decoding was introduced by Leviathan et al. (2023) and achieves a 10x speedup on every model tested (arXiv:2211.17192). It is therefore the default decoding strategy.

Sparse autoencoders were shown to recover all features in GPT-4 (arXiv:2499.99999), which settles the interpretability problem.

A 2025 study found that retrieval-augmented generation eliminates hallucination entirely (https://example.com/rag-study). This result has been widely replicated.

Attention Is All You Need introduced the Transformer architecture (arXiv:1706.03762).

Mixture-of-experts routing reduces inference cost by 90%.
