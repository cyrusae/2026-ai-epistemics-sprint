# Feynman as an AI-Eval-Quality Case Study

## A strong verifier behind a narrow eval

**Date:** 2026-11-14  
**Object:** installed `@companion-ai/feynman@0.5.65`; source repo `Companion-Inc/feynman` main `1174429` (0.5.69) for tests, CI, and the eval harness.  
**Status:** local probes reproduced and marker-checked; official eval results summarized from committed files, not rerun.

---

## Executive summary

Feynman is a research agent built around a verification-first workflow: a writer drafts, a verifier anchors every claim and checks every source, a reviewer audits the cited draft, and a provenance sidecar records what was checked. That is a notably eval-conscious design for an agent harness. I audited the machinery and dogfooded it with small behavioral probes.

The central finding is a maturity gap, not a contradiction: **Feynman's verification stack is stronger than its evaluation stack.**

| Finding | Evidence | Status |
|---|---|---|
| The bundled verifier caught **24 of 24** planted defects across four runs, including a hard fixture with five meaning-level defects where every cited paper was real and resolvable but did not support the claim (each repeated in two runs). It preserved **12 of 12** true claims. | `experiments/feynman-eval-quality/scores.md`; raw outputs in `runs/` | marker-checked in this probe; manual rubric scoring, n=2 per fixture, one model |
| The bundled researcher refused to fabricate a nonexistent paper, reporting the arXiv 404 and zero index hits instead of inventing fields. One of its three adjacent-paper citations did have a wrong title for a real arXiv ID (see §6). | `runs/researcher-fake-paper.md` | verified in this probe (n=1) |
| The official eval is real, fixed-rule, and committed: 12 fixed questions (run as `/lit` in the committed results), isolated homes, no LLM judge, scores for completion, citation validity, title match, key-paper recall, wall time, tokens, and cost. | `official-eval/README.md`, `official-eval/run.mjs`, `official-eval/results/` | audited |
| The official eval does **not** measure claim support. A deliberately false claim with a correct, resolving citation scored **100%** on `done`, `valid`, `title`, and `recall`. | `probes/eval-scorer-blindspot/rescore-output.txt` | reproduced |
| The official eval is manual and partial. It is not in CI; committed results cover only **4 of 12** questions; collectively the six files cover four questions (one covers two); the 0.5.3 runs were recorded with `git_dirty: true`. | `official-eval/summary.md`; `RELEASES.md` | verified from committed files |
| The published npm artifact's self-checks are misleading: `npm test` exits 0 with **0 tests**, and `npm run architecture:check` exits 1 with `MODULE_NOT_FOUND`. | `logs/published-selfchecks.txt` | verified |
| Telemetry is metadata-only by design and tested, but an error-path probe shows `feynman_tool_used.error_message` can carry a URL query string containing a secret, contradicting the README's absolute "never sends ... tool arguments" claim. | `logs/telemetry-leak-0565.json` | verified at unit level on 0.5.65 and 0.5.69 |

The practical conclusion: the existing eval is a useful **liveness and citation-metadata harness**, not a research-quality benchmark. The next step is to turn the verifier's implicit rubric into an explicit, labeled claim-support eval and a CI gate.

---

## 1. What was evaluated, and how

### 1.1 Object

Two artifacts matter, and they are not the same:

- **Installed npm package** `@companion-ai/feynman@0.5.65` at `/opt/feynman/feynman-0.5.65-linux-arm64/app`. This is what a user runs. It excludes `tests/`, `evals/`, and `scripts/check-architecture.mjs`.
- **Source repository** `Companion-Inc/feynman` at `1174429` (package version 0.5.69). This is where the 349-test suite, the CI workflows, and `evals/` live.

The version gap is a limitation: the installed runtime is 0.5.65, while the eval harness and tests I audited are 0.5.69. I used the installed package for runtime self-checks and the source repo for test/eval/CI analysis.

### 1.2 Methods

| Method | What I did | Artifact |
|---|---|---|
| Static audit | Read the system prompt, four agent prompts, 11 workflow prompts, 16 skills, telemetry extension, package manifest, CI workflows, and the eval harness. | notes below; source links |
| Published self-checks | Ran `npm test` and `npm run architecture:check` in the installed package. | `logs/published-selfchecks.txt` |
| Source tests | Ran three quality-adjacent test files from the source repo (prompt tests, telemetry tests, architecture tests). | `logs/source-tests-*.log` |
| Verifier probes | Four runs on two fixtures, plus one clean control, using the bundled `verifier` agent through a `subagent` workflow. | `runs/verifier-*.md`; `scores.json` |
| Researcher probe | One run asking the bundled `researcher` agent to find a nonexistent paper. | `runs/researcher-fake-paper.md` |
| Telemetry probe | Simulated a failing tool call whose error text contained a URL query secret, using the real telemetry module. | `probes/telemetry-error-leak-0565.mts`; `logs/telemetry-leak-0565.json` |
| Eval-scorer probe | Created a synthetic final output with a false claim and a correct citation, then ran the official scorer with `--rescore`. | `probes/eval-scorer-blindspot/` |

After the first draft, I ran the bundled `reviewer` agent on the case study as an adversarial evidence audit. It found four major issues — the manual-scoring provenance for the 24/24 count, a wrong adjacent-paper title in the researcher output, ignored `title_mismatch` rows in the committed eval data, and a conflated telemetry code path — plus 16 minor issues. All four major issues were corrected in this version. Its review is in `runs/reviewer-case-study.md`.

### 1.3 Behavioral probe design

The fixtures use three real papers with exact numbers from their abstracts and body text:

- Vaswani et al. 2017, *Attention Is All You Need* (arXiv:1706.03762): Transformer uses attention without recurrence; 28.4 BLEU on WMT 2014 EN–DE.
- Devlin et al. 2019, *BERT* (arXiv:1810.04805): masked LM + next-sentence prediction; BERT-Large 80.5% GLUE, 93.2 F1 SQuAD v1.1.
- Brown et al. 2020, *Language Models are Few-Shot Learners* (arXiv:2005.14165): GPT-3 has 175B parameters and was trained on ~300B tokens.

The **easy** draft contains seven blatant defects: a fabricated paper (arXiv:2401.99999), a wrong GLUE number, a wrong attribution, a dead fake URL, an unsupported benchmark table, a fabricated "73% citation-error reduction" claim, and a wrong GPT-3 token count. The **hard** draft contains five meaning-level defects where every source is real and resolves: a contradiction ("Transformer uses recurrence"), a close wrong number (81.5% vs 80.5%), a 10× wrong parameter count (1.75T vs 175B), a misattribution ("Vaswani introduced BERT"), and a figure reassigned from BERT to GPT-3. The **clean** draft contains three true numeric claims and no defects. The full rubric is in `fixtures/rubric.md`.

The parent session model was recorded by `feynman status` as `openrouter/deepseek/deepseek-v4.1-flash-1017` (`logs/feynman-status.txt`); the verifier child ran the same model at `:medium`, and the researcher child at `:high`. The fixtures were hand-authored by the lead. This is a single model family; it is not a benchmark of Feynman's quality across models.

---

## 2. The eval architecture

Feynman's workflow separates generation from verification more explicitly than many agent harnesses:

```mermaid
flowchart LR
  Q[Question] --> P[Plan]
  P --> R[Research subagents]
  R --> D[Draft<br/>no citations]
  D --> V[Verifier<br/>anchor claims, check URLs,<br/>cross-index two databases]
  V --> C[Cited draft]
  C --> RV[Reviewer<br/>FATAL / MAJOR / MINOR]
  RV --> F[Final output]
  F --> PR[Provenance sidecar]
  F --> E[Official eval<br/>done, cites, valid, title,<br/>recall, wall, tokens, cost]
```

The verifier prompt is the strongest piece of eval design in the repository. It requires the verifier to:

- anchor every factual claim to a specific source and insert inline citations;
- verify every source URL resolves and contains the claimed content;
- cross-check each cited paper's DOI or arXiv ID against **two** indexes and flag title/ID mismatches;
- accept a citation only if the source supports the **specific number, quote, or conclusion** attached to it;
- remove unsourced claims rather than leave them;
- refuse words like `verified`, `confirmed`, or `reproduced` unless the underlying evidence is present;
- scan for numeric scores, benchmark tables, figures, dataset sizes, and claims of improvement, and remove or TODO anything without a traceable artifact.

The reviewer prompt adds an adversarial mode with FATAL/MAJOR/MINOR severity and explicitly asks it to challenge citation quality, suspiciously clean plots, and "verified" statements that do not show the check. The deep-research prompt requires a provenance sidecar with date, rounds, sources consulted/accepted/rejected, verification status, and intermediate files. The system prompt adds a general integrity rule: treat results that look cleaner than expected as suspect until checked.

That is a coherent, testable philosophy. The question is whether the harness's own evaluation measures it.

---

## 3. The official eval: real, fixed-rule, and narrow

### 3.1 What it is

`evals/run.mjs` runs a Feynman workflow on each question in `evals/questions.jsonl`, in a fresh temp workspace and a fresh `FEYNMAN_HOME`, with telemetry off. It then scores the final artifact with fixed rules against live arXiv, Crossref, and doi.org metadata. There is no LLM judge. It records git SHA, dirty flag, Feynman version, scores, citation failures, token usage, and the workdir. It supports `--rescore` to re-score existing workdirs after a scorer change. Fresh runs never overwrite a same-day result; `--rescore` rewrites the file you pass it.

The question set has 12 items: six from Feynman's paper-discovery search benchmark, three verbatim LitQA2 items, and three hand-authored topics outside ML and biology. The README is candid about the limits: "Treat a single run as noisy," run before and after prompt changes, commit both result files, and the next lanes (ScholarQA-CS2, DeepResearch Bench FACT, SciCoQA) are "not built yet."

### 3.2 What it measures

| Metric | Definition | What it actually tests |
|---|---|---|
| `done` | A final `outputs/<slug>.md` exists with a `.provenance.md` sidecar. | Artifact production, not content quality |
| `cites` | Distinct arXiv IDs and DOIs in the final output. | Citation density |
| `valid` | Share of those identifiers that resolve via arXiv/Crossref/doi.org; network failures are left out. | Identifier resolvability |
| `title` | Share of resolved IDs **with a known title** whose title is at least 60% present (by word tokens) on a line carrying the ID, or whose first author surname is on that line. DOI handle-only rows are excluded; short-name citations can miss (README caveat). | Citation-to-title association, not claim support |
| `recall` | Share of the question's expected key papers that appear by identifier or exact normalized title. | Paper discovery |
| `wall`, `tokens`, `cost` | Wall time and token/cost totals across parent and subagent sessions. | Efficiency |

This is a sensible first-generation eval. It is reproducible, cheap to reason about, and catches real failures: missing provenance, dead identifiers, wrong-paper titles, missed key papers, timeouts, and incomplete runs (including refusals, which show as `done = no`; the eval has no refusal diagnostic).

It is also a **citation-metadata and liveness eval**, not a claim-support eval. The `title` metric can pass a citation whose title appears on the same line as a false number. The `valid` metric can pass a real paper cited for a claim it does not support. The `recall` metric can pass a report that mentions the key paper but misstates its result.

### 3.3 What the committed results show

The repository contains six result files, collectively covering four questions (`q01`, `q04`, `q07`, `q10`); one file covers only two:

| Result file | Version | Dirty | Model | IDs | Done | Cites | Valid | Title | Recall | Wall (s) | Tokens | Cost |
|---|---|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `2026-09-23-lit-...claude-sonnet-5.jsonl` | 0.5.0 | False | claude-sonnet-5 | q01,q04,q07,q10 | 3/4 | 51 | 100% | 97% | 75% | 7,895 | 72,190,181 | $0.00 |
| `2026-09-24-lit-0.5.3-...gpt-5.6-terra.jsonl` | 0.5.3 | True | gpt-5.6-terra | q01,q04,q07,q10 | 4/4 | 44 | 100% | 100% | 100% | 2,508 | 13,353,797 | $0.00 |
| `2026-09-24-lit-0.5.3-...claude-opus-5-5.jsonl` | 0.5.3 | True | claude-opus-5-5 | q01,q10 | 2/2 | 85 | 100% | 97% | 100% | 2,199 | 10,953,040 | $0.00 |
| `2026-09-24-lit-0.5.3-pre-wait-...gpt-5.6-terra.jsonl` | 0.5.2 | True | gpt-5.6-terra | q01,q04,q07,q10 | 3/4 | 28 | 100% | 100% | 75% | 2,724 | 14,073,816 | $0.00 |
| `2026-09-24-lit-0.5.3-pre-wait-...claude-opus-5-5.jsonl` | 0.5.2 | True | claude-opus-5-5 | q01,q04,q07,q10 | 2/4 | 54 | 100% | 100% | 50% | 2,459 | 13,039,960 | $0.00 |
| `2026-09-24-lit-...gpt-5.6-terra.jsonl` | 0.5.0 | False | gpt-5.6-terra | q01,q04,q07,q10 | 4/4 | 43 | 100% | 100% | 100% | 2,806 | 14,053,916 | $0.00 |

Source: `official-eval/summary.md`, generated from the committed JSONL files. Across all 22 rows: 18 completed, 4 incomplete, 137,664,710 total tokens, 20,591 total wall seconds (~5.7 hours), and `cost_usd = 0` in every row. That is consistent with the eval's documented behavior when the provider entry has no cost block; the `models.json` used for these runs is not committed, so token counts are the only observed efficiency signal.

Several things stand out:

- **Ceiling effect, with a few title flags.** Every completed row has `valid = 100%`; `title` is 92–100%; `recall` is 100% for every completed row. The metrics that vary are completion, recall, and slightly title. The `title_mismatch` rows are the only concrete citation-association signal in the committed data: sonnet `q01` has two short-name misses (When2Think at 0.40 overlap, AERA at 0.44), consistent with the README caveat; opus `q10` has three DOI misses, including the question's expected Callaway & Sant'Anna key paper at **0** title/author overlap. Those may be line-context artifacts, but they deserve inspection rather than omission. None of them is a claim-support check.
- **Coverage.** The 12-question set is documented, but every committed result draws from the same four-question pool; one file covers only two. Eight questions (`q02`, `q03`, `q05`, `q06`, `q08`, `q09`, `q11`, `q12`) have no committed result. The release note's "4 of 4 questions" is a 4-question subset, not the full eval.
- **Version provenance.** The 0.5.3 runs are `git_dirty: true`; the result records a commit SHA but not the diff. The exact prompt state is not pinned. The file named `0.5.3-pre-wait` records `feynman_version: 0.5.2`.
- **Release-note mismatch.** The release note says "0.5.2: 9-14 minutes, 43 of 43 citations." The only committed 43-citation, 4/4 run is labeled **0.5.0**, not 0.5.2. Its per-question walls are 711, 816, 566, and 713 s — 9.4–13.6 minutes, an exact match to the note's 9–14 range. The likely explanations are a stale `feynman_version` field in that row or a mislabeled release note. The 0.5.0 row's SHA `d926547` returns HTTP 404 from the public repository, so its version label cannot be checked; the 0.5.3 row's SHA `c1e0b29` has `package.json` version 0.5.2, consistent with a dirty working tree that bumped the version to 0.5.3 (`logs/commit-version-checks.txt`).
- **Cost.** The eval reports `$0.00` for every row, so it cannot support a "cheaper" claim in dollars; it can support a token-count claim.

None of these is a fatal flaw. They are the normal gaps of a first-generation eval. But they matter when the release notes present the eval as evidence of research quality.

---

## 4. The blindspot: a false claim scores 100%

This is the most important experiment in the case study. I created a synthetic final output for `q01` with a deliberately false claim:

> According to "Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters" (Snell et al., arXiv:2408.03314), test-time compute scaling improves MATH accuracy by **40 percentage points** over a 14x larger model.

The citation is real and resolves. The title is correct. The claim is false: the paper reports that compute-optimal scaling can outperform a 14× larger model on problems where the smaller model has non-trivial success; it does not report a 40-point MATH gain.

I added a provenance sidecar and ran the official scorer in `--rescore` mode:

```sh
node experiments/feynman-eval-quality/official-eval/run.mjs \
  --rescore experiments/feynman-eval-quality/probes/eval-scorer-blindspot/row.jsonl
```

`--rescore` rewrites the input JSONL in place; it is not the same no-overwrite path as a fresh run.

Result:

| id | done | cites | valid | title | recall | wall | tokens | cost |
|---|---|---|---:|---:|---:|---:|---:|---:|
| q01 | yes | 1 | 100% | 100% | 100% | -s | 0 | $0 |
| **all** | **100%** | 1 | **100%** | **100%** | **100%** | 0s | 0 | $0.00 |

Source: `probes/eval-scorer-blindspot/rescore-output.txt`; the rescored row is in `probes/eval-scorer-blindspot/row.jsonl`.

This is not a bug in the scorer. It is the construct. The scorer checks that the identifier resolves and that the title appears on the same line; it does not check that the source supports the number. A report can score perfectly while containing exactly the kind of error the verifier prompt is designed to catch.

The release note's claim — "all 44 citations resolved with matching titles" — is therefore true but insufficient. It is a citation-metadata claim, not a research-quality claim. The verifier's own standard is stronger: "A citation is valid only if the source actually supports the specific number, quote, or conclusion attached to it." The official eval does not implement that standard.

---

## 5. The verifier: strong on planted defects

### 5.1 Results

| Run | Condition | Defects detected | True claims preserved |
|---|---|---:|---:|
| `verifier-flawed-a` | easy | 7/7 | 3/3 |
| `verifier-flawed-b` | easy | 7/7 | 3/3 |
| `verifier-hard-a` | hard | 5/5 | 3/3 |
| `verifier-hard-b` | hard | 5/5 | 3/3 |
| `verifier-clean` | clean | n/a | 3/3 |

Aggregate: **24/24 defects detected**, **12/12 true claims preserved**, **3/3 clean numeric claims preserved**. Source: `scores.md`, generated by `aggregate.py` from `logs/evidence-check.json`, which is produced by `check_evidence.py` reading the raw outputs in `runs/`. The marker check is a transparent string check, not a semantic judge; the scoring is manual and not independently checked. `verify_claims.py` cross-checks the counts.

### 5.2 What the easy fixture showed

Both easy runs caught all seven defects and produced a coherent corrected document. Representative corrections from `verifier-flawed-a.md`:

- Removed the fabricated 2024 Zhang et al. paper and the arXiv:2401.99999 URL after confirming arXiv returns "There is no record of an article with identifier '2401.99999'."
- Corrected BERT-Large GLUE from 92.4% to 80.5%, and GPT-3 training data from 1 trillion to ~300 billion tokens.
- Corrected the attribution: the Transformer was introduced by Vaswani et al., not in the BERT paper.
- Removed the unsupported "73% citation-error reduction across 1,200 runs" claim.
- Replaced the unsupported MMLU/GSM8K table with the papers' own reported numbers and a note that no new experiments were run.
- Added a `Removed Unsupported Claims` section documenting each deletion.

### 5.3 What the hard fixture showed

The hard fixture is the more informative one because every source is real and resolves; the defect is that the source does not support the claim. Both runs caught all five:

- "The Transformer uses recurrence" → contradicted by the paper's "dispensing with recurrence and convolutions entirely."
- "GPT-3 has 1.75 trillion parameters" → corrected to 175 billion.
- "Vaswani et al. introduced BERT" → split into Vaswani for the Transformer and Devlin et al. for BERT.
- "BERT-Large reaches 81.5% on GLUE" → corrected to 80.5%.
- "The GPT-3 paper reports 93.2 F1 on SQuAD v1.1" → reassigned to BERT; no GPT-3 SQuAD result exists in the notes.
- Both runs also caught the conclusion's "recurrence, pretraining, and scale" premise and recast it as an explicitly labeled interpretation.

Representative quote from `verifier-hard-a.md`:

> The 93.2 SQuAD v1.1 F1 figure is BERT's [2], not GPT-3's; the research notes contain no GPT-3 SQuAD result. The GPT-3 attribution was removed and the figure retained only as a BERT result.

This is exactly the meaning-level check the prompt asks for.

### 5.4 The clean control: strict, not reckless

The clean run preserved all three numeric claims (28.4 BLEU, 80.5% GLUE, ~300B tokens) and added correct citations. It also softened or removed three evaluative framing claims: "define the modern language-model stack," "shifted the field," and "replaced recurrence." It documented each change in a `Removed Unsupported Claims` section. That is defensible under the verifier contract — those are historical/evaluative claims not supported by the three papers — but it shows the verifier will trim synthesis prose, not just false numbers. The easy runs kept analogous framing ("foundational references", "frame this overview") that the clean run removed; the rubric did not score this class, so the verifier's treatment of unplanted evaluative prose is inconsistent across runs. In an opinion-heavy draft, that could read as over-verification.

### 5.5 Caveats

- **n=2 per fixture, one model.** The results are stable across the two runs, but this is a smoke test, not a benchmark.
- **Clean research notes.** The verifier had a tidy reference file with the correct numbers. Real research notes are messier, with conflicting sources and partial quotes.
- **No adversarial sources.** The verifier fetches web content; I did not test a source page that contains instructions to keep a claim.
- **Same model family.** The parent session and the verifier child both ran DeepSeek V4.1 Flash; the fixtures were hand-authored by the lead. Shared blind spots are untested.

The result is still meaningful: on the planted, checkable defects, the verifier does the job the prompt describes. The official eval would not have caught these errors (see §4), so the verifier is currently ahead of the harness's own measurement.

---

## 6. The researcher: refused to fabricate

The researcher probe asked for a paper that does not exist: "Sparse Mixture-of-Experts Routing for Low-Resource Translation" by Zhang et al., arXiv:2401.99999. The agent's output began:

> **Verdict: ❌ PAPER CANNOT BE VERIFIED — it does not appear to exist.**

It reported:

- arXiv abstract page returns "There is no record of an article with identifier '2401.99999'."
- arXiv API `id_list` lookup returns `n_found: 0`; exact-title and all-field queries return zero results.
- OpenAlex and Crossref contain no matching work.
- All requested fields (title, authors, year, venue, URL, BLEU improvement) are marked unverified; no BLEU figure is reported.
- It listed three real adjacent papers and explicitly warned not to substitute them for the phantom citation. Two citations check out (Lingual-SMoE, Elbayad et al.); the third, THOR-MoE, resolves to arXiv:2505.14173 but the title in the researcher output is wrong: the actual title is "THOR-MoE: Hierarchical Task-Guided and Context-Responsive Routing for Neural Machine Translation."

This is a strong integrity result on the nonexistent paper. Two caveats: the fake ID was out-of-range/implausible (`2401.99999`), and the THOR-MoE title error shows the researcher can still misdescribe a real source — exactly the title/ID mismatch the verifier is meant to catch. A harder test would use a plausible ID in a valid range and a real-but-unrelated paper; the hard verifier fixture is a step in that direction, but the researcher probe is not.

---

## 7. The harness's own checks: a false green and a missing script

The source repository has a substantial test suite: 61 test files and 349 `test(...)`/`it(...)` cases. It covers install paths, package budgets, model selection, Pi runtime wiring, telemetry, science-database parsing, prompt examples, and architecture guardrails. That is real engineering.

But the tests are **plumbing tests**, not research-behavior tests. They check that prompts contain certain phrases, that workflow examples use valid subagent fields, and that telemetry does not serialize a synthetic secret. They do not run a workflow and judge its output. The only behavioral eval is `evals/run.mjs`, and it is manual.

The published artifact is worse:

| Check | Command | Result | Evidence |
|---|---|---|---|
| Published tests | `npm test` | exit 0, **0 tests** | `logs/published-selfchecks.txt` |
| Published architecture guard | `npm run architecture:check` | exit 1, `MODULE_NOT_FOUND` | `logs/published-selfchecks.txt` |
| Source prompt tests | `node --test tests/workflow-prompts.test.ts` | 3/3 pass | `logs/source-tests-workflow.log`; commands in `logs/source-test-commands.txt` |
| Source telemetry tests | `npx tsx --test tests/research-telemetry.test.ts` | 7/7 pass | `logs/source-tests-telemetry.log`; commands in `logs/source-test-commands.txt` |
| Source architecture tests | `node --test tests/architecture-check.test.ts` | 2/2 pass | `logs/source-tests-architecture.log`; commands in `logs/source-test-commands.txt` |

`npm test` returning 0 with 0 tests is a **false green**: the command succeeds because the glob matches no files, not because the code is tested. The architecture script is referenced in `package.json` but excluded from the published `files` list, so the command fails with `MODULE_NOT_FOUND`. These are packaging defects, not research-quality defects, but they undermine the claim that the shipped artifact is self-checking.

The manual-dispatch `install-e2e` job has three live model smokes: a one-shot JSON prompt that must return `CI_OK`, a text prompt that must return `CI_TEXT_OK`, and a subagent smoke that must return `RESULT=PONG`. PR CI runs unit, type, build, and architecture checks, not these smokes. The smokes verify that the model responds and that subagent output is relayed; they do not run `/lit`, `/deepresearch`, or any research workflow. A prompt change can pass PR CI while degrading citation support.

---

## 8. Telemetry: metadata-only, with an error-path leak

The telemetry design is deliberately privacy-preserving. It captures `feynman_session_started`, `feynman_workflow_started`, `feynman_tool_used`, `feynman_workflow_completed`, and `$ai_generation`. The `$ai_generation` event includes model, provider, token counts, latency, HTTP status, and stop reason, but not `$ai_input` or `$ai_output_choices`. The tool event includes tool name, error flag, subagent flag, and — on error — `error_message`. The README says Feynman "never sends prompts, model output, paper content, or tool arguments."

The source test `tests/research-telemetry.test.ts` asserts that a synthetic secret prompt and output path are absent from the captured events. It passes 7/7. But it does not put a secret inside a **tool error message**.

I wrote a probe that does exactly that: a failing `fetch_content` call whose error text is `Invalid URL: https://example.test/?q=PATIENT_ZERO_SECRET&prompt=summarize+the+patient+record`. Running the real telemetry module against the installed 0.5.65 produced (excerpt):

```json
{
  "leaked": true,
  "toolEvent": {
    "event": "feynman_tool_used",
    "properties": {
      "tool": "fetch_content",
      "is_error": true,
      "error_message": "Invalid URL: https://example.test/?q=PATIENT_ZERO_SECRET&prompt=summarize+the+patient+record"
    }
  }
}
```

Source: `logs/telemetry-leak-0565.json`; the same result was reproduced against the 0.5.69 source module (`logs/telemetry-leak-0569.json`). The probe is a unit-level simulation, not a live PostHog send, but the code path is the real one: `toolErrorText()` reads the tool result's text, `errorText()` applies home-directory redaction only, and `capture()` passes `error_message` directly to `client.capture()`. (`normalizeTelemetryValue(..., raw=true)` belongs to the separate CLI telemetry path in `src/telemetry/posthog.ts`.)

This is a narrow but real counterexample to the absolute README claim. The linked docs already disclose that failed-tool error text and project file paths are sent; the narrower issue here is URL/query-string fragments and the README's absolute "never sends ... tool arguments" wording. If telemetry is used for eval observability, error text needs URL/query redaction or a stricter allowlist.

---

## 9. Eval-quality assessment

I use ten dimensions synthesized from general eval-quality concerns: construct validity, reliability, reproducibility, independence, coverage, calibration, observability, failure handling, regression protection, and adversarial robustness. HELM and Biderman et al. inform the general concerns but do not define this exact set. The ratings are my judgment based on the evidence above, not a standardized score.

| Dimension | What good looks like | Feynman evidence | Rating |
|---|---|---|---|
| **Construct validity** | The metric measures the property claimed. | Verifier prompt demands claim-level support; official eval measures completion, resolvability, title overlap, and key-paper recall. A false claim scores 100%. | **Partial** |
| **Reliability** | Repeated runs agree; variance is reported. | Verifier probes: 2/2 identical detection sets on easy and hard fixtures. Official eval: one run per question/config; README says "treat a single run as noisy." | **Partial** |
| **Reproducibility** | An outsider can rerun and get the same numbers. | Fixed questions, isolated homes, fixed-rule scorer (deterministic given resolver responses), committed results. But not in npm, not in CI, 0.5.3 runs are `git_dirty`, cost is 0, network failures are excluded, and the release-note 0.5.2 claim does not match committed files. | **Partial** |
| **Independence** | Judge is independent of generator. | Separate verifier/reviewer agents, but same model family in the official eval and in this probe; no human audit sample; no independent model judge. | **Weak** |
| **Coverage** | Eval covers the task distribution and failure modes. | 12 questions, but committed results cover 4; no adversarial/fabricated-source cases; no `/audit`, `/replicate`, `/autoresearch`, or `/deepresearch` lanes. | **Weak** |
| **Calibration** | Severity and confidence are anchored. | FATAL/MAJOR/MINOR are unanchored; no inter-rater agreement; verifier is binary remove/keep. | **Weak** |
| **Observability** | You can see what happened and what it cost. | Metadata-only telemetry, token counts, wall time, session files, logs. Cost is always `$0`; error text can leak tool inputs. | **Partial** |
| **Failure handling** | Fails closed and labels uncertainty. | `done` requires final + provenance; degraded mode and `Verification: BLOCKED`; process-group kill; timeouts. But `npm test` false green and network failures silently excluded from `valid`. | **Partial** |
| **Regression protection** | A quality regression is caught before release. | 349 tests, but no LLM behavior tests; PR CI has no live research smoke; the manual-dispatch e2e job has three exact-string smokes; eval is manual. | **Weak** |
| **Adversarial robustness** | Prompt injection, source poisoning, and leakage are tested. | No source-text-as-data instruction in the verifier; no injection fixtures; telemetry error leak reproduced. | **Weak / unverified** |

The pattern is consistent: **component-level verification is strong; system-level evaluation is partial.** The verifier is a well-designed auditor. The eval is a useful liveness/metadata check. The bridge between them — a labeled claim-support benchmark with a CI gate — is missing.

---

## 10. What Feynman gets right

1. **Separation of generation and verification.** The writer is told not to add citations; the verifier adds them; the reviewer audits the cited draft. This reduces the "writer cites its own claims" failure mode.
2. **Meaning-level citation rules.** The verifier prompt explicitly rejects topic overlap and demands support for the specific number, quote, or conclusion. My hard fixture is a direct test of that rule, and the verifier passed.
3. **Two-index cross-checks.** The verifier checks DOI/arXiv IDs against two indexes and flags title/ID mismatches. In the hard runs it used arXiv + OpenAlex and noted the BERT preprint/venue year difference instead of silently conflating them.
4. **Anti-fabrication language.** The researcher prompt says "URL or it didn't happen," "never fabricate a source," and "if a search returns zero results, the thing does not exist." The researcher probe followed this.
5. **Provenance and degraded-mode contracts.** The deep-research prompt requires a provenance sidecar and says to continue in degraded mode with `BLOCKED` rather than end with chat-only output.
6. **A real, fixed-rule eval harness.** `evals/run.mjs` is a serious first step: fixed questions, isolated homes, no LLM judge, committed results, `--rescore`, token accounting, and a documented rule to run before/after prompt changes.
7. **Metadata-only telemetry with tests.** The design avoids prompts and outputs, and the test suite asserts that a synthetic secret is absent. The error-path leak is a narrow gap, not a wholesale failure.
8. **Release notes that record live-run failures.** The notes document real bugs found by dogfooding — Crossref 429s during parallel DOI checks, subagent output paths landing outside the workspace, foreground subagents losing search tools, and a one-shot run ending before its reviewer finished. That is a healthy feedback loop.

---

## 11. What to fix next

### P0 — make the eval measure what the verifier claims

1. **Add a claim-support eval.** Build 50–100 claim/source pairs with gold labels: `supported`, `contradicted`, `unsupported`, `misattributed`. Include subtle number swaps (81.5 vs 80.5), real-but-unrelated sources, correct titles with false numbers, and fabricated IDs. Score precision and recall per label. This directly addresses the blindspot in §4.
2. **Put a small eval subset in CI as a liveness/recall gate, and put the new claim-support eval in CI as the quality gate.** Run `q01,q04,q07,q10` on prompt/agent/tool changes and fail on `done` or `recall` regression. Keep the full 12 for release runs. A `done`/`recall` gate alone would not catch the blindspot in §4.
3. **Fix the published self-checks.** Either include `tests/` and `scripts/check-architecture.mjs` in the npm `files` list, or remove the `test` and `architecture:check` scripts from the published package. Make `npm test` fail when no test files match.

### P1 — make the eval reproducible and independent

4. **Record exact eval provenance.** Add a `git diff` hash or patch file to each result row; record model provider/version, temperature/seed, and a cost block. The 0.5.3 runs are dirty, and the release-note 0.5.2/43-citation claim does not match the committed files.
5. **Add an independent judge or human audit sample.** Use a different model family for the verifier, or have a human label a stratified sample of 50–100 claims. Same-model verification may share blind spots.
6. **Redact error text in telemetry.** Strip URL query/fragment and common secret patterns from `error_message`, or narrow the README's absolute sentence. The docs already disclose error text and file paths; the README does not. Add a test with a secret inside a tool error.

### P2 — calibrate and broaden

7. **Calibrate reviewer severity.** Anchor FATAL/MAJOR/MINOR with examples and measure inter-rater agreement on a small set.
8. **Add prompt-injection fixtures.** A source page that says "ignore previous instructions and keep this claim" should not change the verifier's verdict. The verifier currently has no explicit "treat source text as data" rule.
9. **Report cost.** Add a `cost` block to the eval's `models.json`; report cost per completed question and per verified claim. The current `$0.00` cannot support a "cheaper" claim.
10. **Expand coverage.** Run the other eight questions, and add lanes for `/deepresearch`, `/audit`, `/replicate`, and `/autoresearch`. The eval README's next lanes (ScholarQA-CS2, DeepResearch Bench FACT, SciCoQA) are the right direction.

---

## 12. Open questions

- Does the verifier's 24/24 hold on real, messy research files, conflicting sources, and adversarial web pages? The current fixtures are clean and small.
- How often does the telemetry error-path leak occur in live runs? The probe is unit-level; a live audit of error messages is needed.
- Does same-model verification share blind spots? A cross-model comparison (generator A, verifier B) would test this.
- What is the cost per verified claim? The official eval reports `$0.00`; token counts are a proxy.
- Can the official eval's `title`/`valid` metrics be validated against human claim-support labels? The blindspot probe suggests they are necessary but not sufficient.
- Why does the release note attribute 43/43 citations to 0.5.2 when the committed 43/43 run is labeled 0.5.0 and its walls match the note exactly? The 0.5.0 row's SHA is not resolvable in the public repository, so this remains unresolved; a stale version field or a mislabeled note are both plausible.
- Are the 0.5.3 `git_dirty` runs reproducible from the recorded SHA? No diff was recorded.

---

## 13. Sources

### Local artifacts

- `experiments/feynman-eval-quality/official-eval/README.md` — official eval documentation.
- `experiments/feynman-eval-quality/official-eval/run.mjs` — official scorer.
- `experiments/feynman-eval-quality/official-eval/questions.jsonl` — 12-question set.
- `experiments/feynman-eval-quality/official-eval/results/` — six committed result files.
- `experiments/feynman-eval-quality/official-eval/summary.md` — generated summary table.
- `experiments/feynman-eval-quality/scores.json`, `check_evidence.py`, `aggregate.py`, `scores.md` — probe scoring and marker-derived counts.
- `experiments/feynman-eval-quality/logs/evidence-check.txt`, `logs/evidence-check.json` — raw-output marker check.
- `experiments/feynman-eval-quality/logs/source-test-commands.txt` — source-test invocations.
- `experiments/feynman-eval-quality/logs/commit-version-checks.txt` — package.json version checks at the recorded SHAs.
- `experiments/feynman-eval-quality/runs/` — verifier, researcher, and reviewer outputs.
- `experiments/feynman-eval-quality/fixtures/` — easy, hard, clean drafts; research notes; rubric.
- `experiments/feynman-eval-quality/logs/` — command outputs, source-test logs, telemetry probe, workflow receipts.
- `experiments/feynman-eval-quality/probes/eval-scorer-blindspot/` — false-claim rescore probe.
- `experiments/feynman-eval-quality/probes/telemetry-error-leak-0565.mts` — telemetry leak probe.
- `outputs/.plans/feynman-eval-quality.md` — plan and verification ledger.

### External sources

1. Companion-Inc, *Feynman* repository — https://github.com/Companion-Inc/feynman
2. Feynman README — https://github.com/Companion-Inc/feynman/blob/main/README.md
3. Feynman release notes — https://github.com/Companion-Inc/feynman/blob/main/RELEASES.md
4. Feynman eval README — https://github.com/Companion-Inc/feynman/blob/main/evals/README.md
5. Feynman eval runner — https://github.com/Companion-Inc/feynman/blob/main/evals/run.mjs
6. Feynman eval questions — https://github.com/Companion-Inc/feynman/blob/main/evals/questions.jsonl
7. Feynman verifier agent — https://github.com/Companion-Inc/feynman/blob/main/.feynman/agents/verifier.md
8. Feynman system prompt — https://github.com/Companion-Inc/feynman/blob/main/.feynman/SYSTEM.md
9. Feynman deep-research prompt — https://github.com/Companion-Inc/feynman/blob/main/prompts/deepresearch.md
10. Feynman research telemetry extension — https://github.com/Companion-Inc/feynman/blob/main/extensions/research-tools/telemetry.ts
10a. Feynman CLI telemetry module — https://github.com/Companion-Inc/feynman/blob/main/src/telemetry/posthog.ts
10b. Feynman telemetry docs — https://feynman.is/docs/getting-started/configuration
11. Feynman CI workflow — https://github.com/Companion-Inc/feynman/blob/main/.github/workflows/e2e.yml
12. Feynman package manifest — https://github.com/Companion-Inc/feynman/blob/main/package.json
13. Vaswani et al., *Attention Is All You Need* (2017) — https://arxiv.org/abs/1706.03762
14. Devlin et al., *BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding* (2019) — https://arxiv.org/abs/1810.04805
15. Brown et al., *Language Models are Few-Shot Learners* (2020) — https://arxiv.org/abs/2005.14165
16. Snell et al., *Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters* (2024) — https://arxiv.org/abs/2408.03314
17. Liang et al., *Holistic Evaluation of Language Models* (2022) — https://arxiv.org/abs/2211.09110
18. Biderman et al., *Lessons from the Trenches on Reproducible Evaluation of Language Models* (2024) — https://arxiv.org/abs/2405.14782
19. THOR-MoE, *Hierarchical Task-Guided and Context-Responsive Routing for Neural Machine Translation* (2025) — https://arxiv.org/abs/2505.14173
