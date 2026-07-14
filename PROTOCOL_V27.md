# v27: index-inclusion flows (synthetic constituents) — pre-registration (2026-07-14)

## Hypothesis & why this family is different

Every dead strategy so far traded an INFORMATION signal (someone knew
something; disclosure leaked it; the market front-ran us). Index
inclusion is a FLOW signal: when a stock enters an index, tracker funds
must buy it mechanically, information-free. Documented in US large caps
for decades (and famously arbitraged toward zero there by the 2010s).
India's boundaries are less arbitraged; that is the open question.

## Data (frozen)

`data/constituents_synth.parquet` (built + calibrated 2026-07-14,
never used in any study — both windows below are virgin for this
family). Ranks: ffmcap for the 50 and 100 boundaries (free-float beat
plain mcap on all ten Nifty50 snapshots), mcap for the 500 boundary
(calibration preferred it). Known limitation, designed around: rank
error is largest AT the boundary, so events require DEEP crossings.

## Events (frozen; monthly rank series, entry next open after month-end)

| id | boundary | definition (rank at t-1 → rank at t) |
|---|---|---|
| A50 | Nifty50-ish | > 60 → ≤ 40 |
| A100 | Nifty100-ish | > 120 → ≤ 80 |
| A500 | Nifty500-ish | > 550 → ≤ 450 |
| D50/D100/D500 | drops | exact mirrors (≤ 40 → > 60, etc.) |

Adds are the long candidates; drops are risk-screen candidates. One
event per (symbol, boundary) per 6 months (gap_days=126 on the same
boundary; a stock may fire different boundaries).

## The confound, and the two nulls (frozen)

A boundary-crosser is by construction a recent winner — naive excess
would just rediscover momentum (which we already own via v4). Verdict
therefore requires beating BOTH:
1. **Near-boundary non-crossers**: same month, rank within [0.8N, 1.2N]
   at t for two consecutive months without crossing. Controls for
   "similar-size stock at the same moment".
2. **Momentum-matched null**: same month, liquid non-crossers in the
   SAME 12-1 momentum decile and rank within [0.5N, 2N]. Controls for
   "recent winner of similar size". This is the null that kills the
   lazy version of this idea.

Engine: events17 run_kind (excess vs NIFTYBEES, liquidity ≥ ₹5cr),
hold 63 primary; 21 and 126 variants for A50/A100 only. Null events
run through the IDENTICAL engine as pseudo-events.

## Windows (frozen)

IS 2023-01→2027-01 (decision), OOS 2018-01→2023-01 (single shot, virgin
for this family). Both reported; IS decides, OOS judges consistency.

## Pass criteria (frozen)

- Adds (A50/A100/A500): PASS only if IS mean excess ≥ +3pp above BOTH
  nulls AND median above both null medians AND n ≥ 30. (Boundary events
  are rare; n≥100 is unreachable — the small-n limit is disclosed, and
  any pass is CONFIRMATORY-ONLY: it earns a fresh-data second shot
  before challenger status, never direct promotion.)
- Drops: risk screen CONFIRMED only if IS mean excess ≤ −3pp below both
  nulls, n ≥ 30.
- No post-hoc thresholds, no new boundaries, no buffer tuning.

## Registered prediction

OOS adds weakly positive (the effect existed somewhere in 2018-22);
IS adds ≈ 0 vs the momentum-matched null (visible + famous ⇒ eaten,
per the alpha-decay law). Drops: no confident prior. We register the
possibility of being wrong exactly where it matters: if IS adds beat
the momentum-matched null, that's the first flow-based survivor
candidate of the project.

## Amendments

None after this commit. Failed variants stay dead.
