# Dual Momentum Trading Strategy (Gary Antonacci) — Rules, Setup, Backtest Analysis

**Source**: [[2026-04-04-Dual-Momentum-Trading-Strategy-(Gary-Antonacci)-—-Rules,-Setup,-Backtest-Analysis]] | [Unknown](https://quantifiedstrategies.substack.com/p/dual-momentum-trading-strategy-gary-73d)
**Date**: 2026-04-04
**Tags**: #article #substack #strategy #backtest #trend-following

## One-Sentence Summary

> Dual Momentum Trading Strategy (Gary Antonacci) — Rules, Setup, Backtest Analysis
QuantifiedStrategies.com
Sep 10, 2024
1
Share
The dual momentum trading strategy by Gary Antonacci is a method of inve...

## Key Insights

1. **原文来源**: [Unknown](https://quantifiedstrategies.substack.com/p/dual-momentum-trading-strategy-gary-73d)

## Full Content

Dual Momentum Trading Strategy (Gary Antonacci) — Rules, Setup, Backtest Analysis
QuantifiedStrategies.com
Sep 10, 2024
1
Share
The dual momentum trading strategy by Gary Antonacci is a method of investing that selects only assets that have outperformed their peers over a given time and also making positive returns. It is based on the idea that an asset with a superior relative momentum and a positive absolute momentum would continue to perform until another outperforms it. Thus, it is a sort of trend strategy.
We make a backtest of Antonacci’s dual momentum strategy. The trading rules are like this:
Did S&P 500 outperform US Treasury Bills over the last 12 months?
If the answer is no, then buy US Treasury Bills.
If the answer is yes, did S&P 500 outperform the world index (ex. USA) over the last 12 months?
If S&P 500 outperformed the world index, then buy S&P 500.
If S&P 500 underperformed the world index, then buy the world index (global stocks).
We used the following ETFs: SPY for S&P 500, EFA for global stocks (world index ex. USA), and AGG for Treasury Bills (not an optimal proxy, but serves our purpose). Dividends are included and reinvested.
The equity curve of the strategy looks like the image shown below.
You can find more info about this trading strategy here:
https://www.quantifiedstrategies.com/dual-momentum-trading-strategy/
1
Share
Previous
Next

---

*由 Substack Strategy Tracker 自动抓取*

---

*Imported from Substack on 2026-04-25*
