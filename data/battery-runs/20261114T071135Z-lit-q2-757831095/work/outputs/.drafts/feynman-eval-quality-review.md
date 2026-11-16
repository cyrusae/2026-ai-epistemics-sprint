# Adversarial review: `feynman-eval-quality-draft.md`

**Reviewed artifact:** `/work/outputs/.drafts/feynman-eval-quality-draft.md` (31,807 bytes)
**Review date:** 2026-11-14
**Review mode:** evidence-quality audit; the draft was not edited.
**Evidence inspected:** installed Feynman 0.5.65 tree at `/opt/feynman/feynman-0.5.65-linux-arm64/app`; repo `main` at commit `1174429075`; `evals/README.md`, `evals/run.mjs`, `evals/questions.jsonl`, all six published result sets; probe artifacts under `/work/experiments/eval-quality-probes` and `/work/eval-run`; subagent `*_meta.json` and transcripts under `/state/.feynman/sessions`; npm registry; arXiv 2410.18164.

## Summary

The draft is a case study of whether Feynman’s *stated* evidence discipline is *machine-enforced*. Its strongest move is to separate prompt-level policy from runtime acceptance: the four Feynman agents omit `acceptanceRole`, the pilot’s ungated children resolve to `attested` with empty `verifyRuns`, and the one explicit typed gate resolves to `verified` with a recorded host command. That distinction is well supported by the installed agent frontmatter, the acceptance ledgers, and the pi-subagents documentation, and it is the draft’s most durable contribution.

The draft is also unusually candid about its own failures: the pilot’s verifier read `ground_truth.json`, two later waves had leakage channels, and the deterministic checker needed several revisions. That transparency is a strength and should be preserved. The problems are that two headline evidence claims do not survive checking: the official eval’s “real regression finding” is contradicted by the published result metadata, and the probe 7/7 is a heavily scaffolded, in-sample result presented too close to a property of the harness. Several smaller quantitative and code/config claims also need correction.

## Strengths

- **[S1] The stated-vs-enforced thesis is directly evidenced.** `researcher.md`, `verifier.md`, `reviewer.md`, and `writer.md` contain no `acceptanceRole`; the pilot `*_meta.json` files show `status: "attested"`, `verifyRuns: []`, and `inferredReason: ["default lightweight attestation"]`; p8’s ledger records `status: "verified"` with a host `gate` command and structured stdout. The pi-subagents docs state that “Child-reported command success does not count” toward `verified`. This is a clean, artifact-backed finding.
- **[S2] The p8 gate demo is documented at the artifact level.** The p8 meta records `verifyRuns: [{ id: "gate", exitCode: 0, stdout: "{\"verdict\": \"ok\", \"expected\": 133, \"got\": 133}", structuredOutput: ... }]`. The draft’s description of the mechanism is accurate, even though its framing of “correctness established by the harness” is not (see W5).
- **[S3] The draft reports its own contamination and checker defects.** §6.2–§6.3 explicitly record the pilot’s answer-key citation, wave 2’s pilot-directory exposure, and four checker revisions. This is the right behavior for an evidence audit and is materially better than a clean-looking scorecard.
- **[S4] The wave-3 artifact hygiene is reproducible.** All seven answer-file SHA-256 prefixes and byte counts in §11 match `experiments/eval-quality-probes/wave3-runs/`; the ground-truth hash `190c93f9e17bf31e` matches; recomputation gives 66 rows / 17,616.39, B mean 260.16 over 141 rows, and C count 133. I reproduced these values independently.
- **[S5] The official-eval table is mostly transcribed correctly.** The sonnet, gpt-5.6, and opus counts, token totals, title-match values, and recall values match the published `.md`/`.jsonl` files, with the important exception of the pre-wait version labels (W2) and the non-uniform question count (W6d).
- **[S6] The n=1 / single-model caveat is explicit.** §2 (“Not claimed: … statistical stability (n=1 per probe)”), §6.4 (“n=1 per probe”), and §10 (“single harness version … single model … one run per probe”) are appropriately cautious. The remaining overinterpretation is not the sample size per se; it is the experimental demand characteristics and post-hoc scoring rules (W1).

## Weaknesses

### [W1] **MAJOR:** The 7/7 behavioral result is overinterpreted because the probe prompts are leading and the scorer was revised on the same seven outputs.

> “Given short, unambiguous, locally checkable tasks, the harness follows its own evidence rules well, including the hardest one: refusing to assert a value for a missing file (p5) and refusing to invent a paper (p2).” — §6.4

> “**Wave 3 score: 7/7** under the final rule set” — §6.4

The draft acknowledges n=1 and a single model, which is good. Those are not the main problem. The main problem is that the probe tasks *tell the model the desired behavior*:

- p2: “Never guess a DOI, arXiv ID, or URL.”
- p3: “Check the claim against the CSV.”
- p5: “Do not invent a value for a missing part.”
- p6: “keep it only if a local source supports it … remove or explicitly flag numbers with no source.”
- p7: “Inspect this workspace for supporting artifacts.”

These are demand characteristics: a 7/7 under these instructions demonstrates instruction following under a verification checklist, not spontaneous evidence discipline. The draft’s “short, unambiguous” framing does not say “leading.”

The second problem is in-sample rule selection. The same wave-3 answers score **5/7 under checker v2/v3, 6/7 under v4, and 7/7 under `check_probes_final.py`**. The final rule set was chosen after reading the seven answers; the draft says so (“The scorer needed four revisions”) but still reports the last point as “the” score. That is not an out-of-sample estimate. The draft should report the score trajectory and either (a) pre-register the final rules on a fresh probe set, (b) report a held-out/no-hint control, or (c) label 7/7 as “in-sample, under leading prompts.” The n=1/single-model caveat does not cover this.

### [W2] **FATAL:** The official eval’s “real regression finding” is contradicted by the published result metadata.

> “The 0.5.3 pre-wait → final comparison is a real regression finding: adding the `bg_wait` rule to `SYSTEM.md` raised completion from 75% to 100% on the same four questions and model. This is exactly the kind of harness-level effect an eval should catch.” — §5.2

> “| 2026-09-24 gpt-5.6-terra (0.5.3 pre-wait) | same 4 | 75% | 100% | 100% | 75% | 14,073,816 |” — §5.1

The rows themselves say otherwise. In `2026-09-24-lit-0.5.3-pre-wait-ferrylane-openai_gpt-5.6-terra.jsonl`, every row has `"feynman_version": "0.5.2"`, `"git_sha": "7c5fc51"`, and `"git_dirty": true`. The final row has `"feynman_version": "0.5.3"`, `"git_sha": "c1e0b29"`, and `"git_dirty": true`. The pre-wait `.md` itself says “Trimmed 0.5.3 prompts, before the `bg_wait` rule was added,” but the recorded version is 0.5.2.

The recorded commits do not isolate the claimed change. `7c5fc51...c1e0b29` contains two commits (“Cut duplicated and dead instructions from the system and workflow prompts” and “Send CLI telemetry through posthog-node only”) and touches all 11 prompt files, `SYSTEM.md`, `src/telemetry/posthog.ts`, and tests. The diff contains no `bg_wait` string. `bg_wait` appears in current `main` at `1174429075` (`SYSTEM.md` line 21), but not in the recorded final commit `c1e0b29`. Because both runs are `git_dirty: true`, the actual prompt state is not recoverable from the recorded SHAs; the `bg_wait` rule could have been uncommitted, but so could other changes.

This is not a controlled regression finding. It is a 0.5.2-dirty → 0.5.3-dirty before/after with several simultaneous prompt and telemetry changes, one question’s completion flipping. The draft’s own §5.2 says the suite “Treats single runs as noisy”; §10’s open question says the pre-wait/final comparison is “one run per arm.” Calling it “real” contradicts both. Fix: relabel the rows as recorded (`0.5.2` pre-wait, `0.5.3` final, both dirty), add `git_sha`/`git_dirty` columns, retrieve the worktree diff if it exists, and either show `bg_wait` was the only relevant change or downgrade the claim to “suggestive, not controlled.”

### [W3] **MAJOR:** “Provenance is required for 4 of 11 workflows” is wrong; `draft.md` does not require a sidecar.

> “**Provenance is required for 4 of 11 workflows** (`deepresearch`, `lit`, `draft`, `recipe`); the other 7 have no sidecar requirement.” — §1, point 4

> “| `draft.md` | yes |” — §4.5 table

`AGENTS.md` line 95 says: “Every output from `/deepresearch` and `/lit` must include a `.provenance.md` sidecar.” `recipe.md` explicitly writes `outputs/<slug>-recipe.provenance.md` (lines 16 and 27). `deepresearch.md` and `lit.md` explicitly write sidecars. `draft.md` says only: “Follow the system prompt’s provenance rules for all results, figures, charts, images, tables, benchmarks, and quantitative comparisons” (line 16) and “Every figure or table needs provenance” (line 17); it does **not** require an `outputs/<slug>.provenance.md` sidecar. It saves “exactly one draft to `papers/<slug>.md`” (line 19).

So the prompt-level sidecar set is 3 (`deepresearch`, `lit`, `recipe`), not 4; the `AGENTS.md` set is 2. The scorecard’s “7/11 prompts lack sidecars” should be 8/11 (or 9/11 on the `AGENTS.md` reading), not 7/11. The verification log’s method — “grep for ‘provenance’ | 4 of 11 prompts” — conflates a mention of provenance with a sidecar requirement. The substantive point about `/audit` and `/autoresearch` stands; the number does not.

### [W4] **MAJOR:** Telemetry is not “metadata-only by construction”; it sends error messages and stack traces.

> “Telemetry is metadata-only by construction: tool name, error flag, model, tokens, cache counts, latency, HTTP status. The code comment and README both state no prompts, outputs, paper text, or tool arguments are sent.” — §4.4

The second sentence is true as far as it goes, but the first is false. `extensions/research-tools/telemetry.ts` sends, on a tool error:

```ts
...(event.isError ? { error_message: toolErrorText(event.result) } : {}),
```

and on a model error:

```ts
$ai_error: message.stopReason === "error" ? errorText(message.errorMessage) : undefined,
```

`errorText` can include arbitrary text, and the README itself says: “Feynman sends anonymous usage data to PostHog: commands, workflows, tools, models, token counts, and errors with their messages and stack traces (your home folder shown as `~`).” That is not a bare “error flag.” The no-prompts/no-outputs/no-tool-arguments claim remains true, but “metadata-only by construction” overstates the guarantee. Rewrite as: “The code sends no prompts, outputs, paper text, or tool arguments; it does send error messages and stack traces, which the README documents.”

### [W5] **MAJOR:** The p8 framing says correctness was established by the harness “rather than … my external checker,” but the gate command is the author’s external checker.

> “This is the only run in the study whose correctness was established by the harness itself rather than by prose or my external checker.” — §6.5

The p8 acceptance ledger records:

```json
"verify": [{
  "id": "gate",
  "command": "python3 experiments/eval-quality-probes/check_gate.py experiments/eval-quality-probes/runs/p8/answer.md",
  "output": "json"
}]
```

`check_gate.py` is the author’s script; it reads `ground_truth.json` and compares the parsed count. The harness mechanically **executed** the author’s check and recorded that it passed. That is valuable — it converts an attestation into a host-run event — but it is not independent correctness established by the harness. The honest formulation is: “The harness enforced an author-supplied gate and recorded its pass/fail; the gate’s validity is still the author’s responsibility.” This distinction matters for recommendation 1, which says “a single command per claim converts `attested` into `verified`”; a gate only verifies that the command passed, not that the command is a valid check.

### [W6] **MAJOR:** The official-eval assessment misses several blind spots that matter more than the ones it lists.

> “Its published results use 4 questions per run, one run per configuration, and citation validity is 100% in every completed row — a ceiling that leaves no headroom for citation precision.” — §1, point 5

> “Citation validity 100% in every completed row | Ceiling effect: the metric cannot distinguish good from excellent, and cannot detect a wrong claim attached to a real paper” — §5.3

The draft’s listed limitations (4 questions, one run, no negative controls, no false premises, no claim-level correctness, completion ≠ correctness) are real. It misses five:

1. **Filtered denominator for citation validity.** `run.mjs` lines 183–189 compute `const checked = rows.filter((r) => r.resolves !== undefined)` and then `citation_validity = checked.filter((r) => r.resolves).length / checked.length`. Network-failed lookups (`resolves === undefined`) are silently removed from the denominator. The README says “Lookups that fail on the network are left out,” and the pre-wait `.md` says “q01 citation validity was re-scored after a transient lookup failure.” The 100% ceiling is therefore conditional on successful lookups and at least one manual re-score, not a purely deterministic measurement.
2. **All published runs are `/lit`.** Every row in all six result sets has `"workflow": "lit"`. The suite’s README advertises `--workflow deepresearch`, but there is no published `/deepresearch` result. The flagship verifier→reviewer pipeline is unmeasured by the project’s own eval.
3. **Dirty worktrees.** The pre-wait and final rows are `git_dirty: true`; `git_sha` does not pin the prompt state. The draft’s scorecard says “version capture are good,” but the published evidence is from dirty trees. This is the same issue as W2, generalized.
4. **Non-uniform question sets.** The opus final run has only `q01,q10` (2 questions), not 4; the draft’s table says “4 questions per run.” The run is 100% on 2/2, not comparable to the 4-question sonnet/gpt runs. The draft says “Not claimed: model ranking,” which helps, but the table still invites the comparison.
5. **`done` selects the largest output with a sidecar.** `run.mjs` lines 87–93 sort matching `outputs/*.md` by size descending and take the first. A workflow that writes multiple sidecar-backed outputs can satisfy `done` with a large artifact that is not the canonical final. This is another way “completion ≠ correctness” can fail.

Add these to §5.3. The first two are the most important: they directly affect the headline 100% and the suite’s coverage claim.

### [W7] **MAJOR:** “Pre-registered … rules” contradicts the draft’s own checker-revision narrative.

> “Mitigations: pre-registered fixtures and rules, external checker, on-disk artifacts, explicit reporting of the pilot’s contamination and the checker’s own defects.” — §10

> “This is itself an eval-quality result. The scorer needed four revisions” — §6.2

The fixtures were generated once with a fixed seed and the ground truth was computed before the runs; that part is pre-registered. The **scoring rules** were not. The draft says the scorer needed four revisions, and the same wave-3 answers score 5/7 (v2/v3), 6/7 (v4), 7/7 (final). A rule set selected after seeing the outputs cannot be described as pre-registered. Change to: “pre-registered fixtures and ground truth; scoring rules were revised post hoc, and all revisions are reported,” and add the per-revision scores.

### [W8] **MINOR:** “`acceptance` / `gate` appear zero times” is false as written.

> “`acceptance` / `gate` appear zero times in the 11 workflow prompts and 4 agent definitions, even though pi-subagents supports host-run verification commands and typed JSON gates.” — §1, point 2

`reviewer.md` contains “do not predict venue acceptance” (line 31) and “Do not predict venue acceptance” (line 57). The verification log’s narrower wording — “0 `acceptance`/`gate`/`acceptanceRole` settings” — is accurate. The substantive point (no acceptance configuration) stands; the summary sentence should say “no `acceptance`/`gate` configuration fields,” not “zero times.”

### [W9] **MINOR:** The 12-question composition is mischaracterized.

> “12 fixed questions: 6 ML paper-discovery queries, 3 verbatim LitQA2 items (CC-BY-SA-4.0), 3 hand-authored non-ML topics.” — §5

`questions.jsonl` shows q01–q06 as the six paper-discovery queries, but q04 is `"field": "genome editing"` (“CRISPR base editing”), not ML. And q11 is `"field": "earth science"` with the question “machine-learning medium-range global weather forecasting,” which is an ML application; the README calls q10–q12 “outside ML and biology (econometrics, weather forecasting, cosmology),” but the draft’s “non-ML” label is still inaccurate. The accurate description is “five ML/interpretability queries plus one genome-editing query; three LitQA2 biology items; three hand-authored topics, one of which is ML weather forecasting.” This does not change the “narrow” conclusion, but it should be correct.

### [W10] **MINOR:** The pilot table says “7 runs” for the ungated researcher condition; the pilot had 6.

> “| Researcher probe, no explicit gate (7 runs) | `attested` | 0 | …” — §4.2

The pilot had 6 ungated researcher children (p1, p2, p3, p4, p5, p7), 1 gated researcher (p8, `verified`), and 1 verifier (p6, `attested`). That is why the executive summary’s “7 of 8 children were attested” is correct. The table’s “7 runs” double-counts the verifier or the gated child. Change to “6 ungated researcher runs + 1 verifier.”

### [W11] **MINOR:** “85 tool calls … 0.79 MB” is stale or unverifiable.

> “At final inspection the probe session held 85 tool calls with arguments in 0.79 MB.” — §4.4

The only parent session JSONL now contains 97 tool calls with arguments and is 0.891 MB. The draft’s number may have been true at an earlier point, but it is not tied to a named artifact or timestamp. Either record the measurement time and file hash, or remove the specific numbers and keep the qualitative point.

### [W12] **MINOR:** “Citation precision” is the wrong term, and “4 questions per run” is not uniform.

> “citation validity is 100% in every completed row — a ceiling that leaves no headroom for citation precision” — §1, point 5

The eval measures **citation validity** (does an ID resolve), not precision (does the cited source support the claim). The draft later makes exactly this distinction (“Citation validity asks ‘does this ID resolve’; claim support asks ‘does this source say this’”), so the summary should use “citation validity.” Separately, the opus final run uses 2 questions, not 4; say “4 questions for most runs; 2 for the final opus run.”

### [W13] **MINOR:** “Stronger starting point than most agent harnesses” has no baseline.

> “That is a stronger starting point than most agent harnesses.” — §1

No sample of harnesses, criteria, or comparison is given. This is a reasonable impression, but it is not an evidence claim. Soften to “stronger than the harnesses inspected here” or remove it.

### [W14] **MINOR:** “The project’s prose describes the harness as producing reproducible, evidence-backed research” is not quoted.

> “The deepest issue is construct validity: the suite measures **citation hygiene and task completion**, then the project’s prose describes the harness as producing **reproducible, evidence-backed research**. Those are not the same claim.” — §5.3

`SYSTEM.md` says “produce reproducible written artifacts” and “Evidence over fluency”; the README says “research-quality evals” and describes `/deepresearch` as “Planned investigation with parallel researchers and citation checks.” Those support the spirit of the sentence, but the exact phrase “reproducible, evidence-backed research” is the draft’s paraphrase. Quote the actual sentence you are contrasting, or soften to “the project’s framing” and cite `SYSTEM.md` line 4.

## Questions for Authors

- **Q1 (W2):** Can you produce the uncommitted worktree diff for the pre-wait and final eval runs? What exactly changed between `7c5fc51` and `c1e0b29`, and can you show that `bg_wait` was the only relevant difference? If not, will you relabel the comparison as uncontrolled?
- **Q2 (W1):** What are the wave-3 scores under checker v2, v3, v4, and final? If the final 7/7 depends on post-hoc rule changes, what is the score on a fresh, no-hint probe set or under a pre-registered rule set?
- **Q3 (W1):** Were the explicit task instructions (“Never guess a DOI,” “Do not invent a value,” “keep it only if a local source supports it”) part of the intended construct? If so, how do you distinguish instruction following from evidence discipline?
- **Q4 (W6):** Why are all six published eval runs `workflow: "lit"`? Is there any `/deepresearch` eval result? What is the citation-validity number before dropping network-failed lookups and before the q01 manual re-score?
- **Q5 (W3):** Which provenance count is authoritative: `AGENTS.md` (2 sidecar workflows), the prompt-level explicit sidecar paths (3), or the “provenance” grep (4)? Does `draft.md` require a sidecar at all?
- **Q6 (W4):** What exactly does `errorText` send on tool/model errors, and can it contain prompts, tool arguments, or paths? The README says “errors with their messages and stack traces”; is “metadata-only by construction” still accurate?
- **Q7 (W5):** Why is p8 described as “correctness established by the harness itself” when the gate command is your `check_gate.py`? What would an independent gate look like?
- **Q8 (W7):** Which scoring rules were fixed before seeing the seven answers, and which were selected after? Can you report the score trajectory as a sensitivity table?

## Verdict

The draft’s central distinction—policy-rich prompts vs. machine-enforced verification—is well supported and worth publishing as a case study, and its transparency about contamination and checker defects is exemplary. But two headline evidence claims are not safe as written: the official eval’s “real regression finding” is contradicted by the result metadata (pre-wait rows are `0.5.2`/dirty; the recorded commits do not contain `bg_wait`; the final run is dirty), and the probe 7/7 is an in-sample, heavily scaffolded result presented too close to a property of the harness. The provenance 4/11 count, the telemetry “metadata-only” claim, and the p8 “harness-established correctness” framing also need correction. Revision priority: fix or withdraw the regression claim and re-scope the 7/7 first; then correct the quantitative/config claims and add the missing eval-design blind spots (filtered citation denominator, all-`/lit` coverage, dirty worktrees, non-uniform question sets, manual re-score). With those revisions, the core thesis remains credible; without them, a skeptical reader can reasonably discount the two strongest positive examples.

## Revision Plan

1. **Fix or withdraw the 0.5.3 pre-wait/final regression claim (W2).** Add `git_sha` and `git_dirty` to the results table; label the pre-wait rows `0.5.2` as recorded; state that both arms are dirty; retrieve the worktree diff. If `bg_wait` cannot be isolated, downgrade §5.2 to “suggestive, not controlled” and remove it from “What this suite does well,” or keep it only as an example of the suite’s before/after *process*.
2. **Re-scope the 7/7 (W1).** Add a no-hint control for p2/p5/p6/p7 (ask for the result without telling the model to refuse/invent/flag). Report the per-checker-version scores (v2/v3 5/7, v4 6/7, final 7/7) in a sensitivity table. Either pre-register the final rules on a fresh probe set or label the current 7/7 “in-sample, under leading prompts.”
3. **Correct provenance coverage (W3).** Change “4 of 11 / 7 without” to “3 prompt-level sidecar workflows (`deepresearch`, `lit`, `recipe`); `AGENTS.md` names 2; 8 of 11 prompts lack a sidecar requirement.” Update the scorecard and verification log; explain that `draft.md`’s provenance language is about figures/tables, not a `.provenance.md` file.
4. **Correct telemetry wording (W4).** Replace “metadata-only by construction: tool name, error flag …” with “no prompts, outputs, paper text, or tool arguments; error messages and stack traces are sent, as the README documents.” Note the `error_message`/`$ai_error` fields.
5. **Fix the p8 framing (W5).** Say “the harness executed and recorded an author-supplied gate; it did not independently establish the gate’s validity.” Add a sentence to recommendation 1: a gate is only as good as the command it runs.
6. **Expand the official-eval blind-spot section (W6).** Add the filtered `citation_validity` denominator, the all-`/lit` published coverage, the dirty worktrees, the opus 2-question run, and the largest-output `done` selection. This is the most useful substantive addition to the draft.
7. **Fix the “pre-registered rules” claim (W7).** Say “pre-registered fixtures and ground truth; post-hoc scoring rules, with all revisions and scores reported.”
8. **Fix the minor counts and terminology (W8–W14).** “No acceptance/gate configuration fields” rather than “zero times”; correct the 12-question composition; fix “7 runs” to “6 ungated researcher runs + 1 verifier”; update or timestamp the 85-call/0.79 MB number; use “citation validity” not “citation precision”; soften “most agent harnesses”; quote the project prose or soften the paraphrase.

## Inline Annotations

> “**Provenance is required for 4 of 11 workflows** (`deepresearch`, `lit`, `draft`, `recipe`); the other 7 have no sidecar requirement.”
**[W3] MAJOR:** The count is wrong. `draft.md` requires provenance for figures/tables but never a `.provenance.md` sidecar; `AGENTS.md` line 95 names only `/deepresearch` and `/lit`; `recipe.md` explicitly writes a sidecar. Correct prompt-level count: 3 (`deepresearch`, `lit`, `recipe`). See the §4.5 table and scorecard “7/11” for the same error.

> “`acceptance` / `gate` appear zero times in the 11 workflow prompts and 4 agent definitions”
**[W8] MINOR:** `reviewer.md` contains “do not predict venue acceptance” (line 31) and “Do not predict venue acceptance” (line 57). The verification log’s “0 `acceptance`/`gate`/`acceptanceRole` settings” is the accurate claim; the summary should say “no acceptance/gate configuration fields.”

> “| Researcher probe, no explicit gate (7 runs) | `attested` | 0 | …”
**[W10] MINOR:** The pilot had 6 ungated researcher children (p1, p2, p3, p4, p5, p7), 1 gated researcher (p8), and 1 verifier (p6). The exec summary’s “7 of 8 children were attested” is correct; the table’s “7 runs” is not. Change to “6 ungated researcher runs + the verifier.”

> “At final inspection the probe session held 85 tool calls with arguments in 0.79 MB.”
**[W11] MINOR:** The only parent session JSONL now contains 97 tool calls with arguments and is 0.891 MB. The number may have been true earlier, but it is not tied to a timestamp or artifact. Either record the measurement time/file hash or remove the specific numbers.

> “Telemetry is metadata-only by construction: tool name, error flag, model, tokens, cache counts, latency, HTTP status. The code comment and README both state no prompts, outputs, paper text, or tool arguments are sent.”
**[W4] MAJOR:** `telemetry.ts` sends `error_message: toolErrorText(event.result)` on tool errors (line 226) and `$ai_error: errorText(message.errorMessage)` on model errors (line 259). The README says “errors with their messages and stack traces.” “Metadata-only by construction” is false; the no-prompts/outputs/tool-args claim is true but incomplete. See W4.

> “The 0.5.3 pre-wait → final comparison is a real regression finding: adding the `bg_wait` rule to `SYSTEM.md` raised completion from 75% to 100% on the same four questions and model. This is exactly the kind of harness-level effect an eval should catch.”
**[W2] FATAL:** The pre-wait rows are `feynman_version: 0.5.2`, `git_sha: 7c5fc51`, `git_dirty: true`; the final rows are `0.5.3`, `c1e0b29`, `git_dirty: true`. The `7c5fc51...c1e0b29` diff contains prompt trimming and telemetry changes, touches all 11 prompts, and does **not** contain `bg_wait`. `bg_wait` appears in current `main` (`1174429075`) but not in `c1e0b29`. Both runs are dirty, so the exact prompt state is not recoverable. This is a suggestive before/after, not a controlled regression finding. See W2.

> “| 2026-09-24 gpt-5.6-terra (0.5.3 pre-wait) | same 4 | 75% | 100% | 100% | 75% | 14,073,816 |”
**[W2] FATAL:** The row metadata says `feynman_version: 0.5.2`, not 0.5.3. The `.md` says “Trimmed 0.5.3 prompts,” but the JSON is authoritative for the run version. Label the row 0.5.2 and add `git_dirty: true`; same for the opus pre-wait row.

> “Its published results use 4 questions per run, one run per configuration, and citation validity is 100% in every completed row — a ceiling that leaves no headroom for citation precision.”
**[W12] MINOR:** “Citation precision” is the wrong term; the metric is citation validity/resolvability. Also, the opus final run uses 2 questions, not 4. See W6d and W12.

> “Citation validity 100% in every completed row | Ceiling effect: the metric cannot distinguish good from excellent, and cannot detect a wrong claim attached to a real paper”
**[W6] MAJOR:** The ceiling is real, but the metric’s denominator is filtered: `run.mjs` lines 183–189 drop `resolves === undefined` (network-failed lookups) before computing `citation_validity`. The README says failed lookups are “left out,” and the pre-wait `.md` says “q01 citation validity was re-scored after a transient lookup failure.” The 100% is conditional on successful lookups and a manual re-score. Add this to the limitations table.

> “The deepest issue is construct validity: the suite measures **citation hygiene and task completion**, then the project’s prose describes the harness as producing **reproducible, evidence-backed research**. Those are not the same claim.”
**[W14] MINOR:** The contrast is fair, but “reproducible, evidence-backed research” is a paraphrase. `SYSTEM.md` says “produce reproducible written artifacts” and “Evidence over fluency”; the README says “research-quality evals” and “citation checks.” Quote the actual sentence or soften to “the project’s framing.”

> “Given short, unambiguous, locally checkable tasks, the harness follows its own evidence rules well, including the hardest one: refusing to assert a value for a missing file (p5) and refusing to invent a paper (p2).”
**[W1] MAJOR:** The tasks are not merely short; they are leading. p2’s task says “Never guess a DOI, arXiv ID, or URL”; p5’s says “Do not invent a value for a missing part”; p6’s says “keep it only if a local source supports it … remove or explicitly flag numbers with no source”; p7’s says “Inspect this workspace for supporting artifacts.” The 7/7 demonstrates compliance with a verification checklist, not spontaneous evidence discipline. Add a no-hint control.

> “**Wave 3 score: 7/7** under the final rule set”
**[W1] MAJOR:** The same wave-3 answers score 5/7 under checker v2/v3, 6/7 under v4, and 7/7 under `check_probes_final.py`. The final rules were revised after reading the seven answers, so 7/7 is an in-sample endpoint, not an out-of-sample estimate. Report the trajectory and either pre-register the rules on a fresh set or label the score “in-sample, under leading prompts.”

> “This is the only run in the study whose correctness was established by the harness itself rather than by prose or my external checker.”
**[W5] MAJOR:** The p8 gate command is `python3 experiments/eval-quality-probes/check_gate.py ...` — your own checker, which reads `ground_truth.json`. The harness executed the author’s check and recorded its pass; it did not independently establish correctness. Rewrite as “the harness mechanically enforced an author-supplied gate.”

> “Mitigations: pre-registered fixtures and rules, external checker, on-disk artifacts, explicit reporting of the pilot’s contamination and the checker’s own defects.”
**[W7] MAJOR:** The fixtures and ground truth were pre-registered; the scoring rules were not. §6.2 says the scorer needed four revisions, and the score moves 5/7 → 6/7 → 7/7 across v2/v3 → v4 → final. Change to “pre-registered fixtures and ground truth; post-hoc scoring rules, with all revisions and scores reported.”

> “12 fixed questions: 6 ML paper-discovery queries, 3 verbatim LitQA2 items (CC-BY-SA-4.0), 3 hand-authored non-ML topics.”
**[W9] MINOR:** q04 is genome editing, not ML; q11 is ML weather forecasting, not non-ML. The accurate description is five ML/interpretability queries + one genome-editing query; three LitQA2 biology items; three hand-authored topics (one ML). See W9.

> “That is a stronger starting point than most agent harnesses.”
**[W13] MINOR:** No sample of harnesses, criteria, or comparison is given. Soften to “stronger than the harnesses inspected here” or remove.

## Sources

**Primary, local**

- Reviewed draft: `/work/outputs/.drafts/feynman-eval-quality-draft.md`
- Installed app: `/opt/feynman/feynman-0.5.65-linux-arm64/app`
- Agent definitions: `/opt/feynman/feynman-0.5.65-linux-arm64/app/.feynman/agents/{researcher,verifier,reviewer,writer}.md`
- `AGENTS.md` line 95; `prompts/{deepresearch,lit,draft,recipe}.md`
- Telemetry: `/opt/feynman/feynman-0.5.65-linux-arm64/app/extensions/research-tools/telemetry.ts` (lines 226, 259)
- Probe artifacts: `/work/experiments/eval-quality-probes/{scores,wave3-runs,ground_truth.json,check_probes_final.py,check_gate.py}`; `/work/eval-run/{runs,scores-v2.json,scores-v3.json}`
- Subagent ledgers/transcripts: `/state/.feynman/sessions/subagent-artifacts/*_meta.json`, `*_transcript.jsonl`; parent session `/state/.feynman/sessions/2026-11-14T07-42-01-866Z_01a1d901-948a-728b-ad1a-c359153c2a77.jsonl`

**Primary, remote**

- Repo `main` at `1174429075`: https://github.com/Companion-Inc/feynman/commit/11744290758648c2ecd7c0d6389cdca9ae580290
- Eval README: https://github.com/Companion-Inc/feynman/blob/11744290758648c2ecd7c0d6389cdca9ae580290/evals/README.md
- Eval runner: https://github.com/Companion-Inc/feynman/blob/11744290758648c2ecd7c0d6389cdca9ae580290/evals/run.mjs
- Eval questions: https://github.com/Companion-Inc/feynman/blob/11744290758648c2ecd7c0d6389cdca9ae580290/evals/questions.jsonl
- Published result sets: https://github.com/Companion-Inc/feynman/tree/11744290758648c2ecd7c0d6389cdca9ae580290/evals/results
- Final gpt-5.6-terra result: https://github.com/Companion-Inc/feynman/blob/11744290758648c2ecd7c0d6389cdca9ae580290/evals/results/2026-09-24-lit-0.5.3-ferrylane-openai_gpt-5.6-terra.md
- Pre-wait gpt-5.6-terra result: https://github.com/Companion-Inc/feynman/blob/11744290758648c2ecd7c0d6389cdca9ae580290/evals/results/2026-09-24-lit-0.5.3-pre-wait-ferrylane-openai_gpt-5.6-terra.md
- Compare `7c5fc51...c1e0b29`: https://github.com/Companion-Inc/feynman/compare/7c5fc51...c1e0b29
- Current `SYSTEM.md`: https://github.com/Companion-Inc/feynman/blob/11744290758648c2ecd7c0d6389cdca9ae580290/.feynman/SYSTEM.md
- npm registry latest: https://registry.npmjs.org/@companion-ai%2Ffeynman/latest
- TabDPT: https://arxiv.org/abs/2410.18164
