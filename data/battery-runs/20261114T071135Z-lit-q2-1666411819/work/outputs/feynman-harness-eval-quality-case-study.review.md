> **Post-review note (2026-11-14):** After this review, the report was revised to fix M1 (p-value pairing), M2 (trace-capture claim), M3 (q01 re-score disclosure), and the MINOR items. This file preserves the review of the earlier revision; the current report text contains the applied fixes.

# Verification review: `feynman-harness-eval-quality-case-study.md`

**Target:** `/work/outputs/feynman-harness-eval-quality-case-study.md` (45,696 bytes; SHA-256 `cbfe4d4232df88b80f7c91ef2f889389ac0e64923a9e7de5feb0f83e6a2a819a`).
**Review mode:** evidence audit, not peer review. The report was updated at 08:44:51 and again at 08:54:08; this review targets the 08:54:08 text. The 08:54:08 edit resolved two earlier findings (the q01 re-score omission and the Opus p-value misattribution in Section 5.2) and added "on differing question subsets" plus a `[10]` citation; the remaining issues are below.

---

## Summary

The report's central thesis is well supported by the artifacts. The committed eval is a deterministic bibliographic/completion smoke test, not a claim-faithfulness eval: the scorer is blind to negation and to URL/author-year citations (P4/P5/P8), zero-citation rows disappear from the aggregate, `done` is file existence, transparent removal is penalized (75% vs. 100%), and the clean runtime verifier caught errors the scorer cannot see. I reproduced nearly every table row and every token/wall/citation total exactly against `evals/results/*.jsonl`, the probe outputs, and the verifier transcripts.

Two major issues remain, plus a set of smaller precision, attribution, and inventory errors. Section 8.1's statistical table is now stale: it still prints "4/4 vs. 2/4 *p* = 0.43" and calls the Opus comparison "partial," while the corrected Section 5.2 says the Opus comparison is invalid and that the only like-for-like comparison is Terra. Separately, Strength #3's trace-capture claim is still false about workdir deletion. No fabricated result or thesis-invalidating error was found.

---

## Strengths (what checked out)

- **Table 5.1 reproduces exactly.** Cites 51/43/28/54/44/85; validity 100% in every row with citations; title 97/100/100/100/97; recall 75/100/75/50/100/100; wall 7,895/2,806/2,724/2,459/2,508/2,199; tokens 72,190,181/14,053,916/14,073,816/13,039,960/13,353,797/10,953,040; cost `$0` per row / `$0.00` aggregate.
- **Row-level counts.** 22 rows; 4 of 6 result files dirty; five title mismatches (2 in baseline q01, 3 in final Opus q10); baseline q10 timed out at 2,700 s with 18,029,830 tokens; pre-wait Terra q04 consumed 3,968,890 tokens (28.2%).
- **Provenance checks.** `d926547` is not a valid object; `c1e0b29`'s `package.json` says `0.5.2`; `b1c4231` is a descendant of `c1e0b29` and adds the `bg_wait` line; `8e7efc5` is the last change to `evals/run.mjs`; `evals/run.mjs` SHA-256 is `23ba3bff…`; HEAD is `1174429`; package version is `0.5.69`; the installed CLI reports `0.5.65`.
- **Cadence checks.** RELEASES.md has 66 sections from 0.5.4 through 0.5.69; 10 commits touch `prompts/`, `.feynman/agents/`, `.feynman/SYSTEM.md`, or `skills/` after the last eval commit (also 10 from `e2bcb84`); no `evals/` reference in `.github/workflows/` or package scripts; `git diff v0.5.65..HEAD -- prompts/ .feynman/agents/` is empty.
- **Probe checks.** 8/8 probes match expectations; P4/P5/P8 gaps; table probe and `done` probe match the report; verifier scoring is 66.7% / 75.0% / 100.0%.
- **Clean verifier checks.** 594,620 tokens = 36,576 input + 10,460 output + 547,584 cache read; $0.0174; 31 `toolResult` records; 82.8 s from start to completion; zero `eval-scorer-probe` references in the clean transcript; draft SHA-256 unchanged.
- **Question set.** 12 questions; 6 Feynman-search-bench, 3 verbatim LitQA2, 3 hand-authored; only q01/q04/q07/q10 committed; 8 never run.
- **External citations.** arXiv 2407.01502, 2407.10362, 2506.11763, and 2508.15804 match the titles and authors in the report.

---

## Weaknesses (prioritized)

### MAJOR

**M1. Section 8.1's statistical table is stale after the Section 5.2 correction.**
> "| Statistical test | none | 4/4 vs. 3/4 Fisher *p* = 1.0; 4/4 vs. 2/4 *p* = 0.43 |"
> "| Paired comparisons | partial | same four questions, but different subsets for Opus |" (Section 8.1)

Section 5.2 now correctly says: "So 2/2 versus 2/4 reflects a different question set, not a prompt effect. The only like-for-like before/after comparison is Terra: 4/4 versus 3/4, *p* = 1.0." But Section 8.1 still presents 4/4 vs. 2/4 *p* = 0.43 as a statistical test and calls the Opus comparison "partial." The p-value 0.4286 is arithmetically correct for 4/4 vs. 2/4 (final Terra vs. pre-wait Opus), but that is the cross-model comparison Section 5.2 rejects. The table should drop it or label it cross-model and non-paired; the "Paired comparisons" row should say the Opus pair is not comparable (different question sets) and only Terra is like-for-like.

**M2. The "trace capture" claim is false about workdir deletion.**
> "The result row records `git_sha`, `git_dirty`, `feynman_version`, model, `workdir`, per-question token usage, and the full session JSONL. That is enough to audit a run after the fact, even if the workdir is later deleted." (Section 3, Strength #3)

The JSONL row records `workdir` and `usage.session_files` (a count), not the session JSONL content. The session JSONL lives inside the workdir (`evals/README.md`: the workdir holds "the full workspace, session JSONL and `feynman.log`"). If the workdir is deleted, the session is gone; the baseline workdirs are `/var/folders/...` temp paths. The report's own Section 8.3 ("workdirs are local; `--rescore` is not portable") and Recommendation #10 ("Commit … session JSONLs") contradict the claim.

### Resolved during this pass

- **R1. q01 re-score disclosure.** The 08:54:08 text now says: "**Citation validity has never failed on a completed run — as committed.** … One caveat: both pre-wait summaries state that q01 citation validity was re-scored after a transient lookup failure. The committed 100% is therefore post-rescore; the first-pass value is not in the record. 'Never failed' describes the committed rows, not the raw first pass." This resolves the earlier omission; keep this wording.
- **R2. Opus comparison.** Section 5.2 now correctly says the Opus 2/2 vs. 2/4 comparison "reflects a different question set, not a prompt effect" and that the only like-for-like comparison is Terra. The old p = 0.43 sentence is gone. The remaining problem is only that Section 8.1 was not updated (M1).
- **R3. Result-file and configuration counts.** The current text says "six committed result files" and "Six `.md`/`.jsonl` pairs (six configurations)," and "Each configuration was run once; most on four questions, one on two." These are correct.

### MINOR

**m1. 18.05M is the per-question mean, not q10.**
> "18.05M for the baseline's timed-out q10." (Section 1)

q10 is 18,029,830 (18.03M); 18,047,545 (18.05M) is the four-question mean. Section 5.2 gets this right ("18,029,830 … 25.0%").

**m2. "One committed result row references d926547" — it is four rows.**
> "One committed result row references a git SHA (`d926547`) that does not exist in the public repository." (Section 1; also Section 5.1 footnote)

`2026-09-24-lit-ferrylane-openai_gpt-5.6-terra.jsonl` has four rows, all with `d926547`. Say "one result file (four rows)."

**m3. "Nine transcript references" is not reproducible.**
> "Nine transcript references to `eval-scorer-probe` confirm the leak." (Section 7.3)

The contaminated transcript (`/state/.feynman/sessions/subagent-artifacts/a1f6227c-9de8-4bf5-961e-6d6806898d71_verifier_transcript.jsonl`) has 65 substring occurrences of `eval-scorer-probe` across 15 JSONL records; 5 `toolResult` records mention it; 4 tool calls use the probe paths. "Nine" matches none of these counts. The leak itself is unambiguous.

**m4. The `/work` parenthetical is incomplete.**
> "the only `/work` substrings are inside `crossref.org/works` and `openalex.org/works` URLs." (Section 7.2)

The clean transcript also contains `feynman.is/docs/workflows/review/`, `/deep-research/`, and `/literature-review/` URLs. The substantive claim — zero references to the probe fixtures — holds (0 `eval-scorer-probe` hits).

**m5. "last two months of releases" is ~7 weeks.**
> "for the last two months of releases the eval was either not run or not recorded." (Section 8.4)

0.5.3 (2026-09-24) to 0.5.69 (2026-11-13) is 50 days. Say "the last ~7 weeks" or "since 0.5.3."

**m6. The zero-cost cause is inferred, not verified.**
> "Every committed table reports `$0.00` because the provider entry in `models.json` has no `cost` block." (Section 1)

`models.json` is not in the repository; the committed runs used an external file. The README says cost is 0 when no cost block exists, and all `usage.cost_usd` are 0, so the inference is plausible, but "because" is not directly checkable from the repository. Phrase as "consistent with the documented behavior" or "the committed rows record no cost."

**m7. "Title match is 97–100%" is aggregate.**
> "Title match is 97–100%, with five mismatches across two rows." (Section 1)

The 97% values are means; the underlying rows are 92.3% (baseline q01) and 93.0% (final Opus q10). The "five mismatches" sentence mitigates, but "row-level title match ranges 92–100%; aggregate means 97–100%" would be precise.

**m8. The v0.5.3 release note's 0.5.2 comparison is also inconsistent, and the report does not flag it.**
`RELEASES.md` line 476: "(0.5.2: 9-14 minutes, 43 of 43 citations)". The relevant committed 0.5.2 pre-wait Terra row has 28 citations and 3/4 completion; 43/43 is the 0.5.0 Terra file. The report flags the Markdown summary's "0.5.2 run" pointing at a 0.5.0 file, but not this release-note instance of the same mislabel.

**m9. Appendix B omits the transcripts and `experiments/score-verifier-output.log`.**
The contamination claims rely on transcripts; the inventory lists only the output files. The transcripts exist under `/state/.feynman/sessions/subagent-artifacts/` and the clean one has 0 fixture references, so the claim is true, but the artifact inventory is incomplete.

**m10. Sources [2], [5], [7], [8] are not cited by number in the body.**
They are used in the question table and the verifier fixture, but only [1], [3], [4], [6] appear as bracketed citations. Either map them inline or label them as background.

**m11. "one runtime verification probe" vs. the provenance's "2 runtime verification probes."**
The report explains the contaminated attempt, so this is a wording inconsistency, not a substantive error.

---

## Questions for Authors

1. Section 8.1 still prints 4/4 vs. 2/4 *p* = 0.43; should it be removed, or relabeled as the cross-model Terra-vs-Opus comparison that Section 5.2 now says is invalid?
2. Does the `terra-r2` / `opus-r2` workdir naming indicate an earlier uncommitted round? If so, does "one run per configuration" describe the committed record only?
3. Is the v0.5.3 release note's "0.5.2: 43 of 43" a third instance of the 0.5.0/0.5.2 mislabel?
4. Where is the clean verifier transcript archived, and should it be added to Appendix B?

---

## Verdict

**Verification verdict: pass with major corrections.** The central thesis and nearly all quantitative table rows are supported. Two evidence-integrity issues remain: Section 8.1's statistical table contradicts the corrected Section 5.2, and Strength #3's trace-capture claim is false about workdir deletion. The 08:54:08 edit resolved the q01 re-score omission and the Opus p-value misattribution in Section 5.2. Confidence: high on the table/sum arithmetic and probe outputs; high on the Section 8.1 inconsistency and the trace-capture error.

---

## Revision Plan

1. **Fix M1.** In Section 8.1, remove "4/4 vs. 2/4 *p* = 0.43" or label it as the cross-model Terra-vs-Opus comparison; change "Paired comparisons | partial" to "none for Opus (different question sets); Terra only."
2. **Fix M2.** Rewrite Strength #3 to say the row records the workdir path, not the session content; delete "even if the workdir is later deleted."
3. **Fix m1–m7.** 18.03M; four rows for `d926547`; transcript counts; `/work` parenthetical; "~7 weeks"; cost phrasing; row-level title range.
4. **Fix m8–m11.** Disclose the release-note 43/43, add the transcripts and `score-verifier-output.log` to Appendix B, map the uncited sources, and align the probe-count wording.

---

## Checks Performed

| Check | Command / artifact | Result |
|---|---|---|
| Repo HEAD and version | `git rev-parse HEAD`; `package.json`; `.sandbox/environment.txt` | `11744290758648c2ecd7c0d6389cdca9ae580290`; package `0.5.69`; installed `0.5.65` |
| Scorer blob | `sha256sum evals/run.mjs`; `git log -- evals/run.mjs` | `23ba3bff…`; last change `8e7efc5` (2026-09-24) |
| All committed rows | Python parse of `evals/results/*.jsonl` | 22 rows; all table values and sums reproduce |
| Title mismatches | parsed `title_mismatch` arrays | baseline q01 = 2; final Opus q10 = 3 |
| Dangling SHA | `git cat-file -t d926547` | not a valid object |
| Dirty-tree commit | `git show c1e0b29:package.json`; `git show c1e0b29:.feynman/SYSTEM.md \| grep bg_wait` | `0.5.2`; no `bg_wait` |
| `bg_wait` commit | `git merge-base --is-ancestor c1e0b29 b1c4231`; `git show b1c4231` | ancestor; adds the `bg_wait` line |
| Tags / prompt diff | `git tag -l v0.5.65 v0.5.69`; `git diff v0.5.65..HEAD -- prompts/ .feynman/agents/` | both tags; empty diff |
| Release cadence | `grep '^## v0.5.' RELEASES.md`; range count | 66 sections from 0.5.4 to 0.5.69 |
| Prompt commits | `git log 8e7efc5..HEAD -- prompts/ .feynman/agents/ .feynman/SYSTEM.md skills/ \| wc -l` | 10 (also 10 from `e2bcb84`) |
| CI / scripts | `grep -rn eval .github/workflows`; `package.json` scripts | no `evals/` reference |
| Generated scorer | `diff experiments/.tmp-eval-scorer.generated.mjs evals/run.mjs` | only the `main()` call replaced by `export` |
| Probe results | `experiments/eval-scorer-probe-results.json` | 8/8 pass; P4/P5/P8 gaps; table/done probes match |
| Verifier scoring | `experiments/verifier-output-score.json` | draft 3 cites / 66.7%; clean 4 / 75.0%; silent 3 / 100.0% |
| Fisher | exact hypergeometric recomputation | 4/4 vs 3/4 = 1.0; 4/4 vs 2/4 = 0.4286; 2/2 vs 2/4 = 0.4667 |
| Wilson | recomputed | 4/4 → [0.51, 1.00] |
| Clean verifier usage | `8eb27331…_verifier_meta.json` | 36,576 + 10,460 + 547,584 = 594,620; $0.0174; 82.8 s |
| Clean verifier tools | transcript `toolResult` records | 31 |
| Clean transcript leakage | `grep eval-scorer-probe`; `/work` contexts | 0 fixture hits; `/work` hits are crossref/openalex `works` and `feynman.is/docs/workflows` |
| Contaminated transcript | `a1f6227c…_verifier_transcript.jsonl` | 65 `eval-scorer-probe` occurrences / 15 records; 5 `toolResult`; 4 tool calls |
| Draft integrity | `sha256sum draft.md` vs. `.probes` copy | identical (`316ed808…`) |
| Question set | `evals/questions.jsonl` | 12 questions; 6 / 3 / 3 |
| Prompt / verifier instructions | `prompts/lit.md`; `.feynman/agents/verifier.md` | provenance and verification instructions match |
| Isolation | `evals/run.mjs` | `FEYNMAN_HOME`, `TMPDIR`, `FEYNMAN_TELEMETRY=0`, `pkill` reaping |
| Cost block | `grep -rn '"cost"' --include=*.json .`; `models.json` present? | no cost block in repo; `models.json` is external |
| External citations | arXiv lookups 2407.01502, 2407.10362, 2506.11763, 2508.15804 | titles/authors match |

---

## Inline Annotations

> "| Statistical test | none | 4/4 vs. 3/4 Fisher *p* = 1.0; 4/4 vs. 2/4 *p* = 0.43 |"
> "| Paired comparisons | partial | same four questions, but different subsets for Opus |"
**[M1] MAJOR:** Section 5.2 now says the Opus 2/2 vs. 2/4 comparison reflects a different question set and is not a prompt effect. Section 8.1 has not caught up: it still prints 4/4 vs. 2/4 *p* = 0.43 and calls the Opus comparison "partial." The 0.4286 is the cross-model Terra-vs-Opus comparison, not a paired Opus comparison. Update the table.

> "The result row records `git_sha`, `git_dirty`, `feynman_version`, model, `workdir`, per-question token usage, and the full session JSONL. That is enough to audit a run after the fact, even if the workdir is later deleted."
**[M2] MAJOR:** The row records the workdir path and `usage.session_files`, not the session JSONL. The session JSONL is inside the workdir. Delete the workdir and the audit trail is gone. Recommendation #10 already proposes committing session JSONLs, which concedes the point.

> "**Citation validity has never failed on a completed run — as committed.** … One caveat: both pre-wait summaries state that q01 citation validity was re-scored after a transient lookup failure. The committed 100% is therefore post-rescore; the first-pass value is not in the record."
**[resolved]** The 08:54:08 edit now discloses the re-score and hedges "as committed." This addresses the earlier omission; keep this wording.

> "So 2/2 versus 2/4 reflects a different question set, not a prompt effect. The only like-for-like before/after comparison is Terra: 4/4 versus 3/4, *p* = 1.0."
**[resolved]** The 08:54:08 edit correctly rejects the Opus comparison. The only remaining inconsistency is Section 8.1 (M1).

> "18.05M for the baseline's timed-out q10."
**[m1] MINOR:** q10 is 18,029,830 (18.03M). 18,047,545 (18.05M) is the per-question mean. Section 5.2 has the correct q10 figure.

> "One committed result row references a git SHA (`d926547`) that does not exist in the public repository."
**[m2] MINOR:** Four rows in `2026-09-24-lit-ferrylane-openai_gpt-5.6-terra.jsonl` carry `d926547`. "One result file (four rows)" is accurate.

> "Nine transcript references to `eval-scorer-probe` confirm the leak."
**[m3] MINOR:** Measured 65 substring occurrences across 15 JSONL records; 5 `toolResult` records; 4 tool calls with the probe paths. The leak is real; the count is not reproducible.

> "the transcript contains zero references to the probe fixtures or to `/work/...` paths (the only `/work` substrings are inside `crossref.org/works` and `openalex.org/works` URLs)."
**[m4] MINOR:** The clean transcript also contains `feynman.is/docs/workflows/...` URLs. The "zero fixture references" part is verified; the parenthetical is not exhaustive.

> "for the last two months of releases the eval was either not run or not recorded."
**[m5] MINOR:** 0.5.3 (2026-09-24) to 0.5.69 (2026-11-13) is 50 days, not two months.

> "Every committed table reports `$0.00` because the provider entry in `models.json` has no `cost` block."
**[m6] MINOR:** `models.json` is not in the repository and the committed runs used an external file. The zero cost is consistent with the README's documented behavior, but the causal "because" is inferred.

> "Title match is 97–100%, with five mismatches across two rows."
**[m7] MINOR:** 97% and 100% are aggregate means. Row-level title match is 92.3% (baseline q01) and 93.0% (final Opus q10). The five-mismatch sentence mitigates, but the range is aggregate.

> "**Re-analysis of the six committed result files** (JSONL plus matching Markdown summaries) in `evals/results/`"
**[verified]** `evals/results/` contains exactly six `.jsonl` + six `.md` pairs. This was "seven" in the pre-08:44:51 version; the current text is correct.

> "Each configuration was run once; most on four questions, one on two."
**[verified]** Five configurations ran four questions; the final Opus configuration ran q01/q10. This is now accurate.

---

## Sources

- Feynman repository, audited commit `11744290758648c2ecd7c0d6389cdca9ae580290`: https://github.com/Companion-Inc/feynman
- Kapoor et al. (2024), *AI Agents That Matter*: https://arxiv.org/abs/2407.01502
- Laurent et al. (2024), *LAB-Bench*: https://arxiv.org/abs/2407.10362
- Du et al. (2025), *DeepResearch Bench*: https://arxiv.org/abs/2506.11763
- Li et al. (2025), *ReportBench*: https://arxiv.org/abs/2508.15804
- Local evidence inspected: `/tmp/feynman-src` (repo at `1174429`), `/work/experiments/*`, `/work/outputs/.probes/*`, `/work/.sandbox/environment.txt`, `/state/.feynman/sessions/subagent-artifacts/*_verifier_transcript.jsonl`, `/state/.feynman/sessions/subagent-artifacts/*_verifier_meta.json`.
- arXiv API lookup used for the four paper records: `https://export.arxiv.org/api/query?id_list=2407.01502,2407.10362,2506.11763,2508.15804&max_results=4`

---

## Acceptance Report

```acceptance-report
{
  "criteriaSatisfied": [
    {
      "id": "criterion-1",
      "status": "satisfied",
      "evidence": "Wrote outputs/feynman-harness-eval-quality-case-study.review.md with a 2-paragraph summary, a prioritized MAJOR/MINOR issue list, resolved-item notes, inline annotations, and a checks-performed table covering the repo, JSONL rows, probes, verifier transcripts, and statistical recomputation."
    }
  ],
  "changedFiles": [
    "outputs/feynman-harness-eval-quality-case-study.review.md"
  ],
  "testsAddedOrUpdated": [],
  "commandsRun": [
    {
      "command": "git -C /tmp/feynman-src rev-parse HEAD; git show c1e0b29:package.json; git cat-file -t d926547",
      "result": "passed",
      "summary": "HEAD 1174429; c1e0b29 package 0.5.2; d926547 invalid"
    },
    {
      "command": "python3 parse of evals/results/*.jsonl",
      "result": "passed",
      "summary": "22 rows; all table cites/tokens/wall/validity/title/recall values reproduce"
    },
    {
      "command": "python3 exact Fisher recomputation",
      "result": "passed",
      "summary": "4/4 vs 3/4 = 1.0; 4/4 vs 2/4 = 0.4286; 2/2 vs 2/4 = 0.4667"
    },
    {
      "command": "grep -c eval-scorer-probe on the clean and contaminated verifier transcripts",
      "result": "passed",
      "summary": "clean = 0; contaminated = 65 occurrences / 15 records"
    },
    {
      "command": "python3 parse of verifier meta/usage",
      "result": "passed",
      "summary": "594,620 tokens; $0.0174; 31 toolResult records; 82.8 s"
    },
    {
      "command": "grep '^## v0.5.' RELEASES.md and git log 8e7efc5..HEAD -- prompts/ ...",
      "result": "passed",
      "summary": "66 release sections (0.5.4-0.5.69); 10 prompt/agent commits"
    }
  ],
  "validationOutput": [
    "Table 5.1 reproduces exactly; 22 rows; 4 dirty files; title mismatches 2+3; token/wall sums match.",
    "Section 5.2 now discloses the q01 re-score and correctly rejects the Opus 2/2 vs 2/4 comparison (resolved during this pass).",
    "Section 8.1 still prints 4/4 vs 2/4 p=0.43 and calls the Opus comparison 'partial' (M1).",
    "Strength #3 still claims auditability after workdir deletion; the row only stores the workdir path (M2)."
  ],
  "residualRisks": [
    "The report changed twice during this pass (08:44:51 and 08:54:08); the review targets SHA-256 cbfe4d4232df88b80f7c91ef2f889389ac0e64923a9e7de5feb0f83e6a2a819a and may not cover further edits.",
    "The first-pass q01 validity value is not recoverable from the committed record; the report now discloses this, but the magnitude of the re-score effect remains unknown.",
    "The models.json used for the committed runs is not in the repository, so the zero-cost cause remains an inference."
  ],
  "noStagedFiles": true,
  "diffSummary": "Added a verification review file; did not modify the report.",
  "reviewFindings": [
    "blocker: M1 - Section 8.1 still reports 4/4 vs 2/4 p=0.43 and calls the Opus comparison 'partial,' contradicting the corrected Section 5.2.",
    "blocker: M2 - Strength #3 claims a run is auditable after workdir deletion; the result row only stores the workdir path."
  ],
  "manualNotes": "Reviewed the 08:54:08 version. The earlier q01 re-score omission and the Section 5.2 Opus p-value misattribution are now fixed; the remaining Section 8.1 table is stale. The earlier 'seven committed result files' and 'each configuration on four questions' errors are also fixed. No report text was rewritten."
}
```
