# nse-screener

Systematic-trading research platform for Indian (NSE) and US equities:
EOD data pipelines, pre-registered backtests, and a validation harness
(walk-forward consistency, deflated Sharpe, PBO). Every strategy verdict
is git-timestamped: protocol committed before the first run, no post-hoc
parameter rescue.

**Operating manual → [RUNBOOK.md](RUNBOOK.md)** — run everything without an AI assistant.

**Start here → [STATE.md](STATE.md)** — the single source of truth:
full scoreboard (27 strategies tested, 26 dead, 1 in paper trial),
method rules, data traps, pending decisions.

**The story, interactive →** https://deshpanda.github.io/nse-screener/
(every chart runs on the real backtest data; the live paper-trial
section reads `paper/log.csv` straight from this repo).

**The full datasets →** https://github.com/deshpanda/nse-screener-data
(~400MB of panels with a beginner-friendly guide to what each dataset
is; small derived files remain in this repo under `data/`).

## The one survivor

v4: top-20 by 12-1 momentum among liquid NSE stocks, equal weight,
monthly rebalance, 100% cash when Nifty < its 200-DMA. IS +100pt /
OOS +116pt vs Nifty after costs; deflated Sharpe 0.995 at 40-trial
penalty; survived 10 direct challengers. Now in a public paper trial
(`paper/log.csv`, append-only) before any capital.

## Data (all free, all public sources)

- NSE bhavcopy 2016→present (two formats), delivery merged from MTO
  archives, symbol renames canonicalized (1,041 mappings)
- Corporate actions (equities + mf segments) with back-adjustment and
  an implied-split detector for feed gaps
- 43,421 quarterly results parsed from XBRL, keyed to broadcast
  timestamps (banking taxonomy handled)
- 151,787 named bulk/block deals; India VIX; corporate announcements
- US: point-in-time S&P 500 membership + prices; Form 4 insider
  purchases; 13F holdings for 15 funds; Senate trades snapshot

## Setup

```bash
pip install -r requirements.txt
python backfill.py --start 2016-01-01        # NSE rate-limited; hours
python -m ingest.mto                         # 2016-19 delivery
python -m ingest.renames                     # symbol-change master
python daily.py                              # cron ~19:30 IST weekdays
python -m backtest.run --strategy v2|v3|v5   # daily-engine strategies
python -m backtest.monthly                   # v4 family
python -m backtest.validate                  # DSR / PBO / consistency
python -m unittest discover tests
```

## Layout

```
ingest/     NSE + EDGAR + misc ingestion (see module docstrings for
            the API quirks each one works around)
screener/   daily shortlist, monthly portfolio, paper-trial logger
backtest/   point-in-time features, daily + monthly engines, event
            studies, validation harness
us/         US-market studies (momentum, insiders, 13F, senate, events)
docs/       the public site (GitHub Pages)
PROTOCOL_*  pre-registrations — each committed BEFORE its first run
paper/      append-only paper-trial log + machine-readable status
```

Nothing in this repository is investment advice.
