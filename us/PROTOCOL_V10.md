# v10: 13F guru-cloning — pre-registration

Committed BEFORE the first run. The most-sold version of "follow smart
money": buy what famous hedge funds disclose buying. 13F holdings are
filed up to 45 days after quarter-end — the STALEST footprint we test.
Prior after v9 (2-day disclosure, dead since ~2023): very low. Run for
completeness — this is the "clone Buffett" app pitch, tested honestly.

## Funds (frozen list — all famous BEFORE 2016 to limit hindsight bias;
residual bias remains and is disclosed: they're famous partly because
they won historically, which flatters this test)

Berkshire Hathaway · Appaloosa · Baupost · Pershing Square · Third Point
· Greenlight Capital · Lone Pine · Viking Global · Tiger Global · Coatue
· Duquesne Family Office · Icahn Capital/Carl Icahn · ValueAct · Soros
Fund Management · Paulson & Co. (CIKs resolved programmatically from
EDGAR; any fund that stopped filing simply stops producing events.)

## Event definition (frozen)

- NEW position: ticker present in fund's 13F for quarter Q, absent in
  its Q-1 filing, with position value ≥ 1% of the fund's total 13F value
- event date: the FILING date (public knowledge), never quarter-end
- one event per ticker per 63 sessions across all funds (first wins)
- universe: S&P 500 member on event date (price data honesty)
- issuer names mapped to tickers via SEC company_tickers.json normalized
  matching; unmatched names dropped and the drop-rate reported
- entry next session's open; hold 63 sessions; excess vs SPY

## Windows

in-sample 2023→present · out-of-sample 2016–2022, frozen

## Grid (one-at-a-time, both windows)

weight ≥0.5% · consensus (≥2 funds, same quarter) · hold {21, 126}

## Pass criteria: identical to PROTOCOL_V9 (mean AND median excess > 0
in-sample; grid majority; same OOS; quarter concentration ≤ 25%)
