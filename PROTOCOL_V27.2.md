# v27.2: confirmation gauntlet for the N500 announce→effective add cell — pre-registration (2026-07-14)

## What is being confirmed

The single surviving cell of PROTOCOL_V27.1: Nifty-500 additions,
bought at next open after the ANNOUNCEMENT, sold at the close of the
EFFECTIVE date. Decision-window pass was marginal (+0.14pp over the
bar, n=94); OOS was same-direction but sub-bar. Both windows are now
SPENT — no further hypothesis mining happens on them. This protocol
defines the only two things that can still be learned honestly:
whether the existing pass is a plateau or a spike (Stage A), and
whether it repeats on data that does not exist yet (Stage B).

The declared cell is frozen. No perturbation below can ever be
promoted to "the strategy" — they exist to test fragility, not to
find better settings.

## Stage A — robustness diagnostics on the spent windows (run now)

Perturbations of the declared cell, IS window, all pre-listed:
1. entry at announce+2 open (one day later)
2. entry at announce+1 close (same day close instead of open)
3. exit at effective−2 close (leave early)
4. exit at effective+5 close (overstay into the fade)
5. liquidity floor ₹2.5cr (half)
6. liquidity floor ₹10cr (double)
7. IS first half only (2023-01→2024-12)
8. IS second half only (2025-01→2027-01)

Pass bars (frozen):
- **A1 plateau**: in ≥ 6 of 8 perturbations the cell's mean excess
  stays ABOVE both null means (sign/ordering stability — the +3pp bar
  is not re-applied to perturbations; a plateau degrades gracefully).
- **A2 not-a-lottery** (the v21 lesson): group event excess by
  calendar quarter; the best quarter's share of summed positive
  quarterly excess must be < 40%.
- **A3 tax-viability**: with after-tax event return defined as
  r − 0.20·max(r, 0) (all holds ≤ 1yr ⇒ STCG), the cell's mean
  after-tax excess must remain above both nulls' (same transform).

Any Stage-A failure = the cell is downgraded to DEAD (spike), Stage B
is cancelled, and the scoreboard says so.

## Stage B — fresh-data confirmation (the real test)

- Universe of new evidence: N500 add events with ANNOUNCE date after
  2026-07-14 (this commit). The press-release archive is immutable and
  NSE-timestamped, so events need no live logging — the review script
  re-scrapes and re-parses (ingest.reconstitution list/pdfs/parse) at
  review time with zero hindsight risk.
- Review date: the later of 2027-04-01 or ≥ 30 fresh add events.
- Bars: IDENTICAL to PROTOCOL_V27.1 (mean ≥ +3pp above both nulls,
  medians above both, n ≥ 30) — the marginal pass must repeat, not
  merely rhyme. Nulls constructed by the same code, same seeds.
- Pass ⇒ sleeve-design conversation + its own paper phase (2027-H2 at
  the earliest). Fail ⇒ DEAD, and the v27 scoreboard row is updated to
  say the confirmation failed.

## Registered prediction

Stage A passes (the effect looked temporally spread, not lottery-like,
and survives its own tax math at ~25-day holds). Stage B is a genuine
coin flip given the margin — that is precisely why it exists.

## Amendments

None after this commit.
