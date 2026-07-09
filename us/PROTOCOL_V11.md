# v11: US Senate trades — pre-registration (historical-only)

Committed BEFORE the first run. The original pitch that started this
project referenced congressional-trade tracking (Quiver). Testing it on
the only free dataset that survives: a community snapshot of Senate PTR
filings, 2012 → Dec 2020 (the project died; no fresher free source).

## Honest limitations (disclosed before results)

1. Data ENDS Dec 2020 — this can only test the historical claim, not
   whether following Congress works today. No in-sample/out-of-sample
   split is possible; sub-period consistency (2016-18 vs 2019-20) is
   reported instead.
2. No disclosure timestamps in the snapshot. STOCK Act allows ~45 days;
   entry is assumed at transaction_date + 45 calendar days (the
   conservative, realistic follower's entry).
3. Amounts are ranges; "size" means the range floor.

## Event definition (frozen)

- Senate PTR Purchase with clean ticker, amount floor ≥ $15,001
- event date: transaction_date + 45 calendar days
- one event per ticker per 63 sessions; S&P 500 member at event date
- entry next session's open; hold 63 sessions; excess vs SPY

## Grid: amount ≥$1,001 (all) · hold {21, 126}

## Read-out criteria

Mean AND median excess > 0 over the full window AND both sub-periods
non-negative AND no quarter > 25% of positive excess. Anything less =
the historical claim fails even before the modern-era question.
