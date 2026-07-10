# STATE — the single source of truth for this project

> Read this top-to-bottom before touching anything. It exists so that any
> fresh session — new context window, new collaborator, future us — starts
> with everything we know. **Update it at every milestone** (verdict, new
> data source, infra change). A stale STATE.md is worse than none.
> Last updated: 2026-07-10 evening (v7 DEAD, incumbent stands; campaign concluded: 15 tested / 14 dead / v4 survives; next events: paper log Jul 31, go-live review ~Oct).

## 1. Mission & the deal

Goal: profits from the stock market. The binding deal that governs all
work: **nothing trades real money until it (a) beats buy-and-hold Nifty
after costs in a backtest, (b) survives out-of-sample validation, and
(c) survives 2–3 months of paper trading.** No stock picks, no
predictions, no exceptions. The owner's identity in this repo is
`deshpanda` (repo-local git config; personal account, not the work one).
No AI attribution anywhere in the repo — no co-author trailers, no tool
names in code/docs/site (local untracked config files are fine).

## 2. Method rules (learned the hard way, non-negotiable)

- **Pre-register before first run**: spec, windows, grid, pass criteria
  committed to git BEFORE any result is computed (see PROTOCOL_V*.md).
  No post-hoc parameter rescue — a failed variant stays dead.
- **In-sample designs on 2023→present; out-of-sample is a single frozen
  shot on older data.** Once an OOS window is used for a strategy family,
  re-mining it is contaminated.
- **Demand plateaus, not spikes**: perturb every parameter ±~25%; a real
  edge degrades gracefully. In-sample sensitivity spikes have predicted
  OOS inversion every single time here (v2's best IS knobs were its worst
  OOS).
- **Incumbent wins ties**: a challenger replaces the champion only by
  beating it on the pre-registered criteria in BOTH windows.
- **Benchmark is Nifty buy-and-hold (NIFTYBEES)**, costs 0.25%/side.
- **Event studies need TWO nulls** (learned in the 2026-07-10 audit): vs
  the index (the capital question) AND vs the average investable stock
  (the information question). In 2023-26 the avg S&P stock did -1.8%/63d
  vs SPY — cap-weight concentration made "vs SPY" nearly unbeatable for
  any stock-picker; scope claims accordingly.
- **Audit the survivor hardest**: v4's 24 OOS "delists" were audited
  name-by-name (7 renames, 16 EQ→BE series migrations returning ~97d
  later at -5% avg gap, 1 merger). Realistic haircut keeps OOS edge +59.
  A naive 50% haircut would flip the verdict — the audit, not the
  assumption, settles it.

## 3. Scoreboard (as of 2026-07-10)

| id | idea | verdict | key numbers |
|----|------|---------|-------------|
| v1 | trend template, buy near highs, 8% fixed stop | DEAD | -15% vs Nifty +37%; stops = noise triggers |
| v2 | VCP breakout, ATR stops, breadth regime | DEAD (curve-fit) | IS +34pt → OOS **-64pt**; knife-edge grid |
| v3 | delivery-spike accumulation clusters | DEAD | IS -9.2pt; grid scatter (-36..+25) |
| **v4** | **top-20 12-1 momentum, monthly, 200DMA regime→cash** | **PASS → paper phase** | IS +100pt, OOS +77pt; 7/7 grid positive both windows; survives 2× costs, ₹10cr floor. Matches published N200M30 behavior |
| v4.1 | vol-scaling / FIP smoothness on v4 | DEAD (incumbent stands) | vol-scaling OOS edge -23 (dilutes Indian momentum); FIP great OOS (Sharpe 1.23) but worse IS — mixed → incumbent |
| v5 | follow sticky-institution bulk/block buys T+1 | DEAD | IS -18.7pt; ALL variants negative; disclosure lag = market front-runs you |
| v6 | US "obvious rally" joining (event study) | DEAD | 927 events: mean excess ≈0, win rate 56%, worst -62%. MU itself fired 5 signals, 2 lost |
| v7 | earnings momentum (SUE overlay on v4; 43,421 point-in-time filings, 99.4% coverage incl. banking-taxonomy fix) | DEAD (incumbent stands) | Overlay beat v4 IS on ALL criteria (Sharpe 1.34/1.24, DD -10.1/-11.9, edge +118/+100) but lost OOS 2020-22 (1.42/1.66, +45/+83) — mixed → incumbent rule. Standalone: -22 vs Nifty OOS, corr(v4)=0.80. Earnings momentum is REAL (beats Nifty both windows, grid plateau) but subtracts from pure momentum. v13-quality also dead standalone |
| v8 | US large-cap momentum (v4 recipe on point-in-time S&P 500) | DEAD | OOS 2016-22 all variants -40..-100pt vs SPY; the 200DMA regime HURTS in the US (V-recovery whipsaw) — regime filters don't port across market cultures |
| v9 | US insider cluster buys (Form 4, 2-day disclosure, openinsider) | DEAD | IS 2023-26 mean/median excess NEGATIVE (all variants); OOS 2016-22 shows the documented 6-month drift (+3.4 mean at 126d hold, 60% win) — the edge EXISTED and decayed once insider-tracking became a retail commodity. 78,300 filings ingested (us/insiders.py) |
| v10 | 13F guru-cloning (15 pre-2016-famous funds, EDGAR, new positions ≥1%) | DEAD for capital; skill EXISTS | vs avg-stock null (+3.6 mean) funds genuinely pick above-average stocks — but stock-picking itself lost to cap-weighted SPY 2023-26. IS median -1.3 vs SPY. 538 filings/28k positions (us/thirteenf.py) |
| v11 | Senate trades (community snapshot 2012-2020, +45d disclosure lag) | DEAD | mean/median excess negative even historically; raw win 68% vs excess win 47% = the bull-market illusion these services sell. Data ends Dec 2020 |
| v12 | short-horizon news-pop reaction, entry×hold grid, both markets | DEAD | US: all cells negative both windows (pops FADE). India IS: no positive-median cell, net ≈ 0. India OOS 2017-22: real drift existed (net +0.7-0.9%, 53-57% win) — decayed to nothing by 2023 |
| v13 | India low-volatility sleeve (naive 252d realized vol, bottom-20) | DEAD standalone; ALIVE as combo candidate | Standalone criteria failed. BUT audit follow-up: 70/30 v4/lowvol beats pure v4 Sharpe BOTH windows (1.27/1.06 vs 1.24/0.97), OOS DD -23.8 vs -33.5. Result came from an exploratory peek → needs formal combo pre-registration + confirmation in PAPER phase (untouched data). Quality variant still awaits v7 data |
| v4.2 | rebalance-cadence sweep on v4 (k in 5/10/21/42/63 sessions) | DEAD (incumbent stands) | weekly OOS edge -82 (churn+costs); fortnightly flips sign OOS; quarterly DDs balloon to -44. Monthly = plateau top. Anchor-day luck swings IS edge +-70pt over 43 rebalances - treat single backtest numbers as estimates, trust cross-window patterns |
| v14 | India VIX-augmented regime on v4 (F&O data as info only) | DEAD (incumbent stands) | VIX<25 + DMA = identical to v4 IS (redundant); OOS -24pt (VIX stays high post-crash exactly when re-entry pays). vix<20 OOS -79pt. High fear = high forward returns in India. data: ingest/vix.py |

Deep insight thread: every *visible* signal (patterns, disclosures,
rallies) is already priced by the time you can act. v4 works because it
harvests a slow behavioral bias, not information. v8 showed edges are
local (US large caps don't pay naive momentum; India-fit regime params
hurt there). And v9/v10/v12 independently show the SAME alpha-decay
signature: edges that were real in 2016-2022 (insider drift, India
post-pop drift, slow 13F diffusion) are measurably gone in 2023-2026 —
killed by commoditized data apps and the discount-broker retail boom.
"Follow smart money" is now closed at all four disclosure speeds:
same-evening (v5), 2-day (v9), 45-day funds (v10), 45-day Senate (v11).

## 4. Current status & pending

- **Research campaign CONCLUDED 2026-07-10**: 15 strategies tested, 14
  dead, v4 the sole survivor. Fundamentals dataset complete (43,421
  filings, 99.4%; banking taxonomy = ProfitLossForThePeriod). No further
  hypotheses queued except v13.1 combo confirmation (paper phase).
- **v4 paper phase**: `paper/log.csv` (append-only), entry #1 =
  2026-07-08 regime OFF/CASH. Cron: last day of month 23:00 IST runs
  `screener.paper_log`; daily 19:30 IST cron runs `daily.py` + screener.
  Decision pending after ~2-3 clean months: deploy small real money
  (sizing details are a private conversation, not a repo topic).
- **Public site**: docs/ on GitHub Pages
  (deshpanda.github.io/nse-screener), self-contained, charts run on real
  exported data (`docs/data.js`, regenerate via the export script in the
  session scratchpad pattern — rebuild from backtest outputs when new
  verdicts land). v7 verdict should become its next chapter.

## 5. Data infrastructure (what exists, where, and the traps)

Panel: `data/bhav/*.parquet` — 2016-01→present, OHLCV+delivery, EQ series,
2,671+ trading days, no holes (a features-level guard refuses >10-day
gaps). Sources: legacy `cm*bhav.csv.zip` pre-2020 (no delivery; delivery
merged from MTO archives), `sec_bhavdata_full` 2020+ (only exists ~2020+).
Delivery for 2016-19 came from `MTO_ddmmyyyy.DAT` files (`ingest/mto.py`).

Corporate actions: `data/corporate_actions.parquet` via
`corporates-corporateActions` API — **must pull BOTH 'equities' AND 'mf'
segments** (NIFTYBEES's 10:1 split lives in mf; missing it fakes a -90%
benchmark crash). Parser handles abbreviated pre-2018 wording
("Fv Splt Frm Rs 10 To Re 1"). `implied_splits()` detects feed-missing
splits from clean price ratios + volume scale-up, price floor ₹20
(penny-stock ticks land on clean ratios). ~87 implied events, saved to
`data/implied_splits.csv`. Real single-day crashes (INFIBEAM -71%) are
correctly NOT adjusted.

Deals: `data/deals_hist/*.parquet` — 151,787 bulk+block deals 2016→now.
API trap: JSON caps at 70 rows silently; **`&csv=true` bypasses**. Column
names come BOM-mangled; read bytes with utf-8-sig; qty has Indian commas.

Fundamentals: `data/fr_list.parquet` (100k filings index w/ broadcast
timestamps) + `data/fr_xbrl/parsed.parquet` (net profit/EPS/revenue).
Traps: results before Dec-2024 quarter via `corporates-financial-results`
API; **after that via `integrated-filing-results` API which pages at 20
rows unless `&size=` is passed**. Legacy XBRL files reference context
'OneD' (current quarter) WITHOUT declaring it — parse by convention
first, declared-period fallback (tests in `tests/test_parsers.py`).
Old-format (pre-2018) filings have no XBRL at all.

ETFs: `data/etf_list.parquet` (328) — they trade in EQ series and MUST be
excluded from stock universes and breadth (v2's top "stock" winners were
silver ETFs). NIFTYBEES stays as benchmark only.

NSE client quirks: browser headers + cookie warmup on www.nseindia.com
(`ingest/nse.py`); nsearchives tolerates ~1s cadence; 404 = holiday.

US: `us/data/prices.parquet` — 598 tickers, point-in-time S&P 500
membership (`us/data/sp500_hist.csv`, fja05680 dataset), yfinance,
84% coverage (delisted tickers missing — flatters results, disclosed).

## 6. Backtest engines

- `backtest/features.py` — point-in-time panel + shared context
  (`_panel`, `_context`), signal builders `build` (v2), `build_v3`,
  `build_v5`. ETF exclusion + breadth (stocks only) inside `_context`.
- `backtest/engine.py` — daily event-driven sim: ATR stops on CLOSE
  (gap-opens fill at open), scale-out at target→breakeven, 50DMA trail,
  1% risk sizing, 15% cap, 8 slots, cooldown (`BT_COOLDOWN`).
- `backtest/monthly.py` — monthly sim (v4 family): formation at
  month-end, fills next open, cost on churn, regime→cash, `vol_target`,
  `fip_pool`, and `select_fn` hook (v7 uses it). Delisted mid-hold exit
  at last close (logged in `delist` count; renames look like delists —
  known ambiguity, roughly conservative).
- `backtest/v7.py` — SUE frame keyed to broadcast+1, overlay/standalone.
- Known engine caveats: no circuit-limit modeling (upper-circuit fills
  assumed at open — flatters momentum; the ₹10cr-floor variant is the
  robustness check), NIFTYBEES ≈ TRI-ish benchmark (ETF accrues
  dividends; strategy legs don't get dividends — slightly conservative
  for us).

## 7. Standing conventions

- Python 3.14 venv at `.venv/`; run everything as `.venv/bin/python`.
- Commits: owner identity only, no co-author trailers, no tool names.
- Tests: `.venv/bin/python -m unittest discover tests`.
- Cron (user's crontab): 19:30 IST weekdays daily.py + screener;
  23:00 IST last-day-of-month paper log.
- Site data regeneration: export script writes `docs/data.js` (see git
  history of docs/ for the shape) — keep title/favicon stable.

## 8. Next-decision queue

1. v7 verdict when fetch lands (criteria above, then site chapter).
2. July 31: first automatic paper-log rebalance entry — sanity-check it.
3. After ~Sep/Oct 2026: paper-vs-backtest review → real-money decision
   (size such that total loss is survivable; full sizing context lives
   outside the repo).
4. Queued: v10 = 13F guru-cloning event study (EDGAR access verified;
   45-day lag, prior very low after v9's fresher signal died — run for
   completeness of the "follow smart money" question). Congressional
   trades: free datasets dead (403), parked.
5. Parked ideas: FIP smoothness (promising OOS, failed IS — needs fresh
   pre-registration on NEW data only), quarterly shareholding-pattern
   ingestion (v5 phase 2), weekly regime checks.
