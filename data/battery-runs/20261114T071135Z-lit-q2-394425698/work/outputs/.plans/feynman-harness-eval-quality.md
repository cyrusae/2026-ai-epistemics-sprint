# Plan: Feynman harness case study (AI-eval-quality lens)

- **Slug:** `feynman-harness-eval-quality`
- **Date:** 2026-11-14
- **Harness under study:** `@companion-ai/feynman` 0.5.65 at `/opt/feynman/feynman-0.5.65-linux-arm64/app`
- **Mode:** ad-hoc instrumented self-study, not a `/deepresearch` conformance run
- **Status:** complete (probes run; reviewer untested)

## Key questions

1. What eval-quality properties should an AI research harness be judged on, per the
   evaluation-science literature?
2. Which of those properties does Feynman 0.5.65 implement as explicit mechanisms
   (prompts, agent contracts, tool schemas, artifact rules), and which are absent?
3. Does the central integrity mechanism — the `verifier` agent — actually detect
   seeded citation/claim defects at the rate its contract implies?
4. What does the harness's evidence-gathering default do to precision (a key input
   to any downstream evaluation)?
5. Where are the honest limits of this study?

## Evidence needed

- Primary eval-quality frameworks: construct validity, agentic benchmark rigor,
  variance/error bars, reproducibility, citation-integrity.
- Verbatim harness artifacts: `SYSTEM.md`, `.feynman/agents/*.md`, `prompts/*.md`,
  `extensions/research-tools/*.ts`, `RELEASES.md`.
- Direct experimental output from the harness itself.

## Scale decision

Lead-owned work, plus one delegated `verifier` run as the behavioral probe.
No multi-researcher fan-out: the evidence base is small, curated, and mostly
local, so delegation would add coordination cost without reducing uncertainty.
(Exception: the probe deliberately exercises one subagent path to observe
file-handoff behavior.)

## Task ledger

| # | Task | Owner | Status | Output |
|---|------|-------|--------|--------|
| T1 | Extract harness eval-relevant mechanisms | lead | done | this plan + notes |
| T2 | Build literature-grounded rubric | lead | done | brief |
| T3 | Static mechanism audit with file:line evidence | lead | done | brief |
| T4 | Build seeded-defect verifier probe + oracle | lead | done | `experiments/verifier-probe/` |
| T5 | Run `verifier` subagent on probe | subagent | done | `experiments/verifier-probe/verified.md`, `verified2.md` |
| T6 | Score probes against oracles | lead | done | `experiments/verifier-probe/results.md` |
| T7 | Retrieval precision probe (5 queries) | lead | done | `experiments/retrieval-probe/results.md` |
| T8 | Process/handoff observations | lead | done | brief §6 |
| T9 | Write brief + provenance sidecar | lead | done | `outputs/feynman-harness-eval-quality.md` |

## Verification log

| Check | Method | Result |
|---|---|---|
| All planned citations resolve to the claimed title/year/first author | arXiv ID lookup batch + Crossref/S2 | verified 2026-11-14 |
| `2410.18982` = LitSearch (my prior) | arXiv lookup | **FALSE** — resolves to "O1 Replication Journey". ID dropped. |
| Harness version | `package.json` | 0.5.65 |
| Runtime | `node --version`, `date -u` | Node v24.21.0, 2026-11-14T07:33:38Z |
| Probe defects unambiguous | manual oracle construction | done |
| Verifier probe scored by oracle | diff + item table | done — 10/10 + 5/5; 6/6 + 4/4 |
| Probe 1 confound identified and corrected | second probe with empty research file | done |
| Verifier's OpenAlex records re-queried | openalex_get_work | confirmed W7197047848, W4416268504 |
| Final probe URLs live | `curl -L` | 8/8 HTTP 200 |
| Retrieval probe reproducible | fixed query list + endpoint provenance | done, n=5 |

## Decision log

- **D1:** Treat this as a *case study of one harness version*, not a benchmark of
  Feynman across models/versions. n=1 is stated throughout.
- **D2:** Use the harness's own `verifier` agent as the behavioral probe rather
  than a hand-written checker, because the claim under test is about the harness's
  integrity layer, not about my own checking ability.
- **D3:** Score probes by *whether a defect survives as an asserted fact*, not by
  whether the agent narrates that it checked something. Narration is cheap.
- **D4:** Do not invoke `/deepresearch` end-to-end; that would test a different
  construct (workflow conformance) and blow the scope. Listed as next step.

## Next step

Run T5 (verifier subagent), then score T6.
