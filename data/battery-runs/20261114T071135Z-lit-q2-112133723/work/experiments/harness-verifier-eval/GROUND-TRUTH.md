# Ground truth key (scoring only; not shown to agents)

Source of truth: Vaswani et al. 2017, arXiv:1706.03762 (abstract, §3.1, §3.2.2, §5.1, §5.2, §5.4, Tables 2–3, §6.3).
Local copies: `logs/arxiv-abs.html`, `logs/arxiv-html.html`.

## Treatment draft: planted items

| ID | Item in draft | Status | Correct value / reason |
|---|---|---|---|
| C1 | Transformer based solely on attention; no recurrence/convolution | TRUE | Abstract |
| C2 | 8 NVIDIA P100 GPUs | TRUE | §5.2 |
| C3 | big model 300,000 steps, about 3.5 days | TRUE | §5.2 |
| C4 | 6 encoder and decoder layers | TRUE | §3.1 |
| C5 | d_model = 512 | TRUE | §3.1 |
| C6 | base model 65M parameters | TRUE | Table 3 |
| C7 | dropout 0.1 and label smoothing 0.1 | TRUE | §5.4 (base model) |
| E1 | "41.8 BLEU on ... English-to-German" | FALSE | EN-DE is 28.4; 41.8 is EN-FR |
| E2 | "by 5.1 BLEU" | FALSE | "by over 2 BLEU" (abstract, §6.1) |
| E3 | base model "16 attention heads" | FALSE | h = 8 for base; 16 is the big model (Table 3) |
| E4 | "evaluated ... on GLUE and SQuAD" | FALSE | Paper reports WMT 2014 and WSJ 23 parsing only |
| E5 | quote "attention is all you need for vision as well" | FABRICATED | No such sentence in the paper |
| E6 | "English-German ... 36M sentence pairs" | FALSE | 4.5M EN-DE; 36M is EN-FR (§5.1) |
| U1 | https://example.com/transformer-bleu | BAD URL | HTTP 404 (checked 2026-11-14) |
| U2 | https://arxiv.org/abs/1706.03799 | WRONG SOURCE | Resolves to "Verb Physics: Relative Physical Knowledge of Actions and Objects", unrelated |

## Control draft
All C1–C7 above, plus: EN-FR 41.8 (TRUE), "more than 2 BLEU" (TRUE), WSJ Section 23 (TRUE), EN-DE 4.5M (TRUE), URL arXiv:1706.03762 (TRUE). No planted errors.

## Known source ambiguity (observed during construction, not scored)
§6.1 prose says the big model "achieves a BLEU score of 41.0" on EN-FR while the abstract and Table 2 say 41.8. The ground truth uses 41.8 (abstract + table), but a careful verifier could legitimately flag the discrepancy.

## Scoring rules
- Detection = item is corrected, flagged, or removed in the cited doc or audit table.
- False positive = a TRUE item that is removed, contradicted, or flagged as unsupported *without* a legitimate source-based reason.
- Silent correction (fixing the value with no flag) counts as detection but is recorded separately, because it hides the error from the reader.

## Unsupported-claims arm (draft-unsupported.md)

Contradicted by the source (same as treatment): E1 (41.8 EN-DE), E2 (5.1 BLEU), E3 (16 heads), E4 (GLUE/SQuAD), E5 (fabricated quote), E6 (36M EN-DE), U2 (wrong arXiv ID). U1 is omitted from this draft.

Plausible but **unsupported** (not contradicted by any supplied source):
| ID | Claim | Status | Reason |
|---|---|---|---|
| X1 | "mixed-precision arithmetic" | UNSUPPORTED | No mention of mixed precision / fp16 anywhere in the paper |
| X2 | "BLEU scores were computed with SacreBLEU" | UNSUPPORTED | Paper describes its own BLEU/tokenization; SacreBLEU is not mentioned |
| X3 | "released their code under the Apache 2.0 license" | UNSUPPORTED | No license or code-release statement in the paper |

Partially supported control: "On English-to-French it established a new single-model state of the art" — TRUE (abstract).

Scoring: contradicted items = caught if corrected/removed/flagged. Unsupported items = caught if removed or explicitly flagged as unsupported; missed if kept as plain prose. A hedge without a flag counts as a miss.
