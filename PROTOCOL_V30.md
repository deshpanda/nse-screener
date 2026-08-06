# v30: the overnight anomaly ("the market works at night") — pre-registration (2026-08-06)

## Provenance

A viral chart (found in the wild, 2026-08-06): Nifty50 Jan-2000→Jul-2026
decomposed into overnight (close→next open, +9,935%) vs intraday
(open→close, −84%). The phenomenon is documented in academic literature
since ~2008 (US) and the motivating evidence is already public — v24
pattern: the claim arrives pre-peeked, so the registration freezes OUR
replication windows, cost model, and pass bar before we compute anything.

## Cells (frozen — this is the entire grid)

- **C1 decomposition, NIFTYBEES**: cumulative gross overnight vs
  intraday vs buy-and-hold, on our CA-adjusted daily panel (2016→).
  Replication check only: does overnight >> intraday, intraday ≲ 0?
- **C2 decomposition, breadth**: same split on the equal-weight liquid
  (≥₹5cr) non-ETF stock panel — index quirk or market-wide?
- **C3 the tradable version, NIFTYBEES**: buy every close, sell every
  next open. Net of round-trip cost tiers: 0.50% (our standard
  0.25%/side), 0.10%, 0.05%, 0.02%. One trade pair per trading day;
  no leverage; no shorting of the intraday leg (owner excludes F&O,
  and cash equities cannot short overnight the other way).

## Windows (frozen)

IS 2023-01→2027-01 and OOS 2016-01→2022-12 (single shot) for verdicts;
full-period 2016→present additionally shown for the decomposition
charts. Benchmark: buy-and-hold NIFTYBEES.

## Pass criteria (frozen)

- C1/C2 are descriptive (no pass/fail — they answer "is the chart
  real on our data").
- C3 PASSES only if net total beats buy-and-hold in BOTH windows at
  the **0.05% round-trip tier or worse** — the best cost a disciplined
  retail account can plausibly claim once STT, stamp duty, slippage
  and the opening-auction reality are counted. Cheaper tiers are
  diagnostics (institutional curiosities), never a pass.
- Tax reality is reported alongside (every gain is short-term /
  business income) but the cost gate above already decides.

## Registered predictions

C1 and C2 replicate the qualitative claim (the anomaly is real and
market-wide). C3 DIES at 0.50% and 0.10%; dies or is marginal at
0.05%; may show life at 0.02% — which no retail account gets. Summary
prediction: the chart is true and the trade is not, because here
friction is the wall rather than the moat. If C3 instead passes at
0.05%, that is a genuine surprise and gets the full v27.2-style
concentration + plateau treatment before anything further.

## Amendments

None after this commit. Failed cells stay dead.
