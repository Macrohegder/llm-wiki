---
title: "Pullback Trading Strategies (Backtest, Setup, Rules, Performance)"
author: QuantifiedStrategies.com
url: https://quantifiedstrategies.substack.com/p/pullback-trading-strategies-backtest
date: 2023-12-25
topics:
  - pullback
  - mean-reversion
  - RSI
  - trend-filter
  - MA
source: Substack
---

# Pullback Trading Strategies (Backtest, Setup, Rules, Performance)

## Reproduced: SPY Pullback Strategy (2026-04-26)

We implemented this QuantifiedStrategies pullback strategy in vnpy CTA framework.

**Strategy Logic:**
- Entry: close > SMA(200) (uptrend) AND close < SMA(20) (short-term pullback) AND RSI(5) < 45
- Exit: RSI(5) > 65
- Data: SPY daily bars from 2006-05 to 2026-04 (5,027 bars)

**Results:**

| Version | Sharpe | Trades | MaxDD | Years |
|---------|--------|--------|-------|-------|
| Default params (SMA200/20, RSI5, 45/65) | **0.52** | 214 | -9.9% | 20yr |
| GA Optimized (SMA101/14, RSI3, 30/53) | **0.85** | 308 | **-4.8%** | 20yr |

**Key Observations:**
- The trend filter (SMA200) ensures entries only during uptrends, avoiding bear markets
- RSI exit at 65 captures quick mean reversion profit without holding too long
- Low drawdown (-4.8% GA, -9.9% default) makes this suitable for capital preservation
- Returns are modest (+0.36% total over 20yr) due to infrequent entry signals
- The SMA200 filter severely limits opportunities in a long-term bull market

**Verdict: 🟡 Yellow** — Solid risk metrics (Sharpe 0.85, low DD) make this useful as a portfolio hedge or capital preservation component, but absolute returns are too low to use as a standalone strategy. Better suited as a timing filter for other strategies.

## Summary

A pullback mean reversion strategy:
1. Close > 200-day SMA (long-term uptrend filter)
2. Close < 20-day SMA (short-term pullback)
3. 5-day RSI < 45 (oversold on short timeframe)
4. Entry: at close when all 3 conditions true
5. Exit: at close when 5-day RSI > 65

Backtested on SPX from 1993 to Sep 2021, $100k compounded.
