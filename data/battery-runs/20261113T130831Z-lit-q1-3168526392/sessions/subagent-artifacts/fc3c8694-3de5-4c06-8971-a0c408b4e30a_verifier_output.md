# Evaluation drift in production ML

*(Citation-checked draft. Two claims in the original draft could not be traced to any source and have been removed; see "Removed Unsupported Claims".)*

The Transformer architecture replaces recurrence with multi-head self-attention [1]. Vaswani et al. (2017) introduced the Transformer at NeurIPS [1]. GPT-3, a 175-billion-parameter autoregressive language model, reaches 64.3% zero-shot and 71.2% few-shot accuracy on TriviaQA [2]. The Transformer is reported to be more parallelizable and to require significantly less time to train than the recurrent and convolutional sequence-transduction models that dominated the field, although the paper does not quantify this as a fixed cost reduction [1]. BERT is pretrained with masked-language-model and next-sentence-prediction objectives [3].

## Removed Unsupported Claims

Five defects in the draft were checked against the research notes and the primary sources. All five are flagged, not silently dropped.

1. **"Vaswani et al. (2019)"** — wrong year. arXiv 1706.03762 was submitted 12 June 2017 and the paper appeared at NeurIPS 2017. Corrected to 2017 [1].
2. **"Chen, Liu, and Park (2023) report that sparse mixture routing improves long-context retrieval by 41%"** — removed. arXiv:2309.99999 returns "There is no record of an article with identifier '2309.99999'", and the research notes record no matching title in arXiv, Crossref, OpenAlex, or Semantic Scholar, with no DOI or venue found. No support exists for the paper, the authors, or the 41% figure. This claim needs to be re-sourced from scratch before it can return.
3. **"GPT-3 reaches 95.2% zero-shot accuracy on TriviaQA"** — wrong number. The GPT-3 paper reports 64.3% zero-shot, 68.0% one-shot, and 71.2% few-shot on TriviaQA (Table 3.3). Corrected to the reported values [2].
4. **"A 2024 industry survey found that 68% of ML teams report evaluation drift"** — removed. `https://example.com/2024-ml-evaluation-survey` resolves only to the IANA example-domain placeholder page ("This domain is for use in documentation examples… This is not a service"), and no alternative source for the 68% figure was found. No survey, sample size, or methodology is available, so the number cannot stand. The document title was also softened from "a 2024 survey" to avoid asserting a survey that could not be located.
5. **"Transformers reduce training cost by 10x compared with recurrent networks"** — not in the source. The paper claims the model is "more parallelizable and requiring significantly less time to train" and describes its English–French result as "a small fraction of the training costs of the best models from the literature", but states no 10x (or any other fixed) cost ratio. Replaced with the qualitative claim the paper does make [1].

TODO: the draft's stated subject — evaluation drift between offline benchmarks and production behavior — currently has no supporting source at all. Any reintroduction of that thesis needs a primary survey or study with a resolvable URL and an inspectable sample.

## Sources

1. Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., & Polosukhin, I. "Attention Is All You Need." NeurIPS 2017 (arXiv:1706.03762; DOI 10.48550/arXiv.1706.03762). https://arxiv.org/abs/1706.03762
2. Brown, T. B., Mann, B., Ryder, N., et al. "Language Models are Few-Shot Learners." 2020 (arXiv:2005.14165; DOI 10.48550/arXiv.2005.14165). https://arxiv.org/abs/2005.14165
3. Devlin, J., Chang, M.-W., Lee, K., & Toutanova, K. "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding." NAACL 2019 (arXiv:1810.04805, first posted 2018; DOI 10.48550/arXiv.1810.04805). https://arxiv.org/abs/1810.04805