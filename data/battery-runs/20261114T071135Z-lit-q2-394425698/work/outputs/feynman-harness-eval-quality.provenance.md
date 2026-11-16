# Provenance: Feynman harness case study (AI-eval-quality lens)

- **Date:** 2026-11-14 (UTC)
- **Subject:** `@companion-ai/feynman` 0.5.65, Node v24.21.0
- **Rounds:** 1 literature round; 2 verifier-probe rounds; 1 retrieval-probe round
- **Sources consulted:** 17 distinct arXiv IDs queried (16 accepted, 1 dropped),
  5 Semantic Scholar queries, 1 OpenAlex fallback query, 2 OpenAlex work lookups,
  2 web searches, 6 local harness files/dirs (`SYSTEM.md`, `.feynman/agents/`,
  `prompts/`, `extensions/research-tools/`, `RELEASES.md`, `package.json`)
- **Sources accepted:** 17 in the Sources section, plus local harness artifacts
- **Sources rejected:** 1 misremembered ID (2410.18982 was recalled as "LitSearch"
  but resolves to "O1 Replication Journey"; dropped), plus irrelevant retrieval
  hits (NER, KG construction, a Dostoevsky Journal "Conference Papers" record,
  a clinical-diagnosis paper)
- **Verification:** **PASS WITH NOTES**
  - Citation metadata (title/year/first author) batch-verified by arXiv lookup: verified
  - All eight final probe URLs returned HTTP 200 on 2026-11-14: verified by `curl -L`
  - Probe outputs scored against pre-written oracles: done (`experiments/verifier-probe/results.md`)
  - Verifier's self-reported OpenAlex records W7197047848 and W4416268504: independently re-queried and confirmed
  - `reviewer` agent behavioural test: **not run**
  - Multi-model / multi-run reliability: **not run**
  - Retrieval probe relevance judgments: single unblinded rater, **n=5 queries**
- **Plan:** `outputs/.plans/feynman-harness-eval-quality.md`
- **Research files:** this provenance; `experiments/verifier-probe/`; `experiments/retrieval-probe/`
- **Final artifact:** `outputs/feynman-harness-eval-quality.md`

## Notes

- Probe 1 was designed with the correct answers present in `sources.md`; that
  confound is disclosed in the artifact and was addressed by Probe 2, which used
  a deliberately empty research file.
- Neither probe run appears in the final artifact with model/cost metadata by
  default; those values were recovered from the child `session.jsonl` files and
  are reported in `experiments/verifier-probe/results.md`.
- The harness did not produce this provenance file; it was written by the lead
  agent. That is itself one of the findings.
