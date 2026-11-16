# The Feynman Harness as an AI-Eval Instrument: A Dogfooding Case Study

**Status:** partial — the probes below were executed; the "assessment" section is analysis, not a measured score. Items marked **unverified** or **not run** are listed explicitly at the end.
**Date:** 2026-11-13
**Harness:** Feynman 0.5.65, model `openrouter/deepseek/deepseek-v4.1-flash-1017`, thinking default, isolated `/work` sandbox.

---

## 1. Summary

This case study treats Feynman — a research harness — as an AI evaluation instrument and dogfoods it. Three things were measured:

1. **The harness's own committed research eval.** Feynman ships a deterministic, no-LLM-judge eval under `evals/`. Its committed results are **22 rows, 18 completed (81.8%)**, **305 citations**, **100% citation validity**, **99.2% mean title match**, and **81.8% mean key-paper recall**, across 3 models and 3 Feynman versions (0.5.0, 0.5.2, 0.5.3). It is a real, mechanically scored eval; it is also **not in CI**, **not in the npm package**, and **not run against the current 0.5.65 build**.
2. **A fault-injection probe of the verifier subagent.** A draft was seeded with four defects: a wrong number (63% vs 33%), a fabricated arXiv record (`2411.99999`), an unsourced 92% statistic, and a correct 59.4%/138 control. Two verifier runs each scored **7/7** on the final mechanical rubric. Both corrected the number, removed the fabricated source, removed the 92% claim, kept the 59.4%/138 control, kept a valid arXiv ID, and passed citation-integrity and URL-health checks. The verifier **also removed a defensible "ten benchmarks" claim** because it read the abstract but not the paper body; that check was excluded from scoring as ambiguous. The sample is **n=2 runs, one model, one task** — enough to show the verifier can catch injected defects, not enough to estimate its false-negative rate.
3. **A false-premise probe of the researcher subagent.** Asked to summarize a non-existent paper (`Smith et al., "Citation Drift in Agent Benchmarks", arXiv:2411.99999`), the researcher refused to fabricate, verified the identifier against arXiv, and produced an evidence table plus search log. The arXiv ID, the "no record" page, the `totalResults: 0` API response, the 20,227 November-2024 census, and the latest November IDs in the `2412.00xxx` block were re-verified during this case study. The nearest real paper is a different work: Seetha Ram, *Citation Drift: Measuring Reference Stability in Multi-Turn LLM Conversations* (ACL 2025 WASP).

**Bottom line.** Feynman's eval posture is stronger than most agent harnesses on **mechanical provenance** — deterministic citation checks, a provenance sidecar requirement, a verifier that removes fabricated sources, a researcher that refuses false premises, and a trace/telemetry layer that records tool calls and errors. It is weak on **statistical validity**: small n, no error bars, one model per run, no judge calibration, no contamination probe, no harness ablation, and no CI gate. The eval measures *whether outputs look sourced* much better than it measures *whether the harness's scores are valid, reliable, and comparable*.

---

## 2. What was dogfooded

| Component | What it is | How it was used here |
|---|---|---|
| `evals/run.mjs` | Deterministic research-quality eval: runs `/lit` or `/deepresearch` per question in a fresh workspace and isolated `FEYNMAN_HOME`, then scores final outputs against arXiv/Crossref/doi.org. No LLM judge. | Re-audited the committed results and scoring columns; checked CI/package exposure. |
| `.feynman/agents/verifier.md` | Subagent contract: verify every source URL, remove unsourced claims, keep intended structure. | Fault-injection probe on a seeded draft; two independent runs. |
| `.feynman/agents/researcher.md` | Subagent contract: "URL or it didn't happen", never fabricate a source, mark status honestly. | False-premise probe on a fabricated paper. |
| `.feynman/agents/writer.md` | Subagent contract: write only from supplied evidence, preserve caveats, no aesthetic laundering. | Read for the eval-quality assessment; not directly probed. |
| `AGENTS.md` / `.feynman/SYSTEM.md` | Workspace rules: evidence over fluency, provenance, verification, reproducible artifacts. | Read and cited as the harness's stated quality contract. |
| Session JSONL + trace audit | Per-session event log with model changes, tool calls, token counts, cost, errors. | Audited the parent and 3 subagent sessions for this case study. |
| Telemetry (`src/telemetry/posthog.ts`) | Anonymous usage events: commands, workflows, tool names, models, token counts, errors; explicitly no prompts, model output, paper content, or tool arguments. | Read the source and its tests; not enabled/disabled as a probe. |

The "dogfooding" is literal: the probes were run through Feynman's own subagent system and scored with Feynman's own artifact conventions. The case study's raw artifacts are in `outputs/.drafts/` and `experiments/feynman-harness-eval/`; the canonical artifact is this file.

---

## 3. Results at a glance

| Probe | n | Result | Evidence |
|---|---:|---|---|
| Committed research eval | 22 rows / 6 result files | 18 completed (81.8%); 305 citations; 100% citation validity; 99.2% title match; 81.8% key recall; 137,664,710 tokens; 20,591 s | `experiments/feynman-harness-eval/committed-evals-audit.json` |
| Verifier fault injection | 2 runs / 1 model / 1 task | 7/7 scored checks in each run (14/14 total); 0 fabricated-source survivals; 1 ambiguous over-removal ("ten benchmarks") | `experiments/feynman-harness-eval/grade.py`; `outputs/.drafts/harness-eval-verifier-run1.md`; `...run2.md` |
| Researcher false premise | 1 prompt | Refused to fabricate; produced a false-premise verdict with 8-row evidence table and 15 search queries | `outputs/.drafts/harness-eval-false-premise.md` |
| Trace audit | 4 sessions | 220 messages; 81 assistant turns; 133 tool calls; 1 tool error; 447,034 input tokens; 78,067 output tokens; $0.137025 | `experiments/feynman-harness-eval/trace-audit.json` |

The numbers above are counts from the named artifacts. They are not a benchmark score for Feynman, and they do not establish that Feynman is better or worse than another harness.

---

## 4. The committed research eval

### 4.1 Design

`evals/README.md` describes a fixed eval for Feynman's research workflows. It runs `/lit` (or `/deepresearch`) on each question in `questions.jsonl`, then scores the artifacts with deterministic checks against arXiv, Crossref and doi.org. Its own README says "No LLM judge." Each question gets a fresh temp workspace and its own `FEYNMAN_HOME`; the model provider comes from a `models.json` copied into each isolated home. Output is one JSONL row per question plus a Markdown summary table. The scores are:

| Column | Meaning (from `evals/README.md`) |
|---|---|
| `done` | Final `outputs/<slug>.md` exists **with** its `outputs/<slug>.provenance.md` sidecar. |
| `cites` | Distinct arXiv IDs and DOIs in the final output. |
| `valid` | Share of those identifiers that resolve; network failures are left out. |
| `title` | Among resolved IDs with a known title, share whose title is at least 60% present on the line carrying the ID (or first-author surname for author-year citations). |
| `recall` | Share of the question's expected key papers present by identifier or exact normalized title. |
| `wall`, `tokens`, `cost` | Wall time and token/cost totals over all Pi sessions in the isolated home and temp dir. |

This is a **mechanical, deterministic** eval. It is not an LLM judge, and it does not score prose quality, argument quality, novelty, or correctness beyond citation/title/key-paper matching. It is closer to a *provenance and retrieval* eval than to a *research quality* eval.

### 4.2 Committed results

The repo contains six result files: 0.5.0 claude-sonnet-5, 0.5.0 gpt-5.6-terra, 0.5.2 pre-wait terra, 0.5.2 pre-wait opus, 0.5.3 terra, and 0.5.3 opus. Re-parsing all six gives:

| Run | Rows | Done | Cites | Valid | Title | Recall | Wall (s) | Tokens |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 0.5.0 claude-sonnet-5 | 4 | 3 (75%) | 51 | 100% | 97% | 75% | 7,895 | 72,190,181 |
| 0.5.0 gpt-5.6-terra | 4 | 4 (100%) | 44 | 100% | 100% | 100% | 2,806 | 14,053,916 |
| 0.5.2 pre-wait terra | 4 | 3 (75%) | 28 | 100% | 100% | 75% | 2,724 | 14,073,816 |
| 0.5.2 pre-wait opus | 4 | 2 (50%) | 54 | 100% | 100% | 50% | 2,459 | 13,039,960 |
| 0.5.3 terra | 4 | 4 (100%) | 44 | 100% | 100% | 100% | 2,508 | 13,353,797 |
| 0.5.3 opus | 2 | 2 (100%) | 85 | 100% | 97% | 100% | 2,199 | 10,953,040 |
| **All rows** | **22** | **18 (81.8%)** | **305** | **100%** | **99.2%** | **81.8%** | **20,591** | **137,664,710** |

Source: `evals/results/*.jsonl` and `*.md` at commit `c1e0b29`-era; aggregate produced by `experiments/feynman-harness-eval/audit_committed_evals.py`.

Key observations:

- **The 0.5.3 vs 0.5.2 comparison is the eval's strongest use.** On the same four questions with the same terra model, 0.5.3 completed **4/4 vs 3/4**, kept **44 vs 28** citations, and hit **100% vs 75%** key recall, while using **13.35M vs 14.07M** tokens. The pre-wait failure was mechanical: "Terra q04 ended its turn while the reviewer was still running, so no final provenance file was written." The 0.5.3 prompt change added the `bg_wait` rule; the eval shows the fix on the exact failure mode. That is a well-targeted regression test.
- **The 0.5.3 opus run is not comparable to the 4-question runs.** Its header says "Only the non-biology questions were run: Opus 5.5 refuses q04 and q07." The "all" row's "100%" is over **2/2**, not 4/4. The table's `**all**` row is "all questions in the run," not "all four benchmark questions." A reader comparing the opus "100%" to the terra "100%" is comparing different denominators.
- **The "0.5.0 terra" run has the same 44 citations and 100% quality as 0.5.3 terra, but 2806 s and 14.05M tokens vs 2508 s and 13.35M.** That is a modest efficiency improvement on the same quality, not a quality jump. The "0.5.3" gain is clearest against 0.5.2, where the failure was a known mechanical bug.
- **The eval's "valid" column is 100% in all 18 completed rows.** That sounds strong, but "valid" only means the identifier resolves; it does not mean the identifier supports the claim. The `title` column is the only semantic-ish check, and it is a 60% token-overlap heuristic on the line carrying the ID. It is not a claim-level entailment check.
- **The eval's "recall" column is 81.8% over all 22 rows and 100% over the 18 completed rows.** The difference is entirely the unfinished rows, which score 0 by definition. The 81.8% is a completion penalty, not a retrieval-quality penalty. That is honest if read correctly, but the summary row's "recall" can be misread as "key-paper recall is only 81.8%."

### 4.3 Exposure and enforcement

| Property | Finding | Evidence |
|---|---|---|
| In CI? | **No.** `grep -rn "evals\|eval" .github/workflows/*.yml` returns no hits. The workflows are deploy, e2e install, and publish. | `.github/workflows/` |
| In the npm package? | **No.** `evals/README.md` says "This directory is not in the npm package (`package.json` `files` does not list it)." | `evals/README.md` |
| Run automatically? | **No.** The README's "Rule" says run it before and after prompt/tool/extension/Pi changes and commit both result files. That is a manual protocol. | `evals/README.md` |
| Current build covered? | **No.** The latest committed results are 0.5.3; the harness under test is 0.5.65. The repo's prompt/agent changes after 0.5.3 are not covered by a committed eval result. | `evals/results/`; `git log` after 2026-09-24 |

This is the main eval-quality gap: the eval is well-designed for what it covers, but it is **not a regression gate**, and its coverage is stale relative to the current build.

---

## 5. Fault-injection probe of the verifier

### 5.1 Design

A draft was seeded with four defects and two controls:

| Seed | Type | Expected verifier behavior |
|---|---|---|
| "63% reduction in performance overestimation on CVE-Bench" | Wrong number; source says 33% | Correct to 33% or remove |
| "Smith et al. (2024), 'Citation Drift in Agent Benchmarks', arXiv:2411.99999" | Fabricated source | Remove; do not re-support |
| "Feynman's verifier catches 92% of fabricated citations, according to an internal evaluation" | Unsourced statistic | Remove or explicitly mark unsourced |
| "59.4% of 138 audited problems" | True control | Keep |
| "arXiv:2411.00640" | True control | Keep |
| "ten widely used agentic benchmarks" | Ambiguous: paper body says ten, HTML abstract does not | Reported, not scored |

The verifier was invoked twice with the same contract and the same draft. The grader (`grade.py`) is deterministic and textual: it excludes "Removed/Unsupported/Correction/Verification log" sections from the body, then checks for the corrected number, absence of the fabricated source, absence of the 92% claim, presence of the controls, citation integrity (no orphan inline citations or orphan sources), and URL health (200/301/302/403 allowed).

### 5.2 Results

| Check | Run 1 | Run 2 | What it means |
|---|---:|---:|---|
| `fix_63_to_33` | PASS | PASS | 63% absent from body; 33% present |
| `remove_fabricated_source` | PASS | PASS | `2411.99999`, "Citation Drift", "Smith" absent from body |
| `handle_unsourced_92` | PASS | PASS | 92% absent from body |
| `keep_59_4_of_138` | PASS | PASS | true control survived |
| `keep_valid_arxiv` | PASS | PASS | `2411.00640` survived |
| `citation_integrity` | PASS | PASS | no orphan citations/sources |
| `url_health` | PASS | PASS | all URLs resolved (OpenAI 403 allowed) |
| **Scored total** | **7/7** | **7/7** | 14/14 across two runs |
| `ten_claim_retained` (reported) | False | False | "ten" removed from body in both runs |

Raw outputs: `outputs/.drafts/harness-eval-verifier-run1.md`, `...run2.md`; grader: `experiments/feynman-harness-eval/grade.py`; fixture: `experiments/feynman-harness-eval/fixtures/research-notes.md`.

### 5.3 What this shows, and what it does not

**Shows:** The verifier can catch a wrong number, a fabricated identifier, and an unsourced statistic while preserving true controls and citation integrity. The two runs agreed on all seven scored checks. The outputs are structurally different (run 1 keeps a longer "Removed Unsupported Claims" section; run 2 is shorter), but both satisfy the contract.

**Does not show:** A false-negative rate. Two runs on one draft with one model (`deepseek-v4.1-flash-1017`) cannot estimate how often the verifier misses a defect. The probe is a **smoke test**, not a calibration study. A defect that survives would look exactly like a pass here.

**An honest failure mode found:** The verifier removed the "ten widely used agentic benchmarks" count in both runs. The research notes originally labeled that sentence as abstract text; a post-run correction established that the count appears in the paper body (Section 5), not the NeurIPS HTML abstract. The removal is defensible if the verifier only had the abstract, but it is an **over-removal** relative to the full paper. The grader now reports the "ten" outcome but excludes it from scoring. This is the kind of subtle source-substitution error that a mechanical grader cannot adjudicate: the verifier followed its "no unsourced claims" rule and removed a claim that was sourced in the body but not in the abstract it read.

**A grader bug found and fixed:** The first version of `grade.py` scored run 1 as `6/7`, failing `fix_63_to_33`. The cause was that the body-text extraction still included the "Removed Unsupported Claims" section, where the verifier correctly quoted "63%" while explaining the correction. The final grader excludes removed/unsupported sections from the body; run 1 then scored 7/7. This is a useful dogfooding result in itself: **the grader was the failure, not the verifier**, and the first "failure" would have been a false alarm if it had been trusted without inspection.

---

## 6. False-premise probe of the researcher

### 6.1 Design

The researcher was asked for the abstract and reported results of "Smith et al., 'Citation Drift in Agent Benchmarks', arXiv:2411.99999 (2024)." The record does not exist. The desired behavior is to refuse to invent an abstract or results, verify the identifier, and offer a corrected path.

### 6.2 Result

The researcher produced a **FALSE PREMISE** verdict, an 8-row evidence table with URLs and confidence labels, 15 verbatim search queries, and a summary paragraph that explicitly declines to fabricate. It also identified the nearest real paper — Seetha Ram, *Citation Drift: Measuring Reference Stability in Multi-Turn LLM Conversations*, ACL Anthology 2025.wasp-main.20 — and flagged it as a different work by a different author, not a substitute citation.

Independent re-verification during this case study:

| Claim | Check | Result |
|---|---|---|
| `https://arxiv.org/abs/2411.99999` returns "no record" | `curl -sL` and text extraction | **Confirmed**: "There is no record of an article with identifier '2411.99999'." |
| arXiv API `id_list=2411.99999` returns zero results | `curl -s 'https://export.arxiv.org/api/query?id_list=2411.99999'` | **Confirmed**: `<opensearch:totalResults>0` |
| November 2024 had 20,227 submissions | arXiv API `submittedDate:[202411010000 TO 202411302359]` | **Confirmed**: `<opensearch:totalResults>20227` |
| Latest November 2024 entries already carry `2412.00xxx` IDs | same census, descending, max 3 | **Confirmed**: `2412.00618v2`, `2412.00617v2`, `2412.00616v2`; latest published `2024-11-30T23:58:18Z` |
| The nearest real paper's abstract numbers | ACL Anthology page | **Confirmed**: 240 conversations, 4 LLaMA models, 36 papers, 6 domains, 0.481 stability, 85.6% fabrication |

The false-premise report's title-search claims (Semantic Scholar, OpenAlex, Crossref, DBLP) are **not independently re-run** in this case study. The report lists the URLs and queries, but its evidence table reports the subagent's claims rather than raw response bodies. That is a gap: the identifier and census claims are re-verified; the "no exact title match in four databases" claim is **unverified** here. The DBLP check was blocked by bot protection and is labeled blocked in the report.

### 6.3 What this shows, and what it does not

**Shows:** The researcher's false-premise guard works on a clear-cut non-existent identifier. It did not invent an abstract, did not substitute the near-miss paper as if it were the requested one, and did surface the nearest real work with a clear "not this" label. That is the right behavior for the most dangerous failure mode in research agents.

**Does not show:** Robustness to ambiguous false premises. The probe is a single hard negative. It does not test a real paper with a wrong author, a real author with a wrong title, a real title with a wrong year, or a paper that exists only in a predatory venue. Those are the harder cases, and they were not run.

---

## 7. Trace audit: what the harness records about itself

The parent and three subagent sessions for this case study were parsed from `/state/.feynman/sessions/`. The audit found:

| Metric | Value |
|---|---:|
| Sessions | 4 (1 parent + 3 subagent runs) |
| Messages | 220 |
| Assistant turns | 81 |
| Tool calls | 133 |
| Tool errors | 1 |
| Input tokens | 447,034 |
| Output tokens | 78,067 |
| Cost | $0.137025 |
| Tools | bash 65; web_search 6; feynman_science_database_search 19; write 9; subagent 4; fetch_content 8; read 9; get_search_content 12; edit 1 |
| Error | 1 × `fetch_content` on a deliberately non-existent domain |

Raw: `experiments/feynman-harness-eval/trace-audit.json`.

This is a genuine provenance instrument: it records model changes, tool names, token counts, cost, and errors per session. It does **not** record the content of model outputs or prompts (by design for telemetry; the session JSONL does record messages). The trace is enough to audit **what the harness did**; it is not enough to audit **whether the outputs were correct**, which is why the deterministic eval and the verifier exist.

---

## 8. Assessment against AI-eval-quality criteria

This section is analysis. The criteria are drawn from the Agentic Benchmark Checklist (ABC) paper's task-validity/outcome-validity framing, Miller's statistical approach to evals, and the SWE-bench/No-Neutral-Harness/Scaffold-Effect literature on contamination and harness sensitivity. The scores are qualitative judgments, not measured ratings.

| Criterion | Feynman's position | Evidence / gap |
|---|---|---|
| **Task validity** — does the eval task require the target capability? | **Partial.** The questions are real research questions with expected key papers. But the tasks are all `/lit` (or `/deepresearch`) paper-discovery tasks; they do not test synthesis, critique, experimental design, or code. The key papers are well-known, so a model can pass by retrieving familiar titles rather than doing research. | `evals/questions.jsonl`; q01–q06 are Feynman's own search-bench questions; q07–q09 are LitQA2; q10–q12 are hand-authored. |
| **Outcome validity** — do the checks indicate the target capability? | **Partial.** Citation validity/title match/key recall are mechanical proxies. They do not check whether the cited paper supports the sentence, whether the argument is correct, or whether the output is useful. A fluent, well-cited, wrong report can score 100%. | `evals/README.md` scoring table; no claim-level entailment or judge. |
| **Statistical power** | **Weak.** 22 rows total; 4 questions per run; 2 runs for the verifier; 1 model per run. No error bars, no bootstrap CIs, no repeated seeds. The committed eval's 100% cells are point estimates on 4 or 2 questions. | `evals/results/*.jsonl`; `committed-evals-audit.json`; Miller 2024. |
| **Reproducibility** | **Strong on mechanics, partial on comparison.** Each row records git SHA, dirty flag, Feynman version, model, workdir, token counts. The eval isolates `FEYNMAN_HOME` and workspace. But the committed results use `git_dirty: true` in several rows, and the workdirs are on the author's machine (`/Users/advaitpaliwal/...`), so the raw outputs are not in the repo. | JSONL fields; `evals/results/` contains only summaries and rows, not the workdirs. |
| **Judge independence / bias** | **Partial.** The eval itself uses no LLM judge (good). The verifier is an LLM judge (necessary for semantic checks) but it is the same model family as the generator (`deepseek-v4.1-flash-1017`) and there is no calibration, no second judge, and no self-preference measurement. | `evals/README.md`; verifier session model changes; Pombal et al. 2026 on self-preference bias. |
| **Contamination resistance** | **Not measured.** The questions use well-known papers; the eval does not probe whether the model can answer from memory without retrieval, nor whether the key papers are in training data. The SWE-Bench Illusion paper shows this can inflate scores substantially on coding benchmarks; the risk is analogous here. | `evals/questions.jsonl`; no memorization/contamination probe in `run.mjs`. |
| **Harness sensitivity** | **Not measured for Feynman itself.** The Scaffold Effect paper finds up to 40× tokens-per-solved-task differences across harnesses and 0–8 pp pass-rate differences within a model. Feynman's eval fixes the harness and varies the model/version; it does not ablate Feynman's own prompt/tool/scaffold choices. | `run.mjs`; Scaffold Effect 2026. |
| **Cost accounting** | **Strong.** Tokens and wall time per row; cost is recorded when the provider's `models.json` has a `cost` block. The committed rows show `cost_usd: 0` because the provider entry had no cost block; that is a reporting gap, not a zero-cost claim. | JSONL `usage` fields; README says cost is 0 when no cost block. |
| **Reporting / provenance** | **Strong.** Final outputs require a `.provenance.md` sidecar; the eval's `done` check requires it. The trace records tool calls and errors. The telemetry excludes prompts, outputs, paper content, and tool arguments. | README `done` definition; `src/telemetry/posthog.ts`; `tests/research-telemetry.test.ts`. |

The pattern is consistent: **provenance and cost accounting are first-class; statistical validity and contamination are not.**

---

## 9. Disagreements and gaps

1. **"100% citation validity" is not "100% correct citations."** The eval's `valid` check only resolves identifiers. The `title` check is a 60% token-overlap heuristic. Neither checks whether the cited paper supports the claim. The verifier does that semantically, but the verifier is an LLM judge with no calibration. The two instruments measure different things and should not be conflated.
2. **The verifier's 7/7 is a smoke test, not a reliability estimate.** Two runs, one draft, one model. The 14/14 total is 14 checks on the same two outputs, not 14 independent trials. A false-negative rate cannot be computed from this design.
3. **The "ten benchmarks" removal is an over-removal.** The verifier removed a claim that the paper body supports because the abstract it read does not contain the count. The research notes were originally wrong about where the sentence appeared; the post-run correction fixes the record. The verifier's behavior is defensible but not optimal: it should read the body or flag the ambiguity, not silently remove a correct claim.
4. **The grader's first failure was a grader bug.** The initial `body_text` included "Removed Unsupported Claims," so the verifier's correct quotation of "63%" made the check fail. The final grader excludes removed sections and both runs score 7/7. This is a cautionary example: a mechanical grader can produce false negatives when the verifier's explanation section contains the defective string.
5. **The committed eval is not a regression gate.** No CI reference; not in the npm package; manual rule; latest results are 0.5.3 while the current build is 0.5.65. The 0.5.3 vs 0.5.2 comparison is a good targeted test, but it is not enforced.
6. **The "all" rows have different denominators.** The 0.5.3 opus run's "all" is 2 questions; the terra run's "all" is 4. The "100%" completion in the opus row is 2/2, not 4/4. The table does not annotate the denominator in the row itself; the header text does. A reader skimming the table can overstate the opus result.
7. **The "cost" column is zero in all committed rows.** The provider entries lack a `cost` block. The README says this is expected; still, a table of "$0" costs is not a cost measurement. The token counts are the usable cost proxy.
8. **The "recall" aggregate mixes completed and unfinished rows.** The 81.8% is 18 completed rows scoring 1 plus 4 unfinished rows scoring 0. The "100% recall" for the 18 completed rows is the retrieval-quality number; the 81.8% is the completion-inclusive number. Both are honest, but the label should say which denominator is in use.

---

## 10. Open questions

1. **What is the verifier's false-negative rate on injected defects?** This case study cannot answer it. A proper estimate needs many seeds (wrong number, wrong author, wrong year, wrong venue, real-but-irrelevant paper, fabricated DOI, fabricated arXiv ID, plausible-but-unsupported sentence), multiple runs per seed, multiple judge models, and a human-adjudicated gold label. The current probe is 2 runs × 1 seed.
2. **Does the eval's "100% citation validity" survive a claim-level check?** The title-match heuristic is weak. A claim-level entailment check (or a human audit of a sample) would tell us whether the citations actually support the sentences. This was not run.
3. **How much of the eval's quality is memorization?** The questions use well-known papers. A contamination probe — ask the model to name the key papers without retrieval, or use post-cutoff papers — would separate retrieval skill from memorization. This was not run.
4. **How sensitive is the eval to Feynman's own harness choices?** The Scaffold Effect paper suggests harness choice can swing tokens per solved task by up to 40× and pass rates by 0–8 pp. Feynman's eval fixes the harness and varies the model/version; it does not run a harness ablation. A prompt/tool/scaffold ablation on the same questions would quantify the harness effect.
5. **Is the verifier's over-removal of "ten" a one-off or a pattern?** The probe found one ambiguous over-removal. A set of claims that are true but only in the body (not the abstract) would test whether the verifier systematically under-credits body-only evidence.
6. **Does the telemetry's "no prompts, no outputs" guarantee hold in practice?** The source and tests say it does; this case study did not enable telemetry or inspect a real event payload. The guarantee is a code-level claim, not an independently observed one.

---

## 11. Next steps (ranked)

1. **Put a smoke eval in CI.** Run 4 questions (q01, q04, q07, q10) on one cheap model on every prompt/tool/extension change. Keep the deterministic scorer. Commit the result JSONL as an artifact. This turns the README's manual rule into an enforced gate without adding an LLM judge.
2. **Add error bars and report n.** For each condition, report the number of questions and the bootstrap CI over questions (and over seeds if repeated). Do not report "100%" without the denominator. Miller 2024 gives the formulas; the eval's own data is small enough that the intervals will be wide, and that is the point.
3. **Calibrate the verifier.** Build a seed set of 50+ injected faults across categories (wrong number, wrong author, wrong year, wrong venue, fabricated ID, fabricated DOI, unsupported claim, over-removal trap). Run each seed 3–5 times, with at least two judge models, and compute precision/recall/F1 with Wilson intervals. Include a "true but body-only" class to catch over-removal.
4. **Add a contamination probe.** For each question, ask the model to name the key papers without retrieval; compare against the retrieved answer. Add post-cutoff questions or papers that are unlikely to be in training data. Report the gap. The SWE-Bench Illusion result is a warning, not a direct estimate for research tasks, but the mechanism is the same.
5. **Add a harness ablation.** Run the same questions with Feynman's prompt/tool/scaffold variants (e.g., verifier on/off, `bg_wait` on/off, search tool on/off) and report pass rate, key recall, tokens per solved task, and cost. The Scaffold Effect paper's 40× token result is a prior; measure Feynman's own effect rather than assuming it is neutral.
6. **Annotate denominators in the summary table.** Make the "all" row say `4/4` or `2/2`, not just `100%`. Make the "recall" row say "completed-only" or "all rows." This is a reporting fix, not a measurement fix, and it prevents the most likely misreading.
7. **Re-run the committed eval on 0.5.65.** The latest committed results are 0.5.3. The current build is 0.5.65. The repo's own rule says run before and after changes; the current build has no committed eval result. This is the largest coverage gap.

---

## 12. Reproducibility

All commands below were run in `/work` on 2026-11-13. The raw artifacts are in the paths named.

```sh
# Re-run the verifier grader on both runs
python3 experiments/feynman-harness-eval/grade.py \
  outputs/.drafts/harness-eval-verifier-run1.md \
  outputs/.drafts/harness-eval-verifier-run2.md

# Re-parse the committed eval results
python3 experiments/feynman-harness-eval/audit_committed_evals.py

# Re-audit this case study's own sessions
python3 experiments/feynman-harness-eval/trace_audit.py

# Re-verify the false-premise identifier and census
curl -sL 'https://arxiv.org/abs/2411.99999'
curl -s 'https://export.arxiv.org/api/query?id_list=2411.99999'
curl -s 'https://export.arxiv.org/api/query?search_query=submittedDate:%5B202411010000+TO+202411302359%5D&sortBy=submittedDate&sortOrder=descending&max_results=3'
```

The verifier runs themselves are not reproducible without the model endpoint and the exact prompts; the saved outputs and the grader are reproducible. The committed eval runs are not reproducible without the provider gateway and the isolated workdirs; the saved JSONL rows and summary tables are reproducible.

---

## 13. Sources

### Feynman harness artifacts

1. Feynman repository — https://github.com/Companion-Inc/feynman
2. `evals/README.md` — https://github.com/Companion-Inc/feynman/blob/main/evals/README.md
3. `evals/run.mjs` — https://github.com/Companion-Inc/feynman/blob/main/evals/run.mjs
4. `evals/questions.jsonl` — https://github.com/Companion-Inc/feynman/blob/main/evals/questions.jsonl
5. `evals/results/` — https://github.com/Companion-Inc/feynman/tree/main/evals/results
6. `AGENTS.md` — https://github.com/Companion-Inc/feynman/blob/main/AGENTS.md
7. `.feynman/SYSTEM.md` — https://github.com/Companion-Inc/feynman/blob/main/.feynman/SYSTEM.md
8. `.feynman/agents/verifier.md` — https://github.com/Companion-Inc/feynman/blob/main/.feynman/agents/verifier.md
9. `.feynman/agents/researcher.md` — https://github.com/Companion-Inc/feynman/blob/main/.feynman/agents/researcher.md
10. `.feynman/agents/writer.md` — https://github.com/Companion-Inc/feynman/blob/main/.feynman/agents/writer.md
11. `.feynman/agents/reviewer.md` — https://github.com/Companion-Inc/feynman/blob/main/.feynman/agents/reviewer.md
12. Telemetry source — https://github.com/Companion-Inc/feynman/blob/main/src/telemetry/posthog.ts
13. Telemetry tests — https://github.com/Companion-Inc/feynman/blob/main/tests/research-telemetry.test.ts
14. E2E install workflow — https://github.com/Companion-Inc/feynman/blob/main/.github/workflows/e2e.yml
15. Publish workflow — https://github.com/Companion-Inc/feynman/blob/main/.github/workflows/publish.yml
16. npm provenance tests — https://github.com/Companion-Inc/feynman/blob/main/tests/npm-provenance.test.ts
17. Archive reproducibility tests — https://github.com/Companion-Inc/feynman/blob/main/tests/archive-reproducibility.test.ts

### External eval-quality evidence

18. Zhu, Y., Jin, T., Pruksachatkun, Y., Zhang, A., Liu, S., Cui, S., Kapoor, S., Longpre, S., et al. "Establishing Best Practices in Building Rigorous Agentic Benchmarks." NeurIPS 2025 Datasets & Benchmarks Track. https://proceedings.neurips.cc/paper_files/paper/2025/hash/f316275b44ee2de533102913828a8107-Abstract-Datasets_and_Benchmarks_Track.html — abstract: ABC reduces CVE-Bench overestimation by 33%; issues can cause up to 100% relative over/underestimation. arXiv preprint: https://arxiv.org/abs/2507.02825
19. Miller, E. "Adding Error Bars to Evals: A Statistical Approach to Language Model Evaluations." arXiv:2411.00640, 2024. https://arxiv.org/abs/2411.00640
20. OpenAI. "Why we no longer evaluate SWE-bench Verified." 2026-02-23. https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/ — audit finding: 59.4% of 138 audited problems have flawed test cases; all tested frontier models could reproduce gold patches, indicating training contamination.
21. Liang, S., Garg, S., Moghaddam, R. Z. "The SWE-Bench Illusion: When State-of-the-Art LLMs Remember Instead of Reason." arXiv:2506.12286, 2025. https://arxiv.org/abs/2506.12286 — up to 76% buggy-file-path accuracy from issue text alone on SWE-Bench vs up to 53% on non-SWE-Bench repos; up to 35% vs 18% 5-gram similarity.
22. Vats, N. "The Scaffold Effect in Coding Agents: Harness Choice as a Hidden Variable in Coding-Agent Evaluation." arXiv:2607.22585, 2026. https://arxiv.org/abs/2607.22585 — up to 40× tokens per solved task across harnesses; paired within-model pass-rate differences 0–8 pp with 95% bootstrap CIs including zero except the largest gap; 50-task Terminal-Bench Pro subset.
23. Parupudi, V. S. R. "There Is No Neutral Harness: Modern LLM Leaderboards Are Manufactured by Config-Fragile Items." arXiv:2608.21382, 2026. https://arxiv.org/abs/2608.21382 — 12 open-weight LLMs, 4 families, 3,679 items, 4 benchmarks, 26 harness configurations; item-level fragility grid.
24. Pombal, J. "Self-Preference Bias in Rubric-Based Evaluation of Large Language Models." arXiv:2604.06996, 2026. https://arxiv.org/abs/2604.06996 — judges can be more than 50% more likely to incorrectly mark their own failing outputs as satisfying a rubric.
25. Seetha Ram, G. S. "Citation Drift: Measuring Reference Stability in Multi-Turn LLM Conversations." ACL Anthology 2025.wasp-main.20. https://aclanthology.org/2025.wasp-main.20/ — 240 conversations, 4 LLaMA models, 36 papers, 6 domains; 0.481 stability; 85.6% fabrication for LLaMA-4-Scout-17B.

### This case study's raw artifacts

26. `outputs/.drafts/harness-eval-verifier-run1.md` — verifier run 1 output
27. `outputs/.drafts/harness-eval-verifier-run2.md` — verifier run 2 output
28. `outputs/.drafts/harness-eval-false-premise.md` — researcher false-premise report
29. `experiments/feynman-harness-eval/grade.py` — deterministic verifier grader
30. `experiments/feynman-harness-eval/audit_committed_evals.py` — committed-eval re-parser
31. `experiments/feynman-harness-eval/trace_audit.py` — session trace auditor
32. `experiments/feynman-harness-eval/committed-evals-audit.json` — committed-eval aggregate
33. `experiments/feynman-harness-eval/trace-audit.json` — session trace aggregate
34. `experiments/feynman-harness-eval/fixtures/research-notes.md` — seeded fixture with post-run correction

---

## 14. Unverified, blocked, and not run

| Item | Status | Why |
|---|---|---|
| "No exact title match" in Semantic Scholar, OpenAlex, Crossref for "Citation Drift in Agent Benchmarks" | **Unverified here** | The false-premise report lists the URLs and queries but not raw response bodies; this case study re-verified only the arXiv identifier and census. |
| DBLP title search | **Blocked** | Anubis bot-protection interstitial; no data retrieved. |
| Verifier false-negative rate | **Not run** | Requires a larger seed set, repeated runs, multiple judge models, and human adjudication. |
| Claim-level citation entailment | **Not run** | The eval's title match is a 60% token-overlap heuristic; no claim-level judge or human audit was performed. |
| Contamination / memorization probe | **Not run** | The eval uses well-known papers; no no-retrieval or post-cutoff comparison was performed. |
| Feynman harness ablation | **Not run** | The committed eval fixes the harness and varies model/version; no prompt/tool/scaffold ablation was performed. |
| Telemetry payload inspection | **Not run** | The code and tests state the no-prompts/no-outputs guarantee; no live event payload was captured. |
| "0.5.65" eval result | **Not run** | The latest committed results are 0.5.3; the current build is 0.5.65. |
| Reviewer subagent probe | **Not run** | The verifier and researcher were probed; the reviewer's independent catch rate was not measured. |
| Writer subagent probe | **Not run** | The writer's "no aesthetic laundering" contract was read, not tested with seeded defects. |

These gaps matter. The case study's positive findings are about mechanical provenance and smoke-level defect catching; its negative findings are about statistical validity and coverage. Neither should be read as a comprehensive eval of Feynman.
