# Lab notebook

## 2026-11-13 — Feynman eval-quality case study

Slug: `feynman-harness-eval-quality`

- Pre-registered a 6-probe protocol before running behavioral probes.
- Found the upstream repo has a real deterministic eval harness (`evals/`) that is excluded from the npm package; committed results stop at v0.5.3 while the release is v0.5.65.
- Behavioral probes: verifier caught 5/5 coached and 4/4 uncoached seeded defects with 0 false positives; researcher refused a fabricated paper; reviewer caught an arithmetic inconsistency in an underpowered eval fixture.
- Instrument hazards: Crossref identifier queries are fuzzy `/works?query=` searches with no `not_found`; a 2025 `10.65215/*` zombie DOI matches the Transformer title but 404s; `fetch_content` returns example.com placeholder pages as ordinary success.
- Final artifact: `outputs/feynman-harness-eval-quality-case-study.md`; provenance: `outputs/feynman-harness-eval-quality-case-study.provenance.md`.
- Next: re-run the upstream eval on the current release; add claim-level and negative-control probes; test whether exact Crossref lookup + soft-404 detection reduce verifier errors.
