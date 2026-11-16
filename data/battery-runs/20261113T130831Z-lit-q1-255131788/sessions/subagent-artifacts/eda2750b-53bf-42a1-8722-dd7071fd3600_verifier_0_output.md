# Evidence notes on provenance gating for research agents

## Findings

An ensemble of residual networks reaches 3.57% top-5 error on the ImageNet test set (He et al., 2015, arXiv:1512.03385) [1].

The original Transformer reaches 28.4 BLEU on WMT 2014 English-to-German translation (Vaswani et al., 2017, arXiv:1706.03762) [2].

The GPT-4 Technical Report (arXiv:2303.08774) reports 86.4% on MMLU under 5-shot evaluation [3].

BERT: Pre-training of Deep Bidirectional Transformers (Devlin et al., 2019, arXiv:1810.04805) introduced the masked language model (MLM) pre-training objective [4].

## Open questions

TODO: the research material supplied for this note contains no evidence on whether provenance gates generalize beyond English-language scientific text; the question remains open.

## Removed Unsupported Claims

The following material from the draft could not be supported and was removed or corrected.

- **Removed — Krishnamurthy et al. (2024), "Calibrated Retrieval Augmentation for Scientific Agents" (arXiv:2405.19999), and its claimed 31% reduction in unsupported citations.** The arXiv ID resolves to a different paper: Chen, Fan, Shao & Wang, "The spectral radius and the distance spectral radius of complements of block graphs" (math.CO) [5]. The claimed paper, authors, and figure do not exist at that ID and are absent from the research notes.
- **Removed — Okafor et al. (2025), "Provenance-Gated Retrieval for Autonomous Research Agents" (arXiv:2502.14444), and its claimed reduction of fabricated citations from 18% to 2%.** The arXiv ID resolves to Benavides, Masapol, Morano & Cortez, "An Enhancement of Jiang, Z., et al.'s Compression-Based Classification Algorithm Applied to News Article Categorization" [6]. The research notes also record that this source came from a search-result snippet and that the URL was never opened.
- **Removed — "Feynman's verifier reduces citation errors by 43% in production deployments."** No source exists for this figure; the research notes explicitly state that no source was found.
- **Removed — "Independent benchmark results are collected at https://example.com/feynman-eval-report."** The URL returns HTTP 404 and resolves only to the generic "Example Domain" placeholder page [7].
- **Corrected — GPT-4 MMLU score.** The draft's 92.0% is not the MMLU result. Table 2 of the GPT-4 Technical Report gives 86.4% for MMLU (5-shot); 92.0% is the GSM-8K entry in the same table [3].
- **Corrected — BERT arXiv ID.** The draft cited arXiv:1706.03762, which is "Attention Is All You Need" [2]. BERT is arXiv:1810.04805 [4].

After these removals, this note contains no verified evidence on provenance gating; the title and section structure are retained from the draft.

## Sources

1. He, K., Zhang, X., Ren, S., & Sun, J. (2015). *Deep Residual Learning for Image Recognition.* arXiv:1512.03385. https://arxiv.org/abs/1512.03385 — Abstract and §4.1 report 3.57% top-5 error on the ImageNet test set for an ensemble. Cross-checked against OpenAlex W2949650786 (DOI 10.48550/arXiv.1512.03385).
2. Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., & Polosukhin, I. (2017). *Attention Is All You Need.* arXiv:1706.03762. https://arxiv.org/abs/1706.03762 — Abstract reports 28.4 BLEU on WMT 2014 English-to-German. Cross-checked against OpenAlex W2626778328 (DOI 10.48550/arXiv.1706.03762).
3. OpenAI (2023). *GPT-4 Technical Report.* arXiv:2303.08774. https://arxiv.org/abs/2303.08774 — Table 2 reports 86.4% on MMLU (5-shot); 92.0% is the GSM-8K entry. Cross-checked against OpenAlex W4327810158 (DOI 10.48550/arXiv.2303.08774).
4. Devlin, J., Chang, M.-W., Lee, K., & Toutanova, K. (2019). *BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding.* arXiv:1810.04805. https://arxiv.org/abs/1810.04805 — §3.1 introduces the "masked language model" (MLM) pre-training objective. Cross-checked against OpenAlex W2896457183 (DOI 10.48550/arXiv.1810.04805).
5. Chen, X., Fan, D., Shao, R., & Wang, G. (2024). *The spectral radius and the distance spectral radius of complements of block graphs.* arXiv:2405.19999. https://arxiv.org/abs/2405.19999 — Record retrieved to establish that arXiv:2405.19999 is not the paper cited in the draft.
6. Benavides, S. L. C., Masapol, C. A. F., Morano, J. C., & Cortez, D. M. A. (2025). *An Enhancement of Jiang, Z., et al.'s Compression-Based Classification Algorithm Applied to News Article Categorization.* arXiv:2502.14444. https://arxiv.org/abs/2502.14444 — Record retrieved to establish that arXiv:2502.14444 is not the paper cited in the draft.
7. https://example.com/feynman-eval-report — checked and found dead (HTTP 404, generic "Example Domain" placeholder page). No archived or alternative version located; the claim depending on it was removed.