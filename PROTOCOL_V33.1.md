# v33.1: confirmation gauntlet for dual momentum's surprise pass (2026-08-18)

v33 PRIMARY passed the gate in both windows against the registered
prediction (miss printed). Per PROTOCOL_V33, a surprise pass earns the
v27.2 treatment before anything further. Known concerns to test, stated
before running: the D2 diagnostic shows GOLD is the entire engine, and
the OOS margin is +7.3pt over 15 years — thin.

## Stage A (frozen, run now)

Perturbations (each keeps edge-vs-NIFTYBEES > 0 in its window to count):
1. lookback 9m (full both-windows)      2. lookback 15m (same)
3. formation 3 trading days EARLY        4. formation 3 days LATE
5. cost 0.50%/side                       6. cash leg +5%/yr (D1)
7. OOS halves: 2008-2014                 8. OOS half: 2015-2022
A1 plateau: ≥6 of 8 stay positive.
A2 lottery (v21/v27.2 detector): quarterly excess vs NIFTYBEES; best
positive quarter < 40% of summed positive quarterly excess, per window.
A3 after-tax: realized gains at switches taxed (20% if held ≤365d,
12.5% else); benchmark taxed 12.5% at horizon end. After-tax totals
must still beat the benchmark in BOTH windows.

Any Stage-A failure ⇒ v33 downgraded to DEAD (spike/fragile), printed.

## Stage B (if A passes)

Paper phase: v33's monthly pick logged from the next month-end
(machinery: paper/dualmom.csv, same discipline as garp.csv). Review
≥ 2027-04 with ≥6 logged months: behavioral fidelity + realized
tracking. v33 CANNOT enter the 2026 go-live (PROTOCOL_GOLIVE).
It is an ALLOCATION strategy — if confirmed it competes for the
cash/ballast role, not v4's equity sleeve.

## Registered prediction
A1 passes (GEM is famously parameter-insensitive); A2 is the real
threat (gold-dependency smells like concentration); A3 passes (long
holds → LTCG). Net: coin flip on A2.

## Amendments
None after this commit.
