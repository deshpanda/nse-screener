# nse-screener

EOD momentum screener for NSE equities. Free public data only.
Pipeline: ingest NSE bhavcopy (OHLCV + delivery %), bulk/block deals, FII/DII flows
→ store as parquet → run Minervini-style trend template + RS rank + VCP proxy
+ institutional-footprint overlays → daily ranked shortlist.

**This screens candidates. It does not tell you what to buy.**
Nothing goes live until it beats Nifty in a backtest after costs.

## Setup

```bash
pip install -r requirements.txt
python backfill.py --days 420        # ~2 min per 100 days, be patient with NSE
python daily.py                      # run every evening after ~7pm IST
python -m screener.screen            # writes data/shortlist_YYYY-MM-DD.csv
```

## Notes

- NSE blocks non-browser user agents and rate-limits aggressively. The client
  sends browser headers, warms up a session cookie, retries, and sleeps between
  requests. If you get 403s, increase SLEEP_SECS in config.py or run later at night.
- Bhavcopy (`sec_bhavdata_full`) is published on trading days only; 404 = holiday,
  the backfill skips silently.
- Data lands in `data/` as parquet partitioned by date. Delete a date dir to re-pull.
- FII/DII endpoint returns aggregate cash-market flows only (no stock-level data —
  that granularity does not exist publicly).

## Layout

```
ingest/nse.py        shared NSE HTTP session
ingest/bhavcopy.py   OHLCV + delivery qty/% per symbol
ingest/bulk_deals.py bulk + block deals
ingest/fii_dii.py    aggregate FII/DII buy/sell
backfill.py          historical pull
daily.py             today's pull (cron this)
screener/screen.py   trend template + RS + VCP proxy + overlays
```
