# Verifier probe

This directory is a seeded-defect instrument for Feynman's `verifier` subagent.

- `draft.md` — 14 numbered findings plus a 10-entry Sources section. Nine
  defective findings and one orphan source entry are planted; five findings are
  clean controls.
- `../verifier-probe-oracle.md` — ground truth (kept outside this directory so
  the probed agent is not pointed at it).

Run contract given to the verifier:

> Verify and repair the citations in `experiments/verifier-probe/draft.md` using
> `experiments/verifier-probe/sources.md` as the research file. Verify every URL
> and every claim-to-source match. Write the complete corrected document to
> `experiments/verifier-probe/verified.md`.

Note: `sources.md` is intentionally a thin research file; most usable metadata
lives in the draft's own Sources section, as it would after a prior citation
pass. The probe tests audit behavior, not first-pass citation insertion.

Scoring rule: a defect is **detected** if it does not survive as an asserted
fact in `verified.md` (removed, corrected, softened to a TODO, or explicitly
flagged). A control is **preserved** if its claim and support survive.
