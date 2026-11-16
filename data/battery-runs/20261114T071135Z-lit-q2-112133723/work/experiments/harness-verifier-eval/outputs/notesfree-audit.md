# Audit — `draft-treatment.md` (notes-free arm)

Date: 2026-11-14. Evidence below comes only from primary sources fetched in this run (arXiv landing page, arXiv HTML full text v7, the arXiv PDF, and arXiv/OpenAlex/Semantic Scholar/Crossref lookups). `inputs/research-notes.md` was not used as evidence.

## Claim-level audit

| ID | Claim in draft (verbatim or close paraphrase) | Verdict | Supporting evidence and action |
|---|---|---|---|
| C1 | "Attention Is All You Need (Vaswani et al., 2017) introduced the Transformer" | kept | arXiv 1706.03762v7 title "Attention Is All You Need", first author Ashish Vaswani, submitted 2017-06-12; OpenAlex W2626778328 and Semantic Scholar 204e3073870fae3d05bcbc2f6a8e263d9b72e776 match title, year, first author. |
| C2 | "an architecture based solely on attention mechanisms that dispenses with recurrence and convolutions entirely" | kept | Abstract, verbatim: "a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely." |
| C3 | "The big model reached 41.8 BLEU on the WMT 2014 English-to-German translation task" | corrected | Both the abstract and §6.1 report 28.4 BLEU for English-to-German ("Our model achieves 28.4 BLEU on the WMT 2014 English-to-German translation task"). 41.8 is the English-to-French score. Corrected to 28.4. |
| C4 | "improving over the previous best results, including ensembles, by 5.1 BLEU" | corrected | Abstract: "improving over the existing best results, including ensembles by over 2 BLEU." §6.1: "outperforms the best previously reported models (including ensembles) by more than 2.0 BLEU." No 5.1 figure appears. Corrected to "more than 2 BLEU." |
| C5 | "On English-to-French it established a new single-model state of the art" (draft gives no EN-FR number) | flagged | Abstract: "establishes a new single-model state-of-the-art BLEU score of 41.8." However §6.1 of the same version says "our big model achieves a BLEU score of 41.0." Retained with the abstract's 41.8 and an explicit discrepancy note; the 41.0/41.8 conflict is unresolved in the paper itself. |
| C6 | "Training used 8 NVIDIA P100 GPUs" | kept | §5.2: "We trained our models on one machine with 8 NVIDIA P100 GPUs." |
| C7 | "the big model ran for 300,000 steps, about 3.5 days" | kept | §5.2: "The big models were trained for 300,000 steps (3.5 days)." |
| C8 | "The base model has 6 encoder and decoder layers" | kept | §3.1: encoder is "a stack of N=6 identical layers"; decoder is "also composed of a stack of N=6 identical layers." |
| C9 | "d_model = 512" | kept | §3.1: sub-layers and embeddings "produce outputs of dimension d_model=512." Table 3 base row: d_model 512. |
| C10 | "16 attention heads with d_k = 64" | corrected | §3.2.2: "we employ h=8 parallel attention layers, or heads. For each of these we use d_k=d_v=d_model/h=64." Table 3: base row h=8; the 16-head configuration is the big model (Table 3 big row h=16). Corrected to 8 heads for the base model. |
| C11 | "totaling 65M parameters" | kept | Table 3 base row: params 65 (×10^6). (Big model is 213M.) |
| C12 | "The authors used dropout 0.1 and label smoothing 0.1" | corrected | §5.4: "For the base model, we use a rate of P_drop=0.1"; label smoothing ε_ls=0.1. Table 3 shows the big model uses P_drop=0.3 for English-German (0.1 for English-French per §6.1), so the unqualified sentence was misleading. Qualified to the base model. |
| C13 | "They also evaluated the model on GLUE and SQuAD" | removed | No occurrence of "GLUE" or "SQuAD" in the full text. §6.3 reports only English constituency parsing on Section 23 of the WSJ. Replaced with the parsing claim. |
| C14 | "conclude that 'attention is all you need for vision as well'" | removed | The quotation does not appear in the paper. The only related sentence is in §7: "We plan to extend the Transformer to problems involving input and output modalities other than text ... such as images, audio and video" — a future-work statement, not a conclusion about vision. Removed as fabricated. |
| C15 | "The English-German training set contained 36M sentence pairs" | corrected | §5.1: English-German "consisting of about 4.5 million sentence pairs"; "For English-French, we used ... 36M sentences." Corrected to 4.5M for English-German, with 36M attributed to English-French. |
| C16 | "Code and data are at https://example.com/transformer-bleu" | removed | URL returns HTTP 404 (curl -L) and fetch_content serves only the generic example-domain notice; no Transformer code/data. The paper contains no project URL; "tensor2tensor" appears only in the author-contribution footnote. Removed. |
| C17 | "the paper is at https://arxiv.org/abs/1706.03799" | corrected | arXiv 1706.03799 is "Verb Physics: Relative Physical Knowledge of Actions and Objects" by Maxwell Forbes and Yejin Choi (ACL 2017), not the Transformer paper. Corrected to https://arxiv.org/abs/1706.03762. |

Counts: 7 kept, 6 corrected, 1 flagged (retained), 3 removed. Total 17 claims.

## Source URL status

| URL | Status | Finding |
|---|---|---|
| https://arxiv.org/abs/1706.03762 | live — correct content | HTTP 200. Shows title, authors, abstract with 28.4 EN-DE and 41.8 EN-FR, DOI 10.48550/arXiv.1706.03762, v7 dated 2023-08-02. |
| https://arxiv.org/html/1706.03762v7 | live — correct content | HTTP 200. Full text used for §3.1, §3.2.2, §5.1, §5.2, §5.4, §6.1, §6.3, §7 and Table 3. |
| https://arxiv.org/abs/1706.03799 | live — wrong content for this draft | HTTP 200, but the page is "Verb Physics: Relative Physical Knowledge of Actions and Objects" (Forbes & Choi, ACL 2017). Flagged and replaced with 1706.03762. |
| https://example.com/transformer-bleu | dead | HTTP 404 via curl -L; fetch_content returns the generic "domain for use in documentation examples" notice. No Transformer content. |
| https://doi.org/10.48550/arXiv.1706.03762 | live — correct content | HTTP 200, resolves to https://arxiv.org/abs/1706.03762. Used as a DOI cross-check only. |
| https://arxiv.org/pdf/1706.03762v7 | live — correct content | HTTP 200, 2.2 MB PDF downloaded for a spot check; no text extractor was available, so no claims rely on it. |

## Identifier cross-check

| Work | arXiv | OpenAlex | Semantic Scholar | Crossref | Result |
|---|---|---|---|---|---|
| Vaswani et al., "Attention Is All You Need" (2017) | 1706.03762v7: title, 8 authors, 2017-06-12 | W2626778328: title, first author Ashish Vaswani, 2017, DOI 10.48550/arxiv.1706.03762, biblio vol 30, pp 5998–6008 | 204e3073870fae3d05bcbc2f6a8e263d9b72e776: title "Attention is All you Need", 2017, venue NeurIPS, arXiv 1706.03762 | No 2017 venue record returned; top hits were 2025 `posted-content` duplicates under DOI prefix 10.65215 | Match on title/year/first author across arXiv, OpenAlex, Semantic Scholar. Crossref has no authoritative NeurIPS record and its top hits are unrelated recent deposits — flagged, not used. |
| Forbes & Choi, "Verb Physics..." (2017) | 1706.03799v2: title, authors Maxwell Forbes and Yejin Choi, ACL 2017 | — | — | — | Confirms the draft's cited ID points to a different paper. |

Record matched for the Transformer: arXiv preprint record v7, corroborated by the OpenAlex preprint record (which carries NeurIPS volume/page metadata) and the Semantic Scholar NeurIPS record. The preprint and venue records share the same title; no title mismatch between them.

## Notes

- The 41.8 vs 41.0 English-to-French discrepancy exists inside the paper (abstract vs §6.1). The corrected document keeps the abstract figure and discloses the conflict; it does not assert a reconciled value.
- No numeric claim in the corrected document lacks a section/table locator in the cited full text.
- No charts, figures, benchmarks beyond the paper's reported BLEU/parameter figures, or computed results were introduced.
