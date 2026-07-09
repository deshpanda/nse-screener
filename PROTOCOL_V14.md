# v14: VIX-augmented regime for v4 — pre-registration

Committed BEFORE the first run. Uses India VIX (option-implied fear) as
INFORMATION only — no derivatives are traded, per the owner's rule.
Challenger to the incumbent v4-regime under the standard replacement bar.
Prior is LOW: v4.1 already showed regime tinkering tends to lose.

## Rules (frozen)

- v14 = v4 verbatim, except new-month entries also require India VIX
  close < 25 at formation (25 = the conventional panic threshold, chosen
  from convention BEFORE any backtest, not tuned)
- when blocked: 100% cash that month (same as regime-off)

## Grid (one-at-a-time, both windows)

VIX < 20 · VIX < 30 · VIX-only (drop the 200DMA condition) ·
VIX percentile < 80th of trailing 756 sessions (adaptive threshold)

## Windows: IS 2023→present · OOS 2017–2022 (VIX data from 2016)

## Pass criteria — replaces v4-regime only if, in BOTH windows:

Sharpe ≥ v4-regime's AND maxDD ≤ v4-regime's AND edge > 0, AND the grid
majority keeps Sharpe ≥ v4-regime. Incumbent wins ties and mixed results.
