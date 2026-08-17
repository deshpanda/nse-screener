# v33: dual momentum, India adaptation (Antonacci GEM) — pre-registration (2026-08-18)

## Why & family

The most-followed systematic retail strategy globally; never tested
here. NEW family: asset-class rotation (4 ETFs), not stock selection —
no contaminated windows. Monthly decisions, ~2-6 switches/yr → tax-light
per our measured ~6pp/yr fast-strategy drag. Faces 2008 AND the 2010-15
chop that just humbled v4's breaker.

## Data constraints that dictate design (from our own trap list)

1. bhav ETF OPEN prints are fake (v30 trap) → ALL fills at next-day
   CLOSE (signal at month-end close, execute at the following close).
2. LIQUIDBEES yield arrives as bonus units, invisible in prices → the
   cash leg earns 0% in PRIMARY (conservative, biases AGAINST v33;
   diagnostic D1 adds 5%/yr accrual to cash periods to bound the error).
3. NIFTYBEES 10:1 split handled by the CA-adjusted panel (verified).

## Spec (frozen)

Universe: NIFTYBEES (equity large), JUNIORBEES (equity next-50),
GOLDBEES (gold), LIQUIDBEES (cash). Monthly at month-end:
- Relative momentum: winner of NIFTYBEES vs JUNIORBEES by trailing
  12-month total return (no skip — GEM convention, frozen).
- Absolute momentum: if that winner's 12m return > LIQUIDBEES' 12m
  return, hold it; else hold the better of GOLDBEES/LIQUIDBEES (12m).
- Costs: 0.25%/side on switches only (house standard).

## Cells (frozen — entire grid)

- PRIMARY: as above.
- D1: PRIMARY + 5%/yr accrual on cash-leg months (bounds trap #2).
- D2: equity-only dual momentum (no gold; fallback = cash) — isolates
  gold's contribution.
- Sub-period reporting: 2008, 2009, 2010-15, 2016-22, 2023-26.

## Windows & pass (frozen)

IS 2023-01→2027-01; OOS 2008-01→2022-12 single shot (12m warmup from
2007). Benchmark NIFTYBEES buy-and-hold. PASS = PRIMARY beats the
benchmark after costs in BOTH windows. MaxDD reported alongside — the
strategy's marketing claim is drawdown, and we test the claim as made.

## Registered predictions

1. 2008: absolute momentum sidesteps most of the crash (its one job).
2. 2010-15 chop: whipsaw rent, like our breaker paid (−66pt lesson).
3. Full-window maxDD roughly HALF of buy-and-hold's.
4. The both-windows total-return gate FAILS — insurance profile, not
   an alpha engine. If it passes both windows, that is a genuine
   surprise → v27.2-style confirmation before anything further.

## Amendments
None after this commit.
