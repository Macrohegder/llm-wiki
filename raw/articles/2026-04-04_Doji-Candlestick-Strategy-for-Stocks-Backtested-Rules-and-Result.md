# Doji Candlestick Strategy for Stocks: Backtested Rules and Result

**原文链接**: https://quantifiedstrategies.substack.com/p/doji-candlestick-strategy-for-stocks

**发布时间**: Mar 10, 2026

**抓取时间**: 2026-04-04 22:08:23

---

## 摘要

Doji Candlestick Strategy for Stocks: Backtested Rules and Result
QuantifiedStrategies.com
Mar 10, 2026
2
Share
In today’s article, we present a doji candlestick strategy for stocks. As we always do, we quantify and backtest it.
The doji is one of the most famous candlestick patterns in trading. It appears when the open and close are nearly the same, producing a very small body.
Many traders interpret the doji as a sign of indecision between buyers and sellers and often expect a reversal after it forms. But does the pattern actually work?
Instead of relying on chart examples, we tested a few simple rules.
First, a quick definition.
What is a doji candlestick pattern?
A doji occurs when price opens and closes at almost the same level. The candle usually has longer upper and lower shadows, s...

---

## 全文

Doji Candlestick Strategy for Stocks: Backtested Rules and Result
QuantifiedStrategies.com
Mar 10, 2026
2
Share
In today’s article, we present a doji candlestick strategy for stocks. As we always do, we quantify and backtest it.
The doji is one of the most famous candlestick patterns in trading. It appears when the open and close are nearly the same, producing a very small body.
Many traders interpret the doji as a sign of indecision between buyers and sellers and often expect a reversal after it forms. But does the pattern actually work?
Instead of relying on chart examples, we tested a few simple rules.
First, a quick definition.
What is a doji candlestick pattern?
A doji occurs when price opens and closes at almost the same level. The candle usually has longer upper and lower shadows, showing that the market moved around during the session but ultimately ended where it started. This reflects uncertainty in the market and often appears near the end of short-term trends.
This is a doji candlestick pattern
To see if the pattern has an edge, we ran a backtest on SPY, the ETF tracking the S&P 500.
Doji Candlestick Strategy for Stocks (simple doji setup)
Trading rules:
Identify a doji candlestick
At least one of the last two days must be a down day
The IBS indicator must be below 0.5
We sell when the close ends higher than yesterday’s high
Results:
Doji Candlestick Strategy for Stocks
• 339 trades
• 248 winners
• Average gain: about 0.4% per trade (commissions and slippage of 0.03% per trade)
The results are decent but not spectacular. Like many simple patterns, the edge appears modest.
Strategy 2 (oversold filter)
Next, we added a filter: only take the trade when the close is below the 10-day moving average.
This reduces the number of trades but improves the results:
Doji Candlestick Strategy for Stocks backtested
153 trades
119 winners
Average gain: about 0.7% per trade
This improvement suggests the doji may work best in oversold conditions, where markets tend to mean revert.
Key takeaway
The doji pattern by itself is not magic. But when combined with context, like short-term weakness, it can become part of a systematic strategy.
In other words, the edge may come less from the candlestick itself and more from the underlying mean-reversion behavior of the stock market.
2
Share
Previous
Next

---

*由 Substack Strategy Tracker 自动抓取*
