# v25: promoter ownership-trend (quarterly shareholding) — pre-registration

Registered 2026-07-13, BEFORE any return is computed on this hypothesis.
Basis: the format review committed earlier today (STATE §research-queue) —
data facts only, no outcome peeks.

## Family disclosure (required reading before the numbers)

Promoter stake increases are the slow cousin of **v21** (India insider
market purchases): same actors, same direction, visible at a ~17-day
disclosure lag instead of same-evening, and capturing ALL mechanisms
(open-market buys, buybacks changing the denominator, warrant
conversion, creeping acquisition) rather than only market purchases.
v21's verdict is on the books: the drift existed OOS 2018-22, and is
gone in 2023-26. Therefore:

- The 2018-22 window is ALREADY SPENT for this family. We still run it,
  as a single shot, but a positive result there is EXPECTED and counts
  as mechanism confirmation, not discovery.
- **The decision window is IS 2023-26 alone.**
- Registered prior: long variants (E1/E2/E4) FAIL — per the alpha-decay
  law. The decrease screen (E3) is the genuinely open question, with a
  weak-negative prior tempered by the v22 retraction lesson (a "toxic"
  signal that evaporated under better data).

## Data (frozen)

`data/shareholding/*.parquet` — rows with non-null broadcastDate only
(the point-in-time era, 2015→present). Quarter-end rows only; dedupe
(symbol, quarter) keep=last (revisions supersede). Promoter % =
`pr_and_prgrp`; symbols via renames.canonical.

## Events (frozen; entry at next open after broadcastDate)

| id | definition | prior |
|---|---|---|
| E1 | QoQ promoter change ≥ +0.5pp, promoter > 0 | fail |
| E2 | QoQ promoter change ≥ +2.0pp, promoter > 0 | fail |
| E3 | QoQ promoter change ≤ −0.5pp, promoter > 0 (risk screen) | weak toxic |
| E4 | two consecutive quarters of promoter increase (any size > 0) | fail |

## Engine & grid (frozen — the v21 harness verbatim)

- backtest/events17 `run_kind`: excess return vs NIFTYBEES, universe =
  liquid (20d median turnover ≥ ₹5cr) non-ETF stocks.
- Hold 63 trading days (variants: 21, 126 — grid is these three, nothing
  else). Per-symbol cooldown gap_days=63.
- TWO nulls, per the two-null rule: (a) random-announcement baseline
  (ann_full, n=60k, seed 7 — same as v21's), (b) all-shareholding-filings
  null (every PIT quarter-end broadcast regardless of direction) — the
  activity tilt of merely filing.
- Windows: IS 2023-01-01→2027-01-01 (decision), OOS 2018-01-01→
  2023-01-01 (family-spent; consistency only).

## Pass criteria (frozen)

- E1/E2/E4 (long): PASS only if IS mean excess ≥ +3pp above the
  random-announcement null AND median excess > null median AND n ≥ 100.
  Anything less = DEAD; no post-hoc rescue, no new thresholds.
- E3 (screen): CONFIRMED only if IS mean excess ≤ −3pp below the
  random-announcement null AND n ≥ 100. Between −3pp and 0 = personal
  hygiene note at most, not a certified screen (v22 wording).
- A long PASS would then need the standard sensitivity plateau + OOS
  shot before promotion to challenger status (it does not touch v4
  regardless before a full gauntlet + its own paper phase, per
  PROTOCOL_GOLIVE's no-new-sleeves-in-2026 rule).

## Amendments

None after this commit. Failed variants stay dead.
