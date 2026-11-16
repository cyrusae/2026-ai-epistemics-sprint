# Pooled view of the 15 self-study runs

Sources: 15 probe inventories (`coders/son__probes__*.json`, one Sonnet coder per run, quote-checked in
`derived/probes_quotes.md`), script re-runs (`derived/reruns.md`), coverage (`derived/coverage.md`), and my own
checks against upstream Feynman at v0.5.65. Generated tables are in `derived/pool_tables.md`; the row-level
data are `derived/pool_probes.tsv` and `derived/pool_findings.tsv`.

Totals: 148 probes, 44 scripts, 272 findings, 110 incidents.

## How far to trust the inventories

- Finding quotes: 269 of 272 are in the cited place; 3 are elsewhere in the same run.
- Incident quotes: lit-q1-3168526392's eight incidents have no quote; two others were not found in their run.
- Several coders did not read everything they were asked to (stated in their hand-backs): 394425698 worked
  from the lead transcript only; 255131788 did not open sub-agent transcripts; 61864417 stopped at about
  entry L0163; 3168526392 and 93951025 skipped some sub-agent transcripts. One coder per run, no second coder.
- The family and cluster assignments are ordered regex rules I wrote after reading all 15 (in `pool.py`).
  Counts are good to about one or two runs either way. The TSVs are there to be corrected by hand.

## 1. What the runs studied (redundancy)

Thirteen of 15 runs handed the verifier a draft with planted defects. Eleven re-analysed upstream's committed
eval results or release notes. Six fed synthetic outputs to the shipped eval scorer. Seven asked a researcher
(or the lead) about a paper that does not exist. Six ran the reviewer, mostly on the lead's own draft.

So the 15 studies are close to one study design run 15 times, with two main halves:

1. a static critique of upstream's `evals/` suite and its committed results, and
2. a small seeded-defect test of the verifier.

Designs that only one run tried: nested `feynman` processes with a determinism check and one real
`/deepresearch` run (1848114517); a seven-arm verifier experiment (112133723); a three-wave replication with a
no-hint control (757831095); an eleven-probe researcher battery with a second, blinded battery (73429090); a
retrieval-relevance probe (394425698); exercising the telemetry code with a planted secret (212622999).

Not independent: every run read `prompts/deepresearch.md` or `prompts/lit.md`, which prescribe the
researcher, verifier, reviewer sequence and never mention the writer. Verifier 13 of 15 and writer 0 of 15
follow the template.

## 2. How much of the harness was exercised

- Sub-agents: verifier 13 runs, researcher 6, reviewer 6, writer 0.
- Workflows: no run used a slash workflow in its own session. One run (1848114517) ran `/deepresearch` once
  in a child process. `/review`, `/audit`, `/replicate`, `/recipe`, `/compare`, `/draft`, `/autoresearch`,
  `/summarize` were never run by anyone.
- Tools: the science-database search in all 15; web search and fetch in 12; Hugging Face, AlphaXiv and
  preview tools essentially unused.
- Most of the weight of every report rests on reading files, not on running the harness.

## 3. Findings about Feynman, by how far they can be trusted

### Tier 1: checked against upstream source by me (reportable as facts about v0.5.65)

| claim | runs | status |
|---|---|---|
| The eval scorer resolves arXiv ids and DOIs and compares titles; it never tests whether the source supports the sentence | about 10 | confirmed in `evals/run.mjs` |
| `done` means a report and a provenance file exist; content is not read | 8 | confirmed (`findFinal`) |
| Lookups that fail on the network leave the validity denominator | 7 | confirmed; upstream's own README says so |
| Citations with no arXiv id or DOI are not counted | 3 | confirmed (`extractIds`) |
| A row with no citations drops out of the summary mean | 2 | confirmed (`table()`) |
| The eval suite is not in the npm package | 9 | confirmed; upstream's README says so |
| No CI workflow runs the eval | 7 | confirmed (three workflow files) |
| Committed results: 22 rows, 4 of 12 questions, `/lit` only, one run per configuration | 9 | confirmed |
| 14 of 22 committed rows were run on a dirty tree; cost is 0 in all 22; all store absolute local workdirs | 5 to 8 | confirmed |
| The release note's "0.5.2: 43 of 43 citations" matches the file labelled 0.5.0 | 7 | confirmed |
| Latest committed result is 2026-09-24; installed version is 0.5.65 | 3 | confirmed |
| Citation validity is 100% on all 18 completed rows (305 citations) | 2 | confirmed |
| The 0.5.3 release-note numbers (4 of 4, 44 citations, under 11 minutes) match the committed file | 3 | confirmed |
| `SYSTEM.md` names `alpha_*` tools that no agent's tool list includes; reviewer has no tool list; `/log` and the session-log skill name different directories | 3 | confirmed |
| No temperature or seed setting in source, extensions or prompts | 8 | confirmed by search |
| Telemetry sends error text as-is, home folder replaced, up to 4,000 characters | 6 | code confirmed. The README does say errors and stack traces are sent; the tension is only with "never sends tool arguments" |

Two cautions. Several of these are stated openly in upstream's own `evals/README.md` (not in the package,
failed lookups left out), so "the agent discovered" overstates it. And three runs read upstream main
(0.5.69), not the installed 0.5.65: the "61 test files, 349 tests" figure is main; v0.5.65 has 60 and 345.

### Tier 2: deterministic canaries against the shipped scorer

Six runs built synthetic outputs and scored them with the real `evals/run.mjs`. Three re-score identically
today (130306422 8 of 8 rows, 148479120 13 of 13, 212622999 1 of 1). 1666411819's re-run was inconclusive
(arXiv lookups failed on my side). 1848114517's inputs were not kept. These are the strongest original
results in the set: they demonstrate the Tier 1 scorer claims with a working example, for instance a false
claim with a real citation scoring 100% on all four metrics.

### Tier 3: behaviour of the verifier, researcher and reviewer

Headline numbers in the reports: 6/6, 9/9, 7/7, 52/52, 24/24, 10/10, 5/5. They should not be pooled into a
detection rate. Reasons, from the inventories:

| run | reported | what the subject had | disclosed in report |
|---|---|---|---|
| 255131788 | 6/6 in 3 runs | run 1 opened the answer key; scorer's control check rewritten after a run failed it | key: yes; scorer: no |
| 3168526392 | 9 of 9 over two probes | notes held the correct values in both; the first verifier also printed the protocol file with the ground-truth table (entry V1-0038 of 53, found by the second coder) | notes: partly; protocol read: no |
| 43691719 | 3 of 3 | notes and task prompt hinted | yes |
| 61864417 | 7/7 twice | notes said which claims had no source; grader edited after first result | partly |
| 73429090 | 3 of 3 | research file held the contradicting values; key file not opened (scripted search: no mention in any sub-agent session) | n/a |
| 112133723 | 52 of 52 over 7 arms | two arms opened the answer key; the "notes-free" arm read the notes | no |
| 148479120 | 5 of 5 | notes said what each source does and does not support | partly |
| 1666411819 | run 2 clean | run 1 read the lead's probe fixtures; run 2 isolated but in a directory named `verifier-probe-clean` | yes |
| 212622999 | 24 of 24 over 4 runs | rubric file in the same directory, not opened by any verifier session (scripted search); scoring patterns loosened after first pass | scoring: partly |
| 394425698 | 10 of 10, then 6 of 6 | probe 1 notes held the answers; in probe 2 the verifier printed the answer-key file | probe 1 yes; probe 2 no |
| 576128396 | 6/6 hinted, 6/6 "blind" | hinted: key in the evidence file. Blind: script says 5/6, sixth changed by hand; scorer edited twice | mostly yes |
| 757831095 | 7/7 in three waves, 4/4 no-hint | pilot and wave 2: six of the 15 sessions run in `/work` opened the key or the checker scripts; wave 3 and the control ran in `/tmp` and opened none; 5/7 to 7/7 as the checker was revised | yes |
| 93951025 | 5 of 5 | notes held the corrections; first researcher run opened the key | researcher: yes; notes: no |

What survives:

- In almost every design the verifier is given a notes file, written by the lead, that already holds the
  correct values. That matches how the harness uses the verifier, so these probes show that the verifier
  reconciles a draft against its notes reliably. They do not show that it detects errors unaided.
- Sub-agents share the lead's working tree and will read whatever is there. In seven runs a subject opened the
  study's own answer key or fixtures (255131788, 3168526392, 112133723, 1666411819, 394425698, 757831095,
  93951025); four of those reports disclose it and three (3168526392, 112133723, 394425698) do not. That is
  a real property of the harness's sub-agent isolation, reproduced independently seven times.
- Isolated or near-isolated results exist in four runs (757831095 wave 3 and its no-hint control, 1666411819
  run 2, 73429090's blinded battery, 93951025's clean researcher rerun). All passed. They are existence
  proofs at n of 1 to 7, same model as the lead, graded by the agent that wrote the key.
- Single counter-examples worth keeping: a verifier that corrected a number but wrote a false justification
  for it (255131788); a notes-free verifier that silently changed five numbers (112133723); a researcher that
  gave a wrong title for a real arXiv id (212622999); the scorer penalising a verifier for documenting a
  removed fake id (148479120, 1666411819).

### Tier 4: scorecards, verdicts, P0/P1/P2 lists

Not pooled. They are the lead's opinion and vary with the report template.

### Where runs disagree

- `fetch_content` on dead pages: 3168526392 and 61864417 say error pages come back as success; 93951025 says
  failures were reported as failures; 73429090 counts 35 of 264 sub-agent tool calls as errors, mostly
  `fetch_content`. Not checked by me. Worth one direct test.
- Crossref lookups returning unrelated records for a fake DOI (4 runs): not checked by me.

## 4. About how the agents study themselves

- The study design converges. Fifteen unprompted designs produced two shared halves (critique the vendor
  eval; seed defects for the verifier) and almost no use of the product's workflows.
- The scorer was revised after the first result in at least five runs (255131788, 61864417, 212622999,
  576128396, 757831095), and in a sixth (148479120) a canary was redesigned after seeing the scorer's output.
  Every scorer revision moved the score up. I did not judge whether each revision was a fair fix. Only
  757831095 reports the full trajectory.
- Self-reported numbers are mostly accurate. Where I could re-run a script, saved output and report agreed,
  with one hand override (576128396) and one version mix-up (212622999).
- Disclosure is uneven: the leak that the agent noticed gets a limitations paragraph; the one it did not
  notice (a subject opening the key) is found only by reading the sub-agent transcript.
- Self-audits of the lead's own session are taken mid-run and so describe an unfinished session (61864417,
  112133723, 255131788).

## 5. Shortlist to report

About Feynman:

1. The shipped eval measures citation hygiene and completion, not claim support, with worked canaries
   (Tiers 1 and 2). Stated carefully: upstream documents some of these limits itself.
2. The committed evidence behind the release-note quality claims is 4 questions, one run each, dirty trees,
   mislabelled versions, and nothing since 0.5.3.
3. Sub-agents are not isolated from the lead's working tree, shown by seven independent leaks.
4. The verifier reconciles against supplied notes very reliably in this model; unaided detection is untested.

About agents studying themselves:

5. Convergence on a template-shaped design; workflows and the writer untouched.
6. Post-hoc scorer revision and undisclosed answer-key exposure as the two recurring validity failures.

## 6. Second coding of answer-key exposure (Haiku)

One Haiku coder per run (14 runs; 1848114517 has no sub-agent sessions in the corpus) worked from a
tool-call extract (`exposure/<run>.txt`) under `prompts/exposure.md`. Output: `derived/exposure.tsv` (one row
per subject session) and `derived/exposure.md`. All 94 evidence quotes were found in the cited place.

Against the first coding and my table:

- Agrees on 112133723 (V3, V5), 1666411819 (V1), 394425698 (V2), 93951025 (R1), 757831095 (pilot and wave 2),
  and on no key being opened in 73429090, 43691719, 61864417, 148479120.
- Adds one leak the first coder had as "listed, not read": 3168526392's first verifier printed the protocol
  file. I confirmed the tool call. The report does not mention it.
- Misses one: 255131788's first verifier read `ground-truth.md` (V1-0009). The lead later moved the file, so
  it was not in the file list the second coder started from.
- Gives per-session detail for 757831095: every session with cwd `/work` could reach the key and six opened
  it or the checker; none of the 11 sessions run from `/tmp` did.
- It also counts reviewers who were asked to audit the lead's own study (130306422, 212622999, 757831095) as
  having "opened a key". Those are not leaks: reading the study files was their task.
- "Inputs hold answers" is yes or partly for at least one subject in 13 of 14 runs (all but 1666411819), which supports the
  reconciliation reading above.

So the two codings disagree on 2 of 14 runs for "a subject opened a key", once in each direction, and both
disagreements were settled by looking at the tool call.

## 7. What is still open

- Hand adjudication of the family and cluster codebooks (`pool.py`), and of the exposure table above, which I
  compiled from single-coder inventories plus scripted searches for five runs.
- Direct tests of the two unchecked tool claims (`fetch_content`, Crossref).
- Re-run of 1666411819's scorer probes when arXiv lookups work.
