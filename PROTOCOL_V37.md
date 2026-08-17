# v37: India insider purchases re-test — frozen 2026-08-18, gated on fresh events

Provenance: v21 found real pre-2023 drift, dead in 2023-26; windows
spent. This freezes the re-test on events that DO NOT EXIST YET.

Spec (frozen): v21 baseline verbatim (promoter/director market
purchases ≥₹25L, PIT feed, entry next open after broadcast, hold 63d,
gap 63d, two nulls incl. random-announcement seed 7 — the committed
pit_study code unchanged).

Run gate: when ≥300 qualifying events with broadcast AFTER 2026-08-18
have accumulated (est. ~2028), and no earlier than 2027-07-01.
Pass: identical to v21's original bars (mean ≥ +3pp over null, median
above, n≥100 evaluated on fresh events only) + the v27.2 lottery check
(v21's original sin was lottery-shaped payoffs). Prediction: fails —
decayed edges have never returned anywhere in this project.
Amendments: none after commit.
