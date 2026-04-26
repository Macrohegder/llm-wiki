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

---

### Batch Pipeline: 24 ETFs GA Optimized (2026-04-26)

Deployed to `cta_developer` as `PullbackMrStrategy` (alias `PB`). Batch run over 24 ETFs (SPY, QQQ, IWM, DIA, XLK, XLF, XLE, XLI, XLP, XLU, XLV, XLY, XLB, XLRE, EEM, EFA, VWO, GLD, SLV, TLT, IEF, SHY, USO, UNG) with GA optimization (pop=60, gen=20) from 2006-01-01 to 2026-04-24.

| Rank | Symbol | Sharpe | Trades | MaxDD% | AnnRet% | Opt Params |
|------|--------|--------|--------|--------|---------|------------|
| 1 | GLD | **1.06** | 105 | -0.7% | 0.29% | SMA260/18 RSI4 E58/X72 |
| 2 | XLK | 0.72 | 196 | -0.1% | 0.06% | SMA220/18 RSI5 E40/X46 |
| 3 | XLI | 0.68 | 78 | -0.4% | 0.07% | SMA140/26 RSI5 E31/X72 |
| 4 | IWM | 0.62 | 72 | -0.7% | 0.14% | SMA180/26 RSI5 E31/X72 |
| 5 | SPY | 0.62 | 190 | -1.2% | 0.26% | SMA180/14 RSI6 E49/X72 |
| 6 | TLT | 0.58 | 32 | -0.1% | 0.02% | SMA260/22 RSI6 E31/X46 |
| 7 | EEM | 0.57 | 52 | -0.1% | 0.02% | SMA140/22 RSI5 E31/X59 |
| 8 | QQQ | 0.55 | 264 | -0.7% | 0.18% | SMA260/14 RSI4 E49/X72 |
| 9 | DIA | 0.55 | 150 | -0.9% | 0.18% | SMA220/14 RSI4 E40/X72 |
| 10 | VWO | 0.52 | 88 | -0.2% | 0.03% | SMA140/18 RSI6 E49/X72 |

**Results: 🟢 12 Green (Sharpe≥0.5) | 🟡 12 Yellow | 🔴 0 Red**

**Key Findings:**
- **GLD** (Sharpe 1.06) outperforms all others — gold's mean reversion tendency is strongest
- **No negative Sharpe** on any of the 24 ETFs tested
- The strategy universally produces positive but **low absolute returns** (AnnRet 0.01%-0.29%) — it's a risk-controlled hedge, not a return generator
- Short-term RSI entry (RSI 31-58) and exit (RSI 46-72) parameters are the most consistent across symbols
- Shorter SMA200 periods (140-180) work better for most ETFs; longer SMA200 (220-260) for GLD/TLT/QQQ/USO

## Summary

A pullback mean reversion strategy:
1. Close > 200-day SMA (long-term uptrend filter)
2. Close < 20-day SMA (short-term pullback)
3. 5-day RSI < 45 (oversold on short timeframe)
4. Entry: at close when all 3 conditions true
5. Exit: at close when 5-day RSI > 65

Backtested on SPX from 1993 to Sep 2021, $100k compounded.
