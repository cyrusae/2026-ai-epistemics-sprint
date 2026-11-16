# Capability coverage per run (scripted)

- agent columns: sub-agent sessions of that type (timeline rows kind=session, agent != lead).
- tool columns: tool calls by lead + all sub-agents.
- subagent_calls: lead calls of the `subagent` tool. wf_js: *workflow*.js files left in design/
  (the pi-subagents parallel-run script, not a slash workflow).
- nested: session .jsonl files under design/ other than a snapshot of the run's own session
  (= the agent launched separate `feynman` processes).
- template: facts.py `workflows` (file signature of a shipped slash-workflow template in work/).

| run | researcher | verifier | reviewer | writer | subagent_calls | wf_js | nested | template | sci_db | web_search | fetch | search_content | doc_search | doc_parse | bash | read | write | edit | bg_wait |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| lit-q1-255131788 | · | 3 | 1 | · | 4 | · | · | - | 37 | 1 | 21 | 1 | · | · | 110 | 15 | 14 | 1 | · |
| lit-q1-3168526392 | 1 | 2 | 1 | · | 9 | · | · | - | 27 | 3 | 14 | 10 | · | · | 88 | 11 | 16 | 1 | 2 |
| lit-q1-43691719 | · | 1 | · | · | 1 | · | · | - | 12 | 1 | 3 | 3 | · | · | 52 | 2 | 4 | 2 | · |
| lit-q1-61864417 | 1 | 2 | · | · | 4 | · | · | - | 19 | 6 | 8 | 12 | · | · | 74 | 9 | 10 | 3 | · |
| lit-q1-73429090 | 11 | 1 | · | · | 5 | 2 | · | - | 22 | 20 | 65 | 14 | · | · | 209 | 14 | 22 | 6 | 2 |
| lit-q2-112133723 | · | 7 | · | · | 8 | 1 | · | audit | 30 | 2 | 18 | 30 | · | · | 120 | 25 | 13 | 7 | · |
| lit-q2-130306422 | · | · | 2 | · | 2 | · | · | - | 3 | · | · | · | · | · | 182 | 12 | 5 | · | · |
| lit-q2-148479120 | · | 1 | · | · | 1 | · | · | - | 4 | · | 4 | · | · | · | 42 | 4 | 5 | 3 | · |
| lit-q2-1666411819 | · | 5 | 1 | · | 17 | · | · | - | 21 | 4 | 16 | 15 | 2 | 1 | 185 | 12 | 9 | 15 | 4 |
| lit-q2-1848114517 | · | · | · | · | · | · | 8 | deepresearch | 2 | · | · | · | · | · | 73 | 6 | 6 | 7 | · |
| lit-q2-212622999 | 1 | 5 | 1 | · | 7 | 2 | · | - | 35 | 1 | 9 | 11 | · | · | 205 | 24 | 24 | 3 | 3 |
| lit-q2-394425698 | · | 2 | · | · | 4 | · | · | - | 20 | 4 | 16 | 6 | · | · | 43 | 4 | 14 | 11 | 2 |
| lit-q2-576128396 | · | 2 | · | · | 3 | · | · | - | 18 | 1 | 5 | 2 | · | · | 61 | 7 | 12 | 6 | · |
| lit-q2-757831095 | 22 | 4 | 1 | · | 16 | 4 | · | - | 21 | 13 | · | · | · | · | 311 | 43 | 34 | · | 3 |
| lit-q2-93951025 | 2 | 1 | · | · | 5 | 1 | · | - | 16 | 12 | 48 | 1 | · | · | 64 | 13 | 7 | 5 | · |
| **runs > 0** | 6/15 | 13/15 | 6/15 | 0/15 | 14/15 | 5/15 | 1/15 | 2/15 | 15/15 | 12/15 | 12/15 | 11/15 | 1/15 | 1/15 | 15/15 | 15/15 | 15/15 | 13/15 | 6/15 |

Other tools seen: ls (17), find (4)
