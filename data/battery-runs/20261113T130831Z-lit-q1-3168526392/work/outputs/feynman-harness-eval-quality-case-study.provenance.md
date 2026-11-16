# Provenance: Dogfooding Feynman — eval-quality case study

- **Date:** 2026-11-13
- **Harness:** Feynman 0.5.65 (released 2026-11-06)
- **Model:** `openrouter/deepseek/deepseek-v4.1-flash-1017`, thinking high
- **Artifact:** `outputs/feynman-harness-eval-quality-case-study.md`
- **Protocol:** `experiments/feynman-eval-case-study/protocol.md`
- **Plan:** `outputs/.plans/feynman-harness-eval-quality.md`
- **Raw observations:** `experiments/feynman-eval-case-study/probe-outputs.md`

## Source accounting

### Consulted and accepted

- Installed v0.5.65 prompts: `SYSTEM.md`, `deepresearch.md`, `lit.md`, `review.md`, `audit.md`, `replicate.md`, `autoresearch.md`.
- Installed v0.5.65 agents: `researcher.md`, `verifier.md`, `reviewer.md`, `writer.md`.
- Installed v0.5.65 code: `extensions/research-tools/science-databases.ts`, `extensions/research-tools/telemetry.ts`, `dist/telemetry/posthog.js`, `metadata/commands.mjs`, `package.json`.
- Public repo `evals/`: `README.md`, `run.mjs`, `questions.jsonl`, six committed result files (2026-09-23/24).
- Primary metadata: arXiv API records for 1706.03762, 2005.14165, 1810.04805; NeurIPS 2017 proceedings page; OpenAlex W2626778328; Crossref record 10.65215/r5bs2d54; IANA example-domain page.
- Behavioral probes: two verifier runs, one researcher run, one reviewer run; all outputs saved under `experiments/feynman-eval-case-study/`.

### Consulted and rejected

- `10.65215/r5bs2d54` (and sibling `10.65215/*` records): title-matched but 2025 `posted-content`, unrelated publisher, DOI landing page 404. Not used as the canonical Transformer record.
- `https://example.com/2024-ml-evaluation-survey`: IANA placeholder, not a survey. Claim removed by the verifier.
- "Chen, Liu & Park (2023), Sparse Mixture Routing..." and `arXiv:2309.99999`: no record; fabricated fixture. Removed.
- "Sparse Tensor Routing for Low-Power Federated Learning" (Zhang/Okafor/Lindqvist 2022): fabricated entity; researcher confirmed non-existence.
- Claim "GPT-3 95.2% zero-shot TriviaQA": contradicted by the GPT-3 paper (64.3% zero-shot, 68.0% one-shot, 71.2% few-shot).
- Claim "Transformer reduces training cost by 10x": not stated in the paper; removed/softened.

## Verification status

**Verification: PASS WITH NOTES.**

Checked directly in this session:

- Tool outputs for arXiv, OpenAlex, Crossref, Semantic Scholar, `fetch_content`, and DOI resolution.
- Verifier defect detection on a 5-defect coached fixture and a 4-defect uncoached fixture; both output documents and logs read back from disk.
- Researcher negative-result output read back from disk.
- Reviewer output read back from disk; arithmetic check reproduced independently (mean of 3 runs on 100 examples must be a multiple of 1/300).
- NeurIPS-vs-arXiv BLEU discrepancy (27.5/41.1 vs 28.4/41.8) confirmed from the NeurIPS page.
- Upstream eval code and committed result tables read from the public repo; key rows cross-checked against the copied JSONL/result files.
- Final artifact exists on disk and hash recorded below.

Not checked / not run:

- The upstream `evals/run.mjs` harness was not executed in this session (requires a repo build and provider quota). Its code and committed results were audited; a fresh run is a `not run` item.
- Telemetry was not captured live at the network level. The prompt/model-output exclusion is supported by static inspection of the `$ai_generation` property list, not by a packet capture.
- The case study is N=1 session, one model. No repeated trials or inter-model comparison.
- Crossref pollution was observed at one point in time (2026-11-13); upstream records may change.

## Hashes (SHA-256)

- Final artifact: `c62a42f20f175c1af25ab839a27c73ae17d3144c14db74a8609ee2cfbfba21c6`
- Raw observations: `12417bbf22d86b90bb2b4f885a7087cd2e23a40381c35998b4fdab397559ca7b`
- Hard verifier log: `f04a46d75de95b6e0baaf9a087a888be8a3ee6536c135090f286f0e2a5ad7017`
- Reviewer output: `851904c683367c1533fe951b17f948be6403050ce4c2a633dbc343f3b06102ae`

## Notes

- This run is a case study, not a `/deepresearch` or `/lit` workflow. The provenance format follows the repo convention but the artifact contract is the case-study protocol.
- The session trace is at `/state/.feynman/sessions/2026-11-13T13-08-35-301Z_01a1d506-3164-77c2-a925-c045394b666d.jsonl`. It is outside the workspace and not included in the delivered artifact.
