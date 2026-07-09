# v13.1: v4 + low-vol combo sleeve — pre-registration (with disclosure)

## Disclosure first

The motivating result (70/30 v4/low-vol beats pure v4 on Sharpe in both
backtest windows: 1.27/1.06 vs 1.24/0.97; OOS maxDD -23.8% vs -33.5%)
was found in an EXPLORATORY analysis during the 2026-07-10 methodology
audit — after v13's standalone criteria had already failed. Both backtest
windows are therefore contaminated for this hypothesis. This protocol
exists to define the confirmation standard on data that cannot be
contaminated: the future.

## Spec (frozen)

- Sleeve A: v4-regime verbatim (incumbent, unchanged).
- Sleeve B: v13 low-vol verbatim (20 lowest 252d-realized-vol among
  liquid non-ETF stocks, monthly, no regime).
- Combo: 70% A / 30% B, rebalanced to weights monthly. No other change.

## Confirmation standard (paper phase, ≥3 month-end rebalances)

1. Both sleeves logged monthly in paper/log.csv from 2026-07 onward.
2. At go-live review: combo qualifies over pure v4 only if, during the
   paper window, (a) each sleeve's live behavior matches its simulation
   within slippage tolerance, AND (b) realized sleeve correlation stays
   < 0.6. No return threshold is set for the paper window — three months
   of returns is noise; the check is BEHAVIORAL, the sizing evidence
   remains the (disclosed, peeked) backtest.
3. Default allocation if confirmed: 70/30. If anything is anomalous,
   pure v4 stands (incumbent wins).
