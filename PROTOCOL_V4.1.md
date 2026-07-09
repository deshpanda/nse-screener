# v4.1: Risk-managed momentum — pre-registration

Committed BEFORE the first run. v4-regime (PROTOCOL_V4.md) passed and is
in paper phase; v4.1 tests two literature-standard refinements. The bar is
NOT "beat Nifty" — it is "beat v4-regime," and specifically on risk.

## Refinements (frozen)

1. Volatility scaling (Barroso–Santa-Clara): at each formation date,
   compute annualized vol of an equal-weight portfolio of the SELECTED
   names over the trailing 63 sessions (point-in-time). Exposure =
   min(1, 15% / vol); remainder in cash. No leverage.
2. FIP smoothness (Da–Gurun–Warachka): rank the top 40 by 12-1 momentum,
   keep the 20 smoothest — lowest ID = sign(12-1 return) ×
   (%down days − %up days) over the formation year. Gap-jumpers out,
   grinders in.

Variants: v4.1-vol (1 only) · v4.1-fip (2 only) · v4.1-full (both).
Everything else is v4-regime verbatim: top-20 eq-weight, monthly, 12-1,
₹5cr floor, regime→cash, next-open fills, 0.25%/side on churn.

## Windows

Same as v4: in-sample 2023→present, out-of-sample 2017–2022.

## Pass criteria — a variant replaces v4 only if, in BOTH windows:

1. Edge vs Nifty positive (unchanged gate)
2. Sharpe (monthly returns, annualized) ≥ v4-regime's
3. Max drawdown ≤ v4-regime's
4. Robustness: grid (vol target {12%, 20%}, vol lookback {42, 126},
   FIP pool {60}) — majority of perturbations keep Sharpe ≥ v4-regime

If no variant passes all four, v4 stands and v4.1 is recorded as a dead
refinement. Ties/mixed results default to v4 (incumbent wins — fewer
moving parts).
