"""The Oct-15 go-live review, mechanized. Implements PROTOCOL_GOLIVE.md
verbatim — run it and read the verdict; there is nothing to interpret.

    .venv/bin/python -m scripts.golive_review

Safe to run early: before the three automatic entries exist it reports
progress and marks the review NOT DUE.
"""
import subprocess
from pathlib import Path

import pandas as pd

from backtest import features
from scripts.reconcile_paper import recompute, logged_names, diff

ROOT = Path(__file__).resolve().parent.parent
LOG = ROOT / "paper" / "log.csv"
REQUIRED_MONTHS = ("2026-07", "2026-08", "2026-09")
SEED = "2026-07-08"
TOL = 0.01          # Gate 2: 1.0pp fill-assumption tolerance
CORR_MAX = 0.6      # Gate 3
MIN_OVERLAP = 30    # Gate 3: overlapping invested days


def _commit_dates():
    """author dates of every commit touching paper/log.csv, oldest first"""
    out = subprocess.run(
        ["git", "log", "--reverse", "--format=%ad", "--date=short",
         "--", "paper/log.csv"], cwd=ROOT, capture_output=True, text=True)
    return [pd.Timestamp(d) for d in out.stdout.split()]


def gate1(log):
    fails = []
    commits = _commit_dates()
    for m in REQUIRED_MONTHS:
        rows = log[(log["asof"].dt.strftime("%Y-%m") == m)
                   & (log["asof"] != SEED)]
        eom = rows[rows["asof"].dt.day >= 24]   # month-end entry, not a seed
        if eom.empty:
            fails.append(f"no month-end entry for {m}")
            continue
        t = eom["asof"].iloc[-1]
        ok = any(t <= c <= t + pd.Timedelta(days=3) for c in commits)
        if not ok:
            fails.append(f"{m} entry not committed within 3 days of "
                         f"{t.date()} (manual backfill?)")
    hl = ROOT / "health.log"
    if hl.exists():
        bad = [l for l in hl.read_text().splitlines() if "FAIL" in l]
        if bad:
            fails.append(f"health.log has {len(bad)} FAIL line(s): "
                         f"{bad[-1]!r}")
    return fails


def gate2(log, p, ctx):
    close, open_ = p["close"], p["open"]
    fails = []
    # names must reproduce (reconcile core)
    for _, row in log.iterrows():
        t = row["asof"]
        if t not in close.index:
            fails.append(f"{t.date()} missing from panel")
            continue
        regime_on, mom, low = recompute(p, ctx, t)
        if (row["regime"] == "ON") != regime_on:
            fails.append(f"{t.date()} regime does not reproduce")
        if row["regime"] == "ON" and diff("momentum",
                                          logged_names(row["holdings"]),
                                          mom):
            fails.append(f"{t.date()} momentum names drifted")
        if "@" in str(row["lowvol_sleeve"]) and diff(
                "lowvol", logged_names(row["lowvol_sleeve"]), low):
            fails.append(f"{t.date()} lowvol names drifted")

    def next_open(t):
        later = open_.index[open_.index > t]
        return later[0] if len(later) else None

    for i in range(len(log) - 1):
        a, b = log.iloc[i], log.iloc[i + 1]
        for col in ("holdings", "lowvol_sleeve"):
            cell = str(a[col])
            if "@" not in cell:
                continue                     # cash month passes trivially
            names = dict(x.split("@") for x in cell.split(";"))
            nxt = {s.split("@")[0] for s in str(b[col]).split(";")
                   if "@" in str(b[col])}
            paper = pd.Series({
                s: close.loc[:b["asof"], s].dropna().iloc[-1] / float(px)
                for s, px in names.items()
                if len(close.loc[:b["asof"], s].dropna())}).mean()
            fa, fb = next_open(a["asof"]), next_open(b["asof"])
            if fa is None or fb is None:
                continue
            rel = pd.Series({s: open_.loc[fb, s] / open_.loc[fa, s]
                             for s in names if pd.notna(open_.loc[fa, s])
                             and pd.notna(open_.loc[fb, s])})
            churn = (len(set(names) - nxt) / len(names)) if nxt else 1.0
            sim = rel.mean() * (1 - 0.0025) * (1 - 0.0025 * churn)
            gap = abs(paper - sim)
            tag = "ok" if gap <= TOL else "FAIL"
            print(f"    gate2 {col:<13} {a['asof'].date()}→"
                  f"{b['asof'].date()}: paper {paper-1:+.2%} "
                  f"sim {sim-1:+.2%} gap {gap:.2%} [{tag}]")
            if gap > TOL:
                fails.append(f"{a['asof'].date()} {col} fill gap "
                             f"{gap:.2%} > 1.0pp")
    return fails


def gate3(log, p):
    close = p["close"]
    daily = close.pct_change()
    ra, rb = [], []
    for i in range(len(log)):
        row = log.iloc[i]
        start = row["asof"]
        end = log.iloc[i + 1]["asof"] if i + 1 < len(log) else close.index[-1]
        days = daily.index[(daily.index > start) & (daily.index <= end)]
        mom = logged_names(row["holdings"]) if row["regime"] == "ON" else []
        low = logged_names(str(row["lowvol_sleeve"])) \
            if "@" in str(row["lowvol_sleeve"]) else []
        for d in days:
            if mom and low:
                ra.append(daily.loc[d, [s for s in mom
                                        if s in daily.columns]].mean())
                rb.append(daily.loc[d, [s for s in low
                                        if s in daily.columns]].mean())
    n = len(ra)
    if n < MIN_OVERLAP:
        return None, n
    return float(pd.Series(ra).corr(pd.Series(rb))), n


def main():
    log = pd.read_csv(LOG, parse_dates=["asof"])
    today = pd.Timestamp.now().normalize()
    print(f"go-live review per PROTOCOL_GOLIVE.md — {today.date()}, "
          f"{len(log)} log entries\n")
    month = log["asof"].dt.strftime("%Y-%m")
    have = [m for m in REQUIRED_MONTHS
            if ((month == m) & (log["asof"].dt.day >= 24)).any()]
    if len(have) < len(REQUIRED_MONTHS):
        print(f"NOT DUE: month-end entries present for {have or 'none'} "
              f"of {list(REQUIRED_MONTHS)}. Review runs 2026-10-15.")
        return

    p = features._panel(None, None)
    ctx = features._context(p)
    g1 = gate1(log)
    print(f"GATE 1 operational: {'PASS' if not g1 else 'FAIL'}")
    for f in g1:
        print(f"    - {f}")
    g2 = gate2(log, p, ctx)
    print(f"GATE 2 behavioral:  {'PASS' if not g2 else 'FAIL'}")
    for f in g2:
        print(f"    - {f}")
    corr, n = gate3(log, p)
    if corr is None:
        g3 = f"DEFERRED ({n}/{MIN_OVERLAP} overlapping invested days)"
        combo = False
    else:
        g3 = f"corr={corr:.2f} over {n} days → " + \
             ("combo CONFIRMED" if corr < CORR_MAX else "combo DEAD")
        combo = corr < CORR_MAX
    print(f"GATE 3 combo:       {g3}")

    print()
    if g1 or g2:
        print("VERDICT: NOT LIVE. Fix the specific cause, extend paper "
              "2 clean month-ends, re-run verbatim. No strategy changes.")
    elif combo:
        print("VERDICT: LIVE from Oct-31 rebalance — 70/30 v4/low-vol "
              "per PROTOCOL_V13.1.")
    else:
        print("VERDICT: LIVE from Oct-31 rebalance — pure v4."
              + (" Combo deferred, stays candidate." if corr is None
                 else " Combo dead."))
    print("Sizing: decided privately AFTER this verdict; cannot flip it.")


if __name__ == "__main__":
    main()
