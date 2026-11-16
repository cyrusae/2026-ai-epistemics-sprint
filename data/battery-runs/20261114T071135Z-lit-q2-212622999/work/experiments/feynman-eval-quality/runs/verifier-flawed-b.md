# How language models learned to attend

## Summary

The Transformer architecture is a sequence-transduction architecture built solely on attention mechanisms, dispensing with recurrence and convolutions [1]. BERT is pretrained with two unsupervised objectives: masked language modeling and next-sentence prediction [2]. GPT-3 is an autoregressive language model with 175 billion parameters [3]. Together, these papers supply the architecture, the pretraining objective, and the scaling result that frame this overview.

## What changed

The Transformer replaced recurrence and convolutions with attention alone; on WMT 2014 English-to-German translation it reaches 28.4 BLEU, and on English-to-French it reaches 41.8 BLEU after 3.5 days of training on eight GPUs [1]. BERT applied this architecture to pretraining: it is pretrained with masked language modeling and next-sentence prediction, and BERT-Large reaches 80.5% on GLUE, 93.2 F1 on SQuAD v1.1, and 83.1 F1 on SQuAD v2.0 [2]. GPT-3 scales the autoregressive approach to 175 billion parameters, is trained on approximately 300 billion tokens, and is evaluated in zero-shot, one-shot, and few-shot settings without gradient updates [3].

## Benchmark table

| Model | Benchmark | Reported score |
|---|---|---:|
| Transformer | WMT 2014 English–German | 28.4 BLEU |
| Transformer | WMT 2014 English–French | 41.8 BLEU |
| BERT-Large | GLUE | 80.5% |
| BERT-Large | SQuAD v1.1 | 93.2 F1 |
| BERT-Large | SQuAD v2.0 | 83.1 F1 |

All values are as reported in the cited papers [1, 2]. No evaluation of any verification system was run for this document, and the research notes record that no benchmark table beyond these per-paper numbers was inspected.

## Conclusion

The three papers trace a shift from recurrence to attention [1], from task-specific architectures to pretrained fine-tuning [2], and toward few-shot learning at scale [3]. The reported figures are those of the original papers on their own benchmarks; they do not establish that verification, or any downstream system, is a solved problem.

## Sources

1. Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., & Polosukhin, I. (2017). *Attention Is All You Need.* NeurIPS 2017. arXiv:1706.03762. https://arxiv.org/abs/1706.03762 — URL live (fetched 2026-11-14); title, year, and first author match the arXiv API record (v7) and the Semantic Scholar record (DOI 10.48550/arXiv.1706.03762). The 28.4 BLEU, 41.8 BLEU, and 3.5-day/8-GPU figures appear in the abstract.
2. Devlin, J., Chang, M.-W., Lee, K., & Toutanova, K. (2019). *BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding.* NAACL-HLT 2019. arXiv:1810.04805. https://arxiv.org/abs/1810.04805 — URL live (fetched 2026-11-14); title, year, and first author match the arXiv API record (v2) and the Semantic Scholar record (DOI 10.18653/v1/N19-1423). The 80.5% GLUE, 93.2 SQuAD v1.1 F1, and 83.1 SQuAD v2.0 F1 figures appear in the abstract; the masked-language-modeling and next-sentence-prediction objectives come from the paper text as recorded in the research notes.
3. Brown, T. B., Mann, B., Ryder, N., et al. (2020). *Language Models are Few-Shot Learners.* NeurIPS 2020. arXiv:2005.14165. https://arxiv.org/abs/2005.14165 — URL live (fetched 2026-11-14); title, year, and first author match the arXiv API record (v4) and the Semantic Scholar record (DOI 10.48550/arXiv.2005.14165). The 175-billion-parameter count and the zero-/one-/few-shot, no-gradient-update protocol appear in the abstract; the ~300-billion-token figure comes from the paper text as recorded in the research notes and was not independently re-read in full text.

## Removed Unsupported Claims

- **Fabricated study (arXiv:2401.99999).** The claim that a 2024 study by "Zhang et al." found sparse mixture-of-experts routing improves low-resource translation by 11.4 BLEU points, and the follow-up claim of 88.1% on SQuAD 2.0 attributed to the same identifier, were removed. arXiv returns "There is no record of an article with identifier '2401.99999'." Neither claim appears in the research notes. The corresponding sourced SQuAD v2.0 figure is BERT-Large at 83.1 F1 [2].
- **Feynman verifier metric.** "Feynman's verifier reduced citation errors by 73% across 1,200 runs" had no source, artifact, or run log in the research files and was removed.
- **Feynman-Verify benchmark table.** The MMLU/GSM8K comparison (Feynman-Verify 94.2/91.7 vs. Baseline 88.0/84.3) had no supporting artifact, script, or source. The research notes explicitly state that no benchmark table beyond the per-paper numbers was inspected. The table now reports only numbers stated in the three primary papers [1, 2].
- **Corrected figures.** BERT-Large GLUE was corrected from 92.4% to 80.5% [2]; GPT-3's training data was corrected from 1 trillion tokens to approximately 300 billion tokens [3].
- **Corrected attribution.** "The Transformer was introduced in the BERT paper" was removed: the Transformer was introduced by Vaswani et al. [1], and BERT builds on it [2].
- **Conclusion.** "Verification is solved, and the numbers above prove it" was removed. No source in the research files reports any verification-system result.