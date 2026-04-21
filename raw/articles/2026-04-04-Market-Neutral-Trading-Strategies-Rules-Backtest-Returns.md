# Market-Neutral Trading Strategies (Rules, Backtest, Returns)

**原文链接**: https://quantifiedstrategies.substack.com/p/market-neutral-trading-strategies

**发布时间**: Oct 14, 2024

**抓取时间**: 2026-04-04 22:00:55

---

## 摘要

Market-Neutral Trading Strategies (Rules, Backtest, Returns)
QuantifiedStrategies.com
Oct 14, 2024
1
Share
A market-neutral strategy is a type of investment approach that enables an investor to benefit from both rising and falling stock prices. This is achieved by taking long positions in one stock and short positions in another stock. The strategy is designed to reduce exposure to specific market risks and can be applied in one or more markets.
We backtest the following trading rules.
First, make the following calculations:
* Make a pair ratio of XLU divided by TLT; and
* Calculate the 5-day RSI of the pair ratio; and
* Calculate the High - Low for TLT every day - (Volatility).
We take a long position in XLU (60% of equity) and go short TLT (40% of equity) when the following are true:
* T...

---

## 全文

Market-Neutral Trading Strategies (Rules, Backtest, Returns)
QuantifiedStrategies.com
Oct 14, 2024
1
Share
A market-neutral strategy is a type of investment approach that enables an investor to benefit from both rising and falling stock prices. This is achieved by taking long positions in one stock and short positions in another stock. The strategy is designed to reduce exposure to specific market risks and can be applied in one or more markets.
We backtest the following trading rules.
First, make the following calculations:
* Make a pair ratio of XLU divided by TLT; and
* Calculate the 5-day RSI of the pair ratio; and
* Calculate the High - Low for TLT every day - (Volatility).
We take a long position in XLU (60% of equity) and go short TLT (40% of equity) when the following are true:
* The 5-day RSI of the pair ratio must be below 20; and
* The five-day average of TLT volatility is higher than the 25-day average (#3 above).
Close out the positions when the 5-day RSI of the pair reaches 50.
The trading rules are flipped to take the opposite position. When we apply the trading rules we get the following equity curve shown below
1
Share
Previous
Next

---

*由 Substack Strategy Tracker 自动抓取*
