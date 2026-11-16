# Provenance — `feynman-harness-eval-case-study.md`

Run date: 2026-11-14
Harness: Feynman 0.5.65 (`/opt/feynman/feynman-0.5.65-linux-arm64/app`)
Model: `openrouter/deepseek/deepseek-v4.1-flash-1017`, reasoning `high`
Workspace: `/work`
Lead session: `/state/.feynman/sessions/2026-11-14T08-05-41-567Z_01a1d917-3e3f-7157-8f13-31ea82eed8fd.jsonl`

## Source accounting

| # | Source | How used | Status |
|---|---|---|---|
| 1 | Vaswani et al. 2017, arXiv:1706.03762 | Ground truth for planted claims; full HTML v7 and abstract page saved locally | live, content matched (HTTP 200) |
| 2 | Miller 2024, arXiv:2411.00640 | Statistical-rigor criterion ("evals are experiments"; error bars) | abstract fetched and read (HTTP 200) |
| 3 | Biderman et al. 2024, arXiv:2405.14782 | Reproducibility criterion (lm-eval lessons) | abstract fetched and read (HTTP 200) |
| 4 | Reuel et al. 2024, arXiv:2411.12990 (BetterBench) | Benchmark-quality lifecycle criteria (46 practices, 24 benchmarks) | abstract + methodology passages read (HTTP 200) |
| 5 | Inspect, UK AI Security Institute | Contrast case: dataset + solver + scorer + sandbox | docs fetched (HTTP 200) |
| 6 | Companion-Inc/feynman repository | Version/licence/repo identity | GitHub API checked (10,121 stars, MIT); HTTP 200 |
| 7 | Crossref REST API query | Lookalike-DOI hazard | raw response saved at `experiments/harness-verifier-eval/logs/crossref-query.json` |

Local primary artifacts:
- `experiments/harness-verifier-eval/logs/arxiv-abs.html` (43,071 bytes)
- `experiments/harness-verifier-eval/logs/arxiv-html.html` (188,707 bytes)
- 4 input drafts + 1 research-notes file (hashes below)
- 7 cited documents + 4 audit tables

## Verification log

| Claim in case study | Check performed | Status |
|---|---|---|
| 4 agents / 16 skills / 11 prompts / 3,537 policy words / 71 rule markers | `ls`, `wc`, regex count on installed package | verified |
| 0 shipped tests/eval suites; 0 code references to `.provenance` | `find` + `grep -r` over installed package | verified |
| 52/52 planted items caught; 0 unjustified removals | Manual scoring of each output against `GROUND-TRUTH.md` | verified (unblinded, lead-scored) |
| 5 silent numeric corrections in the notes-free cited doc | Read `notesfree-cited.md` and compared to `draft-treatment.md` | verified |
| 8/8 disclosed in `default-contract-cited.md`; 0/8 in `noaudit-cited.md` | Read both files; child message confirms filename confound | verified |
| Crossref returns three 2025 `posted-content` lookalikes with real author list | `crossref-query.json`; `jq` inspection | verified |
| Paper says 41.0 in §6.1 but 41.8 in abstract/Table 2 | Searched `arxiv-html.html`; four verifier runs independently flagged it | verified |
| Token counts per arm | Parsed child `session.jsonl` usage fields | verified |
| `/deepresearch` / `/lit` emit valid provenance sidecars end-to-end | Not run | **not run** |
| Verifier behavior across seeds/models | N=1 per arm, one model | **unverified / not run** |

## Explicit non-claims

- This is not a reliability estimate. N = 1 per arm; no confidence intervals.
- The 52/52 detection result does not generalize to longer documents, other models, paywalled sources, or adversarial citation graphs.
- The "0 runtime checks" claim covers citation/provenance enforcement only; the CLI does verify model endpoints and package loading.
- The case study was written by the same harness it studies. No independent auditor scored the outputs.

## Artifact hashes (SHA-256)

```
4f728afab440529fb8c8056f91f451ff8bc5688aab5b19ff7ed73bc84f45fd7c  GROUND-TRUTH.md
74fc390c9fd7bbbbb3a816779530f03326fcbd45661a9df5410e0b608f099c82  inputs/draft-treatment.md
61c359ff134a82ad210c529c80bf1be87894409c533713c9d5b292ac9fe6af3a  inputs/draft-control.md
12904626b5beb258591f582b28bc4bac46211ba0923480ed48d5e6c62d4ca88a  inputs/draft-unsupported.md
5854f9852471ee6e591b06b8154d001d240b13e0713035a2ca7a1bfd6c69b572  inputs/research-notes.md
dfad93a1cab187f01878eb8784e29e63e30885fc146673768153afe9e4ac7655  logs/crossref-query.json
2558b8957de7a14c670ba2a4b4553b0ff5cf63c1f5e06a35d153f7f95ad8ba61  outputs/treatment-cited.md
4d38fd7a78ff1bdc183f258067a915809c2abd12775b42e2ec5fe03781b8757d  outputs/treatment-audit.md
0c92102cf8c2ff88a13d748dd0580a6b6114184250ccbfcb50919b4027722e6b  outputs/control-cited.md
7c702b6ad5e4a414f6f16541c4c07fc6395eff47fe0baeb260b5717f8f2cb76f  outputs/control-audit.md
623d047945ff8c300396a34bc79d3e5411ea37e138f1d677b2a94f969f5d9856  outputs/notesfree-cited.md
86b992f99c5e32e444d7ffed69094dd0d4949bcbe68b8023642d146710c63ab4  outputs/notesfree-audit.md
4d7d8e8da329d958a8d1c07783982b0bb6fe33706688ab5e780cb20971808070  outputs/unsupported-cited.md
f5d9af8be97ad381982927e2190e3080f670c41103b0e89736aa606b23afd7e6  outputs/unsupported-audit.md
b10805a3fc060fe240506df7acf3655c0c7346eeddb58efed7a7c9abcf78d7ec  outputs/unsupported-default-cited.md
cd242ed2091f3f9c1114390ca20510beea12975fc28c251c215790bd813a6e33  outputs/noaudit-cited.md
35219d41c6f417d962821337eab74d291dfb3b7ce99f69bee8e5381bd6ee042a  outputs/default-contract-cited.md
```
