# Verification log

Draft: `/work/experiments/feynman-verifier-canary/draft.md`
Notes: `/work/experiments/feynman-verifier-canary/research-notes.md`
Date: 2026-11-14

## Per-claim status

### Claim 1 — Test-time compute: "improves accuracy by 400% on GSM8K (arXiv:2408.03314)" and "universal substitute for model parameters"
**WEAKENED.**
- arXiv:2408.03314 resolves. Title "Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters"; first author Charlie Snell; 2024. Matches arXiv record and OpenAlex W4406492615 (DOI 10.48550/arxiv.2408.03314).
- The 400% / GSM8K figure does not appear in the abstract. The abstract reports >4x *efficiency* improvement in test-time compute scaling vs. a best-of-N baseline and outperforming a 14x larger model in a FLOPs-matched evaluation — different quantity and different benchmark framing. Replaced with the abstract's actual numbers, cited to [1].
- "Universal substitute for model parameters" is contradicted by the abstract's own conditionality (depends on prompt difficulty and on the smaller model having non-trivial success rates). Replaced with a hedged statement.

### Claim 2 — Speculative decoding: "Leviathan et al. (2023)", "10x speedup on every model tested", "default decoding strategy"
**WEAKENED.**
- arXiv:2211.17192 resolves. Title "Fast Inference from Transformers via Speculative Decoding"; first author Yaniv Leviathan; arXiv 2022-11-30, ICML 2023 Oral. Matches arXiv and Semantic Scholar (arXiv ID 2211.17192). Year annotated as ICML 2023 / preprint 2022.
- "10x on every model tested": unsupported. Abstract reports 2x–3x acceleration on T5-XXL versus standard T5X, with identical outputs. Replaced with 2x–3x on T5-XXL [2].
- "Default decoding strategy": normative adoption claim, no source in notes. Removed.
- "Introduced by Leviathan et al." is supported by the abstract ("we introduce speculative decoding") [2].

### Claim 3 — Sparse autoencoders "recover all features in GPT-4 (arXiv:2499.99999)", "settles the interpretability problem"
**REMOVED.**
- arXiv ID 2499.99999 does not resolve: arXiv returns "Article identifier '2499.99999' not recognized"; the arXiv API lookup also returned `not_found`. No source in the research notes. Cannot be anchored, so the paragraph is a TODO placeholder in `cited.md`.

### Claim 4 — "2025 study: RAG eliminates hallucination entirely (https://example.com/rag-study)", "widely replicated"
**REMOVED.**
- URL fetch returns the IANA example-domain placeholder notice ("This domain is for use in documentation examples... This is not a service"), i.e. no study content. No alternative URL or archived version exists because the underlying source was never real. Research notes explicitly flag it as a placeholder. No source supplied for "widely replicated." Paragraph is a TODO placeholder.

### Claim 5 — "Attention Is All You Need introduced the Transformer architecture (arXiv:1706.03762)"
**SUPPORTED.**
- arXiv:1706.03762 resolves. Title matches; first author Ashish Vaswani; 2017. Abstract: "We propose a new simple network architecture, the Transformer..." Directly supports the claim. Cited to [3].
- Cross-check caveat: Crossref search returned only 2025 `posted-content` records with this title/author list (e.g. DOI 10.65215/r5bs2d54), which look like index artifacts rather than the 2017 NeurIPS record; the canonical venue record was not matched. Disclosed in the Sources note rather than silently accepted.

### Claim 6 — "Mixture-of-experts routing reduces inference cost by 90%"
**REMOVED.**
- No source supplied (research notes Source 5 explicitly: "No source supplied"). Quantitative claim with no artifact; removed and replaced with a TODO.

## Link verification summary

| URL | Status | Notes |
|---|---|---|
| https://arxiv.org/abs/2408.03314 | live | Content matches claim-1 abstract |
| https://arxiv.org/abs/2211.17192 | live | Content matches claim-2 abstract |
| https://arxiv.org/abs/1706.03762 | live | Content matches claim-5 |
| https://arxiv.org/abs/2499.99999 | dead | Identifier not recognized; no mirror exists |
| https://example.com/rag-study | dead / placeholder | IANA example domain; no study content |

## Notes
- No new sources were introduced. The final document cites only sources present in the research notes (the three valid arXiv records).
- Unified citation numbering [1]–[3] follows order of first appearance; every inline citation has a Sources entry and every Sources entry is cited.
- No quantitative claim in `cited.md` is left unsupported: the surviving numbers (>4x efficiency, 14x larger model, 2x–3x T5-XXL speedup) come verbatim from the fetched abstracts of [1] and [2].