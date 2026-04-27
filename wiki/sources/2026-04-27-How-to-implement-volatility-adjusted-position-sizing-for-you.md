---
title: "How to implement volatility-adjusted position sizing for your strategies."
author: "SetupAlpha"
source: "Substack"
url: "https://setup4alpha.substack.com/p/how-to-implement-volatility-adjusted"
date: "2026-04-27"
topics: ["systematic-trading", "algorithmic-trading"]
---

# How to implement volatility-adjusted position sizing for your strategies.

**来源**: [SetupAlpha](https://setup4alpha.substack.com/p/how-to-implement-volatility-adjusted)  
**日期**: 2026-04-27  
**作者**: SetupAlpha

---

## 摘要

How to implement volatility-adjusted position sizing for your strategies.
Volatility-adjusted position sizing and RealTest codes.
SetupAlpha
Mar 07, 2025
18
4
7
Share
Marcos Lopez de Prado suggests using
volatility-adjusted position sizing
instead of fixed lot sizes. This approach tailors your position size based on market volatility, ensuring you're not overexposed in more volatile conditions. It’s a smarter way to manage risk and enhance performance.
How to implement volatility-adjusted position sizing for your strategies…
1. Decide Your Risk Per Trade:
Choose a fixed percentage of your account equity that you're willing to lose on a single trade (e.g., 1–2%).
2. Select a Volatility Measure:
Use a reliable indicator like the Average True Range (ATR) or the standard deviation of recent pr...

---

## 原文

How to implement volatility-adjusted position sizing for your strategies.
Volatility-adjusted position sizing and RealTest codes.
SetupAlpha
Mar 07, 2025
18
4
7
Share
Marcos Lopez de Prado suggests using
volatility-adjusted position sizing
instead of fixed lot sizes. This approach tailors your position size based on market volatility, ensuring you're not overexposed in more volatile conditions. It’s a smarter way to manage risk and enhance performance.
How to implement volatility-adjusted position sizing for your strategies…
1. Decide Your Risk Per Trade:
Choose a fixed percentage of your account equity that you're willing to lose on a single trade (e.g., 1–2%).
2. Select a Volatility Measure:
Use a reliable indicator like the Average True Range (ATR) or the standard deviation of recent price movements. ATR is popular because it captures both trends and sudden spikes.
3. Determine Your Stop Loss:
Set your stop loss based on volatility. For instance, you might set it at 2×ATR. This gives the price some breathing room while defining a clear exit point.
4. Calculate the Position Size:
Use the formula:
Position Size = (Account Risk) / (Stop Loss Distance)
Example: If you risk 1% of a $10K account ($100) and your stop loss is 2 ATR with an ATR of $1, then: Position Size = $100 / (2 × $1) = 50 shares.
In realtest we can use code like this:
Data:
   Risk:        0.01

Strategy:
   Quantity: 	(S.Equity * Risk) / (2 * atr(14))
   QtyType: 	Shares
You can visually see the stop loss distance on the chart by using code like this:
Charts:
   AtrStopLoss:	  close - (2 * atr(14))
Top industry traders are already subscribing, you should too!
Subscribe
5. Integrate into Your Strategy:
Adjust your order size automatically based on the current ATR value. This means every time volatility changes, your position size recalculates, keeping your risk constant.
6. Backtest and Optimize:
Test this method across different market regimes to ensure that your stop loss multiples and risk percentages are optimal.
Compare results with fixed lot sizing to see the impact on drawdowns and overall performance.
Our backtest
Below is our backtest. We tested volatility-adjusted position sizing and fixed position sizing in our mean reversion strategy. There's not a huge difference, but the volatility-based position sizing equity curve is slightly smoother than the fixed one.
By implementing these steps, you effectively size your trades to accommodate market volatility. This way, during high volatility, you'll take smaller positions (reducing risk), and during low volatility, you can afford larger positions, thus keeping your risk exposure consistent.
https://setupalpha.com/
You can watch his full talk here:
Subscribe
18
4
7
Share

---

*由 Substack Strategy Tracker 自动抓取*

---

*Imported from Substack on 2026-04-27*
