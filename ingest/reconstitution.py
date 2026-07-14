"""Index reconstitution press releases from NSE Indices (niftyindices.com)
— the actual add/drop announcements with announce AND effective dates,
1998→present. Queued by v27's post-mortem: the honest power source for
any index-flow re-test (v27's synthetic detection gave 9-17 events;
these are the real thing).

    python -m ingest.reconstitution list   # scrape the 1,400+ item index
    python -m ingest.reconstitution pdfs   # download the ~1,100 relevant
Parse phase comes after a format review of the PDFs (the v25 pattern).
"""
import html as hu
import re
import sys
import time
from pathlib import Path

import pandas as pd
import requests

import config

DIR = config.DATA_DIR / "reconstitution"
PDF_DIR = DIR / "pdfs"
BASE = "https://www.niftyindices.com"
H = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
     "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36"}
KW = re.compile(r"replac|reconstit|exclusion|inclusion|change", re.I)


def scrape_list() -> None:
    DIR.mkdir(parents=True, exist_ok=True)
    page = requests.get(BASE + "/press-release", headers=H, timeout=60).text
    items = re.findall(
        r'data-date="([^"]+)"[^>]*>\s*<p>[^<]*</p>\s*'
        r'<a href=[\'"]([^\'"]+\.pdf)[\'"][^>]*>(.*?)</a>', page, re.S)
    rows = [{"announce": pd.to_datetime(d, format="%b %d, %Y"),
             "url": u if u.startswith("http") else BASE + u,
             "title": re.sub(r"\s+", " ", hu.unescape(t)).strip()}
            for d, u, t in items]
    df = pd.DataFrame(rows).drop_duplicates("url")
    df["relevant"] = df["title"].str.contains(KW)
    df.to_parquet(DIR / "index.parquet", index=False)
    print(f"{len(df)} press releases indexed "
          f"({df['relevant'].sum()} reconstitution-flavored) "
          f"{df['announce'].min().date()} → {df['announce'].max().date()}")


def fetch_pdfs() -> None:
    PDF_DIR.mkdir(parents=True, exist_ok=True)
    df = pd.read_parquet(DIR / "index.parquet")
    todo = df[df["relevant"]]
    got = 0
    for _, r in todo.iterrows():
        out = PDF_DIR / Path(r["url"]).name
        if out.exists():
            continue                              # restartable
        try:
            resp = requests.get(r["url"], headers=H, timeout=60)
            if resp.status_code == 200 and resp.content[:4] == b"%PDF":
                out.write_bytes(resp.content)
                got += 1
            else:
                print(f"skip {out.name}: {resp.status_code}", flush=True)
        except Exception as e:
            print(f"{out.name}: {e}", flush=True)
        time.sleep(0.7)
        if got and got % 100 == 0:
            print(f"{got} PDFs fetched", flush=True)
    print(f"pdf fetch done: {got} new, "
          f"{len(list(PDF_DIR.glob('*.pdf')))} total on disk")


if __name__ == "__main__":
    {"list": scrape_list, "pdfs": fetch_pdfs}[sys.argv[1]]()
