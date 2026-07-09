# v9: US insider cluster buys — pre-registration

Committed BEFORE the first event study run. The US version of "follow the
institutional footprint" (v5 died in India on disclosure lag). US Form 4
insider trades disclose within 2 business days — the freshest attributed
footprint in any market we can access — and opportunistic insider
PURCHASES have real academic support (Cohen-Malloy-Pomorski). This is the
strongest fair test the "follow smart money" thesis will ever get from us.

## Data

openinsider.com screener (aggregates SEC Form 4), purchases only,
value ≥ $25k, monthly chunks 2016→present. Event timing uses the FILING
timestamp (public knowledge), never the trade date.

## Event definition (frozen)

- cluster: ≥ 3 DISTINCT insiders of the same company filing purchases
  within 21 calendar days, combined value ≥ $250k
- event date: the filing date that completes the cluster; one event per
  ticker per 63 sessions (first wins)
- universe: stock must be an S&P 500 member on event date (price data +
  point-in-time honesty; NOTE: insider signal is strongest in small caps
  per literature — this restriction biases AGAINST the signal, disclosed)
- entry: next session's open; hold 63 sessions; excess vs SPY

## Windows

in-sample 2023→present · out-of-sample 2016–2022, frozen, single shot

## Grid (pre-registered, one-at-a-time, both windows)

cluster ≥2 insiders · combined ≥$100k · hold {21, 126} · officers-only
(CEO/CFO/COO/Pres titles)

## Pass criteria (all required)

1. Mean AND median excess > 0 in-sample
2. Grid majority positive in-sample
3. Same, out-of-sample, frozen
4. No calendar quarter > 25% of summed positive excess

Context: v5 (India, same-evening disclosure) was -18.7pt. If 2-day
disclosure + academic backing can't produce a positive distribution here,
"follow the smart money" is dead everywhere we can reach it.
