"""Point-in-time features over the whole bhavcopy panel, vectorized as
date × symbol frames. Every value at row t uses only data up to and
including t — the engine acts on them at t+1's open, so no lookahead.

Mirrors screener/screen.py rules exactly; if you change one, change both.
"""
import numpy as np
import pandas as pd

import config
from ingest import bhavcopy, corporate_actions, etf_list


def build(start: str | None = None, end: str | None = None) -> dict:
    df = corporate_actions.adjust(bhavcopy.load_all())
    if start:
        df = df[df["date"] >= start]
    if end:
        df = df[df["date"] <= end]

    gaps = df["date"].drop_duplicates().sort_values().diff().dt.days
    if (gaps > 10).any():
        raise SystemExit(
            "Panel has a >10-day hole (backfill incomplete?). Rolling "
            "windows would span it and produce garbage. Finish the "
            "backfill, then rerun.")

    def wide(col):
        return df.pivot_table(index="date", columns="symbol", values=col)

    close, high, low = wide("close"), wide("high"), wide("low")
    vol, turn = wide("volume"), wide("turnover_lacs")

    ma50 = close.rolling(50).mean()
    ma150 = close.rolling(150).mean()
    ma200 = close.rolling(200).mean()
    lo52 = close.rolling(250, min_periods=210).min()
    hi52 = close.rolling(250, min_periods=210).max()

    trend = ((close > ma150) & (close > ma200) & (ma150 > ma200)
             & (ma200 > ma200.shift(21))          # 200-DMA rising ~1 month
             & (ma50 > ma150) & (close > ma50)
             & (close >= config.ABOVE_LOW_PCT * lo52)
             & (close >= config.NEAR_HIGH_PCT * hi52))

    rs_raw = (0.4 * (close / close.shift(63) - 1)
              + 0.2 * (close / close.shift(126) - 1)
              + 0.2 * (close / close.shift(189) - 1)
              + 0.2 * (close / close.shift(250) - 1))
    rs_pctile = rs_raw.rank(axis=1, pct=True) * 100

    tr = np.maximum(high - low,
                    np.maximum((high - close.shift()).abs(),
                               (low - close.shift()).abs()))
    atr14 = tr.rolling(14).mean()
    atr_pct = (tr / close).rolling(10).mean()
    tightening = atr_pct < 0.75 * atr_pct.shift(config.VCP_LOOKBACK - 10)
    vol_dryup = (vol.rolling(10).mean()
                 < 0.8 * vol.rolling(config.VCP_LOOKBACK).mean())
    contraction = (tightening.fillna(False).astype(int)
                   + vol_dryup.fillna(False).astype(int))

    # breakout DAY only: first close above the prior 60d high, on real volume.
    # Buying hover-days near the pivot (v1) meant buying local tops.
    pivot = high.rolling(config.VCP_LOOKBACK).max().shift(1)
    breakout = (close > pivot) & (close.shift(1) <= pivot.shift(1))
    vol_confirm = vol > config.BT_VOL_BREAKOUT * vol.rolling(20).mean().shift(1)

    liquid = turn.rolling(20).median() >= config.MIN_AVG_TURNOVER_LACS

    signal = (trend.fillna(False) & liquid.fillna(False)
              & (rs_pctile >= config.RS_PERCENTILE_MIN)
              & (contraction >= config.BT_MIN_CONTRACTION)
              & breakout.fillna(False) & vol_confirm.fillna(False))

    # stocks only: ETFs trade in the EQ series and sneak in as candidates
    # (v2's top winners were silver ETFs — a stealth commodity bet)
    etfs = [s for s in etf_list.symbols() if s in signal.columns]
    signal[etfs] = False

    bench = close[config.BT_BENCH]
    # regime = index uptrend AND healthy breadth. 2025 proved the index alone
    # lies: Nifty held its 200-DMA while the momentum universe collapsed.
    breadth = (close > ma200).sum(axis=1) / ma200.notna().sum(axis=1)
    regime = ((bench > bench.rolling(200).mean())
              & (breadth >= config.BT_BREADTH_MIN))

    return {"open": wide("open"), "high": high, "low": low, "close": close,
            "ma50": ma50, "atr": atr14, "rs_pctile": rs_pctile,
            "signal": signal, "bench": bench, "regime": regime}
