Wrote `/work/notes/feynman-eval-quality-review.md` (151 lines, 10 findings). Same list inline:

---

# Adversarial review: `outputs/feynman-harness-eval-quality.md`

**Scope:** checked every number against `/tmp/feynman-src` @ `1174429` (0.5.69), `evals/`, and both audit dirs. **No fatal errors found.** The report's central claims reproduce: 6 JSONL files / 22 rows / 4 ids, 12 questions / 18 key papers, 44 citations (11+11+7+15), 44/44 valid, max 652 s = 10.87 min, 14/22 dirty rows, all 22 `cost_usd=0`, Wilson [0.92,1.00] and [0.51,1.00], f5 = 8/11 = 72.7%, probe = 17 bytes / exit 0, installed 0.5.65 / Node 24.21.0 / Pi 1.5.0 / pi-subagents 0.86.0 / pi-web-access 0.47.0, and all 10 `run.mjs` line references. The v0.5.3 release quote is verbatim, and all three related-work arXiv IDs exist with matching titles.

## Findings

### F1 — MAJOR
**Location:** Bottom line ¶4; §5 "Two further facts"; §8.3; §3 "Process adherence".
**Problem:** "110 commits touched those surfaces" reproduces (`git log --since=2026-09-24 -- <6 paths>` → 110; `git-stats.txt:11`), but is never decomposed. 63/110 touch **only `package.json`** among the six paths; 51 of those carry release/version-bump subjects (e.g. `f39aec3 "Update pi-subagents to 0.88.1; release 0.5.69"`, `32cfff4 "Release 0.5.4"`); 1 is a merge (109 non-merge). The substantive prompt/agent/skill/extension/`SYSTEM.md` count is **47** (46 excluding `SYSTEM.md`). The audit's own `git-stats.txt` records a much narrower `prompt_commits_since_2026-09-24: 6`. The claim is literally true but reads as ~110 substantive changes — roughly a 2.3× overstatement of the evidence behind "decayed operating discipline."
**Evidence:** `git log` decomposition; `/work/experiments/feynman-eval-audit/git-stats.txt:11-12`.

### F2 — MINOR
**Location:** §5 first bullet.
**Problem:** "47 of those touch prompts/agents/skills/extensions **alone**" is off by one. 46 touch `prompts/`, `.feynman/agents/`, `skills/`, `extensions/`; the 47th includes `.feynman/SYSTEM.md`, which the sentence lists separately. Should be "46 excluding `SYSTEM.md`" or "47 including it."
**Evidence:** `git log --since=2026-09-24 -- prompts .feynman/agents skills extensions | wc -l` → 46; +`.feynman/SYSTEM.md` → 47.

### F3 — MAJOR
**Location:** §2 "Determinism"; §2 `valid` row; §3 "Isolation and determinism | **Strong**".
**Problem:** `valid` is not a property of the artifact alone. `run.mjs:183` computes `checked = rows.filter(r => r.resolves !== undefined)`, so a network/API failure silently removes an ID from both numerator and denominator and never appears in `unresolved`; `evals/README.md:48` says "Lookups that fail on the network are left out." Worse, two committed summaries state: **"q01 citation validity was re-scored after a transient lookup failure"** — a manual re-score, not a deterministic pass, in the files the report says it read. A transient failure can yield `valid: 100%` on a shrunken denominator. "Strong"/"same score" needs this caveat; `citations` vs `citations_checked` is the audit check.
**Evidence:** `evals/README.md:48`; `run.mjs:183,188`; `evals/results/2026-09-24-lit-0.5.3-pre-wait-…-terra.md:3` and `…-opus-5-5.md:3`.

### F4 — MINOR
**Location:** §4 `f7-bare-id` row; §4 item 6.
**Problem:** f7 contains **both** the exact key-paper title and the bare ID. `keyRecall` (`run.mjs:198`) passes on `normed.includes(norm(p.title))` regardless of the ID, so `recall=100%` is guaranteed by the title. The fixture cannot isolate the claimed bare-ID path; a bare ID with a non-exact title was needed. The broader "recall is presence, not use" conclusion still holds from code.
**Evidence:** `make_fixtures.py` (`f7` body); `run.mjs:198`.

### F5 — MINOR
**Location:** §3 "Statistical power | **Weak** | 4 questions per run…".
**Problem:** `2026-09-24-lit-0.5.3-ferrylane_claude-opus-5-5.jsonl` has **2** rows (q01, q10); its `.md` explains the biology refusals. "Typical run is four" is fine; the blanket "4 questions per run" is not.
**Evidence:** that file (2 lines) and its `.md:3`.

### F6 — MINOR
**Location:** §9, "Why only q01, q04, q07, and q10? … The committed results cannot tell."
**Problem:** The Opus subset **is** explained in the committed `.md` ("Only the non-biology questions were run: Opus 5.5 refuses q04 and q07") and in `RELEASES.md:484`. Only the Terra panel choice remains unexplained.
**Evidence:** `…-opus-5-5.md:3`; `RELEASES.md:484`; pre-wait Opus q04/q07 exit 1.

### F7 — MINOR
**Location:** §6 probe code block.
**Problem:** The report's command includes `FEYNMAN_TELEMETRY=off`; the recorded `command:` line in `probe-result.txt` omits it. Outcome reproduces, but the shown command is not the recorded one.
**Evidence:** `/work/experiments/feynman-harness-probe/probe-result.txt`; `outputs/probe-artifact.md` (17 bytes incl. `\n`).

### F8 — MINOR
**Location:** §6 "The eval is not shipped… (`package.json` `files`; README line 5)."
**Problem:** `evals/README.md:5` supports only the `evals/` half. `tests/` is indeed absent from `package.json.files`, but not from the cited README line — the same citation-vs-wording failure the report audits.
**Evidence:** `evals/README.md:5`; `package.json.files`.

### F9 — MINOR
**Location:** §5 "A concrete missed regression" (`278e9af`).
**Problem:** "Exactly the kind of failure the eval's `done` metric is designed to catch" overstates `done`, which only checks artifact+provenance existence (`run.mjs:87-94`); a run can have a failed first workflow call and still recover to write both. The case `done` demonstrably catches is the pre-wait `bg_wait` failure (Terra q04).
**Evidence:** `git show -s 278e9af`; `run.mjs:87-94`; pre-wait Terra `.md:3`.

### F10 — MINOR
**Location:** §8 lesson 2.
**Problem:** "Eight fixtures found four false-positive modes" is oversold. f3 (relevance), f4 (numeric claims), and f8 (rejected-source presence) restate what `evals/README.md:48-50` already defines. Only f5 (prose satisfying the title check) is a genuinely undocumented failure mode, plus f7's extraction inconsistency.
**Evidence:** `evals/README.md:48-50`; §4 table.

## Category coverage
1. **Numbers vs artifacts:** only F2 (47 vs 46); F1 is a framing overclaim, not a mismatch. All other numbers reproduce exactly.
2. **Overstating what the eval measures:** core framing is accurate. Overstatements are F1, F9, F10, plus the missing F3 caveat.
3. **Git history / test coverage:** only F2 is wrong. `e2bcb84`, `0` commits since 2026-09-25 touching `evals`, `61` test files, `0` test references, and "CI does not run it" (workflows: `deploy-website`, `e2e`, `publish`) all verify.
4. **Missing caveats:** F3 is material; F5/F6 smaller.

---