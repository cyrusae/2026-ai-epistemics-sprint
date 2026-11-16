# Inference-time methods: a short brief

Test-time compute scaling can improve model performance: with a compute-optimal allocation strategy, Snell et al. report improving the efficiency of test-time compute scaling by more than 4x relative to a best-of-N baseline, and in a FLOPs-matched evaluation they find that test-time compute can let a smaller base model outperform a 14x larger model on problems where the smaller model already attains non-trivial success rates [1]. These results are conditional on prompt difficulty and on the base model having some baseline competence; they do not establish that extra inference compute is a universal substitute for model parameters [1].

Speculative decoding was introduced by Leviathan et al. (ICML 2023; arXiv preprint 2022) as an algorithm that samples from autoregressive models faster without changing the output distribution [2]. In the reported experiments it accelerates T5-XXL by 2x–3x compared with the standard T5X implementation, with identical outputs [2]. The source does not support a 10x speedup on every model tested, nor a claim that speculative decoding is the default decoding strategy [2].

TODO: The draft's claim that sparse autoencoders recover all features in GPT-4 (arXiv:2499.99999) and thereby settle the interpretability problem could not be verified. The arXiv ID does not resolve and no source was supplied. Claim removed pending a citable source.

TODO: The draft's claim that a 2025 study found retrieval-augmented generation eliminates hallucination entirely (https://example.com/rag-study), and that the result has been widely replicated, could not be verified. The URL is a documentation placeholder domain with no study content, and no source was supplied. Claim removed pending a citable source.

Attention Is All You Need introduced the Transformer architecture [3].

TODO: The draft's claim that mixture-of-experts routing reduces inference cost by 90% had no supplied source and was removed pending a citable source.

## Sources

1. Snell, C., Lee, J., Xu, K., & Kumar, A. (2024). *Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters.* arXiv:2408.03314. https://arxiv.org/abs/2408.03314 — Link verified live on 2026-11-14. Title, year, and first author match the arXiv record and the OpenAlex record (W4406492615, DOI 10.48550/arxiv.2408.03314).
2. Leviathan, Y., Kalman, M., & Matias, Y. (2022; ICML 2023). *Fast Inference from Transformers via Speculative Decoding.* arXiv:2211.17192. https://arxiv.org/abs/2211.17192 — Link verified live on 2026-11-14. Title, year, and first author match the arXiv record and the Semantic Scholar record (arXiv ID 2211.17192).
3. Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, L., & Polosukhin, I. (2017). *Attention Is All You Need.* arXiv:1706.03762. https://arxiv.org/abs/1706.03762 — Link verified live on 2026-11-14; title, year, and first author match the arXiv record. Note: Crossref returned only anomalous 2025 "posted-content" records carrying this title and author list, not a venue record for the 2017 NeurIPS paper; the citation is therefore anchored to the arXiv record.

## Removed Unsupported Claims

- **Sparse autoencoders / GPT-4 / arXiv:2499.99999.** No such arXiv record exists (identifier not recognized by arXiv); no research note supplied any supporting paper. The associated "settles the interpretability problem" conclusion was also unsupported. Removed.
- **RAG eliminates hallucination entirely (https://example.com/rag-study), "widely replicated."** The URL is the IANA documentation placeholder domain and hosts no study; no source supplied for the replication claim. Removed.
- **"400% accuracy improvement on GSM8K."** The cited abstract (arXiv:2408.03314) reports a >4x efficiency improvement over a best-of-N baseline and outperforming a 14x larger model in a FLOPs-matched evaluation, not a 400% GSM8K accuracy gain. Replaced with the abstract's actual findings.
- **"10x speedup on every model tested" and "therefore the default decoding strategy."** The source reports 2x–3x on T5-XXL only, and makes no claim about default adoption. Replaced/removed.
- **"Mixture-of-experts routing reduces inference cost by 90%."** No source supplied. Removed.