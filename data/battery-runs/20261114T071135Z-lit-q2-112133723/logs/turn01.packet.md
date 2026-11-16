# Evidence packet: 20261114T071135Z-lit-q2-112133723 / turn01

Mechanically extracted from the Feynman session log and filesystem. No interpretation applied.

## Prompt

```
I'm interested in a case study of the Feynman harness from an AI-eval-quality perspective, so dogfooding it a bit.
```

## Run metadata

`{"turn":1,"exa":true,"mode":"new","exit_code":0,"seconds":342,"model":"openrouter/deepseek/deepseek-v4.1-flash-1017","prompt":"p1.md","prompt_sha256":"f3b1050bf027"}`

## Agent actions (in order)

1. **bash** `{"command": "cd /work && ls -la && echo \"---\" && ls -la /opt/feynman/feynman-0.5.65-linux-arm64/app | head -50", "timeout": 30}`
2. **bash** `{"command": "cd /opt/feynman/feynman-0.5.65-linux-arm64/app && cat package.json 2>/dev/null | head -80; echo \"---GIT---\"; git log --oneline -5 2>/dev/null; echo \"---TREE---\"; ls -R . 2>/dev/null | head -100", "timeout": 30}`
3. **bash** `{"command": "cd /opt/feynman/feynman-0.5.65-linux-arm64/app && echo \"=== .feynman ===\"; find .feynman -maxdepth 3 -type f | sort; echo; echo \"=== prompts ===\"; ls -la prompts; echo; echo \"=== skills ===\"; ls skills; echo; echo \"=== metadata ===\"; ls -la metadata; echo; echo \"=== agents ===\"; for f in .feynman/agents/*; do echo \"--- $f ---\"; head -60 \"$f\"; done", "timeout": 30}`
4. **bash** `{"command": "cd /opt/feynman/feynman-0.5.65-linux-arm64/app && wc -l .feynman/SYSTEM.md AGENTS.md README.md RELEASES.md skills/*/SKILL.md prompts/* 2>/dev/null | sort -n | tail -40", "timeout": 30}`
5. **bash** `{"command": "cd /opt/feynman/feynman-0.5.65-linux-arm64/app && echo \"=== SYSTEM.md ===\"; cat .feynman/SYSTEM.md; echo; echo \"=== settings.json ===\"; cat .feynman/settings.json; echo; echo \"=== README ===\"; cat README.md", "timeout": 30}`
6. **bash** `{"command": "cd /opt/feynman/feynman-0.5.65-linux-arm64/app && echo \"=== AGENTS.md ===\"; cat AGENTS.md; echo; echo \"=== RELEASES head ===\"; head -120 RELEASES.md", "timeout": 30}`
7. **bash** `{"command": "cd /opt/feynman/feynman-0.5.65-linux-arm64/app && sed -n '1,90p' prompts/deepresearch.md; echo \"=== SCAFFOLD ===\"; sed -n '1,80p' extensions/research-tools/project-scaffold.ts", "timeout": 30}`
8. **bash** `{"command": "ls -la ~/.feynman 2>/dev/null; echo \"---\"; cat ~/.feynman/agent/settings.json 2>/dev/null | head -40; echo \"--- models ---\"; cat ~/.feynman/agent/models.json 2>/dev/null | head -40; echo \"--- env hints ---\"; env | grep -iE 'FEYNMAN|PI_|MODEL|OPENAI|ANTHROP\\w*_BASE' | sed 's/=.*/=<set>/'", "timeout": 30}`
9. **bash** `{"command": "echo \"PI_MODEL=$PI_MODEL\"; echo \"FEYNMAN_MODEL=$FEYNMAN_MODEL\"; echo \"PI_PROVIDER=$PI_PROVIDER\"; echo \"PI_REASONING_LEVEL=$PI_REASONING_LEVEL\"; echo \"FEYNMAN_VERSION=$FEYNMAN_VERSION\"; echo \"SESSION=$PI_SESSION_FILE\"; ls -la \"$PI_SESSION_FILE\" 2>/dev/null; echo \"--- session head ---\"; head -c 2000 \"$PI_SESSION_FILE\" 2>/dev/null", "timeout": 30}`
10. **bash** `{"command": "cd /work && find outputs notes papers .sandbox -type f | head -50; echo \"--- disk ---\"; df -h /work | tail -1; echo \"--- tools ---\"; which python3 curl jq git node; python3 -V", "timeout": 30}`
11. **bash** `{"command": "cd /work && mkdir -p experiments/harness-verifier-eval/{inputs,outputs,logs} notes outputs/.plans && curl -sL --max-time 45 \"https://arxiv.org/abs/1706.03762\" -o experiments/harness-verifier-eval/logs/arxiv-abs.html; echo \"exit=$?\"; wc -c experiments/harness-verifier-eval/logs/arxiv-abs.html; grep -oE '<title>[^<]*' experiments/harness-verifier-eval/logs/arxiv-abs.html | head -2", "timeout": 60}`
12. **bash** `{"command": "cd /work && curl -sL --max-time 60 \"https://arxiv.org/html/1706.03762v7\" -o experiments/harness-verifier-eval/logs/arxiv-html.html; echo \"exit=$?\"; wc -c experiments/harness-verifier-eval/logs/arxiv-html.html; grep -oiE '28\\.4|41\\.8|27\\.3|65M|213M|3\\.5 days|12 hours' experiments/harness-verifier-eval/logs/arxiv-html.html | sort | uniq -c | head", "timeout": 80}`
13. **bash** `{"command": "cd /work/experiments/harness-verifier-eval/logs && python3 - <<'PY'\nimport re,html\ns=open('arxiv-html.html',encoding='utf-8',errors='replace').read()\ns=re.sub(r'<script.*?</script>','',s,flags=re.S)\ns=re.sub(r'<style.*?</style>','',s,flags=re.S)\nt=re.sub(r'<[^>]+>',' ',s)\nt=html.unescape(t)\nt=re.sub(r'\\s+',' ',t)\nfor kw in ['28.4','41.8','27.3','65M','213M','8 NVIDIA P100','3.5 days','12 hours','4.5 million','36M','label smoothing','h = 8','d_{model} = 512','dmodel = 512','dropout']:\n    i=t.find(kw)\n    print(f'--- {kw} @ {i} ---')\n    if i>=0: print(t[max(0,i-320):i+ …[+26 chars]`
14. **bash** `{"command": "cd /work/experiments/harness-verifier-eval/logs && python3 - <<'PY'\nimport re,html\ns=open('arxiv-html.html',encoding='utf-8',errors='replace').read()\ns=re.sub(r'<script.*?</script>','',s,flags=re.S); s=re.sub(r'<style.*?</style>','',s,flags=re.S)\nt=html.unescape(re.sub(r'<[^>]+>',' ',s)); t=re.sub(r'\\s+',' ',t)\nfor kw in ['512','parameters','Table 3','Table 1','maximum path length','self-attention layer connects']:\n    for m in list(re.finditer(re.escape(kw),t))[:3]:\n        i=m.start(); print(f'--- {kw} ---'); print(t[max(0,i-260):i+300]); print()\nPY", "timeout": 30}`
15. **bash** `{"command": "cd /work/experiments/harness-verifier-eval/logs && python3 - <<'PY'\nimport re,html\ns=open('arxiv-html.html',encoding='utf-8',errors='replace').read()\ns=re.sub(r'<script.*?</script>','',s,flags=re.S); s=re.sub(r'<style.*?</style>','',s,flags=re.S)\nt=html.unescape(re.sub(r'<[^>]+>',' ',s)); t=re.sub(r'\\s+',' ',t)\nfor kw in ['65','213','base model','Table 4','English constituency']:\n    ms=list(re.finditer(re.escape(kw),t))[:4]\n    print(f'===== {kw} ({len(list(re.finditer(re.escape(kw),t)))} hits) =====')\n    for m in ms:\n        i=m.start(); print(t[max(0,i-200):i+240]);  …[+33 chars]`
16. **bash** `{"command": "mkdir -p /work/experiments/harness-verifier-eval/{inputs,outputs,logs} && cd /work/experiments/harness-verifier-eval && cat > inputs/research-notes.md <<'EOF'\n# Research notes — Transformer (source excerpts)\n\nPrimary source: Vaswani et al., \"Attention Is All You Need\", 2017.\n- Abstract/landing page: https://arxiv.org/abs/1706.03762\n- Full text used for excerpts: https://arxiv.org/html/1706.03762v7\n\n## Abstract (verbatim)\n\"We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entir …[+4292 chars]`
17. **bash** `{"command": "curl -sIL --max-time 30 \"https://arxiv.org/abs/1706.03799\" | head -5; echo \"---\"; curl -sL --max-time 30 \"https://arxiv.org/abs/1706.03799\" | grep -oE '<title>[^<]*' | head -1; echo \"--- example.com ---\"; curl -sIL --max-time 20 \"https://example.com/transformer-bleu\" | head -5", "timeout": 60}`
18. **bash** `{"command": "cd /work && cat > experiments/harness-verifier-eval/GROUND-TRUTH.md <<'EOF'\n# Ground truth key (scoring only; not shown to agents)\n\nSource of truth: Vaswani et al. 2017, arXiv:1706.03762 (abstract, §3.1, §3.2.2, §5.1, §5.2, §5.4, Tables 2–3, §6.3).\nLocal copies: `logs/arxiv-abs.html`, `logs/arxiv-html.html`.\n\n## Treatment draft: planted items\n\n| ID | Item in draft | Status | Correct value / reason |\n|---|---|---|---|\n| C1 | Transformer based solely on attention; no recurrence/convolution | TRUE | Abstract |\n| C2 | 8 NVIDIA P100 GPUs | TRUE | §5.2 |\n| C3 | big model 300 …[+6108 chars]`
19. **subagent** `{"workflow": ">/work/outputs/.plans/harness-verifier-eval-workflow.js</white>", "async": true, "options": {"globalConcurrencyLimit": 3}}`
   - _tool error:_ Failed to read workflow script '/work/>/work/outputs/.plans/harness-verifier-eval-workflow.js</white>': ENOENT: no such file or directory, open '/work/>/work/outputs/.plans/harness-verifier-eval-workflow.js</white>' A workflow string is a named workflow resource or a script file path. To run script  …[+99 chars]
20. **subagent** `{"workflow": "outputs/.plans/harness-verifier-eval-workflow.js", "async": true, "options": {"globalConcurrencyLimit": 3}}`
21. **bash** `{"command": "cd /opt/feynman/feynman-0.5.65-linux-arm64/app && echo \"=== scripts ===\"; find scripts -type f | sort; echo; echo \"=== any tests/eval dirs shipped? ===\"; find . -maxdepth 2 -type d \\( -name tests -o -name test -o -name evals -o -name eval \\) -not -path './node_modules/*'; echo; echo \"=== dist grep for enforcement terms ===\"; for t in provenance verifier \"risk\" \"verification\" \"unsupported\" \"TODO\"; do printf '%-14s %s\\n' \"$t\" \"$(grep -rIl --exclude-dir=node_modules -i \"$t\" dist extensions bin 2>/dev/null | wc -l)\"; done; echo; echo \"=== scripts/check-architec …[+89 chars]`
22. **bash** `{"command": "cd /opt/feynman/feynman-0.5.65-linux-arm64/app && python3 - <<'PY'\nimport re,glob\nfiles=['.feynman/SYSTEM.md','.feynman/agents/researcher.md','.feynman/agents/verifier.md','.feynman/agents/writer.md','.feynman/agents/reviewer.md']\npat=re.compile(r'\\b(must|never|do not|don\\'t|only|required|shall|always)\\b',re.I)\nfor f in files:\n    t=open(f).read()\n    print(f\"{f:40s} words={len(t.split()):5d} rules={len(pat.findall(t)):3d}\")\nt=''.join(open(f).read() for f in files)\nfor term in ['verified','confirmed','reproduced','blocked','unverified','inferred','URL','citation','fab …[+88 chars]`
   - _tool error:_ === scripts ===
scripts/check-node-version.mjs
scripts/check-pi-rpc.mjs
scripts/install/install-skills.ps1
scripts/install/install-skills.sh
scripts/install/install.ps1
scripts/install/install.sh

=== any tests/eval dirs shipped? ===

=== dist grep for enforcement terms ===
provenance     7
verifier …[+150 chars]
23. **bash** `{"command": "cd /opt/feynman/feynman-0.5.65-linux-arm64/app && grep -rIn --exclude-dir=node_modules -iE 'provenance|verification|unsupported' dist extensions bin | head -30; echo \"=== check-pi-rpc ===\"; head -60 scripts/check-pi-rpc.mjs", "timeout": 30}`
24. **bash** `{"command": "cd /work && cat > experiments/harness-session-audit/audit.py <<'PY'\n#!/usr/bin/env python3\n\"\"\"Audit a Pi/Feynman JSONL session for observability + artifact evidence.\n\nUsage: python3 audit.py <session.jsonl> [--json out.json]\nPrints tool-call counts, message roles, token usage, artifact paths mentioned,\nand integrity vocabulary counts. Read-only.\n\"\"\"\nimport json, sys, re, collections, os\n\ndef walk(obj, acc):\n    if isinstance(obj, dict):\n        for k, v in obj.items():\n            if k in (\"content\", \"text\", \"message\", \"summary\", \"output\") and isinstan …[+3952 chars]`
25. **bash** `{"command": "cd /work && mkdir -p experiments/harness-session-audit && cat > experiments/harness-session-audit/audit.py <<'PY'\n#!/usr/bin/env python3\n\"\"\"Audit a Pi/Feynman JSONL session for observability + artifact evidence.\n\nUsage: python3 audit.py <session.jsonl> [--json out.json]\nPrints tool-call counts, message roles, token usage, artifact paths mentioned,\nand integrity vocabulary counts. Read-only.\n\"\"\"\nimport json, sys, re, collections, os\n\ndef texts(v):\n    if isinstance(v, str):\n        return [v]\n    if isinstance(v, list):\n        out = []\n        for x in v:\n    …[+3802 chars]`
26. **subagent** `{"action": "status", "id": "ddeb55c9"}`
27. **feynman_science_database_search** `{"source": "arxiv", "query": "BetterBench validating LLM benchmark quality", "limit": 3}`
28. **feynman_science_database_search** `{"source": "arxiv", "query": "Adding Error Bars to Evals statistical approach language model evaluation", "limit": 3}`
29. **web_search** `{"queries": ["Inspect AI evaluation framework documentation UK AI Safety Institute", "AI agent evaluation reproducibility provenance framework"], "numResults": 5}`
30. **feynman_science_database_search** `{"source": "semanticscholar", "query": "BetterBench How to Validate LLM Benchmark Quality", "limit": 3}`
31. **subagent** `{"action": "status", "id": "ddeb55c9"}`
32. **bash** `{"command": "cd /tmp/pi-subagents-uid-1000/async-subagent-runs/ddeb55c9-744e-43d9-8f08-de9772dc6070 && ls -la && echo \"--- tail events ---\" && tail -c 3000 events.jsonl 2>/dev/null", "timeout": 30}`
33. **bash** `{"command": "cd /work/experiments/harness-verifier-eval/outputs && ls -la; for f in *; do echo \"=== $f ===\"; wc -l \"$f\"; done 2>/dev/null", "timeout": 30}`
   - _tool error:_ total 0
drwxr-xr-x 2 researcher researcher  64 Nov 14 08:06 .
drwxr-xr-x 6 researcher researcher 192 Nov 14 08:06 ..
=== * ===


Command exited with code 1
34. **bash** `{"command": "cd /tmp/pi-subagents-uid-1000/async-subagent-runs/ddeb55c9-744e-43d9-8f08-de9772dc6070 && find . -maxdepth 3 -type f | head -40; echo \"--- control ---\"; ls -la control 2>/dev/null; find control -type f -maxdepth 2 -exec sh -c 'echo \"## $1\"; tail -c 800 \"$1\"' _ {} \\; 2>/dev/null | head -60", "timeout": 30}`
35. **bash** `{"command": "ls -la /tmp/pi-subagents-uid-1000/async-subagent-runs/ | tail -10; echo \"---\"; for d in d73697d4-e891-457a-b8e0-614acf937de7 65bc97c1-3dde-4f28-846d-262138c622bd 62a40724-7cba-4f88-9ee2-5d422a34913b; do echo \"== $d ==\"; ls -la /tmp/pi-subagents-uid-1000/async-subagent-runs/$d 2>/dev/null | head; done; echo \"--- ps ---\"; ps aux | grep -iE 'pi|node' | grep -v grep | head -10", "timeout": 30}`
36. **bash** `{"command": "for d in d73697d4-e891-457a-b8e0-614acf937de7 65bc97c1-3dde-4f28-846d-262138c622bd 62a40724-7cba-4f88-9ee2-5d422a34913b; do echo \"===== $d =====\"; tail -c 1500 /tmp/pi-subagents-uid-1000/async-subagent-runs/$d/output-0.log | tr -d '\\000'; echo; done", "timeout": 30}`
37. **bash** `{"command": "cd /work/experiments/harness-verifier-eval/logs && curl -s --max-time 30 \"https://api.crossref.org/works?query=Attention+Is+All+You+Need+Vaswani+2017&rows=3&select=DOI,title,published-print,published-online,issued,container-title,author,is-referenced-by-count,URL,type\" -o crossref-query.json; jq -r '.message.items[] | [.DOI, (.title[0] // \"\"), (.type // \"\"), ((.issued[\"date-parts\"][0][0])|tostring), ((.[\"is-referenced-by-count\"])|tostring)] | @tsv' crossref-query.json", "timeout": 45}`
38. **bash** `{"command": "cd /work && python3 - <<'PY'\nimport json,re\n# extract the tool-call sequence from one child's events to see observability granularity\np='/tmp/pi-subagents-uid-1000/async-subagent-runs/d73697d4-e891-457a-b8e0-614acf937de7/events.jsonl'\nnames={}\ntypes={}\nn=0\nfor line in open(p,encoding='utf-8',errors='replace'):\n    n+=1\n    try: e=json.loads(line)\n    except: continue\n    types[e.get('type')]=types.get(e.get('type'),0)+1\n    s=json.dumps(e)\n    for m in re.finditer(r'\"name\":\"(bash|read|write|web_search|fetch_content|feynman_science_database_search|subagent)\"',s):\n …[+137 chars]`
39. **bash** `{"command": "cd /work/experiments/harness-verifier-eval/logs && for id in 2411.00640 2405.14782; do curl -sL --max-time 40 \"https://arxiv.org/abs/$id\" -o \"abs-$id.html\"; echo \"=== $id ===\"; python3 - \"$id\" <<'PY'\nimport re,sys,html\nid=sys.argv[1]\ns=open(f'abs-{id}.html',encoding='utf-8',errors='replace').read()\nm=re.search(r'<blockquote class=\"abstract[^>]*>(.*?)</blockquote>',s,re.S)\nt=html.unescape(re.sub(r'<[^>]+>',' ',m.group(1))) if m else 'NO ABSTRACT'\nprint(re.sub(r'\\s+',' ',t).strip()[:1200])\nprint('TITLE:', html.unescape(re.search(r'<title>([^<]*)',s).group(1)))\nPY\n …[+21 chars]`
40. **web_search** `{"queries": ["BetterBench \"How to Validate LLM Benchmark Quality\" arxiv"], "numResults": 4}`
41. **bash** `{"command": "cd /work/experiments/harness-verifier-eval/outputs && ls -la; echo \"--- status ---\"; python3 -c \"\nimport json\np='/tmp/pi-subagents-uid-1000/async-subagent-runs/ddeb55c9-744e-43d9-8f08-de9772dc6070/status.json'\nd=json.load(open(p))\nprint(json.dumps(d,indent=1)[:1200])\" 2>/dev/null; echo \"--- ps count ---\"; ps aux | grep -c 'subagent-runner-bootstrap'", "timeout": 30}`
42. **bash** `{"command": "cd /work/experiments/harness-verifier-eval/outputs && echo \"=== TREATMENT CITED ===\"; cat treatment-cited.md; echo; echo \"=== CONTROL CITED ===\"; cat control-cited.md", "timeout": 30}`
43. **bash** `{"command": "cd /work/experiments/harness-verifier-eval/logs && python3 - <<'PY'\nimport re,html\ns=open('arxiv-html.html',encoding='utf-8',errors='replace').read()\ns=re.sub(r'<script.*?</script>','',s,flags=re.S); s=re.sub(r'<style.*?</style>','',s,flags=re.S)\nt=html.unescape(re.sub(r'<[^>]+>',' ',s)); t=re.sub(r'\\s+',' ',t)\nfor m in re.finditer(r'dropout rate of 0\\.1|dropout.{0,80}0\\.3|0\\.3.{0,80}dropout',t):\n    i=m.start(); print('...',t[max(0,i-300):i+200],'\\n')\nPY", "timeout": 30}`
44. **bash** `{"command": "cd /work/experiments/harness-verifier-eval/outputs && ls -la; echo; for f in *audit*; do echo \"=== $f ===\"; head -40 \"$f\"; done 2>/dev/null", "timeout": 30}`
45. **bash** `{"command": "cd /work/experiments/harness-verifier-eval/outputs && ls -la; echo \"=== notesfree-cited (if any) ===\"; cat notesfree-cited.md 2>/dev/null | head -60; echo \"=== notesfree-audit head ===\"; head -30 notesfree-audit.md 2>/dev/null", "timeout": 30}`
46. **bash** `{"command": "d=/tmp/pi-subagents-uid-1000/async-subagent-runs/62a40724-7cba-4f88-9ee2-5d422a34913b; tail -c 600 $d/output-0.log | tr -d '\\000'; echo; echo \"--- terminal? ---\"; cat $d/process-terminal.json 2>/dev/null; cat $d/process-terminal-candidate.json 2>/dev/null", "timeout": 30}`
   - _tool error:_ total 36
drwxr-xr-x 7 researcher researcher  224 Nov 14 08:07 .
drwxr-xr-x 6 researcher researcher  192 Nov 14 08:06 ..
-rw-r--r-- 1 researcher researcher 8272 Nov 14 08:07 control-audit.md
-rw-r--r-- 1 researcher researcher 2036 Nov 14 08:07 control-cited.md
-rw-r--r-- 1 researcher researcher 2570  …[+2826 chars]
47. **bash** `{"command": "cd /work/experiments/harness-verifier-eval && cat > inputs/draft-unsupported.md <<'EOF'\n# The Transformer, in brief\n\nAttention Is All You Need (Vaswani et al., 2017) introduced the Transformer, an architecture based solely on attention mechanisms that dispenses with recurrence and convolutions entirely. The big model reached 41.8 BLEU on the WMT 2014 English-to-German translation task, improving over the previous best results, including ensembles, by 5.1 BLEU. On English-to-French it established a new single-model state of the art. Training used 8 NVIDIA P100 GPUs in mixed-prec …[+1991 chars]`
48. **bash** `{"command": "cd /work && sleep 5; ls -la experiments/harness-verifier-eval/outputs/; echo \"--- workflow state ---\"; python3 -c \"\nimport json; d=json.load(open('/tmp/pi-subagents-uid-1000/async-subagent-runs/ddeb55c9-744e-43d9-8f08-de9772dc6070/status.json')); print(d['state']); print([(s['label'],s['status']) for s in d.get('steps',[])])\"", "timeout": 30}`
49. **bash** `{"command": "cd /work/experiments/harness-verifier-eval && cat >> GROUND-TRUTH.md <<'EOF'\n\n## Unsupported-claims arm (draft-unsupported.md)\n\nContradicted by the source (same as treatment): E1 (41.8 EN-DE), E2 (5.1 BLEU), E3 (16 heads), E4 (GLUE/SQuAD), E5 (fabricated quote), E6 (36M EN-DE), U2 (wrong arXiv ID). U1 is omitted from this draft.\n\nPlausible but **unsupported** (not contradicted by any supplied source):\n| ID | Claim | Status | Reason |\n|---|---|---|---|\n| X1 | \"mixed-precision arithmetic\" | UNSUPPORTED | No mention of mixed precision / fp16 anywhere in the paper |\n| X2 | …[+655 chars]`
50. **bash** `{"command": "cd /work/experiments/harness-verifier-eval/outputs && sed -n '1,80p' notesfree-audit.md", "timeout": 30}`
51. **subagent** `{"agent": "verifier", "task": "Read experiments/harness-verifier-eval/inputs/draft-unsupported.md and experiments/harness-verifier-eval/inputs/research-notes.md. Verify the draft per your agent instructions. Write the verified document to experiments/harness-verifier-eval/outputs/unsupported-cited.md and a claim-level audit to experiments/harness-verifier-eval/outputs/unsupported-audit.md. The audit must list every factual claim in the draft with verdict (kept, corrected, flagged, removed), the supporting evidence, and every source URL with live/dead/wrong-content status. For any claim that th …[+176 chars]`
52. **bash** `{"command": "for f in /state/.feynman/sessions/2026-11-14T08-05-41-567Z_01a1d917-3e3f-7157-8f13-31ea82eed8fd/*/run-0/session.jsonl; do echo \"== $f\"; grep -m1 'model_change' \"$f\" 2>/dev/null | python3 -c \"import sys,json; d=json.loads(sys.stdin.read()); print(d.get('provider'), d.get('modelId'))\" 2>/dev/null; done", "timeout": 30}`
53. **bash** `{"command": "cd /work && cat > notes/feynman-harness-static-analysis.md <<'EOF'\n# Static analysis — Feynman 0.5.65 harness (eval-quality lens)\n\nInstall root: `/opt/feynman/feynman-0.5.65-linux-arm64/app`\nPerformed 2026-11-14. All counts from the shipped package only (source repo `src/` and `tests/` are not shipped).\n\n## Surface inventory\n\n| Surface | Count | Evidence |\n|---|---|---|\n| Bundled subagents | 4 (`researcher`, `verifier`, `writer`, `reviewer`) | `.feynman/agents/*.md`; `AGENTS.md` |\n| Skills | 16 directories | `skills/` |\n| Slash-command prompts | 11 | `prompts/` |\n| Sy …[+3654 chars]`
54. **subagent** `{"agent": "verifier", "task": "Read experiments/harness-verifier-eval/inputs/draft-treatment.md and experiments/harness-verifier-eval/inputs/research-notes.md. Verify the draft per your agent instructions. Write the verified document to experiments/harness-verifier-eval/outputs/noaudit-cited.md. Do not create any other output file. Do not edit the input files.", "async": true, "output": false}`
55. **bash** `{"command": "cd /work && cat > experiments/harness-verifier-eval/scorecard.md <<'EOF'\n# Scorecard — verifier arms vs planted ground truth\n\nScored manually by the lead agent on 2026-11-14 against `GROUND-TRUTH.md`, reading the cited document and the audit table for each arm. N = 1 run per arm; counts are descriptive, not estimates of reliability.\n\n## Arm 1 — treatment (6 contradicted claims + fabricated quote + 2 bad URLs, notes supplied)\n\n| Item | Expected | Observed | Score |\n|---|---|---|---|\n| E1 41.8 EN-DE | correct to 28.4 | corrected, disclosed | caught |\n| E2 5.1 BLEU | correc …[+1886 chars]`
56. **bash** `{"command": "cd /work/experiments/harness-verifier-eval/outputs && ls -la; echo; for f in unsupported-cited.md noaudit-cited.md; do [ -f \"$f\" ] && { echo \"=== $f ===\"; head -30 \"$f\"; }; done", "timeout": 30}`
   - _tool error:_ total 44
drwxr-xr-x 8 researcher researcher  256 Nov 14 08:07 .
drwxr-xr-x 7 researcher researcher  224 Nov 14 08:08 ..
-rw-r--r-- 1 researcher researcher 8272 Nov 14 08:07 control-audit.md
-rw-r--r-- 1 researcher researcher 2036 Nov 14 08:07 control-cited.md
-rw-r--r-- 1 researcher researcher 7892  …[+277 chars]
57. **bash** `{"command": "cd /work && python3 - <<'PY'\nimport json,glob,collections\nbase='/state/.feynman/sessions/2026-11-14T08-05-41-567Z_01a1d917-3e3f-7157-8f13-31ea82eed8fd'\nfor d in sorted(glob.glob(base+'/*/run-0/session.jsonl')):\n    u=collections.Counter(); tools=collections.Counter(); n=0\n    for line in open(d,encoding='utf-8',errors='replace'):\n        try: e=json.loads(line)\n        except: continue\n        if e.get('type')=='message':\n            m=e.get('message',{}); n+=1\n            for k,v in (m.get('usage') or {}).items():\n                if isinstance(v,(int,float)): u[k]+=v\n …[+298 chars]`
58. **bash** `{"command": "cd /work/experiments/harness-verifier-eval/outputs && ls -la *.md; echo \"--- noaudit ---\"; cat noaudit-cited.md 2>/dev/null | head -40", "timeout": 30}`
59. **bash** `{"command": "cd /opt/feynman/feynman-0.5.65-linux-arm64/app && echo \"--- .provenance refs outside prompts/skills/docs ---\"; grep -rIn --exclude-dir=node_modules --exclude-dir=prompts --exclude-dir=skills --exclude-dir=.feynman --exclude=RELEASES.md --exclude=AGENTS.md -E 'provenance\\.md|\\.provenance' . | head -20; echo \"--- count of prompt files ---\"; ls prompts/*.md | wc -l; echo \"--- skill dirs ---\"; ls -d skills/*/ | wc -l; echo \"--- agents ---\"; ls .feynman/agents/*.md | wc -l; echo \"--- md lines/words in policy ---\"; cat .feynman/SYSTEM.md .feynman/agents/*.md | wc -w", "timeo …[+8 chars]`
60. **bash** `{"command": "cd /work && python3 - <<'PY'\nimport re,glob\nfiles=['.feynman/SYSTEM.md']+glob.glob('.feynman/agents/*.md')\nimport os\nos.chdir('/opt/feynman/feynman-0.5.65-linux-arm64/app')\nfiles=['.feynman/SYSTEM.md']+glob.glob('.feynman/agents/*.md')\npat=re.compile(r'\\b(must|never|do not|don\\'t|only|required|shall|always)\\b',re.I)\ntot_words=0; tot_rules=0\nfor f in files:\n    t=open(f).read(); w=len(t.split()); r=len(pat.findall(t))\n    tot_words+=w; tot_rules+=r\n    print(f,w,r)\nprint('TOTAL',tot_words,tot_rules)\nPY", "timeout": 30}`
61. **bash** `{"command": "for d in 52ff045b-a8f1-4f11-a850-de2cd5362c53 f63e0c1e-0d54-484c-9a69-98c214609cec; do echo \"== $d ==\"; tail -c 400 /tmp/pi-subagents-uid-1000/async-subagent-runs/$d/output-0.log 2>/dev/null | tr -d '\\000'; echo; cat /tmp/pi-subagents-uid-1000/async-subagent-runs/$d/process-terminal.json 2>/dev/null; done; echo; ls -la /work/experiments/harness-verifier-eval/outputs/*.md", "timeout": 30}`
62. **bash** `{"command": "cd /work/experiments/harness-verifier-eval/outputs && cat unsupported-cited.md", "timeout": 30}`
63. **subagent** `{"agent": "verifier", "task": "Read experiments/harness-verifier-eval/inputs/draft-unsupported.md and experiments/harness-verifier-eval/inputs/research-notes.md. Verify the draft per your agent instructions. Write the verified document to experiments/harness-verifier-eval/outputs/unsupported-default-cited.md. Do not create any other output file. Do not edit the input files.", "async": true, "output": false}`
64. **bash** `{"command": "cd /work/experiments/harness-verifier-eval/outputs && ls -la *.md; echo \"=== unsupported-audit ===\"; cat unsupported-audit.md 2>/dev/null | head -50", "timeout": 30}`
65. **bash** `{"command": "cd /work/experiments/harness-verifier-eval/outputs && ls -la *.md; echo \"=== noaudit ===\"; cat noaudit-cited.md 2>/dev/null; echo \"=== unsupported-audit head ===\"; head -25 unsupported-audit.md 2>/dev/null; echo \"=== unsupported-default ===\"; cat unsupported-default-cited.md 2>/dev/null | head -30", "timeout": 30}`
66. **bash** `{"command": "for d in 52ff045b-a8f1-4f11-a850-de2cd5362c53 f63e0c1e-0d54-484c-9a69-98c214609cec de33d54a-9182-4a9c-91e2-96ef067dc5f5; do echo \"== ${d:0:8} ==\"; ls -la /tmp/pi-subagents-uid-1000/async-subagent-runs/$d/ 2>/dev/null | head -5; tail -c 300 /tmp/pi-subagents-uid-1000/async-subagent-runs/$d/output-0.log 2>/dev/null | tr -d '\\000'; echo; done", "timeout": 30}`
67. **bash** `{"command": "sleep 10; cd /work/experiments/harness-verifier-eval/outputs && ls -la *.md; echo; find /work/experiments/harness-verifier-eval -name 'noaudit*' -o -name 'unsupported-audit*' | head", "timeout": 40}`
68. **bash** `{"command": "cd /work/experiments/harness-verifier-eval/outputs && echo \"=== noaudit-cited.md ===\"; cat noaudit-cited.md; echo; echo \"=== unsupported-default-cited.md ===\"; cat unsupported-default-cited.md", "timeout": 30}`
69. **bash** `{"command": "cd /work/experiments/harness-verifier-eval/outputs && sed -n '1,60p' unsupported-audit.md", "timeout": 30}`
70. **subagent** `{"agent": "verifier", "task": "Read experiments/harness-verifier-eval/inputs/draft-treatment.md and experiments/harness-verifier-eval/inputs/research-notes.md. Verify the draft per your agent instructions. Write the verified document to experiments/harness-verifier-eval/outputs/default-contract-cited.md. Do not edit the input files.", "async": true, "output": false}`
71. **bash** `{"command": "cd /work/experiments/harness-verifier-eval/outputs && cat notesfree-cited.md; echo \"=== control full ===\"; cat control-cited.md", "timeout": 30}`
72. **bash** `{"command": "cd /work && python3 - <<'PY'\nfrom pathlib import Path\np=Path('experiments/harness-verifier-eval/scorecard.md')\nt=p.read_text()\nt=t.replace(\"\"\"## Arm 4 — unsupported (3 plausible-but-unsupported claims + contradicted items, notes supplied)\n\nTODO: score when `unsupported-cited.md` and `unsupported-audit.md` land.\n\n## Arm 5 — no-audit (default output contract; audit not requested)\n\nTODO: score when `noaudit-cited.md` lands. Measure whether corrections are disclosed without an explicit audit request (tests observability of the verifier's work).\n\"\"\",\"\"\"## Arm 4 — un …[+1784 chars]`
73. **bash** `{"command": "cd /work && curl -sIL --max-time 25 https://github.com/Companion-Inc/feynman | head -3; echo \"---\"; curl -s --max-time 25 \"https://api.github.com/repos/Companion-Inc/feynman\" | jq -r '.full_name, .description, .stargazers_count, .license.spdx_id' 2>/dev/null", "timeout": 60}`
74. **bash** `{"command": "cd /work/experiments/harness-verifier-eval/outputs && ls -la default-contract-cited.md 2>/dev/null && head -30 default-contract-cited.md", "timeout": 30}`
   - _tool error:_ (no output)

Command exited with code 2
75. **write** `{"path": "/work/outputs/feynman-harness-eval-case-study.md", "content": "# Feynman as an Eval Harness: A Dogfooded Case Study\n\n**Status:** experiment run 2026-11-14; 7 verifier arms, N = 1 per arm. All claims below trace to files under `experiments/` or to a source URL in §Sources. Where a check failed or was not run, it says so.\n\n**Harness under test:** Feynman 0.5.65 (local install `/opt/feynman/feynman-0.5.65-linux-arm64/app`), model `openrouter/deepseek/deepseek-v4.1-flash-1017`, reasoning level `high`. Every subagent in the experiment inherited that model (confirmed from child session …[+22797 chars]`
76. **bash** `{"command": "cd /work/experiments/harness-verifier-eval/outputs && cat default-contract-cited.md; echo \"=== files ===\"; ls -la *.md", "timeout": 30}`
77. **bash** `{"command": "cd /work && python3 - <<'PY'\nfrom pathlib import Path\np=Path('experiments/harness-verifier-eval/scorecard.md')\nt=p.read_text()\nt=t.replace(\"\"\"## Summary so far\n\n| Arm | Planted items | Caught | Unjustified removals | Disclosed in cited doc |\n|---|---|---|---|---|\n| treatment | 8 | 8 | 0/7 clean | 8/8 |\n| control | 0 (15 true claims) | — | 0/15 | n/a |\n| notesfree | 8 | 8 | 0/7 clean | 3/8 (removals only; 5 silent numeric corrections) |\n| unsupported (instructed) | 10 | 10 | 0/10 | 10/10 |\n| unsupported-default | 10 | 10 | 0/10 | 9/9 changed items listed |\n| no-audi …[+1309 chars]`
78. **bash** `{"command": "cd /work && python3 - <<'PY'\nfrom pathlib import Path\np=Path('outputs/feynman-harness-eval-case-study.md')\nt=p.read_text()\nt=t.replace(\"\"\"2. **The bundled verifier is genuinely good at catching planted errors.** Across 6 completed arms it caught **44 of 44 planted item instances** (11 distinct error types) with **0 unjustified removals** of true claims — including a wrong-but-live arXiv ID, a fabricated quote, and three plausible-but-unsupported claims.\n3. **Its weak point is disclosure, not detection.** The verifier's default output contract requires a \"Removed Unsupport …[+5042 chars]`
79. **bash** `{"command": "cd /work && python3 - <<'PY'\nimport json,glob,collections,os\nbase='/state/.feynman/sessions/2026-11-14T08-05-41-567Z_01a1d917-3e3f-7157-8f13-31ea82eed8fd'\nlabels={\n'd73697d4':'treatment','65bc97c1':'control','62a40724':'notesfree','52ff045b':'unsupported',\n'de33d54a':'unsupported-default','f63e0c1e':'no-audit','cf64d430':'default-contract'}\nrows=[]\nfor d in sorted(glob.glob(base+'/*/run-0/session.jsonl')):\n    key=d.split('/')[-3][:8]\n    u=collections.Counter(); tools=collections.Counter(); msgs=0\n    for line in open(d,encoding='utf-8',errors='replace'):\n        try:  …[+855 chars]`
80. **bash** `{"command": "cd /work && python3 - <<'PY'\nfrom pathlib import Path\np=Path('outputs/feynman-harness-eval-case-study.md')\nt=p.read_text()\nold=\"\"\"| Arm | Input | Output | Input+Output | Wall-clock behavior |\n|---|---|---|---|---|\n| treatment | 26,466 | 11,624 | 38,090 | notes supplied |\n| control | 28,075 | 12,910 | 40,985 | notes supplied |\n| notesfree | 57,990 | 16,556 | 74,546 | fetched HTML + PDF itself |\n| unsupported | 29,134 | 2,056 | 31,190 | notes supplied |\n| no-audit | 5,284 | 1,475 | 6,759 | short run |\n\nSupplying notes roughly halves input tokens for the same draft (38 …[+1473 chars]`
   - _tool error:_ ok


Command exited with code 1
81. **bash** `{"command": "cd /work/experiments/harness-verifier-eval/logs && jq -r '.message.items[0] | {DOI, type, issued, authors: [.author[]?.family], title: .title[0]}' crossref-query.json; echo \"--- urls ---\"; for u in https://arxiv.org/abs/1706.03762 https://arxiv.org/abs/2411.00640 https://arxiv.org/abs/2405.14782 https://arxiv.org/abs/2411.12990 https://inspect.aisi.org.uk/ https://github.com/Companion-Inc/feynman; do printf '%-45s %s\\n' \"$u\" \"$(curl -sL -o /dev/null -w '%{http_code}' --max-time 25 \"$u\")\"; done", "timeout": 120}`
82. **bash** `{"command": "cd /work && grep -n \"TODO\\|TBD\\|pending\" outputs/feynman-harness-eval-case-study.md experiments/harness-verifier-eval/scorecard.md | head -20; echo \"--- word count ---\"; wc -w outputs/feynman-harness-eval-case-study.md", "timeout": 30}`
83. **bash** `{"command": "cd /work && python3 - <<'PY'\nfrom pathlib import Path\np=Path('experiments/harness-session-audit/audit.py')\nt=p.read_text()\nt=t.replace(\"\"\"    tool_errors = 0\n    paths = set()\n    all_text = []\"\"\",\"\"\"    tool_errors = 0\n    paths = set()\n    all_text = []\n    assistant_text = []\n    first_ts = last_ts = None\"\"\")\nt=t.replace(\"\"\"            rows.append(ev)\"\"\",\"\"\"            rows.append(ev)\n            ts = ev.get(\"timestamp\")\n            if ts:\n                first_ts = first_ts or ts\n                last_ts = ts\"\"\")\nt=t.replace(\"\"\"      …[+1432 chars]`
84. **bash** `{"command": "cd /work && sha256sum experiments/harness-verifier-eval/GROUND-TRUTH.md experiments/harness-verifier-eval/inputs/*.md experiments/harness-verifier-eval/logs/crossref-query.json experiments/harness-verifier-eval/outputs/*.md | sed 's|/work/||' | head -30", "timeout": 30}`
85. **write** `{"content": "# Provenance — `feynman-harness-eval-case-study.md`\n\nRun date: 2026-11-14\nHarness: Feynman 0.5.65 (`/opt/feynman/feynman-0.5.65-linux-arm64/app`)\nModel: `openrouter/deepseek/deepseek-v4.1-flash-1017`, reasoning `high`\nWorkspace: `/work`\nLead session: `/state/.feynman/sessions/2026-11-14T08-05-41-567Z_01a1d917-3e3f-7157-8f13-31ea82eed8fd.jsonl`\n\n## Source accounting\n\n| # | Source | How used | Status |\n|---|---|---|---|\n| 1 | Vaswani et al. 2017, arXiv:1706.03762 | Ground truth for planted claims; full HTML v7 and abstract page saved locally | live, content matched (HTTP …[+4663 chars]`
86. **bash** `{"command": "cd /work && python3 - <<'PY'\nfrom pathlib import Path\np=Path('outputs/.plans/feynman-harness-eval.md')\nt=p.read_text()\nt=t.replace(\"\"\"| T3 | Run verifier arms (treatment / control / notes-free) | subagents | todo | experiments/harness-verifier-eval/outputs/ |\n| T4 | Score outputs against ground truth | lead | todo | experiments/harness-verifier-eval/scorecard.md |\n| T5 | Session observability audit | lead | todo | experiments/harness-session-audit/ |\n| T6 | Write case study | lead | todo | outputs/feynman-harness-eval-case-study.md |\n| T7 | Provenance sidecar | lead | t …[+1077 chars]`
87. **bash** `{"command": "cd /work && python3 - <<'PY'\nfrom pathlib import Path\np=Path('outputs/.plans/feynman-harness-eval.md')\nt=p.read_text()\nt=t.replace('| T1 | Static inventory of harness rules and agent contracts | lead | in_progress | notes |','| T1 | Static inventory of harness rules and agent contracts | lead | done | notes/feynman-harness-static-analysis.md |')\nt=t.replace('Direct static analysis (no researchers) + one small controlled experiment with 3 verifier subagents.\\nRationale: the claim under test is about the harness\\'s own verification behavior; a 3-arm, N=1-per-arm experiment is …[+405 chars]`
88. **bash** `{"command": "cd /work && python3 - <<'PY'\nfrom pathlib import Path\np=Path('outputs/feynman-harness-eval-case-study.md')\nt=p.read_text()\nreps=[\n(\"but 0 shipped tests or eval suites, and 0 runtime checks\",\"but no shipped output-quality tests or eval suites, and 0 runtime checks\"),\n(\"- Draft: `experiments/harness-verifier-eval/inputs/draft-treatment.md` (~150 words, 15 claims).\",\"- Draft: `experiments/harness-verifier-eval/inputs/draft-treatment.md` (~150 words, 15 sentences).\"),\n(\"### 4.1 Detection: every planted item, in every completed arm\",\"### 4.1 Detection: every planted i …[+1281 chars]`
89. **bash** `{"command": "cd /work && python3 - <<'PY'\nplanted={'treatment':8,'notesfree':8,'unsupported':10,'unsupported-default':10,'no-audit':8,'default-contract':8}\nclean={'treatment':7,'notesfree':7,'no-audit':7,'default-contract':7,'control':15}\nprint('planted sum',sum(planted.values()))\nprint('clean sum',sum(clean.values()))\ncost=[38090,40985,74546,49422,28249,26681,30616]\ninp=[26466,28075,57990,38816,20962,18465,21685]\nout=[11624,12910,16556,10606,7287,8216,8931]\nprint('cost sum',sum(cost),'in',sum(inp),'out',sum(out))\nassert sum(cost)==288589 and sum(inp)==212459 and sum(out)==76130\nprin …[+210 chars]`
90. **bash** `{"command": "cd /work && cat experiments/harness-verifier-eval/scorecard.md", "timeout": 30}`
91. **bash** `{"command": "cd /work && python3 experiments/harness-session-audit/audit.py \"$PI_SESSION_FILE\" --json experiments/harness-session-audit/final.json | python3 -c \"\nimport json,sys\nd=json.load(sys.stdin)\nprint('events',d['events'],'tool_calls',d['tool_calls_total'],'errors',d['tool_errors'])\nprint('tools',d['tool_calls'])\nprint('usage',d['usage'])\nprint('artifacts',d['artifact_paths_mentioned'],'urls',d['distinct_urls_in_transcript'])\nprint('first',d['first_timestamp'],'last',d['last_timestamp'])\n\"", "timeout": 30}`
92. **bash** `{"command": "cd /work && sed -i 's/| unsupported-default | 10 | 10 | 0\\/10 | 9\\/9 changed items listed |/| unsupported-default | 10 | 10 | 0\\/10 | all changed items listed (9 bullets cover 10 planted items) |/' experiments/harness-verifier-eval/scorecard.md && grep -n 'unsupported-default | 10' experiments/harness-verifier-eval/scorecard.md", "timeout": 30}`
93. **bash** `{"command": "date -u; echo \"---\"; tail -2 \"$PI_SESSION_FILE\" | cut -c1-300; echo \"--- count lines ---\"; wc -l \"$PI_SESSION_FILE\"", "timeout": 30}`
94. **bash** `{"command": "cd /work && python3 - <<'PY'\nfrom pathlib import Path\np=Path('outputs/feynman-harness-eval-case-study.md')\nt=p.read_text()\nanchor=\"\"\"---\n\n## 5. Eval-quality assessment\"\"\"\nsection=\"\"\"### 4.5 Operational dogfooding notes\n\nBecause the case study ran inside the harness, the session transcript is itself evidence about the harness. At the snapshot used for this write-up (2026-11-14 08:10 UTC, ~5 minutes into the run):\n\n| Observation | Value |\n|---|---|\n| Lead tool calls | 92 (`bash` 77, `subagent` 8, `feynman_science_database_search` 3, `web_search` 2, `write` 2) | …[+1186 chars]`
95. **bash** `{"command": "cd /work && python3 - <<'PY'\nfrom pathlib import Path\np=Path('outputs/feynman-harness-eval-case-study.md')\nt=p.read_text()\nt=t.replace(\"It has 71 imperative integrity rules across 3,537 words of prompt policy\",\"It has 71 imperative-rule markers (`must`/`never`/`do not`/…) across 3,537 words of prompt policy\")\np.write_text(t)\nPY\ngrep -n \"71 imperative\" outputs/feynman-harness-eval-case-study.md; echo \"---\"; grep -nE \"TODO|TBD|FIXME|\\[\\[\" outputs/feynman-harness-eval-case-study.md experiments/harness-verifier-eval/scorecard.md outputs/feynman-harness-eval-case-stu …[+33 chars]`
96. **bash** `{"command": "cd /work && for f in outputs/feynman-harness-eval-case-study.md outputs/feynman-harness-eval-case-study.provenance.md experiments/harness-verifier-eval/scorecard.md experiments/harness-verifier-eval/GROUND-TRUTH.md notes/feynman-harness-static-analysis.md; do printf '%-70s %s lines %s words\\n' \"$f\" \"$(wc -l < $f)\" \"$(wc -w < $f)\"; done; echo \"--- mermaid check ---\"; grep -c '```mermaid' outputs/feynman-harness-eval-case-study.md; echo \"--- table rows ---\"; grep -c '^|' outputs/feynman-harness-eval-case-study.md", "timeout": 30}`
   - _tool error:_ 11:1. **Feynman is an evidence-production harness, not an eval harness.** It has 71 imperative-rule markers (`must`/`never`/`do not`/…) across 3,537 words of prompt policy, 4 research agents, 16 skills, and 11 workflow prompts — but no shipped output-quality tests or eval suites, and 0 runtime check …[+131 chars]
97. **bash** `{"command": "cd /work && python3 - <<'PY'\nimport json\np='/state/.feynman/sessions/2026-11-14T08-05-41-567Z_01a1d917-3e3f-7157-8f13-31ea82eed8fd.jsonl'\nfor line in open(p,encoding='utf-8',errors='replace'):\n    try: e=json.loads(line)\n    except: continue\n    if e.get('type')!='message': continue\n    c=e.get('message',{}).get('content')\n    if not isinstance(c,list): continue\n    for part in c:\n        if isinstance(part,dict) and part.get('type')=='toolCall' and part.get('name')=='subagent':\n            a=part.get('arguments') or {}\n            print({k:(v if k!='task' else str(v)[ …[+49 chars]`
98. **bash** `{"command": "cd /work && python3 - <<'PY'\nfrom pathlib import Path\np=Path('outputs/feynman-harness-eval-case-study.md')\nt=p.read_text()\nt=t.replace(\"| Subagent launches | 8 (one 3-child workflow + five single runs) |\",\"| `subagent` tool calls | 8: 5 launches (1 workflow × 3 children + 4 single runs), 2 status checks, 1 malformed call |\")\nt=t.replace(\"| Recorded tool errors | 0 |\",\"| Child-run failures | 0 (all 7 verifier runs completed and wrote their files) |\")\np.write_text(t)\nprint('ok')\nPY\npython3 experiments/harness-session-audit/audit.py \"$PI_SESSION_FILE\" --json experi …[+286 chars]`
99. **bash** `{"command": "cd /work && python3 -c \"\nimport json; d=json.load(open('experiments/harness-session-audit/final.json')); print(d['tool_calls'])\"", "timeout": 30}`
100. **bash** `{"command": "cd /work && python3 - <<'PY'\nfrom pathlib import Path\np=Path('outputs/feynman-harness-eval-case-study.md')\nt=p.read_text()\nt=t.replace(\"At the snapshot used for this write-up (2026-11-14 08:10 UTC, ~5 minutes into the run):\",\"At the snapshot used for this write-up (2026-11-14 08:11 UTC, ~5.5 minutes into the run):\")\nt=t.replace(\"| Lead tool calls | 92 (`bash` 77, `subagent` 8, `feynman_science_database_search` 3, `web_search` 2, `write` 2) |\",\"| Lead tool calls | 98 (`bash` 83, `subagent` 8, `feynman_science_database_search` 3, `web_search` 2, `write` 2) |\")\nt=t.repl …[+273 chars]`
101. **bash** `{"command": "cd /work && sed -i 's|├── inputs/                  # 4 drafts + research notes|├── inputs/                  # 3 drafts + research notes|' outputs/feynman-harness-eval-case-study.md && grep -n \"3 drafts\" outputs/feynman-harness-eval-case-study.md; echo \"--- final tree ---\"; find experiments/harness-verifier-eval -maxdepth 2 -type f | sort; echo; ls -la outputs/feynman-harness-eval-case-study*", "timeout": 30}`
102. **bash** `{"command": "cd /work && python3 - <<'PY'\nimport re\nt=open('outputs/feynman-harness-eval-case-study.md').read()\n# sanity: numbers referenced vs tables\nfor n in ['52','43','288,589','212,459','76,130','3,537','71','16','11']:\n    print(n, t.count(n))\n# check markdown tables have consistent pipe counts per block\nbad=0\nfor block in re.split(r'\\n\\s*\\n',t):\n    lines=[l for l in block.splitlines() if l.strip().startswith('|')]\n    if len(lines)>=3:\n        counts={l.count('|') for l in lines}\n        if len(counts)>1:\n            bad+=1\n            print('INCONSISTENT TABLE:', line …[+74 chars]`
103. **bash** `{"command": "cd /work && python3 - <<'PY'\nfrom pathlib import Path\np=Path('outputs/feynman-harness-eval-case-study.md')\nt=p.read_text()\nt=t.replace(\"One run with a full audit table still silently corrected five numbers in the cited document; another disclosed nothing when the output filename signaled \\\"no audit.\\\"\",\"One run with a full audit table still silently corrected five numbers in the cited document; a filename-confounded run disclosed nothing at all.\")\np.write_text(t)\nprint('ok')\nPY\ngrep -n \"filename-confounded\" outputs/feynman-harness-eval-case-study.md; echo \"---\" …[+70 chars]`
   - _said:_ I ran the case study inside Feynman, including a controlled audit of its own verifier. Here's what I found.

## What I did

1. **Static audit of the shipped harness** — counted the policy surface and checked whether any of it is enforced in code.
2. **Planted-error experiment** — 7 verifier arms on a 150-word draft about *Attention Is All You Need*: contradicted claims, a fabricated quote, a dead  …[+3042 chars]

Last stopReason: `stop` (assistant messages this turn: 75)

## Final reply

I ran the case study inside Feynman, including a controlled audit of its own verifier. Here's what I found.

## What I did

1. **Static audit of the shipped harness** — counted the policy surface and checked whether any of it is enforced in code.
2. **Planted-error experiment** — 7 verifier arms on a 150-word draft about *Attention Is All You Need*: contradicted claims, a fabricated quote, a dead URL, a wrong-but-live arXiv ID, plausible-but-unsupported claims, plus a clean control.
3. **Scored detection, false positives, and disclosure** against a pre-registered ground-truth key.

## Key results

- **Feynman is an evidence-production harness, not an eval harness.** 71 imperative-rule markers across 3,537 words of prompt policy, 4 agents, 16 skills — but **no shipped output-quality tests**, and **no runtime check** that a provenance sidecar exists, a citation resolves, or a number matches its source. `grep` for `.provenance` in `dist/`, `extensions/`, and `bin/` returns 0.
- **The verifier is genuinely strong on bounded, source-checkable drafts.** 52/52 planted item instances caught across 7 arms, 0 unjustified removals across 43 clean-claim checks. It caught misattributed numbers, a fabricated quote, a wrong-but-live citation, and all three unsupported claims even without an explicit absence instruction.
- **Disclosure is the weak link.** The output contract requires a "Removed Unsupported Claims" section but not a corrections log. One run with a complete audit table still silently changed five numbers in the cited document. A repaired draft can look identical to a clean one — there is no draft↔cited diff primitive.
- **It surfaced real source hazards.** Crossref returns three 2025 `posted-content` lookalikes with the correct title and author list for a 2017 paper (`10.65215/*`), and the paper contradicts itself on EN→FR BLEU (41.0 in §6.1 vs 41.8 in the abstract/Table 2). All seven verifier runs flagged the latter.
- **Operational dogfooding:** 98 lead tool calls, 8 `subagent` calls, 0 child-run failures, ~5.5 minutes. File-based handoffs and the JSONL session log made the run reconstructible.

## Caveats

N = 1 per arm, one model (`deepseek-v4.1-flash`), short drafts, unblinded manual scoring. The `no-audit` arm was confounded by its filename and is excluded; a neutral-filename arm replaces it. `/deepresearch` and `/lit` were not run end-to-end. This is a failure-mode demonstration, not a reliability estimate.

## Artifacts

- `outputs/feynman-harness-eval-case-study.md` — the case study
- `outputs/feynman-harness-eval-case-study.provenance.md` — source accounting, verification log, hashes
- `experiments/harness-verifier-eval/scorecard.md` — per-arm scores
- `experiments/harness-verifier-eval/outputs/` — all cited docs and audit tables
- `notes/feynman-harness-static-analysis.md` — static counts
- `experiments/harness-session-audit/audit.py` + `final.json` — session telemetry

**Sources:** [Vaswani et al. 2017, arXiv:1706.03762](https://arxiv.org/abs/1706.03762) · [Miller 2024, arXiv:2411.00640](https://arxiv.org/abs/2411.00640) · [Biderman et al. 2024, arXiv:2405.14782](https://arxiv.org/abs/2405.14782) · [Reuel et al. 2024, arXiv:2411.12990](https://arxiv.org/abs/2411.12990) · [Inspect](https://inspect.aisi.org.uk/) · [Feynman repo](https://github.com/Companion-Inc/feynman) · [Crossref query](https://api.crossref.org/works?query=Attention+Is+All+You+Need+Vaswani+2017&rows=3)

## Files created this turn

- state/.feynman/sessions/2026-11-14T08-05-41-567Z_01a1d917-3e3f-7157-8f13-31ea82eed8fd.jsonl
- state/.feynman/sessions/2026-11-14T08-05-41-567Z_01a1d917-3e3f-7157-8f13-31ea82eed8fd/52ff045b-a8f1-4f11-a850-de2cd5362c53/run-0/session.jsonl
- state/.feynman/sessions/2026-11-14T08-05-41-567Z_01a1d917-3e3f-7157-8f13-31ea82eed8fd/62a40724-7cba-4f88-9ee2-5d422a34913b/run-0/session.jsonl
- state/.feynman/sessions/2026-11-14T08-05-41-567Z_01a1d917-3e3f-7157-8f13-31ea82eed8fd/65bc97c1-3dde-4f28-846d-262138c622bd/run-0/session.jsonl
- state/.feynman/sessions/2026-11-14T08-05-41-567Z_01a1d917-3e3f-7157-8f13-31ea82eed8fd/cf64d430-3e71-449c-9128-b3c9a9770461/run-0/session.jsonl
- state/.feynman/sessions/2026-11-14T08-05-41-567Z_01a1d917-3e3f-7157-8f13-31ea82eed8fd/d73697d4-e891-457a-b8e0-614acf937de7/run-0/session.jsonl
- state/.feynman/sessions/2026-11-14T08-05-41-567Z_01a1d917-3e3f-7157-8f13-31ea82eed8fd/de33d54a-9182-4a9c-91e2-96ef067dc5f5/run-0/session.jsonl
- state/.feynman/sessions/2026-11-14T08-05-41-567Z_01a1d917-3e3f-7157-8f13-31ea82eed8fd/f63e0c1e-0d54-484c-9a69-98c214609cec/run-0/session.jsonl
- state/.feynman/sessions/subagent-artifacts/52ff045b-a8f1-4f11-a850-de2cd5362c53_verifier_input.md
- state/.feynman/sessions/subagent-artifacts/52ff045b-a8f1-4f11-a850-de2cd5362c53_verifier_meta.json
- state/.feynman/sessions/subagent-artifacts/52ff045b-a8f1-4f11-a850-de2cd5362c53_verifier_output.md
- state/.feynman/sessions/subagent-artifacts/52ff045b-a8f1-4f11-a850-de2cd5362c53_verifier_transcript.jsonl
- state/.feynman/sessions/subagent-artifacts/62a40724-7cba-4f88-9ee2-5d422a34913b_verifier_input.md
- state/.feynman/sessions/subagent-artifacts/62a40724-7cba-4f88-9ee2-5d422a34913b_verifier_meta.json
- state/.feynman/sessions/subagent-artifacts/62a40724-7cba-4f88-9ee2-5d422a34913b_verifier_output.md
- state/.feynman/sessions/subagent-artifacts/62a40724-7cba-4f88-9ee2-5d422a34913b_verifier_transcript.jsonl
- state/.feynman/sessions/subagent-artifacts/65bc97c1-3dde-4f28-846d-262138c622bd_verifier_input.md
- state/.feynman/sessions/subagent-artifacts/65bc97c1-3dde-4f28-846d-262138c622bd_verifier_meta.json
- state/.feynman/sessions/subagent-artifacts/65bc97c1-3dde-4f28-846d-262138c622bd_verifier_output.md
- state/.feynman/sessions/subagent-artifacts/65bc97c1-3dde-4f28-846d-262138c622bd_verifier_transcript.jsonl
- state/.feynman/sessions/subagent-artifacts/cf64d430-3e71-449c-9128-b3c9a9770461_verifier_input.md
- state/.feynman/sessions/subagent-artifacts/cf64d430-3e71-449c-9128-b3c9a9770461_verifier_meta.json
- state/.feynman/sessions/subagent-artifacts/cf64d430-3e71-449c-9128-b3c9a9770461_verifier_output.md
- state/.feynman/sessions/subagent-artifacts/cf64d430-3e71-449c-9128-b3c9a9770461_verifier_transcript.jsonl
- state/.feynman/sessions/subagent-artifacts/d73697d4-e891-457a-b8e0-614acf937de7_verifier_input.md
- state/.feynman/sessions/subagent-artifacts/d73697d4-e891-457a-b8e0-614acf937de7_verifier_meta.json
- state/.feynman/sessions/subagent-artifacts/d73697d4-e891-457a-b8e0-614acf937de7_verifier_output.md
- state/.feynman/sessions/subagent-artifacts/d73697d4-e891-457a-b8e0-614acf937de7_verifier_transcript.jsonl
- state/.feynman/sessions/subagent-artifacts/de33d54a-9182-4a9c-91e2-96ef067dc5f5_verifier_input.md
- state/.feynman/sessions/subagent-artifacts/de33d54a-9182-4a9c-91e2-96ef067dc5f5_verifier_meta.json
- state/.feynman/sessions/subagent-artifacts/de33d54a-9182-4a9c-91e2-96ef067dc5f5_verifier_output.md
- state/.feynman/sessions/subagent-artifacts/de33d54a-9182-4a9c-91e2-96ef067dc5f5_verifier_transcript.jsonl
- state/.feynman/sessions/subagent-artifacts/f63e0c1e-0d54-484c-9a69-98c214609cec_verifier_input.md
- state/.feynman/sessions/subagent-artifacts/f63e0c1e-0d54-484c-9a69-98c214609cec_verifier_meta.json
- state/.feynman/sessions/subagent-artifacts/f63e0c1e-0d54-484c-9a69-98c214609cec_verifier_output.md
- state/.feynman/sessions/subagent-artifacts/f63e0c1e-0d54-484c-9a69-98c214609cec_verifier_transcript.jsonl
- work/experiments/harness-session-audit/audit.py
- work/experiments/harness-session-audit/final.json
- work/experiments/harness-session-audit/prelim.json
- work/experiments/harness-verifier-eval/GROUND-TRUTH.md
- work/experiments/harness-verifier-eval/inputs/draft-control.md
- work/experiments/harness-verifier-eval/inputs/draft-treatment.md
- work/experiments/harness-verifier-eval/inputs/draft-unsupported.md
- work/experiments/harness-verifier-eval/inputs/research-notes.md
- work/experiments/harness-verifier-eval/logs/abs-2405.14782.html
- work/experiments/harness-verifier-eval/logs/abs-2411.00640.html
- work/experiments/harness-verifier-eval/logs/arxiv-abs.html
- work/experiments/harness-verifier-eval/logs/arxiv-html.html
- work/experiments/harness-verifier-eval/logs/crossref-query.json
- work/experiments/harness-verifier-eval/outputs/control-audit.md
- work/experiments/harness-verifier-eval/outputs/control-cited.md
- work/experiments/harness-verifier-eval/outputs/default-contract-cited.md
- work/experiments/harness-verifier-eval/outputs/noaudit-cited.md
- work/experiments/harness-verifier-eval/outputs/notesfree-audit.md
- work/experiments/harness-verifier-eval/outputs/notesfree-cited.md
- work/experiments/harness-verifier-eval/outputs/treatment-audit.md
- work/experiments/harness-verifier-eval/outputs/treatment-cited.md
- work/experiments/harness-verifier-eval/outputs/unsupported-audit.md
- work/experiments/harness-verifier-eval/outputs/unsupported-cited.md
- work/experiments/harness-verifier-eval/outputs/unsupported-default-cited.md
- work/experiments/harness-verifier-eval/scorecard.md
- work/notes/feynman-harness-static-analysis.md
- work/outputs/.plans/feynman-harness-eval.md
- work/outputs/.plans/harness-verifier-eval-workflow.js
- work/outputs/feynman-harness-eval-case-study.md
- work/outputs/feynman-harness-eval-case-study.provenance.md

## Files modified this turn

(none)
