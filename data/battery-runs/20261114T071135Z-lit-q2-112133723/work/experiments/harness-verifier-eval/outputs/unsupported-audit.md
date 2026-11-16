# Claim-level audit — `inputs/draft-unsupported.md`

Verification date: 2026-11-14. Inputs were read-only; nothing in `inputs/` was modified.
Output document: `outputs/unsupported-cited.md`.

## Summary

| Verdict | Count |
|---|---|
| Kept (supported as written or with only citation/scope added) | 10 |
| Corrected (source supports a different number/fact) | 6 |
| Removed (unsupported or contradicted) | 5 |
| Flagged (record-level caveat, claim retained) | 1 |
| **Total claims audited** | **22** |

The draft's central failure mode is not dead links but **misattributed numbers**: the 41.8 BLEU English-to-French score was attached to English-to-German, the 36M English-French corpus size was attached to English-German, and the 16-head big-model configuration was attached to the base model. Three claims (SacreBLEU, Apache 2.0 code release, GLUE/SQuAD + vision quote) have no basis in the paper at all and were removed.

## Claim-level table

Claim IDs follow draft sentence order (S1–S10).

| ID | Draft claim (verbatim fragment) | Verdict | Evidence in research files / paper | Action in output |
|---|---|---|---|---|
| C1 | "Attention Is All You Need (Vaswani et al., 2017)" | kept | arXiv abs page [1]: title, 8 authors, first author Vaswani, submitted 2017-06-12; OpenAlex W2626778328 matches title/year/first author; notes header names the paper | Cited [1, 2] |
| C2 | "an architecture based solely on attention mechanisms that dispenses with recurrence and convolutions entirely" | kept | Abstract verbatim, notes and [1]/[2]: "based solely on attention mechanisms, dispensing with recurrence and convolutions entirely" | Cited [1, 2] |
| C3 | "The big model reached 41.8 BLEU on the WMT 2014 English-to-German translation task" | **corrected** | Table 2: big model = 28.4 EN-DE, 41.8 EN-FR. Abstract: "28.4 BLEU on the WMT 2014 English-to-German". 41.8 belongs to EN-FR | Changed to "28.4 BLEU ... English-to-German" |
| C4 | "improving over the previous best results, including ensembles, by 5.1 BLEU" | **corrected** | Abstract: "improving over the existing best results, including ensembles by over 2 BLEU"; §6.1: "by more than 2.0 BLEU". "5.1" appears nowhere in the notes or paper | Changed to "by over 2 BLEU" |
| C5 | "On English-to-French it established a new single-model state of the art" | kept | Abstract: "establishes a new single-model state-of-the-art BLEU score of 41.8"; Table 2 EN-FR = 41.8 | Kept, with 41.8 BLEU added |
| C6 | "Training used 8 NVIDIA P100 GPUs" | kept | §5.2: "one machine with 8 NVIDIA P100 GPUs" | Kept |
| C7 | "in mixed-precision arithmetic" | **removed (unsupported)** | Supplied notes do not mention training precision; the fetched §5.2 excerpt does not state it. Notes neither support nor contradict → treated as unsupported, not inferred | Phrase deleted |
| C8 | "the big model ran for 300,000 steps, about 3.5 days" | kept | §5.2: "The big models were trained for 300,000 steps (3.5 days)"; Table 3 big = 300K steps | Kept |
| C9 | "6 encoder and decoder layers" | kept | §3.1: "stack of N=6 identical layers" for both encoder and decoder; Table 3 base N=6 | Kept |
| C10 | "d_model = 512" (base) | kept | §3.1: "produce outputs of dimension d_model = 512"; Table 3 base d_model 512 (big is 1024) | Kept, scoped to base model |
| C11 | "16 attention heads with d_k = 64" (base) | **corrected** | §3.2.2: "h = 8 parallel attention layers ... d_k = d_v = d_model/h = 64"; Table 3 base h=8, big h=16 | Changed to "8 attention heads" |
| C12 | "d_k = 64" | kept | §3.2.2 verbatim; Table 3 base d_k 64 | Kept |
| C13 | "totaling 65M parameters" (base) | kept | Table 3 base params = 65M (big = 213M) | Kept, scoped to base model |
| C14 | "The authors used dropout 0.1" | **corrected (scope)** | §5.4: "For the base model, we use a rate of P_drop = 0.1"; Table 3 big P_drop = 0.3. Unqualified "0.1" is wrong for the big model | Scoped: "For the base model ... dropout 0.1" |
| C15 | "label smoothing 0.1" | kept | §5.4: "label smoothing of value epsilon_ls = 0.1"; Table 3 base epsilon_ls 0.1 | Kept |
| C16 | "BLEU scores were computed with SacreBLEU" | **removed (unsupported)** | No mention in notes; no mention in fetched abstract, §5, §6. Notes neither support nor contradict → unsupported. (SacreBLEU was also not the tool used in 2017; not asserted here, only noted as reason for skepticism) | Deleted |
| C17 | "released their code under the Apache 2.0 license" | **removed (unsupported)** | Notes: official code (tensor2tensor) is referenced in a footnote, "No code URL was verified in these notes." No license statement anywhere in notes or fetched text | Deleted |
| C18 | "They also evaluated the model on GLUE and SQuAD" | **removed (contradicted)** | Notes "Notes on scope": "No GLUE or SQuAD experiments appear in the paper." Fetched §6 covers WMT 2014 and §6.3 WSJ 23 only | Deleted |
| C19 | "conclude that 'attention is all you need for vision as well'" | **removed (fabricated quote)** | No such statement in notes or any fetched section. Conclusion mentions future work on "images, audio and video" but contains no such sentence. Quotation marks make this a fabricated quote | Deleted |
| C20 | "The English-German training set contained 36M sentence pairs" | **corrected** | §5.1: "English-German dataset consisting of about 4.5 million sentence pairs"; "For English-French, we used ... 36M sentences" | Changed to 4.5M EN-DE; 36M attributed to EN-FR |
| C21 | "The paper is at https://arxiv.org/abs/1706.03799" | **corrected (wrong content)** | 1706.03799 resolves to a different 2017 ACL paper on inferring physical knowledge (Forbes et al.), not this paper. Correct ID 1706.03762 | URL replaced |
| C22 | English-to-French score 41.8 | **flagged** | Abstract and Table 2 say 41.8; v7 body §6.1 says "achieves a BLEU score of 41.0". Internal paper inconsistency | 41.8 kept, discrepancy disclosed in output |

## Source URL status

| # | URL | Status | Checks performed | Notes |
|---|---|---|---|---|
| 1 | https://arxiv.org/abs/1706.03762 | **live / correct content** | Fetched 2026-11-14; abstract matches notes verbatim (28.4 EN-DE, >2 BLEU, 41.8 EN-FR, 3.5 days, eight GPUs); DOI 10.48550/arXiv.1706.03762 listed | Canonical landing page; used for C1–C5, C19 |
| 2 | https://arxiv.org/html/1706.03762v7 | **live / correct content** | Fetched full HTML (42,666 chars); confirmed §3.1, §3.2.2, §5.1, §5.2, §5.4, §6.1, §6.2 Table 3, Table 2, §6.3 Table 4 (WSJ 23) | Used for C2, C6, C8–C15, C18, C20, C22 |
| 3 | https://arxiv.org/abs/1706.03799 | **live / WRONG CONTENT** | Fetched; abstract is "Learning physical knowledge..." (Forbes et al.), ACL 2017 — unrelated to the Transformer | Draft link was wrong; replaced with 1706.03762 |
| 4 | https://openalex.org/W2626778328 | **live / correct record** | OpenAlex search: DOI 10.48550/arxiv.1706.03762, title "Attention Is All You Need", 2017-06-12, first author Ashish Vaswani, 8 authors | Used as second index for ID/title/author cross-check |

## Index cross-check (per citation-integrity rule)

| Record | Index | Title match | Year | First author | Verdict |
|---|---|---|---|---|---|
| arXiv:1706.03762v7 | arXiv API (`arxiv_get_papers`) | "Attention Is All You Need" ✓ | 2017 ✓ | Ashish Vaswani ✓ | match |
| DOI 10.48550/arXiv.1706.03762 | OpenAlex (W2626778328) | "Attention Is All You Need" ✓ | 2017 ✓ | Ashish Vaswani ✓ | match (preprint record) |
| Crossref | Crossref REST | No authoritative record found. A title query returned only non-authoritative `posted-content` mirrors under DOI prefix 10.65215 (2025 deposit dates, e.g. 10.65215/r5bs2d54) | n/a | n/a | flagged: no usable Crossref record; venue version is NeurIPS 2017 proceedings, which is not DOIs-registered in Crossref under this title |

Caveat recorded rather than resolved: the paper has preprint and venue (NeurIPS 30, pp. 5998–6008) records; all bibliographic checks above match the **preprint** record. No Crossref venue DOI was found, so the venue record could not be independently confirmed in this pass.

## Unsupported-but-not-contradicted items

These statements were treated as **unsupported** (notes are silent) and were removed rather than inferred:

- C7 mixed-precision training arithmetic.
- C16 SacreBLEU as the BLEU implementation.
- C17 Apache 2.0 license and a public code release at a project URL.

## Remaining risks

- The 41.8 vs 41.0 English-to-French inconsistency exists inside the paper itself (§6.1 body vs abstract/Table 2); a reader following only §6.1 would see 41.0. Disclosed in the output document.
- arXiv v7 HTML is a 2023 conversion of a 2017 paper; section text and tables were treated as authoritative only where they agree with the abstract or are corroborated by the research notes.
- No raw artifact, script, figure, or dataset file was involved; the only quantitative claims retained are numbers printed in the paper, so no code-backed provenance gap applies.
