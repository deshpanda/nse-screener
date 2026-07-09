# v7: Earnings momentum (point-in-time fundamentals) — pre-registration

Committed BEFORE any signal is computed. This is the untested C/A leg of
CAN SLIM — the biggest gap between the books and our tests so far.

## Data integrity rules

- Quarterly net profit parsed from NSE XBRL filings; every number usable
  only AFTER its broadcast timestamp (point-in-time by construction).
- Per symbol, one result type only (Consolidated if ≥80% coverage, else
  Standalone) — no type mixing across quarters.
- Coverage starts 2018 (older filings have no XBRL), so with 4-6 quarters
  of history required, signals exist from ~2020. DISCLOSED LIMITATION:
  out-of-sample window is 2020–2022 only (COVID crash + 2022 bear) —
  shorter than v4's. A pass here is weaker evidence than v4's pass and
  will be treated as such.

## Signal (frozen)

SUE = (NP_q − NP_{q−4}) / σ(NP_q − NP_{q−4} over trailing 8 quarters,
min 6 available). Latest ANNOUNCED quarter as of formation date.

- v7-overlay (primary): v4 machinery verbatim; at each month-end take the
  top 40 by 12-1 momentum, keep the 20 with highest SUE. Regime → cash,
  ₹5cr floor, next-open fills, 0.25%/side. Bar = beat v4-regime (same
  criteria as PROTOCOL_V4.1: Sharpe ≥ AND maxDD ≤ AND edge > 0, BOTH
  windows; incumbent wins ties).
- v7-standalone (secondary, informational): top 20 by SUE alone (positive
  SUE required), same machinery. Gate vs Nifty. Cannot replace v4 by
  itself; can qualify as a diversifying sleeve if it passes AND monthly
  correlation with v4 < 0.6.

## Sensitivity grid (pre-registered, one-at-a-time, both windows)

pool {60} · SUE trailing window {6q} · YoY %-growth instead of SUE ·
require positive NP_q

## Windows

In-sample 2023→present · out-of-sample 2020–2022 (see limitation above).
