# v16: Residual (idiosyncratic) momentum — pre-registration

Committed BEFORE the first run. Literature (Blitz et al.; robust across
emerging markets): rank stocks by their OWN trend with the market's
contribution stripped out — reportedly similar returns to plain momentum
at roughly half the volatility, less crash-prone. A v4 challenger with an
actual theoretical mechanism, unlike the parameter tweaks that died.

## Signal (frozen)

- beta: rolling regression of daily stock returns on NIFTYBEES returns,
  trailing 756 sessions (min 500)
- residual r_i − β·r_mkt daily; score = mean(residual) / std(residual)
  over sessions t−252 … t−21 (12-1 window, t-stat form)
- portfolio: top 20 by score among liquid non-ETF stocks, equal weight,
  monthly, regime→cash, fills next open, 0.25%/side — v4 machinery verbatim

## Grid (one-at-a-time, both windows)

52-week-high proximity ranking (close / 252d max) instead of residual
score · beta window 504 · no-regime · top 30

## Windows & bar

IS 2023→present · OOS 2017–2022. Challenger bar (v4.1 standard):
replaces v4-regime only if Sharpe ≥ AND maxDD ≤ AND edge > incumbent's
in BOTH windows; incumbent wins ties/mixed. METHOD2 lenses reported.
