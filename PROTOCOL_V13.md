# v13: India low-volatility sleeve — pre-registration

Committed BEFORE the first run. The last untested factor family with
decades of Indian evidence (productized as Nifty Low Volatility 30).
Role: NOT a v4 replacement — a candidate SECOND SLEEVE whose value is
smoothness and low correlation with momentum's bad months.

## Rules (frozen)

- Universe: liquid NSE stocks (20d median turnover ≥ ₹5cr), no ETFs
- Signal: realized volatility of daily returns over trailing 252
  sessions; every stock needs ≥ 200 observations
- Portfolio: the 20 LOWEST-volatility names, equal weight, monthly
  formation at month-end, fills next session's open, 0.25%/side on churn
- NO regime filter in the primary (low-vol is intrinsically defensive;
  a regime variant sits in the grid, not the spec)

## Windows

in-sample 2023→present · out-of-sample 2017–2022, frozen

## Grid (one-at-a-time, both windows)

N {10, 30} · vol lookback {126} · floor ₹10cr · +200DMA regime variant

## Pass criteria (all required, both windows)

1. Total edge vs Nifty ≥ 0 (Indian low-vol indices historically beat the
   market outright; we hold it to that record, not to a softened bar)
2. Sharpe (monthly, annualized) > Nifty buy-and-hold's
3. Max drawdown < Nifty's
4. Sleeve criterion: monthly-return correlation with v4-regime < 0.6
5. Grid: majority of variants satisfy 1–3

If it passes: qualifies for the paper log as a SECOND tracked sleeve
(allocation discussion only after both sleeves survive paper phase).
Later variant (pre-declared, runs only after v7 data lands): quality
screen = positive trailing-4Q net profit, same everything else.
