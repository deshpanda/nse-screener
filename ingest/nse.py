"""Shared NSE HTTP client. NSE blocks obvious bots: send browser headers,
warm up cookies against the homepage before hitting /api/, retry on 401/403."""
import time
import requests

HEADERS = {
    "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                   "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"),
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.nseindia.com/",
}

_session = None


def session() -> requests.Session:
    global _session
    if _session is None:
        s = requests.Session()
        s.headers.update(HEADERS)
        try:  # cookie warmup, needed for www.nseindia.com/api/* endpoints
            s.get("https://www.nseindia.com", timeout=15)
        except requests.RequestException:
            pass
        _session = s
    return _session


def get(url: str, timeout: int = 30, retries: int = 3) -> requests.Response:
    for attempt in range(retries):
        try:
            r = session().get(url, timeout=timeout)
            if r.status_code in (401, 403):
                # cookie expired / bot-flagged: rebuild session, back off
                globals()["_session"] = None
                time.sleep(3 * (attempt + 1))
                continue
            return r
        except requests.RequestException:
            if attempt == retries - 1:
                raise
            time.sleep(3 * (attempt + 1))
    return r
