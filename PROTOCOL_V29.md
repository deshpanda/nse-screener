# v29: the "Peter Lynch rules" GARP screen — India + US — pre-registration (2026-07-16)

## Provenance & honesty preamble

Source: a viral tweet claiming Lynch's "6 rules" ("turned $18M into
$14B"). Debunked framing, registered anyway: the $18M→$14B is Magellan
AUM growth (mostly inflows; his return ~29%/yr ≈ $18M→$500M), and Lynch
never published this checklist. Underneath is a standard GARP screen —
and the FIRST valuation-family test of this project (29 prior tests,
zero value screens). Both markets, per owner: India and US.

## Rules as tweeted, and the frozen deviations

| tweet rule | India | US |
|---|---|---|
| 1. trailing P/E < 25 | ✔ price ÷ trailing-4q EPS (PIT broadcast) | ✔ price ÷ trailing-4q EPS (PIT filed date) |
| 2. forward P/E < 15 | DROPPED — historical analyst estimates don't exist freely (disclosed) | same |
| 3. debt/equity < 35% | DROPPED — quarterly filings carry no balance sheet (future annual-XBRL project) | same |
| 4. EPS growth > 15% | ✔ TTM EPS vs prior-year TTM (both > 0) | ✔ same |
| 5. PEG < 2 | ✔ P/E ÷ (100 × TTM growth) | ✔ same |
| 6. mcap > $5B | PRIMARY: > ₹5,000cr (India translation of "no tiny caps", frozen now); SECONDARY cell: literal ≈ ₹42,000cr | satisfied by point-in-time S&P 500 membership (all ≥ $5B era-typical; disclosed simplification) |

Testing 4 of 6 rules; the two dropped are dropped IDENTICALLY in both
markets and disclosed on the site. No other deviations permitted later.

## Portfolio construction (frozen, both markets)

- Monthly formation at month-end from PIT-known fundamentals (latest
  broadcast/filed ≤ formation date), fills next open, 0.25%/side churn
  cost — the audited monthly engine.
- Universe: India = liquid (≥₹5cr, 20d median) non-ETF NSE stocks;
  US = point-in-time S&P 500 members (survivor-biased prices, long
  disclosed).
- Hold ALL qualifiers equal-weight; if > 40 qualify, the 40 with
  lowest PEG; if none qualify, cash that month.
- Cells per market: PRIMARY no-regime (the screen as pitched);
  SECONDARY with the v4-style 200-DMA circuit breaker (disclosed
  add-on, reported separately, never blended post-hoc). India adds the
  literal-mcap secondary. That is the ENTIRE grid: 3 India cells,
  2 US cells.

## Data

- India: fr_xbrl parsed EPS (99.1% coverage, banking tags fixed
  2026-07-14), implied shares × raw close for the mcap floor.
- US: SEC Financial Statement Data Sets (quarterly ZIPs, 2009q2→),
  tags EarningsPerShareBasic/Diluted, filed date = availability;
  ingester ingest/sec_fundamentals.py (restartable; committed before
  any US result). CIK→ticker via us/data/company_tickers.json.

## Windows (frozen)

- India: IS 2023-01→2027-01 (decision); OOS 2019-07→2022-12 single
  shot (EPS history begins 2018 — TTM needs the first year to build).
- US: IS 2023-01→2027-01; OOS 2010-01→2022-12 single shot.
- Benchmarks: NIFTYBEES / SPY buy-and-hold.

## Pass criteria (frozen — the standard gate)

A market passes only if the PRIMARY cell beats its benchmark after
costs in BOTH windows. Secondary cells are diagnostics, never rescues.
An India pass then faces the incumbent rule vs v4 (all criteria, both
windows) + the v27.2-style concentration check. Nothing goes live in
2026 (PROTOCOL_GOLIVE).

## Registered predictions

Both markets FAIL the index gate. US: GARP is among the most
commoditized screens on earth and large-cap value lagged SPY for most
of the sample. India: the screen tilts large-cap quality-value, which
underperformed the 2023-26 midcap regime; OOS is the more interesting
window. Wrong-prediction risk accepted and printed, as always.

## Amendments

None after this commit. Failed cells stay dead.
