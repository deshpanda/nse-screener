"""Point-in-time quarterly fundamentals from NSE corporate filings.

Two stages:
  python -m ingest.financials list      # filings index 2018→now (~5 min)
  python -m ingest.financials xbrl      # fetch+parse XBRL per filing (hours)

Point-in-time integrity: every number is keyed to the filing's BROADCAST
timestamp (when the market first saw it), never the quarter it describes.
Only 'New'-format (Ind-AS XBRL) filings carry parseable files — coverage
effectively starts 2018, which the v7 protocol discloses.

Per symbol we fetch ONE result type: Consolidated if ≥80% of its quarters
have a consolidated filing, else Standalone — mixing types across quarters
would corrupt YoY comparisons.
"""
import io
import sys
import time
import xml.etree.ElementTree as ET
from datetime import date, timedelta

import pandas as pd

import config
from ingest import nse

LIST_URL = ("https://www.nseindia.com/api/corporates-financial-results"
            "?index=equities&from_date={frm}&to_date={to}&period=Quarterly")
# From the Dec-2024 quarter, SEBI's Integrated Filing regime moved results
# to a different API (which pages at 20 rows unless size= is passed).
INTG_URL = ("https://www.nseindia.com/api/integrated-filing-results"
            "?index=equities&from_date={frm}&to_date={to}"
            "&type=Integrated%20Filing-%20Financials&size=5000")
INTG_FROM = date(2024, 12, 1)
LIST_OUT = config.DATA_DIR / "fr_list.parquet"
XBRL_DIR = config.DATA_DIR / "fr_xbrl"

PROFIT_TAGS = ("ProfitLossForPeriod", "ProfitLossAfterTaxForThePeriod",
               "NetProfitLossForThePeriod")
EPS_TAGS = ("BasicEarningsLossPerShareFromContinuingOperations",
            "BasicEarningsLossPerShare")
REV_TAGS = ("RevenueFromOperations", "Income", "TotalIncome")


def backfill_list(start: date = date(2018, 1, 1)) -> pd.DataFrame:
    s = nse.session()
    s.get("https://www.nseindia.com/companies-listing/"
          "corporate-filings-financial-results", timeout=15)
    frames, d = [], start
    while d <= date.today():
        q_end = d + timedelta(days=89)
        r = nse.get(LIST_URL.format(frm=d.strftime("%d-%m-%Y"),
                                    to=q_end.strftime("%d-%m-%Y")),
                    timeout=90)
        rows = r.json()
        rows = rows if isinstance(rows, list) else rows.get("data", [])
        if rows:
            frames.append(pd.DataFrame(rows))
        print(f"  {d} → {q_end}: {len(rows)} filings")
        d = q_end + timedelta(days=1)
        time.sleep(config.SLEEP_SECS)
    df = pd.concat(frames, ignore_index=True)
    df = df[df["period"] == "Quarterly"].copy()
    df["broadcast"] = pd.to_datetime(df["broadCastDate"],
                                     format="%d-%b-%Y %H:%M:%S",
                                     errors="coerce")
    df["q_end"] = pd.to_datetime(df["toDate"], format="%d-%b-%Y",
                                 errors="coerce")

    # integrated-filing era (Dec 2024 quarter onward)
    iframes, d = [], INTG_FROM
    while d <= date.today():
        m_end = d + timedelta(days=30)
        r = nse.get(INTG_URL.format(frm=d.strftime("%d-%m-%Y"),
                                    to=m_end.strftime("%d-%m-%Y")),
                    timeout=90)
        rows = r.json().get("data", [])
        if rows:
            iframes.append(pd.DataFrame(rows))
        print(f"  intg {d} → {m_end}: {len(rows)} filings")
        d = m_end + timedelta(days=1)
        time.sleep(config.SLEEP_SECS)
    if iframes:
        idf = pd.concat(iframes, ignore_index=True)
        idf["broadcast"] = pd.to_datetime(idf["broadcast_Date"],
                                          format="%d-%b-%Y %H:%M:%S",
                                          errors="coerce")
        idf["q_end"] = pd.to_datetime(idf["qe_Date"], format="%d-%b-%Y",
                                      errors="coerce")
        keep = ["symbol", "broadcast", "q_end", "consolidated", "xbrl"]
        df = pd.concat([df[keep + ["audited"]],
                        idf[keep + ["audited"]]], ignore_index=True)

    df = df.dropna(subset=["broadcast", "q_end", "symbol"])
    df = df[df["xbrl"].str.len() > 60]          # placeholder-dash rows out
    df = df.drop_duplicates(subset=["symbol", "q_end", "consolidated",
                                    "broadcast"])
    df.to_parquet(LIST_OUT, index=False)
    print(f"{len(df)} usable filings → {LIST_OUT}")
    return df


def _liquid_universe() -> set[str]:
    from ingest import bhavcopy, etf_list
    bhav = bhavcopy.load_all()
    med = (bhav.set_index("date").groupby("symbol")["turnover_lacs"]
               .rolling(20).median().reset_index())
    liquid = set(med[med["turnover_lacs"] >= config.MIN_AVG_TURNOVER_LACS]
                 ["symbol"].unique())
    return liquid - etf_list.symbols()


def fetch_plan() -> pd.DataFrame:
    """Earliest filing per (symbol, quarter) in the chosen result type."""
    fl = pd.read_parquet(LIST_OUT)
    fl = fl[fl["symbol"].isin(_liquid_universe())]
    cons_share = (fl.groupby("symbol")["consolidated"]
                    .apply(lambda s: (s == "Consolidated").mean()))
    prefer_cons = cons_share >= 0.8
    fl["want"] = fl.apply(
        lambda r: (r["consolidated"] == "Consolidated") ==
                  bool(prefer_cons.get(r["symbol"], False)), axis=1)
    plan = (fl[fl["want"]].sort_values("broadcast")
              .groupby(["symbol", "q_end"], as_index=False).first())
    return plan


def parse_xbrl(content: bytes, q_end: pd.Timestamp) -> dict | None:
    try:
        root = ET.fromstring(content)
    except ET.ParseError:
        return None
    ctx_period = {}
    for el in root.iter():
        tag = el.tag.split("}")[-1]
        if tag == "context":
            cid = el.get("id")
            start = end = None
            for sub in el.iter():
                st = sub.tag.split("}")[-1]
                if st == "startDate":
                    start = sub.text
                elif st == "endDate":
                    end = sub.text
            ctx_period[cid] = (start, end)

    def grab(tags):
        for el in root.iter():
            tag = el.tag.split("}")[-1]
            if tag in tags and el.text:
                per = ctx_period.get(el.get("contextRef"), (None, None))
                if per[1] and pd.Timestamp(per[1]) == q_end and per[0] \
                        and (q_end - pd.Timestamp(per[0])).days < 100:
                    try:
                        return float(el.text)
                    except ValueError:
                        continue
        return None

    np_ = grab(PROFIT_TAGS)
    if np_ is None:
        return None
    return {"net_profit": np_, "eps": grab(EPS_TAGS), "revenue": grab(REV_TAGS)}


def backfill_xbrl() -> None:
    XBRL_DIR.mkdir(parents=True, exist_ok=True)
    plan = fetch_plan()
    print(f"fetch plan: {len(plan)} filings "
          f"({plan['symbol'].nunique()} symbols)")
    done_file = XBRL_DIR / "parsed.parquet"
    done = pd.read_parquet(done_file) if done_file.exists() else pd.DataFrame()
    have = (set(zip(done["symbol"], done["q_end"]))
            if len(done) else set())
    rows, since_save = [], 0
    for _, f in plan.iterrows():
        if (f["symbol"], f["q_end"]) in have:
            continue
        try:
            r = nse.get(f["xbrl"], timeout=config.TIMEOUT)
            parsed = (parse_xbrl(r.content, f["q_end"])
                      if r.status_code == 200 else None)
        except Exception:
            parsed = None
        rows.append({"symbol": f["symbol"], "q_end": f["q_end"],
                     "broadcast": f["broadcast"],
                     "consolidated": f["consolidated"],
                     **(parsed or {"net_profit": None})})
        since_save += 1
        if since_save >= 500:
            done = pd.concat([done, pd.DataFrame(rows)], ignore_index=True)
            done.to_parquet(done_file, index=False)
            ok = done["net_profit"].notna().mean()
            print(f"  {len(done)} parsed ({100*ok:.0f}% with profit), "
                  f"at {f['symbol']} {f['q_end'].date()}")
            rows, since_save = [], 0
        time.sleep(0.8)
    if rows:
        done = pd.concat([done, pd.DataFrame(rows)], ignore_index=True)
        done.to_parquet(done_file, index=False)
    print(f"done: {len(done)} filings parsed, "
          f"{100*done['net_profit'].notna().mean():.0f}% with net profit")


if __name__ == "__main__":
    {"list": backfill_list, "xbrl": backfill_xbrl}[sys.argv[1]]()
