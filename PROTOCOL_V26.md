# v26: hysteresis execution for v4 (after-tax re-registration) — frozen 2026-07-14, runs no earlier than 2027-07-01

## Provenance (why this is registered years early)

v24 (the stranger's algorithm) demonstrated hold-till-top-40 hysteresis
is a genuinely good anti-churn idea (its OOS edge was +23 WITH
hysteresis vs -4 without). Applying it to v4 was parked because both
backtest windows are spent — v24's runs exposed them for this idea.
The 2026-07-14 tax audit (PROTOCOL_TAX) then quantified v4's churn cost
at ~6pp/yr of tax drag (0 of 308 IS lots held past 12 months → all
STCG at 20%). Hysteresis attacks that drag MECHANICALLY — fewer taxable
events, more lots crossing into the 12.5% LTCG band — which upgrades
its prior without touching contaminated windows. This protocol freezes
everything now so no future session can tune it after watching v4 live.

## Spec (frozen)

- v26 = v4 verbatim (top-20 by 12-1, monthly, regime circuit-breaker,
  0.25%/side) with ONE change: a held stock exits only when it falls
  below momentum rank 40 (v24's hysteresis band, not re-tuned); its
  replacement is the highest-ranked non-held stock.
- No other variants. The band (40) is fixed by v24's precedent — a
  grid over bands would be tuning; refused.

## Run gate (frozen)

- Earliest run: 2027-07-01. Test window: 2026-07-01 → run date
  (≥ 12 fresh months, untouched by any prior study — the paper-trial
  era). A second confirmation run on 2026-07→2028-06 follows in 2028
  if the first passes.
- Comparator: v4 verbatim on the identical window and panel.

## Pass criteria (frozen; decision metric is AFTER-TAX)

1. AFTER-TAX edge vs Nifty (PROTOCOL_TAX machinery, same tax model)
   must exceed v4's after-tax edge on the same window.
2. Mechanical sanity: realized churn reduction ≥ 25% vs v4 (else the
   idea isn't doing what it claims and a win is luck).
3. Pre-tax edge must not degrade by more than 2pp/yr vs v4 (the tax
   saving must not be purchased with signal decay).
4. Incumbent wins ties, as always. A pass earns v26 its own paper
   phase — it does NOT inherit v4's live status.

## Registered prediction

Passes 2 easily; the fight is between 1 and 3 — hysteresis holds
losers longer, and whether tax savings outrun momentum-purity loss is
genuinely unknown. No confident directional prior.

## Amendments

None after this commit. If v4 is not live or the paper trail broke,
the window shifts accordingly but criteria never do.
