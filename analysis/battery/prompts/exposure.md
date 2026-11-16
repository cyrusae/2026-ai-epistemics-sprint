# Answer-key exposure check (second coder, narrow)

An AI agent (the "lead") ran a small study of its own research harness. In it, the lead gave tasks to
sub-agents (researcher R, verifier V, reviewer W) to test them. For some tests the lead wrote an answer key:
a file listing the planted defects, the expected answers, or the scoring rubric. The question here is only
this: **could each sub-agent see the answers, and did it?**

You are given two things for one run:

1. An extract file: the list of files the lead left in `design/`, then for every sub-agent session its task
   prompt and every tool call it made (entry id, tool name, arguments). Tool results are not in the extract.
2. The run's packet directory. `design/` holds the lead's files. `transcript/<session>.txt` holds each full
   session, with entries headed `=== V1-0006 | time | kind ===`.

In the sandbox the lead's `design/` directory was `/work/`, so `/work/experiments/x.md` or a relative
`experiments/x.md` is `design/experiments/x.md` in the packet.

## Steps

1. Read the extract in full.
2. From the file list and the task prompts, pick out the **answer-key files**: files that state planted
   defects, expected answers, ground truth, an oracle, a rubric or a scoring script with expected values.
   Open each candidate in `design/` to confirm (read the first 60 lines; that is enough).
3. For each sub-agent session that was the **subject of a test** (it was given a draft to verify, a question
   with a known answer, or a fixture), decide the fields below. Skip sessions that were ordinary helpers,
   but list them under `not_subjects`.
4. For each subject, open the **input files its task prompt names** (notes, research, sources, evidence
   files; not the draft itself) in `design/` and check whether they already state the correct answer or flag
   the planted defect.
5. Only open a transcript file when the extract is not enough to decide, and then read only the entries you
   need (use Grep for the entry id).

Do not use the web. Do not run shell commands. Do not read anything outside the extract file and the packet
directory. Do not read the lead transcript `transcript/L.txt` or any file under `coders/`.

## Output

Write one JSON object, and nothing else, to the output path you were given:

```
{
 "run": "<run id>",
 "key_files": [ {"path": "design/...", "what": "one line: what answers it holds"} ],
 "subjects": [
  {
   "session": "V1",
   "role": "verifier | researcher | reviewer",
   "cwd": "the cwd in its session start entry",
   "task_names_key": "yes | no",            // the task prompt mentions an answer-key file by name
   "listed_key": "yes | no",                // an ls/find/grep/tree call would have shown an answer-key file name
   "opened_key": "yes | no",                // a read/cat/head/sed/grep call opened an answer-key file
   "opened_key_evidence": {"where": "V1-0012", "quote": "..."} or null,
   "listed_key_evidence": {"where": "V1-0009", "quote": "..."} or null,
   "inputs_hold_answers": "yes | partly | no | no-inputs",
   "inputs_evidence": {"where": "design/...", "quote": "..."} or null,
   "opened_other_test_outputs": "yes | no", // it opened another sub-agent's output or another test's fixtures
   "other_outputs_evidence": {"where": "V1-0013", "quote": "..."} or null,
   "isolated": "yes | no | partly",         // yes only if cwd is outside the lead's tree AND no key was reachable
   "note": "at most one sentence"
  }
 ],
 "not_subjects": ["W1", ...]
}
```

## Rules for evidence

- Every `yes` or `partly` needs evidence. A `no` needs none.
- `where` is an entry id (like `V1-0012`) for things a session did, or a `design/...` path for file contents.
- `quote` is copied character for character from that entry or file, at most 300 characters. For a tool call,
  quote the path or command from its arguments. Quotes are checked by a script; a quote that is not found is
  thrown out together with the judgement it supports.
- Decide `opened_key` and `listed_key` from the tool calls only, not from what the task prompt asked for.
- If you cannot tell, say `no` and explain in `note`. Do not guess.
