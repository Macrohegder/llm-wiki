# Bollinger Band Squeeze Strategy — Backtest and Performance Analysis

**Source**: [[2026-04-04-Bollinger-Band-Squeeze-Strategy-—-Backtest-and-Performance-Analysis]] | [Unknown](https://quantifiedstrategies.substack.com/p/bollinger-band-squeeze-strategy-backtest-4a6)
**Date**: 2026-04-04
**Tags**: #article #substack #strategy #backtest

## One-Sentence Summary

> Bollinger Band Squeeze Strategy — Backtest and Performance Analysis
QuantifiedStrategies.com
May 29, 2024
1
Share
The Bollinger Band Squeeze strategy is about going in the same direction as the breako...

## Key Insights

1. **原文来源**: [Unknown](https://quantifiedstrategies.substack.com/p/bollinger-band-squeeze-strategy-backtest-4a6)

## Full Content

Bollinger Band Squeeze Strategy — Backtest and Performance Analysis
QuantifiedStrategies.com
May 29, 2024
1
Share
The Bollinger Band Squeeze strategy is about going in the same direction as the breakout after a period of low volatility. The assumption is that the breakout sets the tone of the action over the following days (or weeks — depending on the time frame).
Let’s dig in and see if we can make a profitable backtested Bollinger Band Squeeze strategy.
We backtest the following trading rules:
We use weekly bars (it seems to work better than daily)
We use 10-week data
We create a volatility band (10 weeks) that is the difference between the upper and lower Bollinger Bands
We create a 10-bar RSI value for the volatility bands
The buy and sell signals read like this:
The RSI of the volatility bands must be lower than 45
The close (of the asset) must set a new 5-day high
We sell after 20 weeks
The strategy doesn’t do particularly well for any asset, perhaps except for consumer staples. For example, this is how it performs (Shown in the image on Pepsi (PEP):
1
Share
Previous
Next

---

*由 Substack Strategy Tracker 自动抓取*

---

*Imported from Substack on 2026-04-25*
