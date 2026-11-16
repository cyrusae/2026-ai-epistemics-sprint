# Battery analysis: 15 `lit-q*` sandbox runs (prompt p1 / p1-b, + one p2 follow-up)

Pipeline (run from this folder; `corpus/ packets/ coders/ derived/ ref/` are gitignored):

```sh
# 1. per-run corpora (reuses the exhibit renderer; entry ids L0001, V1-0001, ...)
for r in ../../sandbox/runs/*lit-q*; do n=$(basename $r | sed -E 's/.*-(lit-q[12])-([0-9]+)$/\1-\2/')
  python3 -I ../exhibit/build_corpus.py $(ls $r/state/.feynman/sessions/*.jsonl | head -1) corpus/$n; done
# 2. scripted facts (no judgement): derived/facts.md, files/harness_reads/executions/keywords .tsv
python3 -I facts.py ../../sandbox/runs 'lit-q*' derived
# 3. Feynman source at v0.5.65 (README + evals/) for the feature-anchoring comparison
git clone --filter=blob:none --no-checkout https://github.com/Companion-Inc/feynman.git ref/feynman-src
(cd ref/feynman-src && git sparse-checkout set evals && git checkout v0.5.65)
# 4. one read-only packet per run: PROMPTS.md, design/ (work/), transcript/, reference/, FACTS.md, MANIFEST.txt
python3 -I make_packets.py ../../sandbox/runs 'lit-q*' corpus ref/feynman-src packets
for d in packets/*/; do (cd $d && find . -type f | sed 's#^\./##' | sort | while read f; do printf "%8s  %s\n" $(wc -c < "$f") "$f"; done > MANIFEST.txt); done
# 5. coders -> coders/<coder>__<task>__<run>.json
xargs -P 4 -L 1 ./run_agy.sh < derived/agy-jobs.txt     # Gemini (agy), task battery|rubric
#    Claude coders: Agent subagents reading packets/<run>/ only (son = Sonnet battery, hai = Haiku rubric)
# 6. quote check + merge -> derived/battery.md, derived/rubric.md
python3 -I verify.py
```

- `prompts/battery.md`: the qualitative battery (12 dimensions: observation / quoted evidence / draft interpretation), plus free `notable` items. Draft interpretations are for the researcher to accept or overwrite.
- `prompts/rubric.md`: the pre-registered rubric items (I1–I3, R1–R4, C1, S1) verbatim from `poke-with-stick.md` §4, **without** the hypothesis or predictions. Coders see only `design/` + `PROMPTS.md`.
- Blinding: coders get a copy of one packet (Gemini runs in a temp dir; Claude subagents are told to read only that packet). None see `poke-with-stick.md`.
- Workflow detection (`facts.py`): no run loaded a skill/prompt template with the `read` tool; all read harness files via bash (`cat`/`sed`), which in this design can be research, not invocation. `workflows` = file signature of a shipped template present in `work/`.
- Keyword spot checks (`derived/keywords.tsv`): regexes over thinking + replies of all sessions. "Feynman" is the topic, so read the context column.

## Timelines

```sh
python3 -I timeline.py corpus derived                     # derived/timeline.tsv (every call/session), derived/timing.tsv (per turn)
uv run -q --with matplotlib python plot_timeline.py derived/timeline.tsv derived/timeline   # static .pdf/.png for the paper
python3 -I build_timeline_page.py corpus derived/timeline.tsv derived/timing.tsv timeline_template.html derived/timeline.html
```
Model call = assistant message, `timestamp` (request start) + `durationMs`. Tool call = toolResult timestamp − `durationMs`. Time 0 = the human's message for that turn.

## Coder results (first pass, 2026-11-14)

Two coders per task (battery: Gemini 3.8 Flash + Sonnet; rubric: Gemini + Haiku). Quote checks: Sonnet 388/394 found, Haiku 184/184, Gemini ~88% (40 rejected on battery). Gemini picks the most favourable value on nearly every battery dimension; Sonnet discriminates more. Biggest disagreement: `warrant` (Gemini "grounded" 14/15, Sonnet "assumed" 15/15), a definitional question for the researcher.
