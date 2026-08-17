# v40: buyback tender-offer price path — pre-registration (2026-08-19)

## What this can and CANNOT test (format review done first)

Dataset: `data/buybacks/events.parquet` — 330 tender-offer events
2016-2026 (record dates from the corporate-actions API), 310 (94%)
matched back to their announcement in the ann_full store; median
announce→record lag 14 days (p25 9, p75 51).

**CANNOT be tested with our data, stated plainly:** the full tender
arbitrage return needs (a) the TENDER PRICE and (b) the realized
ACCEPTANCE RATIO. Format review established that announcement snippets
truncate before the tender price — the numbers that regex out are FACE
values (Rs 10, Rs 2), not offer prices — and acceptance ratios live in
post-offer "basis of acceptance" PDFs we have not parsed. Any claim of
"~6-7% post-tax per tender event" (the figure our research sweep
surfaced) is therefore UNVERIFIED by us and must not be repeated as
though this study confirmed it.

**CAN be tested, and it is the decision-relevant half:** whether the
tender premium is already competed away in the stock price by the time a
retail participant can act. If the stock runs up into the record date
and gives it back after, the quota is worth less than the headline
premium suggests — and that is measurable now.

## Cells (frozen — entire grid)

Entry at next open after the stated signal date; excess vs NIFTYBEES;
liquid (≥₹5cr 20d median) only; one event per symbol per 126 days.
- **A1 announcement drift**: enter after the ANNOUNCEMENT, exit at the
  record-date close.
- **A2 accumulation window**: enter 5 trading days before the record
  date, exit at the record-date close.
- **A3 post-record decay**: enter the day after the record date, hold 21
  trading days. (Long-only project: a negative result here is a
  do-not-hold finding, not a short signal.)
- Two nulls, identical engine: random-announcement baseline (ann_full,
  n=60k, seed 7) and an all-buyback-events null for A3's window.

## Windows & pass (frozen)

IS 2023-01→2027-01 (decision); OOS 2016-01→2022-12 (single shot).
PASS for A1/A2 requires mean excess ≥ +3pp over the random-announcement
null AND median above the null median AND n ≥ 30 in the window, then the
v27.2 concentration check. A3 is descriptive (reported, no gate).

## Registered predictions

1. A1 and A2 FAIL the +3pp bar — the announcement is public and the
   tender-arb crowd is well organised, so the run-up is competed away.
2. A3 shows measurable post-record-date weakness (unaccepted shares get
   sold), making the record date an avoid-window for a momentum book.
3. If A2 passes, the quota trade's edge is bigger than the acceptance
   ratio alone implies, and the tender-price/acceptance PDF pipeline
   becomes the project's highest-value next dataset.

## Amendments
None after this commit.
