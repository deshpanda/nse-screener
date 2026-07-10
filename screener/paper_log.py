"""v4-regime paper-trade log. Run on each month's last trading day (and
whenever you want a checkpoint):

    python -m screener.paper_log            # append today's state
    python -m screener.paper_log --report   # paper P&L vs Nifty so far

Appends to paper/log.csv: what the strategy holds, the benchmark level,
and equal-weight entry prices. The log is append-only history — the whole
point is that it can't be rewritten after the fact.
"""
import argparse
import json
import subprocess
from pathlib import Path

import pandas as pd

import config
from backtest import features

PAPER = Path(__file__).resolve().parent.parent / "paper"
LOG = PAPER / "log.csv"
STATUS = PAPER / "status.json"


def _push(msg: str) -> None:
    """Best-effort publish of paper/ to the public repo (site reads it)."""
    root = PAPER.parent
    try:
        subprocess.run(["git", "add", "paper"], cwd=root, check=True,
                       capture_output=True)
        dirty = subprocess.run(["git", "status", "--porcelain", "paper"],
                               cwd=root, capture_output=True, text=True)
        if not dirty.stdout.strip():
            return
        subprocess.run(["git", "commit", "-q", "-m", msg], cwd=root,
                       check=True, capture_output=True)
        subprocess.run(["git", "push", "-q", "origin", "main"], cwd=root,
                       check=True, capture_output=True, timeout=120)
        print("→ published to repo (site will reflect it)")
    except Exception as e:                    # offline is fine; next run carries it
        print(f"→ publish skipped ({type(e).__name__})")


def build_status(regime_on: bool, t, bench_now: float,
                 n_holdings: int, n_lowvol: int,
                 stance: str | None = None) -> None:
    log = pd.read_csv(LOG) if LOG.exists() else pd.DataFrame()
    STATUS.write_text(json.dumps({
        "updated": str(pd.Timestamp.now().date()),
        "asof": str(t.date()),
        "regime": "ON" if regime_on else "OFF",
        "stance": stance or (f"{n_holdings} stocks held" if regime_on
                             else "100% cash — circuit-breaker open"),
        "lowvol_names": n_lowvol,
        "entries": int(len(log)),
        "nifty_start": float(log["niftybees"].iloc[0]) if len(log) else None,
        "nifty_now": bench_now,
    }, indent=1))


def snapshot() -> None:
    p = features._panel(None, None)
    ctx = features._context(p)
    close = p["close"]
    t = close.index[-1]

    bench = ctx["bench"]
    regime_on = bool(bench.loc[t] >= bench.rolling(200).mean().loc[t])

    liquid = (p["turnover_lacs"].rolling(20).median() >= 500).loc[t]
    if regime_on:
        mom = (close.shift(21) / close.shift(252) - 1).loc[t]
        ok = liquid.reindex(mom.index, fill_value=False)
        ok[[s for s in mom.index if s not in ctx["stocks"]]] = False
        top = mom[ok].dropna().nlargest(20)
        holdings = ";".join(f"{s}@{close.loc[t, s]:.2f}" for s in top.index)
    else:
        holdings = "CASH"

    # v13.1 sleeve B: low-vol 20 (always invested — no regime by spec)
    vol = close.pct_change().rolling(252, min_periods=200).std().loc[t]
    okv = liquid.reindex(vol.index, fill_value=False)
    okv[[s for s in vol.index if s not in ctx["stocks"]]] = False
    low20 = vol[okv].dropna().nsmallest(20)
    lowvol = ";".join(f"{s}@{close.loc[t, s]:.2f}" for s in low20.index)

    row = pd.DataFrame([{
        "asof": t.date(), "regime": "ON" if regime_on else "OFF",
        "holdings": holdings, "lowvol_sleeve": lowvol,
        "niftybees": round(float(bench.loc[t]), 2),
    }])
    LOG.parent.mkdir(exist_ok=True)
    header = not LOG.exists()
    row.to_csv(LOG, mode="a", header=header, index=False)
    print(row.to_string(index=False))
    print(f"→ appended to {LOG}")
    build_status(regime_on, t, round(float(bench.loc[t]), 2),
                 0 if holdings == "CASH" else holdings.count(";") + 1,
                 lowvol.count(";") + 1)
    _push(f"paper log: {t.date()}")


def refresh_status() -> None:
    """Daily hook: republish status ONLY when the regime flips — watchers
    see stance changes within a day without daily commit noise."""
    prev = json.loads(STATUS.read_text()) if STATUS.exists() else {}
    p = features._panel(None, None)
    ctx = features._context(p)
    t = p["close"].index[-1]
    bench = ctx["bench"]
    regime_on = bool(bench.loc[t] >= bench.rolling(200).mean().loc[t])
    if prev.get("regime") == ("ON" if regime_on else "OFF"):
        return
    build_status(regime_on, t, round(float(bench.loc[t]), 2), 0,
                 prev.get("lowvol_names") or 0,
                 stance=("regime flipped ON — portfolio forms at next "
                         "month-end" if regime_on else
                         "regime flipped OFF — exits at next month-end"))
    _push(f"regime change: {'ON' if regime_on else 'OFF'} as of {t.date()}")


def report() -> None:
    if not LOG.exists():
        raise SystemExit("No log yet. Run without --report first.")
    log = pd.read_csv(LOG, parse_dates=["asof"])
    p = features._panel(str(log["asof"].iloc[0].date()), None)
    close = p["close"]
    t = close.index[-1]

    equity = 1.0
    for i in range(len(log) - 1):
        h = log["holdings"].iloc[i]
        nxt = log["niftybees"].iloc[i + 1] / log["niftybees"].iloc[i]
        if h == "CASH":
            leg = 1.0
        else:
            rets = []
            for item in h.split(";"):
                sym, px = item.split("@")
                now = close.loc[:log["asof"].iloc[i + 1], sym].dropna()
                if len(now):
                    rets.append(now.iloc[-1] / float(px))
            leg = sum(rets) / len(rets) if rets else 1.0
        equity *= leg
        print(f"{log['asof'].iloc[i].date()} → "
              f"{log['asof'].iloc[i+1].date()}: strategy {leg-1:+.2%}, "
              f"nifty {nxt-1:+.2%}")
    bench_total = log["niftybees"].iloc[-1] / log["niftybees"].iloc[0]
    print(f"\npaper so far: strategy {equity-1:+.2%} vs nifty "
          f"{bench_total-1:+.2%} (since {log['asof'].iloc[0].date()})")


if __name__ == "__main__":
    a = argparse.ArgumentParser()
    a.add_argument("--report", action="store_true")
    if a.parse_args().report:
        report()
    else:
        snapshot()
