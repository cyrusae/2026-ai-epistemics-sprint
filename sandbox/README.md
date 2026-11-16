# Feynman sandbox

Disposable, clean-room Feynman runs for repeated trials of the same prompt.

- **Image** (`Dockerfile`): Debian slim + the pinned Feynman 0.5.65 Linux bundle, checksum-verified against the GitHub release. Telemetry off. No memory package, no Zotero MCP, no web-search API keys (see "Differences from local").
- **Run directory** (`runs/<timestamp>-<label>-<rand>/`): one per trial. It holds everything that trial touched:
  - `state/.feynman/`: `FEYNMAN_HOME` (settings, `sessions/*.jsonl` transcripts, `sessions/subagent-artifacts/`, memory)
  - `work/`: Feynman's cwd (`outputs/`, `outputs/.drafts/`, `outputs/.plans/`, fetched sources)
  - `logs/turnNN.{prompt.md,stdout.txt,stderr.txt}` and `logs/turns.jsonl` (exit code, wall time, model)
  - `work/.sandbox/environment.txt`: bundle, version, model, image digest
- Containers are `--rm`. Nothing persists outside the run dir. The API key is passed as an env var and never written to disk.

## Usage

```sh
docker build -t feynman-sandbox:0.5.65 sandbox/      # once
# model is pinned to openrouter/deepseek/deepseek-v4.1-flash-1017 by default; override with FEYNMAN_MODEL=...

R=$(sandbox/fs new stickpoke)            # fresh run dir
sandbox/fs ask   $R -f prompts/p1.md     # turn 1, new session, non-interactive
# ...read $R/logs/turn01.stdout.txt and $R/work/outputs/, decide...
sandbox/fs reply $R -f prompts/p2.md     # turn 2, continues the same session
sandbox/fs tui   $R                      # or: take over interactively in the TUI
sandbox/fs shell $R                      # bash inside that run's sandbox
sandbox/fs export $R                     # session .jsonl -> HTML in work/.sandbox/html/

sandbox/fs batch 5 lit-q1 -f prompts/p1.md   # 5 fresh runs, turn 1 only
```

Keys are read from `../.env`: OpenRouter as a bare `sk-or-...` line or `OPENROUTER_API_KEY=...`, plus `EXA_API_KEY=...`. Already-exported env vars take precedence. Both keys are passed as env vars only and are never written into run dirs. `web-search.seed.json` mirrors the local non-secret web-search config.

**Model pin:** `deepseek/deepseek-v4.1-flash-1017`, the snapshot used in the original 2026-11-12/13 sessions. Note that unsuffixed `deepseek/deepseek-v4.1-flash` on OpenRouter is a *different* snapshot (2026-09-10).

## Two-prompt protocol (conditional follow-up)

```sh
sandbox/fs batch -j 4 10 q1 -f p1.md        # 10 fresh runs, 4 at a time, turn 1 only
sandbox/fs ls q1                            # per-run table + per-condition summary

# decide each run's turn 1, by hand...
sandbox/fs packet <run>                     # evidence packet (actions, final reply, files created)
sandbox/fs decide <run> not-attempted "no scaffolding, only prose"
# ...or with a local judge CLI (packet on stdin, cwd = empty temp dir; must print `VERDICT: <word>`)
sandbox/fs judge q1 -- claude -p "$(cat judge.md)"

sandbox/fs followup -j 4 q1 not-attempted -f p2.md   # turn 2 only for runs judged not-attempted
```

`agy -p` ignores stdin, so it needs the wrapper, which appends the packet to the prompt. Give it an absolute path, because the judge runs from an empty temp dir:

```sh
sandbox/fs judge q1 -- "$PWD/sandbox/agy-judge" "$(cat judge.md)" --model gemini-3.8-flash-high
```

- Verdict words are free-form. `followup` matches the first line of `logs/turn01.decision` exactly, skips runs that are already past turn 1, and lists undecided runs instead of guessing.
- Each decision file records its source (`human` or `judge` plus the command). The judge's full output is saved to `logs/turn01.judge.txt`. `fs decide` overwrites a judge verdict.
- Packets are built mechanically from the session `.jsonl` and before/after file snapshots (`logs/turnNN.files.tsv`, with sha256). Thinking blocks are deliberately left out, so a judge sees actions, not stated intentions.
- The judge runs in an empty temp dir so it can't read the repo. This matters because `poke-with-stick.md` contains the predictions.

## Conditions

Every turn records which prompt it got: `prompt` (the `-f` file's basename, or `inline`) and `prompt_sha256` (first 12 hex characters of the exact text) in `logs/turns.jsonl`. The exact text is also saved in `logs/turnNN.prompt.md`. `fs ls` shows the condition as `p1-b.md@abc123 > p2.md@def456`, so a run's conditions are visible even if the label doesn't say. The hash catches edits to a prompt file between batches. A good habit is to also put the condition in the label, e.g. `fs batch 10 base -f p1.md` and `fs batch 10 budget -f p1-b.md`, so `fs ls budget` filters by condition.

## Notes

- Keep `FEYNMAN_MODEL` the same across turns of a run. It applies per turn, so a different value switches models mid-session.
- `ask`/`reply` don't stream to the terminal; output goes to `logs/turnNN.stdout.txt`/`.stderr.txt`. Use `fs tui` to watch live.
- `ask`/`reply` use `--prompt`, which runs one turn and exits; stdout is only the final reply. The complete trace (system prompt, tool calls, subagent dispatches) is in the session `.jsonl`.
- Runs can be executed in parallel (each run dir is independent), subject to OpenRouter rate limits.

## Differences from local install (record these as conditions)

- No `@samfp/pi-memory` package (the source of cross-session memory locally).
- No Zotero MCP server.
- No pandoc or browser-preview runtime.

## Isolation

Each container mounts only its own run's `state/` and `work/`, plus read-only seed files. It cannot see other runs, the rest of the repo, or your home directory. What runs do share: outbound network/IP, the OpenRouter and Exa accounts (rate limits, spend), and the image. The web-search cache lives in each run's `state/`, so it is not shared.
