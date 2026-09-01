# v43: the buyback tender trade, per-event — pre-registration (2026-09-01)

## Disclosure first (two peeks, both stated before any cell runs)

1. **We have already seen an encouraging number.** On 2026-08-30 an
   INDICATIVE arithmetic was computed and published: median acceptance
   38.7% x median record-date premium +28.5%, minus the unaccepted
   portion at v40's −1.1% post-record drift, ≈ **+10.4% gross per
   event**. That is not a backtest — it multiplies medians of separate
   distributions, ignores costs and tax, and assumes an entry price it
   never modelled. This protocol is written knowing it, which is why
   the prediction below is deliberately far lower.
2. **v40 already characterised the price path** on these same events
   (no run-up into the record date; ~2pp of post-record weakness). That
   window is therefore partially spent; v43 asks a different question
   (what a tender actually RETURNS) but on overlapping data, and the
   overlap is declared rather than assumed harmless.

## The binding limitation: n = 41, and it is not a random 41

Only 41 events carry BOTH a validated acceptance ratio and a validated
tender price. Two consequences that cannot be engineered away:

- **No IS/OOS split is possible.** Splitting gives ~20 per window,
  below our own n>=30 floor. This is therefore a SINGLE-WINDOW,
  UNDERPOWERED study, and the strongest verdict it can ever produce is
  CONFIRMATORY-ONLY — meaning fresh events must repeat it before any
  capital is discussed. A pass here promotes nothing.
- **PARSE SELECTION BIAS, disclosed.** The 41 are the filings whose
  PDFs parsed. Scanned filings failed (ASHIANA-2023 being the
  documented case), and scans skew toward smaller, less organised
  issuers. So this sample likely over-represents larger buybacks, whose
  acceptance and premium behaviour may differ. The direction of the
  bias is unknown; its existence is not.

## Trade spec (frozen)

Eligibility requires holding on the record date, so entry must precede
it. Three entry cells, no others:
- **E1**: next open after the ANNOUNCEMENT date.
- **E2**: close 5 trading days before the record date.
- **E3**: close 2 trading days before the record date (the latest entry
  that settles in time).

Exit, frozen: the accepted fraction `a` (= small_acceptance, the
<=Rs 2L reserved category) is paid the tender price B; the unaccepted
(1 − a) is sold at the close 5 trading days AFTER the post-offer
announcement date (an approximation of when unaccepted shares are
credited back and tradable — disclosed as such).

Per-event return:
    gross = [a*B + (1-a)*P_exit] / P_entry - 1
    net   = gross - 0.50% round-trip costs
    after-tax = net - 20% STCG on any positive net (holding is weeks)
Excess = after-tax return minus the NIFTYBEES return over the identical
calendar days.

**All prices RAW, never CA-adjusted** (the documented trap: an adjusted
panel restates history for later splits and inflated our first premium
estimate to +52.6%). Any event with a split/bonus corporate action
between entry and exit is DROPPED, not adjusted.

## Pass criteria (frozen)

ALL of:
1. mean after-tax return per event > 0;
2. mean excess over the index >= +3pp;
3. n >= 30 after CA-window drops;
4. concentration — the single best event contributes < 25% of the
   summed positive excess (with n=41 one blowout event is the primary
   way a false positive appears here).

Reported for each of E1/E2/E3. A pass in any cell is CONFIRMATORY-ONLY:
it earns a fresh-events re-test, not capital, and nothing enters the
2026 go-live regardless (PROTOCOL_GOLIVE).

## Registered predictions

1. Mean net after-tax return lands **well below the indicative +10.4%**
   — my estimate is +2% to +6% per event — because medians do not
   compose, costs and STCG bite, and the unaccepted majority drags.
2. E3 (latest entry) beats E1, because v40 showed the stock drifts
   DOWN into the record date, so waiting buys cheaper.
3. The concentration check is the real risk and the likeliest single
   cause of failure at n=41.
4. Criterion 2 (+3pp over index) passes more easily than it should,
   because these are weeks-long holdings and the index barely moves —
   so criterion 1 and the concentration check carry the verdict.

## Amendments
None after this commit.
