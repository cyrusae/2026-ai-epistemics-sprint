# Efficiency and Evaluation Claims in Transformer Research

Transformer architectures have become a widely used sequence model [1, 2]. The original Transformer paper reports 28.4 BLEU on the WMT 2014 English-to-German translation task (Vaswani et al., 2017) [1].

BERT-Large obtains an official GLUE leaderboard score of 80.5 (Devlin et al., 2019) [3, 4], a result that remains widely cited [4].

The Transformer architecture uses multi-head self-attention to model token interactions (Vaswani et al., 2017) [1].

These results suggest that architectural design and pre-training are complementary directions.

## Sources

1. Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., & Polosukhin, I. (2017). *Attention Is All You Need.* arXiv:1706.03762. https://arxiv.org/abs/1706.03762 (DOI: 10.48550/arXiv.1706.03762). Verified live: abstract and Section 6.1/Table 2 report 28.4 BLEU on WMT 2014 English-to-German; Section 3.1–3.2.2 describes multi-head self-attention. Metadata cross-checked against OpenAlex W2626778328 (title, year, first author match).
2. OpenAlex record for *Attention Is All You Need* (2017), W2626778328. https://openalex.org/W2626778328. Verified live via OpenAlex API; cited-by count recorded at retrieval (2026-11-14) was 136,318, the basis for describing the architecture as widely used.
3. Devlin, J., Chang, M.-W., Lee, K., & Toutanova, K. (2019). *BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding.* arXiv:1810.04805. https://arxiv.org/abs/1810.04805 (DOI: 10.48550/arXiv.1810.04805). Verified live: abstract reports a GLUE score of 80.5. Metadata cross-checked against the NAACL 2019 venue record (source 4) and OpenAlex W2963341956.
4. Devlin, J., Chang, M.-W., Lee, K., & Toutanova, K. (2019). *BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding.* Proceedings of NAACL-HLT 2019, pp. 4171–4186. https://aclanthology.org/N19-1423/ (DOI: 10.18653/v1/N19-1423). Verified live: anthology page and PDF confirm title, year, authors, venue, and that "BERT LARGE obtains a score of 80.5" on the official GLUE leaderboard (Section 4.1); note that Table 1 reports a separately computed 82.1 average, so 80.5 is attributed specifically to the leaderboard score. Crossref record for DOI 10.18653/v1/n19-1423 reports 11,859 citations, the basis for describing the result as widely cited.

## Removed Unsupported Claims

- **Sparse Retrieval Augmentation (Rivera et al., 2024) and the "12.3% average improvement on LongBench across seven tasks."** The supplied source, https://arxiv.org/abs/2405.99999, returns HTTP 404, and no paper matching the title or author list was found in OpenAlex or web search. With no verifiable source, the paragraph was removed rather than retained.
- **"Feynman's verifier agent reduces citation errors by 40% in production research workflows."** No source was supplied in the research notes; the claim was removed.
- **BERT-Large GLUE figure corrected from 90.5% to 80.5.** The draft figure contradicted the cited source, which reports an official leaderboard score of 80.5 for BERT-Large [3, 4]. The wording was also narrowed: the paper's Table 1 reports a different, separately computed average of 82.1, so the claim is stated as the leaderboard score rather than a generic "average accuracy."
- **Mismatched arXiv ID not used.** The research notes flag https://arxiv.org/abs/1706.03763 as having been offered for the Transformer claim; that URL resolves to an unrelated mathematical-physics paper ("The higher spin Laplace operator in several vector variables"). The Transformer claims are instead cited to arXiv:1706.03762 [1].
