# v21: India insider (PIT) market purchases — pre-registration
# v22: announcement-based risk screens — pre-registration

Committed BEFORE either dataset's outcomes are computed.

## v21 — the India version of the insider test

US insider clusters (v9) worked until tracking apps commoditized them
(~2023). India's PIT disclosures are the same legal footprint, less
app-saturated. Data: NSE corporates-pit API, 2017→present.

Event (frozen): person category contains Promoter OR Director, acquisition
mode is a MARKET purchase (not ESOP/gift/allotment), disclosed value
≥ ₹25 lakh; event date = broadcast timestamp; entry next session's open;
hold 63 sessions; liquid non-ETF universe; one event per symbol per hold.
Grid: cluster (≥2 distinct insiders/21d) · value ≥ ₹1cr · hold {21, 126}
· promoters-only.
Two nulls: NIFTYBEES + all-PIT-disclosure baseline (including sells and
ESOPs) per the two-null rule. Windows: IS 2023-26 · OOS 2018-22.
Pass: standard event bar (IS mean AND median > 0 net of 0.5% RT vs both
nulls; grid majority; OOS single shot; quarter concentration ≤ 30%).

## v22 — risk screens from the full announcements taxonomy

Re-fetch of all announcements keeping category (and a text snippet for
director/auditor/rating categories). Two pre-registered event types,
EXPECTED NEGATIVE (these are avoid-signals):
- credit-rating downgrade mentions
- auditor resignation / abrupt CFO exit mentions
Study: 63-session forward excess distribution; if mean/median are
materially negative (< -2% vs both nulls) in BOTH windows, the screen
qualifies as a v4 EXCLUSION FILTER — then tested as v4-challenger
(v4 + screen vs v4, standard incumbent rules). A screen that doesn't
show negative forward returns is dead — no rescue as a long signal.
