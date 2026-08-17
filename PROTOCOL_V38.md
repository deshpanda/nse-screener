# v38: rating upgrade-drift — frozen 2026-08-18, gated on fresh events

Provenance: upgrade-drift was flagged during the v22 ratings work but
never cleanly tested (the era's events are spent/contaminated by the
v22 arc). Frozen now, tested on future upgrades only.

Spec (frozen): PDF-verified rating UPGRADES (ingest/ratings.py
direction engine, liquid universe), entry next open after the
announcement, holds 63d and 126d (both registered now), gap 126d,
two nulls (random-announcement seed 7 + all-ratings-events null).

Run gate: ≥150 PDF-verified upgrade events dated after 2026-08-18
(requires re-running the ratings pipeline forward; est. 2028), and no
earlier than 2027-07-01. Pass: v25-style bars (mean ≥ +3pp over both
nulls, medians above, n≥100) + lottery check. Prediction: small
positive that fails the bar — upgrades are the most publicized rating
events and the family record is 0-for-7.
Amendments: none after commit.
