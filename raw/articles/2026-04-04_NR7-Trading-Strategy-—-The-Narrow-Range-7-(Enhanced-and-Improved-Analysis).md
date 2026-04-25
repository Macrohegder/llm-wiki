# NR7 Trading Strategy — The Narrow Range 7 (Enhanced and Improved Analysis)

**原文链接**: https://quantifiedstrategies.substack.com/p/nr7-trading-strategy-the-narrow-range-b35

**发布时间**: May 12, 2024

**抓取时间**: 2026-04-04 21:52:02

---

## 摘要

NR7 Trading Strategy — The Narrow Range 7 (Enhanced and Improved Analysis)
QuantifiedStrategies.com
May 12, 2024
1
Share
In this post, we backtest the Narrow Range NR7 trading strategy. The strategy works reasonably well, but we improved it by adding one simple parameter.
We made our own version of the NR7 trading strategy and made the following trading rules listed below. We test the following hypothesis on stocks:
The range, or volatility, is the difference between the High and the Low (each day).
If today has the lowest range of the previous last 6 trading days, then we go long at the close.
We exit at the close when today’s close is higher than yesterday’s high.
We have one parameter for entry and one exit criterium, and a trading strategy can hardly get any simpler than that (?). We t...

---

## 全文

NR7 Trading Strategy — The Narrow Range 7 (Enhanced and Improved Analysis)
QuantifiedStrategies.com
May 12, 2024
1
Share
In this post, we backtest the Narrow Range NR7 trading strategy. The strategy works reasonably well, but we improved it by adding one simple parameter.
We made our own version of the NR7 trading strategy and made the following trading rules listed below. We test the following hypothesis on stocks:
The range, or volatility, is the difference between the High and the Low (each day).
If today has the lowest range of the previous last 6 trading days, then we go long at the close.
We exit at the close when today’s close is higher than yesterday’s high.
We have one parameter for entry and one exit criterium, and a trading strategy can hardly get any simpler than that (?). We test on the S&P 500 by using the ETF with the ticker code SPY.
If we invest 100 000 and let it compound since the inception of the ETF in 1993 we get the following equity curve and drawdowns ((Shown in the image below)
1
Share
Previous
Next

---

*由 Substack Strategy Tracker 自动抓取*
