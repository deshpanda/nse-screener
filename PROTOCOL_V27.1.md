# v27.1: index-inclusion flows, re-tested on REAL announcements — pre-registration (2026-07-14)

## Provenance & contamination disclosure (read first)

v27 tested this hypothesis on synthetic monthly rank-crossings and DIED
on the frozen n≥30 floor (9-17 IS events). Its refused point estimates
were POSITIVE (+10 to +17pp) — we have seen that, and we register this
re-test knowing it. Precedent: v22 → v22.1 (keyword events → verified
events, same windows) — which famously RETRACTED the earlier signal.
The discipline cuts both ways and we accept either outcome. One cell
below is genuinely virgin: the announce→effective window, which monthly
synthetic ranks were structurally blind to.

## Data (frozen)

`data/reconstitution/events.parquet` — 17,590 add/drop events parsed
from 1,115 NSE Indices press releases (parse committed 81a85dd BEFORE
this protocol ran; sanity: UPL/SHRIRAMFIN 2024 and HINDPETRO/BRITANNIA
2019 verified; 95.1% have effective dates; announce→effective median
25 days). Symbols come from the PDFs' own symbol column.

## Test indices (frozen — chosen for tracker-money size, before results)

Nifty 50, Nifty Next 50, Nifty 100, Nifty 500, Nifty Midcap 150.
Reported per index AND pooled (dedupe by announce+symbol+action,
attributing to the largest index). No other indices may be promoted to
"tested" after the fact — the thematic/strategy indices in the file
are out of scope (no meaningful tracker flows).

## Design (frozen)

- Entry: next open after ANNOUNCE date (first tradable moment).
- Exit cells: (E) close of EFFECTIVE date — the flow window, the
  virgin cell (events lacking an effective date are excluded from E,
  disclosed); (F63) fixed 63-day hold; (F21) fixed 21-day hold.
- Adds = long candidates. Drops = risk screen (mirror expectations).
- Engine: events17-style next-open entry, excess vs NIFTYBEES,
  liquidity ≥ ₹5cr at entry. gap_days=0 across indices (an event IS
  the unit), dedupe within the pooled cell as above.
- Two nulls, run through the identical engine as same-day pseudo-events:
  1. random liquid stocks (market/activity baseline; seed 7);
  2. momentum-matched — same 12-1 momentum decile, liquid, same day
     (the null that separates flow from "recent winner").

## Windows (frozen)

IS 2023-01→2027-01 (decision). OOS 2016-01→2023-01 (single shot).

## Pass criteria (frozen — identical to v27, no softening)

- Adds: PASS only if IS mean excess ≥ +3pp above BOTH nulls AND median
  above both null medians AND n ≥ 30, per cell per index (or pooled).
- Drops: screen CONFIRMED only if IS mean ≤ −3pp below both, n ≥ 30.
- A pass is CONFIRMATORY-ONLY: it earns the standard gauntlet
  (sensitivity, OOS consistency, DSR) + its own paper phase. Nothing
  goes live in 2026 regardless (PROTOCOL_GOLIVE).

## Registered predictions

- (E) announce→effective adds: positive in BOTH windows — mechanical
  tracker demand is the least-arbitragable effect we have ever tested,
  strongest away from the mega-caps (500/Midcap150 > 50).
- (F63) post-effective drift: ≈ 0 or negative IS (the US pattern: pop,
  then fade once the forced buying is done).
- Drops: negative in E, decaying like everything else in IS.

## Amendments

None after this commit. Failed cells stay dead.
