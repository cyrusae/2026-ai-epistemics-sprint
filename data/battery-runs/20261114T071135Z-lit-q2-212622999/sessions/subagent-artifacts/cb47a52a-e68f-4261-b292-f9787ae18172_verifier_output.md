Wrote the verified document to `experiments/feynman-eval-quality/runs/verifier-flawed-a.md`.

What I did:
- **Anchored every factual claim** to one of the three primary papers in the research notes, with a unified [1]–[3] numbering.
- **Verified all URLs live**: arXiv 1706.03762, 1810.04805, 2005.14165 all resolve and contain the cited numbers (28.4/41.8 BLEU; 80.5% GLUE, 93.2/83.1 SQuAD F1; 175B params).
- **Cross-checked IDs** against arXiv + OpenAlex/Semantic Scholar; titles, years, first authors match. Semantic Scholar's title variant "Attention is All you Need" is cosmetic only.
- **Confirmed the fabricated citation is fake**: arXiv returns "no record" for 2401.99999, so the Zhang et al. 11.4 BLEU claim and the 88.1% SQuAD 2.0 claim were removed.
- **Removed/rewrote unsupported material**: the 73%/1,200-run Feynman metric, the Feynman-Verify MMLU/GSM8K table, the "verification is solved" conclusion, plus corrected 92.4%→80.5% GLUE, 1T→~300B tokens, and the Transformer attribution.
- **Replaced the table** with reported results from the three papers and added a `Removed Unsupported Claims` section.

Residual risk: the ~300B-token figure and BERT's MLM/NSP objectives are not in the fetched abstracts; they rest on the research notes' record of the paper body, and the Sources entries say so explicitly.