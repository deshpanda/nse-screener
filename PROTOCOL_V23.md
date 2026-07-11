# v23: Futures open-interest signals — pre-registration

Committed BEFORE the futures backfill completes (data still downloading;
no outcome computable yet). F&O data as INFORMATION only per owner's rule.

## Two pre-registered hypotheses (from STATE priors, sketched before data)

A. **OI-confirmation overlay on v4**: at month-end, within v4's top-40
   momentum pool, prefer the 20 with highest 21-session growth in
   near-month futures OI ("long buildup": price up + positions building).
   Universe shrinks to F&O stocks (~180-220 names) — DISCLOSED: this
   changes the pool vs v4; the fair incumbent is v4 RESTRICTED to F&O
   names, reported alongside standard v4.
B. **Basis as crowding gauge**: near-month futures premium (basis =
   fut/spot - 1) z-scored per stock; AVOID entering names in their top
   basis decile (crowded longs). Tested as exclusion on v4-F&O.

## Bar: v4.1 challenger criteria vs the F&O-restricted incumbent, both
windows (IS 2023-26, OOS 2017-22), incumbent wins ties. Grid: OI growth
window {10, 42} · prefer LOW OI-growth (contrarian) · basis decile {top 2}.
