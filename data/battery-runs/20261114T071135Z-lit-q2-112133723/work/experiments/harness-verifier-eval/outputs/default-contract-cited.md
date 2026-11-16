# The Transformer, in brief

Attention Is All You Need (Vaswani et al., 2017) introduced the Transformer, an architecture based solely on attention mechanisms that dispenses with recurrence and convolutions entirely [1]. The big model reached 28.4 BLEU on the WMT 2014 English-to-German translation task, improving over the previous best results, including ensembles, by more than 2 BLEU [1, 2]. On English-to-French, the abstract reports a new single-model state of the art at 41.8 BLEU [1], although §6.1 of the HTML full text states 41.0 BLEU [2] — an internal inconsistency in the paper. Training used 8 NVIDIA P100 GPUs, and the big model ran for 300,000 steps, about 3.5 days [2]. The base model has 6 encoder and decoder layers, d_model = 512, and 8 attention heads with d_k = 64, totaling 65M parameters [2]. For the base model, the authors used dropout 0.1 and label smoothing 0.1 [2]. They also evaluated the model on English constituency parsing on Section 23 of the WSJ [2].

## Sources

1. Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., & Polosukhin, I. (2017). *Attention Is All You Need*. arXiv:1706.03762. https://arxiv.org/abs/1706.03762
2. Vaswani, A., et al. (2017). *Attention Is All You Need* (full text, arXiv HTML v7). https://arxiv.org/html/1706.03762v7

## Source Verification Notes

- arXiv:1706.03762 matched the arXiv API record for "Attention Is All You Need" (2017; first author Ashish Vaswani) and the OpenAlex record W2626778328 (DOI 10.48550/arxiv.1706.03762, same title, year, and first author). The arXiv record notes version 7.
- Crossref returned only unrelated 2025 posted-content records for the title query, so the DOI cross-check relied on OpenAlex.
- The draft's `https://arxiv.org/abs/1706.03799` resolves to an unrelated paper, "Verb Physics: Relative Physical Knowledge of Actions and Objects"; it was replaced with the correct `https://arxiv.org/abs/1706.03762`.
- The draft's `https://example.com/transformer-bleu` resolves to an IANA documentation placeholder ("This domain is for use in documentation examples... This is not a service"), not project code or data; it was removed.

## Removed Unsupported Claims

- **"41.8 BLEU on the WMT 2014 English-to-German translation task ... by 5.1 BLEU"** — 41.8 BLEU is the English-to-French result; the English-to-German big-model result is 28.4 BLEU, an improvement of more than 2 BLEU. Corrected in the text.
- **Base model "16 attention heads"** — the base model uses h = 8 heads; 16 heads is the big-model configuration in Table 3. Corrected in the text.
- **English-German training set "36M sentence pairs"** — 36M is the English-French dataset size; English-German has about 4.5 million sentence pairs. Corrected by removing the sentence-pair count.
- **"evaluated the model on GLUE and SQuAD"** — no GLUE or SQuAD experiments appear in the paper. Removed.
- **Quote "attention is all you need for vision as well"** — no such statement or vision discussion appears in the paper. Removed.
- **Code/data URL** — the example.com URL is a documentation placeholder, not a project link. Removed.
- **arXiv link 1706.03799** — points to an unrelated paper. Replaced with 1706.03762.
