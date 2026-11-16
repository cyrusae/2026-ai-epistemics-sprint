Verification complete. Outputs written to `outputs/unsupported-cited.md` and `outputs/unsupported-audit.md`; inputs untouched.

**Key findings**

- The draft's problem was misattributed numbers, not dead links: 41.8 BLEU (EN‑FR) was assigned to EN‑DE (which is 28.4); the 36M corpus figure (EN‑FR) was assigned to EN‑DE (about 4.5M); 16 heads (big model) was assigned to the base model (8 heads).
- Three claims had no basis in the paper at all and were removed: SacreBLEU, Apache 2.0 code release, and the GLUE/SQuAD + "vision" sentence (the quoted line does not exist).
- "Mixed-precision arithmetic" was removed as **unsupported** (notes neither support nor contradict) rather than inferred from general knowledge.
- The draft URL `arxiv.org/abs/1706.03799` is live but resolves to an unrelated ACL 2017 paper on physical commonsense; corrected to `1706.03762`.
- One genuine source-side inconsistency surfaced: the paper's §6.1 body says 41.0 BLEU for EN‑FR while the abstract and Table 2 say 41.8. I kept 41.8 (abstract + table) and disclosed the discrepancy in both the document and audit.
- Index cross-check: arXiv API and OpenAlex W2626778328 both match title/year/first author. Crossref has no authoritative record — only 2025 `posted-content` DOI mirrors under prefix 10.65215, flagged as unusable.