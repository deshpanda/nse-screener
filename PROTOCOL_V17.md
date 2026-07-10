# v17: Corporate-event studies (buybacks, order wins) — pre-registration

Committed BEFORE any event outcome is computed. Mechanism-backed events
from NSE's corporate-announcements feed (timestamps = point-in-time):
a buyback makes the company itself a bidder for its own shares; an order
win is a real cash-flow shock.

## Events (frozen)

- Buyback: first announcement per symbol whose category/desc mentions
  buyback (board approval or record-date notice; FIRST mention wins,
  one event per symbol per 126 sessions)
- Order win: announcements categorized as award/receipt of orders
- entry: first session open after announcement timestamp; hold 63
- universe: liquid (₹5cr), non-ETF; excess vs NIFTYBEES

## The two-null rule (learned in the audit, now formalized)

Every event type is judged against BOTH nulls:
(a) vs NIFTYBEES (the capital question), AND
(b) vs the ALL-ANNOUNCEMENTS baseline — the mean excess of a random
    announcement in the same window (the universe-tilt control that
    exposed v15). An event type must beat BOTH to pass.

## Grid: hold {21, 126} · buyback record-date-only · order wins ≥ (text
mentions 'crore') · IS/OOS = 2023-26 / 2017-22 (announcements exist
across the full panel)

## Pass criteria: IS mean AND median > 0 net of 0.5% round-trip vs BOTH
nulls · grid majority · OOS single shot same · quarter concentration ≤ 30%
