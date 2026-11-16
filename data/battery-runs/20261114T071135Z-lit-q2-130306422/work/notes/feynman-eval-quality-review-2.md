# Second-pass verification: `outputs/feynman-harness-eval-quality.md`

**Reviewer role:** evidence-integrity audit (second pass, after `notes/feynman-eval-quality-review.md`)
**Target:** `/work/outputs/feynman-harness-eval-quality.md`
**Pinned source:** `/tmp/feynman-src` @ `11744290758648c2ecd7c0d6389cdca9ae580290` (package 0.5.69)
**Rule followed:** report not rewritten; this note is the only authored artifact.

**Verdict:** **9 of 10 prior findings are resolved.** **F1 is only partially resolved:** the headline now uses the defensible 46-commit substantive count, but §5 says **64** commits touch only `package.json`; the git count is **63**. The stated 46+64 arithmetic also silently drops the one `.feynman/SYSTEM.md`-only commit, and the 110 still includes one merge commit. One additional factual error remains in the §5 release-claim table (the search benchmark file). f7 isolation, the probe command, and the 46/110 totals otherwise reproduce.

---

## Prior findings: pass/fail

| ID | Prior finding | Status | Verification |
|---|---|---|---|
| **F1** | 110 presented as substantive churn; no decomposition | ❌ **PARTIAL / FAIL** | 110 total ✅; 46 four-path substantive ✅; 47 including `.feynman/SYSTEM.md` ✅; 6 prompt commits ✅; **63 package-only, not 64** ❌; 1 merge (`f57b849`) still undisclosed; 46 includes that merge. See R1. |
| **F2** | “47 … alone” off by one | ✅ Resolved | `git log --since=2026-09-24 -- prompts .feynman/agents skills extensions | wc -l` = 46; adding `.feynman/SYSTEM.md` = 47. Report now states both correctly. |
| **F3** | Determinism “Strong” omitted network-dependent `valid` and manual q01 re-score | ✅ Resolved | §2 caveat cites `run.mjs:183` and `README.md:48`; §3 splits “Scoring logic determinism” (Strong) from “Measurement stability” (Adequate). Both pre-wait summaries say “q01 citation validity was re-scored after a transient lookup failure.” |
| **F4** | f7 fixture confounded by exact key-paper title | ✅ Resolved | Fixture body is now `Test-time compute scaling (Snell et al.) 2408.03314.` — no exact key-paper title. Re-ran `--rescore`: f7 row has `cites: 0`, `valid: null`, `title: null`, `recall: 1`. Recall can only come from the bare-ID substring. |
| **F5** | “4 questions per run” false for one run | ✅ Resolved | Row counts are 4, 4, 2, 4, 4, 4. The 0.5.3 Opus run has 2 rows (q01, q10); its `.md` says only non-biology questions were run because Opus 5.5 refuses q04/q07. Report now says “2–4 questions per run (one Opus run has 2…).” |
| **F6** | §9 “committed results cannot tell” overstated | ✅ Resolved | `2026-09-24-lit-0.5.3-ferrylane_claude-opus-5-5.md:3` documents the q04/q07 refusals; Terra’s 0.5.3 `.md` has no panel explanation. Report now says Opus is explained, Terra is not. |
| **F7** | Probe command did not match recorded command | ✅ Resolved | `probe-result.txt` command is `env -u PI_SESSION_ID -u PI_SESSION_FILE FEYNMAN_TELEMETRY=off timeout 240 feynman --no-session --prompt '…'`. Report shows the same env assignments, timeout, flags, and prompt text; only single-vs-double quote style and line wrapping differ. |
| **F8** | README line 5 cited for `tests/` absence | ✅ Resolved | `evals/README.md:5` supports only `evals/`; `package.json.files` omits both `evals/` and `tests/`. Report now says exactly that. |
| **F9** | `done` described as catching an arbitrary failed workflow call | ✅ Resolved | Report now says `done` catches the failure only if it prevents the final artifact, and an eval run would at least exercise the path. |
| **F10** | “Eight fixtures found four false-positive modes” oversold | ✅ Resolved | Report now says several documented limits were confirmed, one undocumented title-heuristic false positive (`f5`), and one extraction inconsistency (`f7`). |

---

## Remaining issues

### R1 — **MAJOR (F1 residual): §5 says 64 package-only commits; git says 63**
**Location:** §5, “Two further facts matter…”, first bullet.

> “A looser count including `package.json` is 110, but **64 of those touch only `package.json`** and are mostly version/release metadata.”

Per-commit classification of the 110 commits since 2026-09-24 over the six cited paths:

- **63** touch only `package.json` among the six paths;
- **1** touches only `.feynman/SYSTEM.md`;
- **46** touch `prompts/`, `.feynman/agents/`, `skills/`, or `extensions/` (13 of those also touch `package.json`);
- **1** of the 110 is a merge commit (`f57b849`, PR #300, touching `extensions/`).

So the correct partitions are **63 + 47 = 110** (including `SYSTEM.md`) or **63 + 46 + 1 = 110**. The report’s **46 + 64 = 110** works only by folding the `SYSTEM.md`-only commit into the package-only bucket. `git-stats.txt` also records `only_package_json_among_six_paths: 64`, which appears to be the same 110−46 subtraction rather than a measured count. Fix §5 to 63 and make the partition explicit. The headline claim (“46 substantive”) is otherwise correct and no longer presents 110 as substantive churn.

Secondary residuals in the same finding: (a) the 110 still includes one merge commit, so “110 commits” double-counts PR #300 unless non-merge (109) is stated; (b) 13 of the 46 substantive commits also touch `package.json`, so “46 substantive + 63 package-only” is not a clean two-bucket partition of the 46.

### R2 — **MINOR/MAJOR (additional, not among the prior 10): “No benchmark file” for the 7/9 search benchmark is false**
**Location:** §5 release-claim table, last row.

> “Search benchmark: 7/9 vs 2/9 seminal papers | Look for the benchmark in the repo | **No benchmark file or result artifact; only the release note** | Unverified”

The six queries and their nine key papers are in `evals/questions.jsonl`: `q01`–`q06` have 1+2+2+1+2+1 = 9 key papers, and `evals/README.md:61` explicitly calls `q01`–`q06` “the six queries from Feynman's paper-discovery search benchmark.” The repo therefore contains the benchmark inputs; what is missing is the **7/9 vs 2/9 result artifact**. The table should say “benchmark inputs in `evals/questions.jsonl`; no result artifact for the 7/9 comparison.” This also contradicts §2’s own statement that q01–q06 are the paper-discovery search benchmark. `feynman-harness-eval-quality.provenance.md` repeats the “no benchmark file in repo” claim.

### R3 — **MINOR (evidence traceability): fixture score rows have no case IDs and are not in report order**
`fixtures.jsonl` rows carry only `id: q01` and an absolute `workdir`; the case name is only inferable from the path. The rows are in dict order **f1, f2, f3, f4, f5, f7, f8, f6**, while the report table lists f1…f8 with **f6 before f7**. A reader matching table order to raw rows would swap f6 and f7. The f7 row is row **6**, not row 7. Add a `case` field or reorder the table to match. This does not affect the f7 isolation result itself.

### R4 — **MINOR: “All four 0.5.3 rows” is ambiguous**
There are **six** 0.5.3 rows (Terra 4 + Opus 2), and all six are `git_dirty: true`; the report’s “All four 0.5.3 rows” is true for Terra but reads as all 0.5.3 rows. Say “all four Terra 0.5.3 rows” or “all six 0.5.3 rows.” No numeric contradiction, because every 0.5.3 row is dirty.

---

## Verification log

| Check | Result |
|---|---|
| `git log --since=2026-09-24 -- prompts .feynman/agents .feynman/SYSTEM.md skills extensions package.json | wc -l` | **110** ✅ |
| Per-commit six-path classification | 63 package-only; 1 SYSTEM-only; 46 four-path (13 also package); 1 merge ✅ (but report says 64) |
| `git log --since=2026-09-24 -- prompts | wc -l` | **6** ✅ |
| `git log --since=2026-09-24 -- prompts .feynman/agents skills extensions | wc -l` | **46** ✅ |
| `... plus .feynman/SYSTEM.md` | **47** ✅ |
| f7 fixture body | `Test-time compute scaling (Snell et al.) 2408.03314.`; no exact title ✅ |
| Re-run `node evals/run.mjs --rescore …/fixtures.jsonl` | Row 6 (`f7-bare-id`): `cites 0`, `valid -`, `title -`, `recall 100%` ✅ |
| `probe-result.txt` vs report command | Same env vars, `timeout 240`, `--no-session --prompt`, same prompt text; only quoting differs ✅ |
| Probe artifact | 17 bytes, `FEYNMAN_PROBE_OK\n`; exit 0; stdout `DONE`; dirs include `notes/`, `outputs/`, `outputs/.drafts/`, `outputs/.plans/`, `papers/` ✅ |
| 0.5.3 Terra rows | 11+11+7+15 = 44 citations; `citations_checked` 44; all `citation_validity` 1; all `title_match` 1; 4/4 completed; wall 652/628/578/650 ✅ |
| 0.5.3 Opus row count | 2 (q01, q10) ✅ |
| Dirty rows | 14/22 ✅ |
| Cost rows | 22/22 `$0` ✅ |
| 43-citation baseline | Only `2026-09-24-lit-ferrylane-openai_gpt-5.6-terra.jsonl`; version 0.5.0 ✅ |
| Pre-wait q01 re-score note | Present in both pre-wait `.md` files ✅ |
| `run.mjs:183` / `README.md:48` | `checked = rows.filter(r => r.resolves !== undefined)`; README says network failures are left out ✅ |
| Test/CI | 61 `*.test.ts` files; 0 reference `evals/`; workflows are `deploy-website`, `e2e`, `publish` (no eval job) ✅ |
| Installed versions | Feynman 0.5.65; Node 24.21.0; Pi 1.5.0; pi-subagents 0.86.0; pi-web-access 0.47.0 ✅ |
| Session | `openrouter/deepseek/deepseek-v4.1-flash-1017`; telemetry off; alphaXiv not configured ✅ |
| Search benchmark inputs | q01–q06 = 6 queries, 9 key papers; `evals/README.md:61` calls it the paper-discovery search benchmark ❌ report says “no benchmark file” |

No other numeric regressions were found in the revised passages. The **64** is a new error relative to the prior review’s 63; all other headline numbers reproduce.

---

## Inline annotations

> “In that window, 46 substantive commits touched prompts, agents, skills, or extensions (110 if `package.json` release/version commits are included)…”
**[F1] PARTIAL:** The 46/110 totals are right, but 110 also includes one `.feynman/SYSTEM.md`-only commit and one merge commit; the parenthetical does not state that partition.

> “A looser count including `package.json` is 110, but **64 of those touch only `package.json`** and are mostly version/release metadata.”
**[F1] FAIL:** Git gives **63**, not 64. 110 = 63 package-only + 46 four-path (13 also package) + 1 SYSTEM-only. The 64 is 110−46 and hides the SYSTEM-only commit; `git-stats.txt` repeats the same derived number.

> “Search benchmark: 7/9 vs 2/9 seminal papers | Look for the benchmark in the repo | **No benchmark file or result artifact; only the release note**”
**[R2] MINOR/MAJOR:** The benchmark inputs are in `evals/questions.jsonl` (q01–q06, nine key papers), which `evals/README.md:61` explicitly calls the paper-discovery search benchmark. Only the 7/9 result artifact is missing. This also contradicts §2.

> “`f7-bare-id` contains the bare ID `2408.03314` and no exact key-paper title. `cites` is 0 … but `recall` is 100% because `keyRecall` does a raw substring match on the text.”
**[F4] PASS:** Verified by re-running `--rescore`: row 6 is `cites 0`, `valid -`, `title -`, `recall 100%`; the fixture has no exact title, so the ID substring is the only recall source. Note the raw row is row 6 (f7), while the report table places f7 after f6.

> “2–4 questions per run (one Opus run has 2 after biology refusals)”
**[F5] PASS:** Row counts are 4, 4, 2, 4, 4, 4; the 0.5.3 Opus `.md` documents the q04/q07 refusals.

> “env -u PI_SESSION_ID -u PI_SESSION_FILE FEYNMAN_TELEMETRY=off timeout 240 … feynman --no-session --prompt …”
**[F7] PASS:** Matches the recorded command in `probe-result.txt` except for quote style/line wrapping; artifact is 17 bytes, exit 0, stdout `DONE`.

> “All four 0.5.3 rows have `git_dirty: true`; 14/22 rows overall are dirty.”
**[R4] MINOR:** There are six 0.5.3 rows (Terra 4 + Opus 2), all dirty; this is true for Terra but ambiguous as written.

---

## Sources

- Pinned repository: <https://github.com/Companion-Inc/feynman/tree/11744290758648c2ecd7c0d6389cdca9ae580290>
- `evals/run.mjs`: <https://github.com/Companion-Inc/feynman/blob/11744290758648c2ecd7c0d6389cdca9ae580290/evals/run.mjs>
- `evals/README.md` (line 5 package exclusion; line 48 `valid`; line 61 search benchmark): <https://github.com/Companion-Inc/feynman/blob/11744290758648c2ecd7c0d6389cdca9ae580290/evals/README.md>
- `evals/questions.jsonl`: <https://github.com/Companion-Inc/feynman/blob/11744290758648c2ecd7c0d6389cdca9ae580290/evals/questions.jsonl>
- 0.5.3 Terra results: <https://github.com/Companion-Inc/feynman/blob/11744290758648c2ecd7c0d6389cdca9ae580290/evals/results/2026-09-24-lit-0.5.3-ferrylane-openai_gpt-5.6-terra.jsonl>
- 0.5.3 Opus results: <https://github.com/Companion-Inc/feynman/blob/11744290758648c2ecd7c0d6389cdca9ae580290/evals/results/2026-09-24-lit-0.5.3-ferrylane_claude-opus-5-5.jsonl>
- Pre-wait Terra results: <https://github.com/Companion-Inc/feynman/blob/11744290758648c2ecd7c0d6389cdca9ae580290/evals/results/2026-09-24-lit-0.5.3-pre-wait-ferrylane-openai_gpt-5.6-terra.jsonl>
- Merge commit `f57b849`: <https://github.com/Companion-Inc/feynman/commit/f57b849b380b04985ba0cfe8d9acaf33ecc52e28>
- `278e9af`: <https://github.com/Companion-Inc/feynman/commit/278e9afe4a5b34e42e774563c3f14d3af7346955>
- Local: `/work/experiments/feynman-eval-audit/{git-stats.txt,make_fixtures.py,fixtures.jsonl,fixtures.md,rescore.log}`
- Local: `/work/experiments/feynman-harness-probe/{probe-result.txt,probe.log,outputs/probe-artifact.md}`
