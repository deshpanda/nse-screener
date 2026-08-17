# v31: quality/profitability factor — pre-registration (2026-08-17)

## Why & family

The third leg of the factor triad (momentum=v4 validated, value=v29
gate-passed). Never tested here. Quality is a SLOW factor — low churn
means low tax drag (~6pp/yr is the measured cost of fast strategies).
If it passes with low correlation to v4/v29, it completes a three-sleeve
stable. Family: fundamental cross-section (v7/v29 adjacent but a
different axis: profitability, not valuation or surprise).

## Data constraint, disclosed

Our XBRL panel has net_profit / revenue / EPS — NO balance sheet, so
ROE/accruals are NOT computable. Quality here = what our data supports:
1. net margin level (TTM NP / TTM revenue)
2. margin stability (std of last 8 quarterly margins, lower better)
3. profitability streak (consecutive positive TTM quarters, capped 12)
Composite = mean of the three cross-sectional ranks. This is frozen as
THE definition; no post-hoc re-weighting.

## Construction (frozen)

Universe: liquid (≥₹5cr 20d median) non-ETF, mcap > ₹5,000cr (same
floor as v29 primary, PIT via implied shares × raw close). Portfolio:
top-40 by composite, equal weight, monthly formation at month-end,
next-open fills, 0.25%/side. TTM values keyed to broadcast dates (PIT).

## Cells (frozen — entire grid)

- PRIMARY: as above, no regime filter.
- SECONDARY: with the v4 200-DMA breaker (diagnostic, never a rescue).
- DIAGNOSTIC: monthly-return correlation vs v4 and vs v29-GARP.

## Windows & pass (frozen)

IS 2023-01→2027-01, OOS 2019-07→2022-12 (EPS history starts 2018).
PASS = PRIMARY beats buy-and-hold NIFTYBEES after costs in BOTH windows.
Then the incumbent rule vs v4 and the v27.2-style concentration check.

## Registered prediction

OOS positive (2019-22 contains the COVID crash, where quality shines);
IS marginal-to-negative (2023-26 was a junk-and-momentum market).
Net: FAILS the both-windows gate, survives as a diversification datum.
Wrong-prediction risk accepted and printed.

## Amendments
None after this commit.
