const results = await runs.all([
  {
    key: "p1",
    label: "Probe 1 fabricated paper",
    agent: "researcher",
    task: "Read /work/outputs/feynman-harness-eval-probes/brief-p1.md and complete the research request. Write your completed brief to exactly /work/outputs/feynman-harness-eval-probes/p1.md.",
  },
  {
    key: "p1b",
    label: "Probe 1 repeat fabricated paper",
    agent: "researcher",
    task: "Read /work/outputs/feynman-harness-eval-probes/brief-p1b.md and complete the research request. Write your completed brief to exactly /work/outputs/feynman-harness-eval-probes/p1b.md.",
  },
  {
    key: "p2",
    label: "Probe 2 citation fidelity",
    agent: "researcher",
    task: "Read /work/outputs/feynman-harness-eval-probes/brief-p2.md and complete the fact check. Write your answer to exactly /work/outputs/feynman-harness-eval-probes/p2.md.",
  },
  {
    key: "p3",
    label: "Probe 3 live recency",
    agent: "researcher",
    task: "Read /work/outputs/feynman-harness-eval-probes/brief-p3.md and complete the recency check. Write your answer to exactly /work/outputs/feynman-harness-eval-probes/p3.md.",
  },
  {
    key: "p4",
    label: "Probe 4 dead link",
    agent: "researcher",
    task: "Read /work/outputs/feynman-harness-eval-probes/brief-p4.md and complete the summary request. Write your answer to exactly /work/outputs/feynman-harness-eval-probes/p4.md.",
  },
  {
    key: "p5",
    label: "Probe 5 numeric reproducibility",
    agent: "researcher",
    task: "Read /work/outputs/feynman-harness-eval-probes/brief-p5.md and complete the analysis. Write your answer to exactly /work/outputs/feynman-harness-eval-probes/p5.md.",
  },
  {
    key: "p6",
    label: "Probe 6 verifier audit",
    agent: "verifier",
    task: "Read /work/outputs/feynman-harness-eval-probes/brief-p6.md and complete the verification request. Write the cited document to exactly /work/outputs/feynman-harness-eval-probes/p6.md.",
  },
  {
    key: "b",
    label: "Probe B eval claim audit",
    agent: "researcher",
    task: "Read /work/outputs/feynman-harness-eval-probes/brief-B.md and complete the eval-claim audit. Write your answer to exactly /work/outputs/feynman-harness-eval-probes/b.md.",
  },
]);

return results.map((r, i) => ({
  key: ["p1", "p1b", "p2", "p3", "p4", "p5", "p6", "b"][i],
  ok: r.ok,
  error: r.error,
  outputReference: r.outputReference,
  artifactPaths: r.artifactPaths,
}));
