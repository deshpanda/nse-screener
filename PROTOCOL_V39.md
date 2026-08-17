# v39: rights-entitlement (RE) discount capture — pre-registration (2026-08-19)

## Why & family

NEW family: primary-market plumbing (no prior test touches it — all
windows virgin). REs are the tradable right to subscribe to a rights
issue. They exist for a few sessions, then expire worthless if unsold
and unexercised — Zerodha clients alone lapsed ~Rs 10cr of REs
May-2020→Mar-2021 (Kamath, Mar-2021). Time-boxed, price-insensitive
forced supply with no natural arbitrageur is a structurally different
reason for mispricing than any information story we have tested.
No published Indian backtest exists; this builds the dataset.

## Data (format review done BEFORE this protocol — facts frozen)

- `data/rights_re/re_trades.parquet` — RE trades harvested from raw NSE
  archives, **series E1-E9** (verified: TATASTEEL E1, 70,492 shares,
  2020-05-27). The main panel filters to EQ, so this data has been
  invisible to all 34 prior studies; config.SERIES stays untouched.
- `data/rights_re/issues.parquet` — 243 rights issues 2019-2026 from the
  corporate-actions API.
- **Issue price = faceVal + premium**, both from the same feed; ratio
  from the same subject string. Parse rate **228/243 = 94%**, spot-
  validated against real history (BHARTIARTL 2019 Rs 220 at 19:67;
  IDEA Rs 12.50 at 87:38). Frozen regexes:
  ratio `(\d+(?:\.\d+)?)\s*[:/]\s*(\d+(?:\.\d+)?)`,
  premium `premium\s*(?:of\s*)?rs\.?\s*(\d+(?:\.\d+)?)`.
  Unparseable issues (6%) are DROPPED, not guessed.
- Theoretical RE value on day t = max(0, underlying_close(t) − issue_px).
  Discount = (theoretical − RE_close) / theoretical.

## Cells (frozen — entire grid)

- **D1 descriptive**: distribution of the discount across all issues and
  sessions; whether it widens toward the RE window's close. Answers "is
  the mispricing real", no pass/fail.
- **T1 the registered trade**: when an RE closes at a discount ≥ X% to
  theoretical, buy the RE at that close, subscribe (pay issue price),
  sell the resulting shares at the first tradable close after allotment.
  Net return = (share proceeds − RE cost − issue price) / (RE cost +
  issue price), minus 0.25%/side, minus **20% STCG** (verification
  established the buy-RE→subscribe→sell-shares route is STCG-taxed,
  unlike a bare RE flip). Thresholds frozen at **X = 5% and 10%** —
  two cells, no others.
- **T2 diagnostic**: the naive RE flip (buy RE, sell RE), taxed at
  **slab (~30%)** because RE sales carry no STT so s.111A does not
  apply. Reported, never promotable.
- Allotment assumption, stated: RE holders who subscribe are entitled to
  those shares — there is no IPO-style lottery. Partial/technical
  rejections are unmodelled and would reduce returns.

## Windows & pass (frozen)

IS 2023-01→2027-01 (decision). OOS 2020-01→2022-12 (single shot; RE
trading began 2020). Pass for T1 at either threshold requires ALL of:
1. mean net after-tax return per event > 0,
2. mean excess ≥ +3pp over the index over the identical holding days,
3. n ≥ 30 events in the window,
4. the v27.2 concentration check (best quarter < 40% of positive excess).
Fewer than 30 events ⇒ reported as DATA-LIMITED, not as a pass. Any T1
pass then needs a plateau check on the threshold before promotion.

## Registered predictions

1. D1: the discount is REAL and material (median mid-single-digit %,
   widening in the final sessions) — the lapse evidence demands it.
2. T1: FAILS the both-conditions bar, because the ~2-3 week unhedged
   gap between RE purchase and share sale swamps a 5-10% discount with
   directional risk, and rights issuers skew distressed (adverse
   selection).
3. T2 (flip) shows a positive gross edge destroyed by slab tax.
4. Event supply is the binding constraint: expect 30-80 usable events
   total, so a data-limited verdict is more likely than a clean one.

If T1 passes with n ≥ 30 and survives concentration, this is the first
structural (non-factor, non-information) edge the project has found.

## Amendments
None after this commit.

---

## ADDENDUM 2026-08-19 (same day; criteria above unchanged) — BLOCKED ON DATA

The data route this protocol assumed does not exist. Series E1/E2/E3 are
**partly-paid shares**, not rights entitlements: TATASTEEL/HATSUN E1 rows
predate RE trading entirely, and HATSUN's E1 window does not straddle its
rights record date. Direct verification then settled it — on 2020-05-26,
2020-05-28 and 2020-06-01, inside Reliance's RE trading window, the only
RELIANCE row in the full bhavcopy is series EQ. REs are not published in
the equity bhavcopy under any series.

Status: **BLOCKED-DOCUMENTED**, not dead. The hypothesis is untested and
the pass criteria above stand unamended for whenever a data route opens.
Untried routes, in rough order of promise: (1) NSE's separate rights-
entitlement reports//ISIN-keyed instrument files; (2) the BSE equivalent;
(3) reconstructing RE prices from broker/depository statements; (4) paid
vendor data. NOTHING in this protocol may be relaxed to fit whatever
route is found — if the new source cannot support these cells, the study
does not run.
