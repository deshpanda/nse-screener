# nse-screener

NSE equities research platform: EOD data pipeline, momentum screener, and
a backtesting harness with pre-registered validation.

**Nothing trades until a strategy beats Nifty buy-and-hold out-of-sample,
after costs.** Scoreboard so far (see PROTOCOL_V3.md for the method):

| strategy | idea | verdict |
|---|---|---|
| v1 | trend template, buy near highs, fixed 8% stop | dead — lost money outright |
| v2 | VCP breakout + ATR stops + breadth regime | dead — +34pt in-sample, **-64pt out-of-sample** (curve-fit) |
| v3 | delivery-accumulation clusters (pre-registered) | dead — -9.2pt in-sample, no plateau in grid |

## Data (all free, all NSE public)

- bhavcopy 2016→present: OHLCV + delivery qty/% (legacy cm format pre-2020,
  sec_bhavdata_full after; delivery for 2016-19 merged from MTO archives)
- corporate actions with back-adjustment: splits/bonuses from the equities
  AND mf segments (ETF splits live in mf), abbreviated-wording parser, plus
  a price-ratio detector for events the feed misses entirely
- bulk/block deals, FII/DII flows, ETF list (excluded from stock universes)

## Setup

```bash
pip install -r requirements.txt
python backfill.py --start 2016-01-01          # ~2h, NSE rate-limited
python -m ingest.mto                            # 2016-19 delivery + merge
python daily.py                                 # cron ~19:30 IST weekdays
python -m screener.screen                       # daily ranked shortlist
python -m backtest.run --strategy v3 --start 2022-01-01
```

## Layout

```
ingest/      NSE HTTP client, bhavcopy (2 formats), MTO delivery,
             corporate actions, bulk/block deals, FII/DII, ETF list
screener/    daily shortlist: trend template + RS + VCP proxy + footprints
backtest/    point-in-time features (no lookahead, no survivorship bias),
             event-driven engine (ATR stops, risk sizing, cooldown),
             run.py with --strategy/--start/--end
PROTOCOL_V3.md  pre-registration template: spec frozen before first run
```

## Hard-won gotchas

- Unadjusted splits look like -90% crashes; the NIFTYBEES 10:1 split (Dec
  2019) lives in the mf CA segment and silently broke the benchmark.
- `bool_frame.shift(1).fillna(False)` goes object dtype where `~True == -2`
  — always `shift(1, fill_value=False)`.
- ETFs trade in the EQ series; a "stock" screen will happily buy silver.
- In-sample sensitivity spikes (one lucky knob, neighbors negative) predict
  out-of-sample inversion. Demand plateaus.
