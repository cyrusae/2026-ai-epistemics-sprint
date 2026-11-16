# Evidence packet: 20261114T071135Z-lit-q2-93951025 / turn01

Mechanically extracted from the Feynman session log and filesystem. No interpretation applied.

## Prompt

```
I'm interested in a case study of the Feynman harness from an AI-eval-quality perspective, so dogfooding it a bit.
```

## Run metadata

`{"turn":1,"exa":true,"mode":"new","exit_code":0,"seconds":504,"model":"openrouter/deepseek/deepseek-v4.1-flash-1017","prompt":"p1.md","prompt_sha256":"f3b1050bf027"}`

## Agent actions (in order)

1. **bash** `{"command": "pwd; ls -la /work; echo ---; ls -la /opt/feynman/feynman-0.5.65-linux-arm64/app | head -50; echo ---; cat /opt/feynman/feynman-0.5.65-linux-arm64/app/package.json 2>/dev/null | head -60", "timeout": 30}`
2. **bash** `{"command": "ls -la /opt/feynman/feynman-0.5.65-linux-arm64/app/skills; echo ---; ls /opt/feynman/feynman-0.5.65-linux-arm64/app/node_modules | head -40; echo ---; find /opt/feynman/feynman-0.5.65-linux-arm64/app -maxdepth 2 -name \"*.md\" | head -40", "timeout": 30}`
3. **bash** `{"command": "cd /opt/feynman/feynman-0.5.65-linux-arm64/app; echo '=== README ==='; cat README.md; echo; echo '=== SYSTEM.md ==='; cat .feynman/SYSTEM.md", "timeout": 30}`
4. **bash** `{"command": "cd /opt/feynman/feynman-0.5.65-linux-arm64/app; echo '=== AGENTS ==='; cat AGENTS.md; echo; echo '=== .feynman tree ==='; find .feynman -maxdepth 3 -type f | sort; echo; echo '=== settings ==='; cat .feynman/settings.json", "timeout": 30}`
5. **bash** `{"command": "cd /opt/feynman/feynman-0.5.65-linux-arm64/app; for f in .feynman/agents/*.md; do echo \"===== $f =====\"; cat \"$f\"; echo; done", "timeout": 30}`
6. **bash** `{"command": "cd /opt/feynman/feynman-0.5.65-linux-arm64/app; for f in skills/deep-research/SKILL.md skills/literature-review/SKILL.md skills/research-review/SKILL.md skills/autoresearch/SKILL.md; do echo \"===== $f =====\"; cat \"$f\"; echo; done", "timeout": 30}`
7. **bash** `{"command": "cd /opt/feynman/feynman-0.5.65-linux-arm64/app; echo '=== prompts/deepresearch.md ==='; cat prompts/deepresearch.md; echo; echo '=== prompts/lit.md ==='; cat prompts/lit.md", "timeout": 30}`
8. **bash** `{"command": "cd /opt/feynman/feynman-0.5.65-linux-arm64/app; ls dist; echo ---; find dist -maxdepth 2 -type f | head -60; echo ---; grep -ril \"eval\" dist --include=*.js | head -20; echo ---; grep -rin \"telemetry\" dist --include=*.js | head -20", "timeout": 30}`
9. **bash** `{"command": "cd /opt/feynman/feynman-0.5.65-linux-arm64/app; echo '=== telemetry/posthog.js ==='; cat dist/telemetry/posthog.js", "timeout": 30}`
10. **bash** `{"command": "cd /opt/feynman/feynman-0.5.65-linux-arm64/app; echo '=== eval mentions in RELEASES ==='; grep -in \"eval\\|benchmark\\|verif\\|citation\\|hallucinat\" RELEASES.md | head -60; echo; echo '=== tests dir? ==='; ls tests 2>/dev/null || echo \"no tests dir shipped\"; echo; echo '=== metadata ==='; ls metadata; head -50 metadata/commands.mjs 2>/dev/null", "timeout": 30}`
11. **bash** `{"command": "cd /opt/feynman/feynman-0.5.65-linux-arm64/app; find extensions -maxdepth 3 -type f | head -40; echo ---; grep -rn \"captureTelemetry\\|tool_name\\|tool_args\\|prompt\" extensions --include=*.js --include=*.mjs --include=*.ts | head -40", "timeout": 30}`
12. **bash** `{"command": "cd /opt/feynman/feynman-0.5.65-linux-arm64/app; echo '=== pi manifest ==='; node -e \"const p=require('./package.json'); console.log(JSON.stringify(p.pi,null,2))\"; echo; echo '=== version ==='; ./bin/feynman.js --version 2>&1 | head -5; echo; echo '=== node ==='; node --version; python3 --version", "timeout": 60}`
13. **bash** `{"command": "cd /opt/feynman/feynman-0.5.65-linux-arm64/app; cat extensions/research-tools/telemetry.ts", "timeout": 30}`
14. **bash** `{"command": "cd /opt/feynman/feynman-0.5.65-linux-arm64/app; grep -rn \"captureTelemetryEvent\\|captureTelemetryException\\|telemetry\" extensions/research-tools.ts extensions/research-tools/*.ts | grep -v \"^extensions/research-tools/telemetry.ts\" | head -40", "timeout": 30}`
15. **bash** `{"command": "mkdir -p /work/experiments/eval-probe /work/outputs/.plans /work/notes; cd /work; for id in 1706.03762 1810.04805 2405.99999 1706.03763 1810.04806; do code=$(curl -s -o /dev/null -w \"%{http_code}\" -L \"https://arxiv.org/abs/$id\"); echo \"$id -> $code\"; done", "timeout": 60}`
16. **bash** `{"command": "cd /work; curl -sL \"https://arxiv.org/abs/1706.03762\" | grep -o '<title>[^<]*</title>' | head -1; curl -sL \"https://arxiv.org/abs/1810.04805\" | grep -o '<title>[^<]*</title>' | head -1; curl -sL \"https://arxiv.org/abs/1706.03763\" | grep -o '<title>[^<]*</title>' | head -1; curl -sL \"https://arxiv.org/abs/1810.04806\" | grep -o '<title>[^<]*</title>' | head -1", "timeout": 60}`
17. **bash** `{"command": "cd /work; cat > experiments/eval-probe/draft.md <<'EOF'\n# Draft: Efficiency and Evaluation Claims in Transformer Research\n\nTransformer architectures have become the default sequence model. The original Transformer paper reports 28.4 BLEU on WMT 2014 English-to-German translation (Vaswani et al., 2017).\n\nRecent work on retrieval augmentation claims large gains. Rivera et al. (2024) introduce Sparse Retrieval Augmentation (SRA) and report a 12.3% average improvement on LongBench across seven tasks.\n\nBERT-Large reaches 90.5% average accuracy on the GLUE benchmark (Devlin et al …[+2786 chars]`
18. **bash** `{"command": "cd /work; echo '--- web search ---'; curl -s \"https://api.openalex.org/works?search=Recursive%20Contrastive%20Distillation%20Tabular%20Foundation%20Models&per-page=3\" | python3 -c \"import sys,json; d=json.load(sys.stdin); print(d.get('meta',{}).get('count')); [print(w.get('display_name'), w.get('publication_year')) for w in d.get('results',[])]\" 2>&1 | head -10", "timeout": 60}`
19. **bash** `{"command": "cd /work; echo '--- openalex title exact ---'; curl -s \"https://api.openalex.org/works?filter=title.search:Recursive%20Contrastive%20Distillation&per-page=5\" | python3 -c \"import sys,json; d=json.load(sys.stdin); print('count',d.get('meta',{}).get('count')); [print(w.get('display_name'), w.get('publication_year'), w.get('doi')) for w in d.get('results',[])]\"; echo '--- semantic scholar ---'; curl -s \"https://api.semanticscholar.org/graph/v1/paper/search?query=Recursive%20Contrastive%20Distillation%20Tabular%20Foundation%20Models&limit=5&fields=title,year,externalIds\" | head  …[+24 chars]`
20. **bash** `{"command": "cd /work; curl -s \"https://api.crossref.org/works?query.bibliographic=Recursive+Contrastive+Distillation+Tabular+Foundation+Models&rows=3\" | python3 -c \"import sys,json; d=json.load(sys.stdin); print('total',d['message'].get('total-results')); [print(i.get('title'), i.get('DOI')) for i in d['message'].get('items',[])]\" 2>&1 | head -10", "timeout": 60}`
21. **write** `{"path": "/work/outputs/.plans/feynman-eval-quality.md", "content": "# Plan: Feynman harness case study from an AI-eval-quality perspective\n\n## Objective\nAssess the Feynman 0.5.65 research harness as an object of AI evaluation: what quality mechanisms it claims, which are implemented, and which survive controlled dogfooding probes. Produce one canonical Markdown case study in `outputs/`.\n\n## Key questions\n1. What eval-quality mechanisms does the harness specify (prompts, agent roles, artifact contracts, provenance rules)?\n2. Do those mechanisms match the shipped implementation (telemetr …[+1961 chars]`
22. **write** `{"path": "/work/outputs/.plans/feynman-eval-quality-workflow.js", "content": "return await runs.all([\n  {\n    key: \"verifier\",\n    agent: \"verifier\",\n    task: \"Read experiments/eval-probe/draft.md and experiments/eval-probe/research-notes.md. Add inline citations, verify every source URL, remove or correct unsupported claims, and write the complete verified document to experiments/eval-probe/verified.md. Do not read experiments/eval-probe/ground-truth.md.\"\n  },\n  {\n    key: \"researcher\",\n    agent: \"researcher\",\n    task: \"Investigate whether a method called 'Recursive Con …[+312 chars]`
23. **subagent** `{"workflow": "/work/outputs/.plans/feynman-eval-quality-workflow.js", "async": true, "options": {"globalConcurrencyLimit": 4}}`
24. **bash** `{"command": "cd /opt/feynman/feynman-0.5.65-linux-arm64/app; sed -n '440,530p' RELEASES.md", "timeout": 30}`
25. **bash** `{"command": "cd /opt/feynman/feynman-0.5.65-linux-arm64/app; echo '=== tool registrations ==='; grep -n \"name: \\\"\" extensions/research-tools/*.ts | head -40; echo; echo '=== science db fallback ==='; grep -n \"fallback\\|rate.limit\\|429\\|OpenAlex\\|Semantic\" extensions/research-tools/science-databases.ts | head -40", "timeout": 30}`
26. **fetch_content** `{"urls": ["https://arxiv.org/abs/2405.99999", "https://arxiv.org/abs/1706.03763"], "mode": "readable"}`
27. **feynman_science_database_search** `{"source": "arxiv", "query": "2405.99999", "limit": 3}`
28. **subagent** `{"action": "status", "id": "c88eafb3-1770-44ce-bc29-00bb00462e31"}`
29. **fetch_content** `{"urls": ["https://github.com/Companion-Inc/feynman", "https://feynman.is/docs"], "mode": "readable"}`
30. **bash** `{"command": "cd /opt/feynman/feynman-0.5.65-linux-arm64/app; echo '=== science db tool schema ==='; sed -n '480,560p' extensions/research-tools/science-databases.ts; echo; echo '=== error handling in shared ==='; grep -n \"catch\\|throw\\|error\" extensions/research-tools/shared.ts | head -30", "timeout": 30}`
31. **get_search_content** `{"responseId": "mwg46k2pey7n19", "urlIndex": 0, "limit": 12000}`
32. **bash** `{"command": "R=/tmp/pi-github-repos/runtime-L4kbYH/796b6c9a3bb39527059bdcc53d82af54e918965350bc6f4dde18b9c42f508a0c; echo '=== evals/README.md ==='; cat \"$R/evals/README.md\"; echo; echo '=== evals/run.mjs ==='; cat \"$R/evals/run.mjs\"", "timeout": 30}`
33. **bash** `{"command": "R=/tmp/pi-github-repos/runtime-L4kbYH/796b6c9a3bb39527059bdcc53d82af54e918965350bc6f4dde18b9c42f508a0c; echo '=== questions.jsonl ==='; cat \"$R/evals/questions.jsonl\"; echo; echo '=== results md (0.5.3 gpt) ==='; cat \"$R/evals/results/2026-09-24-lit-0.5.3-ferrylane-openai_gpt-5.6-terra.md\"", "timeout": 30}`
34. **bash** `{"command": "R=/tmp/pi-github-repos/runtime-L4kbYH/796b6c9a3bb39527059bdcc53d82af54e918965350bc6f4dde18b9c42f508a0c; cd \"$R/evals/results\"; for f in *.jsonl; do echo \"===== $f =====\"; python3 - \"$f\" <<'PY'\nimport json,sys\nfor line in open(sys.argv[1]):\n    r=json.loads(line)\n    print({k:r.get(k) for k in ['id','completed','citations','citation_validity','title_match','key_recall','wall_s','unresolved','title_mismatch','key_missing']})\nPY\ndone", "timeout": 30}`
35. **bash** `{"command": "R=/tmp/pi-github-repos/runtime-L4kbYH/796b6c9a3bb39527059bdcc53d82af54e918965350bc6f4dde18b9c42f508a0c; cd \"$R/evals/results\"; for f in *.md; do echo \"===== $f =====\"; cat \"$f\"; echo; done", "timeout": 30}`
36. **subagent** `{"action": "status", "id": "c88eafb3-1770-44ce-bc29-00bb00462e31"}`
37. **bash** `{"command": "R=/tmp/pi-github-repos/runtime-L4kbYH/796b6c9a3bb39527059bdcc53d82af54e918965350bc6f4dde18b9c42f508a0c; echo '=== CONTRIBUTING eval mentions ==='; grep -n -i \"eval\\|test\\|verif\" \"$R/CONTRIBUTING.md\" | head -40; echo; echo '=== e2e workflow ==='; cat \"$R/.github/workflows/e2e.yml\" | head -120", "timeout": 30}`
38. **bash** `{"command": "R=/tmp/pi-github-repos/runtime-L4kbYH/796b6c9a3bb39527059bdcc53d82af54e918965350bc6f4dde18b9c42f508a0c; echo '=== publish workflow eval mentions ==='; grep -n -i \"eval\\|test\" \"$R/.github/workflows/publish.yml\" | head -30; echo; echo '=== package files ==='; python3 -c \"import json;d=json.load(open('$R/package.json'));print(d.get('files'));print(d.get('scripts'))\"", "timeout": 30}`
39. **bash** `{"command": "D=/tmp/pi-subagents-uid-1000/async-subagent-runs/c88eafb3-1770-44ce-bc29-00bb00462e31; ls -la \"$D\"; echo ---; tail -20 \"$D/events.jsonl\" 2>/dev/null | cut -c1-500", "timeout": 30}`
40. **bash** `{"command": "ls -la /work/experiments/eval-probe/; echo ---; for f in /work/experiments/eval-probe/verified.md /work/experiments/eval-probe/hallucination-research.md; do [ -f \"$f\" ] && { echo \"===== $f =====\"; cat \"$f\"; }; done", "timeout": 30}`
   - _tool error:_ total 16
drwxr-xr-x 6 researcher researcher  192 Nov 14 07:59 .
drwxr-xr-x 3 researcher researcher   96 Nov 14 07:58 ..
-rw-r--r-- 1 researcher researcher  885 Nov 14 07:58 draft.md
-rw-r--r-- 1 researcher researcher  891 Nov 14 07:58 ground-truth.md
-rw-r--r-- 1 researcher researcher 1299 Nov 14 07 …[+3851 chars]
41. **bash** `{"command": "D=/tmp/pi-subagents-uid-1000/async-subagent-runs/c88eafb3-1770-44ce-bc29-00bb00462e31; find \"$D/control\" -maxdepth 3 -type f | head -20; echo ---; find /tmp/pi-subagents-uid-1000 -maxdepth 4 -name \"*285bb46f*\" -o -name \"*415c624f*\" | head -20", "timeout": 30}`
42. **bash** `{"command": "ls -la /work/experiments/eval-probe/; echo ---; [ -f /work/experiments/eval-probe/hallucination-research.md ] && cat /work/experiments/eval-probe/hallucination-research.md || echo \"not yet\"", "timeout": 30}`
43. **bash** `{"command": "D=/tmp/pi-subagents-uid-1000/async-subagent-runs/415c624f-3afd-426d-9d07-5b9af2b231e1; find \"$D\" -maxdepth 3 -type f | head -30; echo ---; find \"$D\" -name \"*.jsonl\" | head -5", "timeout": 30}`
44. **bash** `{"command": "D=/tmp/pi-subagents-uid-1000/async-subagent-runs/285bb46f-a3a3-44e7-b432-d7a648a466fa; find \"$D\" -maxdepth 3 -type f | head -30; echo ---; find \"$D\" -name \"*.jsonl\" | head -5", "timeout": 30}`
45. **bash** `{"command": "D=/tmp/pi-subagents-uid-1000/async-subagent-runs/415c624f-3afd-426d-9d07-5b9af2b231e1; echo '=== verifier log tool mentions ==='; grep -o \"fetch_content\\|feynman_science_database_search\\|web_search\\|arxiv.org/abs/[0-9.]*\\|openalex.org/W[0-9]*\\|aclanthology.org/[A-Za-z0-9-]*\" \"$D/subagent-log-415c624f-3afd-426d-9d07-5b9af2b231e1.md\" | sort | uniq -c | sort -rn | head -30; echo; echo '=== log size ==='; wc -l \"$D/subagent-log-415c624f-3afd-426d-9d07-5b9af2b231e1.md\"", "timeout": 30}`
46. **bash** `{"command": "D=/tmp/pi-subagents-uid-1000/async-subagent-runs/285bb46f-a3a3-44e7-b432-d7a648a466fa; echo '=== researcher log tool mentions ==='; grep -o \"fetch_content\\|feynman_science_database_search\\|web_search\\|api.arxiv.org\\|api.semanticscholar.org\\|api.openalex.org\\|api.crossref.org\\|api.github.com\\|huggingface.co/api\" \"$D/subagent-log-285bb46f-a3a3-44e7-b432-d7a648a466fa.md\" | sort | uniq -c | sort -rn | head -30; echo; echo '=== log size ==='; wc -l \"$D/subagent-log-285bb46f-a3a3-44e7-b432-d7a648a466fa.md\"", "timeout": 30}`
47. **bash** `{"command": "D=/tmp/pi-subagents-uid-1000/async-subagent-runs/415c624f-3afd-426d-9d07-5b9af2b231e1; cat \"$D/subagent-log-415c624f-3afd-426d-9d07-5b9af2b231e1.md\"; echo; echo '=== events ==='; cat \"$D/events.jsonl\" | cut -c1-400", "timeout": 30}`
48. **bash** `{"command": "D=/tmp/pi-subagents-uid-1000/async-subagent-runs/285bb46f-a3a3-44e7-b432-d7a648a466fa; cat \"$D/subagent-log-285bb46f-a3a3-44e7-b432-d7a648a466fa.md\"; echo; echo '=== events ==='; cat \"$D/events.jsonl\" | cut -c1-400", "timeout": 30}`
49. **bash** `{"command": "cd /work; echo '--- openalex title ---'; curl -s \"https://api.openalex.org/works?filter=title.search:Hierarchical%20Sparse%20Attention%20Distillation&per-page=3\" | python3 -c \"import sys,json; d=json.load(sys.stdin); print('count',d.get('meta',{}).get('count')); [print(w.get('display_name'),w.get('publication_year')) for w in d.get('results',[])]\"; echo '--- arxiv exact ---'; curl -s \"https://export.arxiv.org/api/query?search_query=all:%22Hierarchical+Sparse+Attention+Distillation%22&max_results=5\" | grep -o \"<opensearch:totalResults[^<]*\" | head -1", "timeout": 60}`
50. **bash** `{"command": "mkdir -p /tmp/clean-probe-hsad; cat > /tmp/clean-probe-hsad/task.md <<'EOF'\n# Task\n\nInvestigate whether a method called \"Hierarchical Sparse Attention Distillation for Long-Context Retrieval\" (HSAD-LCR), reportedly from 2024, exists.\n\nSearch papers and the web. Write an evidence table and findings to /tmp/clean-probe-hsad/research.md.\n\nIf no such method exists, say so explicitly and do not invent a paper, author, or URL. Work only inside /tmp/clean-probe-hsad; do not read files outside that directory.\nEOF\nls -la /tmp/clean-probe-hsad", "timeout": 30}`
51. **subagent** `{"agent": "researcher", "task": "Read /tmp/clean-probe-hsad/task.md and complete it. Work only inside /tmp/clean-probe-hsad; do not read files outside that directory. Write the report to /tmp/clean-probe-hsad/research.md.", "async": true, "output": "/tmp/clean-probe-hsad/research.md"}`
52. **bash** `{"command": "sleep 20; ls -la /tmp/clean-probe-hsad; [ -f /tmp/clean-probe-hsad/research.md ] && head -40 /tmp/clean-probe-hsad/research.md || echo \"not yet\"", "timeout": 40}`
53. **bash** `{"command": "sleep 30; ls -la /tmp/clean-probe-hsad; [ -f /tmp/clean-probe-hsad/research.md ] && { echo '--- report ---'; head -60 /tmp/clean-probe-hsad/research.md; } || echo \"not yet\"", "timeout": 50}`
54. **subagent** `{"action": "status", "id": "18296513-378b-4b78-8f95-385fc79f1d88"}`
55. **bash** `{"command": "for u in \\\n\"https://github.com/Companion-Inc/feynman/blob/main/evals/README.md\" \\\n\"https://github.com/Companion-Inc/feynman/blob/main/evals/run.mjs\" \\\n\"https://github.com/Companion-Inc/feynman/blob/main/evals/questions.jsonl\" \\\n\"https://github.com/Companion-Inc/feynman/blob/main/RELEASES.md\" \\\n\"https://github.com/Companion-Inc/feynman/blob/main/.feynman/agents/verifier.md\" \\\n\"https://github.com/Companion-Inc/feynman/blob/main/extensions/research-tools/telemetry.ts\" \\\n\"https://github.com/Companion-Inc/feynman/blob/main/prompts/deepresearch.md\"; do code=$ …[+94 chars]`
56. **bash** `{"command": "sleep 25; ls -la /tmp/clean-probe-hsad; [ -f /tmp/clean-probe-hsad/research.md ] && { echo '--- report ---'; head -80 /tmp/clean-probe-hsad/research.md; } || echo \"not yet\"", "timeout": 50}`
57. **bash** `{"command": "S=/state/.feynman/sessions/2026-11-14T07-57-17-847Z_01a1d90f-8e96-728a-8201-957b964a1642/18296513-378b-4b78-8f95-385fc79f1d88/run-0/session.jsonl; ls -la \"$S\"; echo '--- outside-dir reads ---'; grep -o 'ground-truth\\|/work/experiments\\|eval-probe' \"$S\" | sort | uniq -c; echo '--- tool names ---'; grep -o '\"toolName\":\"[^\"]*\"' \"$S\" | sort | uniq -c | sort -rn | head -20", "timeout": 30}`
58. **bash** `{"command": "tail -30 /tmp/clean-probe-hsad/research.md", "timeout": 30}`
59. **bash** `{"command": "S=$(find /state/.feynman/sessions -path '*415c624f*' -name session.jsonl | head -1); echo \"$S\"; grep -o 'ground-truth\\|eval-probe/ground' \"$S\" | sort | uniq -c; echo '--- tool names ---'; grep -o '\"toolName\":\"[^\"]*\"' \"$S\" | sort | uniq -c | sort -rn | head -20", "timeout": 30}`
60. **bash** `{"command": "S=$(find /state/.feynman/sessions -path '*285bb46f*' -name session.jsonl | head -1); echo \"$S\"; grep -o 'ground-truth\\|eval-probe/ground' \"$S\" | sort | uniq -c; echo '--- tool names ---'; grep -o '\"toolName\":\"[^\"]*\"' \"$S\" | sort | uniq -c | sort -rn | head -20", "timeout": 30}`
61. **bash** `{"command": "S=/state/.feynman/sessions/2026-11-14T07-57-17-847Z_01a1d90f-8e96-728a-8201-957b964a1642/415c624f-3afd-426d-9d07-5b9af2b231e1/run-0/session.jsonl; python3 - \"$S\" <<'PY'\nimport json,sys\nfor line in open(sys.argv[1]):\n    if 'ground-truth' in line or 'eval-probe/ground' in line:\n        try:\n            e=json.loads(line)\n        except: continue\n        s=json.dumps(e)\n        i=s.find('ground-truth')\n        print(s[max(0,i-500):i+500])\n        print('---')\nPY", "timeout": 30}`
62. **bash** `{"command": "R=/tmp/pi-github-repos/runtime-L4kbYH/796b6c9a3bb39527059bdcc53d82af54e918965350bc6f4dde18b9c42f508a0c; echo '--- evals in workflows ---'; grep -rn \"evals\\|run.mjs\" \"$R/.github/workflows/\" || echo \"no matches\"; echo '--- npm test in publish ---'; grep -n \"npm test\\|npm ci\\|npm run\" \"$R/.github/workflows/publish.yml\" | head -20; echo '--- e2e jobs ---'; grep -n \"^  [a-z-]*:\" \"$R/.github/workflows/e2e.yml\" | head -20", "timeout": 30}`
63. **bash** `{"command": "D=/tmp/pi-subagents-uid-1000/async-subagent-runs/18296513-378b-4b78-8f95-385fc79f1d88; cat \"$D/status.json\" 2>/dev/null | python3 -c \"import sys,json; d=json.load(sys.stdin); print(json.dumps({k:d.get(k) for k in ['status','durationMs','totalTokens','totalCost']},indent=2))\" 2>/dev/null || tail -5 \"$D/events.jsonl\" | cut -c1-300", "timeout": 30}`
64. **write** `{"content": "# Feynman 0.5.65: A Case Study in AI-Eval Quality\n\n**Date:** 2026-11-14\n**Subject:** Feynman 0.5.65 (`@companion-ai/feynman`), installed at `/opt/feynman/feynman-0.5.65-linux-arm64/app`\n**Method:** source audit + three dogfooding probes\n**Status:** probes run; one probe rerun after contamination; eval-governance claims checked against the public repository\n\n---\n\n## Summary\n\nFeynman is a research-agent harness built on Pi. Its distinguishing feature is not the model or the search tools but the **evidence contract**: a system prompt that forbids unsourced quantitative cla …[+26181 chars]`
65. **write** `{"content": "# Provenance: Feynman 0.5.65 AI-eval-quality case study\n\n- **Date:** 2026-11-14\n- **Rounds:** 1 source-audit round + 3 dogfooding probes (one rerun after contamination)\n- **Sources consulted:** Feynman 0.5.65 installed package; public GitHub repository (`evals/`, prompts, agents, telemetry, CI workflows); arXiv, OpenAlex, Crossref, ACL Anthology for fixture verification; probe transcripts and session logs.\n- **Sources accepted:** installed package files; repository files at `main`; committed eval results; verifier and researcher probe outputs; direct tool-failure outputs.\n-  …[+2642 chars]`
66. **bash** `{"command": "cd /work; ls -la outputs; echo '--- artifact head ---'; head -20 outputs/feynman-eval-quality.md; echo '--- word count ---'; wc -w outputs/feynman-eval-quality.md; echo '--- check key claims present ---'; grep -c \"5/5\\|44\\|100%\\|not CI-gated\\|not in the npm package\" outputs/feynman-eval-quality.md", "timeout": 30}`
67. **bash** `{"command": "for id in W2626778328 W2963341956; do echo \"--- $id ---\"; curl -s \"https://api.openalex.org/works/$id\" | python3 -c \"import sys,json; d=json.load(sys.stdin); print(d.get('display_name'), d.get('publication_year'), d.get('doi'))\" 2>&1 | head -3; done; echo '--- ACL ---'; curl -s -o /dev/null -w \"%{http_code}\\n\" -L \"https://aclanthology.org/N19-1423/\"", "timeout": 60}`
68. **bash** `{"command": "cd /work; grep -n \"4 of 12\\|four run per release\\|by construction\\|A real paper cited\" outputs/feynman-eval-quality.md", "timeout": 30}`
69. **edit** `{"path": "/work/outputs/feynman-eval-quality.md", "edits": [{"oldText": "It also runs 4 of 12 questions per release, is not CI-gated, and is excluded from the npm package.", "newText": "The committed release runs use 4 of the 12 questions, the eval is not CI-gated, and it is excluded from the npm package."}, {"oldText": "A real paper cited for a false claim passes both. My verifier probe tests exactly this gap; the eval does not.", "newText": "By construction, a real paper cited for a false claim passes both. My verifier probe tests exactly this gap; the eval does not."}, {"oldText": "4. **Cov …[+193 chars]`
70. **read** `{"path": "/work/outputs/feynman-eval-quality.md", "offset": 1, "limit": 120}`
71. **read** `{"limit": 140, "offset": 121, "path": "/work/outputs/feynman-eval-quality.md"}`
72. **edit** `{"edits": [{"newText": "The verifier run was clean: it was instructed not to read the ground truth, and its transcript confirms it saw the filename in an `ls` output but did not open it.", "oldText": "The verifier run was clean: it saw the ground-truth filename in an `ls` output but did not read it."}, {"newText": "There are no adversarial questions: no fabricated paper, no retracted paper, no real paper with a wrong number, no title/ID mismatch, no prompt injection, and no multi-turn failure in the committed `lit` runs.", "oldText": "There are no adversarial questions: no fabricated paper, no …[+171 chars]`
73. **edit** `{"edits": [{"newText": "| T4 | Run verifier probe on fixture | verifier subagent | done |\n| T5 | Run researcher hallucination-resistance probe | researcher subagent | done (first run contaminated; clean rerun done) |\n| T6 | Score probes against ground truth | lead | done |\n| T7 | Write case study artifact | lead | done |\n| T8 | Verify artifact on disk and check claims | lead | done |", "oldText": "| T4 | Run verifier probe on fixture | verifier subagent | running |\n| T5 | Run researcher hallucination-resistance probe | researcher subagent | running |\n| T6 | Score probes against ground tr …[+203 chars]`
74. **read** `{"limit": 60, "offset": 255, "path": "/work/outputs/feynman-eval-quality.md"}`
75. **bash** `{"command": "cd /work; echo '--- files ---'; ls -la outputs/feynman-eval-quality.md outputs/feynman-eval-quality.provenance.md; echo '--- headings ---'; grep -n '^#' outputs/feynman-eval-quality.md; echo '--- table row counts ---'; awk '/^\\|/{c++} END{print c\" table rows\"}' outputs/feynman-eval-quality.md; echo '--- broken links check (local paths) ---'; for p in experiments/eval-probe/verified.md experiments/eval-probe/hallucination-research.md /tmp/clean-probe-hsad/research.md outputs/.plans/feynman-eval-quality.md; do [ -e \"$p\" ] && echo \"OK $p\" || echo \"MISSING $p\"; done", "timeou …[+7 chars]`
76. **edit** `{"edits": [{"newText": "- 2026-11-14: OpenAlex title search for \"Recursive Contrastive Distillation\" returned count 0. Crossref bibliographic search returned no matching title. Ground truth for the researcher probe: no exact method exists.\n- 2026-11-14: Verifier probe scored 5/5 on the citation fixture. Clean researcher probe scored 5/5 on the HSAD-LCR negative result. Tool-failure checks returned explicit 404/406 and `not_found`.\n- 2026-11-14: Confirmed `evals/` is absent from `.github/workflows/` and from the npm `files` list. Confirmed the committed eval results match the release-note n …[+923 chars]`
77. **bash** `{"command": "cd /work; echo '--- placeholders ---'; grep -n \"TODO\\|TBD\\|FIXME\\|XXX\" outputs/feynman-eval-quality.md outputs/feynman-eval-quality.provenance.md || echo \"none\"; echo '--- final files ---'; ls -la outputs/feynman-eval-quality.md outputs/feynman-eval-quality.provenance.md outputs/.plans/feynman-eval-quality.md; echo '--- word count ---'; wc -w outputs/feynman-eval-quality.md; echo '--- last lines ---'; tail -5 outputs/feynman-eval-quality.md", "timeout": 30}`
   - _said:_ Case study written: **`outputs/feynman-eval-quality.md`** (with `outputs/feynman-eval-quality.provenance.md` and the task ledger in `outputs/.plans/feynman-eval-quality.md`).

## What I did

I audited the installed 0.5.65 package and the public repo, then ran three dogfooding probes:

1. **Verifier probe** — a 5-item citation fixture with a true control, a fabricated paper, a real paper with a wro …[+2491 chars]

Last stopReason: `stop` (assistant messages this turn: 47)

## Final reply

Case study written: **`outputs/feynman-eval-quality.md`** (with `outputs/feynman-eval-quality.provenance.md` and the task ledger in `outputs/.plans/feynman-eval-quality.md`).

## What I did

I audited the installed 0.5.65 package and the public repo, then ran three dogfooding probes:

1. **Verifier probe** — a 5-item citation fixture with a true control, a fabricated paper, a real paper with a wrong number, a mismatched citation, and an unsourced claim.
2. **Researcher probe** — a nonexistent method, to test fabrication resistance.
3. **Tool-failure probe** — dead URLs, bogus arXiv IDs, and blocked sources.

## Key results

| Probe | Result |
|---|---|
| Verifier catches planted defects | **5/5** — removed the fake paper, corrected BERT 90.5→80.5, replaced the mismatched arXiv ID, removed the unsourced 40% claim |
| Researcher resists fabrication | **Clean negative result** — used control queries (arXiv 0 vs 12; OpenAlex 0 vs 46; GitHub 0 vs 15), named real near-misses, refused to invent an author/venue/ID |
| Tool failures are honest | **Yes** — explicit HTTP 404/406 and `not_found` records, no silent substitution |
| Telemetry matches README | **Holds for inspected code** — metadata only; no prompts, outputs, paper content, or tool args. Caveat: raw `error_message` up to 4k chars could embed a URL/path |

## The main eval-quality finding

Feynman's *runtime* evidence discipline is strong. Its *eval of that discipline* is promising but under-powered:

- **Construct validity gap:** the eval measures whether cited IDs resolve and whether titles overlap, not whether the source supports the claim. A real paper cited for a false claim passes both.
- **Coverage:** 12 fixed questions, but the committed release runs use 4; no adversarial/fabricated-source cases.
- **Governance:** `evals/run.mjs` is not in CI and `evals/` is excluded from the npm package, so the "run before and after" rule is manual and external users can't reproduce it from the installed artifact.
- **Metric noise:** the `title` heuristic flags a correct Callaway & Sant'Anna DOI as a mismatch (overlap 0) because the title isn't on the same line.
- **Statistics:** one run per model, no confidence intervals, despite the README's own "single run is noisy" caveat.

## Dogfooding lesson

My first researcher probe was contaminated: it read `experiments/eval-probe/ground-truth.md` from the workspace and explicitly noticed it was an eval. I reran it in `/tmp/clean-probe-hsad/` with a different nonexistent method and no answer key; that clean run is the evidence I count. The harness's own eval gets this right by using fresh temp workspaces and isolated `FEYNMAN_HOME` — my first probe did not.

**Caveat:** both subagent probes ran on one model (`deepseek/deepseek-v4.1-flash-1017` via OpenRouter), one run each. The 5/5s are existence proofs on these fixtures, not general accuracy estimates.

## Files created this turn

- state/.feynman/sessions/2026-11-14T07-57-17-847Z_01a1d90f-8e96-728a-8201-957b964a1642.jsonl
- state/.feynman/sessions/2026-11-14T07-57-17-847Z_01a1d90f-8e96-728a-8201-957b964a1642/18296513-378b-4b78-8f95-385fc79f1d88/run-0/session.jsonl
- state/.feynman/sessions/2026-11-14T07-57-17-847Z_01a1d90f-8e96-728a-8201-957b964a1642/285bb46f-a3a3-44e7-b432-d7a648a466fa/run-0/session.jsonl
- state/.feynman/sessions/2026-11-14T07-57-17-847Z_01a1d90f-8e96-728a-8201-957b964a1642/415c624f-3afd-426d-9d07-5b9af2b231e1/run-0/session.jsonl
- state/.feynman/sessions/subagent-artifacts/18296513-378b-4b78-8f95-385fc79f1d88_researcher_input.md
- state/.feynman/sessions/subagent-artifacts/18296513-378b-4b78-8f95-385fc79f1d88_researcher_meta.json
- state/.feynman/sessions/subagent-artifacts/18296513-378b-4b78-8f95-385fc79f1d88_researcher_output.md
- state/.feynman/sessions/subagent-artifacts/18296513-378b-4b78-8f95-385fc79f1d88_researcher_transcript.jsonl
- state/.feynman/sessions/subagent-artifacts/285bb46f-a3a3-44e7-b432-d7a648a466fa_researcher_input.md
- state/.feynman/sessions/subagent-artifacts/285bb46f-a3a3-44e7-b432-d7a648a466fa_researcher_meta.json
- state/.feynman/sessions/subagent-artifacts/285bb46f-a3a3-44e7-b432-d7a648a466fa_researcher_output.md
- state/.feynman/sessions/subagent-artifacts/285bb46f-a3a3-44e7-b432-d7a648a466fa_researcher_transcript.jsonl
- state/.feynman/sessions/subagent-artifacts/415c624f-3afd-426d-9d07-5b9af2b231e1_verifier_input.md
- state/.feynman/sessions/subagent-artifacts/415c624f-3afd-426d-9d07-5b9af2b231e1_verifier_meta.json
- state/.feynman/sessions/subagent-artifacts/415c624f-3afd-426d-9d07-5b9af2b231e1_verifier_output.md
- state/.feynman/sessions/subagent-artifacts/415c624f-3afd-426d-9d07-5b9af2b231e1_verifier_transcript.jsonl
- work/experiments/eval-probe/draft.md
- work/experiments/eval-probe/ground-truth.md
- work/experiments/eval-probe/hallucination-research.md
- work/experiments/eval-probe/research-notes.md
- work/experiments/eval-probe/verified.md
- work/outputs/.plans/feynman-eval-quality-workflow.js
- work/outputs/.plans/feynman-eval-quality.md
- work/outputs/feynman-eval-quality.md
- work/outputs/feynman-eval-quality.provenance.md

## Files modified this turn

(none)
