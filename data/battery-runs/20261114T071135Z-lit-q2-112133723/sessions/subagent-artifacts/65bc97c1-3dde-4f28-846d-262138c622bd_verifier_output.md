Verification complete. Both output files were written; input files were not modified.

**Key findings**
- 15 factual claims audited: 13 kept, 1 corrected, 1 flagged, 0 removed.
- Corrected: the draft's unqualified "dropout 0.1" applies only to the base model per §5.4; big models used 0.3 (except the EN-FR big model, which used 0.1).
- Flagged: the paper reports 41.8 BLEU (big, EN-FR) in its abstract and Table 2, but §6.1's body text says 41.0. The document retains 41.8 and discloses the inconsistency in a source note.
- All three source URLs are live and contain the claimed content; arXiv and Semantic Scholar metadata match title, year, and first author.

**Files**
- `experiments/harness-verifier-eval/outputs/control-cited.md`
- `experiments/harness-verifier-eval/outputs/control-audit.md`

**Residual risks**
- The 41.0/41.8 discrepancy is internal to the paper and cannot be resolved without the authors; the chosen 41.8 is backed by two independent locations in the source.
- Crossref has no record for this title/venue, so confirmation rests on arXiv + Semantic Scholar only.
- Table 2 values were read from the PDF; the HTML table body did not render as text.