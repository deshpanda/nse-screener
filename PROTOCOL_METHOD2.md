# Method upgrade 2: walk-forward consistency + DSR + PBO — pre-registration

Committed BEFORE running the harness on anything. Upgrades the gate from
"two fixed windows" to three additional lenses, with interpretation fixed
in advance so results can't be rationalized.

## The three lenses (backtest/validate.py)

1. **Rolling consistency**: 24-month rolling edge vs benchmark across the
   full 10y panel. Report % of windows positive and the worst window.
2. **Deflated Sharpe Ratio** (Bailey–López de Prado): probability the
   strategy's Sharpe is genuinely > 0 after penalizing (a) how many
   strategies we tried, (b) non-normal returns. Trials N = 16 (the
   scoreboard) primary; N = 40 (counting every grid variant) stress.
3. **PBO via CSCV** on the monthly-strategy family: S = 12 blocks, all
   C(12,6) train/test splits; PBO = fraction of splits where the
   in-sample-best variant ranks below median out-of-sample.

## Pre-committed interpretation for the v4 retro-audit

- DSR ≥ 0.90 at N=16: v4's evidence upgraded; proceed as planned.
- 0.50 ≤ DSR < 0.90: proceed with paper phase but real-money sizing at
  go-live is halved vs plan.
- DSR < 0.50: v4 is downgraded to "plausible, unproven" — paper phase
  extends to 6 months minimum.
- PBO < 0.30: selection process healthy. 0.30–0.50: caution note.
  > 0.50: our variant-selection is likely overfit; freeze all new
  strategy launches until understood.
- Rolling consistency: if < 60% of 24-month windows beat Nifty, the
  "long stretches of losing" risk gets a dedicated site disclosure.

## Standing rule for future candidates

Every new strategy must report all three lenses at verdict time, in
addition to the existing two-window + grid gate. Dual-market replication
(India primary, US secondary) is recorded as an evidence tier:
T1 = passed both markets, T2 = passed India + US untestable/mixed,
T3 = passed India, failed US.
