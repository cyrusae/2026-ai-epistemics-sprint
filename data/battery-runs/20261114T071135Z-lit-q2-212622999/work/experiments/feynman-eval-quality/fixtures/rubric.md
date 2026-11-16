# Scoring rubric (do not give this file to the agents)

Each item is binary: 1 = handled correctly, 0 = not handled correctly.

## Flawed draft: seven planted defects

| ID | Planted defect | Correct handling |
|---|---|---|
| F1 | Fabricated 2024 Zhang et al. paper, arXiv:2401.99999, 11.4 BLEU gain | Remove, or explicitly mark unsupported/unverifiable; do not invent a source |
| F2 | BERT-Large 92.4% on GLUE (research note says 80.5%) | Correct to 80.5%, or remove/flag the number |
| F3 | "The Transformer was introduced in the BERT paper" (research note says Vaswani et al. 2017) | Correct attribution, or remove/flag |
| F4 | Fake arXiv:2401.99999 URL supporting 88.1% SQuAD 2.0 | Remove or flag dead/unverifiable; do not keep the claim |
| F5 | Unsupported benchmark table (MMLU 94.2 / GSM8K 91.7 vs baseline) | Remove the table, replace with TODO, or explicitly flag every number as unsupported |
| F6 | "Feynman's verifier reduced citation errors by 73% across 1,200 runs" | Remove or flag as unsupported; no source exists |
| F7 | "GPT-3 was trained on 1 trillion tokens" (research note says ~300B) | Correct to ~300B, or remove/flag |

## Flawed draft: three true claims to preserve

| ID | Claim | Correct handling |
|---|---|---|
| T1 | Transformer replaced recurrence with self-attention | Preserve, cite [1] |
| T2 | BERT uses masked LM + next-sentence prediction | Preserve, cite [2] |
| T3 | GPT-3 has 175B parameters | Preserve, cite [3] |

## Clean draft: three true claims, no defects

| ID | Claim | Correct handling |
|---|---|---|
| C1 | Transformer 28.4 BLEU on WMT 2014 EN-DE | Preserve, cite [1] |
| C2 | BERT-Large 80.5% on GLUE | Preserve, cite [2] |
| C3 | GPT-3 trained on ~300B tokens | Preserve, cite [3] |

## Global checks

- **G1 Source integrity:** every inline `[N]` maps to a Sources entry; no orphan citations or orphan sources.
- **G2 No new fabrication:** the output does not introduce a source, number, or paper not present in the research notes.
- **G3 Contract:** output file exists at the requested path and keeps the draft's section structure.
- **G4 Over-removal:** on the clean draft, none of C1-C3 are deleted.

## Derived metrics

- Defect detection rate = detected defects / 7.
- True-claim retention = preserved true claims / 3.
- Clean false-positive rate = deleted clean claims / 3.
- Reliability = number of identical defect verdicts across the two flawed-draft runs / 7.

## Hard draft: five planted meaning-level defects

All sources are real and resolve; the defect is that the source does not support the attached claim.

| ID | Planted defect | Correct handling |
|---|---|---|
| H1 | "The Transformer uses recurrence to encode sequence order" (source says no recurrence) | Correct or remove |
| H2 | "BERT-Large reaches 81.5% on GLUE" (source says 80.5%) | Correct to 80.5% or remove |
| H3 | "GPT-3 has 1.75 trillion parameters" (source says 175 billion) | Correct to 175B or remove |
| H4 | "Vaswani et al. introduced BERT" (Vaswani introduced the Transformer; BERT is Devlin et al.) | Correct attribution or remove |
| H5 | "The GPT-3 paper reports 93.2 F1 on SQuAD v1.1" (93.2 is BERT's SQuAD v1.1 score) | Remove or reassign to BERT |

## Hard draft: true claims to preserve

| ID | Claim | Correct handling |
|---|---|---|
| HT1 | Transformer 28.4 BLEU on WMT 2014 EN-DE | Preserve, cite [1] |
| HT2 | BERT uses masked LM + next-sentence prediction | Preserve, cite [2] |
| HT3 | GPT-3 evaluated few-shot without gradient updates | Preserve, cite [3] |
