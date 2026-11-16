# Retrieval and attribution: a short evidence note

Retrieval-augmented generation (RAG) combines parametric memory with a non-parametric document index. Lewis et al. (2020), *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks* (arXiv:2005.11401), couple a dense retriever with a sequence-to-sequence generator and set state-of-the-art results on three open-domain QA tasks.

The same paper reports that RAG underperforms closed-book models on all three of those tasks, and that its exact-match score on Natural Questions is 94.2%.

A newer line of work argues that retrieval calibration is the main bottleneck. [related work], *Retrieval Calibration for Long-Context Scientific Synthesis* (arXiv:2409.99999), report that calibration improves citation precision by 31% over an uncalibrated retriever.

The Transformer architecture is the substrate for both systems. Vaswani et al. (2017), *Attention Is All You Need* (arXiv:1706.03762), introduced self-attention without recurrence or convolution.

Base editing is a related precision-editing technique. Komor et al. (2016) demonstrated programmable conversion of one DNA base to another without creating a double-strand break.

Feynman's research-quality eval is documented at https://feynman.is/docs/evals/research-quality and contains 12 questions. Across that suite, citation validity rose from 71% to 100% between versions 0.5.0 and 0.5.3.

## Sources

1. Lewis et al. (2020), arXiv:2005.11401
2. [related work], arXiv:2409.99999
3. Vaswani et al. (2017), arXiv:1706.03762
4. https://feynman.is/docs/evals/research-quality
