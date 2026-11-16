# Evidence notes on provenance gating for research agents

## Findings

An ensemble of residual networks reaches 3.57% top-5 error on the ImageNet test set [1].

The original Transformer reaches 28.4 BLEU on WMT 2014 English-to-German translation [2].

The GPT-4 Technical Report reports 86.4% on MMLU under a 5-shot evaluation (Table 2) [3].

BERT: Pre-training of Deep Bidirectional Transformers (arXiv:1810.04805) introduced masked-language-model (MLM) pre-training [4].

## Open questions

Whether provenance gates generalize beyond English-language scientific text is an open question; the supplied research notes contain no study that evaluates it (TODO: source needed).

## Removed or Corrected Unsupported Claims

The following material in the draft could not be traced to a source, or was contradicted by the source it cited. It has been removed or corrected:

- **Krishnamurthy et al. (2024), "Calibrated Retrieval Augmentation for Scientific Agents" (arXiv:2405.19999), and its "31% reduction in unsupported citations."** Removed. arXiv:2405.19999 resolves to an unrelated mathematics paper ("The spectral radius and the distance spectral radius of complements of block graphs," Chen, Fan, Shao & Wang, 2024). No record with the cited title or author was found in OpenAlex or Crossref, and the research notes list no source for this claim.
- **Okafor et al. (2025), "Provenance-Gated Retrieval for Autonomous Research Agents" (arXiv:2502.14444), and the "18% to 2%" fabricated-citation reduction.** Removed. arXiv:2502.14444 resolves to an unrelated NLP paper ("An Enhancement of Jiang, Z., et al.'s Compression-Based Classification Algorithm Applied to News Article Categorization," Benavides et al., 2025). The research notes also flag that this source was recorded from a search-result snippet and never opened.
- **"Feynman's verifier reduces citation errors by 43% in production deployments."** Removed. The research notes state that no source was found for this claim.
- **"Independent benchmark results are collected at https://example.com/feynman-eval-report."** Removed. The URL is a placeholder domain serving only standard example-domain notices, with no benchmark content.
- **"The GPT-4 Technical Report ... reports 92.0% on MMLU."** Corrected to 86.4% (5-shot, Table 2 of the report) [3]. The 92.0% figure is not in the report.
- **BERT's arXiv identifier.** Corrected from arXiv:1706.03762 (the Transformer paper) to arXiv:1810.04805 [4].

## Sources

1. He, K., Zhang, X., Ren, S., & Sun, J. (2015). *Deep Residual Learning for Image Recognition.* arXiv:1512.03385. https://arxiv.org/abs/1512.03385 — index record: OpenAlex W2949650786 (DOI 10.48550/arxiv.1512.03385); title, first author, and year match.
2. Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., & Polosukhin, I. (2017). *Attention Is All You Need.* arXiv:1706.03762. https://arxiv.org/abs/1706.03762 — index record: OpenAlex W2626778328 (DOI 10.48550/arxiv.1706.03762); title, first author, and year match.
3. OpenAI (2023). *GPT-4 Technical Report.* arXiv:2303.08774. https://arxiv.org/abs/2303.08774 — index record: OpenAlex W4327810158 (DOI 10.48550/arxiv.2303.08774); title, first author, and year match. MMLU figure from Table 2 (Section 4, "Capabilities").
4. Devlin, J., Chang, M.-W., Lee, K., & Toutanova, K. (2019). *BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding.* arXiv:1810.04805. https://arxiv.org/abs/1810.04805 — index record: OpenAlex W2896457183 (DOI 10.48550/arxiv.1810.04805; preprint record dated 2018, published at NAACL 2019); title, first author, and year match.
