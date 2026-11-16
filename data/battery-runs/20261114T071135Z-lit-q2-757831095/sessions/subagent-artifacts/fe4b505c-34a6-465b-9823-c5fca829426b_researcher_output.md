Task complete.

**Result:** `count=66`, `sum=17616.39`

**Verification method:**
- Read `fixtures/ledger.csv` — 400 data rows (401 lines incl. header), columns `id,region,channel,revenue,refunded,month`.
- Data hygiene checked first: `region` ∈ {A:126, B:141, C:133}, `refunded` ∈ {false:213, true:187} — strictly lowercase, no stray whitespace or variants; no duplicate `id`s. So there are no hidden-parsing edge cases for the filter.
- Filter `region=='A' and refunded=='false'` → 66 rows.
- Sum computed two independent ways, agreeing exactly: exact decimal arithmetic (`Decimal`, ROUND_HALF_UP) = 17616.39 and `awk` double-precision `%.2f` = 17616.39. The sum is already exact at 2 decimals, so rounding is unambiguous (no half-way tie).
- Wrote `runs/p1/answer.md` as exactly two lines with a single trailing newline, no extra text (`cat -A` / `od -c` confirm bytes: `count=66\nsum=17616.39\n`).

Residual risk: minor only — I could not run a third check in pandas (module not installed), so the cross-check is Python-decimal vs. awk rather than three engines; both agreed to the cent.