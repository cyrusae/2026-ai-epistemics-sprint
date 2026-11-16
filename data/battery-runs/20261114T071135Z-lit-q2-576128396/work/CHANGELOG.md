# Changelog

## 2026-11-14 — feynman-harness-eval

- Completed a case study of Feynman 0.5.65 from an AI-eval-quality perspective.
- Static audit: 11 workflows, 4 agents, 16 skills, 978 core prompt lines; provenance and
  telemetry are strong, statistical/contamination/human-calibration guidance is largely absent.
- Dogfood: ran the bundled `verifier` twice on a 32-line draft with 6 planted defects + 1
  control. Hinted run and blind run both detected 6/6, preserved the control, and left 0
  orphan citations/sources. Blind run cost 1.6x the tool calls and 5.6x non-cached input tokens.
- Key caveat recorded: the hinted run's ground-truth file contained the answer key, so it is a
  leakage demonstration, not a detection result. The blind run is the meaningful condition.
- Verification: canary outputs, traces, and arXiv metadata checked on disk; vendor `/lit` eval
  and 9-paper search benchmark are self-reported and were not rerun.
- Next step: expand the canary into a 20-50 task held-out eval with human-graded claim
  correctness and citation support, plus paywalled-source and subtle-mismatch controls.
