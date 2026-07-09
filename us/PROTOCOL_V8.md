# v8: US large-cap momentum (the v4 recipe, ported) — pre-registration

Committed BEFORE the first run. Purpose: v4 (Indian monthly momentum +
regime) is our only survivor. If momentum is a real behavioral effect it
should not care about the country. Running the same recipe on US data is
a robustness test of v4's premise — and an evidence-based answer to
"should I trade US stocks?"

## Rules (v4 verbatim, US-flavored)

- Universe: point-in-time S&P 500 members on each formation date
  (fja05680 membership list; no survivorship in membership, but yfinance
  lacks delisted-ticker prices → 84% coverage, DISCLOSED: this flatters
  results somewhat; a pass here is supporting evidence, not primary)
- Signal: 12-1 momentum (252-session return skipping the latest 21)
- Portfolio: top 20 equal weight, monthly formation at month-end,
  fills at next session's open
- Regime: SPY < its 200-DMA at formation → 100% cash
- Costs: 0.10%/side base (zero-commission US retail + spread);
  0.25%/side stress variant
- Prices are yfinance auto-adjusted (splits + dividends in both legs;
  SPY benchmark likewise — consistent total-return comparison)

## Windows

- in-sample 2023 → present
- out-of-sample ~2017-07 → 2022-12 (price history starts 2016-06;
  momentum + regime warmup consumes the first year)

## Grid (pre-registered, one-at-a-time, both windows)

top-N {10, 30} · skip {0} · no-regime · costs 0.25%/side

## Pass criteria (all required)

1. Edge vs SPY buy-and-hold positive in BOTH windows
2. Grid: majority of variants positive in both windows
3. Max drawdown ≤ 1.5× SPY's in each window
4. No single month > 25% of total PnL

## India-specific reality check (disclosed regardless of verdict)

For an Indian resident trading this via LRS: US short-term gains are
taxed at slab rate (~30%), monthly churn makes ALL gains short-term, and
TCS applies on remittances. A gross pass must survive ~30% haircut on
gains to matter in practice — reported alongside the verdict.
