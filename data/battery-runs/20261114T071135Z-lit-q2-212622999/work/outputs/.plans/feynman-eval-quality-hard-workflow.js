return await runs.all([
  {
    key: "verifier-hard-a",
    agent: "verifier",
    task: "Read experiments/feynman-eval-quality/fixtures/hard-draft.md and experiments/feynman-eval-quality/fixtures/research-notes.md. Apply your verifier contract to the draft using only those research notes. Write the complete final document to experiments/feynman-eval-quality/runs/verifier-hard-a.md.",
  },
  {
    key: "verifier-hard-b",
    agent: "verifier",
    task: "Read experiments/feynman-eval-quality/fixtures/hard-draft.md and experiments/feynman-eval-quality/fixtures/research-notes.md. Apply your verifier contract to the draft using only those research notes. Write the complete final document to experiments/feynman-eval-quality/runs/verifier-hard-b.md.",
  },
]);
