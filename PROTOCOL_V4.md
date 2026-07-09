# v4: Monthly-rebalance cross-sectional momentum — pre-registration

Committed BEFORE the first run. Parameters are the standard academic ones
(Jegadeesh-Titman 12-1), not ours — the whole point is minimal knob surface.

## Thesis

12-month price momentum (skipping the most recent month, which reverses)
is the most-replicated equity anomaly in the literature, documented in
India specifically (and productized as the Nifty200 Momentum 30 index).
Monthly rebalance = ~12 decisions/year, low cost drag, nothing to
curve-fit daily.

## Rules (frozen)

- Formation: each month's last trading day. Signal = close(t−21) /
  close(t−252) − 1  (12-month return, most recent 21 sessions skipped)
- Universe: NSE stocks (no ETFs), 20d median turnover ≥ ₹5cr at formation
- Portfolio: top 20 by signal, equal weight, no stops
- Execution: fills at the NEXT session's open after formation;
  0.25%/side costs charged on every position that turns over
- Delisted/suspended mid-hold: exit at last available close (logged;
  if frequent, results are suspect and we say so)
- Secondary pre-registered variant: identical + regime filter (move to
  cash when NIFTYBEES < its 200-DMA at formation) — momentum crashes are
  the anomaly's known failure mode; this is the literature's standard fix,
  not our invention

## Windows

In-sample 2023→present and out-of-sample 2017–2022, reported separately.
(With zero tuned parameters the split is a formality, but the rule stands.)

## Sensitivity grid (pre-registered, both windows)

top-N {10, 30} · skip {0, 21} · turnover floor {₹2.5cr, ₹10cr}

## Pass criteria (all required)

1. Positive edge vs Nifty buy-and-hold in BOTH windows (primary or the
   regime variant — declared per-variant, no mixing)
2. Grid: majority of variants positive in both windows
3. Max drawdown ≤ 1.5× Nifty's in each window
4. No single month > 25% of total PnL
