# Plan: Transformer WMT 2014 EN-DE BLEU and arXiv ID

## Key questions
1. What WMT 2014 English-to-German BLEU score did Vaswani et al. (2017) report in "Attention Is All You Need"?
2. What is the paper's arXiv ID?
3. Are there multiple variants (base vs big) and what exactly does the abstract/table say?

## Evidence needed
- arXiv metadata for the paper (canonical ID, title, year).
- The paper's abstract and Table 2 (or equivalent) reporting WMT 2014 EN-DE BLEU, including base and big model variants.
- Any official ancillary source (NeurIPS proceedings) to cross-check the number.

## Scale decision
Narrow "what is X" factual question. Direct lead-owned search only; no researcher subagents. Target 3-10 tool calls.

## Task ledger
| ID | Task | Owner | Status |
|----|------|-------|--------|
| T1 | Locate arXiv metadata / ID | lead | done |
| T2 | Extract abstract BLEU claim | lead | done |
| T3 | Extract Table 2 base/big BLEU values | lead | done |
| T4 | Cross-check with NeurIPS proceedings or secondary reliable source | lead | done |

## Verification log
- arXiv abs v7, v1, v3 + arXiv API: 28.4 EN-DE confirmed.
- arXiv v7 HTML + NeurIPS PDF: Table 2 base 27.3 / big 28.4 confirmed.
- NeurIPS HTML abstract shows 27.5 — metadata conflict only; PDF resolves to 28.4.
- Direct-mode self-review: PASS WITH NOTES (no BLEU reproduction).

## Decision log
- Chose direct search: single-fact explainer, no decomposition benefit.
