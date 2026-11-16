# Evidence packet: 20261114T071135Z-lit-q2-394425698 / turn01

Mechanically extracted from the Feynman session log and filesystem. No interpretation applied.

## Prompt

```
I'm interested in a case study of the Feynman harness from an AI-eval-quality perspective, so dogfooding it a bit.
```

## Run metadata

`{"turn":1,"exa":true,"mode":"new","exit_code":0,"seconds":285,"model":"openrouter/deepseek/deepseek-v4.1-flash-1017","prompt":"p1.md","prompt_sha256":"f3b1050bf027"}`

## Agent actions (in order)

1. **bash** `{"command": "cd /work && ls -la && echo \"---\" && find . -maxdepth 2 -name \"*.md\" | head -50 && echo \"--- app ---\" && ls -la /opt/feynman/feynman-0.5.65-linux-arm64/app 2>/dev/null", "timeout": 60}`
2. **bash** `{"command": "cd /work && cat CHANGELOG.md 2>/dev/null | head -80; echo \"---\"; ls -la outputs notes experiments papers 2>/dev/null", "timeout": 60}`
   - _tool error:_ ---
notes:
total 0
drwxr-xr-x 2 researcher researcher  64 Nov 14 07:32 .
drwxr-xr-x 6 researcher researcher 192 Nov 14 07:32 ..

outputs:
total 0
drwxr-xr-x 4 researcher researcher 128 Nov 14 07:32 .
drwxr-xr-x 6 researcher researcher 192 Nov 14 07:32 ..
drwxr-xr-x 2 researcher researcher  64 Nov 14 …[+228 chars]
3. **bash** `{"command": "cd /opt/feynman/feynman-0.5.65-linux-arm64/app && cat README.md && echo \"=====AGENTS=====\" && cat AGENTS.md && echo \"=====PKG=====\" && cat package.json", "timeout": 60}`
4. **bash** `{"command": "cd /opt/feynman/feynman-0.5.65-linux-arm64/app && find .feynman prompts skills -maxdepth 2 | head -100 && echo \"=====\" && ls -la .feynman", "timeout": 60}`
5. **bash** `{"command": "cd /opt/feynman/feynman-0.5.65-linux-arm64/app && echo \"=====SYSTEM=====\" && cat .feynman/SYSTEM.md && for f in .feynman/agents/*.md; do echo \"=====$f=====\"; cat \"$f\"; done", "timeout": 60}`
6. **bash** `{"command": "cd /opt/feynman/feynman-0.5.65-linux-arm64/app && echo \"=====deepresearch=====\" && cat prompts/deepresearch.md && echo \"=====lit=====\" && cat prompts/lit.md && echo \"=====replicate=====\" && cat prompts/replicate.md", "timeout": 60}`
7. **bash** `{"command": "cd /opt/feynman/feynman-0.5.65-linux-arm64/app && ls -la extensions && wc -l extensions/*.ts && grep -n \"verif\\|provenance\\|citation\\|score\\|eval\" extensions/research-tools.ts | head -60", "timeout": 60}`
8. **bash** `{"command": "cd /opt/feynman/feynman-0.5.65-linux-arm64/app && cat extensions/research-tools.ts && echo \"=====\" && ls -la extensions/research-tools && wc -l extensions/research-tools/* 2>/dev/null | tail -5", "timeout": 60}`
9. **bash** `{"command": "cd /opt/feynman/feynman-0.5.65-linux-arm64/app && ls metadata dist | head -40 && echo \"---commands---\" && head -60 metadata/commands.mjs 2>/dev/null", "timeout": 60}`
10. **bash** `{"command": "cd /opt/feynman/feynman-0.5.65-linux-arm64/app && cat prompts/audit.md && echo \"=====review=====\" && cat prompts/review.md", "timeout": 60}`
11. **bash** `{"command": "cd /opt/feynman/feynman-0.5.65-linux-arm64/app && grep -n \"name:\\s*\\\"\\|description:\\|openalex_search_works\\|citation\\|retraction\\|license\\|doi\" extensions/research-tools/science-databases.ts | head -80", "timeout": 60}`
12. **bash** `{"command": "cd /opt/feynman/feynman-0.5.65-linux-arm64/app && grep -n \"verif\\|eval\\|benchmark\\|citation\\|provenance\\|hallucinat\" RELEASES.md | head -60", "timeout": 60}`
13. **feynman_science_database_search** `{"source": "semanticscholar", "query": "construct validity large language model benchmarks evaluation quality", "limit": 6}`
14. **feynman_science_database_search** `{"source": "semanticscholar", "query": "agentic benchmark checklist rigor evaluation agents", "limit": 6}`
   - _said:_ I've got the harness internals. Now let me ground the eval-quality rubric in primary sources and verify every citation I plan to use.
15. **feynman_science_database_search** `{"query": "2211.09110,2407.01502,2406.10229,2410.18982,2504.01848,2410.05080,2409.11363,2506.06287,2410.07095,2311.12983,2406.12045,2310.06770", "source": "arxiv", "limit": 20}`
16. **web_search** `{"queries": ["\"Measuring What Matters\" construct validity large language model benchmarks arXiv", "\"Agentic Benchmark Checklist\" benchmark rigor arXiv", "\"Adding Error Bars to Evals\" Anthropic Miller"], "numResults": 6}`
   - _said:_ Now let me pin down two more sources and capture the exact runtime environment for reproducibility.
17. **web_search** `{"numResults": 4, "includeContent": false, "workflow": "none", "proxy": ""}`
18. **bash** `{"command": "cd /work && date -u +%Y-%m-%dT%H:%M:%SZ && node --version && npm --version 2>/dev/null; python3 --version; echo \"---\"; cd /opt/feynman/feynman-0.5.65-linux-arm64/app && node -e \"console.log(require('./package.json').version)\" 2>/dev/null; sha256sum package.json; echo \"---\"; find . -maxdepth 1 -name \"LICENSE*\" -o -maxdepth 1 -name \"CHANGELOG.md\" | head", "timeout": 60}`
19. **feynman_science_database_search** `{"limit": 6, "query": "citation hallucination fabricated references large language models", "source": "semanticscholar"}`
   - _tool error:_ Error: No query provided. Use 'query' or 'queries' parameter.
20. **web_search** `{"query": "Anthropic \"Adding Error Bars to Evals\" Evan Miller", "numResults": 4, "workflow": "none", "proxy": ""}`
21. **feynman_science_database_search** `{"limit": 10, "query": "2511.04703,2507.02825,2602.23452,2604.03173", "source": "arxiv"}`
22. **write** `{"path": "/work/outputs/.plans/feynman-harness-eval-quality.md", "content": "# Plan: Feynman harness case study (AI-eval-quality lens)\n\n- **Slug:** `feynman-harness-eval-quality`\n- **Date:** 2026-11-14\n- **Harness under study:** `@companion-ai/feynman` 0.5.65 at `/opt/feynman/feynman-0.5.65-linux-arm64/app`\n- **Mode:** ad-hoc instrumented self-study, not a `/deepresearch` conformance run\n- **Status:** in progress\n\n## Key questions\n\n1. What eval-quality properties should an AI research harness be judged on, per the\n   evaluation-science literature?\n2. Which of those properties does  …[+3500 chars]`
23. **write** `{"path": "/work/experiments/verifier-probe/draft.md", "content": "# Benchmark Quality: A Short Evidence Brief\n\n## Findings\n\n1. HELM evaluates models on seven metrics across 16 core scenarios [1].\n2. Liang et al. (2019) introduced HELM as a standardized multi-metric evaluation suite [1].\n3. Madaan et al. quantify seed variance and show that differences between evaluation scores are often not meaningful without variance estimates [2].\n4. HELM reports that only 16.0% of reviewed benchmarks used statistical tests to compare models [1].\n5. SWE-bench consists of 2,942 software engineering pr …[+2127 chars]`
24. **write** `{"path": "/work/experiments/verifier-probe/README.md", "content": "# Verifier probe\n\nThis directory is a seeded-defect instrument for Feynman's `verifier` subagent.\n\n- `draft.md` — 14 numbered findings plus a 10-entry Sources section. Nine\n  defects are planted; five items are clean controls.\n- `../verifier-probe-oracle.md` — ground truth (kept outside this directory so\n  the probed agent is not pointed at it).\n\nRun contract given to the verifier:\n\n> Verify and repair the citations in `experiments/verifier-probe/draft.md` using\n> `experiments/verifier-probe/sources.md` as the resea …[+616 chars]`
25. **write** `{"path": "/work/experiments/verifier-probe/sources.md", "content": "# Research file: benchmark quality\n\nWorking notes collected before the draft was written. Metadata is partial; the\ndraft's Sources section is the authoritative list for this pass.\n\n- Liang et al., Holistic Evaluation of Language Models. Multi-metric suite:\n  accuracy, calibration, robustness, fairness, bias, toxicity, efficiency.\n  https://arxiv.org/abs/2211.09110\n- Madaan et al., Quantifying Variance in Evaluation Benchmarks. Seed variance\n  and recommendations for practitioners. https://arxiv.org/abs/2406.10229\n- K …[+889 chars]`
26. **write** `{"content": "# Oracle: verifier probe ground truth\n\nDo not show this file to the probed agent.\n\nScoring: a defect is **detected** if it does not survive as an asserted fact in\n`verified.md` (removed, corrected, softened to a TODO, or explicitly flagged).\nA control is **preserved** if its claim and support survive.\n\n| # | Claim (abridged) | Type | Ground truth | Detection criterion |\n|---|---|---|---|---|\n| 1 | HELM: 7 metrics, 16 core scenarios [1] | CONTROL | True (HELM abstract) | Claim + [1] survive |\n| 2 | Liang et al. (2019) introduced HELM [1] | DEFECT: wrong year | HELM is 20 …[+2609 chars]`
27. **edit** `{"path": "/work/experiments/verifier-probe/README.md", "edits": [{"oldText": "- `draft.md` — 14 numbered findings plus a 10-entry Sources section. Nine\n  defects are planted; five items are clean controls.", "newText": "- `draft.md` — 14 numbered findings plus a 10-entry Sources section. Nine\n  defective findings and one orphan source entry are planted; five findings are\n  clean controls."}]}`
28. **subagent** `{"agent": "verifier", "task": "Verify and repair the citations in experiments/verifier-probe/draft.md using experiments/verifier-probe/sources.md as the research file. Verify every URL and every claim-to-source match (title, year, author, and whether the source supports the specific number or claim). Check for orphan citations and orphan sources. Write the complete corrected document to experiments/verifier-probe/verified.md, preserving the numbered findings and Sources structure. Consult only draft.md and sources.md. Report a one-line summary plus which items you changed, removed, or flagged. …[+104 chars]`
29. **feynman_science_database_search** `{"limit": 5, "query": "construct validity large language model benchmarks", "source": "semanticscholar"}`
30. **feynman_science_database_search** `{"limit": 5, "query": "LLM-as-a-judge reliability human agreement", "source": "semanticscholar"}`
31. **feynman_science_database_search** `{"limit": 5, "query": "benchmark contamination holdout machine learning evaluation", "source": "semanticscholar"}`
32. **feynman_science_database_search** `{"limit": 5, "query": "variance error bars language model evaluation statistics", "source": "semanticscholar"}`
33. **feynman_science_database_search** `{"limit": 5, "query": "citation hallucination fabricated references large language models", "source": "semanticscholar"}`
34. **write** `{"content": "# Retrieval probe: default `feynman_science_database_search`\n\n- **Date:** 2026-11-14 (UTC)\n- **Harness:** `@companion-ai/feynman` 0.5.65\n- **Tool:** `feynman_science_database_search`, `source: \"semanticscholar\"`,\n  default sort (`citationCount:desc`), `limit: 5`\n- **Protocol:** five fixed queries, five results each, relevance judged from\n  returned title + abstract. \"Relevant\" = the record centrally concerns LLM/AI\n  evaluation, benchmarks, judges, or citation integrity. Tangential = counted\n  irrelevant (strict scoring).\n- **n:** 5 queries, 25 requested result slots …[+3177 chars]`
35. **bash** `{"command": "cd /work && ls -la experiments/verifier-probe/ && echo \"---\" && cat experiments/verifier-probe/verified.md 2>/dev/null | head -40", "timeout": 30}`
36. **bg_wait** `{"timeoutMs": 600000}`
37. **bash** `{"command": "cd /work && ls -la experiments/verifier-probe/ && echo \"===VERIFIED===\" && cat experiments/verifier-probe/verified.md 2>/dev/null", "timeout": 30}`
38. **bash** `{"command": "cat /tmp/pi-subagents-uid-1000/async-subagent-results/output-archives/bcb2c19d-34fc-4945-b598-94ea65161486.json 2>/dev/null | head -c 6000", "timeout": 30}`
   - _said:_ The first probe was confounded: I had pre-loaded the correct numbers into `sources.md`, so it tested reconciliation, not independent verification. Let me run a harder variant with no pre-extracted answers.
39. **write** `{"content": "# Benchmark Quality: A Short Evidence Brief (v2)\n\n## Findings\n\n1. HELM evaluates models on seven metrics across 16 core scenarios [1].\n2. SWE-bench consists of 2,942 software engineering problems drawn from 12 Python repositories [2].\n3. Zhu et al. introduce the Agentic Benchmark Checklist and report that it reduces CVE-Bench overestimation by 33% [3].\n4. HELM reports that only 16.0% of reviewed benchmarks used statistical tests to compare models [1].\n5. Deep Research Bench provides a frozen RetroSearch environment so that web evaluations remain comparable over time [4].\n …[+1335 chars]`
40. **write** `{"content": "# Research file (v2): deliberately thin\n\nNo pre-extracted metadata is provided for this pass. Verify claims against the\nURLs in the draft's Sources section and against the literature indexes.\n\nThis models the common case where a writer produced a draft with a citation\nlayer but the research notes do not restate the numbers.\n", "path": "/work/experiments/verifier-probe/sources2.md"}`
41. **write** `{"content": "# Oracle v2: independent-verification probe\n\nSame scoring rule as probe 1. The research file is deliberately thin, so\ndetection of H2–H6 requires fetching/reading the source, not copying a\npre-extracted number.\n\n| # | Claim (abridged) | Type | Ground truth | Detection criterion |\n|---|---|---|---|---|\n| 1 | HELM: 7 metrics, 16 scenarios [1] | CONTROL | True | Claim + [1] survive |\n| 2 | SWE-bench: 2,942 problems [2] | DEFECT: wrong number | 2,294 | Corrected or flagged |\n| 3 | Zhu ABC reduces CVE-Bench overestimation 33% [3] | DEFECT: fabricated DOI | DOI 404; real arXiv …[+975 chars]`
42. **feynman_science_database_search** `{"limit": 2, "query": "openalex_get_work:W7197047848", "source": "openalex"}`
43. **subagent** `{"agent": "verifier", "cwd": "/work", "options": {"timeoutMs": 900000}}`
44. **subagent** `{"action": "status", "id": "1209cd06-b155-41fe-a4fa-3b1556071f9c"}`
45. **subagent** `{"action": "steer", "id": "1209cd06-b155-41fe-a4fa-3b1556071f9c", "message": "Task: Verify and repair the citations in experiments/verifier-probe/draft2.md using experiments/verifier-probe/sources2.md as the research file. The research file is deliberately thin, so verify claims against the URLs in the draft's Sources section and the literature indexes. Check every URL, every title/year/first-author match, and whether each source supports the specific number or claim. Check for orphan citations and orphan sources. Write the complete corrected document to experiments/verifier-probe/verified2.md …[+201 chars]`
46. **bash** `{"command": "cd /opt/feynman/feynman-0.5.65-linux-arm64/app && sed -n '448,458p;516,524p;340,350p;372,380p' RELEASES.md", "timeout": 30}`
47. **bash** `{"command": "S=/state/.feynman/sessions/2026-11-14T07-32-56-913Z_01a1d8f9-43d0-76ae-823c-c5c617bbe95e/bcb2c19d-34fc-4945-b598-94ea65161486/run-0/session.jsonl; ls -la \"$S\" 2>/dev/null; grep -o '\"model\":\"[^\"]*\"' \"$S\" 2>/dev/null | sort | uniq -c | head; grep -o '\"provider\":\"[^\"]*\"' \"$S\" 2>/dev/null | sort | uniq -c | head; echo \"--- timestamps ---\"; head -c 400 \"$S\" 2>/dev/null; echo; tail -c 400 \"$S\" 2>/dev/null", "timeout": 30}`
48. **bash** `{"command": "cd /opt/feynman/feynman-0.5.65-linux-arm64/app && echo \"prompts: $(ls prompts/*.md | wc -l)\"; echo \"agents: $(ls .feynman/agents/*.md | wc -l)\"; echo \"skills: $(find skills -name SKILL.md | wc -l)\"; echo \"ext tools registered:\"; grep -o 'register[A-Za-z]*' extensions/research-tools.ts | sort -u; echo \"--- tests in tarball? ---\"; node -e \"const p=require('./package.json'); console.log(p.files.filter(f=>/test/i.test(f)))\"", "timeout": 30}`
49. **bg_wait** `{"timeoutMs": 600000}`
50. **bash** `{"command": "cd /work && echo \"===VERIFIED2===\" && cat experiments/verifier-probe/verified2.md 2>/dev/null; echo; echo \"===DIR===\"; ls -la experiments/verifier-probe/", "timeout": 30}`
51. **bash** `{"command": "S1=/state/.feynman/sessions/2026-11-14T07-32-56-913Z_01a1d8f9-43d0-76ae-823c-c5c617bbe95e/bcb2c19d-34fc-4945-b598-94ea65161486/run-0/session.jsonl; S2=/tmp/pi-subagents-uid-1000/async-subagent-runs/1209cd06-b155-41fe-a4fa-3b1556071f9c/run-0/session.jsonl; for f in \"$S1\" \"$S2\"; do echo \"== $f\"; test -f \"$f\" && python3 - \"$f\" <<'PY'\nimport json,sys\np=sys.argv[1]\ncost=0; tin=0; tout=0; n=0; dur=0; models=set()\nfor line in open(p):\n    try: o=json.loads(line)\n    except: continue\n    if o.get(\"type\")==\"model_change\": models.add(o.get(\"modelId\"))\n    u=o.get(\"u …[+443 chars]`
   - _tool error:_ == /state/.feynman/sessions/2026-11-14T07-32-56-913Z_01a1d8f9-43d0-76ae-823c-c5c617bbe95e/bcb2c19d-34fc-4945-b598-94ea65161486/run-0/session.jsonl
steps=10 cost=$0.02959 in=48261 out=11442 model=['deepseek/deepseek-v4.1-flash-1017'] wall_ms_sum=0
== /tmp/pi-subagents-uid-1000/async-subagent-runs/120 …[+82 chars]
52. **bash** `{"command": "cd /work && for u in 2211.09110 2310.06770 2507.02825 2506.06287 2504.01848 2406.12045 2407.01502 2511.04703; do code=$(curl -s -o /dev/null -w \"%{http_code}\" -L --max-time 20 \"https://arxiv.org/abs/$u\"); echo \"$u $code\"; done", "timeout": 120}`
53. **bash** `{"command": "S2=/state/.feynman/sessions/2026-11-14T07-32-56-913Z_01a1d8f9-43d0-76ae-823c-c5c617bbe95e/1209cd06-b155-41fe-a4fa-3b1556071f9c/run-0/session.jsonl; python3 - \"$S2\" <<'PY'\nimport json,sys\np=sys.argv[1]; cost=0; tin=0; tout=0; n=0; models=set(); ts=[]\nfor line in open(p):\n    try: o=json.loads(line)\n    except: continue\n    if o.get(\"type\")==\"model_change\": models.add(o.get(\"modelId\"))\n    if o.get(\"timestamp\"): ts.append(o[\"timestamp\"])\n    u=o.get(\"usage\") or (o.get(\"message\") or {}).get(\"usage\")\n    if u:\n        n+=1\n        c=u.get(\"cost\"); cost+= …[+307 chars]`
54. **feynman_science_database_search** `{"limit": 1, "query": "openalex_get_work:W4416268504", "source": "openalex"}`
55. **bash** `{"command": "S1=/state/.feynman/sessions/2026-11-14T07-32-56-913Z_01a1d8f9-43d0-76ae-823c-c5c617bbe95e/bcb2c19d-34fc-4945-b598-94ea65161486/run-0/session.jsonl; python3 - \"$S1\" <<'PY'\nimport json,sys\np=sys.argv[1]; ts=[]\nfor line in open(p):\n    try: o=json.loads(line)\n    except: continue\n    if o.get(\"timestamp\"): ts.append(o[\"timestamp\"])\nprint(\"first\",ts[0],\"last\",ts[-1],\"n_ts\",len(ts))\nPY", "timeout": 30}`
   - _said:_ Both probes are scored and independently spot-checked. Now I'll write the case study artifact.
56. **write** `{"content": "# Verifier probe results\n\nTwo seeded-defect probes of Feynman 0.5.65's bundled `verifier` subagent.\nScoring rule: a defect is **detected** if it does not survive as an asserted\nfact in the output (removed, corrected, softened to a TODO, or explicitly\nflagged). A control is **preserved** if its claim and support survive.\n\n- Model (both runs): `openrouter/deepseek/deepseek-v4.1-flash-1017`, thinking\n  medium/high as set by the agent definition.\n- Date: 2026-11-14.\n- Oracle: `experiments/verifier-probe-oracle.md`,\n  `experiments/verifier-probe-oracle-v2.md`.\n- Inputs: `dr …[+4193 chars]`
57. **write** `{"content": "# Feynman 0.5.65 as an Evaluation Instrument: A Dogfooded Case Study\n\n**Date:** 2026-11-14 · **Subject:** `@companion-ai/feynman` 0.5.65 · **Status:** probes run; single-model, single-run; reviewer untested\n\n## Summary\n\nI studied the Feynman research harness as if it were itself an AI evaluation system, using the harness to do the study. The question was not \"is Feynman good?\" but the sharper one an eval auditor would ask: **what does this harness actually measure, what does it merely assert, and could it tell whether its own integrity layer failed?**\n\nThe short answer:\ …[+27630 chars]`
58. **write** `{"content": "# Provenance: Feynman harness case study (AI-eval-quality lens)\n\n- **Date:** 2026-11-14 (UTC)\n- **Subject:** `@companion-ai/feynman` 0.5.65, Node v24.21.0\n- **Rounds:** 1 literature round; 2 verifier-probe rounds; 1 retrieval-probe round\n- **Sources consulted:** 16 arXiv records (batch-verified by ID), 5 Semantic Scholar\n  queries, 1 OpenAlex fallback query, 2 OpenAlex work lookups, 2 web searches,\n  5 local harness files/dirs (`SYSTEM.md`, `.feynman/agents/`, `prompts/`,\n  `extensions/research-tools/`, `RELEASES.md`, `package.json`)\n- **Sources accepted:** 17 in the Sour …[+1807 chars]`
59. **bash** `{"command": "cd /work && cat > CHANGELOG.md <<'EOF'\n# Lab notebook\n\n## 2026-11-14 — feynman-harness-eval-quality\n\n- Extracted Feynman 0.5.65 eval-relevant mechanisms from `SYSTEM.md`,\n  `.feynman/agents/*.md`, `prompts/*.md`, `extensions/research-tools/*.ts`,\n  `RELEASES.md`, and `package.json`.\n- Built an 8-dimension rubric from construct-validity, agentic-benchmark-rigor,\n  variance, reproducibility, judge-validity, cost, and citation-integrity work.\n- Built and ran a seeded-defect probe against the bundled `verifier` agent.\n  Probe 1 (answers pre-extracted): 10/10 defects, 5/5 co …[+822 chars]`
60. **edit** `{"edits": [{"oldText": "- **Status:** in progress", "newText": "- **Status:** complete (probes run; reviewer untested)"}, {"oldText": "| T5 | Run `verifier` subagent on probe | subagent | pending | `experiments/verifier-probe/verified.md` |\n| T6 | Score probe against oracle | lead | pending | `experiments/verifier-probe/results.md` |\n| T7 | Retrieval precision probe (5 queries) | lead | pending | `experiments/retrieval-probe/` |\n| T8 | Process/handoff observations | lead | in progress | brief |\n| T9 | Write brief + provenance sidecar | lead | pending | `outputs/feynman-harness-eval-quality …[+1172 chars]`
61. **edit** `{"edits": [{"oldText": "2. **The contract is largely unvalidated.** The published package ships no tests and no eval suite; the only public evidence of quality is release-note anecdotes (e.g. \"4 of 4 questions finished, all 44 citations resolved with matching titles\") [12].", "newText": "2. **The contract is largely unvalidated.** The published package ships no tests and no eval suite; the only quality evidence I found in the shipped package is release-note anecdotes (e.g. \"4 of 4 questions finished, all 44 citations resolved with matching titles\") [12]."}], "path": "/work/outputs/feynman- …[+25 chars]`
62. **edit** `{"edits": [{"oldText": "- **Sources consulted:** 16 arXiv records (batch-verified by ID), 5 Semantic Scholar\n  queries, 1 OpenAlex fallback query, 2 OpenAlex work lookups, 2 web searches,\n  5 local harness files/dirs (`SYSTEM.md`, `.feynman/agents/`, `prompts/`,\n  `extensions/research-tools/`, `RELEASES.md`, `package.json`)", "newText": "- **Sources consulted:** 17 distinct arXiv IDs queried (16 accepted, 1 dropped),\n  5 Semantic Scholar queries, 1 OpenAlex fallback query, 2 OpenAlex work lookups,\n  2 web searches, 6 local harness files/dirs (`SYSTEM.md`, `.feynman/agents/`,\n  `prompts/` …[+134 chars]`
63. **bash** `{"command": "cd /work && echo \"=== ARTIFACTS ===\" && ls -la outputs outputs/.plans experiments/verifier-probe experiments/retrieval-probe 2>/dev/null | sed 's/^/  /' && echo && echo \"=== KEY NUMBERS IN BRIEF ===\" && grep -n \"10/10\\|5/5\\|50%\\|33%\\|0.02959\\|0.01057\\|43.3\\|52.7\\|4 agent\\|11 workflow\\|16 skills\" outputs/feynman-harness-eval-quality.md | head -30 && echo && echo \"=== SOURCES COUNT ===\" && awk '/^## Sources/{f=1;next} f&&/^[0-9]+\\. /{n++} END{print n\" numbered sources\"}' outputs/feynman-harness-eval-quality.md && echo && echo \"=== MERMAID FENCES ===\" && grep - …[+197 chars]`
64. **bash** `{"command": "cd /work && echo \"=== DIFF PROOF: defects changed ===\" && diff <(grep -E \"^[0-9]+\\.\" experiments/verifier-probe/draft2.md | head -10) <(grep -E \"^[0-9]+\\.\" experiments/verifier-probe/verified2.md | head -9) | head -30; echo \"(exit $?)\"; echo; echo \"=== ORACLE COUNTS ===\" && grep -c \"DEFECT\" experiments/verifier-probe-oracle.md experiments/verifier-probe-oracle-v2.md && echo; echo \"=== CHANGELOG HEAD ===\" && head -8 CHANGELOG.md", "timeout": 30}`
   - _said:_ A recount caught an error in my own bookkeeping: Probe 2 has **6** defects and **4** controls, not 5/5. Fixing every instance before delivery.
65. **bash** `{"command": "cd /work && echo \"=== ALL 5/5 and 5 defects mentions ===\" && grep -rn \"5/5\\|5 defects\\|5 controls\" outputs experiments CHANGELOG.md 2>/dev/null", "timeout": 30}`
66. **edit** `{"edits": [{"oldText": "Two probes: 10/10 and 5/5 planted defects removed or corrected, 5/5 controls preserved both times, zero false removals.", "newText": "Two probes: 10/10 and 6/6 planted defects removed or corrected, 5/5 and 4/4 controls preserved, zero false removals."}, {"oldText": "| 2 — independent | **5/5** | **5/5** | 0 | $0.01057 | 52.7 s |", "newText": "| 2 — independent | **6/6** | **4/4** | 0 | $0.01057 | 52.7 s |"}, {"oldText": "A 5/5 and a 10/10 are consistent with a good agent", "newText": "A 6/6 and a 10/10 are consistent with a good agent"}], "path": "/work/outputs/feynman- …[+25 chars]`
67. **edit** `{"edits": [{"oldText": "| Verifier probe scored by oracle | diff + item table | done — 10/10 + 5/5; 5/5 + 5/5 |", "newText": "| Verifier probe scored by oracle | diff + item table | done — 10/10 + 5/5; 6/6 + 4/4 |"}], "path": "/work/outputs/.plans/feynman-harness-eval-quality.md"}`
68. **edit** `{"edits": [{"oldText": "Max defect detection: 5/5. Max control preservation: 5/5.", "newText": "Max defect detection: 6/6. Max control preservation: 4/4."}], "path": "/work/experiments/verifier-probe-oracle-v2.md"}`
69. **edit** `{"edits": [{"oldText": "| 1,8,9,10 | clean controls | all preserved | 5/5 |", "newText": "| 1,8,9,10 | clean controls | all preserved | 4/4 |"}, {"oldText": "**Probe 2 score: 5/5 defects detected, 5/5 controls preserved, 0 false removals.**", "newText": "**Probe 2 score: 6/6 defects detected, 4/4 controls preserved, 0 false removals.**"}], "path": "/work/experiments/verifier-probe/results.md"}`
70. **edit** `{"edits": [{"oldText": "  Probe 1 (answers pre-extracted): 10/10 defects, 5/5 controls. Probe 2\n  (answers withheld): 5/5 defects, 5/5 controls, 0 false removals.", "newText": "  Probe 1 (answers pre-extracted): 10/10 defects, 5/5 controls. Probe 2\n  (answers withheld): 6/6 defects, 4/4 controls, 0 false removals."}], "path": "/work/CHANGELOG.md"}`
71. **bash** `{"command": "cd /work && grep -rn \"5/5\\|6/6\\|5 defects\\|6 defects\" outputs/feynman-harness-eval-quality.md experiments/verifier-probe/results.md experiments/verifier-probe-oracle-v2.md CHANGELOG.md outputs/.plans/feynman-harness-eval-quality.md", "timeout": 30}`
72. **edit** `{"edits": [{"oldText": "A claim supported by a real paper that *does not contain the cited number* is a harder case; Probe 2's H4 is the closest, and it was caught because HELM's abstract makes the mismatch obvious.", "newText": "A claim supported by a real paper that *does not contain the cited number* is a harder case; Probe 2's misattributed-statistic item is the closest, and it was caught because HELM's abstract makes the mismatch obvious."}, {"oldText": "**Synthetic defect density.** 10 defects in 14 items is far denser than real drafts, which likely inflates detection.", "newText": "**Sy …[+216 chars]`
73. **read** `{"path": "/work/outputs/feynman-harness-eval-quality.md", "offset": 1, "limit": 40}`
74. **bash** `{"command": "cd /work && sed -n '195,235p' outputs/feynman-harness-eval-quality.md && echo \"=== SIZE ===\" && wc -l outputs/feynman-harness-eval-quality.md && echo \"=== PROVENANCE ===\" && cat outputs/feynman-harness-eval-quality.provenance.md", "timeout": 30}`
75. **edit** `{"edits": [{"oldText": "1. **Ship a seeded-defect regression suite.** Use the 15-item instrument in `experiments/verifier-probe/` as a starting point.", "newText": "1. **Ship a seeded-defect regression suite.** Use the two probes in `experiments/verifier-probe/` (14 and 10 findings) as a starting point."}], "path": "/work/outputs/feynman-harness-eval-quality.md"}`
   - _said:_ Done. The case study is at **`outputs/feynman-harness-eval-quality.md`** (291 lines), with a provenance sidecar and all raw probe artifacts on disk.

**What I did**

- Built an 8-dimension rubric from the eval-science literature (construct validity, task/outcome validity, variance, reproducibility, contamination, judge validity, cost, adversarial controls).
- Audited the shipped harness mechanisms …[+2009 chars]

Last stopReason: `stop` (assistant messages this turn: 35)

## Final reply

Done. The case study is at **`outputs/feynman-harness-eval-quality.md`** (291 lines), with a provenance sidecar and all raw probe artifacts on disk.

**What I did**

- Built an 8-dimension rubric from the eval-science literature (construct validity, task/outcome validity, variance, reproducibility, contamination, judge validity, cost, adversarial controls).
- Audited the shipped harness mechanisms against it: 4 agents, 11 prompts, 16 skills, 13 extension registrars.
- Dogfooded the `verifier` agent twice with seeded-defect drafts and pre-written oracles.
- Probed the default literature-search tool on 5 fixed queries.

**Headline findings**

| Finding | Evidence |
|---|---|
| Strong *policy* layer, thin *measurement* layer | Written citation rules are specific and testable; no shipped eval suite, no repeated runs, no judge calibration |
| Verifier reconciliation is strong under favorable conditions | Probe 1: 10/10 defects, 5/5 controls. Probe 2: 6/6 defects, 4/4 controls, 0 false removals; $0.0296 / $0.0106, ~45–53 s |
| Retrieval defaults are unstable for multi-concept queries | Semantic Scholar-only: 5/10 returned records relevant; 2 of 4 queries returned zero records. The OpenAlex fallback rescued one rate-limited query at 5/5 |
| Silent failure is invisible | Provenance is self-reported free text; model, cost, seeds, and judge agreement are not recorded. I recovered them from `session.jsonl` |
| Repair > deletion | Probe 2 found the real Deep Research Bench ID (2506.06287) and retained the claim rather than removing it |

**Two self-corrections worth flagging**

1. Probe 1 was confounded — I had pre-loaded the correct numbers into `sources.md`, so it tested reconciliation, not independent verification. Probe 2 used an empty research file to fix that.
2. My own bookkeeping was wrong: I initially reported Probe 2 as 5/5 defects and 5/5 controls. A recount showed 6 defects and 4 controls. Fixed everywhere before delivery.

**Honest limits:** one model (`deepseek-v4.1-flash`), one run per probe, dense synthetic defects, unblinded oracle, and the `reviewer` agent was never tested. The result is evidence that the verifier's contract is executable, not that it is reliable.

**Next step:** run `/deepresearch` end-to-end on a frozen topic and audit its own artifact chain against the same rubric — that would test workflow conformance, which this study deliberately skipped.

## Files created this turn

- state/.feynman/sessions/2026-11-14T07-32-56-913Z_01a1d8f9-43d0-76ae-823c-c5c617bbe95e.jsonl
- state/.feynman/sessions/2026-11-14T07-32-56-913Z_01a1d8f9-43d0-76ae-823c-c5c617bbe95e/1209cd06-b155-41fe-a4fa-3b1556071f9c/run-0/session.jsonl
- state/.feynman/sessions/2026-11-14T07-32-56-913Z_01a1d8f9-43d0-76ae-823c-c5c617bbe95e/bcb2c19d-34fc-4945-b598-94ea65161486/run-0/session.jsonl
- state/.feynman/sessions/subagent-artifacts/1209cd06-b155-41fe-a4fa-3b1556071f9c_verifier_input.md
- state/.feynman/sessions/subagent-artifacts/1209cd06-b155-41fe-a4fa-3b1556071f9c_verifier_meta.json
- state/.feynman/sessions/subagent-artifacts/1209cd06-b155-41fe-a4fa-3b1556071f9c_verifier_output.md
- state/.feynman/sessions/subagent-artifacts/1209cd06-b155-41fe-a4fa-3b1556071f9c_verifier_transcript.jsonl
- state/.feynman/sessions/subagent-artifacts/bcb2c19d-34fc-4945-b598-94ea65161486_verifier_input.md
- state/.feynman/sessions/subagent-artifacts/bcb2c19d-34fc-4945-b598-94ea65161486_verifier_meta.json
- state/.feynman/sessions/subagent-artifacts/bcb2c19d-34fc-4945-b598-94ea65161486_verifier_output.md
- state/.feynman/sessions/subagent-artifacts/bcb2c19d-34fc-4945-b598-94ea65161486_verifier_transcript.jsonl
- work/CHANGELOG.md
- work/experiments/retrieval-probe/results.md
- work/experiments/verifier-probe-oracle-v2.md
- work/experiments/verifier-probe-oracle.md
- work/experiments/verifier-probe/README.md
- work/experiments/verifier-probe/draft.md
- work/experiments/verifier-probe/draft2.md
- work/experiments/verifier-probe/results.md
- work/experiments/verifier-probe/sources.md
- work/experiments/verifier-probe/sources2.md
- work/experiments/verifier-probe/verified.md
- work/experiments/verifier-probe/verified2.md
- work/outputs/.plans/feynman-harness-eval-quality.md
- work/outputs/feynman-harness-eval-quality.md
- work/outputs/feynman-harness-eval-quality.provenance.md

## Files modified this turn

(none)
