# v4 after-tax accounting audit — pre-registration (2026-07-14)

## Why

Every edge number we publish is pre-tax. But v4's monthly churn makes
almost every realized gain SHORT-term (Indian STCG: 20% for holdings
≤12 months), while its benchmark — buy-and-hold Nifty — pays only
12.5% LTCG, once, at the end. The tax asymmetry systematically favors
the benchmark, and nobody's backtest models it. Before real money, we
measure what the edge is worth AFTER the tax office visits.

This is ACCOUNTING on the frozen incumbent — no strategy parameter
changes, no gate changes (PROTOCOL_GOLIVE's gates are already locked).
Results feed expectations and the (private) sizing conversation only.

## Tax model (frozen; India FY Apr–Mar, rates as of FY 2025-26)

- STCG 20% on net short-term gains (holding ≤ 365 days).
- LTCG 12.5% on net long-term gains (> 365 days). The ₹1.25L annual
  LTCG exemption is IGNORED (conservative for the strategy, which
  realizes mostly STCG anyway; disclosed).
- Loss offsets per law: short-term losses offset ST then LT gains;
  long-term losses offset LT gains only. Net losses carry forward
  across FYs within the window.
- STT/brokerage/slippage: already inside the engine's 0.25%/side.
- Tax is charged at each FY end as a proportional equity haircut
  (taxes due / portfolio value).

## Method (frozen)

- Holdings timeline: run the v4 engine (verbatim settings: top-20,
  skip 21, regime filter, 0.25%/side) with a recording select_fn that
  logs each month's names; engine equity is the pre-tax base.
- Lots: a name entering the list opens a lot at the entry month's fill
  (next open after formation, +0.25%); leaving the list closes it at
  the exit month-end close (−0.25%). Continuing names are not traded
  (matches the engine's churn-cost assumption). Regime-off flattens all
  lots. Open lots at window end are marked, not taxed (disclosed).
- After-tax equity = engine equity with each FY-end haircut applied,
  where FY taxes come from the lot ledger scaled to the equity path.
- Benchmark: NIFTYBEES bought at window start; 12.5% LTCG applied to
  the terminal gain.
- Windows: v4's registered pair — IS 2023-01→present, OOS 2017-01→
  2022-12 — using the same panel builders as the committed v4 runner.

## Outputs

Per window: pre-tax edge (must reconcile with the scoreboard's numbers
— sanity), after-tax strategy total, after-tax benchmark total,
after-tax edge, and tax drag in pp/yr.

## Registered prediction

Tax drag on v4 lands in the 2–5 pp/yr range and the edge SURVIVES in
both windows (pre-tax edges are +100/+116pt over multi-year windows).
If the edge does NOT survive taxes, that is a published finding and a
mandatory input to the sizing conversation — but per the frozen gates
it does not, by itself, block the October go/no-go.

## Amendments

None after this commit.
