# v4 through the crisis era (2006–2015) — pre-registration (2026-08-17)

## Purpose, and what this is NOT

The champion has never been tested through a true bear market: our panel
starts 2016, so v4's 200-DMA circuit-breaker — the feature that exists
precisely for crashes — has never faced one. This spends the only such
window available (2008: Nifty ~−60% peak-to-trough; 2009: the global
momentum crash) as a SINGLE SHOT.

It is a stress test, not a gate. **It cannot change the October 15
go-live decision**: PROTOCOL_GOLIVE is frozen, its gates are operational
and behavioral, and "we found more supporting evidence" is not one of
them. A good result here does not accelerate anything; a bad result does
not veto anything. It changes what we EXPECT, and it belongs on the site
either way.

## Data (and the four honest deviations, frozen before any run)

Source: legacy NSE bhavcopy archives (`ingest/bhavcopy_old.py`, verified
to 2004), corporate actions from the same API used post-2016 (verified
to serve 2008/2012), NIFTY 50 index OHLC for benchmark and regime.

1. **Universe size differs structurally.** The ₹5cr liquidity floor is
   applied VERBATIM (changing it would be re-tuning), but it leaves
   127–227 names in 2006–2015 versus 1,120 today. Top-20 is therefore
   ~13% of the tradable universe then vs ~1.8% now. This is a genuine
   change in the strategy's character and is reported, not corrected.
2. **Benchmark is the Nifty 50 PRICE index** (NIFTYBEES was too thin
   pre-2016). It excludes dividends (~1.5%/yr), which FLATTERS v4.
   Diagnostic D2 re-runs with +1.5%/yr added to the benchmark.
3. **Rename coverage pre-2016 is likely incomplete.** Unmapped renames
   masquerade as delistings (this error was worth 39 points in the
   2016+ panel). The delist count is reported every run; if it exceeds
   2× the post-2016 rate, the result is flagged as data-limited rather
   than quietly believed.
4. **No delivery data** in the old archives. v4 does not use it.

## Cells (frozen — the entire grid)

- **PRIMARY**: v4 verbatim — top-20 by 12-1 momentum (skip 21), equal
  weight, monthly formation, next-open fills, 0.25%/side, ₹5cr 20-day
  median turnover floor, 100% cash when the index is below its 200-DMA.
  Window: formations 2006-01 → 2015-12 (2005 data loaded for warmup).
- **D1 diagnostic**: same, regime filter OFF — isolates exactly what the
  circuit-breaker contributed.
- **D2 diagnostic**: PRIMARY vs a dividend-adjusted benchmark (+1.5%/yr).
- **D3 diagnostic**: PRIMARY with the liquidity floor scaled by the
  Nifty level ratio — universe-size sensitivity only.
- Sub-period reporting (not separate tests): 2006–07 bull, **2008
  crash**, **2009 recovery**, 2010–15 chop.

No other variants. Diagnostics can never be promoted to the headline.

## Pass criteria (frozen)

PASS requires BOTH, on PRIMARY, over the full window:
1. total return beats the Nifty 50 price index after costs, and
2. maximum drawdown ≤ the index's maximum drawdown.

Anything else is a FAIL, reported as such. A pass does not promote
anything — v4 is already the incumbent; this only tells us whether the
incumbent's crash behavior is what we believed.

## Registered predictions

1. **2008: the breaker works.** v4's drawdown is far smaller than the
   index's (that is the entire purpose of the rule).
2. **2009: v4 badly lags the recovery** — it sits in cash through the
   V-bottom while the index rockets. This is the documented failure mode
   of 200-DMA filters and exactly what killed v8 in the US.
3. **Full window: v4 beats the index, but by much less than +100/+116**,
   and the advantage comes from avoided drawdown rather than return.
4. Delisting/rename noise runs elevated versus the modern panel.

If PRIMARY fails, the honest conclusion is "the circuit-breaker is worth
less than we assumed in regimes we have never traded," and it goes on
the site in those words.

## Amendments

None after this commit. Single shot: once run, this window is spent.
