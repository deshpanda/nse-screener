# v35: 52-week-high proximity — frozen 2026-08-18, runs ≥2027-07-01

Provenance: George-Hwang anchoring; never tested here. Momentum-FAMILY
— all historical windows spent by v4's line, so this waits for fresh
data. Registered now to lock the spec.

Spec (frozen): monthly, liquid (≥₹5cr) non-ETF stocks; rank by
close / trailing-252d high; hold top-20 EW; fills next open;
0.25%/side; regime filter OFF (the paper's spec) plus a breaker
diagnostic. No other variants.

Window: 2026-07-01 → run date (≥12 fresh months). Pass: beats index on
the fresh window; then incumbent rule vs v4 same window. Confirmation
run to 2028-06 before any promotion. Prediction: positive vs index,
loses to v4 (a cousin, not an improvement — the literature's Sharpe
gains came from crash-neutralization our breaker already provides).
Amendments: none after commit.
