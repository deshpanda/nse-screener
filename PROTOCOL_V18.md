# v18: Smart-buyer track records — pre-registration

Committed BEFORE any outcome is computed. v5 asked "are institutions
worth following?" (no). v18 asks "which BUYERS are worth following?" —
scoring all 18,644 named bulk/block counterparties by the forward
returns of their OWN past deals, strictly point-in-time, and following
only the proven. Nobody without a decade of named deals can run this.

## Construction (frozen)

- deal = net BUY per (client, symbol, day) from bulk+block history,
  symbol canonicalized, liquid (₹5cr) non-ETF stock at deal date
- deal outcome = 63-session excess vs NIFTYBEES from next session's open
- client skill at time t: uses ONLY deals whose outcome window closed
  before t (deal date ≥ 95 calendar days before t). PROVEN client:
  n ≥ 10 completed deals AND mean excess > 0 AND t-stat ≥ 1
- event: a PROVEN client makes a new net buy → follow at next session's
  open, hold 63 sessions; one event per symbol per hold window

## The two nulls (both must be beaten)

(a) NIFTYBEES; (b) the ALL-DEALS baseline: mean excess of every net-buy
deal in the same window regardless of buyer skill — if "proven" buyers
don't beat the average deal, the track record carries no information.

## Grid (one-at-a-time, both windows)

n ≥ 20 · t-stat ≥ 2 · hold 21 · block deals only · top-decile clients
by past mean (instead of threshold rule)

## Windows: IS 2023-26 · OOS 2017-22 (early OOS years have thin score
history — fewer proven clients; disclosed). Pass criteria: IS mean AND
median > 0 net of 0.5% round-trip vs BOTH nulls · grid majority · OOS
single shot same · quarter concentration ≤ 30%.
