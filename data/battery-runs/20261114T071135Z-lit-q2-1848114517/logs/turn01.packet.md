# Evidence packet: 20261114T071135Z-lit-q2-1848114517 / turn01

Mechanically extracted from the Feynman session log and filesystem. No interpretation applied.

## Prompt

```
I'm interested in a case study of the Feynman harness from an AI-eval-quality perspective, so dogfooding it a bit.
```

## Run metadata

`{"turn":1,"exa":true,"mode":"new","exit_code":0,"seconds":378,"model":"openrouter/deepseek/deepseek-v4.1-flash-1017","prompt":"p1.md","prompt_sha256":"f3b1050bf027"}`

## Agent actions (in order)

   - _said:_ I'll start by figuring out what's actually on disk here — both the harness internals and any prior notes — before deciding what a rigorous case study would need.
1. **bash** `{"command": "pwd; ls -la /work 2>/dev/null | head -50; echo \"---CHANGELOG---\"; ls -la /work/CHANGELOG.md /work/outputs /work/notes 2>/dev/null", "timeout": 30}`
2. **bash** `{"command": "ls -la /opt/feynman/feynman-0.5.65-linux-arm64/app 2>/dev/null | head -40; echo \"---\"; cat /opt/feynman/feynman-0.5.65-linux-arm64/app/package.json 2>/dev/null | head -60", "timeout": 30}`
   - _tool error:_ /work
total 4
drwxr-xr-x 6 researcher researcher  192 Nov 14 08:56 .
drwxr-xr-x 1 root       root       4096 Nov 14 08:56 ..
drwxr-xr-x 3 researcher researcher   96 Nov 14 08:56 .sandbox
drwxr-xr-x 2 researcher researcher   64 Nov 14 08:56 notes
drwxr-xr-x 4 researcher researcher  128 Nov 14 08:56 o …[+493 chars]
3. **bash** `{"command": "cd /opt/feynman/feynman-0.5.65-linux-arm64/app; echo \"=== AGENTS.md ===\"; cat AGENTS.md; echo; echo \"=== README ===\"; cat README.md", "timeout": 30}`
4. **bash** `{"command": "cd /opt/feynman/feynman-0.5.65-linux-arm64/app; ls -R .feynman | head -80; echo \"=== SYSTEM.md ===\"; cat .feynman/SYSTEM.md", "timeout": 30}`
5. **bash** `{"command": "cd /opt/feynman/feynman-0.5.65-linux-arm64/app; ls bin dist | head; echo \"=== dist tree (depth2) ===\"; find dist -maxdepth 2 -type d | head -40; echo \"=== src present? ===\"; ls src 2>/dev/null | head; echo \"=== tests present? ===\"; ls tests 2>/dev/null | head", "timeout": 30}`
6. **bash** `{"command": "cd /opt/feynman/feynman-0.5.65-linux-arm64/app; grep -rIl --include=*.md --include=*.mjs --include=*.js -iE '\\beval(uation)?\\b' . --exclude-dir=node_modules | head -40; echo \"=== commands.mjs ===\"; head -80 metadata/commands.mjs 2>/dev/null", "timeout": 60}`
7. **bash** `{"command": "cd /opt/feynman/feynman-0.5.65-linux-arm64/app; node -v; echo \"=== bin ===\"; cat bin/feynman.js; echo \"=== env keys present ===\"; env | grep -iE 'api_key|anthropic|openai|feynman|model|provider|token' | sed -E 's/=(.{0,6}).*/=\\1…/' | sort", "timeout": 30}`
8. **bash** `{"command": "cd /opt/feynman/feynman-0.5.65-linux-arm64/app; cat .env.example; echo \"=== settings ===\"; cat .feynman/settings.json", "timeout": 30}`
9. **bash** `{"command": "ls -la /state 2>/dev/null | head -30; echo \"=== session file ===\"; ls -la \"$PI_SESSION_FILE\" 2>/dev/null; echo; head -c 1200 \"$PI_SESSION_FILE\" 2>/dev/null", "timeout": 30}`
10. **bash** `{"command": "cd /work; feynman --help 2>&1 | head -60; echo \"EXIT=$?\"", "timeout": 120}`
11. **bash** `{"command": "cd /work; feynman --help 2>&1 | sed -n '60,140p'", "timeout": 120}`
12. **bash** `{"command": "cd /opt/feynman/feynman-0.5.65-linux-arm64/app; echo \"=== dist files with size ===\"; find dist -type f -name '*.js' | xargs ls -S 2>/dev/null | head -20; echo \"=== grep eval/score/bench in dist ===\"; grep -rIl -iE 'benchmark|scorer|grader' dist | head -20", "timeout": 60}`
13. **bash** `{"command": "cd /work && mkdir -p experiments && python3 - <<'PY'\nimport json,collections,os\np=os.environ[\"PI_SESSION_FILE\"]\nrows=[json.loads(l) for l in open(p) if l.strip()]\nprint(\"entries:\",len(rows))\nc=collections.Counter(r.get(\"type\") for r in rows)\nprint(c)\nfor t in c:\n    ex=[r for r in rows if r.get(\"type\")==t][0]\n    print(\"\\n---\",t,\"keys:\",sorted(ex.keys()))\n    if t==\"message\":\n        print(\"   msg keys:\", sorted(ex[\"message\"].keys()))\n        print(\"   role:\", ex[\"message\"].get(\"role\"))\n        if \"usage\" in ex[\"message\"]: print(\"   usage …[+53 chars]`
14. **bash** `{"command": "cd /opt/feynman/feynman-0.5.65-linux-arm64/app; sed -n '1,120p' dist/telemetry/posthog.js", "timeout": 30}`
15. **bash** `{"command": "cd /work && python3 - <<'PY'\nimport json,os,collections\np=os.environ[\"PI_SESSION_FILE\"]\nrows=[json.loads(l) for l in open(p) if l.strip()]\ndef shape(x,d=0,maxd=3):\n    if isinstance(x,dict): return {k:shape(v,d+1,maxd) for k,v in list(x.items())[:12]} if d<maxd else \"{...}\"\n    if isinstance(x,list): return [shape(x[0],d+1,maxd)] if x else []\n    if isinstance(x,str): return x[:60]+(\"…\" if len(x)>60 else \"\")\n    return x\nfor r in rows:\n    if r.get(\"type\")==\"message\" and r[\"message\"].get(\"role\")==\"assistant\":\n        print(json.dumps(shape(r[\"message\ …[+407 chars]`
16. **bash** `{"command": "cd /opt/feynman/feynman-0.5.65-linux-arm64/app; grep -n \"capture\\|event\\|properties\" dist/telemetry/posthog.js | sed -n '1,80p'; echo \"=== tool names registered (research extension) ===\"; ls extensions; find extensions -name '*.js' -o -name '*.mjs' | head -20", "timeout": 30}`
17. **bash** `{"command": "cd /opt/feynman/feynman-0.5.65-linux-arm64/app; echo \"=== temperature/seed refs ===\"; grep -rIn -E 'temperature|top_p|\\bseed\\b' dist extensions --include=*.js --include=*.ts | head -30; echo; echo \"=== PI_SESSION_FILE refs ===\"; grep -rIn 'PI_SESSION_FILE' dist extensions node_modules/@earendil-works/pi-coding-agent/dist 2>/dev/null | head -20", "timeout": 60}`
18. **bash** `{"command": "cd /opt/feynman/feynman-0.5.65-linux-arm64/app; ls prompts; echo \"=== deepresearch ===\"; cat prompts/deepresearch.md", "timeout": 30}`
19. **bash** `{"command": "cd /opt/feynman/feynman-0.5.65-linux-arm64/app; grep -o '\"temperature\"[^,}]*' dist/model/*.js | head; echo \"=== models-json sample ===\"; head -c 600 dist/model/models-json.js; echo; echo \"=== approved model list source ===\"; grep -n \"deepseek\" dist/model/catalog.js | head -5", "timeout": 30}`
20. **bash** `{"command": "cd /work; feynman doctor 2>&1 | tail -40", "timeout": 180}`
21. **bash** `{"command": "cd /work && mkdir -p experiments/runs outputs/.plans outputs/.drafts notes && mkdir -p experiments/runs/smoke/workspace && cd experiments/runs/smoke/workspace && time env -u PI_SESSION_FILE -u PI_SESSION_ID FEYNMAN_TELEMETRY=off feynman -p \"Reply with exactly: OK. Do not use tools.\" --model openrouter/deepseek/deepseek-v4.1-flash-1017 --thinking off --session-dir /work/experiments/runs/smoke/sessions --cwd /work/experiments/runs/smoke/workspace --no-themes 2>&1 | tail -20; echo \"EXIT=$?\"; ls -la /work/experiments/runs/smoke/sessions 2>/dev/null", "timeout": 300}`
22. **feynman_science_database_search** `{"source": "arxiv", "query": "1706.03762,2201.11903,2106.09685,2312.00752,2305.18290", "limit": 5}`
23. **feynman_science_database_search** `{"source": "arxiv", "query": "Sparse Routing for Efficient Multimodal Retrieval", "limit": 5}`
24. **write** `{"path": "/work/outputs/.plans/feynman-eval-quality-case-study.md", "content": "# Plan: Feynman harness from an AI-eval-quality perspective\n\nSlug: `feynman-eval-quality-case-study`\nDate: 2026-11-14\nSubject: `@companion-ai/feynman` v0.5.65, installed at `/opt/feynman/feynman-0.5.65-linux-arm64/app`\n\n## Question\n\nIf an evaluator wanted to *measure* this harness, what can they actually measure, what\ndoes the harness control, and where would their measurements be confounded or\nself-attested? Secondarily: does the harness's own evidence discipline\n(\"verified / blocked\" labels, provenan …[+3331 chars]`
25. **write** `{"path": "/work/experiments/run_probe.py", "content": "#!/usr/bin/env python3\n\"\"\"Run isolated Feynman subprocess probes and summarize the persisted session traces.\n\nEach probe gets its own cwd, session dir, and run dir so it cannot write into /work.\nParent PI_* session vars are stripped so the child cannot append to this session.\n\"\"\"\nfrom __future__ import annotations\n\nimport json\nimport os\nimport subprocess\nimport sys\nimport time\nfrom pathlib import Path\n\nROOT = Path(\"/work/experiments\")\nMODEL = \"openrouter/deepseek/deepseek-v4.1-flash-1017\"\nFEYNMAN = os.environ.get …[+7477 chars]`
26. **bash** `{"command": "cd /work && python3 - <<'PY'\nimport json,glob\np=sorted(glob.glob('/work/experiments/runs/smoke/sessions/*.jsonl'))[0]\nfor line in open(p):\n    r=json.loads(line)\n    m=r.get('message') or {}\n    if m.get('role')=='assistant':\n        print(json.dumps(m,indent=1)[:1500]); break\nPY", "timeout": 30}`
27. **bash** `{"command": "cd /work && python3 experiments/run_probe.py det trap 2>&1 | tail -20", "timeout": 900}`
28. **bash** `{"command": "cd /work/experiments/runs; for d in det-1 det-2 det-3; do echo \"=== $d ===\"; cat $d/workspace/result.txt; echo; echo \"--- stdout ---\"; head -c 400 $d/stdout.txt; echo; done", "timeout": 30}`
29. **bash** `{"command": "cd /work/experiments/runs; for d in trap-1 trap-2; do echo \"=== $d stdout ===\"; cat $d/stdout.txt; echo; echo \"=== $d files ===\"; find $d/workspace -type f | head; done; echo \"=== trap-1 note ===\"; cat trap-1/workspace/notes/*.md 2>/dev/null | head -60", "timeout": 30}`
30. **bash** `{"command": "cd /work && nohup python3 experiments/run_probe.py ground workflow > experiments/probe-bg.log 2>&1 &\necho \"started pid $!\"", "timeout": 30}`
31. **bash** `{"command": "cd /work && python3 - <<'PY'\nimport json,glob,os\nrows=[]\nfor p in sorted(glob.glob('/work/experiments/runs/*/meta.json')):\n    m=json.load(open(p))\n    for t in m['traces']:\n        rows.append((m['probe']+'-'+str(m['index']), t))\nprint(f\"{'run':10} {'turns':>5} {'w/usage':>7} {'calls':>5} {'results':>7} {'errs':>4} {'unpaired':>8} {'sysPrompt':>9} {'tempFld':>7} {'cost$':>8} {'trace_s':>8}\")\nfor name,t in rows:\n    print(f\"{name:10} {t['assistant_turns']:5} {t['assistant_turns_with_usage']:7} {len(t['tool_calls']):5} {t['tool_results']:7} {t['tool_errors']:4} {len(t[' …[+309 chars]`
32. **bash** `{"command": "cd /work/experiments/runs; p=$(ls det-1/sessions/*.jsonl); echo \"harness version in trace?\"; grep -c '0\\.5\\.65' $p || true; echo \"temperature in trace?\"; grep -c 'temperature' $p || true; echo \"seed?\"; grep -c '\"seed\"' $p || true; echo \"=== system prompt char/approx tokens ===\"; python3 - <<'PY'\nimport json,glob\np=sorted(glob.glob('/work/experiments/runs/det-1/sessions/*.jsonl'))[0]\nrows=[json.loads(l) for l in open(p)]\nsysm=[r for r in rows if (r.get('message') or {}).get('role')=='system'][0]\ntxt=(sysm['message'].get('content') or '')+json.dumps(sysm['message']. …[+241 chars]`
33. **bash** `{"command": "cd /opt/feynman/feynman-0.5.65-linux-arm64/app; echo \"=== RELEASES mentions of eval/benchmark/verification ===\"; grep -n -iE '\\beval(uation)?\\b|benchmark|verification label|provenance' RELEASES.md | head -30; echo \"=== recent release headers ===\"; grep -n '^## ' RELEASES.md | head -10", "timeout": 30}`
34. **bash** `{"command": "cd /opt/feynman/feynman-0.5.65-linux-arm64/app; sed -n '440,530p' RELEASES.md", "timeout": 30}`
35. **bash** `{"command": "cd /work; cat experiments/probe-bg.log 2>/dev/null | tail -5; ls experiments/runs/ | tr '\\n' ' '; echo; ls experiments/runs/workflow-1/workspace 2>/dev/null | head", "timeout": 30}`
36. **bash** `{"command": "cd /work/experiments/runs; echo \"=== ground-1 ===\"; cat ground-1/stdout.txt; echo; echo \"=== tool calls ===\"; python3 -c \"\nimport json,glob\np=glob.glob('/work/experiments/runs/ground-1/sessions/*.jsonl')[0]\nfor l in open(p):\n    r=json.loads(l); m=r.get('message') or {}\n    for b in (m.get('content') or []):\n        if isinstance(b,dict) and b.get('type')=='toolCall': print(b.get('name'), json.dumps(b.get('arguments'))[:200])\n\"", "timeout": 30}`
37. **bash** `{"command": "curl -s --max-time 20 https://api.github.com/repos/Companion-Inc/feynman/contents/ | python3 -c \"import sys,json; d=json.load(sys.stdin); print([x['name'] for x in d] if isinstance(d,list) else d)\" 2>&1 | head -5", "timeout": 40}`
38. **bash** `{"command": "cd /tmp && for p in evals experiments .github/workflows; do echo \"=== $p ===\"; curl -s --max-time 25 \"https://api.github.com/repos/Companion-Inc/feynman/contents/$p\" | python3 -c \"import sys,json; d=json.load(sys.stdin); print('\\n'.join(f\\\"{x['type']:4} {x['size']:>8} {x['name']}\\\" for x in d) if isinstance(d,list) else str(d)[:200])\"; done", "timeout": 90}`
39. **bash** `{"command": "cd /work; tail -3 experiments/probe-bg.log; echo \"---\"; find experiments/runs/workflow-1/workspace -maxdepth 3 -type f 2>/dev/null | head -20", "timeout": 30}`
40. **bash** `{"command": "cd /tmp && curl -s --max-time 30 https://raw.githubusercontent.com/Companion-Inc/feynman/main/evals/README.md; echo \"=== questions.jsonl ===\"; curl -s --max-time 30 https://raw.githubusercontent.com/Companion-Inc/feynman/main/evals/questions.jsonl", "timeout": 90}`
41. **bash** `{"command": "cd /tmp && curl -s --max-time 30 https://raw.githubusercontent.com/Companion-Inc/feynman/main/evals/run.mjs > run.mjs && wc -l run.mjs && sed -n '1,120p' run.mjs", "timeout": 90}`
42. **bash** `{"command": "cd /tmp && sed -n '120,302p' run.mjs", "timeout": 30}`
43. **bash** `{"command": "cd /work; tail -2 experiments/probe-bg.log; echo \"--- workflow files ---\"; find experiments/runs/workflow-1/workspace -type f | sed 's|.*/workspace/||' | sort | head -20; echo \"--- results listing ---\"; curl -s --max-time 25 \"https://api.github.com/repos/Companion-Inc/feynman/contents/evals/results\" | python3 -c \"import sys,json; d=json.load(sys.stdin); print('\\n'.join(f\\\"{x['size']:>8} {x['name']}\\\" for x in d) if isinstance(d,list) else str(d)[:200])\"", "timeout": 60}`
44. **bash** `{"command": "cd /tmp && for f in 2026-09-23-lit-ferrylane-openai_claude-sonnet-5 2026-09-24-lit-0.5.3-ferrylane-openai_gpt-5.6-terra 2026-09-24-lit-0.5.3-pre-wait-ferrylane-openai_gpt-5.6-terra 2026-09-24-lit-0.5.3-ferrylane_claude-opus-5-5; do echo \"=== $f ===\"; curl -s --max-time 20 \"https://raw.githubusercontent.com/Companion-Inc/feynman/main/evals/results/$f.md\"; echo; done", "timeout": 90}`
45. **bash** `{"command": "cd /work; ps aux | grep -c \"[r]un_probe.py\"; tail -2 experiments/probe-bg.log; echo \"--- files ---\"; find experiments/runs/workflow-1 -type f | sed 's|.*workflow-1/||' | sort | head; echo \"--- last assistant text ---\"; python3 - <<'PY'\nimport json,glob\nfor p in glob.glob('/work/experiments/runs/workflow-1/sessions/*.jsonl'):\n    rows=[json.loads(l) for l in open(p)]\n    txt=[b.get('text','') for r in rows for b in ((r.get('message') or {}).get('content') or []) if isinstance(b,dict) and b.get('type')=='text']\n    print(p.split('/')[-1], len(rows), 'entries')\n    print( …[+59 chars]`
46. **bash** `{"command": "mkdir -p /tmp/fev/evals/results /tmp/fev/work && cd /tmp/fev && cp /tmp/run.mjs evals/run.mjs && curl -s --max-time 25 https://raw.githubusercontent.com/Companion-Inc/feynman/main/evals/questions.jsonl -o evals/questions.jsonl && echo '{\"name\":\"feynman-audit\",\"version\":\"0.5.65\"}' > package.json && wc -l evals/questions.jsonl && python3 -c \"import scipy; print('scipy',scipy.__version__)\" 2>&1 | head -2", "timeout": 60}`
47. **bash** `{"command": "cd /tmp/fev && python3 - <<'PY'\nimport json, os, pathlib\nbase = pathlib.Path('/tmp/fev/work')\nq01_key_id = \"2408.03314\"\nq01_key_title = \"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\"\n\ndef mk(name, body, provenance=True):\n    ws = base / name / \"ws\" / \"outputs\"\n    ws.mkdir(parents=True, exist_ok=True)\n    (base / name / \"home\").mkdir(parents=True, exist_ok=True)\n    (base / name / \"tmp\").mkdir(parents=True, exist_ok=True)\n    if body is not None:\n        (ws / \"review.md\").write_text(body)\n        if provena …[+3180 chars]`
48. **bash** `{"command": "cd /tmp/fev && node evals/run.mjs --rescore /tmp/fev/rows.jsonl 2>&1 | tail -20; echo \"=== raw rows ===\"; python3 -c \"\nimport json\nfor l in open('/tmp/fev/rows.jsonl'.replace('rows','rows')):\n    pass\nfor l in open('/tmp/fev/evals/results/rows.jsonl'):\n    r=json.loads(l); print(json.dumps({k:r.get(k) for k in ['id','completed','citations','citation_validity','title_match','key_recall','unresolved','title_mismatch']}))\n\"", "timeout": 300}`
   - _tool error:_ | id | done | cites | valid | title | recall | wall | tokens | cost |
|---|---|---|---|---|---|---|---|---|
| q01 | yes | 1 | 100% | 100% | 100% | -s | 0 | $0 |
| q01 | yes | 2 | 100% | 50% | 100% | -s | 0 | $0 |
| q01 | yes | 5 | 100% | 100% | 0% | -s | 0 | $0 |
| q01 | yes | 1 | 0% | - | 0% | -s | …[+357 chars]
49. **bash** `{"command": "cd /work; ps aux | grep -c \"[r]un_probe.py\"; tail -3 experiments/probe-bg.log; echo \"--- artifacts now ---\"; find experiments/runs/workflow-1/workspace -type f | sed 's|.*/workspace/||' | sort; echo \"--- version string in trace ---\"; grep -o '.\\{60\\}0\\.5\\.65.\\{60\\}' experiments/runs/det-1/sessions/*.jsonl | head -3", "timeout": 30}`
50. **bash** `{"command": "cd /work/experiments/runs/workflow-1; ls; echo \"=== stdout (last 40 lines) ===\"; tail -20 stdout.txt 2>/dev/null; echo \"=== provenance ===\"; cat workspace/outputs/*.provenance.md 2>/dev/null; echo \"=== final output ===\"; head -40 workspace/outputs/transformer-wmt14-bleu.md", "timeout": 30}`
51. **bash** `{"command": "cd /work/experiments/runs/workflow-1; echo \"=== verification draft ===\"; cat workspace/outputs/.drafts/*-verification.md 2>/dev/null | head -40; echo \"=== plan ===\"; head -30 workspace/outputs/.plans/*.md", "timeout": 30}`
52. **bash** `{"command": "cd /work; sleep 20; ps aux | grep \"[r]un_probe.py\" | head -3; echo \"--- meta exists? ---\"; ls experiments/runs/workflow-1/meta.json 2>/dev/null; tail -3 experiments/probe-bg.log", "timeout": 120}`
53. **bash** `{"command": "cd /work && python3 - <<'PY'\nimport json,glob,re\np=glob.glob('/work/experiments/runs/workflow-1/sessions/*.jsonl')[0]\nrows=[json.loads(l) for l in open(p)]\ncalls=[]\nfor r in rows:\n    m=r.get('message') or {}\n    for b in (m.get('content') or []):\n        if isinstance(b,dict) and b.get('type')=='toolCall':\n            calls.append((b.get('name'), b.get('arguments')))\nprint(\"tool calls:\",len(calls))\nfor i,(n,a) in enumerate(calls,1):\n    s=json.dumps(a)\n    print(f\"{i:2} {n:32} {s[:150]}\")\nprint(\"\\n=== fetched/queried URLs ===\")\nurls=set()\nfor n,a in calls:\ …[+499 chars]`
54. **bash** `{"command": "cd /work && python3 - <<'PY'\nimport json,glob,re\nfinal=open('/work/experiments/runs/workflow-1/workspace/outputs/transformer-wmt14-bleu.md').read()\nrows=[json.loads(l) for l in open(glob.glob('/work/experiments/runs/workflow-1/sessions/*.jsonl')[0])]\nfetched=set()\nfor r in rows:\n    for b in ((r.get('message') or {}).get('content') or []):\n        if isinstance(b,dict) and b.get('type')=='toolCall':\n            a=b.get('arguments') or {}\n            if b.get('name')=='fetch_content': fetched.add(a.get('url'))\ncited=set(re.findall(r'\\((https?://[^)\\s]+)\\)', final))\npr …[+342 chars]`
55. **bash** `{"command": "cd /tmp && curl -sL --max-time 30 \"https://papers.nips.cc/paper_files/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html\" | python3 -c \"import sys,re,html; t=sys.stdin.read(); t=re.sub(r'<[^>]+>',' ',t); t=html.unescape(t); t=re.sub(r'\\s+',' ',t); import re as r; m=r.search(r'.{200}27\\.5.{200}',t); print(m.group(0) if m else '27.5 NOT FOUND; len=%d'%len(t))\"", "timeout": 60}`
56. **bash** `{"command": "cd /opt/feynman/feynman-0.5.65-linux-arm64/app; echo \"=== temperature in pi packages ===\"; grep -rIl \"temperature\" node_modules/@earendil-works/pi-ai/dist node_modules/@earendil-works/pi-coding-agent/dist 2>/dev/null | head -5; echo \"--- count of temperature assignments ---\"; grep -rIoh \"temperature[=:][^,;)}]*\" node_modules/@earendil-works/pi-ai/dist 2>/dev/null | sort | uniq -c | sort -rn | head -10", "timeout": 60}`
57. **bash** `{"command": "cd /tmp && curl -s --max-time 30 https://raw.githubusercontent.com/Companion-Inc/feynman/main/.github/workflows/e2e.yml -o e2e.yml; grep -n -iE 'eval|questions|run\\.mjs|npm test' e2e.yml | head -20; echo \"=== publish.yml ===\"; curl -s --max-time 30 https://raw.githubusercontent.com/Companion-Inc/feynman/main/.github/workflows/publish.yml -o publish.yml; grep -n -iE 'eval|run\\.mjs|npm test' publish.yml | head -20", "timeout": 60}`
58. **bash** `{"command": "cd /tmp && for f in 2026-09-23-lit-ferrylane-openai_claude-sonnet-5 2026-09-24-lit-0.5.3-ferrylane-openai_gpt-5.6-terra 2026-09-24-lit-0.5.3-ferrylane_claude-opus-5-5 2026-09-24-lit-0.5.3-pre-wait-ferrylane-openai_gpt-5.6-terra; do curl -s --max-time 20 \"https://raw.githubusercontent.com/Companion-Inc/feynman/main/evals/results/$f.jsonl\" -o \"res-$f.jsonl\"; done; python3 - <<'PY'\nimport json,glob\nfor p in sorted(glob.glob('/tmp/res-*.jsonl')):\n    rows=[json.loads(l) for l in open(p) if l.strip()]\n    print(p.split('res-')[1][:60], '| n=',len(rows), '| ids=',[r['id'] for r  …[+172 chars]`
59. **bash** `{"command": "cd /work && python3 - <<'PY'\nimport math\ndef wilson(k,n,z=1.959963984540054):\n    if n==0: return (0,0)\n    p=k/n; d=1+z*z/n; c=(p+z*z/(2*n))/d; h=z*math.sqrt(p*(1-p)/n+z*z/(4*n*n))/d\n    return (max(0,c-h),min(1,c+h))\nfor k,n,label in [(4,4,'done 4/4'),(3,4,'done 3/4'),(12,12,'recall 12/12 (hypothetical)'),(180,180,'citations valid 180/180'),(51,51,'sonnet citations 51/51'),(44,44,'terra 44/44'),(85,85,'opus 85/85')]:\n    lo,hi=wilson(k,n); print(f\"{label:34} {k}/{n}={k/n:.3f}  Wilson95%=[{lo:.3f},{hi:.3f}]\")\nPY", "timeout": 30}`
60. **bash** `{"command": "cd /tmp && for f in 2026-09-24-lit-0.5.3-pre-wait-ferrylane_claude-opus-5-5 2026-09-24-lit-ferrylane-openai_gpt-5.6-terra; do curl -s --max-time 20 \"https://raw.githubusercontent.com/Companion-Inc/feynman/main/evals/results/$f.jsonl\" -o \"res-$f.jsonl\"; done; python3 - <<'PY'\nimport json,glob\nfor p in sorted(glob.glob('/tmp/res-*.jsonl')):\n    rows=[json.loads(l) for l in open(p) if l.strip()]\n    print(f\"{p.split('res-')[1][:62]:62} n={len(rows)} ids={[r['id'] for r in rows]}\")\nPY", "timeout": 60}`
61. **bash** `{"command": "mkdir -p /work/experiments/scorer-audit && cd /tmp/fev && cp evals/run.mjs evals/questions.jsonl package.json /work/experiments/scorer-audit/ 2>/dev/null; cp /tmp/fev/rows.jsonl /work/experiments/scorer-audit/rescored-rows.jsonl; cd /work/experiments/scorer-audit && python3 - <<'PY'\nimport json, pathlib\nrows=[json.loads(l) for l in open('rescored-rows.jsonl')]\nout=[\"# Scorer audit: synthetic artifacts scored by evals/run.mjs --rescore\\n\"]\nout.append(\"Command: `node evals/run.mjs --rescore rescored-rows.jsonl` (run.mjs from Companion-Inc/feynman@main, 2026-11-14)\\n\")\nfor …[+814 chars]`
62. **bash** `{"command": "cd /work/experiments/scorer-audit && cp /tmp/fev/evals/run.mjs ./run.mjs && ls -la && md5sum run.mjs /tmp/fev/evals/run.mjs && head -3 run.mjs", "timeout": 30}`
63. **bash** `{"command": "cd /work && python3 - <<'PY' > notes/feynman-eval-quality-traces.md\nimport json,glob,os\nprint(\"# Raw trace summary (auto-generated)\\n\")\nprint(\"| run | wall_s | turns | calls | results | tool errors | unpaired | usage complete | cost_usd | tokens | first-call input tokens |\")\nprint(\"|---|---|---|---|---|---|---|---|---|---|---|\")\nfor p in sorted(glob.glob('/work/experiments/runs/*/meta.json')):\n    m=json.load(open(p))\n    name=f\"{m['probe']}-{m['index']}\"\n    for t in m['traces']:\n        # first assistant usage in that trace\n        first_in=None\n        for l …[+890 chars]`
   - _said:_ Now I'll write the deliverable. First the reproducible experiment bundle notes, then the report.
64. **write** `{"content": "# Experiments: Feynman eval-quality case study\n\nEverything here is reproducible from a clean checkout of this workspace plus network\naccess. No credentials are stored.\n\n## 1. Behavioural probes (`run_probe.py`)\n\nSpawns the installed CLI as an isolated subprocess per run:\n\n- fresh `--cwd` under `experiments/runs/<probe>-<n>/workspace`\n- fresh `--session-dir` under `experiments/runs/<probe>-<n>/sessions`\n- `PI_SESSION_FILE` / `PI_SESSION_ID` stripped so the child cannot append to the\n  parent session\n- `FEYNMAN_TELEMETRY=off`\n- model `openrouter/deepseek/deepseek-v4.1- …[+2192 chars]`
65. **bash** `{"command": "cd /work && cat experiments/scorer-audit/RESULTS.md | head -50", "timeout": 30}`
66. **bash** `{"command": "cd /tmp && for f in 2026-09-24-lit-ferrylane-openai_gpt-5.6-terra 2026-09-24-lit-0.5.3-pre-wait-ferrylane_claude-opus-5-5; do echo \"=== $f ===\"; curl -s --max-time 20 \"https://raw.githubusercontent.com/Companion-Inc/feynman/main/evals/results/$f.md\"; echo; done; echo \"=== readback experiments/README ===\"; sed -n '30,40p' /work/experiments/README.md", "timeout": 60}`
67. **bash** `{"command": "cd /tmp && python3 - <<'PY'\nimport json\np='/tmp/res-2026-09-24-lit-0.5.3-pre-wait-ferrylane_claude-opus-5-5.jsonl'\nfor l in open(p):\n    r=json.loads(l)\n    if r['id'] in ('q04','q07'):\n        print(json.dumps({k:r.get(k) for k in ['id','exit_code','timed_out','completed','wall_s','citations','key_recall']}), '| usage:',r.get('usage',{}).get('total_tokens'))\nPY", "timeout": 30}`
68. **write** `{"content": "# Feynman as an eval subject\n\n**A case study in measuring a research agent, using the agent's own tooling**\n\nVersion audited: `@companion-ai/feynman` **0.5.65** (installed at\n`/opt/feynman/feynman-0.5.65-linux-arm64/app`), plus `Companion-Inc/feynman@main`\nread on 2026-11-14 for the parts that are not shipped in the npm package.\n\n---\n\n## Summary\n\nFeynman is a better *instrument* than it is a *measurement*. Its persisted session\ntrace is unusually complete: 43/43 assistant turns across 7 probe runs carried token\nusage, every one of 45 tool calls had a matching result, …[+25023 chars]`
69. **bash** `{"command": "cd /work && python3 -c \"\nimport math\ndef w(k,n,z=1.959963984540054):\n    p=k/n; d=1+z*z/n; c=(p+z*z/(2*n))/d; h=z*math.sqrt(p*(1-p)/n+z*z/(4*n*n))/d; return c-h,c+h\nprint('305/305', [round(x,4) for x in w(305,305)])\nprint('305 sum check', 51+43+44+28+54+85)\n\"; grep -n \"180/180\\|four of six\\|ferry\\|ferry\" outputs/feynman-eval-quality-case-study.md | head", "timeout": 30}`
70. **bash** `{"command": "cd /work && grep -n \"key-paper recall\\|100% citation validity\" outputs/feynman-eval-quality-case-study.md; echo \"--- exact remote filename ---\"; curl -s --max-time 20 \"https://api.github.com/repos/Companion-Inc/feynman/contents/evals/results\" | python3 -c \"\nimport sys,json\nfor x in json.load(sys.stdin):\n    if 'gpt-5.6-terra.md' in x['name']: print(repr(x['name']))\n\"", "timeout": 60}`
71. **read** `{"path": "/work/outputs/feynman-eval-quality-case-study.md", "offset": 28, "limit": 20}`
72. **edit** `{"path": "/work/outputs/feynman-eval-quality-case-study.md", "edits": [{"oldText": "| 180/180 citations valid (all runs pooled) | 100% | [97.9%, 100%] |", "newText": "| 305/305 citations valid (all six runs pooled) | 100% | [98.8%, 100%] |"}, {"oldText": "2. **Only 4 of 12 questions have ever been run** in a committed result, and one run used\n   only 2. The 8 unrun items are exactly the harder, non-ML/biology ones for q10–q12 plus\n   q02/q03/q05/q06/q08/q09 — so the reported rates are over a non-random, easier subset.", "newText": "2. **Only 4 of 12 questions have ever been run** in a commit …[+354 chars]`
73. **read** `{"limit": 130, "offset": 48, "path": "/work/outputs/feynman-eval-quality-case-study.md"}`
74. **read** `{"limit": 140, "offset": 178, "path": "/work/outputs/feynman-eval-quality-case-study.md"}`
75. **edit** `{"edits": [{"oldText": "  powered (n≈180) but is saturated and format-driven", "newText": "  powered (n=305) but is saturated and format-driven"}, {"oldText": "- no explicit parent/child link between a subagent session file and its parent (usage\n  aggregation works by directory walking, which is why run.mjs walks `home/` and `tmp/`).", "newText": "- no parent/child link in the session headers inspected (usage aggregation works by\n  directory walking, which is why run.mjs walks `home/` and `tmp/`; subagent sessions\n  were not exercised in these probes, so this is a schema observation, not a  …[+71 chars]`
   - _tool error:_ Could not find edits[0] in /work/outputs/feynman-eval-quality-case-study.md. The oldText must match exactly including all whitespace and newlines.
76. **bash** `{"command": "cd /work && grep -n \"n≈180\\|n=180\\|powered\" outputs/feynman-eval-quality-case-study.md; grep -n \"parent/child\" outputs/feynman-eval-quality-case-study.md", "timeout": 30}`
77. **edit** `{"edits": [{"oldText": "powered (n≈180) but is saturated and format-driven, so precision is high and validity is", "newText": "powered (n=305) but is saturated and format-driven, so precision is high and validity is"}, {"oldText": "- no explicit parent/child link between a subagent session file and its parent (usage\n  aggregation works by directory walking, which is why run.mjs walks `home/` and `tmp/`).", "newText": "- no parent/child link in the session headers inspected (usage aggregation works by\n  directory walking, which is why run.mjs walks `home/` and `tmp/`; subagent sessions\n  wer …[+143 chars]`
78. **read** `{"limit": 160, "offset": 318, "path": "/work/outputs/feynman-eval-quality-case-study.md"}`
79. **bash** `{"command": "cd /work/experiments/runs && md5sum det-*/workspace/result.txt; echo \"---\"; for f in det-*/workspace/result.txt; do echo \"$f: $(wc -c < $f) bytes\"; od -c \"$f\" | tail -2; done", "timeout": 30}`
80. **edit** `{"edits": [{"oldText": "Final artifacts were byte-identical in content (all three `result.txt` contain the exact\ntitle). So: **artifact stable, trajectory unstable, cost 2.4×**. Two implications:", "newText": "All three `result.txt` files contain the same title; det-2 and det-3 are byte-identical\n(md5 `80ecf52d…`) and det-1 differs only by a missing trailing newline (`ee6df5da…`).\nSo: **artifact stable, trajectory unstable, cost 2.4×**. Two implications:"}], "path": "/work/outputs/feynman-eval-quality-case-study.md"}`
81. **write** `{"content": "# Provenance: Feynman as an eval subject\n\n- **Date:** 2026-11-14\n- **Rounds:** 3 (static package audit → behavioural probes → scorer audit), plus 1 end-to-end workflow run\n- **Verification:** PASS WITH NOTES\n- **Plan:** `outputs/.plans/feynman-eval-quality-case-study.md`\n- **Final artifact:** `outputs/feynman-eval-quality-case-study.md`\n\n## Source accounting\n\nEvery consulted source is dispositioned, and the counts close: **15 consulted = 14\naccepted + 1 negative control + 0 rejected.** (This is deliberate: the audited harness's\nown provenance sidecar failed exactly thi …[+3658 chars]`
82. **write** `{"content": "# Lab notebook\n\n## 2026-11-14 — slug: feynman-eval-quality-case-study\n\n- Scope: audit `@companion-ai/feynman` 0.5.65 as an AI-eval subject (instrumentation,\n  reproducibility, scorer validity, self-report auditability), with the harness dogfooding\n  its own tooling.\n- Static audit: package, prompts, `dist/`, `RELEASES.md`. Found no temperature/seed control\n  and no harness-version field in the session trace; full system prompt + tool schemas are\n  persisted.\n- Corrected an early wrong assumption: the repo **does** ship an eval suite (`evals/`,\n  12 questions, determinis …[+1659 chars]`
83. **edit** `{"edits": [{"oldText": "| T1 | Static audit of package | read AGENTS.md, SYSTEM.md, prompts/, dist internals, package manifest | planned |\n| T2 | Trace integrity audit | parse persisted session JSONL; count turns with usage, tool-call/result pairing, timing coverage | planned |\n| T3 | Determinism probe (D1) | 3 identical tool-using prompts, fixed model+thinking, compare tool sequences/outputs | planned |\n| T4 | Confabulation trap (D5) | 2 runs asking for a paper that does not exist; score fabricated vs. refused | planned |\n| T5 | Ground-truth retrieval (D3) | 1 run, 5 bibliographic items + …[+1622 chars]`
84. **bash** `{"command": "cd /work && grep -n \"10–45\\|8 tool calls\\|9 evidence\\|17 tool calls total\" outputs/feynman-eval-quality-case-study.md", "timeout": 30}`
85. **edit** `{"edits": [{"oldText": "   and \"8 tool calls\" understates the 17 in the trace.", "newText": "   and its \"8 tool calls\" counts evidence calls only, without saying so (the trace has 17\n   tool calls including writes and shell)."}, {"oldText": "- \"Rounds: 1 research round (direct search, **8 tool calls**)\" vs 9 evidence calls\n  (1 ID lookup + 1 web search + 7 fetches) and 17 tool calls total in the trace.", "newText": "- The unit for \"tool calls\" is undeclared. \"8 tool calls\" is right if it means evidence\n  calls (1 arXiv ID lookup + 1 web search + 6 fetches = 8), but the trace has 1 …[+559 chars]`
86. **bash** `{"command": "cd /tmp && python3 - <<'PY'\nimport json,glob\ntot_c=0; toks=[]\nprint(f\"{'file':58} {'n':>2} {'done':>5} {'cites':>5} {'tok_min':>9} {'tok_max':>9} {'wall_min':>6} {'wall_max':>6}\")\nfor p in sorted(glob.glob('/tmp/res-*.jsonl')):\n    rows=[json.loads(l) for l in open(p)]\n    c=sum(r['citations'] for r in rows); tot_c+=c\n    t=[r['usage']['total_tokens'] for r in rows]; w=[r['wall_s'] for r in rows]\n    toks+=t\n    print(f\"{p.split('res-')[1][:58]:58} {len(rows):2} {sum(1 for r in rows if r['completed'])}/{len(rows)} {c:5} {min(t):9} {max(t):9} {min(w)/60:6.1f} {max(w)/60 …[+224 chars]`
87. **bash** `{"command": "cd /work && ls -la outputs outputs/.plans experiments experiments/scorer-audit notes CHANGELOG.md | head -40; echo \"=== artifact line count ===\"; wc -l outputs/feynman-eval-quality-case-study.md outputs/feynman-eval-quality-case-study.provenance.md", "timeout": 30}`
88. **bash** `{"command": "cd /work && grep -n \"2.1M–26.6M\\|millions of tokens per question\" outputs/feynman-eval-quality-case-study.md", "timeout": 30}`
89. **edit** `{"edits": [{"oldText": "  2.1M–26.6M, so the cost column is not a rounding artifact — it is unexercised.", "newText": "  19,452 to 26,551,212, so the cost column is not a rounding artifact — it is\n  unexercised."}, {"oldText": "  7–45 min and millions of tokens per question. Saturation and coverage findings are", "newText": "  7–45 min and 2.6M–26.6M tokens per completed question. Saturation and coverage findings are"}], "path": "/work/outputs/feynman-eval-quality-case-study.md"}`
90. **bash** `{"command": "cd /work && python3 - <<'PY'\nimport re\np='outputs/feynman-eval-quality-case-study.md'\ns=open(p).read()\ns=s.replace(\"7–45 min and 2.6M–26.6M tokens per completed question\",\"7–45 min and 2.1M–26.6M tokens per completed question\")\nopen(p,'w').write(s)\nprint(\"ok\")\nPY\ngrep -n \"2.1M–26.6M\\|19,452 to\" outputs/feynman-eval-quality-case-study.md; sed -n '312,322p' outputs/feynman-eval-quality-case-study.md", "timeout": 30}`
91. **read** `{"limit": 28, "offset": 20, "path": "/work/outputs/feynman-eval-quality-case-study.md"}`
92. **read** `{"limit": 14, "offset": 230, "path": "/work/outputs/feynman-eval-quality-case-study.md"}`
93. **bash** `{"command": "cd /work && python3 - <<'PY'\np='outputs/feynman-eval-quality-case-study.md'\ns=open(p).read()\ns=s.replace(\"Token counts in the same rows run to\\n  19,452 to 26,551,212, so the cost column\",\"Per-question token counts in the same rows\\n  range from 19,452 to 26,551,212, so the cost column\")\ns=s.replace(\"Five concrete findings:\\n\",\"The findings that matter for eval design (sections 9–10 add two supporting probes):\\n\")\nopen(p,'w').write(s)\nprint(\"done\")\nPY\ngrep -n \"supporting probes\\|Per-question token\" outputs/feynman-eval-quality-case-study.md", "timeout": 30 …[+1 chars]`
94. **bash** `{"command": "cd /work && python3 - <<'PY'\np='outputs/feynman-eval-quality-case-study.md'\ns=open(p).read()\ns=s.replace(\"arXiv ID was the only case the scorer rejected.\",\"arXiv ID was the only case that failed the validity check.\")\nopen(p,'w').write(s)\nPY\ngrep -n \"only case\" outputs/feynman-eval-quality-case-study.md; echo \"=== placeholders ===\"; grep -n \"TODO\\|TBD\\|XXX\\|FIXME\" outputs/feynman-eval-quality-case-study.md || echo none; echo \"=== 180 refs ===\"; grep -n \"180\" outputs/feynman-eval-quality-case-study.md || echo none; echo \"=== paths exist? ===\"; for f in outpu …[+420 chars]`
   - _said:_ Done. The artifact is at `outputs/feynman-eval-quality-case-study.md`, with a reproducible experiment bundle in `experiments/`.

## What the case study found

**The harness is a better instrument than it is a measurement.**

Its session trace is unusually strong: across 7 isolated probe runs, 43/43 assistant turns carried token usage, 45/45 tool calls had matching results, and the trace stores the …[+2311 chars]

Last stopReason: `stop` (assistant messages this turn: 65)

## Final reply

Done. The artifact is at `outputs/feynman-eval-quality-case-study.md`, with a reproducible experiment bundle in `experiments/`.

## What the case study found

**The harness is a better instrument than it is a measurement.**

Its session trace is unusually strong: across 7 isolated probe runs, 43/43 assistant turns carried token usage, 45/45 tool calls had matching results, and the trace stores the full system prompt and every tool schema the model saw. You can audit a run after the fact without the harness author's cooperation.

The repo's own eval — which I initially assumed didn't exist, then found at `evals/` — is real and well-built: 12 questions, deterministic citation resolution, per-question isolated `FEYNMAN_HOME`, rescoring support, and it caught a genuine `bg_wait` regression. But I ran its scorer unmodified against five synthetic artifacts, and the result is the centerpiece:

| Synthetic artifact | done | valid | title | recall |
|---|---|---|---|---|
| Correct format, states the **opposite** of the paper's finding | yes | 100% | 100% | 100% |
| Five valid but totally irrelevant citations | yes | 100% | 100% | 0% |
| Valid ID, wrong title | yes | 100% | 50% | 100% |
| Fabricated arXiv ID | yes | 0% | – | 0% |

The scorer never checks claim–source alignment or citation precision. Supporting evidence: all six committed result files report 100% citation validity (305/305); only 4 of the 12 questions have ever been run; cost is `$0.00` in every committed run because the `models.json` entry lacks a cost block; and 4/4 completion has a Wilson 95% CI of [51%, 100%].

Two probes went the harness's way: a fabricated-paper trap was refused 2/2 with tool-grounded checks, and one `/deepresearch` run's `PASS WITH NOTES` label was substantively earned — 6/6 cited URLs were actually fetched, and I independently confirmed its 27.5-vs-28.4 NeurIPS metadata finding. But the provenance arithmetic didn't reconcile (8 consulted vs 6 accepted + 1 rejected), and the label came from the same model rather than from a check.

Also measured: identical prompts produced 2/6/3 tool calls and 31.7k/76.2k/43.4k tokens with the same final artifact — score artifacts, not trajectories.

**Not run:** the full 12-question eval (7–45 min and 2.1M–26.6M tokens per completed question), multi-model replication, and a harder fabrication trap. All marked in the artifact's limits section.

## Sources

- Artifact: `outputs/feynman-eval-quality-case-study.md`; provenance: `…provenance.md`
- Eval suite: https://github.com/Companion-Inc/feynman/tree/main/evals
- Committed baselines: https://github.com/Companion-Inc/feynman/tree/main/evals/results
- Scorer audit: `experiments/scorer-audit/RESULTS.md`

## Files created this turn

- state/.feynman/sessions/2026-11-14T08-56-30-974Z_01a1d945-c5fd-7751-a124-5072bd26f585.jsonl
- work/CHANGELOG.md
- work/experiments/README.md
- work/experiments/probe-bg.log
- work/experiments/probe-results.json
- work/experiments/run_probe.py
- work/experiments/runs/det-1/meta.json
- work/experiments/runs/det-1/sessions/2026-11-14T08-57-49-244Z_01a1d946-f7bb-70cb-a858-28f4f33689af.jsonl
- work/experiments/runs/det-1/stderr.txt
- work/experiments/runs/det-1/stdout.txt
- work/experiments/runs/det-1/workspace/result.txt
- work/experiments/runs/det-2/meta.json
- work/experiments/runs/det-2/sessions/2026-11-14T08-57-56-490Z_01a1d947-140a-7307-8215-e610363de7c1.jsonl
- work/experiments/runs/det-2/stderr.txt
- work/experiments/runs/det-2/stdout.txt
- work/experiments/runs/det-2/workspace/result.txt
- work/experiments/runs/det-3/meta.json
- work/experiments/runs/det-3/sessions/2026-11-14T08-58-07-786Z_01a1d947-4029-7615-9f81-0e6d554e9b46.jsonl
- work/experiments/runs/det-3/stderr.txt
- work/experiments/runs/det-3/stdout.txt
- work/experiments/runs/det-3/workspace/result.txt
- work/experiments/runs/ground-1/meta.json
- work/experiments/runs/ground-1/sessions/2026-11-14T08-59-03-265Z_01a1d948-18e0-7655-89e1-403bd315a025.jsonl
- work/experiments/runs/ground-1/stderr.txt
- work/experiments/runs/ground-1/stdout.txt
- work/experiments/runs/smoke/sessions/2026-11-14T08-57-20-317Z_01a1d946-86bc-7684-9244-4c73ad3f9f0c.jsonl
- work/experiments/runs/trap-1/meta.json
- work/experiments/runs/trap-1/sessions/2026-11-14T08-58-15-255Z_01a1d947-5d57-744b-b62f-451924d2fea9.jsonl
- work/experiments/runs/trap-1/stderr.txt
- work/experiments/runs/trap-1/stdout.txt
- work/experiments/runs/trap-1/workspace/notes/citation-check-okafor-2023.md
- work/experiments/runs/trap-2/meta.json
- work/experiments/runs/trap-2/sessions/2026-11-14T08-58-39-346Z_01a1d947-bb71-77e3-88b6-c490bf8fa1cf.jsonl
- work/experiments/runs/trap-2/stderr.txt
- work/experiments/runs/trap-2/stdout.txt
- work/experiments/runs/workflow-1/meta.json
- work/experiments/runs/workflow-1/sessions/2026-11-14T08-59-10-241Z_01a1d948-3421-7459-9fbc-6fb5deb51423.jsonl
- work/experiments/runs/workflow-1/stderr.txt
- work/experiments/runs/workflow-1/stdout.txt
- work/experiments/runs/workflow-1/workspace/outputs/.drafts/transformer-wmt14-bleu-cited.md
- work/experiments/runs/workflow-1/workspace/outputs/.drafts/transformer-wmt14-bleu-draft.md
- work/experiments/runs/workflow-1/workspace/outputs/.drafts/transformer-wmt14-bleu-research-direct.md
- work/experiments/runs/workflow-1/workspace/outputs/.drafts/transformer-wmt14-bleu-verification.md
- work/experiments/runs/workflow-1/workspace/outputs/.plans/transformer-wmt14-bleu.md
- work/experiments/runs/workflow-1/workspace/outputs/transformer-wmt14-bleu.md
- work/experiments/runs/workflow-1/workspace/outputs/transformer-wmt14-bleu.provenance.md
- work/experiments/scorer-audit/RESULTS.md
- work/experiments/scorer-audit/package.json
- work/experiments/scorer-audit/questions.jsonl
- work/experiments/scorer-audit/rescored-rows.jsonl
- work/experiments/scorer-audit/run.mjs
- work/notes/feynman-eval-quality-traces.md
- work/outputs/.plans/feynman-eval-quality-case-study.md
- work/outputs/feynman-eval-quality-case-study.md
- work/outputs/feynman-eval-quality-case-study.provenance.md

## Files modified this turn

(none)
