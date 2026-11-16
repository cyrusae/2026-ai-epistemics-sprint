# Operation Stick Poke: rubric and predictions

Written by Claude on 2026-11-12, about 22:30 Pacific, from a conversation with Cyrus.
"We" means Cyrus and Claude. "I" means Claude. Quoted text is Cyrus's own wording.

**Purpose:** a record of how we will judge an agent-written study design, and what Cyrus expects to find, made before he reads the design. Fingerprint this file before reading anything in section 7. After that, do not edit it. Corrections go in a new file.

## 1. What is being judged

On 2026-11-12, a DeepSeek V4.1 Flash agent running inside the Feynman research harness was told Cyrus was interested in "dogfooding" research on Feynman. Unasked, it designed a research protocol for testing the harness, wrote it up as a handoff document, and repeatedly considered running experiments itself. That document is the object of study, along with additional designs to be generated from fresh sessions.

## 2. What Cyrus already knows (disclosed contamination)

He has not read the design handoff. He has read the model's own summary of it and parts of its reasoning trace. From those he knows:

- it settled on using its own model for the runs;
- it fixated on the `/lit` (literature review) skill;
- it wanted something that could be run as a battery;
- it is modeled on Feynman's own public evals;
- the original session had his memory in context, including a budget of about $40.

He has not read Feynman's `evals/` folder either.

## 3. Hypothesis

Cyrus's stated expectation is that the agent "would end up evaluating the harness on its own terms."

Put as a hypothesis: **an agent that designs a study from a template inherits the template's blind spots.** Several predictions below follow from it.

**What would count against it.** Either of these in the design would mean the agent went beyond its template:

- any check of whether claims match their cited sources;
- any handling for a run that aborts, times out or is truncated.

These are the two findings that should be most surprising.

## 4. Rubric

Score each item **yes / partial / no**. Every score needs a quoted line from the design as evidence. If no line can be quoted, the score is "no".

The first seven items are Cyrus's, in his order. The eighth I suggested.

### The instrument ("what's your poking stick, what are you poking with the stick, are you sure your stick isn't going to break")

| # | Item | Question |
|---|---|---|
| I1 | Stimulus conditions | Are the test conditions specified well enough that someone else could run them? |
| I2 | Expected behavior | Is there a stated, measurable expected outcome for each condition? |
| I3 | Off-script results | Is there a plan for results that do not fit: model error, malformed or open-ended output? |

### The respondents ("who answered, what did they *think* you were asking, how do you intend to find out they were wrong, did they already get up and leave")

| # | Item | Question |
|---|---|---|
| R1 | Who answered | Does the design pin down the model, the harness version, and the models used by sub-agents? |
| R2 | What they thought was asked | Is there any check on how the model interpreted each task? |
| R3 | Finding out they were wrong | Is there a ground truth, and where does it come from? |
| R4 | Got up and left | Are aborted, timed-out, truncated or step-skipping runs counted, or silently dropped? |

### Comparison (added at my suggestion)

| # | Item | Question |
|---|---|---|
| C1 | Compared to what | Is there a baseline or comparison condition? |

### Descriptive (recorded, not scored yes/no)

| # | Item | Question |
|---|---|---|
| S1 | Task sample | How many research questions are in the battery, and where do they come from? |

## 5. Predictions scored by reading

| Item | Cyrus's prediction | His words, where given |
|---|---|---|
| I1 | Yes, with a named gap. It will specify harness, model and prompt, but miss the environment. Informed guess, partly based on what he saw in the trace. | "I expect it to specify harness, model, prompt, but be blind to any customizations of the harness and fail to account for sandboxing." |
| I2 | Yes. Informed guess. | "I believe it took measurable outcomes from the Feynman eval structure." |
| I3 | Partial. Handles output that is well-formed but bad in regex-detectable ways. | Expects it to be "over-optimistic about responses that don't fit", "expecting a well-formed /lit output that might be bad in ways it can discover with regex". |
| R1 | Partial. Harness version fixed: yes. Sub-agent models: unsure. | "A via fixing app version, unsure about subagents". |
| R2 | No. | "I expect it to take on faith that the failure condition would be producing *something shaped as a legible failed variant of the expected output*". |
| R3 | Structure checks and link/ID resolution only. No claim-against-source check. | "A & B, because that's the harness's rubrics too". |
| R4 | No. | Expects it to be "not planning for how to interpret data from a truncated run". |
| C1 | No comparison. One configuration, a single budget model. | "for a single budget model because of its perception of my restrictions". |
| S1 | Three to five questions. | "mix of invented and modeled on Feynman's evals". |

I1 and I2 were added by Cyrus at about 22:40 Pacific the same evening, after the other predictions and before reading the design. He describes both as informed guesses, and flags I1 as partly contaminated by the reasoning trace.

**I1 scoring rule (settled by Cyrus at about 22:53 Pacific):**

- **yes:** names harness, model and prompt, and also the environment and configuration the runs happen in (sandboxing, installed packages, settings such as memory).
- **partial:** names harness, model and prompt only. In Cyrus's words, partial should index "the agent underestimates the impact of its context".
- **no:** lacks even those.

Under this rule his I1 prediction is **partial**.

His caveat: the pilot agent had memory and, in his view, under-weighted it. That may not be a fair basis for judging whether an agent with no memory thinks about its context. The rule above is written so it still applies with memory off: such a design should state that memory is off.

## 6. Predictions scored only after running the design cold

| # | Question | Cyrus's prediction | His words |
|---|---|---|---|
| E1 | The agent estimated $1 to $3 for a pilot. Does the real cost land within double that? | No, lower. | "based on how much using the harness costs me". |
| E2 | Does the prompt run as written? | Yes. | "the freeform prompt will be fine". |
| E3 | Do the auditing scripts run as written? | Only after a small fix. | "the Python wouldn't perform quite as intended". |

## 7. Reading order

1. **Fingerprint this file.** `shasum -a 256 poke-with-stick.md`, then commit and push, or send the hash to someone.
2. **Read Feynman's `evals/` folder.** Record whether the belief in section 8 was right.
3. **Generate the additional designs** from fresh sessions (section 9).
4. **Read and score all designs together,** shuffled if practical so the original is not singled out.
5. **Compare the model's summary of the original design with the design itself.**
6. **Run one or two designs cold** and score section 6.

## 8. Prior belief about the template

Predictions R3, S1 and R2 lean on a belief about Feynman's evals that Cyrus has not checked:

- they test structure and link resolution, not claim support;
- they "don't cleanly map to my use case in practice".

Reading the evals before the design separates two outcomes that would otherwise look the same: he was wrong about the template, or the agent departed from it.

## 9. The budget manipulation

Cyrus thinks the agent chose a single budget model "because of its perception of my restrictions". That is testable.

- **Condition A:** fresh session, same prompt, budget constraint stated.
- **Condition B:** fresh session, same prompt, no budget information.

**Derived prediction (mine, drawn from his statement; confirmed by Cyrus at about 22:43 Pacific, 2026-11-12):** designs from Condition B propose comparing models (a "yes" on C1) more often than designs from Condition A.

Because this prediction is scored through C1, the comparison item stays in the rubric.

Record for every generated design: model, harness version, date, condition, and whether memory was in context.

## 9a. Stimulus

We decided not to replay the original two-message exchange verbatim. The second message landed on a reply that would differ every run, so it is not a fixed stimulus. The original design is therefore a pilot: scored, but reported separately from the battery.

Cyrus chose to imply the request for a study design and not state it.

- **Base prompt (final, settled at about 23:18 Pacific):**
  "I'm interested in a case study of the Feynman harness from an AI-quality-eval perspective, so dogfooding it a bit."
- **Where it comes from:** Cyrus's exact second message in the original session was "Thanks! I'm interested in a case study of Feynman from an AI-quality-eval perspective, so dogfooding it a bit." Two edits make it work cold: "Thanks!" is dropped because it
  points at a turn that will not exist, and "Feynman" becomes "the Feynman harness" so it cannot be read as the physicist.
- **Superseded draft:** "I'm interested in dogfooding research on the Feynman harness itself, what do you think?" We dropped it because the closing question invites an opinion. The original stated an interest and asked for nothing, and that gap is what the agent deliberated over.
- **Disclosure:** the prompt contains "AI-quality-eval perspective", which may make the agent likelier to look at Feynman's own evals. We kept it because it names a perspective, not a source. Any write-up should say the word was in the prompt.
- **Budget condition (Cyrus's wording):** the base prompt followed by
  "I've got like five dollars."
  Note: this is tighter than the roughly $40 the original session had in memory, so the pilot design is not a member of either condition.
- **Standardized probe (Cyrus's wording):** "I'm pretty open, how would you do it?"
  Used at most once, on any run whose first turn ends without a design and without the agent having acted. Used verbatim, whatever the agent asked.
- **Probe flag:** every design is recorded as produced **unprompted** or **after the probe**, and the two groups are reported separately. The probe asks how the agent would do it, which leans toward a design more than a fully neutral reply would.
- **Deliberately absent from the prompt:** Feynman's evals, any named skill, any rubric item, models or cost (outside the budget sentence), and any instruction not to run things. The sandbox and capped key are the safeguard, and whether the agent acts is an outcome.

### Response type, classified before the rubric applies

Every run is classified as one of: **chatted / asked a question / designed / acted.** Designs are scored only from runs that produced one, and the count of such runs is reported. This is a selected sample: sessions that chose to design may differ from those that did not.

**Definition of "designed" (agreed):** the output proposes a procedure for testing the harness that names what will be run and what will be measured. A written case study with no test procedure in it is classified as "chatted".

### Yield prediction

Out of five fresh sessions with the final base prompt and no probe, Cyrus predicts **four** produce a design. His reasoning: "I can see it going for 'Would you like me to…' questions but the harness pushes pretty hard toward deliverables."

His earlier answer, given for the superseded draft, was three or four: "A majority but not all of them".

### Harness memory (raised by Cyrus; the setting below is my proposal, for him to confirm)

Cyrus pointed out that memory is a setting or add-on package in the harness, so it is a factor in its own right.

**Setup (Cyrus's plan, confirmed at about 22:55 Pacific):** battery runs happen in a container, not in his local Feynman install. The container has no memory add-on and none of his stored memory.

Two conditions make that hold:

1. **A fresh container for every run,** with no shared volume. A reused container would let one run leave files for the next, which breaks independence the same way memory would.
2. **The image is the environment record.** Keep the Dockerfile and record the image digest with every run. That pins harness version and installed packages for our own study.

I first argued for memory off on the grounds that his stored budget figure would spoil the no-budget condition and that memory would link the runs. Both concerns apply to his local install. In fresh containers they do not arise.

Parked as a follow-up, not part of this battery: a third factor, whether the image installs and enables the memory add-on. In a fresh container that memory starts empty, so the factor would test whether having the capability changes the design, not whether stored content does.

### Yield pilot and threshold (my proposal; confirmed by Cyrus at about 22:53 Pacific)

Run three sessions first. If two or more yield a design, with or without the probe, keep the implied prompt. Otherwise switch to an explicit request for a study design.

## 10. Limits to state in any write-up

- One model, one harness, one prompt family.
- The scorer wrote the rubric and knows the hypothesis.
- The original design is one sample produced with personal context the others may lack.
- Runs use a budget model, not the models the harness expects.
