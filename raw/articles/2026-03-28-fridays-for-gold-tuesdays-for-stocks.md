# Fridays for Gold, Tuesdays for Stocks: Two Sides of the Same Fear Cycle

**Source**: https://beyondpassive.substack.com/p/fridays-for-gold-tuesdays-for-stocks
**Date**: 2026-03-28
**Author**: Beyond Passive Investing
**Tags**: #strategy #day-of-week #mean-reversion #vix #gold #equities

---

The previous article showed that gold drifts higher on Fridays — specifically when the VIX term structure compresses into the extended fear zone, driven by institutional risk managers adding weekend protection on Thursday afternoons. The same day-of-week chart that opened that article contains a second significant bar on the opposite side of the cycle. Equities on Tuesday. This article examines that effect: what drives it, how to isolate it, and how it combines with the Friday gold strategy to form a day-of-week ensemble that shares the same capital without ever occupying it simultaneously.

## The Starting Observation

Across the full sample, sorting daily returns by weekday produces a chart that is almost entirely noise. Two results pass a standard significance test at the 5% level.

- Gold on Friday (p = 0.022)
- Equities on Tuesday (p = 0.024)

The Friday gold premium is an institutional story — risk managers systematically bid gold into Thursday close as weekend insurance, and sell it again on Monday. The Tuesday equity effect operates through a different mechanism and a different actor. Retail investors who absorb weekend news execute on Monday: selling at the gap open from overnight sentiment, then continuing intraday. Institutions recognise the oversell and accumulate during the Monday session. Tuesday is the reversal as that institutional bid asserts itself. Both effects are expressions of the same weekly fear cycle seen from opposite angles.

## Conditioning on Prior Price Action

The unconditional Tuesday drift is real but diluted. The question is whether the two sessions immediately preceding Tuesday — Friday and Monday — carry information about the likely magnitude of the reversal. The hypothesis is straightforward: a turnaround requires prior selling. If Monday closed higher than Friday, there is no oversold condition to reverse. The data confirms this asymmetry sharply.

Every condition involving Monday closing lower produces a statistically significant result. The two-day-down condition — requiring two consecutive negative sessions ending on Monday — produces the highest per-trade mean at **+0.452%**. Monday-down alone produces a higher t-statistic at **3.22** because the larger sample (345 vs 152) more than compensates for the lower per-trade mean. The complement is equally informative: when Monday is up, the Tuesday edge is precisely zero across 763 observations. The Tuesday effect is a reversal phenomenon, not a general weekday drift.

## The VIX Term Structure

Price action alone captures part of the picture. The other part is the fear regime in which that price action occurs. The **VIX/VIX3M ratio** measures whether the market is pricing near-term risk above or below its three-month baseline — whether fear is building or already priced in.

### Decile 10 Carries the Effect

Full backwardation — decile 10 — is the regime where retail panic selling is most intense and institutional accumulation most deliberate. If the Tuesday reversal is driven by institutional absorption of retail overselling, it should be strongest precisely here. The decile analysis across three conditioning levels confirms this without ambiguity.

Mean VTI Tuesday return by Monday-close VIX/VIX3M decile across three conditioning levels:
- **Panel A**: unconditional
- **Panel B**: Thursday-to-Friday close down
- **Panel C**: gap and intraday both negative on Monday

In all three panels, decile 10 dominates. Deciles 1 through 8 are statistically indistinguishable from zero in nearly every configuration. Under Panel C, D10 reaches **+1.01% with p = 0.051**.

The Tuesday effect is not a general weekday anomaly that happens to be somewhat stronger in fear regimes. It is almost entirely a decile-10 phenomenon.

## Choosing the Filter — What the Numbers Say

Complete statistical summary for all conditions. “N for t = 2” is derived from rearranging the t-statistic formula: N = (2σ/μ)² — the number of forward trades needed to confirm the edge independently of the backtest.

**Key findings:**
- Within D10, requiring Monday to close lower produces **t = 3.04** across 66 observations — stronger than requiring the full two-day-down condition (t = 2.87, N = 42) because the larger sample more than compensates for the slightly lower mean.
- Outside D10, non-D10 with Monday down alone reaches only **t = 1.44 (p = 0.15)**, and non-D10 with two-day down reaches **t = 1.49 (p = 0.14)**. Neither stands on its own statistical merits.

**The ensemble rule:**
> Enter if **D10 and Monday closed lower than Friday** — the regime is sufficient confirmation — or if **not in D10 but both prior sessions closed lower**, accepting that this leg adds frequency and marginal return without a standalone statistical claim.

The ensemble runs at **t = 3.29** across 176 observations and **10 trades per year**.

## What Conditioning Does to the Distribution

- **Panel A (all daily VTI returns)**: mean +0.049%, slightly left-skewed
- **Panel B (all Tuesdays)**: mean +0.082%, skewness turns positive
- **Panel C (ensemble filter)**: mean **+0.469%**, t = 3.29, skewness +0.79

Standard deviation rises because higher-fear environments are more volatile; the mean rises faster and the left tail compresses. The worst ensemble trade is materially smaller than the worst unconditional Tuesday return.

## The Strategy in Practice

**Unconditional Tuesday VTI (every Tuesday):**
- Max drawdown: −12.3%
- Sharpe: 0.55
- 44 trades per year

**Ensemble-filtered Tuesday VTI:**
- Max drawdown: −6.1%
- Sharpe: **0.75**
- **10 trades per year**
- Same terminal value on one-quarter of the trades

The unconditional strategy and the filtered strategy reach essentially the same terminal value over 17.5 years. The filter removes three-quarters of the trades and halves the drawdown without sacrificing return.

## Combining with the Friday Gold Strategy

The Friday gold strategy holds GLD from Thursday close to Friday close. This strategy holds VTI from Monday close to Tuesday close. There is no day on which both are simultaneously active. The correlation of their daily return series — computed over the full 252-day calendar including all cash days — is **−0.003**.

**Performance (100% position size, 17.5 years):**
| Strategy | Terminal Value | Sharpe | Max DD |
|----------|---------------|--------|--------|
| Friday GLD | $1.97 | 0.93 | — |
| Tuesday VTI Ensemble | $2.21 | 0.75 | −6.1% |
| **Combined** | **$4.36** | **1.18** | — |

The combined strategy deploys capital on **9.8% of trading days** — roughly **25 trades per year**.

Both figures are CAGR divided by annualised daily standard deviation computed over the complete trading calendar including all zero-return days. The t-statistic on the combined return series is **4.99**.

## Why This Belongs in a Portfolio

Most equity strategies suffer in fear regimes. This one activates in them. The ensemble’s statistical power comes almost entirely from decile 10 — full backwardation, the signature of genuine crisis. A strategy with positive expectancy precisely when volatility spikes carries implicit long-vol characteristics: it pays when the rest of the portfolio is under stress. That property is difficult to replicate and expensive to buy through options. Here it arrives as a byproduct of the mechanism itself.
