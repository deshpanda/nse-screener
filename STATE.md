# STATE — the single source of truth for this project

> Read this top-to-bottom before touching anything. It exists so that any
> fresh session — new context window, new collaborator, future us — starts
> with everything we know. **Update it at every milestone** (verdict, new
> data source, infra change). A stale STATE.md is worse than none.
> Last updated: 2026-07-14. NOW 27 tested / 26 dead / v4 in paper
> trial (entry #1 = CASH; #2 lands Jul 31 23:00 cron — now SELF-HEALING:
> watchdog auto-catchup within 3 days if laptop sleeps through it,
> PROTOCOL_GOLIVE gate-1 amendment 2026-07-14). LAST ACT: v4 AFTER-TAX
> AUDIT (PROTOCOL_TAX) — tax drag ~6pp/yr (WORSE than the registered
> 2-5 prediction; miss printed), edge SURVIVES both windows: +54pt IS /
> +63pt OOS after tax (0 of 308 IS lots long-term — churn = 20% STCG).
> Note: pre-tax edges recomputed on today's panel (+90/+135) differ
> from scoreboard-era numbers (+100/+116) — panel evolution (implied
> splits, longer IS window); the audit's finding is the pre/post delta.
> New rule of thumb: pre-tax edge < ~6pp/yr = index fund in disguise.
> Also: trading-live staleness guard (refuses >35d-old signal).
> Earlier: US ENGINE AUDIT PASSED (PROTOCOL_USAUDIT) — our monthly engine on
> 30y of US data tracks Ken French's momentum decile at corr 0.892
> (353 months) and reproduces the era pattern (+9.1pp/yr pre-2009 /
> -25.9pp 2009 crash / decay after). Both bugs found were audit-side
> (French section names, month labeling); ENGINE UNTOUCHED — v4's
> verdicts stand on independently-validated machinery. Site: method
> postscript 2 + US-deep-history data row. Earlier:
> v25 promoter ownership-trend DEAD per PROTOCOL_V25 — both registered
> priors verified (longs fail incl. E2 n=93 near-miss/OOS-worst spike;
> decrease screen not certifiable IS, was real pre-2023). Smart-money
> family closed at every disclosure speed. Site same-day: scoreboard +
> Season-2 rows, shareholding data row, counts 27/26 machine-checked,
> title now "Twenty-Six Ways". Earlier today: GO-LIVE DRILL passed — trading-live cli.py exercised through 7
> propose-mode scenarios (fresh entry / rebalance / cash flip /
> undersized capital / empty env); 3 bugs fixed (empty CAPITAL_INR
> crash, silent zero-qty drop, all-or-nothing order placement),
> SELLs-first ordering, new `verify` cmd (state vs broker holdings),
> execution-day rules in trading-live SETUP.md. NEW:
> scripts/reconcile_paper.py = the Oct-15 "review vs simulation" step;
> run on entry #1 → CLEAN (regime + all 20 lowvol names reproduce from
> today's panel). PLUS: Oct-15 decision PRE-REGISTERED —
> PROTOCOL_GOLIVE.md (3 gates: operational/behavioral/combo-corr;
> returns explicitly NOT a gate; amendments locked after Jul 31) and
> scripts/golive_review.py prints the verdict mechanically. Drilled on
> a synthetic Apr–Jun log: gate 1 caught uncommitted entries, gate 2
> fill gaps 0.2-0.3% << 1pp tol, gate 3 correctly DEFERRED (v4 in cash
> = 0 overlapping days — the likely real October path). Earlier same
> day: v22 retraction published; 3 repos standardized (RUNBOOK.md).
> NOTHING PENDING except calendar (Jul 31 / monthly checks / Oct 15
> go-live runs golive_review) and fresh-data re-registrations
> (upgrade-drift, hysteresis, v21, FIP — 2027).
> Prior: 2026-07-11 (METHOD2 harness live: v4 DSR 0.995/PBO 0.48-caution/74.7% rolling windows positive, worst -50pt. v15 PEAD + v16 residual-mom dead. 17 tested / 16 dead / v4 survives, evidence UPGRADED. Site update for v15/v16 pending).

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
- **New-data rule (2026-07-11, owner-directed)**: any dataset used by
  any study gets, SAME DAY: a row in the site's data section, an entry
  in STATE §5, and its ingest module documented. No invisible inputs.
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

| v15 | PEAD India (event-time, broadcast-timestamped, 43k announcements) | DEAD | IS median -0.04 + OOS qtr-concentration 34%. Two-null diagnostic: NEGATIVE-surprise events also beat Nifty +2.2 IS = universe tilt, not information. Surprise-specific spread: +3.8 OOS -> +0.8 IS (alpha decay again) |
| v16 | residual momentum (Blitz; beta-stripped 12-1 t-stat) + 52w-high grid | DEAD | delivered "half the vol" (DD -3.8/-14.1, OOS Sharpe 1.02>0.97) but NOT the returns: edge -14/-13 vs Nifty both windows. 52w-high: -73 OOS. Incumbent survives 10th challenge |

| v18 | smart-buyer track records (score 18,644 named counterparties point-in-time, follow proven) | DEAD | Skill signal is REAL relative to the deal pool (+1..+6) but the pool is toxic: avg disclosed net-buy deal = -0.4 IS / -6.0 OOS vs Nifty. Best-of-a-bad-pool ~ breakeven gross. Final word on follow-the-institutions |

| v17 | corporate-event studies: buybacks + order wins (3.7k + 3.5k announcements, timestamped, two-null design) | DEAD | All medians negative both windows; events underperform even the random-announcement baseline IS (vs_baseline -0.6..-2.8). Indian buybacks are not undervaluation signals. The all-announcements null (+2.4 IS) caught the activity-tilt that single-benchmark tests would credit as edge |

| v19 | sector momentum (top-3 sectors by median member 12-1, then stock momentum) | DEAD | Declared spec fails vs incumbent both windows (OOS edge +13 vs +116). Grid violently unstable: adjacent cell (top-5) shows +196 OOS — a knife-edge cell we refuse to promote, exactly what PBO 0.48 predicted. Sector map = today's snapshot (disclosed) |
| v20 | promoter-pledge negative screen | DEFERRED | No free point-in-time pledge history (API = current snapshot; backtest would be lookahead + survivorship). Monthly cron now captures snapshots (data/pledge/) — our own dataset accumulates; revisit >=12 months |

| v21 | India insider MARKET purchases (PIT, 290,913 disclosures, 40k market buys) | DEAD by the letter; STRONGEST corpse | IS passes all (+4.6/+1.6 net, beats both nulls). OOS: means strong (+2.0..+4.9 vs null, BOTH windows — unique since v4) but median -1.0 + conc 33%>30% → fail. Insider skew: few big wins. Revisit ONLY via fresh pre-registration on future data (FIP rule) |
| v22 | announcement risk screens | RETRACTED after v22.1: 1,043 PDF-verified downgrades show effect ~gone (IS +3.5 mean!, OOS -4.8 median only) — early -14.6 was 32-event keyword-bias. Screen NOT certified; personal hygiene rule withdrawn. CONTROLS validated method (upgrades +3 both windows — possible future pre-registration on FRESH data only). Auditor-resign: dead |

| v20.1 | pledge-CREATION events (early via PIT; 13,922 creations) | DEAD as screen | OOS toxic as theorized (-3.6 median, -7.8 at 126d, 38% win) but IS 2023-26 POSITIVE (+8.2 at 126d) — refusal signals are regime-dependent too; fails both-windows bar. Only rating-downgrades survived both eras |

| v24 | "NSE-200 winner" found in the wild (12m top-20, hold-till-top-40 hysteresis, no skip/regime) | BEAT NIFTY BOTH WINDOWS (+78/+23) — 2nd ever gate-passer — but LOSES to v4 everywhere (Sharpe 0.88/0.73 vs 1.21/1.04). Hysteresis is a genuinely good anti-churn idea (OOS +23 vs -4 without). Incumbent stands |
| v25 | promoter ownership-trend (quarterly shareholding, PROTOCOL_V25; v21 family, priors REGISTERED: longs fail / decrease weak-toxic) | DEAD — both priors verified. IS vs baseline null: E1 +2.0 / E4 +1.2 (< +3 bar); E2 +3.24 but n=93<100 (frozen floor; also OOS's WORST cell at -4.85 = spike signature). E3 decrease screen: IS -0.9..-1.7 (not certifiable) but OOS 2018-22 genuinely toxic (-3.7 h63, -7.1 h126) — promoter selling was real, decayed like v21/v22. Smart-money family now dead at EVERY disclosure speed (same-evening/2d/17d/45d). First protocol with outcomes predicted in advance and confirmed |

| v23 | futures OI signals (OI-confirm overlay + basis crowding screen; committed runner backtest/oi_study.py) | DEAD both hypotheses | OI-confirm toxic (-59 IS/-138 OOS: OI growth = crowding); basis screen inert. KEY DISCOVERY: v4-restricted-to-F&O collapses (+31/-68 vs full +99/+116) — v4 alpha lives in non-F&O midcaps. Echoes v8: institutionalized names do not pay momentum |

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

TRADING-LIVE repo scaffolded at ~/Documents/personal-github-repos/trading-live
(propose-first, strategies.yaml registry, one-switch TRADING_MODE; user
must create PRIVATE GitHub repo then push; keys never in repo/chat).
Small derived datasets now committed (DATA.md); big panels reproducible.

DONE 2026-07-11 evening: data repo pushed (github.com/deshpanda/nse-screener-data, 354MB, site rows link to it); v24 full chapter live (Chapter 11, with visual); trading-live is FUNCTIONAL (cli.py propose/live + kite adapter — personal API is FREE since 2024, Rs2000 = historical addon we don't need; Upstox = free fallback); calendar: monthly paper-checks Sep-Nov 1 + GO-LIVE REVIEW Oct 15 19:00 (private events).

OLDER QUEUE (2026-07-11 late, context-limited deferrals):
1. v23 verdict when futures backfill notification fires (runner MUST be
   committed script per reproducibility rule).
2. DATA REPO: owner approved separate public repo nse-screener-data for
   the big panels (~430MB). Owner must CREATE it on deshpanda first; then
   push panels + rewrite site data-section hyperlinks: dataset name →
   data repo path, keep ingest-script links as-is; remove committed
   small parquets from nse-screener? NO — keep small ones, move only big.
3. v24 full chapter + Season-2 row (currently only scoreboard row!) —
   include how-we-found-it story, hysteresis insight, maybe a chart.
   OWNER RULE: be generous with chapters + visuals henceforth.
4. Site dfn/count audit after v24 chapter (rules now in CLAUDE.md §7).
5. v24 hysteresis idea: candidate v4 refinement — fresh pre-registration
   on future data only (FIP rule applies).
6. trading-live pushed (private); SETUP.md has full Kite guide.

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
- **Watchdog**: scripts/health.py every 4 waking hours (cron :15 8-23),
  macOS notification + health.log on any failure — panel staleness, cron
  silence/tracebacks, missed month-end snapshots, broken git publish.
- **Live Trial on the site**: docs/ has a section reading paper/log.csv
  + paper/status.json from raw.githubusercontent at view time. The
  month-end snapshot AUTO-COMMITS AND PUSHES paper/ (best-effort, offline
  safe); daily.py pushes a status refresh only on regime flips. Site thus
  self-updates with zero manual steps.
- **Public site**: docs/ on GitHub Pages
  (deshpanda.github.io/nse-screener), self-contained, charts run on real
  exported data (`docs/data.js`, regenerate via the export script in the
  session scratchpad pattern — rebuild from backtest outputs when new
  verdicts land). v7 verdict should become its next chapter.


## Research queue — CLOSED OUT 2026-07-11 night (all items resolved)

- SHAREHOLDING DONE: 1,877 symbols × ~90 quarters, broadcast-timestamped
  (data/shareholding/). Format review then possible ownership-trend
  pre-registration = next research season's opener.
- FORMAT REVIEW DONE 2026-07-13 (registration-gating facts):
  * 94,822 rows, quarters 2004→2026; median 51 q/symbol; 1,579 of 2,369
    current bhav symbols covered (67%).
  * PIT boundary: broadcast timestamps exist 2015→present (59,906 rows);
    pre-2015 rows have NULL broadcastDate — unusable for event timing.
    Median disclosure lag 17d after quarter end (p75 20d), 0 negative.
  * Fields are promoter+group % and public % ONLY — the master API has
    NO FII/DII split. "Institutional accumulation" is NOT testable with
    this dataset; promoter-stake trend is. (FII/DII would need the
    per-quarter detail endpoint — future ingestion if ever wanted.)
  * 38% of rows have promoter=0 (professionally-managed cos — signal
    undefined there). 4.3% non-quarter-end special rows; 6% Revised
    flag; only 143 (symbol,quarter) true duplicates → dedupe keep=last.
  * Event base-rate: QoQ promoter change is exactly 0 in 70% of
    quarters; increases ≥0.5pp = 140–260/yr (2,017 total PIT-era) —
    v21-scale event counts, enough for the two-null design.
  * FAMILY WARNING for the protocol: promoter stake increases are the
    slow (17d-lag) cousin of v21 insider market-purchases, whose OOS
    2018-22 window is already spent (drift existed, gone in IS). Any
    registration must declare the v21 family relation, use the
    events17 two-null engine, and carry a LOW prior per alpha-decay law.
  * Registrable NOW on 2015→ PIT data (this hypothesis never touched
    any window); awaiting owner's go to write PROTOCOL_V25.
    [RESOLVED: v25 registered + DEAD same day, see scoreboard.]
- FII/DII DETAIL INGESTION (2026-07-14, in flight): endpoint
  reverse-engineered from the site's corporate-filings.js —
  `/api/corporate-share-holdings-equities?ndsId=<recordId>&index=
  public-shareholder` (COL_I=category, COL_VII=shares, COL_VIII=pct;
  57 rows/filing incl. Mutual Funds, Insurance, FPI cats, sub-totals
  B(1)/B(2)/B(3)). Detail exists 2016+ ONLY (older quarters route to
  legacy ShareholdingInformation*.html archives — not fetched).
  ingest/shareholding_detail.py: phase `masters` re-stores masters
  WITH recordId (the v25-era ingester dropped it); phase `detail` =
  one call per (symbol, quarter), ~50k calls, per-symbol restartable,
  data/shareholding_detail/. Institutional-accumulation study: format
  review THEN pre-register, after backfill lands (the v25 pattern).
- v22.1 UNBLOCK IN FLIGHT: ingest/ratings.py — 3-phase PDF pipeline
  (urls scan → liquid-universe PDF download → direction regex), chained
  overnight after indices. When parsed.parquet lands: rerun v22 with
  true directions, certify screen if bar met.
- CONSTITUENTS synthetic path (queued idea): shares_out ≈ NP/EPS from
  fr_xbrl → mcap = close × shares → point-in-time mcap ranks →
  approximate index membership, calibrated vs 13 Wayback snapshots.
  [BUILT 2026-07-14: ingest/constituents.py →
  data/constituents_synth.parquet (99 month-ends 2018→, ranks ≤600,
  mcap + free-float variants; RAW closes by design — CA-adjusted
  prices corrupt cross-sectional ranks). Banking EPS gap fixed en
  route (BasicEarningsPerShare*ExtraordinaryItems tags; refill-eps
  recovered 1,021 filings → 99.1% EPS coverage; HDFCBANK/ICICIBANK
  etc. were absent from mcap ranks before). CALIBRATION vs Wayback:
  Nifty500 recall 0.86-0.91 (mcap variant), Nifty50 free-float recall
  0.78-0.88 (ffmcap beats mcap on ALL N50 snapshots — free-float is
  the real methodology). Residual misses = committee rules (F&O
  eligibility, sector balance, buffers) we can't model. USES: PIT
  cap-segment universes (large/mid boundary), benchmark fidelity,
  index-add/drop event candidates via rank-crossing — with the
  disclosed caveat that boundary noise is largest exactly at the
  add/drop threshold. Index-inclusion study: format review done by
  construction; pre-register only on owner's go, and the protocol
  must handle approximation error (e.g., require rank moves DEEP
  through the boundary, not grazes).]
- All studies now have committed runners (runners.py incl v20.1, v24);
  site scoreboard: every row links protocol + code (27 code links).
- OLD NOTE superseded: v22.1 rating detection was BLOCKED-DOCUMENTED — direction lives in PDF
  attachments (~14k files); free-text exhausted (avg 80 boilerplate
  chars). The -14.6 OOS finding stands as knowledge; certification
  requires a future PDF-parsing project. Personal hygiene rule stands.
- Shareholding patterns: ingester live (ingest/shareholding.py, 90
  quarters/symbol, broadcast-timestamped) — backfill running (~1,800
  symbols). Ownership-trend hypothesis: pre-register only AFTER format
  review, never after outcome peeks.
- Reproducibility pass: DONE — backtest/runners.py commits v4.1/v14/
  v16/v19/v13-quality runners.
- Sector indices: ingest/indices.py committed; backfill CHAINED after
  shareholding completes (same host).
- Full constituent history: BLOCKED-DOCUMENTED — niftyindices.com
  unreachable/PDF-based; Wayback partial (13 snapshots) remains the
  standing answer.

## OLD queue (historical record)

Strategy launches paused (paper trial pending). Focus: gather/process
data that unlocks currently-impossible tests. Ranked:

1. DONE (v21 verdict above). BONUS: PIT feed contains 29,657 timestamped pledge CREATION/REVOCATION events since 2017 — partially unblocks v20 YEARS early (pledge-creation negative event study now pre-registrable). Original: **India insider (PIT/SAST) disclosures** — NSE corporates-pit API.
   The genuinely untested family: we tested US insiders (dead post-2023
   commoditization) but never Indian promoter/insider buys. Less
   app-commoditized here. Unlocks v21.
2. DONE (v22 above; 1.26M announcements in data/ann_full/). Follow-up: improve rating-announcement detection, then v22.1 certification run. Original: **Full announcements taxonomy re-fetch** — we kept only buybacks/
   orders; re-fetch keeping ALL category labels: credit-rating changes,
   auditor/CFO resignations, pledge invocations, open offers. Unlocks
   mechanism-backed RISK SCREENS (rating downgrades, resignations) more
   than return chasers.
3. **Historical index constituents** (Nifty 50/100/500 changes from NSE
   press archives) — fixes universe/benchmark fidelity, unlocks
   index-inclusion event studies, enables cap-segment point-in-time work.
4. **Quarterly shareholding patterns** (promoter/FII/DII/public % per
   symbol) — ownership-LEVEL trends vs v5's trade-events. Per-symbol
   fetch, heavy; do after 1-3.
5. DONE (v23 dead; habitat discovery). Was: **F&O stock-futures backfill** (ingest/futures.py,
   data/futstk/, 2016→now, ~3h) — OI, chg_OI, basis per stock/expiry.
   Strategy PRIORS to formalize only after data lands (no registration
   yet): (a) OI-confirmation on momentum ("long buildup": price up +
   OI up), (b) futures basis (premium/discount) as crowding gauge.
   Both must face the two-null rule and the v4 challenger bar.
   Original item: **F&O-derived features (data only, no trading)** —
   stock futures OI changes, PCR, IV from F&O bhavcopy archives.
   Sentiment features with documented literature.
6. **Sector indices OHLC** (NSE inds) — proper sector benchmarks.
3b. DONE (partial): index members via Wayback — 13 point-in-time
   snapshots (Nifty50: 10 spanning 2016-2025; Nifty500: 3 of 2020-22) in
   data/index_members/. Too sparse for inclusion event-studies; usable
   for coarse universe checks. Full press-release parse deferred.
6b. REPRODUCIBILITY PASS (queued, honest gap): v4.1/v14/v16/v19/v13-quality
   and the v13.1 combo ran as inline session runners — protocols + engine
   code are committed but not their exact runner scripts. Consolidate
   into backtest/runners.py. v23 runner MUST be a committed script.
7. Processing wins on existing data: DONE canonicalize fr_xbrl symbols
   (renames — small fidelity fix for v7/v15 reruns); close-location-value
   + gap features from OHLC; delivery-value vs free-float normalization;
   earnings-calendar extraction from board-meeting announcements
   (enables pre/post-earnings conditioning).

Rule unchanged: new data → pre-registered protocol BEFORE any outcome is
computed. Data-first ≠ mine-first.

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

US deep history (engine audit, 2026-07-13): `us/data/prices_deep/`
(batch-restartable) — 764 of 1,203 ever-members, 1995-06→present,
survivors only (levels unscored per PROTOCOL_USAUDIT). Plus
`us/data/french/` — Ken French momentum-decile + factor files
(1927→, CRSP-based, survivorship-clean); parser spot-checked vs
Oct-1987 / Oct-2008 / Apr-2009 known values. Trap found during the
audit: `monthly.simulate`'s eq rows are indexed by t1 = the month-end
a return ENDS at (French's convention) — do NOT shift labels when
comparing to external monthly series.


Pledge dataset (v20, under construction): NSE publishes only the CURRENT
promoter-pledge snapshot (corporate-pledgedata API; ~1,530 companies).
The monthly paper-log run captures it to `data/pledge/<date>.parquet`
(first: 2026-07-10). Plan: after >=12 monthly snapshots, pre-register the
pledge screen properly — join snapshots point-in-time to v4 formations,
test "exclude promoter-pledge > 25%" as a v4 challenger. Until then any
pledge backtest would be lookahead + survivorship and is refused. The
snapshots also serve as raw material for future risk screens (pledge
DELTAS month-over-month may matter more than levels).

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
