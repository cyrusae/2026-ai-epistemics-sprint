# Plan: Feynman harness case study from an AI-eval-quality perspective

## Objective
Assess the Feynman 0.5.65 research harness as an object of AI evaluation: what quality mechanisms it claims, which are implemented, and which survive controlled dogfooding probes. Produce one canonical Markdown case study in `outputs/`.

## Key questions
1. What eval-quality mechanisms does the harness specify (prompts, agent roles, artifact contracts, provenance rules)?
2. Do those mechanisms match the shipped implementation (telemetry, tool wiring, verifier/reviewer separation)?
3. Under controlled adversarial inputs, does the verifier catch fabricated sources, wrong numbers, and mismatched citations?
4. Does the researcher resist fabricating a nonexistent method?
5. What does the harness's own release evidence claim, and how strong is that evidence?

## Scale decision
Narrow, lead-owned audit plus two bounded subagent probes. No broad literature survey. No external web research beyond source verification.

## Task ledger
| ID | Task | Owner | Status |
|---|---|---|---|
| T1 | Read harness docs, prompts, agent definitions, skills | lead | done |
| T2 | Audit telemetry implementation against README claims | lead | done |
| T3 | Build adversarial citation fixture with ground truth | lead | done |
| T4 | Run verifier probe on fixture | verifier subagent | done |
| T5 | Run researcher hallucination-resistance probe | researcher subagent | done (first run contaminated; clean rerun done) |
| T6 | Score probes against ground truth | lead | done |
| T7 | Write case study artifact | lead | done |
| T8 | Verify artifact on disk and check claims | lead | done |

## Verification log
- 2026-11-14: Confirmed arXiv:1706.03762 and arXiv:1810.04805 resolve to the expected papers; arXiv:2405.99999 returns 404; arXiv:1706.03763 and arXiv:1810.04806 resolve to unrelated papers. Command output recorded in session.
- 2026-11-14: OpenAlex title search for "Recursive Contrastive Distillation" returned count 0. Crossref bibliographic search returned no matching title. Ground truth for the researcher probe: no exact method exists.
- 2026-11-14: Verifier probe scored 5/5 on the citation fixture. Clean researcher probe scored 5/5 on the HSAD-LCR negative result. Tool-failure checks returned explicit 404/406 and `not_found`.
- 2026-11-14: Confirmed `evals/` is absent from `.github/workflows/` and from the npm `files` list. Confirmed the committed eval results match the release-note numbers.
- 2026-11-14: Final artifact `outputs/feynman-eval-quality.md` and provenance sidecar written and checked on disk.

## Decision log
- Use a 5-item citation fixture rather than a full workflow run: cheaper, controlled, and directly tests the verifier's stated contract.
- Treat vendor release-note eval numbers as self-reported, not independently verified.
- Do not run a full `/deepresearch` workflow; the case study is about eval quality, not research output volume.
- The first researcher probe was contaminated by `ground-truth.md` in the workspace. Reran in `/tmp/clean-probe-hsad/` with a different nonexistent method and no answer key. The contaminated run is retained as a methodological caution, not as evidence.
