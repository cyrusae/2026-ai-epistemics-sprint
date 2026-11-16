# Stress-testing a research-agent harness (AI × Epistemics sprint, Nov 2026)

Code, prompts, pre-registration, raw runs and analysis for a weekend study of **Feynman 0.5.65**, an open-source research-agent harness, driven by a budget model (DeepSeek V4.1 Flash, snapshot `20261017`, via OpenRouter). Everything here was produced 2026-11-12 → 2026-11-16.

Three studies:

| Study | Question | Where |
|---|---|---|
| **Exhibit** | What went wrong (and right) in one long real session where the agent was asked for a literature review? | `analysis/exhibit/FINDINGS.md` |
| **Battery** | Given only *"I'm interested in a case study of the Feynman harness from an AI-eval-quality perspective, so dogfooding it a bit."*, what do 15 fresh, memory-free sessions build, and why do they escalate from "a bit" to designing and running a study? | `analysis/battery/`, raw runs in `data/battery-runs/` |
| **Reproduction** | Asked to audit and/or replicate a published NLP paper from its code, how well do 20 sessions do: audit → replicate (`seq`) vs replicate only (`repl`)? | `analysis/reproduction/` |

## Layout

```
sandbox/            Docker sandbox: one fresh container + state dir per run (`fs` runner, `fsutil.py`)
sandbox-paper/      Variant image with Python toolchain for the paper runs (`fp` wraps `fs`); prompts used
prompts/            Battery stimulus (p1.md), the single allowed follow-up (p2.md), turn-1 judge (judge.md)
prereg/             Pre-registered rubric and predictions, with the SHA-256 fixed before data collection
data/battery-runs/  The 15 battery runs: logs/ (prompts, stdout, per-turn file manifests, turns.jsonl),
                    sessions/ (full Feynman session logs, including every sub-agent), work/ (what the agent wrote)
analysis/battery/   Scripted facts, coding prompts, coder outputs (Sonnet / Haiku / Gemini), quote verification,
                    adjudications, timelines
analysis/exhibit/   Findings and the scripts/codebook used; the session itself is not published (see below)
analysis/paper-timeline/  Wall-clock timelines of the 20 reproduction runs
analysis/reproduction/    Grading rubric (frozen, hash in judging/rubric.sha256), blind-judge pipeline,
                          per-unit judge outputs, verified scores
scripts/check-public.sh   Pre-publication scan used on this repo
```

## Reproducing a run

```sh
docker build -t feynman-sandbox:0.5.65 sandbox/          # pinned, checksum-verified Feynman release
echo 'OPENROUTER_API_KEY=...' > .env; echo 'EXA_API_KEY=...' >> .env
sandbox/fs new mylabel -f prompts/p1.md                   # one fresh sandbox; outputs in sandbox/runs/
sandbox/fs batch -j 4 15 mylabel -f prompts/p1.md         # 15 at once
sandbox/fs ls mylabel; sandbox/fs packet <run> 1          # summary table; evidence packet for a judge
```
See `sandbox/README.md` for the full command set (judge, decide, followup, export).

## What is withheld, and why

- **The replicated paper is pseudonymized** as *Paper P* with code repository *R*: the study is about the agent, and we do not want this to read as a public audit of the original authors. The topic, method names and numbers are left in, so a determined reader can identify it.
- **Raw transcripts and agent outputs of the 20 reproduction runs are not published**: they quote the paper, its code and its authors throughout. The judging packets were built from them by `analysis/reproduction/judging/build_units.py`; the per-unit judge outputs and verified scores are included.
- **The exhibit session is not published**: it ran on the author's own machine with persistent memory and read the author's other sessions. `FINDINGS.md` cites entry IDs and short quotes only.
- Paths on the author's machine are replaced with `<local path>`. API keys were passed by environment and never written to disk.

## Models used in analysis

Coding and judging used Claude Sonnet and Haiku (via the Claude Code CLI on a subscription), and Gemini 3.8 Flash (via the `agy` CLI). Every quote a coder or judge returned is machine-checked against the source (`verify*.py`); scores resting only on unverifiable quotes are flagged. Where coders disagreed, the researcher's adjudication is recorded (`analysis/battery/adjudication.md`).
