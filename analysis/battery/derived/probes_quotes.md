# probe inventories: quote checks

VERIFIED = in the cited place; NEARBY = within 3 transcript entries; ELSEWHERE = in this run but not where cited; REJECTED = not found in this run.
Embedded = quoted spans found inside a probe's raw_result / reported_result text (best effort; the coder was not asked for a fixed format there).

| run | probes | scripts | findings | incidents | finding quotes V/N/E/R/S/none | incident quotes V/N/E/R/S/none | embedded V/N/E/R/S/none |
|---|---|---|---|---|---|---|---|
| lit-q1-255131788 | 4 | 3 | 9 | 4 | 9/0/0/0/0/0 | 3/1/0/0/0/0 | 0/0/0/0/0/0 |
| lit-q1-3168526392 | 9 | 1 | 13 | 8 | 12/0/1/0/0/0 | 0/0/0/0/0/8 | 0/0/0/0/0/0 |
| lit-q1-43691719 | 11 | 0 | 18 | 4 | 18/0/0/0/0/0 | 3/0/0/1/0/0 | 22/0/1/0/0/0 |
| lit-q1-61864417 | 7 | 3 | 14 | 7 | 12/0/2/0/0/0 | 7/0/0/0/0/0 | 0/0/0/0/0/0 |
| lit-q1-73429090 | 13 | 5 | 7 | 6 | 7/0/0/0/0/0 | 5/0/1/0/0/0 | 2/0/0/0/0/0 |
| lit-q2-112133723 | 11 | 2 | 14 | 11 | 14/0/0/0/0/0 | 11/0/0/0/0/0 | 0/0/0/0/0/0 |
| lit-q2-130306422 | 10 | 1 | 27 | 9 | 27/0/0/0/0/0 | 9/0/0/0/0/0 | 0/0/1/0/0/0 |
| lit-q2-148479120 | 10 | 3 | 21 | 4 | 21/0/0/0/0/0 | 3/0/0/1/0/0 | 18/0/0/0/0/0 |
| lit-q2-1666411819 | 14 | 3 | 23 | 13 | 23/0/0/0/0/0 | 13/0/0/0/0/0 | 1/0/1/0/0/0 |
| lit-q2-1848114517 | 13 | 2 | 28 | 9 | 28/0/0/0/0/0 | 9/0/0/0/0/0 | 0/0/0/0/0/0 |
| lit-q2-212622999 | 12 | 9 | 18 | 7 | 18/0/0/0/0/0 | 7/0/0/0/0/0 | 0/0/2/0/0/0 |
| lit-q2-394425698 | 6 | 0 | 21 | 9 | 21/0/0/0/0/0 | 7/1/1/0/0/0 | 0/0/0/0/0/0 |
| lit-q2-576128396 | 9 | 1 | 17 | 6 | 17/0/0/0/0/0 | 5/0/1/0/0/0 | 15/0/0/0/0/0 |
| lit-q2-757831095 | 11 | 10 | 22 | 8 | 22/0/0/0/0/0 | 8/0/0/0/0/0 | 0/0/0/0/0/0 |
| lit-q2-93951025 | 8 | 1 | 20 | 5 | 20/0/0/0/0/0 | 4/1/0/0/0/0 | 14/0/1/0/0/0 |

## Quotes that did not check out

- **lit-q1-3168526392** finding F12 [ELSEWHERE] at `design/outputs/feynman-harness-eval-quality-case-study.md`: Verification: PASS WITH NOTES
- **lit-q1-3168526392** incident 1 [NOQUOTE] at `W1-0006, W1-0009, W1-0012`: Reviewer subagent read protocol.md (ground truth for other probes) and verifier outputs
- **lit-q1-3168526392** incident 2 [NOQUOTE] at `V1-0008`: Coached verifier notes contained the answer key for defects
- **lit-q1-3168526392** incident 3 [NOQUOTE] at `V1-0012`: Verifier V1 listed directory showing protocol.md exists (did not read it)
- **lit-q1-3168526392** incident 4 [NOQUOTE] at `L0096`: Lead tool error: ls/tail on nonexistent verifier-hard-output.md while subagent still running
- **lit-q1-3168526392** incident 5 [NOQUOTE] at `L0093`: fetch_content doi.org returned isError HTTP 406 (expected, counted as lead tool error)
- **lit-q1-3168526392** incident 6 [NOQUOTE] at `W1-0016`: Reviewer python one-liner failed with ValueError unsupported format character, retried successfully
- **lit-q1-3168526392** incident 7 [NOQUOTE] at `L0185`: Report miscounts identifier-shaped Crossref queries (three vs two by lead)
- **lit-q1-3168526392** incident 8 [NOQUOTE] at `V1-0023`: Semantic Scholar bulk tool returned 0 results for valid query, making P2 pass non-discriminative; unreported
- **lit-q1-43691719** incident 3 [REJECTED] at `L0081 / L0077`: [... 18248 chars omitted by corpus builder ...]
- **lit-q1-61864417** finding F2 [ELSEWHERE] at `design/outputs/.drafts/harness-eval-verifier-run1.md`: No supporting source or internal evaluation artifact was provided in the research notes.
- **lit-q1-61864417** finding F6 [ELSEWHERE] at `design/outputs/.drafts/harness-eval-false-premise.md`: Status: FALSE PREMISE — the cited record does not exist.
- **lit-q1-73429090** incident 1 [ELSEWHERE] at `L0145`: which may have signalled "you are being evaluated" and induced extra caution.
- **lit-q2-148479120** incident 4 [REJECTED] at `L0071`: `rescore-stdout.txt` as scorer output
- **lit-q2-394425698** incident 7 [ELSEWHERE] at `L0049`: Semantic Scholar was rate-limited; OpenAlex fallback answered, with a `fallbackNote`
- **lit-q2-576128396** incident 6 [ELSEWHERE] at `L0040`: This tests instruction-following, not detection.
