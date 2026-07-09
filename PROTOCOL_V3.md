# v3: Institutional-footprint (delivery accumulation) — pre-registration

Committed BEFORE the first backtest run. If v3 fails these criteria it is
dead; no post-hoc parameter rescue counts as anything but a new hypothesis.

## Thesis

Delivery quantity (shares actually moved to demat, not intraday churn) is
the least fakeable public footprint of institutional accumulation. A
cluster of high-delivery up-days in an uptrending stock = someone big is
building a position. Enter on cluster formation, ride with the existing
(v2, unchanged) risk engine.

## Signal (primary, frozen)

- accumulation day: deliv_qty > 2.0 × trailing 60d median deliv_qty
  AND close > prev close
- cluster: ≥ 3 accumulation days within the last 20 trading days
- entry signal: the FIRST day a cluster forms (fresh cross only)
- context: close > 200-DMA, RS percentile ≥ 60, same liquidity filter
  (20d median turnover ≥ ₹5cr), stocks only (no ETFs)
- re-entry cooldown: 20 trading days after any exit in that symbol

## Everything else: v2 engine verbatim, zero retuning

ATR(14)×2.5 stop on close, half off at +2.5R then breakeven, 50-DMA trail,
1% equity risk per trade, 15% position cap, 8 slots, regime = bench>200DMA
AND breadth≥0.40, costs 0.25%/side.

## Windows

- design/in-sample: 2023-01-01 → present (same as v2's, keeps history clean)
- out-of-sample: 2017 → 2022 entries, run ONCE with frozen params
  (delivery for 2016-2019 comes from MTO archives, being backfilled)

## Sensitivity grid (pre-registered, run in-sample AND out-of-sample)

spike mult {1.5, 2.5} · cluster size {2, 4} · RS floor {50, 70} ·
window {15, 30}  — one-at-a-time perturbations of the baseline.

## Pass criteria (all required)

1. In-sample edge vs Nifty positive
2. In-sample sensitivity: majority of perturbations keep positive edge
   (plateau, not spike)
3. Out-of-sample edge positive, frozen params, single shot
4. Out-of-sample sweep: majority of variants positive edge
5. No single symbol > 25% of total PnL

Bulk-deal confirmation is NOT in v3. If tested later it is v3.1, a new
pre-registered hypothesis, not a rescue knob.
