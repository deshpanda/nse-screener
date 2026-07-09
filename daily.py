"""Daily pull: today's bhavcopy + deals + FII/DII. Cron it for ~19:30 IST.
    30 19 * * 1-5  cd /path/to/nse-screener && python daily.py >> cron.log 2>&1
"""
from datetime import date, timedelta

from ingest import bhavcopy, bulk_deals, corporate_actions, fii_dii


def main() -> None:
    d = date.today()
    ok = bhavcopy.store(d)
    print(f"bhavcopy {d}: {'ok' if ok else 'not available yet (or holiday)'}")
    bulk_deals.store(d)
    fii_dii.store(d)
    # keep the CA file fresh: re-pull a trailing+leading window and merge
    corporate_actions.store(d - timedelta(days=30), d + timedelta(days=60))
    print("done")


if __name__ == "__main__":
    main()
