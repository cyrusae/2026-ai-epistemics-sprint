# Lab notebook

## 2026-11-13 — Feynman eval-quality case study

- Inspected installed Feynman 0.5.65 (system prompt, 4 agent prompts, 11 workflow prompts, telemetry extension, session schema, CLI flags) and the public repo's 62 test files.
- Built `experiments/transcript_audit.py`; audited a live-session snapshot: 88 records, 53 tool calls, 0 dangling parents, 0 missing usage/cost/duration/stop_reason, 3 tool errors (all local bash), $0.0640. Status: verified.
- Ran verifier red-team on a 6-defect + 2-control fixture. First run was contaminated: verifier read `ground-truth.md` from its cwd; verification log omitted the read. Re-ran twice in isolated fixtures: 6/6 defects, 2/2 controls, citations consistent both times. Status: verified; leaked run invalid as capability evidence.
- Found run-2 false negative claim: "92.0% figure is not in the report" while 92.0% is GPT-4 GSM-8K in Table 2. Confirmed by direct HTML grep. Status: verified.
- Reviewer probe on run-2 output: caught the false claim as FATAL and flagged BERT/MLM priority overclaim as MAJOR; read only the two supplied files; 18 calls, $0.0427. Status: verified (n=1).
- Next: synthesize `outputs/feynman-eval-case-study.md`; no end-to-end /lit or /deepresearch run (cost/time), so workflow-level provenance behavior remains unverified.

## 2026-11-13 — Eval-suite discovery and correction

- Found the public `evals/` directory after initially missing it: 12 fixed questions (6 search-bench, 3 LitQA2, 3 hand-authored), deterministic runner (`evals/run.mjs`, 302 lines), committed 0.5.3 results. Corrected the case study's "no eval suite" claim.
- Key boundary: `valid`/`title`/`recall` are identifier-level; they do not check whether a source supports the sentence or number. D3 (92.0% MMLU), D5 (unsourced 43%), D6 (dead URL) would pass or be invisible.
- Committed baselines: GPT-5.6 Terra 4 questions, 44 citations, 100/100/100, 2508 s, 13,353,797 tokens, $0; Claude Opus 5.5 2 questions, 85 citations, 100/97/100, 2199 s. All rows `git_dirty: true`; results are 0.5.3, not 0.5.65.
- Final artifact `outputs/feynman-eval-case-study.md` written and verified: 20 sources, no uncited sources, no missing citations. Status: verified for cited claims; eval suite not executed (read-only audit).
