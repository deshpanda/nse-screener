# v34: FIP smoothness re-registration — frozen 2026-08-18, runs ≥2027-07-01

Provenance: FIP (frog-in-the-pan) showed promise OOS but failed IS in
the original v4.1-era grid; all historical windows are SPENT. This
freezes the re-test years early so nobody tunes after watching 2026-27.

Spec (frozen): v4 verbatim except selection = among the top-40 by 12-1
momentum, pick the 20 with the SMOOTHEST path (highest fraction of
positive days over the formation window — the fip_pool=40 variant
exactly as originally coded in backtest/monthly.py; no new knobs).

Window: 2026-07-01 → run date (≥12 fresh months; the paper-trial era).
Comparator: v4 verbatim, identical window/panel.
Pass: beats BOTH the index and v4 on total return AND Sharpe on the
fresh window; incumbent wins ties. Confirmation run on 2026-07→2028-06
required before challenger status. Prediction: fails vs v4 (the IS
failure was likely the true signal). Amendments: none after commit.
