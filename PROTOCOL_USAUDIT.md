# US engine-replication audit — pre-registration (2026-07-13)

## Purpose (what this is and is not)

Validate the MONTHLY ENGINE's mechanics against five decades of
published US momentum evidence. The US momentum premium is the
best-documented anomaly in finance (Jegadeesh–Titman 1993 and the
entire literature after it); if our engine, pointed at US data, does
NOT reproduce the known qualitative record — premium before 2009, the
2009 momentum crash, decay in the 2010s — then our engine (or data
plumbing) has a bug, and v4's India numbers inherit that doubt.

This is an AUDIT like PROTOCOL_METHOD2, not a strategy: nothing here
can go live, regardless of results (v8 already killed US momentum as a
strategy for us; PROTOCOL_GOLIVE forbids new 2026 sleeves anyway).

## Design (frozen)

- Portfolio: the v4 core verbatim — top 20 by 12-1 momentum
  (skip=21 trading days), equal weight, formation at month-end, fills
  at next open, 0.25%/side churn cost. NO regime filter (that is the
  India-specific overlay; v8 established it hurts in the US).
- Universe: point-in-time S&P 500 membership (fja05680 daily lists),
  prices from yfinance extended back to 1995-06 for every ticker that
  EVER appears in the membership file. New file us/data/prices_deep/
  (batch-restartable); the v8-era prices.parquet is not touched.
- Window: formations 1997-01 → 2026-06 (first year burns in the 12-1
  lookback).
- Literature reference: Ken French data library —
  "10 Portfolios Formed on Momentum (12-2)", monthly, decile 10
  ("High"), both value- and equal-weighted; market = Mkt-RF + RF from
  the F-F 3-factor file. Files cached under us/data/french/.

## Known bias, disclosed up front

yfinance has no data for delisted tickers (Enron, Lehman, Bear
Stearns…), so the deep panel holds SURVIVORS only. Direction: inflates
our portfolio's level returns. Therefore levels are NOT scored — only
co-movement and era ordering, which survivorship distorts far less.

## Pass bars (frozen)

- **A. Mechanical fidelity**: correlation of monthly returns, our
  portfolio vs French decile-10, over the full overlap ≥ 0.75 against
  at least one of the VW/EW series. This is the engine test proper —
  formation timing, skip month, holding mechanics.
- **B. Era replication** (our portfolio minus French market,
  annualized):
  1. 1997–2008 excess > 0 (the documented premium era);
  2. 2009 excess < 0 (the momentum crash);
  3. 2010–2019 excess < 1997–2008 excess (the documented decay).
- **C. Reference sanity**: French's own VW decile-10 minus market must
  itself show the same three-era pattern in our processing of their
  file — else our PARSING is wrong and A/B are void.

## Registered predictions

A, B and C all pass. Any failure = suspected engine or plumbing bug →
find it, fix it, re-run THIS protocol unchanged; the audit only closes
when the criteria pass with an explanation for what was wrong. (This is
an audit of our code, not of the market — "momentum didn't exist" is
not an admissible conclusion at these sample sizes.)

## Amendments

None after this commit.
