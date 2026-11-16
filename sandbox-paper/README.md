# sandbox-paper: Feynman `audit` / `replicate` on a target paper and its code

A variant of `../sandbox`. Same runner (`fp` wraps `../sandbox/fs`, so every `fs` command works), same pinned Feynman 0.5.65, model and keys. What's different:

| | baseline `sandbox/` | `sandbox-paper/` |
|---|---|---|
| image | `feynman-sandbox:0.5.65` | `feynman-sandbox-paper:0.5.65` = baseline + python3 3.11, venv, pip, git, build tools |
| runs | `sandbox/runs/` | `/Volumes/fs-runs/paper/` if that external image is mounted, else `sandbox-paper/runs/` (see Storage) |
| `work/` at start | empty | fresh copy of `materials/` (paper PDF + code repo including `.git`) |
| resources | Docker defaults | `--memory 6g --cpus 4` (override with `FS_DOCKER_ARGS`) |

No scientific Python packages are preinstalled. Whether and how the agent installs numpy/sklearn/nltk, and fetches the pretrained data the code expects, is part of what gets observed.

## Keeping the paper anonymous

Nothing committed in this folder names the paper. The identifying parts are gitignored:
- `materials` is a local symlink to the paper folder (PDF + repo). Recreate it with `ln -s ../<paper-folder> sandbox-paper/materials`, or point `FS_SEED_WORK` elsewhere.
- `prompts/audit.md` and `prompts/replicate.md` name the paper, so they're local-only. The `env-*.md` answers are generic and committed.
- `runs/` contains everything (transcripts, copies of the paper), so it stays uncommitted.

## Setup

```sh
export DOCKER_CONTEXT=desktop-linux
sandbox-paper/fp build          # builds baseline image, then the variant
```

## How the commands work

`feynman audit X` and `feynman replicate X` just open the TUI with `/audit X` or `/replicate X` as the first message. Sending `/audit ...` as a one-shot prompt expands the same template (checked: the session's user message is the full audit instructions). So these are ordinary prompts to `fp ask`/`fp reply`, and the prompt files live in `prompts/`.

- **audit** (`prompts/audit.md`) is told not to wait for confirmation. It should finish in one turn with `outputs/.plans/<slug>.md` and `outputs/<slug>-audit.md`.
- **replicate** (`prompts/replicate.md`) has a built-in stop: it must ask where to execute (Local / venv / Docker / Modal / RunPod / Plan only) before running anything. So it takes at least two turns. Turn 2 is one of the environment answers in `prompts/env-*.md`.
  - "Local" means inside the container, which is already isolated, so it's the natural choice for this sandbox.
  - Docker, Modal and RunPod aren't available inside the container (no Docker socket, CLIs or keys). Choosing them tests how it handles a missing environment.

The prompt texts are drafts; edit them before running real batches. The hash in `fp ls` will show which version each run got.

## Designs

**Separate** (each workflow from a clean start):

```sh
sandbox-paper/fp batch -j 3 5 audit -f sandbox-paper/prompts/audit.md
sandbox-paper/fp batch -j 3 5 repl  -f sandbox-paper/prompts/replicate.md
sandbox-paper/fp reply-all -j 3 repl -f sandbox-paper/prompts/env-local.md   # answer the environment question
```

**Sequential** (replicate sees the audit in the same session and the audit files on disk):

```sh
sandbox-paper/fp batch -j 3 5 seq -f sandbox-paper/prompts/audit.md
sandbox-paper/fp reply-all -j 3 seq -f sandbox-paper/prompts/replicate.md
sandbox-paper/fp reply-all -j 3 seq -f sandbox-paper/prompts/env-local.md
```

Running both lets you compare whether a prior audit changes what the replication does. `fp ls` shows each run's prompt chain (`audit.md@… > replicate.md@… > env-local.md@…`).

Before sending the environment answer, check that each run actually stopped to ask (`fp packet <run>`). If a run went ahead without asking, that's a finding, and the answer won't make sense to it. `reply-all` sends to every run with the label, so reply per run with `fp reply` where they differ.

## Inspecting

- `fp packet <run> [turn]`: actions, final reply, files created/modified per turn
- `fp seeddiff <run>`: which of the seeded paper/repo files the agent modified or deleted (`logs/seed.sha256` is the manifest taken at creation)
- `fp export <run>`: HTML transcripts; subagent (researcher/verifier) transcripts are in `state/.feynman/sessions/subagent-artifacts/`
- `fp tui <run>`: continue interactively; `fp shell <run>`: look around inside

## Storage

Replication runs can be large, so `fp` keeps them on an external drive when one is set up. Runs are ordinary host folders bind-mounted into the container, so there is no Docker storage limit involved; the space comes from wherever the runs folder lives.

The external location is an APFS sparse disk image on the Lexar drive. The drive itself is exFAT with 512 KB clusters, so writing runs to it directly would make every small file (a Python environment has tens of thousands) take at least 512 KB. The image gives normal APFS behaviour and grows only as it fills.

```sh
# one-time (already done on this machine)
hdiutil create -size 500g -type SPARSEBUNDLE -fs APFS -volname fs-runs /Volumes/Lexar/fs-runs.sparsebundle
# after each reboot / replug
hdiutil attach /Volumes/Lexar/fs-runs.sparsebundle      # mounts at /Volumes/fs-runs
```

`fp` picks the runs folder in this order:
1. `FS_RUNS`, if set.
2. `/Volumes/fs-runs/paper`, if the image is mounted.
3. Refuses to run if the image file exists but isn't mounted, so runs don't end up split between two places without you noticing.
4. Otherwise `sandbox-paper/runs/`.

`sandbox-paper/runs` is a symlink to `/Volumes/fs-runs/paper` (gitignored), so the runs show up in the editor next to `sandbox/runs/`. It dangles while the image isn't mounted; `fp` refuses to run in that state anyway. On another machine, delete the symlink to use a local folder.

Override the paths with `FP_EXT_IMAGE` / `FP_EXT_MOUNT`. Every `fp` command (`ls`, `reply`, `judge`, …) uses the same rule, so they find the runs wherever they are. Unplugging the drive mid-run loses that run. Detach with `hdiutil detach /Volumes/fs-runs` when nothing is running.

## Caveats

- **Disk:** a real replication may download multi-GB pretrained data into the run's `work/`. Five runs could mean tens of GB in `runs/`. Check `du -sh /Volumes/fs-runs/paper/*` (or `sandbox-paper/runs/*`); see Storage.
- **Memory:** Docker Desktop here has ~7.6 GB total, so the default is 6g per container. Loading large data files may hit that limit (exit 137 in `fp ls`). Running in parallel splits memory between containers, so use `-j 1` for replication turns.
- **Turn length:** turns are one-shot `--prompt` calls with no time limit. A long replication just runs until the agent stops. Watch live with `docker ps` / `fp tui`.
- The agent can see the GitHub URL and the `.git` history and may clone or fetch upstream. Network is open, as in the baseline.
