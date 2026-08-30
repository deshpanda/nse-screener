# v42: factor attribution — is v4's edge alpha, or beta + size? — pre-registration (2026-08-28)

## Why

Every number we publish for v4 (+100 IS, +116 OOS, +54/+63 after tax) is
RAW total return versus the index. That measurement cannot separate
skill from systematic risk exposure anyone can buy cheaply. v4 holds
momentum midcaps, so it plausibly carries a size tilt and non-unit beta.
Jensen (1968) defines alpha as the regression intercept AFTER removing
factor exposure; Fama-French (1992) says the exposures that matter are
market, size and value. We have never run that regression.

This is an AUDIT on the frozen incumbent, like PROTOCOL_TAX and the leak
test. It cannot promote or demote anything, and it changes no gate. It
answers one question: what fraction of the edge is factor exposure?

## THE INDIA LIMITATION, stated up front

We cannot build a value (HML) factor for India. Our XBRL store holds
net_profit / eps / revenue only — Indian quarterly filings carry no
balance sheet, so book-to-market is not computable. The India arm is
therefore MARKET + SIZE only, and its alpha is an estimate with a known
missing regressor. **Arm B exists to bound that error**, not merely to
repeat the exercise where data is better.

## Arm A — India (the subject)

- Dependent: v4 monthly returns from the committed runner
  (`monthly.simulate(regime_filter=True)`), verbatim.
- Market: NIFTYBEES monthly return. Risk-free: constant 6%/yr, FROZEN
  (LIQUIDBEES price returns understate cash yield — its distributions
  arrive as bonus units, a trap documented in v33). Sensitivity at 4%
  and 8% reported.
- SMB proxy, frozen construction: at each month-end, from
  `constituents_synth.parquet` free-float mcap ranks among liquid
  non-ETF names — SMALL = ranks 201-500 equal weight, BIG = ranks 1-100
  equal weight, SMB = SMALL − BIG.
- Cells: **A1** CAPM (market only); **A2** two-factor (market + SMB).
  Report annualized alpha, betas, t-stats, R², over the full panel and
  over v4's registered IS and OOS windows separately.

## Arm B — US (the calibration, and the point of doing it)

Ken French's survivorship-clean monthly data only — NOT our own US
panel, which is survivor-only (disqualified for the same reason as in
PROTOCOL_V41.1).
- Dependent: the momentum WINNER decile ("Hi PRIOR", value-weighted)
  from `10_Portfolios_Prior_12_2`, already cached.
- Factors: Mkt-RF, SMB, HML from the F-F 3-factor file, already cached.
- Cells: **B1** CAPM; **B2** market + SMB (deliberately mirroring
  India's handicap); **B3** market + SMB + HML (the full model).
- **KEY OUTPUT: (B2 alpha − B3 alpha) = the bias introduced by omitting
  the value factor.** That number is the honest error bar to attach to
  Arm A's alpha. Eras as in v41.1: 1926-84, 1985-99, 2000-14,
  2015-present, plus full sample.

## What follows from the result (no promotion either way)

- If A2 alpha stays positive with t > 2, the edge is not merely factor
  exposure, and the site says so with the number.
- If A2 alpha collapses toward zero, then a large share of what we have
  been calling an edge is buyable from a cheap small-cap index fund —
  that must be published, and must enter the private sizing
  conversation, even though it changes no October gate.
- Either way, Arm A's alpha is reported WITH Arm B's omitted-value bias
  as its stated uncertainty.

## Registered predictions

1. v4's beta lands BELOW 1 (0.7-0.95) — the circuit-breaker sits in
   cash for whole months, which drags market exposure down.
2. Large, obvious positive SMB loading (v4 is a midcap strategy).
3. A2 alpha shrinks materially versus the raw edge but stays positive.
4. Arm B: momentum loads NEGATIVELY on HML (winners are growth-like),
   so omitting HML UNDERSTATES alpha — meaning Arm A's India number is
   likely conservative, not flattering. If that sign is wrong, the
   India estimate is optimistic and must be labelled as such.
5. Arm B alpha decays across eras, like everything else we have
   measured.

## Amendments
None after this commit.
