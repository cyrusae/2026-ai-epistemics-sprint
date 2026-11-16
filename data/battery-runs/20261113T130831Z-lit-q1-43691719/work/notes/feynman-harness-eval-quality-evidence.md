# Evidence log: Feynman harness eval-quality case study

Date: 2026-11-13
Canonical artifact: `outputs/feynman-harness-eval-quality-case-study.md`

This log records the raw checks behind the case study. It is not the deliverable.

## Environment

```
$ feynman --version
0.5.65

$ feynman status
Model: openrouter/deepseek/deepseek-v4.1-flash-1017
Model valid: yes
Authenticated models: 348
Authenticated providers: 1
Recommended model: openrouter/openai/gpt-6.1-terra
alphaXiv: not configured
Web access: pi-web-access (Auto)
Service tier: not set
Preview: not configured
Telemetry: off
Sessions: /state/.feynman/sessions
Pi runtime: ready
Pandoc: missing
Browser preview: missing
```

```
$ feynman doctor
alphaXiv auth: missing
supported models: 1592
default model: openrouter/deepseek/deepseek-v4.1-flash-1017
default model valid: yes
authenticated providers: 1
authenticated models: 348
recommended model: openrouter/openai/gpt-6.1-terra
pandoc: missing
browser preview runtime: missing
web access: pi-web-access
pi runtime: ok
```

## E1: published artifact test command

```
$ cd /opt/feynman/feynman-0.5.65-linux-arm64/app && npm test
> @companion-ai/feynman@0.5.65 test
> node --import tsx --import ./tests/isolate-tmpdir.ts --test --test-concurrency=1 tests/*.test.ts

ℹ tests 0
ℹ suites 0
ℹ pass 0
ℹ fail 0
ℹ cancelled 0
ℹ skipped 0
ℹ todo 0
ℹ duration_ms 4.724458
exit=0
```

`tests/` is absent from the installed artifact. `tsx` is a devDependency and is not installed:

```
$ ls -d node_modules/tsx
ls: cannot access 'node_modules/tsx': No such file or directory
```

With a test file present in a temp copy, the command fails:

```
$ cd /tmp/nt && npm test
Error [ERR_MODULE_NOT_FOUND]: Cannot find package 'tsx' imported from /tmp/nt/
...
ℹ tests 1
ℹ pass 0
ℹ fail 1
exit=1
```

The upstream repo does have tests. GitHub contents API for `tests/` lists many files, including `model-harness.test.ts`, `archive-reproducibility.test.ts`, and `npm-provenance.test.ts`.

## E2: verifier probe

Draft (`experiments/verifier-probe/draft.md`):

1. Transformer, Vaswani et al. 2017, arXiv:1706.03762.
2. LoRA, Hu et al. 2021, arXiv:2106.09685, claims 47.3% GPU-memory reduction.
3. Smith et al. 2024, "Scaling laws for retrieval-augmented agents", arXiv:2409.99999, claims 91.2% HotpotQA EM.

Research file (`experiments/verifier-probe/research.md`) supplied only the Transformer source and noted that no source was supplied for the other two claims.

Verifier output (`experiments/verifier-probe/cited.md`):

- kept claim 1 with arXiv URL and OpenAlex W2626778328;
- corrected claim 2 to "3×" with arXiv URL and OpenAlex W3168867926;
- removed claim 3 after arXiv returned no record and OpenAlex found no matching title;
- wrote `experiments/verifier-probe/verification-log.md` with the checks.

This is one run on the session model. It is a demonstration, not a benchmark.

## E3: Crossref false-positive probe

```
feynman_science_database_search(source="crossref", query="10.9999/not.a.real.doi.12345", limit=3)
```

Returned:

```json
{
  "totalCount": 7501524,
  "returned": 3,
  "results": [
    { "doi": "10.1037/t95715-000", "title": "Child-Rearing Scale", ... },
    { "doi": "10.1037/t95714-000", "title": "Feeling Scale for Mothers", ... },
    { "doi": "10.1037/t95710-000", "title": "Victim Cognition Scale for Mothers", ... }
  ]
}
```

`extensions/research-tools/science-databases.ts` `searchCrossref` always calls `/works?query=...`; it does not use `/works/{doi}`.

## E4: arXiv not-found probe

```
feynman_science_database_search(source="arxiv", query="arxiv_get_papers:9999.99999", limit=3)
```

Returned `n_found: 0`, `not_found: ["9999.99999"]`, empty `records`, and provenance with the exact endpoint. No crash, no invented record.

## E5: eval result files

0.5.3 (`evals/results/2026-09-24-lit-0.5.3-ferrylane-openai_gpt-5.6-terra.md`):

| id | done | cites | valid | title | recall | wall | tokens | cost |
|---|---|---|---|---|---|---|---|---|
| q01 | yes | 11 | 100% | 100% | 100% | 652s | 3480101 | $0 |
| q04 | yes | 11 | 100% | 100% | 100% | 628s | 2587943 | $0 |
| q07 | yes | 7 | 100% | 100% | 100% | 578s | 4256526 | $0 |
| q10 | yes | 15 | 100% | 100% | 100% | 650s | 3029227 | $0 |
| all | 100% | 44 | 100% | 100% | 100% | 2508s | 13353797 | $0.00 |

0.5.2 (`evals/results/2026-09-24-lit-ferrylane-openai_gpt-5.6-terra.md`):

| id | done | cites | valid | title | recall | wall | tokens | cost |
|---|---|---|---|---|---|---|---|---|
| q01 | yes | 13 | 100% | 100% | 100% | 711s | 3655492 | $0 |
| q04 | yes | 15 | 100% | 100% | 100% | 816s | 4058278 | $0 |
| q07 | yes | 4 | 100% | 100% | 100% | 566s | 2640763 | $0 |
| q10 | yes | 11 | 100% | 100% | 100% | 713s | 3699383 | $0 |
| all | 100% | 43 | 100% | 100% | 100% | 2806s | 14053916 | $0.00 |

0.5.0 baseline (`evals/results/2026-09-23-lit-ferrylane-openai_claude-sonnet-5.md`):

| id | done | cites | valid | title | recall | wall | tokens | cost |
|---|---|---|---|---|---|---|---|---|
| q01 | yes | 26 | 100% | 92% | 100% | 2188s | 25494037 | $0 |
| q04 | yes | 13 | 100% | 100% | 100% | 443s | 2115102 | $0 |
| q07 | yes | 12 | 100% | 100% | 100% | 2564s | 26551212 | $0 |
| q10 | no | 0 | - | - | 0% | 2700s | 18029830 | $0 |
| all | 75% | 51 | 100% | 97% | 75% | 7895s | 72190181 | $0.00 |

The 0.5.3 JSONL rows include `"git_dirty":true` and `"git_sha":"c1e0b29"`.

## E6: CI audit

The repository has three workflow files:

- `.github/workflows/e2e.yml`
- `.github/workflows/publish.yml`
- `.github/workflows/deploy-website.yml`

`grep -in "eval\|run.mjs\|questions.jsonl"` over all three returned no matches.

`e2e.yml` runs `npm test`, `npm run typecheck`, `npm run build`, `npm run architecture:check`, package-budget checks, consumer installs, and live smoke tests. It does not run `evals/run.mjs`.

## E7: prompt/tool contract

`.feynman/SYSTEM.md`:

> To run several subagents in one call, write the workflow script to `outputs/.plans/<slug>-workflow.js`, and only after that write has succeeded, in a later tool call, call `subagent` with `workflow` set to that path. Do not use `workflow: true`: it needs a fenced block in the visible reply and fails when the block is only in your reasoning.

`node_modules/pi-subagents/docs/workflows.md`:

> `workflow: true` runs the one ```js workflow fenced block written in the same assistant reply as the `subagent` call.

The harness forbids a mode the underlying tool documents as supported. The prohibition may be an intentional workaround, but it is not explained.

## E8: telemetry claims

`RELEASES.md` v0.5.6 (line 404):

> Usage telemetry now carries readable error text ... Paths inside your projects can appear in this text. Prompts, model output, paper content, and tool arguments are still never sent.

`RELEASES.md` v0.5.1 (line 476):

> Prompts, model output, paper content, file paths, and tool arguments are never sent.

`extensions/research-tools/telemetry.ts` sends `error_message` from failed tools and `$ai_error` from failed model calls, with only the home directory redacted. The v0.5.6 note is the accurate one; the v0.5.1 absolute claim is stale.
