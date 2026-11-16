# Claim-level audit — `draft-treatment.md`

Verified against:
- `inputs/research-notes.md` (excerpts supplied with the draft)
- arXiv:1706.03762v7 full text, live at https://arxiv.org/html/1706.03762v7 and local mirror `logs/arxiv-html.html`
- arXiv abstract page, live at https://arxiv.org/abs/1706.03762 and local mirror `logs/arxiv-abs.html`
- Live HTTP checks run 2026-11-14 (`curl -L -o /dev/null -w '%{http_code}'`)
- Indexes: arXiv API (`arxiv_get_papers`), OpenAlex (`W2626778328`), Crossref

Verdicts: **kept** = claim matches the source; **corrected** = claim wrong, value replaced and change disclosed in the output; **flagged** = claim retained but carries a documented caveat; **removed** = unsupported/fabricated, deleted.

## Claim table

| # | Claim as written in draft | Verdict | Correct value / disposition | Evidence (quote → location) |
|---|---|---|---|---|
| 1 | "Attention Is All You Need (Vaswani et al., 2017)" | kept | Attribution and year correct | arXiv metadata: title "Attention Is All You Need", first author Ashish Vaswani, published 2017-06-12 |
| 2 | "architecture based solely on attention mechanisms that dispenses with recurrence and convolutions entirely" | kept | — | Abstract: "a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely" [abs + §1] |
| 3 | "The big model reached 41.8 BLEU on the WMT 2014 English-to-German translation task" | corrected | EN-DE big model = **28.4**; 41.8 is EN-FR | Table 2: "Transformer (big) 28.4 41.8"; §6.1: "establishing a new state-of-the-art BLEU score of 28.4" on EN-DE; abstract: "28.4 BLEU on the WMT 2014 English-to-German" |
| 4 | "improving over the previous best results, including ensembles, by 5.1 BLEU" | corrected | "more than 2.0 BLEU" | §6.1: "outperforms the best previously reported models (including ensembles) by more than 2.0 BLEU"; abstract: "by over 2 BLEU". No "5.1" figure appears anywhere in the paper. |
| 5 | "On English-to-French it established a new single-model state of the art" | kept (expanded) | Correct; explicit 41.8 added | Abstract: "establishes a new single-model state-of-the-art BLEU score of 41.8"; Table 2 EN-FR 41.8 |
| 6 | "Training used 8 NVIDIA P100 GPUs" | kept | — | §5.2: "We trained our models on one machine with 8 NVIDIA P100 GPUs" |
| 7 | "the big model ran for 300,000 steps, about 3.5 days" | kept | — | §5.2: "The big models were trained for 300,000 steps (3.5 days)" |
| 8 | "base model has 6 encoder and decoder layers" | kept | — | §3.1: encoder "a stack of N = 6 identical layers"; decoder "also composed of a stack of N = 6 identical layers"; Table 3 base layers = 6 |
| 9 | "d_model = 512" | kept | — | §3.1: "all sub-layers in the model ... produce outputs of dimension d_model = 512"; Table 3 base 512 |
| 10 | "16 attention heads with d_k = 64" | corrected | Base model h = **8**; d_k = 64 correct. 16 heads is the big model. | §3.2.2: "we employ h = 8 parallel attention layers, or heads. For each of these we use d_k = d_v = d_model/h = 64"; Table 3: base h 8, big h 16 |
| 11 | "totaling 65M parameters" | kept | Correct for the base model | Table 3: base params "65"; big 213 (×10^6) |
| 12 | "dropout 0.1" | kept (qualified) | Base model P_drop = 0.1; big model is 0.3 | §5.4: "For the base model, we use a rate of P_drop = 0.1"; Table 3: base 0.1, big 0.3 |
| 13 | "label smoothing 0.1" | kept | — | §5.4: "we employed label smoothing of value ε_ls = 0.1"; Table 3 ε_ls 0.1 |
| 14 | "They also evaluated the model on GLUE and SQuAD" | removed | No GLUE or SQuAD experiments exist in the paper; replaced with WSJ §23 parsing | Zero occurrences of "GLUE" and "SQuAD" in `logs/arxiv-html.html`; §6.3: "we performed experiments on English constituency parsing"; Table 4: "Results are on Section 23 of WSJ"; abstract: "English constituency parsing ... with large and limited training data" |
| 15 | Quotation: "attention is all you need for vision as well" | removed | Fabricated quotation; no vision claim in the paper | No such sentence in `logs/arxiv-html.html`. Only occurrence of "vision" is reference [36], "Rethinking the inception architecture for computer vision" (Szegedy et al.) — an unrelated cited work. |
| 16 | "The English-German training set contained 36M sentence pairs" | corrected | EN-DE ≈ **4.5 million**; 36M is EN-FR | §5.1: "standard WMT 2014 English-German dataset consisting of about 4.5 million sentence pairs"; "For English-French, we used ... 36M sentences" |
| 17 | Code/data at `https://example.com/transformer-bleu` | removed | HTTP 404; example-domain placeholder | `curl` → 404. Body: "This domain is for use in documentation examples...". Research notes: "No code URL was verified in these notes"; the paper references tensor2tensor in a footnote only. |
| 18 | "the paper is at https://arxiv.org/abs/1706.03799" | corrected | Correct ID is arXiv:**1706.03762** | arXiv API: 1706.03799 = "Verb Physics: Relative Physical Knowledge of Actions and Objects" (Forbes & Choi), 2017 — unrelated. 1706.03762 = "Attention Is All You Need". |

## Source URL status

| URL | Where it appears | HTTP | Status | Action |
|---|---|---|---|---|
| https://arxiv.org/abs/1706.03762 | research notes; used in final Sources [1] | 200 | **live, correct content** — title, ID 1706.03762, Vaswani first author, abstract with 28.4/41.8 | kept as [1] |
| https://arxiv.org/html/1706.03762v7 | research notes; used in final Sources [2] | 200 | **live, correct content** — full text v7 with §3.1, §3.2.2, §5.1, §5.2, §5.4, §6.1, §6.3, Tables 2–3 | kept as [2] |
| https://example.com/transformer-bleu | draft body (code/data link) | 404 | **dead** — example-domain placeholder; no archive or replacement found | removed from draft; not carried into Sources |
| https://arxiv.org/abs/1706.03799 | draft body (paper link) | 200 | **live but wrong content** — "Verb Physics: Relative Physical Knowledge of Actions and Objects" (Forbes & Choi, 2017), unrelated to the Transformer | replaced with 1706.03762; not carried into Sources |

No redirects to unrelated content were observed on the two kept URLs. No alternative/mirror was needed for the dead link because the underlying claim (a project code URL) has no support in the research notes.

## Index cross-check (cited paper)

| Record | Found | Title | Year | First author | Match |
|---|---|---|---|---|---|
| arXiv API, 1706.03762v7 | yes | Attention Is All You Need | 2017 | Ashish Vaswani | matches citation |
| OpenAlex W2626778328 (DOI 10.48550/arxiv.1706.03762) | yes | Attention Is All You Need | 2017 | Ashish Vaswani | matches citation (preprint record; NeurIPS 2017, v30, pp. 5998–6008) |
| arXiv API, 1706.03799v2 | yes | Verb Physics: Relative Physical Knowledge of Actions and Objects | 2017 | Maxwell Forbes | **does not match** the draft's use of it as the Transformer paper |
| Crossref, query "Attention Is All You Need Vaswani 2017" | partial | Returns only 2025 `posted-content` records with the same title/author list (e.g. 10.65215/r5bs2d54) | 2025 | Ashish Vaswani | no canonical venue DOI surfaced in this index; reliance is on the arXiv record above, which two indexes agree on |

## Meaning-level checks

- Verified that 41.8 belongs to EN-FR, not EN-DE, by reading Table 2 rows directly rather than relying on the abstract alone.
- Verified that "more than 2.0 BLEU" is the §6.1 phrasing and "over 2 BLEU" the abstract phrasing; both support the corrected sentence.
- Verified that h = 8 and h = 16 are base vs. big in Table 3, so the head-count error is a base/big mix-up, not a typo in the source.
- Verified absence of GLUE/SQuAD by searching the full extracted text (0 hits each), and absence of the "vision" quotation (only reference [36] uses the word).
- Verified that the code URL claim has no support: notes state the paper references tensor2tensor in a footnote, no project URL.

## Discrepancy noted in the source (not an error in the draft)

§6.1 prose states the big model "achieves a BLEU score of 41.0" on EN-FR, while the abstract and Table 2 state 41.8. The final document uses 41.8 (abstract + Table 2 are the primary reported figures) and discloses the inconsistency inline, so the number is not presented as unqualified.

## Residual risks

- The paper's EN-FR figures are internally inconsistent (41.0 vs 41.8); a reader comparing against §6.1 will see a different number, which is why the note is included.
- Base-model-only qualifiers (dropout 0.1, 8 heads, 65M params) are stated as base-model facts in the text; the big model differs (0.3 dropout, 16 heads, 213M params). This is accurate but easy to misread if the paragraph is skimmed.
- No verified public code URL exists in the supplied research; if a code link is required, it needs a fresh primary-source check rather than a placeholder.
