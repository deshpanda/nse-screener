# v41: long-horizon reversal (De Bondt & Thaler) — pre-registration (2026-08-28)

## Why & family

Source: De Bondt & Thaler (1985), "Does the Stock Market Overreact?" —
3-5 year LOSERS outperform 3-5 year winners over the following years.
Surfaced by a Zerodha research video; the paper is the real citation.

NEW family: long-horizon reversal. This is not a momentum variant — it
is the OPPOSITE sign at a 3x longer horizon, so it does not re-mine
v4's family. Two things make it testable only now:
1. It needs deep history (3-5y formation + multi-year holds). Our panel
   ran from 2016 until the 2026-08-17 crisis backfill extended it to
   2005-01-03 → present (5,424 sessions).
2. Multi-year holds land in the 12.5% LTCG band, versus v4's measured
   ~6pp/yr all-STCG drag (PROTOCOL_TAX). After-tax is therefore a
   PASS CRITERION here, not a footnote.

## Disclosures, made before running

- **Window overlap**: 2006-2015 was examined once already, by the
  crisis test (PROTOCOL_CRISIS). That test looked ONLY at v4's
  momentum output over that period; no long-horizon loser ranking was
  ever computed or seen. Contamination risk is judged low but non-zero,
  and is declared here rather than assumed away.
- **The liquidity floor may be fatal, and that is allowed.** Reversal
  is documented to concentrate in small, distressed, illiquid names.
  Our ₹5cr 20-day-median floor may exclude exactly those. The floor is
  applied VERBATIM. If the effect dies because of it, that is the
  finding — the floor is NOT relaxed afterwards to rescue the result.
- **Power is thin and overlapping portfolios flatter.** ~9-10 years per
  window with multi-year holds gives roughly 3 non-overlapping cycles.
  The concentration check therefore carries more weight than usual.

## Spec (frozen)

Universe: liquid (≥₹5cr 20-day median turnover) non-ETF NSE stocks.
Signal: trailing 36-month total return, SKIPPING the most recent 21
sessions (so short-term reversal cannot contaminate it — same skip
convention as v4). Hold the **20 worst** performers, equal weight.
Formation at month-end, fills next open, 0.25%/side.
Rebalance: `rebalance_every=252` sessions (annual; the engine counts
sessions, not months).

## Cells (frozen — the entire grid)

- **PRIMARY**: 36-month formation, annual rebalance, no regime filter.
- **C2**: 60-month formation, otherwise identical.
- **C3 diagnostic**: PRIMARY plus v4's 200-DMA breaker. Diagnostic
  only; never promotable to the headline.
- Reported alongside: number of qualifying names per formation (to show
  whether the liquidity floor bound), and correlation to v4.

## Windows & pass (frozen)

The house-standard IS window (2023→present) is too short to hold a
multi-year strategy even once, so this family splits the usable history
in halves — declared now, not chosen after seeing results:
- **OOS single shot**: 2008-01 → 2016-12
- **IS decision**: 2017-01 → 2026-08

PASS requires ALL of:
1. beats buy-and-hold NIFTYBEES after costs in BOTH windows;
2. still beats it in the IS window AFTER TAX (12.5% LTCG on holds >365
   days, 20% STCG otherwise, benchmark taxed at 12.5% terminally);
3. concentration check — the best single year contributes < 40% of the
   summed positive annual excess, in each window.

Any failure = DEAD. A pass then faces the incumbent rule against v4 on
identical windows, and could only ever be a diversifying sleeve, never
a v4 replacement, and not before its own paper phase.

## Registered predictions

1. PRIMARY FAILS the both-windows gate.
2. The liquidity floor binds hard — the qualifying universe will look
   like mid/large caps, not the distressed micro-caps where the
   published effect lives.
3. If anything survives, it is the older window only (the decay law has
   now killed seven visible edges in the recent era).
4. The after-tax criterion, unusually, will HELP rather than hurt —
   annual rebalancing puts most lots in the LTCG band.

## Amendments
None after this commit.
