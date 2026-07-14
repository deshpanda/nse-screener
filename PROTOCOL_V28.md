# v28: institutional accumulation (FII/DII quarterly detail) — pre-registration (2026-07-15)

## Family disclosure & the one open question

This is the SIXTH disclosure-based "follow someone" test. The family is
0-for-5 (v5 bulk deals, v9 US insiders, v10 13F, v21 promoters, v25
ownership trends) — the registered prior is LOW accordingly. The one
honest reason to run it anyway: institutions are the first tested actor
whose trading is STRUCTURALLY slow — mandates and size force positions
to build over months — so if any exploitable drift exists, it should
live at LONGER horizons than the insider tests probed. That prediction
(h126 > h63 > h21, if anything survives at all) is registered here,
before any return is computed.

## Data (frozen; format-review facts in STATE, committed 9b05d97)

`data/shareholding_detail/` — 2.46M rows / 58,800 filings, 2016→now,
broadcast-timestamped (median lag ~17d after quarter end). Extraction
rules frozen exactly as the review documented:
- EXACT era-canonical labels only (whitespace-normalized, lowercase):
  MF = {"mutual funds/", "mutual funds"}; FPI = {"foreign portfolio
  investors"} ∪ {"foreign portfolio investors category i", "...ii",
  category-iii variants}. NEVER substring-match (named-holder rows
  like "SBI Mutual Fund" double-count) and NEVER use Sub-total (B)(1)
  (it silently changes meaning across the two filing formats).
- Quarter-end rows only; dedupe (symbol, quarter) keep latest recordId.
- FPI stake per quarter = sum of that quarter's canonical FPI labels.

## Events (frozen; entry at next open after broadcastDate)

| id | definition | prior |
|---|---|---|
| E1 | MF stake QoQ change ≥ +0.5pp | fail |
| E2 | FPI stake QoQ change ≥ +0.5pp | fail |
| E3 | MF AND FPI both ≥ +0.25pp same quarter (double confirmation) | least-surprising positive, esp. h126 |
| E4 | MF stake QoQ change ≤ −0.5pp (risk screen) | weak toxic |
| E5 | FPI stake QoQ change ≤ −0.5pp (risk screen) | weak toxic |

## Engine & grid (frozen — the v25 harness verbatim)

- events17 run_kind: excess vs NIFTYBEES, liquid (≥₹5cr) non-ETF,
  gap_days=63 per symbol.
- Holds: 21, 63, 126 for every event (the horizon LADDER is the
  hypothesis this time — all three registered up front, no post-hoc
  horizon shopping).
- TWO nulls: (a) random-announcement baseline (ann_full n=60k seed 7 —
  identical to v21/v25), (b) all-detail-filings null (every deduped
  quarter-end broadcast regardless of direction).
- Windows: IS 2023-01→2027-01 (decision); OOS 2017-01→2023-01 (single
  shot; virgin for this family).

## Pass criteria (frozen)

- Longs (E1/E2/E3): PASS only if IS mean excess ≥ +3pp above the
  random-announcement null AND median > null median AND n ≥ 100 (the
  base-rate review shows supply supports it — no small-n apologetics).
- Screens (E4/E5): CONFIRMED only if IS mean ≤ −3pp below the null,
  n ≥ 100. Between −3 and 0 = personal-hygiene note at most.
- Any long PASS ⇒ plateau + concentration (v27.2-style lottery check)
  before challenger status. Nothing goes live in 2026 regardless.

## Registered predictions

All longs fail IS at h21/h63 (alpha-decay law, family record). The
registered long-shot: E3 at h126 shows the family's only positive-vs-
null IS cell. Screens: real pre-2023, decayed IS (the v21/v25/v22
pattern). If instead NOTHING is positive even OOS, that too is news:
it would say institutional flows were never exploitable even before
the app era — disclosure lag kills slow actors just as dead.

## Amendments

None after this commit. Failed variants stay dead.
