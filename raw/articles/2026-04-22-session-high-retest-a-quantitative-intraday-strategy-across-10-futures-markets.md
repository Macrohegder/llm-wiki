---
title: "Session High Retest: A Quantitative Intraday Strategy Across 10 Futures Markets"
url: "https://open.substack.com/pub/delphicalpha/p/session-high-retest-a-quantitative"
date: "2026-04-22"
author: "Delphic Alpha"
source: "delphicalpha"
tags: ["intraday", "futures", "long-only", "session-high", "breakout", "mean-reversion"]
---

# Session High Retest: A Quantitative Intraday Strategy Across 10 Futures Markets

Price rallies from the open, pulls back, then retests the session high. Does it break through or stall? We tested 16 configurations across 10 instruments over 17 years of 5-minute data to find out. This is a long-only strategy — every trade is a buy.

There's a setup that every intraday trader recognises intuitively: the market opens, rallies, pulls back, then tries to retest its high. If it breaks through, you're riding a trend. If it fails, you gave back your gains.

The problem is that most traders never test which version of this setup actually works. How big does the rally need to be? How deep should the pullback go? Does it matter whether you're trading Gold or the Nasdaq?

I tested it. Rigorously. Every Sharpe ratio and win rate below represents a long-only, buy-the-retest strategy — buying breakout continuation after a pullback, holding to the session close. The answer is not what I expected.

## The Setup

The strategy has four phases:

1. **Rally:** Price moves at least 75–150 basis points above the RTH (Regular Trading Hours) open. This confirms real directional momentum, not noise.
2. **Pullback:** Price pulls back at least 10 bps from the session high. We need a genuine pullback, not a single tick retracement.
3. **Retest:** After the pullback bottoms, price returns to within 10 bps of the session high. This is the trigger.
4. **Entry & hold (long only):** Go long at the close of the retest bar. Hold until RTH close. No stop loss.

Simple enough. But the raw signal is noisy — and that's where the interesting finding lives.

## The Critical Filter: How Deep Was the Pullback?

I tested four pullback filters across all 10 instruments:

- **No filter** — take every retest signal
- **Shallow pullback (<= 38.2% Fibonacci retracement)** — the pullback barely dipped before retesting
- **Deep pullback (>= 50% retracement)** — a full V-recovery from a meaningful pullback
- **Held above open** — the pullback never went below the RTH open

On average across all instruments, deep pullbacks produce the highest Sharpe (0.58), significantly better than no filter (0.21). But here's the catch: this average hides a critical split.

## Two Groups of Instruments

When I broke out the results by instrument, a clear pattern emerged.

Some instruments strongly prefer shallow pullbacks. Others strongly prefer deep pullbacks.

The split is consistent and large enough to be actionable:

**Shallow pullback works best on:**
NQ, PL, HG, SI, GC, PA — mostly metals plus the Nasdaq. When these instruments barely pull back before retesting, it signals strong demand and the breakout tends to stick.

**Deep pullback works best on:**
FDAX, NKD, ES, YM — the equity indices (except NQ). These instruments need a full V-recovery to confirm genuine buying interest. The shallow pullback on DAX or S&P is more likely a head-fake.

This is not a small difference. The DAX with its best filter (deep pullback, 150 bps rally) posts a **Sharpe of 4.56**. The same instrument with a shallow pullback filter is mediocre. NQ with shallow pullback: **Sharpe 2.24**. NQ with deep pullback: barely positive.

## The Full Instrument Ranking

Every instrument is positive with its best configuration. The portfolio-level numbers using each instrument's best config:

- **Portfolio Sharpe (long-only):** 1.15
- **Annual Return:** +13.6%
- **Annual Volatility:** 11.8%
- **Max Drawdown:** -16.2%
- **Win Rate:** 54.6%

Notably, 9 out of 10 instruments are positive even with the worst filter. The edge is real — the filter just concentrates it.

## Win Rate vs. Expansion: What Happens After the Retest?

One of the most interesting metrics is the **expansion rate** — how often price makes a new session high after the retest entry. This tells you whether the retest is a genuine breakout or a double-top trap.

The equity indices with deep pullback filters show the highest expansion rates: **ES at 97.9%, NKD at 96.4%, FDAX at 95.7%**.

When these instruments pull back 50%+ and then fully recover, they almost always push to new highs. The question is only whether the expansion is large enough to be profitable by the session close — and win rates of 58–67% confirm that it usually is.

Metals show lower expansion rates (77–87%) but compensate with higher trade frequency. NQ is the outlier — an equity index that behaves like a metal, preferring the shallow pullback with 89.4% expansion.

## Where the Profits Come From

NQ dominates total profit with 6,462 bps across 830 trades — about 7.8 bps per trade. That's roughly 3.9 NQ points per trade on a 5-minute chart, which is comfortably above typical execution costs for a single-contract retail trader.

The DAX is an efficiency machine: only 46 trades (about 3 per year), but 56 bps per trade and a Sharpe of 4.56. If you can only monitor one instrument for this setup, FDAX with a deep pullback filter is the highest Sharpe configuration in the entire dataset.

## The Step-by-Step Rules

For anyone who wants to implement this:

1. Load 5-minute bars for your instrument during Regular Trading Hours.
2. Record the RTH Open price.
3. Track the running session high.
4. Wait for it to reach your rally threshold above the open (75–150 bps depending on instrument).
5. Wait for a pullback of at least 10 bps from the session high. Confirm the pullback has bottomed (next bar's Low is higher than the pullback Low).
6. Apply the pullback filter:
   - **NQ, PL, HG, SI, GC, PA:** require the pullback to retrace <= 38.2% of the rally.
   - **FDAX, NKD, ES, YM:** require the pullback to retrace >= 50% of the rally.
7. Watch for the retest: price returns to within 10 bps of the session high.
8. Go long at the close of the retest bar. This is a long-only strategy.
9. Hold until RTH close. No stop loss.

## The Instrument Cheat Sheet

Every instrument's optimal configuration from the grid scan:

| Instrument | Rally | Filter | Sharpe | Trades | Win Rate |
|-----------|-------|--------|--------|--------|----------|
| NQ (Nasdaq) | 75 bps | shallow | +2.24 | 830 | 56.9% |
| PL (Platinum) | 75 bps | shallow | +2.50 | 395 | 56.5% |
| FDAX (DAX) | 150 bps | deep | +4.56 | 46 | 67.4% |
| GC (Gold) | 150 bps | shallow | +2.46 | 104 | 48.1% |
| NKD (Nikkei) | 125 bps | deep | +2.40 | 56 | 64.3% |
| HG (Copper) | 125 bps | shallow | +1.98 | 355 | 51.3% |
| YM (Dow) | 125 bps | deep | +1.85 | 74 | 59.5% |
| ES (S&P 500) | 125 bps | deep | +1.80 | 95 | 58.9% |
| SI (Silver) | 100 bps | shallow | +1.05 | 354 | 50.8% |
| PA (Palladium) | 75 bps | shallow | +0.91 | 312 | 52.9% |

## Why This Works (And Why Most People Get It Wrong)

The raw "session high retest" signal is nearly worthless. If you take every retest with no filter, you get a Sharpe of 0.21 — barely above noise. Most traders who try this setup and give up are trading the unfiltered version.

The pullback filter transforms the signal because it separates two different market microstructures:

- **Shallow pullbacks** in metals/NQ indicate strong underlying demand. The barely-there pullback means aggressive buyers are stepping in immediately. The retest is just confirmation before continuation.
- **Deep pullbacks** in equity indices represent a more complex auction. Price needs to probe lower, find real buyers at support, and build a base before the next leg up. The V-recovery from 50%+ retracement is evidence that the buying is genuine, not just momentum chasing.

NQ's behaviour as a "metal" in this context likely reflects its concentration in mega-cap tech — when institutional buyers want Nasdaq exposure, they're aggressive and don't wait for deep pullbacks.

## Limitations and Caveats

1. **No stop loss.** The strategy holds to session close regardless. Intraday drawdowns can be significant, especially on metals. In practice, you'd want a catastrophic stop for gap risk.
2. **Long-only.** This only captures upside continuation. A mirror strategy for session low retests exists but wasn't tested here.
3. **Transaction costs not included.** With bps/trade ranging from 4.6 (GC) to 56 (FDAX), most instruments clear typical retail futures commissions comfortably, but check your own costs.
4. **Optimal parameters were selected in-sample.** The grid scan identifies the best rally threshold and filter per instrument, which introduces look-ahead bias. The correct approach is walk-forward validation, which would likely reduce Sharpe by 20–40%.
5. **This is one strategy.** A portfolio of day trading strategies with uncorrelated signals will outperform any single setup.

## What's Next

This is the first in a series covering the 7 strategies in the Day Trading Playbook. Next up: the Opening Dip Buy — what happens when price sweeps below the open in the first 45 minutes, and why the 100 bps threshold is the magic number.

*Analysis based on FRD continuous ratio-adjusted futures, 5-minute bars. 10 instruments: GC, SI, HG, PL, PA, ES, NQ, FDAX, NKD, YM. Data period: 2008–2025. Not financial advice.*
