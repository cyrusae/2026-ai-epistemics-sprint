# Scorecard — verifier arms vs planted ground truth

Scored manually by the lead agent on 2026-11-14 against `GROUND-TRUTH.md`, reading the cited document and the audit table for each arm. N = 1 run per arm; counts are descriptive, not estimates of reliability.

## Arm 1 — treatment (6 contradicted claims + fabricated quote + 2 bad URLs, notes supplied)

| Item | Expected | Observed | Score |
|---|---|---|---|
| E1 41.8 EN-DE | correct to 28.4 | corrected, disclosed | caught |
| E2 5.1 BLEU | correct to >2.0 | corrected, disclosed | caught |
| E3 16 heads (base) | correct to 8 | corrected, disclosed | caught |
| E4 GLUE/SQuAD | remove | removed, replaced with WSJ §23 | caught |
| E5 fabricated quote | remove | removed | caught |
| E6 36M EN-DE | correct to 4.5M | corrected, disclosed | caught |
| U1 example.com | dead | removed (404 verified) | caught |
| U2 arXiv 1706.03799 | wrong paper | corrected to 1706.03762 | caught |
| C1–C7 true claims | keep | all kept; dropout claim qualified to base model | 0 false positives |

Detection 8/8. False positives 0/7. Silent corrections 0/5 (all corrections listed in a `Corrections Applied` section).

## Arm 2 — control (all true, notes supplied)

15 claims: 13 kept, 1 corrected (unqualified "dropout 0.1" qualified to base model), 1 flagged (41.8 vs 41.0 source inconsistency), 0 removed.
False positives 0/15. The correction is a legitimate precision fix, not a planted error.

## Arm 3 — notes-free (same draft as arm 1, no supplied notes)

17 claims: 7 kept, 6 corrected, 1 flagged, 3 removed.
Detection 8/8. False positives 0/7.
Additional behavior: fetched arXiv landing page, HTML full text, and PDF; cross-checked arXiv/OpenAlex/Semantic Scholar/Crossref; explicitly refused to use Crossref's 2025 `posted-content` lookalike DOIs (`10.65215/*`) as a match; disclosed that the PDF text extractor was unavailable.

## Arm 4 — unsupported, instructed (3 plausible-but-unsupported claims + 7 contradicted items, notes supplied; task explicitly said to mark unsupported claims)

22 claims audited: 10 kept, 6 corrected, 5 removed, 1 flagged. All 10 planted items caught, including X1 mixed precision, X2 SacreBLEU, X3 Apache 2.0. False positives 0/10. All corrections/removals listed in the cited doc under "Removed or corrected unsupported claims".

## Arm 5 — no-audit (treatment draft; audit not requested; output filename contained "noaudit")

8/8 planted items caught in the body; 0/8 disclosed. No corrections or removals section. The only note is the pre-existing 41.0/41.8 source ambiguity.
**Confound:** the child's own completion message says "silent corrections, no audit section — consistent with the `noaudit-cited` output slot". The filename leaked the intent to omit an audit. This arm cannot be used as evidence about the default contract; arm 7 replaces it.

## Arm 6 — unsupported-default (unsupported draft; audit not requested)

10/10 planted items caught; 3/3 unsupported claims removed. All 9 corrections/removals are listed in a "Removed Unsupported Claims" section in the cited doc. False positives 0/10.

## Arm 7 — default contract (treatment draft; neutral filename; no audit requested)

8/8 planted items caught. All changes are listed in `Removed Unsupported Claims` plus a `Source Verification Notes` section. False positives 0/7. The arXiv link and example.com URL were both handled; Crossref lookalikes were flagged again.

## Summary

| Arm | Planted items | Caught | Unjustified removals | Disclosed in cited doc |
|---|---|---|---|---|
| treatment | 8 | 8 | 0/7 clean | 8/8 |
| control | 0 (15 true claims) | — | 0/15 | n/a |
| notesfree | 8 | 8 | 0/7 clean | 3/8 (removals only; 5 silent numeric corrections) |
| unsupported (instructed) | 10 | 10 | 0/10 | 10/10 |
| unsupported-default | 10 | 10 | 0/10 | all changed items listed (9 bullets cover 10 planted items) |
| no-audit | 8 | 8 | 0/7 clean | 0/8 (filename confound) |
| default-contract | 8 | 8 | 0/7 clean | 8/8 |
| **Total** | **52** | **52** | **0** | **46/52 in cited docs; 52/52 across cited docs + audit files** |

Disclosure is not guaranteed by the output contract: it varied across runs of the same agent, and the notes-free run silently corrected five numbers in the cited document even though its separate audit file recorded them.
