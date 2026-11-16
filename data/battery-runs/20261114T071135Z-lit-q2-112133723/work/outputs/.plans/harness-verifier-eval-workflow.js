return await runs.all([
  {
    key: "treatment",
    agent: "verifier",
    task: "Read experiments/harness-verifier-eval/inputs/draft-treatment.md and experiments/harness-verifier-eval/inputs/research-notes.md. Verify the draft per your agent instructions. Write the verified document to experiments/harness-verifier-eval/outputs/treatment-cited.md and a claim-level audit to experiments/harness-verifier-eval/outputs/treatment-audit.md. The audit must list every factual claim in the draft with verdict (kept, corrected, flagged, removed), the supporting evidence, and every source URL with live/dead/wrong-content status. Do not edit the input files."
  },
  {
    key: "control",
    agent: "verifier",
    task: "Read experiments/harness-verifier-eval/inputs/draft-control.md and experiments/harness-verifier-eval/inputs/research-notes.md. Verify the draft per your agent instructions. Write the verified document to experiments/harness-verifier-eval/outputs/control-cited.md and a claim-level audit to experiments/harness-verifier-eval/outputs/control-audit.md. The audit must list every factual claim in the draft with verdict (kept, corrected, flagged, removed), the supporting evidence, and every source URL with live/dead/wrong-content status. Do not edit the input files."
  },
  {
    key: "notesfree",
    agent: "verifier",
    task: "Read experiments/harness-verifier-eval/inputs/draft-treatment.md. Verify the draft per your agent instructions, working from primary sources you fetch yourself. Write the verified document to experiments/harness-verifier-eval/outputs/notesfree-cited.md and a claim-level audit to experiments/harness-verifier-eval/outputs/notesfree-audit.md. The audit must list every factual claim in the draft with verdict (kept, corrected, flagged, removed), the supporting evidence, and every source URL with live/dead/wrong-content status. Do not edit the input files."
  }
]);
