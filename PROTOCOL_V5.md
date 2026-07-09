# v5: Institutional footprint — follow sticky-money bulk/block buys

Committed BEFORE the first backtest. Client-NAME formats (not outcomes)
were inspected to write the classifier regex; no return was computed
before this file was committed.

## Thesis

Bulk/block deals name the counterparty — the only same-day, stock-level,
attributed institutional footprint in Indian public data. Long-horizon
("sticky") institutions — mutual funds, insurers, pension/sovereign funds
— buy on multi-quarter theses. Following their disclosed buys T+1 tests
the user's original "follow the institutions" idea in its most direct form.
Known headwind, stated upfront: disclosure is same-evening, so the market
gets one session to front-run our entry.

## Classification (frozen)

- sticky = client_name matches
  `MUTUAL FUND|LIFE INSURANCE|PENSION|PROVIDENT|SOVEREIGN` (case-insens.)
- per client/symbol/day: net qty = buys − sells (same-day churn nets out)
- event day for symbol s: total sticky net qty > 0

## Signal (frozen)

- event & close > 200-DMA (no falling knives — institutions average down,
  we cannot) & standard liquidity (20d median turnover ≥ ₹5cr) & no ETFs
- entry: next session's open (honest vs same-evening disclosure)
- engine: v2/v3 engine VERBATIM (ATR×2.5 stop on close, +2.5R half
  scale-out, 50-DMA trail, 1% risk sizing, 15% cap, 8 slots, breadth+trend
  regime, 0.25%/side, 20d re-entry cooldown). Zero retuning.

## Windows

In-sample 2023→present first; out-of-sample 2017–2022 single shot, frozen.

## Sensitivity grid (pre-registered, one-at-a-time)

- category: MUTUAL FUND only
- size: sticky net qty ≥ 10% of that day's traded volume
- context: add RS percentile ≥ 60
- deals: bulk only (drop block)

## Pass criteria (all required)

1. In-sample edge vs Nifty positive
2. In-sample grid: majority of variants positive (plateau)
3. Out-of-sample edge positive, frozen, single shot
4. Out-of-sample grid: majority positive
5. No single symbol > 25% of total PnL

Context: v4 (monthly momentum + regime) already passed at +77pt OOS. v5
must pass vs Nifty to be "real"; to earn capital over v4 it must also be
competitive with v4 or diversifying (low correlation) — reported either way.
