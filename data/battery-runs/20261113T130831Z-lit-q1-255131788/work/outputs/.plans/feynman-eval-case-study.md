# Plan: Feynman harness case study (AI-eval-quality lens)

## Questions
1. What eval-relevant machinery does the harness actually ship (prompts, agents, telemetry, transcripts, gates)?
2. Where does the harness's own verification loop provide evidence vs. self-attestation?
3. What can be measured reproducibly from a live run, and what is missing?

## Method
- Static audit of installed 0.5.65 package: system prompt, 4 subagent prompts, 11 workflow prompts, telemetry extension, session JSONL schema, CLI flags.
- Dogfood probe A: transcript integrity audit over the live session (script + output).
- Dogfood probe B: red-team the `verifier` subagent with 6 planted defects + 2 controls; score detection.
- Report strengths, risks, recommended eval contract.

## Ledger
- [x] static inventory
- [x] transcript audit script + run (88 records, pass; experiments/transcript-audit.json)
- [x] verifier red-team fixture + 3 runs (leaked, clean x2; 6/6 each; leakage found)
- [x] reviewer probe (caught verifier false claim)
- [x] public eval-suite audit (12 questions, deterministic runner, 0.5.3 results)
- [x] synthesis artifact -> outputs/feynman-eval-case-study.md

## Verification log
- Version confirmed: `feynman --version` -> 0.5.65
- No tests/evals directory in distributed package (npm `files` excludes tests).
- Public repo has 62 test files; 0 named eval/verifier/citation; prompt tests assert strings/structure.
- Clean verifier runs: 6/6 defects, 2/2 controls, 1.7x cost spread, one false justification in run 2.
- Reviewer run: caught FATAL false claim; MAJOR disagreement on BERT priority claim.
- Public eval suite: 12 fixed questions, deterministic identifier/title/recall/cost scoring, isolated homes; committed 0.5.3 baselines are git_dirty=true and cover 4/12 questions. No semantic-support metric.
