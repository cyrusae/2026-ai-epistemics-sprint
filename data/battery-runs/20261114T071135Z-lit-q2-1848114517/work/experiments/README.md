# Experiments: Feynman eval-quality case study

Everything here is reproducible from a clean checkout of this workspace plus network
access. No credentials are stored.

## 1. Behavioural probes (`run_probe.py`)

Spawns the installed CLI as an isolated subprocess per run:

- fresh `--cwd` under `experiments/runs/<probe>-<n>/workspace`
- fresh `--session-dir` under `experiments/runs/<probe>-<n>/sessions`
- `PI_SESSION_FILE` / `PI_SESSION_ID` stripped so the child cannot append to the
  parent session
- `FEYNMAN_TELEMETRY=off`
- model `openrouter/deepseek/deepseek-v4.1-flash-1017`, `--thinking low`

```sh
cd /work
python3 experiments/run_probe.py det trap ground workflow
# or a subset: python3 experiments/run_probe.py trap
```

Outputs: `experiments/runs/<run>/stdout.txt`, `stderr.txt`, `meta.json`, and the raw
Pi session JSONL. Aggregate: `experiments/probe-results.json` and
`notes/feynman-eval-quality-traces.md`.

Probe definitions (verbatim prompts) are in `PROBES` in `run_probe.py`.

## 2. Scorer audit (`scorer-audit/`)

Five synthetic artifacts, scored by Feynman's own `evals/run.mjs` in `--rescore` mode.
This tests the measuring instrument, not the agent: same scorer, same question (q01),
different artifact quality.

```sh
cd experiments/scorer-audit
node run.mjs --rescore rescored-rows.jsonl   # see RESULTS.md for recorded output
```

Files:

| File | Purpose |
|---|---|
| `run.mjs` | copy of `Companion-Inc/feynman@main:evals/run.mjs` (md5 `4cfc1d14…`) |
| `questions.jsonl` | copy of the 12-question eval set |
| `rescored-rows.jsonl` | scored rows (scorer rewrites its input path) |
| `RESULTS.md` | each synthetic artifact next to the scores it received |
| `package.json` | minimal repo marker so `run.mjs` can read a version |

Synthetic cases: (1) correct-format review that contradicts the paper, (2) valid ID with
wrong title, (3) five valid but irrelevant citations, (4) fabricated ID, (5) no final
artifact.

## 3. Ground truth

- arXiv IDs/titles for 1706.03762, 2201.11903, 2106.09685, 2312.00752, 2305.18290:
  `feynman_science_database_search` arXiv `id_list` response, 2026-11-14.
- Transformer WMT14 EN-DE BLEU 28.4: same arXiv abstract.
- NeurIPS 2017 HTML abstract page says 27.5: direct fetch of
  `papers.nips.cc/paper_files/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html`
  (2026-11-14). This is the discrepancy the workflow probe found independently.

## 4. Not run

- The full 12-question `/lit` eval against this build (each question took 10-45 min and
  millions of tokens for the models in the committed baselines).
- Multi-model replication of the probes. All probe results here are one cheap model.
