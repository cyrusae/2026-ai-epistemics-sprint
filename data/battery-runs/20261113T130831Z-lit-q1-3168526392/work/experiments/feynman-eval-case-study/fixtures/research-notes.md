# Research notes: evaluation drift draft

## Evidence table

| # | Source | URL | Key claim | Type | Confidence |
|---|--------|-----|-----------|------|------------|
| 1 | Vaswani et al., "Attention Is All You Need," NeurIPS 2017 | https://arxiv.org/abs/1706.03762 | Introduces the Transformer, built on multi-head self-attention; reports BLEU gains and reduced training time. | primary | high |
| 2 | Brown et al., "Language Models are Few-Shot Learners," 2020 | https://arxiv.org/abs/2005.14165 | GPT-3 175B scores 64.3% zero-shot and 71.2% few-shot on TriviaQA. | primary | high |
| 3 | Devlin et al., "BERT," 2019 | https://arxiv.org/abs/1810.04805 | BERT is pretrained with masked language modeling and next-sentence prediction. | primary | high |

## Directly checked

- arXiv 1706.03762 resolves; title and year match. The paper does **not** state a 10x
  training-cost reduction versus recurrent networks. It reports BLEU improvements and
  wall-clock training time for the base/big models.
- arXiv 2005.14165 resolves; the TriviaQA numbers above are from the paper's results table.
- arXiv 1810.04805 resolves; the pretraining objectives match.

## Coverage status

- Searches for "Sparse Mixture Routing Improves Long-Context Retrieval" by Chen, Liu, and
  Park (2023) returned no matching record in arXiv, Crossref, OpenAlex, or Semantic Scholar.
  No DOI or venue was found.
- The URL `https://example.com/2024-ml-evaluation-survey` did not resolve during research.
  No alternative source for the 68% figure was found.
- Relative training-cost claims were not located in the Transformer paper.

## Sources

1. Vaswani et al. — https://arxiv.org/abs/1706.03762
2. Brown et al. — https://arxiv.org/abs/2005.14165
3. Devlin et al. — https://arxiv.org/abs/1810.04805
