# v29.1: v4 + GARP combo sleeve — pre-registration (2026-07-17, with disclosure)

## Disclosure first (contaminated evidence, stated plainly)

The motivating facts were observed AFTER both backtest windows were
spent: v29-India passed the index gate, and its correlation to v4
(0.54 IS / 0.39 OOS) is the lowest of any gate-passer. A single
declared-weight diagnostic (70/30, mirroring v13.1's convention — ONE
weight, computed once, no grid) was then run, also contaminated:
- IS 2023-26: combo Sharpe 1.29 vs v4's 1.21; total +122.2% vs
  +132.1%; maxDD −14.1% vs −11.9%.
- OOS 2019H2-22: Sharpe 1.63 vs 1.63; total +154.3% vs +185.9%;
  maxDD −11.4% vs −13.5%.
Honest summary: the combo buys SMOOTHNESS, not return — a weaker
motivating picture than v13.1's. Both windows are dead for this
hypothesis; confirmation can come only from the future.

## Spec (frozen)

- Sleeve A: v4-regime verbatim (incumbent, unchanged).
- Sleeve C: v29 India GARP primary verbatim (PE<25, TTM growth>15%,
  PEG<2, mcap>₹5,000cr, ≤40 names by lowest PEG, equal weight,
  monthly, NO regime — always invested when qualifiers exist).
- Combo: 70% A / 30% C, rebalanced to weights monthly. No other
  weights may ever be evaluated on the spent windows.

## Paper logging (machinery, from the next month-end)

`screener/paper_log.py` also logs sleeve C monthly to `paper/garp.csv`
(separate file — `paper/log.csv`'s schema and the golive machinery
stay untouched). Same append-only, same-push discipline. Failures of
the GARP hook must never block the main log (best-effort, logged).

## Confirmation standard (future data only)

At a review NO EARLIER than 2027-04-01 and after ≥ 6 logged month-ends
of sleeve C:
1. Behavioral fidelity: every logged C entry's names reproduce from
   the panel (reconcile-style), and paper-vs-sim fill gap ≤ 1.0pp per
   invested month (PROTOCOL_GOLIVE gate-2 tolerance).
2. Realized daily corr(A, C) < 0.6 over ≥ 30 overlapping invested
   days (days A is in cash don't count — same rule as gate 3).
3. Realized combo Sharpe (70/30, from logged sleeves) ≥ realized v4
   Sharpe over the same window — the smoothness claim must show up in
   data that didn't exist today.
All three pass ⇒ combo becomes a go-live-review agenda item alongside
v13.1 (which retains seniority; any three-sleeve question is a NEW
protocol). Any fail ⇒ pure v4 stands; no re-weighting rescue.
Explicitly: this combo CANNOT enter the 2026 go-live under
PROTOCOL_GOLIVE's no-new-sleeves rule.

## Registered prediction

Corr stays < 0.6 live (structural: value vs momentum). The Sharpe
condition is a genuine coin flip — which is the point of paper.

## Amendments

None after this commit.
