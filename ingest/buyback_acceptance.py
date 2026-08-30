"""Buyback ACCEPTANCE RATIOS — the number the whole tender trade rests on.

Why this matters (from v40): buyback stocks do NOT run up into the
record date — they drift ~1-2pp behind the market — and they stay ~2pp
weak for a month after it. So the entry price isn't inflated, but any
shares the company DOESN'T accept are held into reliable weakness.
The trade therefore lives or dies on the acceptance ratio, and for
small shareholders (<=Rs 2L holdings, who get a reserved 15% of every
tender offer) that ratio has historically run far above entitlement.

Our announcement store has 504 post-offer filings but EMPTY snippets —
the numbers are only in PDF attachments. Same shape as the v22.1
ratings pipeline, so same 3-phase design:

    python -m ingest.buyback_acceptance scan    # announcements + PDF urls
    python -m ingest.buyback_acceptance pdfs    # download (restartable)
    python -m ingest.buyback_acceptance parse   # extract (after review)
"""
import re
import sys
import time
from datetime import date

import pandas as pd

import config
from ingest import nse, renames

DIR = config.DATA_DIR / "buybacks"
PDF_DIR = DIR / "pdfs"
ANN_URL = ("https://www.nseindia.com/api/corporate-announcements?index=equities"
           "&from_date={frm}&to_date={to}")
WARMUP = ("https://www.nseindia.com/companies-listing/"
          "corporate-filings-announcements")
# post-offer filings carry the acceptance numbers; the others give context
POST = re.compile(r"post[\s-]?(buyback|offer)", re.I)
ANY_BB = re.compile(r"buy[\s-]?back|post[\s-]?offer", re.I)


def scan() -> None:
    DIR.mkdir(parents=True, exist_ok=True)
    s = nse.session()
    s.get(WARMUP, timeout=15)
    frames = []
    for yr in range(2016, 2027):
        for frm, to in ((f"01-01-{yr}", f"30-06-{yr}"),
                        (f"01-07-{yr}", f"31-12-{yr}")):
            try:
                r = nse.get(ANN_URL.format(frm=frm, to=to), timeout=180)
                d = r.json()
                d = d if isinstance(d, list) else d.get("data", [])
                if not d:
                    continue
                df = pd.DataFrame(d)
                df = df[df["desc"].astype(str).str.contains(ANY_BB, na=False)]
                if len(df):
                    frames.append(df)
                print(f"  {frm[-4:]} {frm[3:5]}-{to[3:5]}: {len(df)} buyback rows",
                      flush=True)
            except Exception as e:
                print(f"  {frm}: {type(e).__name__} {e}"[:110], flush=True)
            time.sleep(1.5)
    ann = pd.concat(frames, ignore_index=True)
    ann["symbol"] = renames.canonical(ann["symbol"].astype(str).str.strip())
    ann["an_dt"] = pd.to_datetime(ann["an_dt"], errors="coerce")
    ann["is_post"] = ann["desc"].astype(str).str.contains(POST, na=False)
    ann = ann.drop_duplicates(["symbol", "an_dt", "desc"])
    keep = ["symbol", "an_dt", "desc", "attchmntFile", "is_post", "sm_name"]
    ann[[c for c in keep if c in ann.columns]].to_parquet(
        DIR / "announcements.parquet", index=False)
    print(f"\nbuyback announcements: {len(ann)} "
          f"({ann['is_post'].sum()} post-offer with the acceptance numbers)")
    print(ann.groupby(ann["an_dt"].dt.year)["is_post"].sum().to_string())


def pdfs(limit: int | None = None) -> None:
    PDF_DIR.mkdir(parents=True, exist_ok=True)
    ann = pd.read_parquet(DIR / "announcements.parquet")
    todo = ann[ann["is_post"] & ann["attchmntFile"].astype(str).str.endswith(
        (".pdf", ".PDF"))]
    if limit:
        todo = todo.head(limit)
    got = 0
    for _, r in todo.iterrows():
        url = str(r["attchmntFile"])
        name = f"{r['symbol']}_{r['an_dt'].date()}_{url.rsplit('/', 1)[-1]}"
        out = PDF_DIR / name[:120]
        if out.exists():
            continue
        try:
            resp = nse.get(url, timeout=120)
            if resp.status_code == 200 and resp.content[:4] == b"%PDF":
                out.write_bytes(resp.content)
                got += 1
            else:
                print(f"  skip {name[:50]}: {resp.status_code}", flush=True)
        except Exception as e:
            print(f"  {name[:50]}: {type(e).__name__}", flush=True)
        time.sleep(0.6)
        if got and got % 50 == 0:
            print(f"  {got} PDFs downloaded", flush=True)
    print(f"pdf fetch done: {got} new, "
          f"{len(list(PDF_DIR.glob('*.pdf')))} total on disk")


# --- parse phase (written AFTER a format review of 167 downloaded PDFs) ---
# Layout, stable across 2018-2026 with one variant:
#   "Reserved category for Small Shareholders <RESERVED> <BIDS> <TENDERED> <RESPONSE>"
# and an older variant (e.g. COCHINSHIP 2018) that puts the numbers BEFORE
# the label. Numbers are Indian-comma format and PDF extraction sprinkles
# stray spaces inside them ("1,84,7 6,817"), so the number regex tolerates
# internal whitespace.
#
# CRITICAL DESIGN CHOICE: the stated "Response" column is sometimes a
# MULTIPLE (10.67) and sometimes a PERCENTAGE (433.37%) — the header text
# differs by filing. So acceptance is DERIVED as reserved/tendered, and the
# stated response is used only as a CROSS-CHECK. A row is kept only if the
# stated figure matches the derived ratio (as-is or x100) within 5%.
SMALL = re.compile(r"Reserved\s+category\s+for\s+Small\s+Shareholders", re.I)
GENERAL = re.compile(r"General\s+[Cc]ategory", re.I)
NUM = re.compile(r"\d[\d,\s]{2,}\d(?:\.\d+)?")


def _nums(text):
    out = []
    for m in NUM.finditer(text):
        t = re.sub(r"[,\s]", "", m.group(0))
        try:
            out.append(float(t))
        except ValueError:
            pass
    return out


def _row_after(flat, marker_match, n=4):
    """the first n numbers following the label (main layout)"""
    return _nums(flat[marker_match.end():marker_match.end() + 220])[:n]


def parse() -> None:
    from pypdf import PdfReader
    rows, unread, no_table, rejected = [], 0, 0, 0
    for f in sorted(PDF_DIR.glob("*.pdf")):
        try:
            txt = "\n".join((pg.extract_text() or "")
                             for pg in PdfReader(str(f)).pages)
        except Exception:
            unread += 1
            continue
        flat = re.sub(r"\s+", " ", txt)
        m = SMALL.search(flat)
        if not m:
            no_table += 1
            continue
        vals = _row_after(flat, m)
        if len(vals) < 3:
            no_table += 1
            continue
        reserved, bids, tendered = vals[0], vals[1], vals[2]
        stated = vals[3] if len(vals) > 3 else None
        if reserved <= 0 or tendered <= 0:
            rejected += 1
            continue
        derived = tendered / reserved                 # "times oversubscribed"
        ok = stated is not None and (
            abs(stated - derived) / derived < 0.05
            or abs(stated - derived * 100) / (derived * 100) < 0.05)
        if not ok:
            rejected += 1                             # parse not trustworthy
            continue
        gm = GENERAL.search(flat, m.end())
        gvals = _row_after(flat, gm) if gm else []
        sym, dt = f.name.split("_")[0], f.name.split("_")[1]
        rows.append({
            "symbol": sym, "an_dt": dt, "pdf": f.name,
            "small_reserved": reserved, "small_bids": bids,
            "small_tendered": tendered,
            "small_oversub_x": derived,
            "small_acceptance": min(1.0, reserved / tendered),
            "gen_reserved": gvals[0] if len(gvals) > 2 else None,
            "gen_tendered": gvals[2] if len(gvals) > 2 else None,
        })
    out = pd.DataFrame(rows)
    out.to_parquet(DIR / "acceptance.parquet", index=False)
    print(f"parsed: {len(out)} filings with a validated small-shareholder "
          f"table  (no table: {no_table}, failed cross-check: {rejected}, "
          f"unreadable: {unread})")
    if len(out):
        a = out["small_acceptance"]
        print(f"\nSMALL-SHAREHOLDER ACCEPTANCE RATIO")
        print(f"  median {100*a.median():.1f}%   mean {100*a.mean():.1f}%")
        print(f"  p25 {100*a.quantile(.25):.1f}%   p75 {100*a.quantile(.75):.1f}%")
        print(f"  share of events accepting >50%: {100*(a > .5).mean():.0f}%")
        print(f"  share accepting 100% (undersubscribed): {100*(a >= 1).mean():.0f}%")
        ent = out.dropna(subset=["gen_tendered"])
        if len(ent):
            gen = (ent["gen_reserved"] / ent["gen_tendered"]).clip(upper=1)
            print(f"\n  general-category acceptance median: {100*gen.median():.1f}%"
                  f"  → small-shareholder advantage: "
                  f"{100*(ent['small_acceptance'].median() - gen.median()):+.1f}pp")


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "pdfs":
        pdfs(int(sys.argv[2]) if len(sys.argv) > 2 else None)
    else:
        {"scan": scan, "parse": parse}[cmd]()
