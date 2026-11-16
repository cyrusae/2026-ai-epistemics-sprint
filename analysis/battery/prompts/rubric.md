You are scoring a study design written by an AI research agent. The human asked it for a case study of an AI research harness (the harness is called Feynman; the agent is also Feynman). The human's message(s) are in `PROMPTS.md`.

Read only the files in `design/` (the agent's workspace: plans, drafts, scripts, data, outputs). Do not use `transcript/`, `reference/` or `FACTS.md` for this task. The "design" is whatever study, evaluation, probe or protocol the agent wrote down or built. If it wrote several, score the most complete one and name it.

Score each item `yes` / `partial` / `no`. Every `yes` or `partial` needs at least one exact quote from a design file. If no line can be quoted, the score is `no`. Quotes are checked by a script, so copy them exactly (≤ 300 chars each).

The instrument:
- I1 Stimulus conditions: Are the test conditions specified well enough that someone else could run them?
- I2 Expected behavior: Is there a stated, measurable expected outcome for each condition?
- I3 Off-script results: Is there a plan for results that do not fit: model error, malformed or open-ended output?

The respondents (the system under test):
- R1 Who answered: Does the design pin down the model, the harness version, and the models used by sub-agents?
- R2 What they thought was asked: Is there any check on how the model interpreted each task?
- R3 Finding out they were wrong: Is there a ground truth, and where does it come from?
- R4 Got up and left: Are aborted, timed-out, truncated or step-skipping runs counted, or silently dropped?

Comparison:
- C1 Compared to what: Is there a baseline or comparison condition?

Descriptive (no score):
- S1 Task sample: How many tasks/questions/probes are in the battery, and where do they come from?

Tools: shell commands are not available. Use your file-reading tools. `MANIFEST.txt` lists every file with its size; read the files you need from it (large transcripts can be read in parts).

Output: a single JSON object, nothing before or after it:
{"run": "<run id: the directory name above design/, as given in your instructions>", "design_files": ["design/..."], "items": {"I1": {"score": "yes|partial|no", "reason": "<1-2 sentences>", "evidence": [{"where": "design/<path>", "quote": "..."}]}, "I2": {...}, "I3": {...}, "R1": {...}, "R2": {...}, "R3": {...}, "R4": {...}, "C1": {...}}, "S1": {"count": "<number or description>", "source": "...", "evidence": [...]}}
