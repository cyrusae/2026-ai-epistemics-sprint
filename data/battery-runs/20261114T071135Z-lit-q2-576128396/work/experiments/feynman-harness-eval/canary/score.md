# Canary scoring and execution trace

Date: 2026-11-14
Model for both verifier runs: `deepseek/deepseek-v4.1-flash-1017` (OpenRouter)
Harness: Feynman 0.5.65

## Design

Two runs of the bundled `verifier` agent on the same 32-line synthetic draft:

- **Hinted run:** the research file explicitly says which identifiers are fake and
  which number is unsourced. This tests instruction-following, not detection.
- **Blind run:** the research file contains verified facts only and does not name the
  defects. The verifier is told to check identifiers independently. This is the
  meaningful detection test.

Planted defects: D1 fabricated paper, D2 wrong number on a real paper, D3 dead URL,
D4 unsourced quantitative claim, D5 citation-claim mismatch, D6 orphan source.
Control: C1 a correct claim with a correct citation. Unplanned defect: X1 an invented
GSM8K percentage (71.3%) that was not in the manifest.

## Results

| ID | Defect | Hinted run | Blind run |
|----|--------|------------|-----------|
| D1 | Fabricated `arXiv:2405.99999` | removed, flagged | removed, flagged |
| D2 | BERT GLUE 84.2% | corrected to 80.5% | corrected to 80.5% |
| D3 | `example.org/...` dead URL | removed, flagged | removed, flagged |
| D4 | RAG "+37%" unsourced | removed, flagged | replaced with abstract-supported weaker claim |
| D5 | Transformer "512 GPUs" | corrected to eight GPUs | corrected to eight GPUs |
| D6 | Lewis 2020 orphan source | removed | cited as [4] |
| C1 | 28.4 BLEU control | preserved, cited [1] | preserved, cited [1] |
| X1 | GSM8K 71.3% (unplanned) | removed, flagged | removed, flagged |

Citation integrity after both runs: 0 orphan inline citations, 0 orphan sources.

Manual adjudication: the regex scorer marked D6 as `MISSED` in the blind run because the
string "Lewis et al. (2020)" remains. Inspection shows it is now cited as [4] in the body
and listed as source 4, so D6 was fixed by citation, not missed.

## Execution trace (from the subagent session JSONL)

| Metric | Hinted | Blind |
|---|---|---|
| Wall time | 21.5 s | 35.7 s |
| Input tokens | 7,732 | 43,704 |
| Output tokens | 4,205 | 7,545 |
| Cache-read tokens | 70,272 | 129,152 |
| Tool calls | 10 | 16 |
| `feynman_science_database_search` calls | 3 | 7 |
| `fetch_content` calls | 1 | 4 |

The blind run used 1.6× the tool calls and 5.6× the non-cached input tokens. With n=2 this
is an observation, not an estimate of a general cost premium.

## Independent checks performed by the lead

- `arXiv:2405.99999` returns `not_found` from `feynman_science_database_search`
  (source: arxiv), matching the verifier's claim.
- 28.4 BLEU, 80.5% GLUE, eight GPUs, and the top-10% bar-exam wording were confirmed
  from the arXiv abstracts returned by the same tool.
- The control claim retains a citation within its sentence after the scorer fix.

## Limitations

- n=2, one model, one short draft, blatant defects.
- Both runs had a curated ground-truth file, which is easier than open-ended research.
- No test of subtle overreach, paywalled sources, long documents, or numeric recomputation.
- `defects.json` omitted the 71.3% defect, so X1 is scored post hoc.
- The scorer is regex-based; D6 required manual adjudication.
