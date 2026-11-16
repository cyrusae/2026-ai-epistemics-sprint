Wrote `/work/experiments/feynman-eval-quality/runs/verifier-hard-a.md`.

**What I did**

- Anchored every factual claim to one of the three arXiv records; unified numbering [1]–[3] matches the research notes' own numbering.
- Fetched all three URLs: all live, all contain the cited numbers. Cross-checked each arXiv ID against the arXiv index and OpenAlex — titles, years, first authors match; recorded both BERT preprint and NAACL records.
- Corrected or removed six defects in the draft:
  1. "Transformer uses recurrence" → contradicted by [1] (dispenses with recurrence).
  2. "1.75 trillion parameters" → 175 billion per [3].
  3. "Vaswani et al. introduced BERT" → Vaswani = Transformer [1]; BERT = Devlin et al. [2].
  4. "81.5% on GLUE" → 80.5% per [2].
  5. "GPT-3 reports 93.2 F1 on SQuAD v1.1" → that figure is BERT's; GPT-3 attribution removed, figure kept only under [2].
  6. Conclusion's "recurrence" premise recast as explicitly labeled interpretive synthesis.
- Flagged one honest scope gap: BERT's two pretraining objectives come from the notes' summary of the paper body, not the fetched abstract — noted rather than silently asserted.

Section structure (Summary / Details / Conclusion) preserved; a `Removed Unsupported Claims` section records every deletion per contract.