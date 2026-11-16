# Lab notebook

## 2026-11-14 — feynman-harness-eval-quality

- Extracted Feynman 0.5.65 eval-relevant mechanisms from `SYSTEM.md`,
  `.feynman/agents/*.md`, `prompts/*.md`, `extensions/research-tools/*.ts`,
  `RELEASES.md`, and `package.json`.
- Built an 8-dimension rubric from construct-validity, agentic-benchmark-rigor,
  variance, reproducibility, judge-validity, cost, and citation-integrity work.
- Built and ran a seeded-defect probe against the bundled `verifier` agent.
  Probe 1 (answers pre-extracted): 10/10 defects, 5/5 controls. Probe 2
  (answers withheld): 6/6 defects, 4/4 controls, 0 false removals.
  **Confound found:** Probe 1's research file contained the correct numbers, so
  it tested reconciliation, not independent verification. Probe 2 was added to
  fix this.
- Spot-checked the verifier's claims: 8/8 arXiv URLs HTTP 200; OpenAlex
  W7197047848 and W4416268504 match its descriptions.
- Retrieval probe: S2-only 5/10 returned records relevant, 2/4 queries
  productive; OpenAlex fallback rescued one rate-limited query at 5/5.
- **Verification:** PASS WITH NOTES. Reviewer agent and multi-run reliability
  not tested.
- **Next step:** run `/deepresearch` end-to-end on a frozen topic and audit its
  own artifact chain against the same rubric.
