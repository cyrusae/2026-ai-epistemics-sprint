# Reviewer: Evidence audit of “Feynman as an AI-Eval-Quality Case Study”

**Reviewed artifact:** `outputs/feynman-eval-quality-case-study.md` (2026-11-14, 37,121 bytes)
**Review mode:** adversarial evidence audit — verify the case study’s claims against the local artifacts it cites, the upstream repository at the recorded SHA, and the external sources needed to check quoted release notes and adjacent-paper citations.
**Scope:** factual errors, misreadings of `evals/run.mjs`, unsupported quantitative claims, and overclaims. Novelty commentary is out of scope.

---

## Summary

The case study argues that Feynman’s verification stack is stronger than its evaluation stack: the bundled verifier catches planted claim-level defects, while the official `/lit` eval measures citation metadata and liveness rather than claim support. The strongest evidence is the `--rescore` blindspot probe: a synthetic `q01` output with a deliberately false claim and a real, resolving Snell et al. citation scores 100% on `done`, `valid`, `title`, and `recall`. That result is reproduced in `probes/eval-scorer-blindspot/row.jsonl`, and the scorer code confirms the metric definitions that make it possible.

The case study’s audit of the committed eval results is also largely accurate: the arithmetic (22 rows, 18 completed, 137,664,710 tokens, 20,591 wall seconds, `cost_usd = 0`) matches `official-eval/summary.md`; the published `npm test`/`architecture:check` failures are real; and the telemetry error-path leak reproduces against both 0.5.65 and 0.5.69. But four claims presented as verified need correction: the “24/24” provenance overstates what `aggregate.py` computes, the researcher probe’s adjacent citations are not all correctly attributed, the official-eval “ceiling effect” analysis ignores the `title_mismatch` flags that are actually present, and the telemetry code-path sentence names a function that is not on the `feynman_tool_used` path. None of these is fatal to the central thesis; all are fixable from the artifacts already in the repository.

---

## Strengths

- **[S1] The blindspot probe is the right experiment and it is reproducible.** `probes/eval-scorer-blindspot/work/ws/outputs/test-time-compute.md` contains a false “40 percentage points on MATH” claim attributed to Snell et al., arXiv:2408.03314; `row.jsonl` records `completed:true`, `citations:1`, `citations_checked:1`, `citation_validity:1`, `title_match:1`, `key_recall:1`. `run.mjs` shows why: `scoreCitations()` checks identifier resolution, title-token overlap on the line, and `keyRecall()` checks identifier/title presence — nothing checks claim support. The case study’s central §4 claim is therefore directly evidenced, not asserted.
- **[S2] The verifier fixtures are well designed and the raw outputs substantively support the counts.** The rubric (`fixtures/rubric.md`) defines seven easy defects (F1–F7), five hard meaning-level defects (H1–H5), three true claims per easy/hard fixture, and three clean numeric claims (C1–C3). Reading `runs/verifier-flawed-a.md`, `verifier-flawed-b.md`, `verifier-hard-a.md`, and `verifier-hard-b.md`, each of the 24 defects is removed or corrected, and each of the 12 true claims survives. The hard fixture is the informative one: all sources are real, and the defects are number/attribution/meaning errors rather than dead links.
- **[S3] The official-eval audit is grounded in the actual scorer and committed rows.** Per-row checks confirm the summary table: 22 rows, 18 completed, 4 incomplete; token sum 137,664,710; wall sum 20,591; every `cost_usd` is 0; every completed row has `citation_validity = 1`, `key_recall = 1`; `title_match` ranges from 0.923 (sonnet `q01`) to 1.0. The “4 of 12 questions” coverage claim is correct.
- **[S4] The published-package finding is reproduced exactly.** `/opt/feynman/feynman-0.5.65-linux-arm64/app` has no `tests/` directory and no `scripts/check-architecture.mjs`; `package.json` keeps both scripts but its `files` list excludes those paths. Re-running `npm test` in the installed package gives `tests 0`, exit 0; `npm run architecture:check` gives `MODULE_NOT_FOUND`, exit 1. The “false green” reading is fair.
- **[S5] The telemetry leak is real and was tested against the real module.** `probes/telemetry-error-leak-0565.mts` imports `registerResearchTelemetry` from the installed 0.5.65 package, emits a failing `fetch_content` tool event whose text contains `PATIENT_ZERO_SECRET`, and the captured `feynman_tool_used.properties.error_message` contains the secret verbatim (`logs/telemetry-leak-0565.json`). The 0.5.69 source run reproduces it (`telemetry-leak-0569.json`). The README’s absolute sentence and the code’s error-text behavior do conflict.
- **[S6] The case study is candid about its limits.** It states that the official eval was summarized from committed files, not rerun; that the verifier probes are n=2 per fixture on one model; that the fixtures use clean research notes; and that no adversarial source page or cross-model comparison was run. That transparency is a genuine strength.

---

## Weaknesses

### MAJOR

**[W1] MAJOR — The “24/24” and “12/12” headline is a manual annotation, not independently checked; the stated provenance is wrong.**
The case study says: “Source: `scores.md`, generated by `aggregate.py` from `scores.json` and the raw outputs in `runs/`.” `aggregate.py` only does `json.loads((ROOT / "scores.json").read_text())` and counts `len(run["defects_detected"])` / `len(run["true_claims_preserved"])`; it never opens `runs/*.md`. `verify_claims.py` likewise only sums the same array lengths. The `artifact` fields in `scores.json` are pointers, not evidence that a script checked each detection. I read all four verifier outputs and the 24 detections do hold up, so the numbers are substantively correct — but the audit trail is a hand-authored `scores.json`, not a derivation from the raw outputs, and nothing in the repository records whether the scoring was independently checked. That distinction matters for a case study whose thesis is that “verified” statements must show the check.

**[W2] MAJOR — “Three real adjacent papers … with correct attributions” is false for THOR-MoE.**
`runs/researcher-fake-paper.md` lists: “**THOR-MoE** — *‘Beyond Token-Level Routing: Task-Guided and Context-Aware Routing in Sparse MoE for Neural Machine Translation,’* arXiv:2505.14173 (May 2025) [8].” The arXiv ID resolves, but its actual title is “THOR-MoE: Hierarchical Task-Guided and Context-Responsive Routing for Neural Machine Translation” (Liang, Meng, Paper P; verified via the arXiv API and the abstract page). The researcher gave a plausible-looking but wrong title for a real ID — exactly the title/ID mismatch the verifier prompt says to flag. The primary integrity result (refusing the nonexistent `2401.99999`) still stands, and the Lingual-SMoE and Elbayad citations do check out, but the case study’s “correct attributions” claim and its “strong integrity result” sentence need a caveat. This is also an unforced error: the researcher supplied the URL, so one fetch would have caught it.

**[W3] MAJOR — The “ceiling effect” analysis ignores the `title_mismatch` rows, and the sentence “the metrics that vary are completion and recall” is false.**
The committed rows contain actual title-association flags:
- `2026-09-23-...sonnet-5.jsonl` `q01`: `title_match = 0.9230769` (24/26), with `title_mismatch` for `arxiv:2609.19671` (“When2Think…”, overlap 0.4) and `arxiv:2608.27964` (“AERA…”, overlap 0.44). These look like the README’s documented “short-name citations also miss” caveat, but the case study does not say so.
- `2026-09-24-...claude-opus-5-5.jsonl` `q10`: `title_match = 0.9302326` (40/43), with `title_mismatch` for `doi:10.1016/j.jeconom.2020.12.001` (“Difference-in-Differences with multiple time periods”, overlap **0**), `doi:10.1093/ectj/utac017` (overlap 0.13), and `doi:10.1111/ajps.12723` (overlap 0). The first is the question’s expected key paper (Callaway & Sant’Anna).

The case study reports “title is 92–100%” but never reads the `title_mismatch` list, then concludes “the metrics that vary are completion and recall” and “there is little headroom to detect a citation-quality regression.” `title` is precisely the metric that varies, and it contains the only concrete citation-association flags in the committed set. Some may be line-context artifacts; the `q10` key-paper flag with zero title and zero first-author overlap is worth explaining rather than omitting.

**[W4] MAJOR — The telemetry code-path sentence names a function that is not on the `feynman_tool_used` path.**
The case study says: “the code path is the real one: `toolErrorText()` takes the tool result’s text and `normalizeTelemetryValue(..., raw=true)` sends it after home-directory redaction.” In the research extension (`extensions/research-tools/telemetry.ts`), `feynman_tool_used` is captured as `capture("feynman_tool_used", { tool, is_error, subagent, ...(event.isError ? { error_message: toolErrorText(event.result) } : {}) })`, and `capture()` calls `shared.client.capture(...)` directly. `normalizeTelemetryValue(..., raw=true)` lives in `src/telemetry/posthog.ts` and is used by `normalizeTelemetryProperties()` for CLI telemetry events; `RAW_TEXT_KEYS` there includes `error_message`, but that is a different module and a different event path. The leak conclusion is unaffected — the probe imports the real extension and the JSON shows the secret — but the asserted mechanism is a conflation of the CLI and research-extension telemetry paths. Fix the sentence to `toolErrorText()` → `errorText()` (home-directory redaction only) → `client.capture()`.

### MINOR

**[W5] MINOR — “The verifier and the generator are both DeepSeek V4.1 Flash” is unsupported.**
The fixtures are hand-authored by the lead (`outputs/.plans/feynman-eval-quality.md`: “Easy/hard/clean fixtures + rubric | lead | done”). The workflow receipts record only child models: verifier `openrouter/deepseek/deepseek-v4.1-flash-1017:medium`, researcher `…:high`. No artifact records the parent/generator model. If the lead is not DeepSeek, the “same model family” caveat is wrong; if it is, the case study should say where that is recorded. Remove the sentence or record the parent model.

**[W6] MINOR — “All six result files draw from the same four questions” and “every committed result uses the same four questions” are imprecise.**
`2026-09-24-lit-0.5.3-ferrylane_claude-opus-5-5.jsonl` has only `q01` and `q10`. The correct wording is: “collectively the six files cover four questions; one file covers only two.” The coverage conclusion (4 of 12) is unchanged.

**[W7] MINOR — The release-note mismatch is left unresolved when the artifacts point to a specific explanation.**
The release note says “0.5.2: 9-14 minutes, 43 of 43 citations.” The committed run labeled **0.5.0** (`2026-09-24-lit-ferrylane-openai_gpt-5.6-terra.jsonl`, SHA `d926547`) has 43 citations, 4/4 completion, and per-question walls of 711, 816, 566, 713 s = 11.85, 13.60, 9.43, 11.88 minutes — i.e. 9.4–13.6 minutes, exactly the note’s 9–14 range. That is strong evidence that either the row’s `feynman_version` is stale or the release note mislabels the version; “I could not reconcile” should be replaced by both hypotheses and a check of `package.json` at `d926547`. The finding is real; the analysis stops one step early.

**[W8] MINOR — The `--rescore` command in §4 is not the command that produced the artifact, and “never overwrites” is overbroad.**
The case study prints `node evals/run.mjs --rescore experiments/feynman-eval-quality/probes/eval-scorer-blindspot/row.jsonl`. There is no `evals/` directory at `/work`; the local scorer is `experiments/feynman-eval-quality/official-eval/run.mjs`, and `rescore-output.txt` reports an absolute output path (`/work/experiments/...`), so the actual invocation used an absolute `--rescore` path. More importantly, `run.mjs` only appends `-2` in the non-rescore branch; the `opt.rescore` branch sets `outBase = opt.rescore.replace(/\.jsonl$/, "")` and rewrites that file. “Fresh runs never overwrite a same-day result; `--rescore` rewrites the file you pass it” is accurate.

**[W9] MINOR — “Deterministic” overstates the eval.**
The scorer makes live arXiv, Crossref, and doi.org requests; `resolveArxiv()` returns `undefined` on network failure and `valid` excludes those rows; titles can change upstream. The case study itself lists “network failures are excluded” as a reproducibility weakness. Say “deterministic given the resolver responses” or “fixed scoring rules over live metadata,” not “deterministic” without qualification.

**[W10] MINOR — The cost-zero explanation is an inference, not evidence.**
“The cost is zero because the eval’s `models.json` entries have no cost block” is consistent with the README’s documented behavior, but the actual `models.json` used for these runs is not committed. The row data only shows `cost_usd = 0`. Say “consistent with the eval’s documented behavior when the provider entry has no cost block; the models.json is not committed.”

**[W11] MINOR — “Exact numbers from their abstracts” is wrong for the GPT-3 token count.**
The ~300B token figure is in the GPT-3 paper body, not the abstract; the verifier outputs themselves say “comes from the paper text as recorded in the research notes.” Change to “from the papers’ abstracts and body text.”

**[W12] MINOR — The verifier’s treatment of unplanted evaluative framing is inconsistent across runs, and the rubric does not measure it.**
`verifier-flawed-a.md` keeps “These three papers are foundational references for the modern language-model stack”; `verifier-flawed-b.md` keeps “Together, these papers supply the architecture, the pretraining objective, and the scaling result that frame this overview.” The clean run removes “These three papers define the modern language-model stack” as “an evaluative historical claim not supported by the research notes.” Same class of claim, different treatment. The rubric’s G1–G4 and the derived false-positive/reliability metrics are not reported, and only planted items are scored. Scope the conclusion “the verifier does the job the prompt describes” to the planted defects, and note the inconsistency.

**[W13] MINOR — “Ten dimensions adapted from general eval-quality work” is uncited, and two comparative claims have no baseline.**
The text never cites a source for the ten dimensions; the Sources list includes HELM (arXiv:2211.09110) and Biderman et al. (arXiv:2405.14782), but those papers do not define this exact set. Either cite the specific source per dimension or say “my own synthesis.” Similarly, “more explicitly than most agent harnesses” (§2) and “unusually eval-conscious” (executive summary) are comparative claims with no baseline; soften or drop.

**[W14] MINOR — The three live smokes are workflow-dispatch-only, not PR CI.**
`.github/workflows/e2e.yml` puts the `install-e2e` job (and its `CI_OK`, `CI_TEXT_OK`, `RESULT=PONG` steps) behind `if: github.event_name == 'workflow_dispatch'`; the PR job runs `npm test`, typecheck, build, architecture, audits, but not the live model checks. “CI has three exact-string smokes” is true of the workflow file, not of PR CI. This strengthens the case study’s point; say it precisely.

**[W15] MINOR — “Obviously malformed” mischaracterizes `2401.99999`.**
The researcher’s own §3.3 calls it “a well-formed-but-nonexistent ID” and “structurally implausible for the stated month,” not malformed. The case study’s caveat should say “out-of-range/implausible,” which is the actual weakness of the test.

**[W16] MINOR — The proposed CI gate on `done` or `recall` has little power against the failure the case study cares about.**
§11 P0 #2 says “fail on `done` or `recall` regression.” But §3.3 says every completed row has `recall = 100%` and the 0.5.3 GPT run is 4/4, so a `done`/`recall` gate is a liveness gate, not a claim-support gate. The gate should run the new claim-support eval; keep `done`/`recall` as a secondary smoke.

**[W17] MINOR — The `title` metric definition omits its denominator restriction and the README’s short-name caveat.**
§3.2 says “Share of resolved IDs whose title is at least 60% present…” but `scoreCitations()` computes `titled = rows.filter(r => r.resolves && r.overlap !== null)`, so DOI rows resolved via the handle API with no title are excluded. The README says “Among resolved IDs with a known title” and warns that “short-name citations … also miss.” Add both qualifiers; they matter for interpreting the 92%/93% rows.

**[W18] MINOR — “Catches … refusals” overstates the eval’s diagnostic power.**
A refusal shows up as `done = no` / a nonzero exit, not as a labeled refusal. The `2026-09-24-lit-0.5.3-pre-wait-...claude-opus-5-5.jsonl` `q04` row (exit 1, 12 s, 19,452 tokens, no final) is consistent with the documented Opus refusal, but the eval records no reason. Say “incomplete runs, including refusals, show as `done = no`; the eval has no refusal diagnostic.”

**[W19] MINOR — The telemetry docs already disclose error text and project file paths.**
The linked docs say: “When something fails, it sends the error message and stack trace, the end of Pi’s error output, and a failed tool’s error text… These can include file paths inside your projects.” The contradiction is narrower than the case study implies: the absolute “never sends … tool arguments” sentence is in the README (and repeated in the docs), but the docs already carve out error text and file paths. Narrow the finding to URL/query-string fragments and the README’s absolute wording; the recommended doc fix is partly already implemented.

**[W20] MINOR — The source-test command lines are not recorded in the logs.**
`logs/source-tests-workflow.log`, `source-tests-telemetry.log`, and `source-tests-architecture.log` contain pass/fail output only, not the invocation. The §7 table lists `node --test` for two files and `npx tsx --test` for the third. Add the commands to the logs (or a `commands.txt`) so a reader can reproduce the three runs.

---

## Questions for Authors

- **[Q1]** What produced the `defects_detected` / `true_claims_preserved` arrays in `scores.json`? Was the scoring blinded, and was it done by the same person who wrote the fixtures? Can you add a quote + line reference for each defect (or a checker script) so `aggregate.py` derives the counts from the outputs rather than from a hand-authored JSON?
- **[Q2]** Can you reconcile the 0.5.2/43-citation release note by checking `package.json` at SHA `d926547`? The 0.5.0-labeled run’s per-question walls match the note’s 9–14 minutes exactly. Is the `feynman_version` field stale, or is the note’s label wrong?
- **[Q3]** Did you inspect the `title_mismatch` entries for sonnet `q01` (two short-name citations) and opus `q10` (three DOIs, including the Callaway & Sant’Anna key paper with overlap 0)? Are they line-context artifacts, or is the `q10` key-paper citation genuinely detached from its title?
- **[Q4]** What model authored the fixtures and orchestrated the probe? The case study says “the verifier and the generator are both DeepSeek V4.1 Flash,” but the receipts record only child models.
- **[Q5]** What exact command produced `probes/eval-scorer-blindspot/rescore-output.txt`? Why does the printed command use `evals/run.mjs`, which does not exist in the workspace?
- **[Q6]** Should the researcher probe be re-scored now that THOR-MoE’s title is known to be wrong? Does “correct attributions” survive, or does the probe become an example of a title/ID mismatch alongside the correct refusal?
- **[Q7]** Is “deterministic” meant as “deterministic given the resolver responses”? If so, say that; if not, how do you reconcile it with the network-failure exclusion in the reproducibility rating?
- **[Q8]** Given the ceiling effect, what would a `done`/`recall` CI gate actually catch that the new claim-support eval would not?

---

## Verdict

**No FATAL findings.** The central thesis — strong component-level verification, narrow system-level evaluation — survives every check I ran. The blindspot probe is the best part of the case study and is fully reproduced; the committed-eval arithmetic and the packaging/telemetry findings are real. But the case study is not yet a clean evidence audit: **W1** overstates how the 24/24 was derived, **W2** endorses a wrong adjacent-paper title, **W3** ignores the only concrete citation-association flags in the committed data, and **W4** misdescribes the telemetry code path. Those four should be fixed before the case study is cited as an evidence-backed claim; the remaining findings are precision and reproducibility issues.

**Confidence:** high (0.85) in the core thesis and the reproduced probes; medium-high (0.75) in the specific 24/24 counts (correct on inspection, but manually scored); medium (0.7) in the release-note provenance and the “generator” identity, because the necessary artifacts are not committed.

**Revision priority:** W1–W4 first, then W6–W9; the rest are polish. Do not change the central argument; tighten the evidence claims around it.

---

## Revision Plan

**P0 — correct claims that are presented as verified**
1. **W1:** Replace “generated by `aggregate.py` from `scores.json` and the raw outputs” with the actual chain. Add per-defect evidence (quote + line) to `scores.json`, or write a checker that greps each output for the expected correction/removal. Disclose that the current scoring is manual and not independently checked. Re-run `verify_claims.py` after the change.
2. **W2:** Change “three real adjacent papers … with correct attributions” to “two of three adjacent citations verified; THOR-MoE’s ID resolves but the title in the researcher output is wrong (‘THOR-MoE: Hierarchical Task-Guided and Context-Responsive Routing…’).” Add this to the §6 caveats and, if possible, re-run the researcher probe with a title check.
3. **W3:** Report the `title_mismatch` rows in §3.3. Distinguish the README-documented short-name misses (sonnet `q01`) from the zero-overlap DOI flags (opus `q10`). Replace “the metrics that vary are completion and recall” with “completion, recall, and (slightly) title; the title flags are listed in `title_mismatch` and are the only citation-association signal in the committed data.”
4. **W4:** Correct the telemetry sentence to `toolErrorText()` → `errorText()` (home redaction only) → `client.capture()`; note that `normalizeTelemetryValue(..., raw=true)` belongs to the CLI `src/telemetry/posthog.ts` path. The leak conclusion is unchanged.

**P1 — reproducibility and precision**
5. **W6/W7/W8/W9:** Fix the “same four questions” wording; add the 9.4–13.6-minute match to the release-note discussion; print the actual rescore command and qualify “never overwrites”; say “deterministic given the resolver responses.”
6. **W5:** Record the parent/generator model in the plan or receipt, or delete the “both DeepSeek” sentence.

**P2 — polish**
7. **W10–W20:** Cost-zero wording, “abstracts” wording, verifier-consistency caveat, dimension citations/comparatives, CI-smoke precision, “malformed” wording, CI-gate target, `title` denominator, refusal diagnostic, telemetry-docs nuance, and source-test command logging.

---

## Inline Annotations

> “The bundled verifier caught **24 of 24** planted defects across four runs … It preserved **12 of 12** true claims.”
**[W1] MAJOR:** Correct on inspection — I read all four outputs and every F1–F7/H1–H5 is addressed — but the 24/24 is a manual annotation in `scores.json`, not a script-derived count. The claim should say “24/24 by manual rubric scoring, not independently checked” or the repository should add a per-defect checker.

> “Aggregate: **24/24 defects detected**, **12/12 true claims preserved**, **3/3 clean numeric claims preserved**. Source: `scores.md`, generated by `aggregate.py` from `scores.json` and the raw outputs in `runs/`.”
**[W1] MAJOR:** `aggregate.py` reads only `scores.json`; it never opens `runs/*.md`. `verify_claims.py` only re-counts array lengths. The phrase “and the raw outputs” is false. The numbers survive; the provenance sentence does not.

> “It listed three real adjacent papers (Lingual-SMoE, THOR-MoE, Elbayad et al.) with correct attributions…”
**[W2] MAJOR:** Lingual-SMoE and Elbayad check out (ICLR 2024 page and arXiv:2212.07571). THOR-MoE’s ID (arXiv:2505.14173) resolves to “THOR-MoE: Hierarchical Task-Guided and Context-Responsive Routing for Neural Machine Translation,” not the title in the researcher output. Replace “correct attributions” with the two-of-three result and add the mismatch to the caveats.

> “**Ceiling effect.** Every completed row has `valid = 100%`; `title` is 92–100%; `recall` is 100% for every completed row. The metrics that vary are completion and recall…”
**[W3] MAJOR:** The percentages are right, but the sentence ignores `title_mismatch`: sonnet `q01` has two (When2Think, AERA), opus `q10` has three (including the Callaway & Sant’Anna key paper with overlap 0). `title` is the metric that varies and the only one carrying a concrete citation-association flag. Analyze them; do not say only completion and recall vary.

> “the code path is the real one: `toolErrorText()` takes the tool result’s text and `normalizeTelemetryValue(..., raw=true)` sends it after home-directory redaction.”
**[W4] MAJOR:** `normalizeTelemetryValue` is in `src/telemetry/posthog.ts` (CLI events); the research extension’s `feynman_tool_used` handler calls `toolErrorText()` and passes `error_message` directly through `capture()`. The leak is real; the named function is not on that path. Correct the mechanism sentence.

> “**Same model family.** The verifier and the generator are both DeepSeek V4.1 Flash in this run. Shared blind spots are untested.”
**[W5] MINOR:** The fixtures are hand-authored by the lead; the receipts record only child models. No artifact identifies the parent/generator model. Remove or support this sentence.

> “all six result files draw from the same four questions”
**[W6] MINOR:** The 0.5.3 Claude Opus file contains only `q01` and `q10`. Say “collectively cover four questions; one file covers two.”

> “every committed result uses the same four questions”
**[W6] MINOR:** Same issue — the Opus 0.5.3 file is a two-question subset.

> “The release note says ‘0.5.2: 9-14 minutes, 43 of 43 citations.’ … I could not reconcile the release note with the committed files.”
**[W7] MINOR:** The 0.5.0-labeled GPT run’s per-question walls are 9.4–13.6 minutes with 43 citations and 4/4 completion — an exact match to the note. The likely explanation is a stale `feynman_version` field or a mislabeled note. State both and check `package.json` at `d926547`.

> “node evals/run.mjs --rescore experiments/feynman-eval-quality/probes/eval-scorer-blindspot/row.jsonl”
**[W8] MINOR:** There is no `evals/` directory at `/work`; the local scorer is `experiments/feynman-eval-quality/official-eval/run.mjs`, and the output reports an absolute path. Print the actual command.

> “It supports `--rescore` … and it never overwrites a same-day result.”
**[W8] MINOR:** True for fresh runs, false for `--rescore`: `outBase = opt.rescore.replace(/\.jsonl$/, "")` rewrites the input file. Qualify.

> “The official eval is real, deterministic, and committed”
**[W9] MINOR:** The scorer makes live arXiv/Crossref/doi.org calls and excludes network failures from `valid`. “Deterministic given the resolver responses” is the defensible claim.

> “The cost is zero because the eval’s `models.json` entries have no cost block”
**[W10] MINOR:** The committed rows show `cost_usd = 0`; the `models.json` is not committed. This is an inference from the README, not an observed cause.

> “The fixtures use three real papers with exact numbers from their abstracts”
**[W11] MINOR:** The GPT-3 ~300B token count is from the paper body, not the abstract; the verifier outputs say so explicitly.

> “The result is still meaningful: on objective, checkable defects, the verifier does the job the prompt describes.”
**[W12] MINOR:** Scope this to the planted defects. The easy runs keep unplanted evaluative framing (“foundational references”, “frame this overview”) that the clean run removes in an analogous sentence; the rubric does not score that class, so “does the job the prompt describes” is broader than the evidence.

> “I use ten dimensions adapted from general eval-quality work…”
**[W13] MINOR:** No citation is attached; HELM and Biderman et al. are listed but do not define this exact ten-dimension set. Cite per dimension or call it a synthesis. “More explicitly than most agent harnesses” and “unusually eval-conscious” also lack a baseline.

> “CI has three exact-string smokes”
**[W14] MINOR:** The three live smokes are in the `install-e2e` job, gated on `workflow_dispatch`; PR CI runs the unit/type/build/architecture jobs but not the smokes. Say “the manual-dispatch e2e job has three exact-string smokes.”

> “The caveat is that the fake ID was obviously malformed (`2401.99999`).”
**[W15] MINOR:** The researcher calls it “well-formed-but-nonexistent” and “structurally implausible for the stated month.” Use “out-of-range/implausible,” not “malformed.”

> “Put a small eval subset in CI. Run `q01,q04,q07,q10` … and fail on `done` or `recall` regression.”
**[W16] MINOR:** The committed 0.5.3 GPT run is 4/4 with 100% recall, and §3.3 says there is little headroom. A `done`/`recall` gate is a liveness check; the quality gate belongs on the new claim-support eval.

> “| `title` | Share of resolved IDs whose title is at least 60% present (by word tokens) on a line carrying the ID, or whose first author surname is on that line.”
**[W17] MINOR:** Add “among resolved IDs with a known title” (DOI handle-only rows are excluded from the denominator) and the README’s short-name caveat.

> “catches real failures: missing provenance, dead identifiers, wrong-paper titles, missed key papers, timeouts, and refusals.”
**[W18] MINOR:** The eval records `done = no` / exit code for refusals; it has no refusal diagnostic. The q04 Opus row (exit 1, 12 s, 19,452 tokens) is consistent with the documented refusal, but the eval does not label it.

> “If not, the docs should say ‘error messages may include fragments of tool inputs.’”
**[W19] MINOR:** The linked docs already say failed-tool error text is sent and “can include file paths inside your projects.” Narrow the recommendation to URL/query-string fragments and the README’s absolute “never sends … tool arguments” sentence.

---

## Sources

### Local artifacts inspected

- `outputs/feynman-eval-quality-case-study.md` — the reviewed artifact (not edited).
- `experiments/feynman-eval-quality/official-eval/README.md`, `run.mjs`, `questions.jsonl`, `summary.md`, `results/*.jsonl` — official eval and committed rows.
- `experiments/feynman-eval-quality/scores.json`, `scores.md`, `aggregate.py`, `verify_claims.py` — probe scoring and claim checker.
- `experiments/feynman-eval-quality/runs/verifier-flawed-a.md`, `verifier-flawed-b.md`, `verifier-hard-a.md`, `verifier-hard-b.md`, `verifier-clean.md`, `researcher-fake-paper.md` — raw agent outputs.
- `experiments/feynman-eval-quality/fixtures/flawed-draft.md`, `hard-draft.md`, `clean-draft.md`, `rubric.md`, `research-notes.md` — fixtures.
- `experiments/feynman-eval-quality/logs/published-selfchecks.txt`, `source-tests-*.log`, `telemetry-leak-0565.json`, `telemetry-leak-0569.json`, `workflow-receipt-*.json`, `verify-claims.txt` — logs and receipts.
- `experiments/feynman-eval-quality/probes/eval-scorer-blindspot/row.jsonl`, `rescore-output.txt`, `work/ws/outputs/test-time-compute.md`, `test-time-compute.provenance.md`; `probes/telemetry-error-leak-0565.mts`, `telemetry-error-leak.mts` — probes.
- `outputs/.plans/feynman-eval-quality.md`, `outputs/feynman-eval-quality-case-study.provenance.md` — plan and provenance.

### External sources additionally inspected

- Companion-Inc/feynman repository, HEAD `1174429` — https://github.com/Companion-Inc/feynman
- Release notes (the “0.5.2: 9-14 minutes, 43 of 43 citations” line) — https://github.com/Companion-Inc/feynman/blob/main/RELEASES.md
- README (telemetry sentence) — https://github.com/Companion-Inc/feynman/blob/main/README.md
- Eval runner — https://github.com/Companion-Inc/feynman/blob/main/evals/run.mjs
- Eval README — https://github.com/Companion-Inc/feynman/blob/main/evals/README.md
- Package manifest (`files`, `test`, `architecture:check`) — https://github.com/Companion-Inc/feynman/blob/main/package.json
- CI workflow (live smokes are `workflow_dispatch`-only) — https://github.com/Companion-Inc/feynman/blob/main/.github/workflows/e2e.yml
- Research telemetry extension — https://github.com/Companion-Inc/feynman/blob/main/extensions/research-tools/telemetry.ts
- CLI telemetry module (`normalizeTelemetryValue`, `RAW_TEXT_KEYS`) — https://github.com/Companion-Inc/feynman/blob/main/src/telemetry/posthog.ts
- Verifier prompt — https://github.com/Companion-Inc/feynman/blob/main/.feynman/agents/verifier.md
- Researcher prompt — https://github.com/Companion-Inc/feynman/blob/main/.feynman/agents/researcher.md
- Reviewer prompt — https://github.com/Companion-Inc/feynman/blob/main/.feynman/agents/reviewer.md
- `/lit` workflow — https://github.com/Companion-Inc/feynman/blob/main/prompts/lit.md
- Snell et al., arXiv:2408.03314 (abstract: “problems where a smaller base model attains somewhat non-trivial success rates … outperform a 14x larger model”; no 40-point MATH claim) — https://arxiv.org/abs/2408.03314
- THOR-MoE, arXiv:2505.14173 (actual title: “THOR-MoE: Hierarchical Task-Guided and Context-Responsive Routing for Neural Machine Translation”) — https://arxiv.org/abs/2505.14173
- Lingual-SMoE, ICLR 2024 (Zhao, Chen, Cheng, Chen; “>5% BLEU on OPUS-100”) — https://proceedings.iclr.cc/paper_files/paper/2024/hash/3b4e1336f775c3dba16ebbb8d2afd258-Abstract-Conference.html
- Elbayad, Sun, Bhosale, arXiv:2212.07571 — https://arxiv.org/abs/2212.07571
- OpenAlex records for the three foundational papers (W2626778328, W2896457183, W2963341956, W3030163527) — https://api.openalex.org/works/W2896457183 (and sibling IDs)
- Telemetry docs (discloses failed-tool error text and project file paths) — https://feynman.is/docs/getting-started/configuration
