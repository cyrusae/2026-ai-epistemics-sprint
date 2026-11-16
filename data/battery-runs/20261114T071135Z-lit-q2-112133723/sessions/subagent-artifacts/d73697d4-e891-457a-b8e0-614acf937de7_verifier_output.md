Done. Both artifacts written; inputs untouched.

## What changed

The draft contained five distinct factual corruptions, all traceable to base/big-model or EN-DE/EN-FR conflation, plus two dead/wrong links and one fabricated quote:

| Item | Draft | Corrected |
|---|---|---|
| EN-DE BLEU | 41.8 | 28.4 (41.8 is EN-FR) |
| Improvement margin | 5.1 BLEU | more than 2.0 BLEU |
| Base-model heads | 16 | 8 (16 is the big model) |
| EN-DE training data | 36M pairs | ≈4.5M (36M is EN-FR) |
| Paper link | arXiv:1706.03799 | arXiv:1706.03762 |
| GLUE/SQuAD evaluation | claimed | removed — no such experiments; replaced with WSJ §23 parsing |
| "vision as well" quote | quoted | removed — no such sentence; "vision" appears only in reference 36 |
| `example.com/transformer-bleu` | cited | removed — HTTP 404, placeholder domain |

Seven true claims (attention-only architecture, 8×P100, 300K steps/3.5 days, 6 layers, d_model 512, 65M params, dropout 0.1 + label smoothing 0.1) were kept with citations. Corrections are disclosed in a `Corrections Applied` section rather than silently applied, and the paper's internal 41.0-vs-41.8 EN-FR inconsistency is noted rather than hidden. Sources = 2 live URLs, both cited, no orphans.

Verification used the local full-text mirror plus live pages; both kept URLs returned HTTP 200 with matching content, and 1706.03799 returned 200 with unrelated content ("Verb Physics", Forbes & Choi). OpenAlex and the arXiv API agree on title/year/first author for 1706.03762; Crossref surfaced only 2025 `posted-content` lookalikes, which is recorded in the audit rather than treated as a match.