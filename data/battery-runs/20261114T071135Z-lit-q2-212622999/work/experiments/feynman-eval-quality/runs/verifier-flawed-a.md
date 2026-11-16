# How language models learned to attend

## Summary

The Transformer architecture replaced recurrence with self-attention [1]. BERT is pretrained with masked language modeling and next-sentence prediction [2]. GPT-3 has 175 billion parameters [3]. These three papers are foundational references for the modern language-model stack.

## What changed

The Transformer introduced a sequence-transduction architecture built solely on attention mechanisms, dispensing with recurrence and convolutions entirely [1]. On WMT 2014 English-to-German translation it reached 28.4 BLEU, and on English-to-French it reached 41.8 BLEU after 3.5 days of training on eight GPUs [1].

BERT applied this architecture to pretraining: it is pretrained with masked language modeling and next-sentence prediction, then fine-tuned with one additional output layer [2]. BERT-Large reaches 80.5% on GLUE, 93.2 F1 on SQuAD v1.1, and 83.1 F1 on SQuAD v2.0 [2]. The Transformer itself was introduced by Vaswani et al. [1], not in the BERT paper.

GPT-3 is an autoregressive language model with 175 billion parameters, trained on approximately 300 billion tokens [3]. It is evaluated in zero-shot, one-shot, and few-shot settings without gradient updates or fine-tuning [3].

## Benchmark table

| Model | Benchmark | Reported score |
|---|---|---:|
| Transformer | WMT 2014 English–German | 28.4 BLEU |
| Transformer | WMT 2014 English–French | 41.8 BLEU |
| BERT-Large | GLUE | 80.5% |
| BERT-Large | SQuAD v1.1 | 93.2 F1 |
| BERT-Large | SQuAD v2.0 | 83.1 F1 |

All values are as reported in the cited papers [1, 2]. No new experiments were run for this document.

## Conclusion

The three papers trace a shift from recurrence to attention [1], from task-specific architectures to pretrained fine-tuning [2], and toward few-shot learning at scale [3]. The reported numbers above describe those papers' own benchmarks; they do not establish that verification, or any downstream system, is solved.

## Sources

1. Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., & Polosukhin, I. (2017). *Attention Is All You Need.* NeurIPS 2017. arXiv:1706.03762. https://arxiv.org/abs/1706.03762 — URL live; title, year, and first author match arXiv, OpenAlex (W2626778328), and Semantic Scholar (204e3073870fae3d05bcbc2f6a8e263d9b72e776).
2. Devlin, J., Chang, M.-W., Lee, K., & Toutanova, K. (2019). *BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding.* NAACL-HLT 2019. arXiv:1810.04805. https://arxiv.org/abs/1810.04805 — URL live; title, year, and first author match arXiv, Semantic Scholar (DOI 10.18653/v1/N19-1423), and OpenAlex. GLUE and SQuAD figures confirmed in the abstract; the masked-language-modeling and next-sentence-prediction objectives come from the paper text as recorded in the research notes.
3. Brown, T. B., et al. (2020). *Language Models are Few-Shot Learners.* NeurIPS 2020. arXiv:2005.14165. https://arxiv.org/abs/2005.14165 — URL live; title, year, and first author match arXiv, OpenAlex (W3030163527), and Semantic Scholar. The 175-billion-parameter count and the zero-/one-/few-shot protocol are confirmed in the abstract; the ~300-billion-token figure comes from the paper text as recorded in the research notes.

## Removed Unsupported Claims

- **Fabricated study (arXiv:2401.99999).** The draft's 2024 Zhang et al. claim that sparse mixture-of-experts routing improves low-resource translation by 11.4 BLEU, and the follow-up 88.1% SQuAD 2.0 result attributed to the same identifier, were removed. arXiv returns "There is no record of an article with identifier '2401.99999'." The real SQuAD v2.0 figure in the research notes is BERT-Large at 83.1 F1 [2].
- **Feynman verifier metric.** "Reduced citation errors by 73% across 1,200 runs" had no source in the research notes and was removed.
- **Feynman-Verify benchmark table.** The MMLU/GSM8K table (Feynman-Verify 94.2/91.7 vs. Baseline 88.0/84.3) had no artifact, script, or source and was removed. The table now reports only numbers stated in the three primary papers [1, 2].
- **Corrected figures.** BERT-Large GLUE was corrected from 92.4% to 80.5% [2]; GPT-3 training data was corrected from 1 trillion to approximately 300 billion tokens [3].
- **Corrected attribution.** "The Transformer was introduced in the BERT paper" was corrected: the Transformer was introduced by Vaswani et al. [1], and BERT builds on it [2].
- **Conclusion.** "Verification is solved, and the numbers above prove it" was removed; the cited papers contain no verification results.
