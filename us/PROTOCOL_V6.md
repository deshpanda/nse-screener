# v6: "Rally following" event study (US large caps) — pre-registration

Committed BEFORE any forward return is computed. Tests the user's claim:
joining an "obvious" rally (Dell on presidential praise, Micron on the AI
wave) is near-guaranteed profit. "Obvious" must be defined ex-ante, so the
enumeration counts the forgotten losers alongside the remembered winners.

## Event definition (frozen — the mechanical version of "obvious rally")

On day t, a stock qualifies if ALL hold:
- close-to-close return ≥ +7% (a pop everyone saw)
- volume ≥ 3× its trailing 20d average (the crowd showed up)
- close > 200-DMA (already-strong stock; the rally has a trend behind it)
- the stock was an S&P 500 member ON day t (point-in-time list, fja05680)
- no other qualifying event for the same ticker in the prior hold window
  (no overlapping double-counts; first event wins)

Entry at t+1 open — same-day-or-next-day join, as the user traded Dell.
Hold 21 trading sessions (primary). Excess return = stock − SPY over the
identical span.

## Windows

- in-sample 2023 → present (covers the user's Dell/Micron trades)
- out-of-sample 2017–2022 (Trump-1 tariffs, COVID, 2022 bear), frozen,
  single shot

## Sensitivity grid (pre-registered, one-at-a-time)

pop {5%, 10%} · volume {2×, 5×} · hold {10, 42, 63} · no-trend-filter

## Pass criteria (all required)

1. In-sample MEAN and MEDIAN excess return > 0
2. In-sample grid: majority of variants positive mean excess
3. Out-of-sample: mean and median excess > 0, frozen
4. No single calendar quarter > 25% of summed excess
5. Win rate reported prominently — the claim under test is "guaranteed";
   anything materially below 100% falsifies the word, whatever the mean says

## Known data caveats (disclosed upfront)

- yfinance lacks history for delisted tickers; events on stocks that later
  vanished are missing. Coverage % of the point-in-time universe is
  reported with results. Large-cap disappearances are mostly M&A (which
  pops prices), so the bias plausibly flatters the strategy — favorable to
  the user's claim, making a FAIL more credible, not less.
- US trading from India (IndMoney/LRS): no margin, slab-rate short-term
  tax, TCS on remittance — real-world drag not modeled here.
