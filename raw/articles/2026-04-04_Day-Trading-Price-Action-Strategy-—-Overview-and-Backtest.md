# Day Trading Price Action Strategy — Overview and Backtest

**原文链接**: https://quantifiedstrategies.substack.com/p/day-trading-price-action-strategy-181

**发布时间**: Jul 04, 2024

**抓取时间**: 2026-04-04 21:55:09

---

## 摘要

Day Trading Price Action Strategy — Overview and Backtest
QuantifiedStrategies.com
Jul 04, 2024
1
Share
A day trading price action strategy refers to the pattern of price movement of an asset. Thus, a day trading price action trading strategy is using patterns of price movements to determine when to enter and exit a trade.
In this post, we take a look at price action and we give some advice on backtesting price action trading strategies.
We believe the trading rules are pretty straightforward: we want to enter a position after a series of lower lows and lower highs in a row.
We backtest the following trading rules:
- We use hourly bars.
- We enter at the close when the bar is the third lower low and third lower high in a row.
- We enter a position only at 1030 local NY time.
- We sell at t...

---

## 全文

Day Trading Price Action Strategy — Overview and Backtest
QuantifiedStrategies.com
Jul 04, 2024
1
Share
A day trading price action strategy refers to the pattern of price movement of an asset. Thus, a day trading price action trading strategy is using patterns of price movements to determine when to enter and exit a trade.
In this post, we take a look at price action and we give some advice on backtesting price action trading strategies.
We believe the trading rules are pretty straightforward: we want to enter a position after a series of lower lows and lower highs in a row.
We backtest the following trading rules:
- We use hourly bars.
- We enter at the close when the bar is the third lower low and third lower high in a row.
- We enter a position only at 1030 local NY time.
- We sell at the close of 1600 NY time.
We backtest the WTI crude oil futures contract that is traded on NYMEX. The equity curve (2000-2021) is shown below.
1
Share
Previous
Next

---

*由 Substack Strategy Tracker 自动抓取*
