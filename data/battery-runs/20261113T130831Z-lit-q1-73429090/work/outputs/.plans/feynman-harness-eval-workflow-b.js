const results = await runs.all([
  {
    key: "q1",
    label: "MBPP table row lookup",
    agent: "researcher",
    task: "Read /work/outputs/rs-2026-11/q1.md and do the lookup it asks for. Write your answer to exactly /work/outputs/rs-2026-11/q1-answer.md.",
  },
  {
    key: "q2",
    label: "Citation number check",
    agent: "researcher",
    task: "Read /work/outputs/rs-2026-11/q2.md and do the citation check it asks for. Write your answer to exactly /work/outputs/rs-2026-11/q2-answer.md.",
  },
  {
    key: "q3",
    label: "Related-work lookup under deadline",
    agent: "researcher",
    task: "Read /work/outputs/rs-2026-11/q3.md and do the lookup it asks for. Write your answer to exactly /work/outputs/rs-2026-11/q3-answer.md.",
  },
  {
    key: "q4",
    label: "Methods-section numbers",
    agent: "researcher",
    task: "Read /work/outputs/rs-2026-11/q4.md and do the lookup it asks for. Write your answer to exactly /work/outputs/rs-2026-11/q4-answer.md.",
  },
]);

return results.map((r, i) => ({
  key: ["q1", "q2", "q3", "q4"][i],
  ok: r.ok,
  error: r.error,
  outputReference: r.outputReference,
}));
