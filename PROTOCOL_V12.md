# v12: Short-horizon news-pop reaction (India + US) — pre-registration

Committed BEFORE the first run. Fills a real gap the Author spotted: all
prior event studies held 10–126 sessions; the day-trader horizons (sell
same day / next day / +2) were never tested. Hypothesis: after a big,
public, everyone-saw-it up-move, is there any further drift a retail
trader can capture at the FIRST price actually available to them?

## Physics disclosed upfront

The overnight gap belongs to holders, not reactors — news is in the open
print. Only post-open drift is testable or tradeable. Intraday entries
cannot be honestly backtested on free decade-long data (no minute bars);
granularity is open/close, which matches EOD retail execution.

## Events (frozen)

- India: stock day-return ≥ +5% AND volume ≥ 3× its 20d average AND
  close > 200-DMA; stocks only (no ETFs), ₹5cr liquidity floor.
  Caveat: upper-circuit stocks can be hard to buy next open — results
  are therefore FLATTERED for the strategy; a fail is extra credible.
- US: identical to v6's definition (≥7% pop, 3× volume, uptrend,
  point-in-time S&P 500) — reused for comparability, holds are new.
- one event per symbol per 21 sessions (first wins)

## Entries & holds (the grid IS the question here)

entry (a) next session's OPEN — the reactor's first price
entry (b) event-day CLOSE — the EOD trader who acts the same evening
holds: 1, 2, 5 sessions (sell at close). Excess vs NIFTYBEES / SPY.

## Windows

India: IS 2023→present · OOS 2017–2022 (frozen)
US: IS 2023→present · OOS 2017–2022 (frozen)

## Pass criteria (per market, all required)

1. IS mean AND median excess > 0 for at least one pre-registered
   entry×hold cell, AND that same cell positive OOS (frozen, single shot)
2. Sign consistency: the winning cell's neighbors (adjacent hold) must
   not flip sign in either window (no lone spikes)
3. Costs: the cell must survive 0.25%/side round trip (India) /
   0.10%/side (US), subtracted explicitly
4. No calendar quarter > 25% of summed positive excess
