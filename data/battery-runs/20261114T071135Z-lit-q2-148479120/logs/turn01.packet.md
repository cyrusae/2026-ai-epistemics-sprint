# Evidence packet: 20261114T071135Z-lit-q2-148479120 / turn01

Mechanically extracted from the Feynman session log and filesystem. No interpretation applied.

## Prompt

```
I'm interested in a case study of the Feynman harness from an AI-eval-quality perspective, so dogfooding it a bit.
```

## Run metadata

`{"turn":1,"exa":true,"mode":"new","exit_code":0,"seconds":385,"model":"openrouter/deepseek/deepseek-v4.1-flash-1017","prompt":"p1.md","prompt_sha256":"f3b1050bf027"}`

## Agent actions (in order)

   - _said:_ I'll start by investigating what's actually on disk — the harness itself — before making any claims about it.
1. **bash** `{"command": "echo \"=== CWD ===\"; pwd; echo; echo \"=== /work ===\"; ls -la /work | head -50; echo; echo \"=== Feynman install ===\"; ls -la /opt/feynman/feynman-0.5.65-linux-arm64/app | head -60; echo; echo \"=== version ===\"; cat /opt/feynman/feynman-0.5.65-linux-arm64/app/package.json 2>/dev/null | head -40", "timeout": 60}`
2. **bash** `{"command": "echo \"=== env (filtered) ===\"; env | grep -iE 'feynman|model|openai|anthropic|eval' | sed 's/=.*KEY.*/=<redacted>/' | head -40; echo; echo \"=== node/python ===\"; node --version 2>/dev/null; python3 --version 2>/dev/null; echo; echo \"=== feynman binary ===\"; which feynman; ls -la /opt/feynman/ 2>/dev/null", "timeout": 60}`
3. **bash** `{"command": "cd /opt/feynman/feynman-0.5.65-linux-arm64/app; echo \"=== README ===\"; cat README.md; echo; echo \"=== .feynman tree ===\"; find .feynman -maxdepth 3 | head -60; echo; echo \"=== prompts ===\"; ls -la prompts; echo; echo \"=== metadata ===\"; ls -la metadata; echo; echo \"=== skills ===\"; ls skills", "timeout": 60}`
4. **bash** `{"command": "cd /opt/feynman/feynman-0.5.65-linux-arm64/app; echo \"=== dist top ===\"; ls -la dist | head -40; echo; echo \"=== find eval-ish files ===\"; find . -path ./node_modules -prune -o -iname '*eval*' -print 2>/dev/null | head -40; echo; echo \"=== find test files ===\"; find . -path ./node_modules -prune -o -iname '*.test.*' -print -o -iname '*.spec.*' -print 2>/dev/null | head -40; echo; echo \"=== package.json scripts ===\"; python3 -c \"import json;d=json.load(open('package.json'));print(json.dumps(d.get('scripts',{}),indent=1))\"", "timeout": 60}`
5. **bash** `{"command": "cd /opt/feynman/feynman-0.5.65-linux-arm64/app; echo \"===== SYSTEM.md =====\"; cat .feynman/SYSTEM.md; echo; echo \"===== settings.json =====\"; cat .feynman/settings.json", "timeout": 60}`
6. **bash** `{"command": "cd /opt/feynman/feynman-0.5.65-linux-arm64/app; for f in .feynman/agents/*.md; do echo \"===== $f =====\"; cat \"$f\"; echo; done", "timeout": 60}`
7. **bash** `{"command": "cd /opt/feynman/feynman-0.5.65-linux-arm64/app; echo \"=== dist/system ===\"; ls -la dist/system dist/search dist/pi dist/model dist/config; echo; echo \"=== grep eval/bench ===\"; grep -rilE '\\beval(uation)?\\b|benchmark' dist .feynman prompts skills 2>/dev/null | head -30", "timeout": 60}`
8. **bash** `{"command": "cd /opt/feynman/feynman-0.5.65-linux-arm64/app; echo \"=== deepresearch.md ===\"; cat prompts/deepresearch.md; echo; echo \"=== lit.md ===\"; cat prompts/lit.md", "timeout": 60}`
9. **bash** `{"command": "cd /opt/feynman/feynman-0.5.65-linux-arm64/app; echo \"=== telemetry ===\"; ls -la dist/telemetry; for f in dist/telemetry/*; do echo \"--- $f\"; head -80 \"$f\"; done", "timeout": 60}`
10. **bash** `{"command": "cd /opt/feynman/feynman-0.5.65-linux-arm64/app; echo \"=== release notes: eval/bench/test mentions ===\"; grep -niE 'eval|benchmark|citation|hallucinat|verif|provenance' RELEASES.md | head -60; echo; echo \"=== first 40 lines ===\"; head -40 RELEASES.md", "timeout": 60}`
11. **bash** `{"command": "cd /opt/feynman/feynman-0.5.65-linux-arm64/app; sed -n '440,530p' RELEASES.md", "timeout": 60}`
12. **bash** `{"command": "cd /opt/feynman/feynman-0.5.65-linux-arm64/app; echo \"=== all 'eval' occurrences ===\"; grep -nioE '.{80}\\beval(uation|s)?\\b.{120}' RELEASES.md | head -40; echo; echo \"=== 'benchmark' occurrences ===\"; grep -nioE '.{60}benchmark.{100}' RELEASES.md | head -30", "timeout": 60}`
13. **bash** `{"command": "cd /opt/feynman/feynman-0.5.65-linux-arm64/app; echo \"=== grep -n eval ===\"; grep -n \"eval\" RELEASES.md | head; echo; echo \"=== package.json full ===\"; cat package.json; echo; echo \"=== files count in dist ===\"; find dist -name '*.js' | wc -l", "timeout": 60}`
14. **bash** `{"command": "timeout 25 curl -sS -o /dev/null -w \"github: %{http_code}\\n\" https://api.github.com/repos/Companion-Inc/feynman 2>&1; timeout 25 curl -sS -o /dev/null -w \"raw: %{http_code}\\n\" https://raw.githubusercontent.com/Companion-Inc/feynman/main/package.json 2>&1", "timeout": 60}`
15. **bash** `{"command": "cd /tmp && timeout 40 curl -sS \"https://api.github.com/repos/Companion-Inc/feynman/git/trees/main?recursive=1\" -o tree.json; python3 - <<'EOF'\nimport json\nd=json.load(open('/tmp/tree.json'))\nif 'tree' not in d:\n    print(d); raise SystemExit\npaths=[t['path'] for t in d['tree']]\nprint(\"total paths:\", len(paths))\nfor p in paths:\n    lp=p.lower()\n    if any(k in lp for k in ['test','eval','bench','fixture','golden','snapshot']):\n        print(p)\nEOF", "timeout": 90}`
16. **bash** `{"command": "cd /tmp && timeout 40 curl -sS \"https://api.github.com/repos/Companion-Inc/feynman/contents/tests\" | python3 -c \"import json,sys; d=json.load(sys.stdin); print([x['name'] for x in d] if isinstance(d,list) else d)\" 2>&1 | head -20", "timeout": 60}`
17. **bash** `{"command": "mkdir -p /work/notes/feynman-evals && cd /work/notes/feynman-evals; base=https://raw.githubusercontent.com/Companion-Inc/feynman/main/evals; for f in README.md questions.jsonl run.mjs; do echo \"--- $f\"; timeout 30 curl -sS \"$base/$f\" -o \"$(basename $f)\" && wc -c \"$(basename $f)\"; done; echo; echo \"=== README ===\"; cat README.md", "timeout": 120}`
18. **bash** `{"command": "cd /work/notes/feynman-evals; base=https://raw.githubusercontent.com/Companion-Inc/feynman/main/evals/results; for f in 2026-09-24-lit-0.5.3-ferrylane-openai_gpt-5.6-terra.jsonl 2026-09-24-lit-0.5.3-ferrylane-openai_gpt-5.6-terra.md; do timeout 30 curl -sS \"$base/$f\" -o \"$f\" && echo \"$f $(wc -c < $f) bytes\"; done; echo; echo \"=== md ===\"; head -60 2026-09-24-lit-0.5.3-ferrylane-openai_gpt-5.6-terra.md; echo; echo \"=== jsonl head ===\"; head -c 3000 2026-09-24-lit-0.5.3-ferrylane-openai_gpt-5.6-terra.jsonl", "timeout": 120}`
19. **bash** `{"command": "mv /work/2026-09-24-lit-0.5.3-ferrylane-openai_gpt-5.6-terra.* /work/notes/feynman-evals/ 2>/dev/null; ls -la /work/notes/feynman-evals; echo; echo \"=== questions.jsonl ===\"; cat /work/notes/feynman-evals/questions.jsonl", "timeout": 60}`
20. **bash** `{"command": "sed -n '1,200p' /work/notes/feynman-evals/run.mjs", "timeout": 60}`
21. **bash** `{"command": "sed -n '200,400p' /work/notes/feynman-evals/run.mjs", "timeout": 60}`
22. **bash** `{"command": "cd /work/notes/feynman-evals; base=https://raw.githubusercontent.com/Companion-Inc/feynman/main/evals/results; for f in 2026-09-23-lit-ferrylane-openai_claude-sonnet-5 2026-09-24-lit-0.5.3-pre-wait-ferrylane-openai_gpt-5.6-terra 2026-09-24-lit-0.5.3-pre-wait-ferrylane_claude-opus-5-5 2026-09-24-lit-0.5.3-ferrylane_claude-opus-5-5 2026-09-24-lit-ferrylane-openai_gpt-5.6-terra; do for ext in jsonl md; do timeout 30 curl -sS \"$base/$f.$ext\" -o \"$f.$ext\"; done; done; ls -la; echo; echo \"=== all md summaries ===\"; for f in *.md; do echo \"##### $f\"; cat \"$f\"; echo; done", "tim …[+11 chars]`
23. **bash** `{"command": "cd /opt/feynman/feynman-0.5.65-linux-arm64/app; echo \"=== recipe provenance ===\"; grep -n -i \"provenance\\|outputs/\\|verifier\\|reviewer\" prompts/recipe.md; echo; echo \"=== telemetry event property names ===\"; grep -nE \"capture\\(|properties|feynman_|tool_name|error\" dist/telemetry/posthog.js | head -60; echo; echo \"=== research-tools extension size ===\"; wc -l extensions/research-tools.ts; grep -nE \"feynman_tool_used|tool_used|capture|telemetry\" extensions/research-tools.ts | head -20", "timeout": 60}`
24. **bash** `{"command": "cd /opt/feynman/feynman-0.5.65-linux-arm64/app; sed -n '80,260p' dist/telemetry/posthog.js", "timeout": 60}`
   - _said:_ Now I'll test the harness's own eval scorer against deliberately defective documents — a canary suite for the evaluator itself.
25. **bash** `{"command": "set -e\nBASE=/work/experiments/feynman-eval-audit\nrm -rf \"$BASE\"; mkdir -p \"$BASE/evals\"\ncp /work/notes/feynman-evals/run.mjs /work/notes/feynman-evals/questions.jsonl \"$BASE/evals/\"\nmkdir -p \"$BASE/work\"\npython3 - <<'PY'\nimport json, os, pathlib\nbase = pathlib.Path('/work/experiments/feynman-eval-audit')\ncanaries = {\n 'c0-correct': ('test-time-compute-scaling.md', '''# Test-time compute\n\nScaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters (arXiv:2408.03314) reports that smaller models with extra inference compute can match …[+3261 chars]`
26. **bash** `{"command": "cd /work/experiments/feynman-eval-audit; python3 - <<'PY'\nimport json\nfor line in open('seed.jsonl'):\n    r=json.loads(line)\n    print(f\"{r['canary']:32s} id={r['id']} cites={r['citations']} checked={r.get('citations_checked')} valid={r.get('citation_validity')} title={r.get('title_match')} recall={r.get('key_recall')} unresolved={r.get('unresolved')} mismatch={[m['id']+':'+str(m['overlap']) for m in r.get('title_mismatch',[])]}\")\nPY", "timeout": 60}`
27. **bash** `{"command": "echo \"=== find a DataCite/Zenodo DOI ===\"; timeout 30 curl -sS \"https://api.datacite.org/dois?query=creators.name:%22Hutson%22&page%5Bsize%5D=1\" | python3 -c \"import json,sys;d=json.load(sys.stdin);print(d['data'][0]['id'] if d.get('data') else d)\" 2>&1; echo \"=== test known zenodo ===\"; for d in 10.5281/zenodo.10000035 10.5281/zenodo.8404160; do echo \"-- $d\"; timeout 20 curl -sS -o /dev/null -w \"crossref=%{http_code} \" \"https://api.crossref.org/works/$d\"; timeout 20 curl -sS \"https://doi.org/api/handles/$d\" | head -c 120; echo; done", "timeout": 120}`
28. **write** `{"path": "/work/experiments/feynman-eval-audit/make_canaries.py", "content": "#!/usr/bin/env python3\n\"\"\"Build canary documents for auditing Feynman's own evals/run.mjs scorer.\n\nEach canary is a minimal final output (plus provenance sidecar) whose seeded\ndefect is known. Running `node evals/run.mjs --rescore seed.jsonl` then shows\nwhich defect classes the shipped scorer can and cannot see.\n\"\"\"\nimport json\nimport pathlib\n\nBASE = pathlib.Path(__file__).resolve().parent\n\n# (name, question id, filename, body, seeded defect)\nCANARIES = [\n    (\"c0-correct\", \"q01\", \"test-time- …[+4600 chars]`
29. **bash** `{"command": "cd /work/experiments/feynman-eval-audit\npython3 make_canaries.py\ncp seed.jsonl seed-input.jsonl\ntimeout 300 node evals/run.mjs --rescore seed.jsonl > rescore-stdout.txt 2> rescore-stderr.txt\necho \"exit=$?\"\npython3 - <<'PY'\nimport json\nkey=json.load(open('/work/experiments/feynman-eval-audit/canary-key.json'))\nprint(f\"{'canary':30s} {'cites':>5s} {'valid':>6s} {'title':>6s} {'recall':>6s}  defect\")\nprint('-'*110)\nfor line in open('/work/experiments/feynman-eval-audit/seed.jsonl'):\n    r=json.loads(line)\n    v='-' if r.get('citation_validity') is None else f\"{r['cit …[+509 chars]`
30. **bash** `{"command": "cd /work/notes/feynman-evals; python3 - <<'PY'\nimport json, glob, os\nrows=[]\nfor f in sorted(glob.glob('*.jsonl')):\n    if f=='seed.jsonl': continue\n    for line in open(f):\n        r=json.loads(line)\n        rows.append((f,r))\nprint(f\"{'file':58s} {'ver':6s} {'sha':8s} {'dirty':5s} {'model':22s} {'id':4s} {'done':4s} {'cites':5s} {'valid':6s} {'title':6s} {'recall':6s} {'wall':6s} {'tokens':10s}\")\nfor f,r in rows:\n    v='-' if r.get('citation_validity') is None else f\"{r['citation_validity']*100:.0f}%\"\n    t='-' if r.get('title_match') is None else f\"{r['title_mat …[+654 chars]`
31. **bash** `{"command": "cd /opt/feynman/feynman-0.5.65-linux-arm64/app; echo \"=== README claim checks ===\"; echo \"-- agents count:\"; ls .feynman/agents/*.md | wc -l; echo \"-- provenance in lit/deepresearch/recipe:\"; for f in lit deepresearch recipe; do printf \"%s: \" $f; grep -c \"provenance\" prompts/$f.md; done; echo \"-- outputs vs papers:\"; grep -n \"papers/\" prompts/deepresearch.md | head -3; echo \"-- pi version pins:\"; python3 -c \"import json;d=json.load(open('package.json'));print({k:v for k,v in d['peerDependencies'].items() if 'pi-' in k})\"; echo \"-- telemetry opt-out accepted:\";  …[+102 chars]`
   - _tool error:_ file                                                       ver    sha      dirty model                  id   done cites valid  title  recall wall   tokens    
2026-09-23-lit-ferrylane-openai_claude-sonnet-5.jsonl      0.5.0  dbf1f6c  False claude-sonnet-5        q01  True    26 100%   92%    100%    …[+3530 chars]
32. **bash** `{"command": "cd /work/notes/feynman-evals; python3 - <<'PY'\nimport json, glob, os\nrows=[]\nfor f in sorted(glob.glob('*.jsonl')):\n    for line in open(f):\n        line=line.strip()\n        if not line: continue\n        rows.append((f,json.loads(line)))\nprint(\"rows:\",len(rows))\nfor f,r in rows:\n    if r.get('citations') is None or r.get('usage') is None:\n        print(\"ANOMALY\", os.path.basename(f), r)\nprint()\nfrom collections import Counter\nprint(\"git_dirty:\", Counter(r.get('git_dirty') for _,r in rows))\nprint(\"versions:\", Counter(r.get('feynman_version') for _,r in rows) …[+691 chars]`
   - _said:_ The scorer audit is done. Now a bounded generator–verifier canary: seed a draft with known defects and see whether the harness's own `verifier` agent catches what the scorer misses.
33. **bash** `{"command": "set -e\nD=/work/experiments/feynman-verifier-canary\nrm -rf \"$D\"; mkdir -p \"$D\"\ncat > \"$D/draft.md\" <<'EOF'\n# Inference-time methods: a short brief\n\nTest-time compute scaling improves accuracy by 400% on GSM8K (arXiv:2408.03314). This makes extra inference compute a universal substitute for model parameters.\n\nSpeculative decoding was introduced by Leviathan et al. (2023) and achieves a 10x speedup on every model tested (arXiv:2211.17192). It is therefore the default decoding strategy.\n\nSparse autoencoders were shown to recover all features in GPT-4 (arXiv:2499.99999) …[+1909 chars]`
34. **subagent** `{"agent": "verifier", "task": "Verify the draft at /work/experiments/feynman-verifier-canary/draft.md against the supplied research notes at /work/experiments/feynman-verifier-canary/research-notes.md. Follow your normal contract: anchor every factual claim to a source, verify each arXiv ID/URL, remove or soften unsupported claims and numbers, and build a Sources section. Do not invent sources. Also write a short verification log to /work/experiments/feynman-verifier-canary/verification-log.md that lists, for each of the six body claims, one of: SUPPORTED, WEAKENED, REMOVED, or UNRESOLVED, wit …[+213 chars]`
35. **bash** `{"command": "cd /work/experiments/feynman-verifier-canary; echo \"=== cited.md ===\"; cat cited.md; echo; echo \"=== verification-log.md ===\"; cat verification-log.md 2>/dev/null || echo \"(missing)\"", "timeout": 60}`
36. **bash** `{"command": "timeout 40 curl -sS \"https://export.arxiv.org/api/query?id_list=2408.03314,2211.17192,1706.03762\" -o /tmp/abs.xml; python3 - <<'PY'\nimport re\nx=open('/tmp/abs.xml').read()\nfor e in x.split('<entry>')[1:]:\n    i=re.search(r'<id>.*?abs/([^<]+)</id>',e)\n    t=re.search(r'<title>([\\s\\S]*?)</title>',e)\n    s=re.search(r'<summary>([\\s\\S]*?)</summary>',e)\n    print(\"ID:\",i.group(1).strip() if i else \"?\")\n    print(\"TITLE:\",re.sub(r'\\s+',' ',t.group(1)).strip() if t else \"?\")\n    print(\"ABS:\",re.sub(r'\\s+',' ',s.group(1)).strip()[:1200] if s else \"?\")\n    pri …[+25 chars]`
37. **bash** `{"command": "python3 - <<'PY'\nimport re\nx=open('/tmp/abs.xml').read()\ne=[e for e in x.split('<entry>')[1:] if '2408.03314' in e][0]\ns=re.search(r'<summary>([\\s\\S]*?)</summary>',e).group(1)\ns=re.sub(r'\\s+',' ',s).strip()\nprint(s)\nprint()\nfor kw in ['4x','4×','14x','14×','FLOP','best-of-N','best of N']:\n    print(kw, '->', kw.lower() in s.lower())\nPY", "timeout": 60}`
38. **bash** `{"command": "ls -lt /state/.feynman/sessions/ 2>/dev/null | head -10; echo; find /state/.feynman -maxdepth 4 -iname '*subagent*' -o -iname '*verifier*' 2>/dev/null | head -20", "timeout": 60}`
39. **bash** `{"command": "cd /work/experiments/feynman-verifier-canary; echo \"word counts:\"; wc -w draft.md cited.md verification-log.md; echo; echo \"differences in claim treatment:\"; diff <(grep -v '^$' draft.md) <(grep -v '^$' cited.md) | head -40", "timeout": 60}`
40. **bash** `{"command": "cd /state/.feynman/sessions/subagent-artifacts; cat ca2880e3-9094-463f-8d95-53d1b626fdb5_verifier_0_meta.json 2>/dev/null | head -80; echo; echo \"=== transcript tail ===\"; tail -2 ca2880e3-9094-463f-8d95-53d1b626fdb5_verifier_0_transcript.jsonl | cut -c1-500", "timeout": 60}`
41. **bash** `{"command": "set -e\ncd /work/experiments/feynman-eval-audit\nmkdir -p work/c12-verifier-output/ws/outputs work/c12-verifier-output/home work/c12-verifier-output/tmp\ncp /work/experiments/feynman-verifier-canary/cited.md work/c12-verifier-output/ws/outputs/test-time-compute-scaling.md\nprintf '# Provenance\\n\\n- Verification: PASS\\n' > work/c12-verifier-output/ws/outputs/test-time-compute-scaling.provenance.md\npython3 - <<'PY'\nimport json\np='/work/experiments/feynman-eval-audit/seed.jsonl'\nrows=[json.loads(l) for l in open(p) if l.strip()]\nrows=[r for r in rows if r['canary']!='c12-veri …[+567 chars]`
   - _said:_ I have enough evidence. Writing the case study and a provenance sidecar in the harness's own convention.
42. **write** `{"path": "/work/outputs/feynman-harness-eval-quality.md", "content": "# Feynman Harness: An AI-Eval-Quality Case Study\n\n**Thesis.** Feynman's product claim is *claim-level* verification: a verifier agent checks that each citation actually supports the sentence attached to it, cross-checks identifiers against two indexes, and removes unsupported material. Its public eval, however, measures *identifier-level attribution*: whether arXiv/DOI IDs resolve and whether the citing line contains enough title tokens. I tested the gap directly. The shipped scorer missed a correct-paper/false-claim docum …[+30446 chars]`
43. **bash** `{"command": "cd /work; python3 - <<'PY'\nimport json, glob, os, re\n# --- 1. result-file facts ---\nrows=[]\nfor f in sorted(glob.glob('notes/feynman-evals/2026-*.jsonl')):\n    for line in open(f):\n        line=line.strip()\n        if line: rows.append((os.path.basename(f),json.loads(line)))\nprint(\"result files:\", len({f for f,_ in rows}))\nprint(\"result rows:\", len(rows))\nprint(\"ids covered:\", sorted({r['id'] for _,r in rows}))\nprint(\"coverage:\", len({r['id'] for _,r in rows}), \"/ 12 =\", round(len({r['id'] for _,r in rows})/12*100,1), \"%\")\nprint(\"dirty rows:\", sum(1 for _ …[+1247 chars]`
44. **write** `{"path": "/work/outputs/feynman-harness-eval-quality.provenance.md", "content": "# Provenance: Feynman harness AI-eval-quality case study\n\n- **Date:** 2026-11-14\n- **Harness:** Feynman 0.5.65 (`/opt/feynman/feynman-0.5.65-linux-arm64/app`), Node v24.21.0\n- **Session model:** `openrouter/deepseek/deepseek-v4.1-flash-1017`\n- **Workflow:** direct investigation with two bounded experiments (no full `/lit` or `/deepresearch` run)\n- **Verification:** PASS WITH NOTES\n\n## Sources consulted\n\n| # | Source | Type | Used for |\n|---|---|---|---|\n| 1 | Installed harness: `.feynman/SYSTEM.md`, `. …[+4781 chars]`
45. **edit** `{"path": "/work/outputs/feynman-harness-eval-quality.md", "edits": [{"oldText": "A single verifier canary, by contrast, caught all five seeded claim-level defects and preserved the control.", "newText": "A single verifier canary, by contrast, caught all five seeded defects and preserved the control."}, {"oldText": "It shows the verifier contract is operational and can catch blatant claim-level errors at low cost.", "newText": "It shows the verifier contract is operational and can catch blatant claim-level and citation-level errors at low cost."}, {"oldText": "- **[S5]** Feynman, result file `2 …[+374 chars]`
46. **read** `{"path": "/work/outputs/feynman-harness-eval-quality.md", "offset": 1, "limit": 140}`
47. **read** `{"path": "/work/outputs/feynman-harness-eval-quality.md", "offset": 141, "limit": 240}`
48. **edit** `{"path": "/work/outputs/feynman-harness-eval-quality.md", "edits": [{"oldText": "- **All 14 rows from the 0.5.2/0.5.3 runs record `git_dirty: true`.** The eight 0.5.0 baseline rows are clean. The headline 0.5.3 result is therefore not tied to a commit.", "newText": "- **All 14 rows from the 0.5.2/0.5.3 runs record `git_dirty: true`.** The eight 0.5.0 baseline rows are clean. The headline 0.5.3 result is therefore not tied to a clean commit."}, {"oldText": "- **The model changes between baseline and treatment.** The first baseline used claude-sonnet-5 because the gateway's GPT quota was exhaust …[+999 chars]`
49. **bash** `{"command": "cd /work; echo \"=== artifacts ===\"; ls -la outputs/; echo; echo \"=== sizes ===\"; wc -l -w outputs/feynman-harness-eval-quality.md outputs/feynman-harness-eval-quality.provenance.md; echo; echo \"=== 'verified/confirmed' occurrences ===\"; grep -n -iE '\\b(verified|confirmed|reproduced)\\b' outputs/feynman-harness-eval-quality.md | head -20; echo; echo \"=== TODO/placeholder in artifact ===\"; grep -n 'TODO' outputs/feynman-harness-eval-quality.md || echo \"none\"; echo; echo \"=== experiment files ===\"; find experiments -maxdepth 2 -type f | sort | head -30; echo; echo \"===  …[+390 chars]`
50. **edit** `{"path": "/work/outputs/feynman-harness-eval-quality.md", "edits": [{"oldText": "- **The `cost` column is `$0` in every row** because the eval `models.json` has no `cost` block. The README says this, but the table still prints `$0.00`.", "newText": "- **The `cost` column is `$0` in every row** because the provider entry used for the run had no `cost` block, which the README names as the condition for `$0`. The table still prints `$0.00`, which reads like a measured cost."}]}`
   - _said:_ Done. The case study is at **`outputs/feynman-harness-eval-quality.md`**, with a provenance sidecar at `outputs/feynman-harness-eval-quality.provenance.md`.

## What I actually did

Three probes, all reproducible on disk:

1. **Static audit** of the installed 0.5.65 harness: `SYSTEM.md`, the four agents, `/deepresearch`, and the public `evals/` directory.
2. **Scorer canary suite**: 13 synthetic f …[+2839 chars]

Last stopReason: `stop` (assistant messages this turn: 35)

## Final reply

Done. The case study is at **`outputs/feynman-harness-eval-quality.md`**, with a provenance sidecar at `outputs/feynman-harness-eval-quality.provenance.md`.

## What I actually did

Three probes, all reproducible on disk:

1. **Static audit** of the installed 0.5.65 harness: `SYSTEM.md`, the four agents, `/deepresearch`, and the public `evals/` directory.
2. **Scorer canary suite**: 13 synthetic final outputs with known defects, run through the unmodified `evals/run.mjs --rescore`.
3. **Verifier canary**: a six-claim draft with five seeded defects, run through the harness's own `verifier` agent.

## The core finding

Feynman's product claim is **claim-level verification**. Its public eval measures **identifier-level attribution**: do arXiv/DOI IDs resolve, and does the citing line contain enough title tokens. Those are different constructs.

The scorer results:

| Seeded defect | Detected? |
|---|---|
| Fabricated arXiv ID | yes (`valid = 0%`) |
| Real ID attached to wrong paper title | yes (`title = 0%`) |
| Correct paper, claim contradicted by paper | **no** (100% across all metrics) |
| Fabricated number, no citation | **no** |
| Reference-section citation, contradictory body | **no** |
| PMID-only citation of the key paper | **no** (`recall = 100%`, `cites = 0`) |
| Terse but correct citation | **false positive** (`title = 0%`) |
| Honest disclosure of a removed fake ID | **penalized** (`valid = 75%`) |

Of the nine defect canaries, three were flagged by the validity/title checks; six were not. All 13 canaries — including the zero-citation and false-claim documents — scored `done = yes`.

The verifier canary, by contrast, addressed all five seeded defects, preserved the control, and replaced the fabricated numbers with figures I checked against the arXiv abstracts.

## Eval-hygiene findings

- **4 of 12 questions** have ever been run (33%); only q01/q04/q07/q10.
- **14/14 rows** from the 0.5.2/0.5.3 runs record `git_dirty: true`; the headline 0.5.3 result is not tied to a clean commit.
- **All cost values are `$0`**, because the provider entry had no cost block — the column reads like a measurement but isn't.
- **The public eval ledger stops at 2026-09-24**; the installed version is 0.5.65 (2026-11-06).
- **Refusals are scored as research failures**: Opus 5.5 refusing CRISPR questions becomes `done: false`, `recall: 0%`.
- The release note's "0.5.2: 43 of 43 citations" actually matches the file recorded as **0.5.0** (`d926547`), not either 0.5.2-labelled file.

## Honest caveats

The canaries are synthetic unit tests of the scorer, not population estimates. The verifier canary is n=1, one model, a 103-word draft with blatant defects, and the research notes pre-flagged two of them. It shows the contract works; it does not estimate a catch rate. I did not run a full `/lit` or `/deepresearch` session.

The constructive version: the harness's verification layer is better than its eval can see. The fix is a claim-level entailment lane plus denominators and separated failure statuses — not a bigger version of the same identifier check.

**Reproduction:** `experiments/feynman-eval-audit/make_canaries.py` and `experiments/feynman-verifier-canary/`; full source list is in the artifact.

## Files created this turn

- state/.feynman/sessions/2026-11-14T08-28-17-029Z_01a1d92b-ed04-76c7-8f4d-7b9e0765be49.jsonl
- state/.feynman/sessions/2026-11-14T08-28-17-029Z_01a1d92b-ed04-76c7-8f4d-7b9e0765be49/ca2880e3-9094-463f-8d95-53d1b626fdb5/run-0/session.jsonl
- state/.feynman/sessions/subagent-artifacts/ca2880e3-9094-463f-8d95-53d1b626fdb5_verifier_0_input.md
- state/.feynman/sessions/subagent-artifacts/ca2880e3-9094-463f-8d95-53d1b626fdb5_verifier_0_meta.json
- state/.feynman/sessions/subagent-artifacts/ca2880e3-9094-463f-8d95-53d1b626fdb5_verifier_0_output.md
- state/.feynman/sessions/subagent-artifacts/ca2880e3-9094-463f-8d95-53d1b626fdb5_verifier_0_transcript.jsonl
- work/experiments/feynman-eval-audit/canary-key.json
- work/experiments/feynman-eval-audit/evals/questions.jsonl
- work/experiments/feynman-eval-audit/evals/run.mjs
- work/experiments/feynman-eval-audit/make_canaries.py
- work/experiments/feynman-eval-audit/rescore-stderr.txt
- work/experiments/feynman-eval-audit/rescore-stdout.txt
- work/experiments/feynman-eval-audit/rescore-stdout2.txt
- work/experiments/feynman-eval-audit/seed-input.jsonl
- work/experiments/feynman-eval-audit/seed.jsonl
- work/experiments/feynman-eval-audit/seed.md
- work/experiments/feynman-eval-audit/work/c0-correct/ws/outputs/test-time-compute-scaling.md
- work/experiments/feynman-eval-audit/work/c0-correct/ws/outputs/test-time-compute-scaling.provenance.md
- work/experiments/feynman-eval-audit/work/c1-wrong-title-real-id/ws/outputs/test-time-compute-scaling.md
- work/experiments/feynman-eval-audit/work/c1-wrong-title-real-id/ws/outputs/test-time-compute-scaling.provenance.md
- work/experiments/feynman-eval-audit/work/c10-doi-wrong-title/ws/outputs/crispr-base-editing.md
- work/experiments/feynman-eval-audit/work/c10-doi-wrong-title/ws/outputs/crispr-base-editing.provenance.md
- work/experiments/feynman-eval-audit/work/c11-datacite-doi/ws/outputs/crispr-base-editing.md
- work/experiments/feynman-eval-audit/work/c11-datacite-doi/ws/outputs/crispr-base-editing.provenance.md
- work/experiments/feynman-eval-audit/work/c12-verifier-output/ws/outputs/test-time-compute-scaling.md
- work/experiments/feynman-eval-audit/work/c12-verifier-output/ws/outputs/test-time-compute-scaling.provenance.md
- work/experiments/feynman-eval-audit/work/c2-fabricated-id/ws/outputs/test-time-compute-scaling.md
- work/experiments/feynman-eval-audit/work/c2-fabricated-id/ws/outputs/test-time-compute-scaling.provenance.md
- work/experiments/feynman-eval-audit/work/c3-right-paper-false-claim/ws/outputs/test-time-compute-scaling.md
- work/experiments/feynman-eval-audit/work/c3-right-paper-false-claim/ws/outputs/test-time-compute-scaling.provenance.md
- work/experiments/feynman-eval-audit/work/c4-uncited-number/ws/outputs/test-time-compute-scaling.md
- work/experiments/feynman-eval-audit/work/c4-uncited-number/ws/outputs/test-time-compute-scaling.provenance.md
- work/experiments/feynman-eval-audit/work/c5-web-only/ws/outputs/test-time-compute-scaling.md
- work/experiments/feynman-eval-audit/work/c5-web-only/ws/outputs/test-time-compute-scaling.provenance.md
- work/experiments/feynman-eval-audit/work/c6-pmid-only/ws/outputs/crispr-base-editing.md
- work/experiments/feynman-eval-audit/work/c6-pmid-only/ws/outputs/crispr-base-editing.provenance.md
- work/experiments/feynman-eval-audit/work/c6-pmid-only/ws/outputs/test-time-compute-scaling.md
- work/experiments/feynman-eval-audit/work/c6-pmid-only/ws/outputs/test-time-compute-scaling.provenance.md
- work/experiments/feynman-eval-audit/work/c7-generic-citation-line/ws/outputs/test-time-compute-scaling.md
- work/experiments/feynman-eval-audit/work/c7-generic-citation-line/ws/outputs/test-time-compute-scaling.provenance.md
- work/experiments/feynman-eval-audit/work/c8-reference-only-contradiction/ws/outputs/test-time-compute-scaling.md
- work/experiments/feynman-eval-audit/work/c8-reference-only-contradiction/ws/outputs/test-time-compute-scaling.provenance.md
- work/experiments/feynman-eval-audit/work/c9-doi-correct/ws/outputs/crispr-base-editing.md
- work/experiments/feynman-eval-audit/work/c9-doi-correct/ws/outputs/crispr-base-editing.provenance.md
- work/experiments/feynman-verifier-canary/cited.md
- work/experiments/feynman-verifier-canary/draft.md
- work/experiments/feynman-verifier-canary/research-notes.md
- work/experiments/feynman-verifier-canary/verification-log.md
- work/notes/feynman-evals/2026-09-23-lit-ferrylane-openai_claude-sonnet-5.jsonl
- work/notes/feynman-evals/2026-09-23-lit-ferrylane-openai_claude-sonnet-5.md
- work/notes/feynman-evals/2026-09-24-lit-0.5.3-ferrylane-openai_gpt-5.6-terra.jsonl
- work/notes/feynman-evals/2026-09-24-lit-0.5.3-ferrylane-openai_gpt-5.6-terra.md
- work/notes/feynman-evals/2026-09-24-lit-0.5.3-ferrylane_claude-opus-5-5.jsonl
- work/notes/feynman-evals/2026-09-24-lit-0.5.3-ferrylane_claude-opus-5-5.md
- work/notes/feynman-evals/2026-09-24-lit-0.5.3-pre-wait-ferrylane-openai_gpt-5.6-terra.jsonl
- work/notes/feynman-evals/2026-09-24-lit-0.5.3-pre-wait-ferrylane-openai_gpt-5.6-terra.md
- work/notes/feynman-evals/2026-09-24-lit-0.5.3-pre-wait-ferrylane_claude-opus-5-5.jsonl
- work/notes/feynman-evals/2026-09-24-lit-0.5.3-pre-wait-ferrylane_claude-opus-5-5.md
- work/notes/feynman-evals/2026-09-24-lit-ferrylane-openai_gpt-5.6-terra.jsonl
- work/notes/feynman-evals/2026-09-24-lit-ferrylane-openai_gpt-5.6-terra.md
- work/notes/feynman-evals/README.md
- work/notes/feynman-evals/questions.jsonl
- work/notes/feynman-evals/run.mjs
- work/outputs/feynman-harness-eval-quality.md
- work/outputs/feynman-harness-eval-quality.provenance.md

## Files modified this turn

(none)
