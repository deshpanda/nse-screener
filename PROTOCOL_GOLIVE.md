# Go-live decision framework — pre-registration (2026-07-13)

Frozen BEFORE paper entry #2 exists (log has only the 2026-07-08 seed).
On 2026-10-15 this document decides; nobody re-argues it on the day.
The whole point: three months from now the paper numbers will tempt us —
a great quarter will whisper "size up, add sleeves", a bad one "delay,
tweak". Both whispers are noise. The decision is behavioral, not
performance-based, and it is written down while we cannot know which
whisper we'll hear.

## Inputs (all mechanical, no judgment)

Run on 2026-10-15:

    .venv/bin/python -m scripts.golive_review

which evaluates the gates below from paper/log.csv, the price panel,
health.log, and git history of paper/. Its printed verdict is the
decision.

## GATE 1 — operational integrity (did the machine run itself?)

- Paper log contains the month-end entries for Jul, Aug and Sep 2026
  (plus the Jul-08 seed), each committed to git within 3 calendar days
  of its formation date (git author date = proof; manual backfill of a
  missed month = FAIL).
- health.log shows no unexplained FAIL lines in the window.
- `scripts.reconcile_paper` is CLEAN, or every DRIFT line is explained
  in writing in STATE.md as a rename / corporate-action re-adjustment.
  Any unexplained drift = FAIL.

## GATE 2 — behavioral fidelity (did paper match simulation?)

- Regime call and name list of every entry reproduce from the current
  panel (this is reconcile_paper again — names are the invariant).
- Fill-assumption gap: for each invested sleeve-month, the paper return
  (logged prices → next entry's logged prices, equal weight) and the
  sim-style return (next-open after formation → next-open after next
  formation, equal weight, 0.25% cost per side on turnover) must agree
  within **1.0 percentage point absolute**. A month outside tolerance =
  FAIL unless traced to a specific corporate action and documented.
- Months where a sleeve is 100% cash trivially pass (nothing to fill).

## GATE 3 — v13.1 combo qualification (per PROTOCOL_V13.1, edges frozen)

- Realized correlation between sleeve A (v4) and sleeve B (low-vol):
  daily equal-weight returns of each sleeve's logged holdings between
  rebalances, computed ONLY over days where BOTH sleeves are invested.
- Requires **≥ 30 such overlapping invested days** in the paper window.
  Fewer (e.g. v4 stayed in cash — plausible given regime is OFF today):
  combo decision is DEFERRED to a later monthly review once 30 days
  accumulate; it does NOT block v4 going live alone, and deferral does
  not expire the combo candidacy.
- If measured: corr < 0.6 AND both sleeves individually passed Gate 2
  ⇒ combo confirmed at 70/30 per PROTOCOL_V13.1. corr ≥ 0.6 ⇒ combo
  DEAD, pure v4 stands, no re-test with the same paper window.

## What is explicitly NOT a gate

- **Returns.** Three months of monthly-rebalance returns is ~3 data
  points; no P&L number, good or bad, changes the decision. The sizing
  evidence remains the backtest (IS +100 / OOS +116, DSR 0.995, known
  cost: 1-in-4 24-month windows lose to Nifty, worst -50pt).
- **Any intervening research.** No sleeve not named here goes live in
  2026 regardless of what any new study shows (new candidates take the
  full gauntlet + their own paper phase).
- **The regime state on decision day.** If regime is OFF on Oct 15, a
  GO decision still arms the system — live means the machine trades the
  signal from now on, and the signal may say cash.

## Decision table (exhaustive)

| Gates 1+2 | Gate 3 | Action from Oct 31 rebalance onward |
|---|---|---|
| pass | corr measured, < 0.6 | LIVE: 70/30 v4/low-vol per v13.1 |
| pass | corr measured, ≥ 0.6 | LIVE: pure v4; combo dead |
| pass | deferred (<30 days) | LIVE: pure v4; combo stays candidate |
| any FAIL | — | NOT live. Fix the specific cause, extend paper by 2 more clean month-ends, re-run this protocol verbatim. **No parameter, universe or code-logic changes to the strategy are permitted during the extension** — only infrastructure fixes. |

## Sizing (ordering rule)

Sizing is decided AFTER and independently of the go/no-go, in a private
conversation (not a repo topic). One constraint is public and binding:
size such that total loss of the deployed amount is survivable. Sizing
pressure can never flip a FAIL into a GO.

## Amendments

None permitted after 2026-07-31 (first automatic entry). Before that,
amendments require a git commit explaining why the change couldn't have
waited for fresh data. After Oct 15 the protocol is spent — a future
go-live re-attempt gets a new protocol file.
