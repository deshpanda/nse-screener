from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"

# --- NSE endpoints ---
BHAV_URL = "https://nsearchives.nseindia.com/products/content/sec_bhavdata_full_{ddmmyyyy}.csv"
BULK_URL = "https://nsearchives.nseindia.com/content/equities/bulk.csv"
BLOCK_URL = "https://nsearchives.nseindia.com/content/equities/block.csv"
FII_DII_URL = "https://www.nseindia.com/api/fiidiiTradeReact"

SLEEP_SECS = 1.5          # between archive requests; raise if you see 403s
TIMEOUT = 30

# --- screener params ---
SERIES = {"EQ"}           # add "BE" if you want trade-to-trade stocks (you don't)
MIN_AVG_TURNOVER_LACS = 500   # ~₹5cr/day median turnover; illiquid names are traps
RS_PERCENTILE_MIN = 70
NEAR_HIGH_PCT = 0.75      # close >= 75% of 52w high
ABOVE_LOW_PCT = 1.25      # close >= 125% of 52w low
VCP_LOOKBACK = 60
DELIVERY_SPIKE_MULT = 2.0
BULK_DEAL_LOOKBACK_DAYS = 30

# --- backtest params (v2: breakout entries, ATR stops, breadth regime) ---
BT_MAX_POSITIONS = 8
BT_RISK_PCT = 0.01        # each trade risks 1% of equity (sizing = risk / stop-width)
BT_ATR_MULT = 2.5         # stop = entry − 2.5 × ATR(14); checked on CLOSE, not lows
BT_TARGET_R = 2.5         # scale out half at +2.5R, stop moves to breakeven
BT_MAX_POS_PCT = 0.15     # position value cap as fraction of equity
BT_VOL_BREAKOUT = 1.5     # breakout-day volume must be ≥ 1.5 × 20d average
BT_MIN_CONTRACTION = 1    # of the 2 VCP legs (range tightening, volume dry-up)
BT_BREADTH_MIN = 0.40     # new entries only if ≥40% of universe above its 200-DMA
BT_COST_PCT = 0.0025      # per side: STT + charges + slippage (delivery brokerage 0)
BT_START_CASH = 1_000_000
BT_BENCH = "NIFTYBEES"    # tradable Nifty proxy, present in bhavcopy
BT_COOLDOWN = 0           # trading days before re-entering an exited symbol

# --- v3: delivery-accumulation (PROTOCOL_V3.md; do not tune post-hoc) ---
V3_SPIKE_MULT = 2.0       # deliv_qty > mult × trailing 60d median
V3_CLUSTER = 3            # accumulation days required…
V3_WINDOW = 20            # …within this many trading days
V3_RS_FLOOR = 60          # RS percentile context filter
V3_COOLDOWN = 20          # re-entry cooldown (engine BT_COOLDOWN for v3 runs)

# --- v5: sticky-institution deal following (PROTOCOL_V5.md) ---
V5_STICKY_RE = "MUTUAL FUND|LIFE INSURANCE|PENSION|PROVIDENT|SOVEREIGN"
