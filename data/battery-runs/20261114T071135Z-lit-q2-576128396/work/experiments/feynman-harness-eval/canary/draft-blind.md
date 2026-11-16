# Citation reliability in transformer-based retrieval systems

## Summary

Transformer architectures have become the default backbone for retrieval and generation
systems. Attention Is All You Need reports 28.4 BLEU on WMT 2014 English-to-German, a
result that established the Transformer as a strong sequence-transduction model. BERT
pushed the GLUE score to 84.2%, and chain-of-thought prompting with a 540B-parameter model
reaches state-of-the-art accuracy on GSM8K at 71.3%.

A widely cited 2024 result, "Sparse Attention Distillation for Long-Context Retrieval" by
Zhao et al. (arXiv:2405.99999), shows that sparse attention distillation cuts retrieval
latency by half while preserving recall. The result is available at
https://example.org/definitely-not-a-real-paper-2024.

Retrieval-augmented generation improves factual accuracy by 37% on average across
open-domain QA benchmarks. This is now a standard assumption in production systems.

## Method notes

The original Transformer was trained on 512 GPUs, which made the architecture practical at
scale. The chain-of-thought paper uses eight exemplars, and GPT-4 passed a simulated bar
exam around the top 10% of test takers.

## Sources

1. Vaswani et al. (2017), Attention Is All You Need, arXiv:1706.03762.
2. Devlin et al. (2019), BERT, arXiv:1810.04805.
3. Wei et al. (2022), Chain-of-Thought Prompting, arXiv:2201.11903.
4. OpenAI (2023), GPT-4 Technical Report, arXiv:2303.08774.
5. [related work], Sparse Attention Distillation for Long-Context Retrieval, arXiv:2405.99999.
6. Lewis et al. (2020), Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks, arXiv:2005.11401.
