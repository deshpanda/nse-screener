# v15: Post-earnings-announcement drift, India — pre-registration

Committed BEFORE the first run. PEAD — prices keep drifting for weeks
after earnings surprises — is among the most-replicated anomalies in
finance. Our unfair advantage: 43,421 announcements with broadcast
timestamps, so entries are honestly after-the-news. This is DIFFERENT
from v7 (which used earnings inside a monthly momentum formation): PEAD
is event-time — enter right after the surprise, hold weeks.

## Event definition (frozen)

- SUE = (NP_q − NP_{q−4}) / σ(trailing 8 YoY changes, min 6) — as v7
- positive-surprise event: SUE ≥ +1.0 on a liquid (₹5cr floor),
  non-ETF stock; entry at the FIRST session open after the broadcast
  timestamp; hold 63 sessions; excess vs NIFTYBEES
- one event per symbol per hold window (first wins)
- NO trend filter in the primary — PEAD stands alone or not at all

## Grid (one-at-a-time, both windows)

SUE ≥ 2 · top-decile SUE per quarter · hold {5, 21} · +200DMA trend
filter · negative side (SUE ≤ −1, informational only — we don't short)

## Windows & lenses

IS 2023→present · OOS 2020–2022 (fundamentals limit, disclosed) ·
plus METHOD2 lenses on the event series where applicable
(quarter concentration, rolling consistency of quarterly mean excess).

## Pass criteria (all required)

1. IS mean AND median excess > 0, surviving 0.5% round-trip costs
2. Grid majority positive IS
3. Same, OOS, frozen, single shot
4. No quarter > 25% of positive excess

## US replication (evidence tier per METHOD2)

Requires historical earnings dates + surprises; being fetched from
Yahoo (secondary-quality source, disclosed). If usable: same event
design vs SPY. T1 = both pass · T2 = India passes, US untestable ·
T3 = India passes, US fails.
