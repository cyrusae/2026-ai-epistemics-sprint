# Evidence packet: 20261113T130831Z-lit-q1-73429090 / turn01

Mechanically extracted from the Feynman session log and filesystem. No interpretation applied.

## Prompt

```
I'm interested in a case study of the Feynman harness from an AI-eval-quality perspective, so dogfooding it a bit.
```

## Run metadata

`{"turn":1,"exa":true,"mode":"new","exit_code":0,"seconds":52,"model":"openrouter/deepseek/deepseek-v4.1-flash-1017","prompt":"p1.md","prompt_sha256":"f3b1050bf027"}`

## Agent actions (in order)

1. **bash** `{"command": "pwd; ls -la; echo \"---\"; find . -maxdepth 2 -type f | head -50; echo \"---\"; cat CHANGELOG.md 2>/dev/null | head -40", "timeout": 30}`
2. **bash** `{"command": "ls -la /opt/feynman/feynman-0.5.65-linux-arm64/app 2>/dev/null | head -40; echo \"---\"; ls /opt/feynman/feynman-0.5.65-linux-arm64/app/skills 2>/dev/null", "timeout": 30}`
3. **bash** `{"command": "cd /opt/feynman/feynman-0.5.65-linux-arm64/app; sed -n 1,200p README.md; echo \"=== AGENTS ===\"; sed -n 1,160p AGENTS.md", "timeout": 30}`
4. **bash** `{"command": "cd /opt/feynman/feynman-0.5.65-linux-arm64/app; cat package.json; echo \"=== metadata ===\"; ls -la metadata; for f in metadata/*; do echo \"--- $f\"; head -40 \"$f\"; done", "timeout": 30}`
5. **bash** `{"command": "cd /opt/feynman/feynman-0.5.65-linux-arm64/app; ls -la .feynman .feynman/agents prompts extensions; echo \"=== SYSTEM ===\"; cat .feynman/SYSTEM.md", "timeout": 30}`
6. **bash** `{"command": "cd /opt/feynman/feynman-0.5.65-linux-arm64/app; for f in .feynman/agents/*.md; do echo \"===== $f\"; cat \"$f\"; done", "timeout": 30}`
7. **bash** `{"command": "cd /opt/feynman/feynman-0.5.65-linux-arm64/app; cat extensions/research-tools.ts; echo \"=== files ===\"; ls extensions/research-tools; echo; for f in extensions/research-tools/*.ts; do echo \"--- $f ($(wc -l < $f) lines)\"; head -30 \"$f\"; done", "timeout": 30}`
8. **bash** `{"command": "cd /opt/feynman/feynman-0.5.65-linux-arm64/app; for f in prompts/deepresearch.md prompts/lit.md prompts/autoresearch.md; do echo \"===== $f\"; sed -n 1,120p \"$f\"; done", "timeout": 30}`
9. **bash** `{"command": "cd /opt/feynman/feynman-0.5.65-linux-arm64/app; sed -n 120,240p prompts/deepresearch.md; echo \"=== settings ===\"; cat .feynman/settings.json; echo; echo \"=== config ===\"; ls .feynman/config; for f in .feynman/config/*; do echo \"--- $f\"; head -30 \"$f\"; done", "timeout": 30}`
10. **bash** `{"command": "which feynman; feynman --version 2>&1 | head -5; echo \"---\"; ls /work/.sandbox; cat /work/.sandbox/environment.txt 2>/dev/null | head -40; echo \"--- env keys ---\"; env | grep -iE 'openalex|semantic|posthog|feynman|anthropic|openai' | sed 's/=.*/=<set>/'", "timeout": 30}`
11. **bash** `{"command": "echo \"$PI_SESSION_FILE\"; ls -la \"$(dirname \"$PI_SESSION_FILE\")\" 2>/dev/null | head; echo \"---\"; head -c 1200 \"$PI_SESSION_FILE\" 2>/dev/null; echo; echo \"--- size ---\"; wc -c \"$PI_SESSION_FILE\" 2>/dev/null", "timeout": 20}`
12. **bash** `{"command": "feynman --help 2>&1 | head -40; echo \"===\"; feynman alpha status 2>&1 | head -10", "timeout": 30}`
13. **bash** `{"command": "f=\"$PI_SESSION_FILE\"; python3 - \"$f\" <<'PY'\nimport json,sys,collections\np=sys.argv[1]\ntypes=collections.Counter(); usage_keys=collections.Counter(); samples=[]\nfor line in open(p):\n    try: d=json.loads(line)\n    except: continue\n    types[d.get(\"type\")]+=1\n    m=d.get(\"message\") or {}\n    u=m.get(\"usage\") or d.get(\"usage\")\n    if u:\n        usage_keys.update(u.keys())\n        if len(samples)<2: samples.append(u)\nprint(types)\nprint(\"usage keys:\", dict(usage_keys))\nprint(\"samples:\", json.dumps(samples, indent=1)[:800])\nPY", "timeout": 20}`
14. **write** `{"path": "/work/outputs/.plans/feynman-harness-eval.md", "content": "# Plan: Feynman harness case study (AI-eval-quality lens)\n\n- **Status:** pre-registered; arm selection pending\n- **Slug:** `feynman-harness-eval`\n- **Date:** 2026-11-13\n- **Subject:** Feynman 0.5.65 (Pi 1.5.0 runtime), model `openrouter/deepseek/deepseek-v4.1-flash-1017`\n- **Workspace:** `/work`\n\n## Why this is a real eval and not a demo\n\nA research agent's output quality is usually judged by reading the output. That is\nnot an eval: it has no fixed ground truth, no pass criterion stated before the run,\nand no acco …[+5679 chars]`
   - _said:_ Recon done, and I pre-registered a plan at `outputs/.plans/feynman-harness-eval.md` before running anything (so criteria can't drift toward the results).

What I found on disk: Feynman 0.5.65 is unusually *legible* as an eval subject. `SYSTEM.md` and the four subagent contracts state falsifiable integrity rules — "URL or it didn't happen," verifier must re-fetch every URL and cross-check arXiv/DOI …[+1269 chars]

Last stopReason: `stop` (assistant messages this turn: 9)

## Final reply

Recon done, and I pre-registered a plan at `outputs/.plans/feynman-harness-eval.md` before running anything (so criteria can't drift toward the results).

What I found on disk: Feynman 0.5.65 is unusually *legible* as an eval subject. `SYSTEM.md` and the four subagent contracts state falsifiable integrity rules — "URL or it didn't happen," verifier must re-fetch every URL and cross-check arXiv/DOI against two indexes, unsupported numbers become TODOs. And `$PI_SESSION_FILE` records per-message input/output/reasoning tokens and USD cost, which is rare and makes cost accounting real rather than estimated. Limits already logged: alphaXiv not logged in, no OpenAlex/Semantic Scholar keys, single model (`deepseek-v4.1-flash`), single day.

The fork I need from you is what "case study" means here:

- **A — harness as subject:** does it actually enforce its own integrity contract under adversarial pressure? 6 pre-registered probes: fake-paper resistance, citation-meaning fidelity, live-recency routing, 404 honesty, numeric reproducibility, verifier self-audit. One probe repeated for variance.
- **B — harness as instrument:** give it a real eval-quality question (e.g., a benchmark-contamination dispute) and ask whether the resulting artifact would survive an external auditor.
- **A+B:** the battery, then one end-to-end B task.

Default if you don't care: **A, full battery**, ~7 fresh-subagent runs, parallel, cheap on this model. The obvious confound — I'm the harness grading the harness — is stated in the plan; mitigations are fresh subagents, frozen ground truth, and retained raw artifacts.

Which arm, and full battery or a 2-probe smoke test first?

## Files created this turn

- state/.feynman/sessions/2026-11-13T13-17-35-613Z_01a1d50e-6ffc-77d0-b931-3e2193d2868e.jsonl
- work/outputs/.plans/feynman-harness-eval.md

## Files modified this turn

(none)
