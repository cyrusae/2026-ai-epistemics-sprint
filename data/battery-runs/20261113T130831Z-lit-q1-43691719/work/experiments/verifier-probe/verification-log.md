# Verification log — experiments/verifier-probe

Date: 2026-11-13

## Claim 1 — Transformer introduced by Vaswani et al. (2017)

- **Draft claim:** The Transformer architecture was introduced by Vaswani et al. (2017) in "Attention Is All You Need" (arXiv:1706.03762).
- **Check performed:**
  - Fetched `https://arxiv.org/abs/1706.03762` — resolved; abstract states "We propose a new simple network architecture, the Transformer, based solely on attention mechanisms."
  - arXiv metadata lookup for `1706.03762` — title "Attention Is All You Need," first author Ashish Vaswani, published 2017-06-12.
  - OpenAlex search "Attention is All you Need" — record W2626778328, DOI 10.48550/arxiv.1706.03762, publicationYear 2017, first author Ashish Vaswani.
- **Outcome:** KEPT, cited as [1]. URL live; title/year/first author consistent across arXiv and OpenAlex. (Crossref title search did not surface the canonical record because arXiv DOIs are DataCite-registered; OpenAlex served as the second index.)

## Claim 2 — LoRA reduces GPT-3 175B fine-tuning GPU memory by 47.3%

- **Draft claim:** LoRA (Hu et al., 2021, arXiv:2106.09685) reduces GPU memory during GPT-3 175B fine-tuning by 47.3%.
- **Check performed:**
  - Fetched `https://arxiv.org/abs/2106.09685` — resolved; abstract: "Compared to GPT-3 175B fine-tuned with Adam, LoRA can reduce the number of trainable parameters by 10,000 times and the GPU memory requirement by 3 times."
  - arXiv metadata lookup for `2106.09685` — title "LoRA: Low-Rank Adaptation of Large Language Models," first author Edward J. Hu, 2021.
  - OpenAlex search — record W3168867926, DOI 10.48550/arxiv.2106.09685, 2021, first author "J. Edward Hu" (name-order formatting variant of the same author).
- **Outcome:** PARTIALLY KEPT / FLAGGED. The paper and its authorship are real, but **the 47.3% figure is not supported by the source** — the abstract reports a 3× reduction (~66.7%), not 47.3%. Removed the 47.3% number and replaced it with the sourced "3×" figure, cited as [2].

## Claim 3 — Smith et al. (2024), "Scaling laws for retrieval-augmented agents," 91.2% EM on HotpotQA

- **Draft claim:** Smith et al. (2024), "Scaling laws for retrieval-augmented agents" (arXiv:2409.99999), report 91.2% exact match on HotpotQA.
- **Check performed:**
  - Fetched `https://arxiv.org/abs/2409.99999` — arXiv returns: "There is no record of an article with identifier '2409.99999'." Identifier is not a valid/resolvable arXiv record.
  - OpenAlex semantic search for the exact title — no matching work; nearest results were unrelated (ReasoningBank, "Towards a Science of Scaling Agent Systems," "Scaling Laws For Dense Retrieval").
  - OpenAlex keyword search for the exact title — no matching work.
  - arXiv lookup by ID — no record (per fetch above).
- **Outcome:** REMOVED. Fabricated citation: dead/invalid identifier and no matching publication in any index. The 91.2% HotpotQA figure was removed with it.

## Result-provenance scan

- Numeric claims in draft: "47.3%" (no source; removed, replaced with sourced 3×), "91.2%" (no source; removed), "GPT-3 175B" (supported by LoRA abstract [2]), "2024/2017/2021" years (2017 and 2021 verified; 2024 belonged to the removed fabricated citation).
- No figures, tables, charts, or benchmark tables in the draft.
- No benchmark/dataset descriptions beyond the removed HotpotQA claim.
- No code artifacts or computed results referenced.

## Orphan-citation check

- Body citations: [1], [2].
- Sources entries: [1], [2]. No orphans in either direction.
- Source URLs in final document: 2, both fetched successfully during this audit.