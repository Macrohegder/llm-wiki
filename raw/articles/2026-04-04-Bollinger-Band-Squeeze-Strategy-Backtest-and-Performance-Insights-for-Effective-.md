# Bollinger Band Squeeze Strategy — Backtest and Performance Insights for Effective Trading

**原文链接**: https://quantifiedstrategies.substack.com/p/bollinger-band-squeeze-strategy-backtest

**发布时间**: Mar 19, 2024

**抓取时间**: 2026-04-04 21:48:34

---

## 摘要

Bollinger Band Squeeze Strategy — Backtest and Performance Insights for Effective Trading
QuantifiedStrategies.com
Mar 19, 2024
1
Share
The Bollinger Band Squeeze strategy is about going in the same direction as the breakout after a period of low volatility. The assumption is that the breakout sets the tone of the action over the following days (or weeks — depending on the time frame).
We use the following rules to make a strategy:
We use weekly bars (it seems to work better than daily)
We use 10-week data
We create a volatility band (10 weeks) that is the difference between the upper and lower Bollinger Bands
We create a 10-bar RSI value for the volatility bands
The buy and sell signals read like this:
The RSI of the volatility bands must be lower than 45
The close (of the asset) must set...

---

## 全文

Bollinger Band Squeeze Strategy — Backtest and Performance Insights for Effective Trading
QuantifiedStrategies.com
Mar 19, 2024
1
Share
The Bollinger Band Squeeze strategy is about going in the same direction as the breakout after a period of low volatility. The assumption is that the breakout sets the tone of the action over the following days (or weeks — depending on the time frame).
We use the following rules to make a strategy:
We use weekly bars (it seems to work better than daily)
We use 10-week data
We create a volatility band (10 weeks) that is the difference between the upper and lower Bollinger Bands
We create a 10-bar RSI value for the volatility bands
The buy and sell signals read like this:
The RSI of the volatility bands must be lower than 45
The close (of the asset) must set a new 5-day high
We sell after 20 weeks
The strategy doesn’t do particularly well for any asset, perhaps except for consumer staples. For example, Below is how it performs on Pepsi (PEP).
1
Share
Previous
Next

---

*由 Substack Strategy Tracker 自动抓取*
