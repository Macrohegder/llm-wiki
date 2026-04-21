# Intraday Trading Strategies: Backtest Results and Practical Examples

**原文链接**: https://quantifiedstrategies.substack.com/p/intraday-trading-strategies-backtest

**发布时间**: Jun 11, 2024

**抓取时间**: 2026-04-04 21:53:49

---

## 摘要

Intraday Trading Strategies: Backtest Results and Practical Examples
QuantifiedStrategies.com
Jun 11, 2024
1
Share
Intraday trading strategies refers to a style of trading where a trader buys and sells a financial instrument within the same trading day. The financial instrument can be stocks, futures, or forex. Intraday trading can be scalping — a trading method that tries to profit from small price fluctuations that happen all through the trading day. It can also be day trading — a trading method that aims to capture the major price movements of each trading day but ensures to close all positions before the market closes for the trading day.
In this post, we take a look at intraday trading and the strategies used for it and we end the article by backtesting intraday trading strategies.
We...

---

## 全文

Intraday Trading Strategies: Backtest Results and Practical Examples
QuantifiedStrategies.com
Jun 11, 2024
1
Share
Intraday trading strategies refers to a style of trading where a trader buys and sells a financial instrument within the same trading day. The financial instrument can be stocks, futures, or forex. Intraday trading can be scalping — a trading method that tries to profit from small price fluctuations that happen all through the trading day. It can also be day trading — a trading method that aims to capture the major price movements of each trading day but ensures to close all positions before the market closes for the trading day.
In this post, we take a look at intraday trading and the strategies used for it and we end the article by backtesting intraday trading strategies.
We backtest the following trading rules:
We use hourly bars.
We enter long at the close when the bar is the third lower low and third lower high in a row.
We enter a position only at 1030 local NY time.
We sell at the close of 1600 NY time.
The strategy is backtested on the WTI crude oil futures contract traded on NYMEX. The equity curve (2000–2021) looks like the image shown below.
You can find more info about this trading strategy here:
https://www.quantifiedstrategies.com/intraday-trading-strategies/
1
Share
Previous
Next

---

*由 Substack Strategy Tracker 自动抓取*
