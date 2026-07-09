"""v4-regime live portfolio: what the strategy holds as of today.

    python -m screener.monthly_portfolio

Prints regime state and the current top-20 momentum names. PAPER TRADING
ONLY until the 2-3 month paper phase confirms live behavior matches the
backtest (PROTOCOL_V4.md passed 2026-07-09; that is necessary, not
sufficient). Rebalance only on the month's last trading day.
"""
import pandas as pd

import config
from backtest import features


def main() -> None:
    p = features._panel(None, None)
    ctx = features._context(p)
    close = p["close"]
    t = close.index[-1]

    mom = (close.shift(21) / close.shift(252) - 1).loc[t]
    liquid = (p["turnover_lacs"].rolling(20).median() >= 500).loc[t]
    ok = liquid.reindex(mom.index, fill_value=False)
    ok[[s for s in mom.index if s not in ctx["stocks"]]] = False

    bench = ctx["bench"]
    regime_on = bench.loc[t] >= bench.rolling(200).mean().loc[t]

    top = mom[ok].dropna().nlargest(20)
    out = pd.DataFrame({
        "mom_12_1_pct": (100 * top).round(1),
        "close": close.loc[t, top.index].round(2),
        "rs_pctile": ctx["rs_pctile"].loc[t, top.index].round(0),
    })

    print(f"as of {t.date()}  |  regime: "
          f"{'ON — hold the portfolio' if regime_on else 'OFF — be in cash'}")
    print(out.to_string())
    path = config.DATA_DIR / f"v4_portfolio_{t.date()}.csv"
    out.to_csv(path)
    print(f"→ {path}")


if __name__ == "__main__":
    main()
