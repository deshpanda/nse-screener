"""System watchdog: silent when healthy, loud when something rots.

    python scripts/health.py        # cron: every 4 waking hours

Checks the things that fail silently; on ANY failure fires a macOS
notification so breakage is noticed the day it happens, not at month-end.
Always appends one line to health.log so the watchdog itself is auditable.
"""
import json
import subprocess
import sys
from datetime import date, datetime, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FAILURES = []


def check(name, ok, detail=""):
    if not ok:
        FAILURES.append(f"{name}: {detail}")


def weekdays_ago(n):
    d, left = date.today(), n
    while left > 0:
        d -= timedelta(days=1)
        if d.weekday() < 5:
            left -= 1
    return d


def main():
    # 1. price panel freshness (allow 2 trading days of lag: NSE evening
    #    publication + one slept-through cron)
    bhav = sorted((ROOT / "data" / "bhav").glob("*.parquet"))
    check("panel", bool(bhav), "no bhav files at all")
    if bhav:
        last = date.fromisoformat(bhav[-1].stem)
        check("panel-freshness", last >= weekdays_ago(3),
              f"latest bhav is {last} (>3 trading days old)")

    # 2. daily cron ran recently and cleanly
    clog = ROOT / "cron.log"
    check("cron.log", clog.exists(), "daily cron has never written its log")
    if clog.exists():
        age = datetime.now() - datetime.fromtimestamp(clog.stat().st_mtime)
        check("cron-recency", age < timedelta(days=4),
              f"cron.log last written {age.days}d ago")
        tail = clog.read_text()[-4000:]
        check("cron-errors", "Traceback" not in tail,
              "Traceback in recent cron.log")

    # 3. paper trial log + month-end entry (checked from the 3rd onward)
    plog = ROOT / "paper" / "log.csv"
    check("paper-log", plog.exists(), "paper/log.csv missing")
    if plog.exists() and date.today().day >= 3:
        lines = plog.read_text().strip().split("\n")[1:]
        last_entry = date.fromisoformat(lines[-1].split(",")[0])
        check("month-end-entry", (date.today() - last_entry).days <= 35,
              f"last paper entry {last_entry} — month-end snapshot missed?")

    # 4. status.json valid
    try:
        json.loads((ROOT / "paper" / "status.json").read_text())
    except Exception as e:
        check("status.json", False, str(e))

    # 5. git remote reachable with cron-like env (publish path works)
    r = subprocess.run(["git", "fetch", "origin", "--dry-run"], cwd=ROOT,
                       capture_output=True, timeout=60)
    check("git-remote", r.returncode == 0,
          r.stderr.decode()[:80] if r.returncode else "")

    stamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    if FAILURES:
        msg = "; ".join(FAILURES)[:200]
        print(f"{stamp} FAIL {msg}")
        subprocess.run(["osascript", "-e",
                        f'display notification "{msg}" with title '
                        f'"nse-screener: HEALTH CHECK FAILED" sound name "Basso"'])
        sys.exit(1)
    print(f"{stamp} OK")


if __name__ == "__main__":
    main()
