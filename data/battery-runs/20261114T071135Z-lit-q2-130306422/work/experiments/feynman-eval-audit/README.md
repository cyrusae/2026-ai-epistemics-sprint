# Feynman eval-scorer probe

Synthetic-artifact meta-evaluation of `evals/run.mjs` from
[Companion-Inc/feynman](https://github.com/Companion-Inc/feynman) at commit
`11744290758648c2ecd7c0d6389cdca9ae580290` (package 0.5.69, 2026-11-13).

The point is to test the scorer, not the model: each case is a hand-written
`outputs/<slug>.md` plus (sometimes) a provenance sidecar. The scorer is run
with `--rescore`, exactly as the repo documents.

## Reproduce

```sh
git clone --depth 1 https://github.com/Companion-Inc/feynman.git /tmp/feynman-src
python3 make_fixtures.py
cd /tmp/feynman-src
node evals/run.mjs --rescore /work/experiments/feynman-eval-audit/fixtures.jsonl
```

`--rescore` rewrites the input JSONL in place with score fields and writes
`fixtures.md` next to it. The scored output is committed here as
`fixtures.jsonl` / `fixtures.md`; raw stdout is in `rescore.log`.

## Cases (all use `q01`, test-time compute scaling)

| id | artifact content | expected probe |
|---|---|---|
| `f1-control` | correct claim + correct paper, arXiv URL, exact title | all metrics pass |
| `f2-fake-id` | exact title, fabricated arXiv ID `2408.99999` | `valid` fails, `recall` still passes |
| `f3-irrelevant` | real paper, exact title, unrelated topic | `valid`/`title` pass, `recall` fails |
| `f4-absurd-number` | "improves MATH accuracy by 1000%" + correct citation | all metrics pass |
| `f5-wrong-title` | correct ID, wrong bracketed title, claim text repeats title words | `title` still passes |
| `f6-no-provenance` | correct artifact, no `.provenance.md` sidecar | `done` fails |
| `f7-bare-id` | bare ID `2408.03314`, no exact title, no URL/prefix | `cites` = 0, `recall` = 100% |
| `f8-rejected` | key paper only in a "Rejected sources" list | `recall` = 100% |

## Results

See `fixtures.md` for the generated table and `fixtures.jsonl` for per-case
fields. Summary:

| case | done | cites | valid | title | recall |
|---|---|---|---|---|---|
| f1-control | yes | 1 | 100% | 100% | 100% |
| f2-fake-id | yes | 1 | 0% | - | 100% |
| f3-irrelevant | yes | 1 | 100% | 100% | 0% |
| f4-absurd-number | yes | 1 | 100% | 100% | 100% |
| f5-wrong-title | yes | 1 | 100% | 100% | 100% |
| f6-no-provenance | no | 0 | - | - | 0% |
| f7-bare-id | yes | 0 | - | - | 100% |
| f8-rejected | yes | 1 | 100% | 100% | 100% |

All results are deterministic given the same fixture text and live
arXiv/Crossref responses. Network lookups were available for these runs.

## What this does and does not show

- It confirms documented scope limits: relevance is not checked by
  `valid`/`title`; numeric claims are not checked at all; and recall is string
  presence, not use. The undocumented findings are the title heuristic
  false-positive (surrounding prose satisfies it) and the `cites`/`recall`
  inconsistency for bare IDs. It also shows the process-only `done` gate.
- It does **not** show that any committed model run contains these errors.
  The committed result files do not include the artifacts, so their 44
  citations cannot be inspected from the repo.
