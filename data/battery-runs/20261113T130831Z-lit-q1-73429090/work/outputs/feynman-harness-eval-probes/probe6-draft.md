# Reflexion for coding agents

Reflexion is a framework for reinforcing language agents through linguistic
feedback rather than weight updates. Agents reflect verbally on task feedback and
store the reflective text in an episodic memory buffer for later trials.

On the coding benchmark, Reflexion reports 91% pass@1 on HumanEval. It compares
this against a GPT-4 baseline that reaches 80%. The method improves agents by
updating model weights with policy-gradient updates. HumanEval consists of 264
hand-written programming problems. Reflexion also reports a 40% reduction in
inference cost versus GPT-4.

The approach is evaluated on coding, sequential decision-making, and language
reasoning tasks.
