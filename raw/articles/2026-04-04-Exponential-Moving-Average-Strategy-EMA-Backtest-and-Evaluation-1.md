# Exponential Moving Average Strategy (EMA): Backtest and Evaluation

**原文链接**: https://quantifiedstrategies.substack.com/p/exponential-moving-average-strategy-4f0

**发布时间**: Jun 29, 2025

**抓取时间**: 2026-04-04 22:03:56

---

## 摘要

Exponential Moving Average Strategy (EMA): Backtest and Evaluation
QuantifiedStrategies.com
Jun 29, 2025
1
Share
Backtests indicate that exponential moving averages strategy do work: They can be useful for mean-reversion strategies if you use a short number of days in the moving average, and useful for long-term trend following if you use a high number of days in the moving average.
We backtest the following trading rules:
This Substack is reader-supported. To receive new posts and support my work, consider becoming a free or paid subscriber.
Subscribe
Strategy 1:
When the close of SPY crosses BELOW the N-day moving average, we buy SPY at the close. We sell when SPY's closes ABOVE the same average. We use CAGR as the performance metric.
Strategy 2:
Opposite, when the close of SPY crosses A...

---

## 全文

Exponential Moving Average Strategy (EMA): Backtest and Evaluation
QuantifiedStrategies.com
Jun 29, 2025
1
Share
Backtests indicate that exponential moving averages strategy do work: They can be useful for mean-reversion strategies if you use a short number of days in the moving average, and useful for long-term trend following if you use a high number of days in the moving average.
We backtest the following trading rules:
This Substack is reader-supported. To receive new posts and support my work, consider becoming a free or paid subscriber.
Subscribe
Strategy 1:
When the close of SPY crosses BELOW the N-day moving average, we buy SPY at the close. We sell when SPY's closes ABOVE the same average. We use CAGR as the performance metric.
Strategy 2:
Opposite, when the close of SPY crosses ABOVE the N-day moving average, we buy SPY at the close. We sell when SPY's closes BELOW the same average. We use CAGR as the performance metric.
Strategy 3:
When the close of SPY crosses BELOW the N-day moving average, we sell after N-days. We use average gain per trade in percent to evaluate performance, not CAGR.
Strategy 4:
When the close of SPY crosses ABOVE the N-day moving average, we sell after N-days. We use average gain per trade in percent to evaluate performance, not CAGR.
The results from the two first backtests are shown in the image below.
This Substack is reader-supported. To receive new posts and support my work, consider becoming a free or paid subscriber.
Subscribe
1
Share
Previous
Next

---

*由 Substack Strategy Tracker 自动抓取*
