# Verification: transformer-wmt14-bleu

Mode: direct search (no researcher/verifier subagents). Lead performed citation and review.

## Checks performed
| Check | Method | Result |
|---|---|---|
| arXiv ID correct | arXiv abs page + arXiv API record | PASS — 1706.03762 |
| Abstract says 28.4 EN-DE | fetched abs page v7, v1, v3 | PASS — all three say 28.4 |
| Table 2 values | fetched v7 HTML and NeurIPS PDF | PASS — base 27.3, big 28.4 |
| §6.1 statement | v7 HTML full text | PASS — "new state-of-the-art BLEU score of 28.4" |
| NeurIPS PDF body | fetched PDF, parsed 11 pages | PASS — 28.4; Table 2 matches |
| Conflicting 27.5 | fetched NeurIPS HTML abstract page | CONFIRMED as metadata-only conflict; paper PDF does not contain it |
| All source URLs reachable | every URL in Sources fetched successfully | PASS |
| No invented numbers | every number traced to fetched source | PASS |
| Reproduction of BLEU | none attempted | NOT RUN — explicitly marked |

## Findings
No FATAL issues.

MAJOR:
- The NeurIPS HTML abstract page conflicts with the paper (27.5 vs 28.4). Handled by explicit caveat in the report; headline answer uses the paper body, abstract, and Table 2, which agree across versions and venues.

MINOR:
- v7 HTML body text says EN-FR 41.0 while its abstract/table say 41.8. Noted in report; does not affect EN-DE.
- "Original paper" is version-ambiguous; report states 28.4 is stable across v1/v3/v7 and NeurIPS PDF.

## Verdict
PASS WITH NOTES. Note: BLEU not independently reproduced; quantitative claims are the paper's own reported values, verified against primary sources.

Verification: PASS WITH NOTES
