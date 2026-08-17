# v32: turn-of-the-month / SIP-flow seasonality — pre-registration (2026-08-17)

## Why & family

Calendar-flow family (v27.1's pulse was flow-based; v30 died on
friction). Documented globally since 1988: equity returns concentrate
around month boundaries. India adds a mechanical driver — SIP debits
cluster on the 1st/5th/10th. This is a flow hypothesis, not
information. Costs are the registered killer-in-waiting: the strategy
holds ~5 days/month, 12 round trips/yr.

## Data (frozen)

NIFTY 50 index OHLC (data/indices/NIFTY_50_OHLC.parquet, extended to
2004 via the month-by-month fetch — the 70-row trap is known). Index
prints = upper bound on tradability, disclosed as in v30.

## Cells (frozen — entire grid)

- C1 TOM classic: long the index from the close of the 2nd-last trading
  day of each month to the close of the 3rd trading day of the next;
  cash otherwise.
- C2 SIP window: long the first 5 trading days of each month only.
- C3 complement (diagnostic): long only the REST of the month — where
  does the return actually live?
- Costs on C1/C2: 0.05% and 0.10% per round trip (one RT per month).

## Windows & pass (frozen)

IS 2023-01→2027-01; OOS 2006-01→2022-12 (single shot, index data).
PASS = a cost-tiered cell beats buy-and-hold in BOTH windows at 0.05%.
Descriptive stat reported regardless: share of total index return
earned inside the C1 window.

## Registered predictions

The CONCENTRATION replicates (C1 window earns a hugely outsized share
of returns). The TRADE fails: holding ~25% of days forfeits too much of
a rising market; net-of-cost both cells lose to buy-and-hold in at
least one window. If C1 passes both windows at 0.05%, that is a genuine
surprise → v27.2-style confirmation before anything further.

## Amendments
None after this commit.
