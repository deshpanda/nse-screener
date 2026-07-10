# v19: Sector momentum — pre-registration
# (+ v20 pledge screen: deferred, dataset under construction)

Committed BEFORE the first run.

## v19 spec (frozen)

- Sector map: NSE Nifty Total Market classification, 751 stocks
  (DISCLOSED: today's snapshot applied historically; industry membership
  is sticky but not immutable; unmapped stocks are excluded)
- Sector score at month-end: MEDIAN 12-1 momentum of its liquid mapped
  members (median = robust to one meme stock)
- Selection: top 3 sectors by score → within them, top 20 stocks by
  individual 12-1 momentum; v4 machinery otherwise verbatim
  (monthly, regime→cash, next-open fills, 0.25%/side)
- Bar: v4 challenger (Sharpe AND maxDD AND edge, BOTH windows, vs the
  rename-merged incumbent; incumbent wins ties)

## Grid (one-at-a-time, both windows)

top-5 sectors · sector score by 126d return · top 30 stocks · no-regime

## v20 pledge screen — why it is NOT run

NSE's pledge API returns only the current snapshot; free point-in-time
history does not exist. Backtesting today's pledges against the past =
lookahead + survivorship (pledge disasters delist). Instead the monthly
cron now CAPTURES the snapshot (data/pledge/), building our own
point-in-time dataset. Revisit when ≥ 12 months accumulate.
