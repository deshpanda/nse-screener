# RUNBOOK — operating this project as a human

Written so a person with basic Python and no AI assistant can run,
check, and extend everything. Read STATE.md for WHAT is true;
this file is HOW to operate it.

## The three repos

| repo | visibility | role |
|---|---|---|
| nse-screener (this) | public | research: data pipelines, backtests, verdicts, the site |
| [nse-screener-data](https://github.com/deshpanda/nse-screener-data) | public | full datasets (~400MB) with a beginner guide |
| trading-live | PRIVATE | execution layer; consumes this repo's signals (see its SETUP.md) |

## What runs automatically (user's crontab, IST)

- **19:30 Mon–Fri**: `daily.py` (data pull, self-heals a trailing week,
  refreshes corporate actions, publishes regime flips) then
  `screener.screen` (daily shortlist). Log: `cron.log`.
- **23:00 last day of month**: `screener.paper_log` — appends the
  month-end paper decision (BOTH sleeves), captures a pledge snapshot,
  auto-commits + pushes `paper/` so the public site updates itself.
  Log: `paper/cron.log`.
- **Every 4h (:15, 8–23)**: `scripts/health.py` watchdog — SILENT when
  healthy (one line in `health.log`), macOS notification when data goes
  stale, a cron dies, a month-end snapshot is missed, or git push breaks.

**If the laptop slept through something**: run `python daily.py`
(heals data) or `python -m screener.paper_log` (heals a missed
month-end, correct as long as run before the next evening's pull).

## Routine rituals

- **Month-end +1 morning** (~10 min): open `paper/log.csv` (or the
  site's Live Trial section) — confirm the new row exists and looks
  sane. That's the entire job.
- **Quarterly**: skim `health.log` for FAIL lines; `git log` in the
  data repo to confirm syncs; run the test suite:
  `.venv/bin/python -m unittest discover tests`

## Running any study yourself

Every verdict's exact code is committed. Engines:
- `python -m backtest.run --strategy v2|v3|v5 [--start] [--end]` (daily engine)
- `python -m backtest.monthly` (v4 family), `python -m backtest.validate`
  (deflated Sharpe / PBO / rolling consistency)
- `python -m backtest.runners v41|v14|v16|v19|v13q|v201|v24` (one-off studies)
- Event studies: `backtest/pead.py`, `pit_study.py`, `events17.py`,
  `smartbuyer.py`, `oi_study.py`, `ratings_cert.py`; US: `us/*.py`

## Adding a NEW strategy (the law)

1. Write `PROTOCOL_V<n>.md`: spec, windows (IS 2023→, OOS earlier),
   grid, pass criteria. COMMIT IT before computing any result.
2. Implement as a committed script. Run IS → grid → OOS once.
3. Judge by the pre-registered criteria only. Mixed result = incumbent
   wins. Never promote a lucky grid cell (see PBO 0.48 in STATE).
4. Same day: scoreboard row + Season-2-row (+ chapter if novel lesson)
   on the site; STATE.md row; links to protocol + code. Counts on the
   page must machine-match the table.
5. New dataset? Ingest module with documented quirks + data-section row
   + entry in STATE §5 + sync to the data repo (`scripts/sync_data_repo.sh`).

## Recovery cheat-sheet

| symptom | fix |
|---|---|
| Panel hole (>10d guard trips) | `python backfill.py --start <gap start>` |
| NSE 403s | raise SLEEP_SECS in config.py; retry at night |
| CA feed missed a split (fake -90% day) | it's auto-detected (implied_splits); verify data/implied_splits.csv |
| Renamed ticker looks delisted | `python -m ingest.renames` (refresh map) |
| Site stale vs verdicts | follow CLAUDE-independent rules in this file §"Adding" |
| paper push failed (offline) | next month-end push carries it; or `git push` manually |

## Go-live (October) — the sequence

Paper ≥3 clean month-ends → review vs simulation → private sizing
decision → trading-live SETUP.md (Kite app, .env) → propose-mode cycle
→ only then TRADING_MODE=live. The gate order is not negotiable.

The "review vs simulation" step is a script, not a vibe:

    .venv/bin/python -m scripts.reconcile_paper   # every log entry must
                                                  # recompute to the same
                                                  # regime + names today
    .venv/bin/python -m screener.paper_log --report   # paper P&L vs Nifty

Both clean ⇒ the paper numbers can be trusted for the go/no-go call.
Any DRIFT line must be explained (rename? data revision? code change?)
before proceeding. The execution pipeline itself was drilled 2026-07-13
(7 scenarios incl. partial fills, cash flips, undersized capital — see
trading-live git log); re-run a propose-mode `cli.py rebalance` on
go-live morning before arming anything.
