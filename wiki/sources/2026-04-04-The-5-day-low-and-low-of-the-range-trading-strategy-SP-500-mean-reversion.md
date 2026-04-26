# The 5-day low and low of the range trading strategy (S&P 500 mean reversion)

**Source**: [[2026-04-04-The-5-day-low-and-low-of-the-range-trading-strategy-(S&P-500-mean-reversion)]] | [Unknown](https://quantifiedstrategies.substack.com/p/the-5-day-low-and-low-of-the-range)
**Date**: 2026-04-04
**Tags**: #article #substack #strategy #mean-reversion #equities

## One-Sentence Summary

> The 5-day low and low of the range trading strategy (S&P 500 mean reversion)
QuantifiedStrategies.com
Aug 01, 2024
1
Share
The 5-Day Low of The Range Strategy, with its simple criteria of IBS lower th...

## Key Insights

1. **原文来源**: [Unknown](https://quantifiedstrategies.substack.com/p/the-5-day-low-and-low-of-the-range)

## Full Content

The 5-day low and low of the range trading strategy (S&P 500 mean reversion)
QuantifiedStrategies.com
Aug 01, 2024
1
Share
The 5-Day Low of The Range Strategy, with its simple criteria of IBS lower than 0.25 and the close lower than the lowest low of the previous 5 days, has shown remarkable results. Over the period from January 1993 until today, it has yielded 309 winners out of 517 trades, with an average return of 0.46% per trade—far exceeding the average return for any 5-day period.
We backtest the following trading rules:
- IBS must be lower than 0.25.
- The close must be lower than the lowest low the previous 5 days.
- If those two simple criteria are met, go long at the close.
- The exit is at the close 5 days later.
This is a very simple strategy. No fancy tools and hardly any calculations.
Below is shown the result from January 1993 until today.
1
Share
Previous
Next

---

*由 Substack Strategy Tracker 自动抓取*

---

## Reproduced: 5-Day Low of The Range (2026-04-26)

Deployed to `cta_developer` as `FiveDayLowRangeStrategy` (alias `FDLR` / `5DLR`).

**Strategy Rules (from original article):**
- IBS (Internal Bar Strength) < 0.25
- Close < lowest low of past 5 days
- Entry: at close | Exit: 5 days later at close
- Original: 517 trades, 309 wins (59.8%), avg return 0.46%/trade (SPY 1993-2024)

**Batch Pipeline: 24 ETFs GA Optimized (2006-2026)**

| Rank | Symbol | Sharpe | Trades | MaxDD% | AnnRet% | Opt Params |
|------|--------|--------|--------|--------|---------|------------|
| 1 | **XLP** | **0.82** | 144 | -0.1% | 0.03% | LLV6 IBS0.275 Hold6 |
| 2 | EEM | 0.74 | 130 | -0.1% | 0.02% | LLV6 IBS0.325 Hold4 |
| 3 | XLK | 0.62 | 250 | -0.1% | 0.04% | LLV4 IBS0.325 Hold4 |
| 4 | XLY | 0.56 | 274 | -0.1% | 0.04% | LLV4 IBS0.325 Hold4 |
| 5 | SPY | 0.56 | 464 | -0.5% | 0.13% | LLV4 IBS0.325 Hold4 |
| 6 | QQQ | 0.53 | 452 | -0.4% | 0.11% | LLV4 IBS0.325 Hold4 |

**Results: 🟢 6 Green (Sharpe≥0.5) | 🟡 16 Yellow | 🔴 2 Red**

**Key Findings:**
- **XLP (Consumer Staples)** tops at Sharpe 0.82 — defensive sector shows strongest IBS+LLV mean reversion
- SPY: 464 trades over 20 years (~23/yr), close to original article's 517 (1993-2024)
- GA optimization shifted IBS threshold from 0.25 to 0.275-0.325, LLV from 5 to 4-6, hold from 5 to 4-6
- Only 2 negative Sharpe (XLE, SHY, USO) — commodities/bonds not suitable
- Character: ultra-low drawdown (≤0.5% for all), ultra-low returns (AnnRet 0-0.13%) — **capital preservation tool**
