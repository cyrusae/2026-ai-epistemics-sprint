# Retrieval and attribution: a short evidence note

Retrieval-augmented generation (RAG) combines parametric memory with a non-parametric document index [1]. Lewis et al. (2020), *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks* (arXiv:2005.11401), couple a dense retriever with a sequence-to-sequence generator and report state-of-the-art results on three open-domain QA tasks [1].

On Natural Questions, the paper reports 44.5 exact-match for RAG-Sequence and 44.1 for RAG-Token, compared with 34.5 for the closed-book T5-11B baseline [1].

The Transformer architecture underlies the RAG generator, which uses BART-large, a pre-trained sequence-to-sequence transformer, as its parametric memory [1]. Vaswani et al. (2017), *Attention Is All You Need* (arXiv:1706.03762), introduced self-attention without recurrence or convolution [2].

Base editing is a precision-editing technique in genomics. Komor et al. (2016) demonstrated programmable conversion of one DNA base into another without creating a double-strand break [3].

Feynman's release notes describe an internal `/lit` research eval: in v0.5.3, run with GPT-5.6 Terra, 4 of 4 questions finished and all 44 citations resolved with matching titles (v0.5.2: 43 of 43 citations) [4].

## Removed Unsupported Claims

- **[related work], *Retrieval Calibration for Long-Context Scientific Synthesis* (arXiv:2409.99999).** The arXiv ID does not resolve; arXiv's lookup API returns it as not found. The same title/ID pair appears in the local probe fixture as a deliberately fabricated citation (`experiments/eval-scorer-probe.mjs`, probe P3) [5]. The paragraph and its claim of a 31% citation-precision improvement were removed.
- **"RAG underperforms closed-book models on all three of those tasks."** Contradicted by Table 1 of the paper: on Natural Questions, RAG-Sequence scores 44.5 EM against 34.5 for the closed-book T5-11B baseline [1]. Replaced with the reported figures.
- **"Exact-match score on Natural Questions is 94.2%."** No such figure appears in the paper; the reported NQ exact-match scores are 44.5 (RAG-Sequence) and 44.1 (RAG-Token) [1]. Removed.
- **Feynman eval page with 12 questions and citation validity rising from 71% to 100% between v0.5.0 and v0.5.3.** `https://feynman.is/docs/evals/research-quality` returns HTTP 404, and `https://feynman.is/docs/evals` also returns HTTP 404. The release notes document a different eval — 4 of 4 questions and 44 of 44 resolved citations for v0.5.3 — and give no 71% baseline or 12-question suite [4]. Replaced with the documented figures.

## Sources

1. Lewis, P., Perez, E., Piktus, A., et al. (2020). *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks.* NeurIPS 2020. arXiv:2005.11401v4. https://arxiv.org/abs/2005.11401 — arXiv record and OpenAlex W3027879771 both match title, 2020, and first author Patrick Lewis.
2. Vaswani, A., Shazeer, N., Parmar, N., et al. (2017). *Attention Is All You Need.* arXiv:1706.03762v7. https://arxiv.org/abs/1706.03762 — arXiv record and OpenAlex W2626778328 both match title, 2017, and first author Ashish Vaswani.
3. Komor, A. C., Kim, Y. B., Packer, M. S., Zuris, J. A., & Liu, D. R. (2016). *Programmable editing of a target base in genomic DNA without double-stranded DNA cleavage.* Nature. https://doi.org/10.1038/nature17946 — Crossref DOI record and PubMed 27096365 both match title, 2016, and first author Alexis C. Komor.
4. Feynman. *Release Notes* (entries for v0.5.2 and v0.5.3; accessed 2026-11-14). https://www.feynman.is/docs/reference/releases/
5. Local research artifact: `experiments/eval-scorer-probe.mjs` (probe P3) and `experiments/eval-scorer-probe-results.json`.