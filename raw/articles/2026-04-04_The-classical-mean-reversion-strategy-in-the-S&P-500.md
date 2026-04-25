# The classical mean reversion strategy in the S&P 500

**原文链接**: https://quantifiedstrategies.substack.com/p/the-classical-mean-reversion-strategy

**发布时间**: Jul 30, 2024

**抓取时间**: 2026-04-04 21:56:14

---

## 摘要

The classical mean reversion strategy in the S&P 500
QuantifiedStrategies.com
Jul 30, 2024
1
Share
The classical mean reversion strategy in the S&P 500 involves specific criteria based on Internal Bar Strength (IBS) and Relative Strength Index (RSI) to determine trading signals.In this post we backtested a strategy on SPY or the S&P 500.
We backtest the following trading rules:
* IBS (internal bar strength) must be lower than 0.25 (using daily bars).
* RSI (21) must be below 45.
* If 1 and 2 are fulfilled, go long at the close.
* Exit when close is higher than yesterday’s close.
The equity curve (Shown in the image below) since January 2000 looks like this (starting with 100,000 in equity and allocating 100% of equity to every trade, ie. compounding, but taxes are not deducted)
1
Share
Pre...

---

## 全文

The classical mean reversion strategy in the S&P 500
QuantifiedStrategies.com
Jul 30, 2024
1
Share
The classical mean reversion strategy in the S&P 500 involves specific criteria based on Internal Bar Strength (IBS) and Relative Strength Index (RSI) to determine trading signals.In this post we backtested a strategy on SPY or the S&P 500.
We backtest the following trading rules:
* IBS (internal bar strength) must be lower than 0.25 (using daily bars).
* RSI (21) must be below 45.
* If 1 and 2 are fulfilled, go long at the close.
* Exit when close is higher than yesterday’s close.
The equity curve (Shown in the image below) since January 2000 looks like this (starting with 100,000 in equity and allocating 100% of equity to every trade, ie. compounding, but taxes are not deducted)
1
Share
Previous
Next

---

*由 Substack Strategy Tracker 自动抓取*
