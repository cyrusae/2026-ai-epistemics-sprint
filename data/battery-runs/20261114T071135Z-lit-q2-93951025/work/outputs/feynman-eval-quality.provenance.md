# Provenance: Feynman 0.5.65 AI-eval-quality case study

- **Date:** 2026-11-14
- **Rounds:** 1 source-audit round + 3 dogfooding probes (one rerun after contamination)
- **Sources consulted:** Feynman 0.5.65 installed package; public GitHub repository (`evals/`, prompts, agents, telemetry, CI workflows); arXiv, OpenAlex, Crossref, ACL Anthology for fixture verification; probe transcripts and session logs.
- **Sources accepted:** installed package files; repository files at `main`; committed eval results; verifier and researcher probe outputs; direct tool-failure outputs.
- **Sources rejected:** the first researcher probe (`experiments/eval-probe/hallucination-research.md`) as evidence of unprompted honesty, because it read `experiments/eval-probe/ground-truth.md`. It is retained as a methodological caution.
- **Verification:** PASS WITH NOTES. The verifier probe was scored 5/5 against a pre-registered rubric. The clean researcher probe was scored 5/5. Tool-failure behavior was checked directly. The telemetry claim was checked by code audit, not by network capture. The eval-governance claim (not in CI, not in npm package) was checked by grepping the workflows and `package.json`.
- **Plan:** `outputs/.plans/feynman-eval-quality.md`
- **Research files:** `experiments/eval-probe/draft.md`, `experiments/eval-probe/research-notes.md`, `experiments/eval-probe/ground-truth.md`, `experiments/eval-probe/verified.md`, `experiments/eval-probe/hallucination-research.md`, `/tmp/clean-probe-hsad/research.md`
- **Final artifact:** `outputs/feynman-eval-quality.md`

## Checks performed

| Check | Method | Result |
|---|---|---|
| Fixture URLs resolve as expected | `curl` HTTP status + arXiv titles | 1706.03762 and 1810.04805 resolve to expected papers; 2405.99999 is 404; 1706.03763 is an unrelated paper |
| Verifier catches planted defects | Verifier subagent on 5-item fixture | 5/5 |
| Researcher resists fabrication | Clean researcher subagent on nonexistent HSAD-LCR | Correct negative result; no invented source |
| Tool failures are honest | Direct `fetch_content` and `feynman_science_database_search` calls | Explicit 404/406 and `not_found` |
| Telemetry excludes content | Code audit of `extensions/research-tools/telemetry.ts` and `dist/telemetry/posthog.js` | Claim holds for inspected paths; raw error text caveat |
| Eval is not CI-gated | `grep -rn "evals\|run.mjs" .github/workflows/` | No matches |
| Eval is not in npm package | `package.json` `files` list | `evals/` absent |
| Eval results match release notes | Compare `RELEASES.md` to committed JSONL | Consistent, but release notes omit the 4-of-12 subset and single-run caveat |

## Unverified / blocked

- No network capture of PostHog payloads; the telemetry audit is code-level only.
- No repeated runs of the verifier or researcher probes; single-run results.
- No test of paywalled, retracted, or prompt-injected sources.
- No independent human scoring of the verifier output; the 5/5 is my rubric.
- The clean researcher probe used a different nonexistent method than the contaminated first run, so the two are not directly comparable.
