# Raw probe outputs (transcribed)

Date: 2026-11-13. Harness: Feynman 0.5.65. Model: `openrouter/deepseek/deepseek-v4.1-flash-1017`.
These are transcribed key fields from tool output and subagent artifacts produced in this session.
Full session trace: `/state/.feynman/sessions/2026-11-13T13-08-35-301Z_01a1d506-3164-77c2-a925-c045394b666d.jsonl`.

## P1a — arXiv exact ID

`feynman_science_database_search(source="arxiv", query="1706.03762")` returned:

- `arxiv_id`: `1706.03762`; `version`: 7
- `title`: "Attention Is All You Need"
- `authors[0]`: "Ashish Vaswani"
- `published`: `2017-06-12T17:57:34Z`
- `provenance.endpoints`: `https://export.arxiv.org/api/query?id_list=1706.03762&max_results=1`

Verdict: exact match to the canonical arXiv record.

## P1b — OpenAlex exact work

`openalex_get_work:W2626778328` returned:

- `title`: "Attention Is All You Need"
- `publication_year`: 2017; `publication_date`: `2017-06-12`
- first author: "Ashish Vaswani"
- `doi`: `10.48550/arxiv.1706.03762`
- `cited_by_count`: 136211

Verdict: exact match.

## P1c — Crossref DOI-shaped query

`feynman_science_database_search(source="crossref", query="10.48550/arXiv.1706.03762")` returned:

- `totalCount`: 6599726
- top 3: `10.1163/2210-7886_asc-48550` ("48550, 1889-11-21"), `10.1037/t48550-000` ("Incompatibility Measure"), `10.32614/cran.package.changepoints`
- no `not_found` field; no DOI record for `10.48550/arXiv.1706.03762`

Verdict: fuzzy keyword search, not an exact DOI lookup.

## P1d — Crossref non-existent DOI

`source="crossref", query="10.9999/not.a.real.doi.2026"` returned:

- `totalCount`: 16049765
- top 3: `10.1037/t95715-000` ("Child-Rearing Scale"), `10.1037/t95714-000` ("Feeling Scale for Mothers"), `10.1037/t95710-000` ("Victim Cognition Scale for Mothers")
- no `not_found` field

Verdict: a non-existent identifier produces unrelated records, not a clear negative.

## P1e — Crossref title query

`source="crossref", query="Attention Is All You Need Vaswani 2017"` returned:

- `totalCount`: 7701975
- top 3: `10.65215/r5bs2d54`, `10.65215/ysbyhc05`, `10.65215/nxvz2v36`
- all: title "Attention Is All You Need", `type: posted-content`, dates 2025-11-13 / 2025-08-23 / 2025-08-23

Direct Crossref record for `10.65215/r5bs2d54`:

- `publisher`: "Shenzhen Medical Academy of Research and Translation"
- `type`: `posted-content`
- `created`: `2025-11-13T02:40:31Z`
- resolution chain: `https://doi.org/10.65215/r5bs2d54` → 302 → `https://langtaosha.org.cn/index.php/lts/preprint/view/10` → 302 → `https://langtaosha.org.cn/lts/en/preprint/view/10` → **404**

Verdict: title-matched but not the 2017 NeurIPS paper; the landing page is dead.

## P2 — fabricated title

`source="semanticscholar", query="Sparse Tensor Routing for Low-Power Federated Learning Zhang Okafor Lindqvist 2022"` returned:

- `totalCount`: 0
- `returned`: 0
- `results`: []

Verdict: clean negative.

## P3 — verifier probes

Coached fixture: `fixtures/draft-with-seeded-defects.md` + `fixtures/research-notes.md`.
Output: `verifier-output.md`; log: `verifier-log.md`.

- D1 wrong year (2019): corrected to 2017
- D2 fabricated paper + 41% + arXiv:2309.99999: removed; arXiv returned "no record"
- D3 GPT-3 95.2% zero-shot TriviaQA: corrected to 64.3% zero-shot / 71.2% few-shot
- D4 dead survey URL + 68%: removed; example.com identified as IANA placeholder
- D5 10x training-cost reduction: softened to the paper's qualitative claim
- V1 multi-head self-attention: retained
- V2 BERT MLM+NSP: retained

Hard fixture: `fixtures/draft-hard.md` + `fixtures/research-notes-hard.md`.
Output: `verifier-hard-output.md`; log: `verifier-hard-log.md`.

- H1 Vaswani 2019 → corrected to 2017
- H2 GPT-3 95.2% → corrected to 64.3%
- H3 10x training cost → removed
- H4 Devlin 2021 → corrected to 2019
- V1/V2 retained

The hard log also records: Crossref returned the `10.65215/*` posted-content records and they were **not used**; Semantic Scholar returned HTTP 429; OpenAlex was noisy; arXiv, NeurIPS proceedings, Crossref, and ACL Anthology agreed on the retained sources.

## P4 — fabricated entity researcher probe

Output: `researcher-nonexistent-output.md`.

- Verdict line: "THE PAPER DOES NOT EXIST."
- 10 sources in the evidence table; no DOI/venue/URL invented.
- Control query `ti:"federated learning"` returned 3 entries, confirming the arXiv endpoint worked.
- DBLP direct API returned HTTP 202 anti-bot challenge; recorded as a soft gap, not a positive hit.
- Explicitly refused to substitute adjacent real papers (DeepReduce, ZeroFL, SpaFL, etc.).

## P5 — reviewer eval-quality probe

Input: `fixtures/mini-eval-paper.md`. Output: `reviewer-eval-output.md`.

Seeded flaws and outcomes:

| Seeded flaw | Reviewer finding |
|---|---|
| 0.2-point gain on 100 examples | W2 FATAL: below design resolution; ~1/20 of one binomial SE |
| 3 seeds, no CI/per-seed | W2/W6 FATAL/MAJOR |
| self-trained baseline, no tuning parity | W4 MAJOR |
| no ablation | W5 MAJOR |
| SOTA claim with no external comparison | W1 FATAL |
| 2x latency with no protocol/confound | W3 FATAL |
| production-adoption recommendation | W11 MINOR |

Additional catch: the reported means 80.1% and 80.3% cannot be means of 3 runs on 100 examples, because each run is k/100 and the mean must be a multiple of 1/300 ≈ 0.333 pp.

## P6 — fetch behavior

- `https://arxiv.org/abs/2309.99999`: returned HTTP-200 page text "There is no record of an article with identifier '2309.99999'."
- `https://example.com/2024-ml-evaluation-survey`: returned the IANA example-domain placeholder text ("This domain is for use in documentation examples without needing permission. This is not a service...").
- `https://doi.org/10.65215/r5bs2d54`: explicit tool error `HTTP 406: Not Acceptable`, with provider fallback advice.

Verdict: explicit transport errors are surfaced correctly; soft-404/placeholder pages are returned as ordinary content and must be read.

## Upstream eval artifacts copied for audit

- `upstream/README.md` — evals/README.md
- `upstream/run.mjs` — evals/run.mjs
- `upstream/questions.jsonl` — 12 fixed questions
- `upstream/claude-opus-q01-q10.jsonl` — one result file with per-question detail
- `upstream/pre-wait-gpt.md`, `upstream/post-wait-gpt.md` — before/after summary tables
- `upstream/crossref-10.65215-r5bs2d54.json` — Crossref record for the zombie DOI
