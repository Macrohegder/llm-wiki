# Simple Moving Average Trading Strategy: Backtest And Statistics

**原文链接**: https://quantifiedstrategies.substack.com/p/simple-moving-average-trading-strategy

**发布时间**: Sep 30, 2024

**抓取时间**: 2026-04-04 21:59:59

---

## 摘要

Simple Moving Average Trading Strategy: Backtest And Statistics
QuantifiedStrategies.com
Sep 30, 2024
1
Share
The SMA is one of the primary indicators in technical analysis and is usually the easiest moving average to construct, which is why it is referred to as the “simple” moving average. The indicator is present on all trading platforms and is widely applied across various financial markets such as shares, currencies, indices, and exchange-traded funds (ETFs), assisting both short-term traders and long-term investors in making well-informed decisions.
We backtest the following four different:
* Strategy 1: When the close of SPY crosses BELOW the N-day moving average, we buy SPY at the close. We sell when SPY's closes ABOVE the same average. We use CAGR as the performance metric.
* Strat...

---

## 全文

Simple Moving Average Trading Strategy: Backtest And Statistics
QuantifiedStrategies.com
Sep 30, 2024
1
Share
The SMA is one of the primary indicators in technical analysis and is usually the easiest moving average to construct, which is why it is referred to as the “simple” moving average. The indicator is present on all trading platforms and is widely applied across various financial markets such as shares, currencies, indices, and exchange-traded funds (ETFs), assisting both short-term traders and long-term investors in making well-informed decisions.
We backtest the following four different:
* Strategy 1: When the close of SPY crosses BELOW the N-day moving average, we buy SPY at the close. We sell when SPY's closes ABOVE the same average. We use CAGR as the performance metric.
* Strategy 2: Opposite, when the close of SPY crosses ABOVE the N-day moving average, we buy SPY at the close. We sell when SPY's closes BELOW the same average. We use CAGR as the performance metric.
* Strategy 3: When the close of SPY crosses BELOW the N-day moving average, we sell after N-days. We use average gain per trade in percent to evaluate performance, not CAGR.
* Strategy 4: When the close of SPY crosses ABOVE the N-day moving average, we sell after N-days. We use average gain per trade in percent to evaluate performance, not CAGR.
The results of the backtests can be summarized in the following four tables - one for each system (Shown in the image below)
What conclusions can we draw from these two tables? The first thing that is quite obvious is that the stock market shows tendencies toward mean-reversion in the short run. This we can see in table one where it’s clearly much more profitable to buy when the close crosses below a short-term moving average than compared when it crosses above. The 5-day moving average returns a CAGR of 8.34% (which is pretty good). The buy and hold CAGR is 9%.
1
Share
Previous
Next

---

*由 Substack Strategy Tracker 自动抓取*
