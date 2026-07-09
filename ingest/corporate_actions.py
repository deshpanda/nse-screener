"""Corporate actions (splits + bonuses) → back-adjustment factors.

Unadjusted bhavcopy prices make every split look like a crash — a 10:1
split reads as a -90% gap. We fetch NSE's CA feed, parse the ratios out
of the free-text subject line, and back-adjust: all prices strictly
before the ex-date are multiplied by the factor, volumes divided.

Dividends and rights are ignored: small relative to momentum moves, and
parsing rights terms reliably is not worth the error surface.
"""
import re
from datetime import date, timedelta

import pandas as pd

import config
from ingest import nse

CA_URL = ("https://www.nseindia.com/api/corporates-corporateActions"
          "?index=equities&from_date={frm}&to_date={to}")
OUT = config.DATA_DIR / "corporate_actions.parquet"

# "Face Value Split (Sub-Division) - From Rs 10/- Per Share To Re 1/- ..."
SPLIT_RE = re.compile(
    r"from\s+r[se]\.?\s*([\d.]+).*?to\s+r[se]\.?\s*([\d.]+)", re.I)
# "Bonus 1:2" = 1 new share per 2 held
BONUS_RE = re.compile(r"bonus\s+(\d+)\s*:\s*(\d+)", re.I)


def fetch(start: date, end: date) -> pd.DataFrame:
    frames, d = [], start
    while d <= end:                       # quarterly chunks; NSE dislikes big ranges
        q_end = min(d + timedelta(days=90), end)
        url = CA_URL.format(frm=d.strftime("%d-%m-%Y"),
                            to=q_end.strftime("%d-%m-%Y"))
        r = nse.get(url, timeout=config.TIMEOUT)
        r.raise_for_status()
        rows = r.json()
        if rows:
            frames.append(pd.DataFrame(rows)[["symbol", "series", "subject",
                                              "exDate"]])
        d = q_end + timedelta(days=1)
    df = pd.concat(frames, ignore_index=True).drop_duplicates()
    df["exDate"] = pd.to_datetime(df["exDate"], format="%d-%b-%Y",
                                  errors="coerce")
    return df.dropna(subset=["exDate"])


def store(start: date, end: date) -> pd.DataFrame:
    df = fetch(start, end)
    if OUT.exists():                      # merge with what we already have
        df = (pd.concat([pd.read_parquet(OUT), df])
                .drop_duplicates(subset=["symbol", "subject", "exDate"]))
    df.to_parquet(OUT, index=False)
    return df


def factor(subject: str) -> float:
    """Combined price-adjustment factor from one subject line (1.0 = none)."""
    f = 1.0
    if "split" in subject.lower():
        m = SPLIT_RE.search(subject)
        if m and float(m.group(1)) > 0:
            f *= float(m.group(2)) / float(m.group(1))   # new_fv / old_fv
    m = BONUS_RE.search(subject)
    if m:
        a, b = int(m.group(1)), int(m.group(2))
        f *= b / (a + b)
    return f


def adjust(df: pd.DataFrame) -> pd.DataFrame:
    """Back-adjust a long bhavcopy frame (symbol/date/OHLC/volume) in place."""
    if not OUT.exists():
        raise SystemExit("No corporate_actions.parquet — run the CA backfill.")
    ca = pd.read_parquet(OUT)
    ca["factor"] = ca["subject"].map(factor)
    ca = ca[(ca["factor"] != 1.0) & (ca["factor"] > 0)]

    px_cols = ["open", "high", "low", "close"]
    df[["volume", "deliv_qty"]] = df[["volume", "deliv_qty"]].astype("float64")
    for sym, grp in ca.groupby("symbol"):
        m_sym = df["symbol"] == sym
        if not m_sym.any():
            continue
        for _, row in grp.iterrows():
            m = m_sym & (df["date"] < row["exDate"])
            if m.any():
                df.loc[m, px_cols] *= row["factor"]
                for c in ("volume", "deliv_qty"):
                    df.loc[m, c] /= row["factor"]
    return df
