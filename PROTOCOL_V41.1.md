# v41.1: long-horizon reversal, US replication arm — pre-registration (2026-08-28)

## Why, and why NOT on our own US panel

v41 killed long-horizon reversal in India by a huge margin and found the
opposite sign (losers keep losing). Two explanations remain open, and
they have different consequences:
  (A) edges are local — the effect is real in the US, absent in India;
  (B) the effect decayed after publication everywhere, and the US
      pre-1985 era will show it while the post-1985 era will not.
This arm distinguishes them on the paper's home turf.

**Our own US price panel is disqualified for this test and will not be
used.** `us/data/prices_deep/` is yfinance-sourced and therefore
SURVIVOR-ONLY (no delisted tickers). For a strategy that buys the
biggest multi-year losers, that is the single most damaging possible
bias: the losers that went to zero are missing from the sample. The
engine audit (PROTOCOL_USAUDIT) worked around this by scoring only
co-movement and era ordering, never levels; a reversal study is entirely
about levels, so no such workaround exists.

## Data (frozen)

Ken French's CRSP-built, survivorship-clean, value- and equal-weighted
monthly portfolio returns, verified downloadable 2026-08-28:
- `10_Portfolios_Prior_60_13` — decile sort on prior 60-to-13 month
  returns (De Bondt & Thaler's construction). Lo = losers, Hi = winners.
- `6_Portfolios_ME_Prior_60_13` — the same sort SPLIT BY SIZE.
- Market return = Mkt-RF + RF from the F-F 3-factor file (already
  cached under `us/data/french/`).
Parsing reuses the audited `_monthly_section` reader from
`us/engine_audit.py`, whose output was spot-checked against Oct-1987,
Oct-2008 and Apr-2009 known values.

## Cells (frozen — the entire grid)

- **R1 the effect**: annualized return of the LOSER decile minus the
  WINNER decile, value-weighted, per era.
- **R2 vs market**: loser decile minus market, per era.
- **R3 size split**: loser-minus-winner within SMALL and within BIG
  (the 6-portfolio file) — tests whether the effect is a small-cap
  phenomenon, which is the open question v41 left in India.
- Equal-weighted variants reported alongside as diagnostics only.

Eras, frozen, chosen on publication dates not on results:
1926–1984 (pre-publication), 1985–1999 (post-publication),
2000–2014, 2015–present.

## Pass / conclusion criteria (frozen)

This arm is a REPLICATION, not a tradable strategy — nothing here can go
live, and no cell can promote anything. It resolves the fork:
- **Verdict (A) "edges are local"** requires R1 > 0 in BOTH the
  1926–84 and 2015–present eras (the effect alive in the US today).
- **Verdict (B) "decayed everywhere"** requires R1 > 0 in 1926–84 AND
  R1 ≤ 0 (or within 1pp/yr of zero) in 2015–present.
- **Verdict (C) "never robust"** if R1 ≤ 0 even in 1926–84 — which
  would also mean our parsing is suspect, since it would contradict the
  published paper on its own data; in that case the result is void
  pending a parsing audit, not published as a finding.

## Registered predictions

1. Verdict (B): strong pre-1985, weak-to-absent post-2015.
2. R3 shows the effect concentrated in SMALL caps in the early era —
   which would mean India's liquidity floor is a plausible reason for
   v41's failure after all, partially reversing my wrong v41 prediction.
3. R2 (losers vs market) is weaker than R1, because the winner leg does
   much of the work in a long-short spread.

## Amendments
None after this commit.
