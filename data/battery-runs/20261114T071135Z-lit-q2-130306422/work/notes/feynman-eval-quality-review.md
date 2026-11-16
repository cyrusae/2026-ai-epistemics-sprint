# Adversarial review: `outputs/feynman-harness-eval-quality.md`

**Reviewer role:** evidence-integrity audit (skeptical, adversarial)
**Target:** `/work/outputs/feynman-harness-eval-quality.md`
**Pinned source:** `/tmp/feynman-src` @ `11744290758648c2ecd7c0d6389cdca9ae580290` (HEAD `1174429`, package 0.5.69, 2026-11-13)
**Audit artifacts:** `/work/experiments/feynman-eval-audit/`, `/work/experiments/feynman-harness-probe/`
**Verdict on the report itself:** no fatal errors found. The report's central claims reproduce. Two major overclaims/missing caveats and eight minor issues follow.

---

## Findings

### F1 — MAJOR — "110 commits" is presented as substantive churn, but 63/110 touch only `package.json` among the cited paths
**Location:** Bottom line ¶4 ("In that window, 110 commits touched those surfaces…"); §5 "Two further facts"; §8 lesson 3; §3 "Process adherence".
**Problem:** The literal count reproduces (`git log --since=2026-09-24 -- prompts .feynman/agents .feynman/SYSTEM.md skills extensions package.json` → 110; `git-stats.txt` records `eval_relevant_commits_since_2026-09-24: 110`). But the report never decomposes it, so a reader infers ~110 substantive prompt/tool changes. In fact:
- 63 of the 110 touch **only `package.json`** among the six rule paths;
- 51 of those 63 carry release/version-update subjects (e.g. `f39aec3 "Update pi-subagents to 0.88.1; release 0.5.69"`, `32cfff4 "Release 0.5.4"`);
- 1 of the 110 is a merge commit (109 non-merge), so the count double-counts at least one PR;
- the substantive prompt/agent/skill/extension/`SYSTEM.md` count is **47** (46 if `SYSTEM.md` is excluded).
The audit's own `git-stats.txt` records a much narrower `prompt_commits_since_2026-09-24: 6`, which the report does not mention. The verdict ("decayed operating discipline") still holds on 47 substantive changes, but "110" overstates the evidence roughly 2.3×.
**Evidence:** `git log` decomposition (see above); `/work/experiments/feynman-eval-audit/git-stats.txt:11-12`.

### F2 — MINOR — "47 of those touch prompts/agents/skills/extensions alone" is off by one
**Location:** §5 "Two further facts", first bullet.
**Problem:** 46 commits touch `prompts/`, `.feynman/agents/`, `skills/`, `extensions/`. The 47th is a commit that also/instead touches `.feynman/SYSTEM.md`, which the same sentence lists separately ("…or `.feynman/SYSTEM.md`…"). Either say "47 including `SYSTEM.md`" or "46 excluding it".
**Evidence:** `git log --since=2026-09-24 --oneline -- prompts .feynman/agents skills extensions | wc -l` → 46; adding `.feynman/SYSTEM.md` → 47. `git-stats.txt` contains no 47; its only prompt count is 6.

### F3 — MAJOR — "Determinism: Strong" omits that scoring depends on live arXiv/Crossref responses, and that a committed row was manually re-scored after a lookup failure
**Location:** §2 "What is genuinely good" ("**Determinism.** … The same artifact text and the same live metadata produce the same score."); §2 metric table `valid` row; §3 scorecard row "Isolation and determinism | **Strong** | … | Removes the largest sources of accidental variance".
**Problem:** `valid` is not a property of the artifact alone. `scoreCitations` computes `checked = rows.filter(r => r.resolves !== undefined)` (`evals/run.mjs:183`), so a network/API failure silently **removes** an identifier from both the `valid` numerator and denominator and never lists it in `unresolved`. `evals/README.md:48` says this explicitly ("Lookups that fail on the network are left out"). More importantly, two committed result summaries state: **"q01 citation validity was re-scored after a transient lookup failure."** That is a manual re-score, not a deterministic single pass, and it is in the very files the report says it read ("all committed result files", §1). A transient failure can therefore yield `valid: 100%` on a shrunken denominator, which is exactly the reading the report warns against elsewhere. The "Strong" rating and "same score" sentence need this caveat; at minimum the report should note `citations` vs `citations_checked` as the audit check.
**Evidence:** `evals/README.md:48`; `evals/run.mjs:183,188`; `evals/results/2026-09-24-lit-0.5.3-pre-wait-ferrylane-openai_gpt-5.6-terra.md:3`; `…-claude-opus-5-5.md:3`.

### F4 — MINOR — the f7 fixture is confounded: the exact title alone guarantees `recall`, so it does not show that recall "sees" a bare ID
**Location:** §4 table `f7-bare-id`; §4 "What the probe establishes" item 6 ("visible to `recall` (100%) because `keyRecall` does a raw substring match on the text").
**Problem:** `f7` contains **both** the exact key-paper title and the bare ID. `keyRecall` (`evals/run.mjs:198`) passes on `normed.includes(norm(p.title))` regardless of the ID, so `recall = 100%` is guaranteed by the title. The fixture cannot isolate the claimed bare-ID behavior; a bare ID with a *non-exact* title would be needed. The broader conclusion ("recall is presence, not use") is still true and is independently visible in the code, but this specific inference is unsupported by the fixture.
**Evidence:** `/work/experiments/feynman-eval-audit/make_fixtures.py` (`f7-bare-id` body); `evals/run.mjs:198`.

### F5 — MINOR — "4 questions per run" is false for one of the six committed runs
**Location:** §3 scorecard "Statistical power | Weak | 4 questions per run…".
**Problem:** `2026-09-24-lit-0.5.3-ferrylane_claude-opus-5-5.jsonl` has **2** rows (q01, q10). Its `.md` explains why: "Only the non-biology questions were run: Opus 5.5 refuses q04 and q07." "Typical run is four questions" is fine; the blanket "4 questions per run" is not.
**Evidence:** `evals/results/2026-09-24-lit-0.5.3-ferrylane_claude-opus-5-5.jsonl` (2 lines); `…-claude-opus-5-5.md:3`.

### F6 — MINOR — §9 open question "the committed results cannot tell" is partly answered by the committed results
**Location:** §9, "Why only q01, q04, q07, and q10? Budget, runtime, or model refusals? The committed results cannot tell."
**Problem:** The Opus subset **is** explained in the committed `.md` ("Only the non-biology questions were run: Opus 5.5 refuses q04 and q07"), and `RELEASES.md` documents the same refusal as a known issue. What remains genuinely unexplained is why *Terra* used the same four-id panel. The sentence overstates the unavailability of the answer.
**Evidence:** `evals/results/2026-09-24-lit-0.5.3-ferrylane_claude-opus-5-5.md:3`; `RELEASES.md:484`; `evals/results/2026-09-24-lit-0.5.3-pre-wait-ferrylane_claude-opus-5-5.jsonl` (q04 exit 1, q07 exit 1).

### F7 — MINOR — live-probe reproduction command in the report does not match the recorded command
**Location:** §6 "Live one-shot probe" code block; §1 table "Live probe".
**Problem:** The report's command sets `FEYNMAN_TELEMETRY=off feynman --no-session --prompt …`. The recorded command line in `probe-result.txt` is `feynman --no-session --prompt '…'` with no env assignment. The outcome (exit 0, `DONE`, 17 bytes, `.plans/`/`.drafts/`/`notes/`/`papers/`) does reproduce from the artifacts, but the exact command shown is not the one recorded.
**Evidence:** `/work/experiments/feynman-harness-probe/probe-result.txt` (`command:` line); `…/outputs/probe-artifact.md` (17 bytes, `FEYNMAN_PROBE_OK\n`).

### F8 — MINOR — `README line 5` is cited for the absence of `tests/` too, but line 5 only covers `evals/`
**Location:** §6 "The eval is not shipped. `evals/` and `tests/` are absent from the npm package (`package.json` `files`; README line 5)."
**Problem:** `evals/README.md:5` says only "This directory is not in the npm package". The absence of `tests/` is true (verified against `package.json.files`) but is not supported by the cited README line. This is the same "citation attached to a claim that does not support the exact wording" failure the report itself audits.
**Evidence:** `evals/README.md:5`; `package.json.files` (neither `evals/` nor `tests/` listed).

### F9 — MINOR — "exactly the kind of failure the eval's `done` metric is designed to catch" overstates `done`
**Location:** §5 "A concrete missed regression" (commit `278e9af`).
**Problem:** `278e9af` fixes a prompt after "a live run improvised `parallel()` and its first workflow call failed." `done` checks only that a largest `outputs/*.md` and its `.provenance.md` exist (`evals/run.mjs:87-94`). A run can have a failed first workflow call and still recover to produce both files. The failure mode `done` demonstrably catches is the *pre-wait* `bg_wait` case (Terra q04, `completed: false`), not an arbitrary failed tool call.
**Evidence:** `git show -s 278e9af`; `evals/run.mjs:87-94`; `evals/results/2026-09-24-lit-0.5.3-pre-wait-ferrylane-openai_gpt-5.6-terra.md:3`.

### F10 — MINOR — "eight fixtures found four false-positive modes" is oversold; three are restatements of the documented metric definitions
**Location:** §8 lesson 2.
**Problem:** `f3` (relevance), `f4` (numeric claims), and `f8` (rejected-source presence) follow directly from what `evals/README.md` already says each metric measures (`valid` = resolves; `recall` = "appear in the final output"). Only `f5` (prose satisfying the title-overlap check) is a genuinely undocumented false-positive mode, plus `f7`'s extraction inconsistency. Presenting all four as discoveries inflates the meta-eval's contribution.
**Evidence:** `evals/README.md:48-50`; §4 results table.

---

## Category coverage (explicit no-issue statements)

1. **Numbers that do not match the artifacts:** apart from **F2** (47 vs 46) and the **F1** framing, no numeric mismatches found. Every other headline number reproduces exactly (see verification log).
2. **Statements that overstate what the eval measures:** the core framing is accurate (`done`/`valid`/`title`/`recall` do not measure claim support). The overstatements are **F1**, **F9**, **F10**, and the missing **F3** caveat.
3. **Claims about git history / test coverage that are wrong:** only **F2** (off-by-one). The `e2bcb84` last-eval-commit claim, `0 commits since 2026-09-25 -- evals`, `0 tests referencing evals/`, `61 test files`, and "CI does not run it" all verify. No wrong claim found beyond F2.
4. **Missing caveats:** **F3** is the material one (network-dependent `valid` denominator + manual re-score). **F5/F6** are smaller.

---

## Verification log (all reproduced unless noted)

| Report number | Check | Result |
|---|---|---|
| 6 JSONL files, 22 rows, 4 ids | `wc -l evals/results/*.jsonl`; distinct ids | ✅ 6 / 22 / q01,q04,q07,q10 |
| 12 questions, 18 key papers | `evals/questions.jsonl` | ✅ 12 / 18 (1 or 2 per question) |
| `e2bcb84`, 2026-09-24, last `evals` commit | `git log -- evals` | ✅ |
| 0.5.3 Terra: 11+11+7+15 = 44; 44/44 valid; all `title_match` = 1 | JSONL | ✅ |
| wall_s 652/628/578/650; max 10.87 min | JSONL | ✅ (652/60 = 10.867) |
| all four 0.5.3 rows `git_dirty: true`; 14/22 dirty overall | JSONL | ✅ 14/22 |
| all 22 rows `cost_usd = 0` | JSONL | ✅ |
| 43-citation baseline exists only in `2026-09-24-lit-ferrylane-openai_gpt-5.6-terra.jsonl`, labeled 0.5.0 | JSONL sums | ✅ 13+15+4+11=43, version 0.5.0; its wall range 9.4–13.6 min matches "9–14 min" |
| 0.5.3 rows `git_sha c1e0b29` (2026-09-23 commit) | `git show -s c1e0b29` | ✅ |
| 110 commits since 2026-09-24; 0 since 2026-09-25 touching `evals` | `git log` | ✅ 110 / 0 |
| 47 touch prompts/agents/skills/extensions "alone" | `git log` | ❌ 46; 47 includes `.feynman/SYSTEM.md` (F2) |
| f5: 8/11 title tokens = 72.7% | re-implemented `tokens()`/`titleOverlap` on fixture | ✅ (STOP list drops `can`,`be`; `than` kept; 11 unique, 8 matched) |
| f1/f2/f3/f4/f5/f6/f7/f8 table | `fixtures.jsonl` | ✅ all eight match |
| Wilson 44/44 [0.92,1.00]; 4/4 [0.51,1.00] | Python | ✅ |
| Probe: exit 0, `DONE`, 17 bytes, dirs | `probe-result.txt`, `probe-artifact.md` | ✅ (17 bytes incl. `\n`) |
| Installed 0.5.65 / Node 24.21.0 / Pi 1.5.0 / pi-subagents 0.86.0 / pi-web-access 0.47.0 | `feynman --version`, `node -v`, installed `package.json`s | ✅ |
| Session model `openrouter/deepseek/deepseek-v4.1-flash-1017`, telemetry off, alphaXiv not configured | `feynman status` | ✅ |
| `evals/` and `tests/` absent from npm package | `package.json.files` | ✅ |
| 61 test files; 0 reference `evals/`; CI has no eval job | `find tests`, grep, `.github/workflows` | ✅ (`deploy-website`, `e2e`, `publish`) |
| All 10 `run.mjs` line references (87-94, 96-106, 111-148, 150-189, 195-199, 246-249, 251-259, 267-274, 279, 285) | `nl -ba evals/run.mjs` | ✅ all resolve to the described code |
| Release quote v0.5.3 | `RELEASES.md:470-484` | ✅ verbatim |
| 3 related-work arXiv IDs + titles/authors/years | arXiv API `id_list` | ✅ all three exist and match |
| "table() unweighted mean, nulls dropped; 3/4 run shows valid 100%, recall 75%" | `run.mjs:251-259`, pre-wait Terra `.md` | ✅ |

---

## Inline annotations

> "In that window, 110 commits touched those surfaces, including a November 5 fix to the `/lit` prompt after a live workflow failure, and **zero commits touched `evals/`**."
**[F1] MAJOR:** The 110 reproduces but is inflated: 63/110 touch only `package.json` among the cited paths, 51 of those are release/version commits, and 1 is a merge. The defensible substantive count is 47 (46 excluding `SYSTEM.md`). The zero-evals half is correct.

> "47 of those touch prompts/agents/skills/extensions **alone**."
**[F2] MINOR:** 46, not 47. The 47th touches `.feynman/SYSTEM.md`, which the preceding clause lists separately.

> "**Determinism.** The scorer is a readable ~300-line Node script with no LLM judge. The same artifact text and the same live metadata produce the same score."
**[F3] MAJOR:** `valid` depends on live arXiv/Crossref/doi.org responses, and `run.mjs:183` silently drops network-failed lookups from the denominator (`README.md:48`). Two committed summaries say "q01 citation validity was re-scored after a transient lookup failure" — a manual re-score, not a deterministic pass. Add this caveat; downgrade or qualify "Strong".

> "`f7-bare-id` is invisible to `cites` (0), but visible to `recall` (100%) because `keyRecall` does a raw substring match on the text."
**[F4] MINOR:** f7 also contains the exact key-paper title, so `normed.includes(norm(title))` guarantees recall. The fixture cannot isolate the bare-ID path.

> "Statistical power | **Weak** | **4 questions per run**, one run per condition, no repeats or intervals…"
**[F5] MINOR:** The Opus 0.5.3 run has 2 questions (q01, q10), per its own `.md` (biology refusals).

> "Why only q01, q04, q07, and q10? Budget, runtime, or model refusals? **The committed results cannot tell.**"
**[F6] MINOR:** The committed Opus `.md` and `RELEASES.md:484` do explain the q04/q07 refusals. Only the Terra panel choice is unexplained.

> "That is **exactly the kind of failure** the eval's `done` metric is designed to catch."
**[F9] MINOR:** `done` checks artifact+provenance existence, not "a workflow call failed". The bg_wait case is the one it demonstrably catches.

> "Eight hand-written fixtures found **four false-positive modes**; scoring them took seconds."
**[F10] MINOR:** Three of the four (relevance, numeric claims, rejected-source presence) are restatements of `evals/README.md`'s metric definitions. Only the prose-satisfies-title case is a new failure mode.

> "`evals/` and `tests/` are absent from the npm package (`package.json` `files`; **README line 5**)."
**[F8] MINOR:** `evals/README.md:5` supports only the `evals/` half; `tests/` absence is supported by `package.json.files` alone.

---

## Sources

- Pinned repo: <https://github.com/Companion-Inc/feynman/tree/11744290758648c2ecd7c0d6389cdca9ae580290>
- `evals/run.mjs`: <https://github.com/Companion-Inc/feynman/blob/11744290758648c2ecd7c0d6389cdca9ae580290/evals/run.mjs>
- `evals/README.md`: <https://github.com/Companion-Inc/feynman/blob/11744290758648c2ecd7c0d6389cdca9ae580290/evals/README.md>
- `evals/questions.jsonl`: <https://github.com/Companion-Inc/feynman/blob/11744290758648c2ecd7c0d6389cdca9ae580290/evals/questions.jsonl>
- `RELEASES.md` (v0.5.3, line 470 ff.; known issue line 484; 7/9 benchmark line 541): <https://github.com/Companion-Inc/feynman/blob/11744290758648c2ecd7c0d6389cdca9ae580290/RELEASES.md>
- `prompts/lit.md` (six steps: Plan, Gather, Synthesize, Cite, Verify, Deliver): <https://github.com/Companion-Inc/feynman/blob/11744290758648c2ecd7c0d6389cdca9ae580290/prompts/lit.md>
- `src/telemetry/posthog.ts` (telemetry notice, "never sends prompts, model output, paper content, or tool arguments"): <https://github.com/Companion-Inc/feynman/blob/11744290758648c2ecd7c0d6389cdca9ae580290/src/telemetry/posthog.ts>
- Commit `278e9af`: <https://github.com/Companion-Inc/feynman/commit/278e9afe4a5b34e42e774563c3f14d3af7346955>
- Related work checked via arXiv: <https://arxiv.org/abs/2511.04703>, <https://arxiv.org/abs/2605.06635>, <https://arxiv.org/abs/2505.19253>
- Local artifacts: `/work/experiments/feynman-eval-audit/{git-stats.txt,release-claim-check.txt,fixtures.jsonl,fixtures.md,rescore.log,make_fixtures.py}`; `/work/experiments/feynman-harness-probe/{probe-result.txt,probe.log,outputs/probe-artifact.md}`
