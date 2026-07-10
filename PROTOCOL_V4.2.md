# v4.2: rebalance-cadence sweep — pre-registration

Committed BEFORE the first run. The Author asked the right question: the
grids never tested v4's REVIEW frequency (monthly). One pre-registered
sweep, then done — this is a robustness probe, not a tuning session.

## Spec (frozen)

v4-regime verbatim except formation every k trading sessions,
k ∈ {5, 10, 21, 42, 63} (≈ weekly, fortnightly, monthly, bimonthly,
quarterly). Costs 0.25%/side on churn as always — higher cadence must
pay its own turnover. Incumbent reference: true month-end v4-regime.

## Windows: IS 2023→present · OOS 2017–2022

## Decision rule

A cadence replaces monthly ONLY if it beats the incumbent on Sharpe AND
maxDD AND edge in BOTH windows (the v4.1 bar). Expected outcome per
literature: a plateau across 10–63 sessions (the 12-1 signal decays over
months, so review frequency shouldn't matter much) with weekly hurt by
costs. If instead results swing wildly with k, that's evidence v4 is
more fragile than believed — worth knowing either way.
