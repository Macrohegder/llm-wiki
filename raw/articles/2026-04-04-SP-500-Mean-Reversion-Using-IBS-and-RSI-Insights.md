# S&P 500 Mean Reversion Using IBS and RSI — Insights

**原文链接**: https://quantifiedstrategies.substack.com/p/s-and-p-500-mean-reversion-using-112

**发布时间**: May 14, 2024

**抓取时间**: 2026-04-04 21:52:09

---

## 摘要

S&P 500 Mean Reversion Using IBS and RSI — Insights
QuantifiedStrategies.com
May 14, 2024
1
Share
The classical mean reversion strategy in the S&P 500 involves specific criteria based on Internal Bar Strength (IBS) and Relative Strength Index (RSI) to determine trading signals. The strategy’s performance can be analyzed using various statistical measures, including win rates, drawdowns (periods of losses), and annual returns. These metrics provide insights into the historical performance of the strategy.
This post includes an equity curve that demonstrates the performance of the strategy when the parameters are reversed or inverted. This information can help traders understand the importance of the chosen criteria.
We backtest the following trading rules:
IBS (internal bar strength) must b...

---

## 全文

S&P 500 Mean Reversion Using IBS and RSI — Insights
QuantifiedStrategies.com
May 14, 2024
1
Share
The classical mean reversion strategy in the S&P 500 involves specific criteria based on Internal Bar Strength (IBS) and Relative Strength Index (RSI) to determine trading signals. The strategy’s performance can be analyzed using various statistical measures, including win rates, drawdowns (periods of losses), and annual returns. These metrics provide insights into the historical performance of the strategy.
This post includes an equity curve that demonstrates the performance of the strategy when the parameters are reversed or inverted. This information can help traders understand the importance of the chosen criteria.
We backtest the following trading rules:
IBS (internal bar strength) must be lower than 0.25 (using daily bars).
RSI (21) must be below 45.
If 1 and 2 are fulfilled, go long at the close.
Exit when close is higher than yesterday’s close.
The equity curve (shown in the image below) since January 2000 looks like this (starting with 100 000 in equity and allocating 100% of equity to every trade, ie. compounding, but taxes are not deducted)
1
Share
Previous
Next

---

*由 Substack Strategy Tracker 自动抓取*
