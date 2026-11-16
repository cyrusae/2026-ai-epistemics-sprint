# Evidence notes on provenance gating for research agents

## Findings

An ensemble of residual networks reaches 3.57% error on the ImageNet test set (He et al., 2015, arXiv:1512.03385) [1].

The original Transformer reaches 28.4 BLEU on the WMT 2014 English-to-German translation task (Vaswani et al., 2017, arXiv:1706.03762) [2].

The GPT-4 Technical Report reports 86.4% on MMLU (5-shot) in its academic-benchmark results table (OpenAI, 2023, arXiv:2303.08774, Table 2) [3].

BERT: Pre-training of Deep Bidirectional Transformers (Devlin et al., 2019, arXiv:1810.04805) introduced masked-language-model pretraining [4].

## Open questions

Whether provenance gates generalize beyond English-language scientific text remains an open question.

## Removed Unsupported Claims

- Removed the claim that Krishnamurthy et al. (2024), "Calibrated Retrieval Augmentation for Scientific Agents" (arXiv:2405.19999), report a 31% reduction in unsupported citations. arXiv:2405.19999 resolves to an unrelated mathematics paper ("The spectral radius and the distance spectral radius of complements of block graphs"), and no matching record was found in Semantic Scholar or Crossref.
- Removed the claim that Okafor et al. (2025), "Provenance-Gated Retrieval for Autonomous Research Agents" (arXiv:2502.14444), found that provenance gates cut fabricated citations from 18% to 2%. arXiv:2502.14444 resolves to an unrelated text-classification paper, and no matching record was found in Semantic Scholar or Crossref.
- Corrected the GPT-4 MMLU figure from 92.0% to 86.4% [3]. In the GPT-4 Technical Report, 92.0% is the GSM-8K result, not MMLU; MMLU is reported as 86.4% (5-shot) in Table 2.
- Corrected the BERT citation: the draft cited arXiv:1706.03762, which is "Attention Is All You Need"; BERT is arXiv:1810.04805 [4].
- Removed the claim that "Feynman's verifier reduces citation errors by 43% in production deployments." No source for this figure exists in the research notes.
- Removed the pointer to "Independent benchmark results ... at https://example.com/feynman-eval-report." The URL is an IANA documentation-example placeholder and hosts no evaluation report.

## Sources

1. He, K., Zhang, X., Ren, S., & Sun, J. (2015). Deep Residual Learning for Image Recognition. arXiv:1512.03385. https://arxiv.org/abs/1512.03385 (published version DOI: 10.1109/CVPR.2016.90)
2. Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., & Polosukhin, I. (2017). Attention Is All You Need. arXiv:1706.03762. https://arxiv.org/abs/1706.03762
3. OpenAI (2023). GPT-4 Technical Report. arXiv:2303.08774. https://arxiv.org/abs/2303.08774
4. Devlin, J., Chang, M.-W., Lee, K., & Toutanova, K. (2019). BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding. arXiv:1810.04805. https://arxiv.org/abs/1810.04805 (published version DOI: 10.18653/v1/N19-1423)
