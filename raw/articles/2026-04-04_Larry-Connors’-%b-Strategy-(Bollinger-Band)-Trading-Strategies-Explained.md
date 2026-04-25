# Larry Connors’ %b Strategy (Bollinger Band) | Trading Strategies Explained

**原文链接**: https://quantifiedstrategies.substack.com/p/larry-connors-b-strategy-bollinger-ab6

**发布时间**: Sep 20, 2024

**抓取时间**: 2026-04-04 21:59:24

---

## 摘要

Larry Connors’ %b Strategy (Bollinger Band) | Trading Strategies Explained
QuantifiedStrategies.com
Sep 20, 2024
1
1
Share
In chapter 5 of Larry Connors‘ book High Probability Trading, published in 2009, there is a trading strategy called %b strategy. 2 years have passed since the book was published and it could be interesting to see if the strategies are still performing well. Larry Connors tested 20 ETFs from their inception up until the end of 2008, while we test from inception until today.
We backtest the following trading rules:
- The close must be above the 200-day moving average.
- The %b must be below 0.2 for the last three (consecutive) days.
- If 1 and 2 are true, buy on the close.
- Exit when the %b closes above 0.8.
We were not able to replicate the results of Connors because w...

---

## 全文

Larry Connors’ %b Strategy (Bollinger Band) | Trading Strategies Explained
QuantifiedStrategies.com
Sep 20, 2024
1
1
Share
In chapter 5 of Larry Connors‘ book High Probability Trading, published in 2009, there is a trading strategy called %b strategy. 2 years have passed since the book was published and it could be interesting to see if the strategies are still performing well. Larry Connors tested 20 ETFs from their inception up until the end of 2008, while we test from inception until today.
We backtest the following trading rules:
- The close must be above the 200-day moving average.
- The %b must be below 0.2 for the last three (consecutive) days.
- If 1 and 2 are true, buy on the close.
- Exit when the %b closes above 0.8.
We were not able to replicate the results of Connors because we lack his parameters. However, the results are very good in QQQ and SPY, but very few fills. This is the equity curve for QQQ (shown below)
1
1
Share
Previous
Next

---

*由 Substack Strategy Tracker 自动抓取*
