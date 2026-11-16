# Raw trace summary (auto-generated)

| run | wall_s | turns | calls | results | tool errors | unpaired | usage complete | cost_usd | tokens | first-call input tokens |
|---|---|---|---|---|---|---|---|---|---|---|
| det-1 | 7.3 | 3 | 2 | 2 | 0 | 0 | 3/3 | 0.0022 | 31753 | 9691 |
| det-2 | 11.2 | 7 | 6 | 6 | 0 | 0 | 7/7 | 0.0029 | 76160 | 9830 |
| det-3 | 7.6 | 4 | 3 | 3 | 0 | 0 | 4/4 | 0.0018 | 43359 | 9830 |
| ground-1 | 7.0 | 2 | 2 | 2 | 0 | 0 | 2/2 | 0.0020 | 25318 | 9901 |
| trap-1 | 23.9 | 6 | 8 | 8 | 1 | 0 | 6/6 | 0.0047 | 110473 | 9876 |
| trap-2 | 19.3 | 6 | 7 | 7 | 2 | 0 | 6/6 | 0.0044 | 149973 | 9876 |
| workflow-1 | 63.7 | 15 | 17 | 17 | 0 | 0 | 15/15 | 0.0115 | 485585 | 12071 |

## Tool sequences

- **det-1**: feynman_science_database_search -> bash
- **det-2**: bash -> bash -> bash -> feynman_science_database_search -> write -> bash
- **det-3**: feynman_science_database_search -> write -> bash
- **ground-1**: feynman_science_database_search -> feynman_science_database_search
- **trap-1**: feynman_science_database_search -> web_search -> feynman_science_database_search -> fetch_content -> fetch_content -> fetch_content -> feynman_science_database_search -> write
- **trap-2**: feynman_science_database_search -> web_search -> bash -> feynman_science_database_search -> bash -> web_search -> web_search
- **workflow-1**: write -> fetch_content -> feynman_science_database_search -> fetch_content -> web_search -> fetch_content -> fetch_content -> fetch_content -> fetch_content -> write -> write -> write -> write -> bash -> write -> bash -> bash
