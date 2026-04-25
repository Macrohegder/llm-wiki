# Systematic Intraday Trend-Following Strategy

**Source**: [[2026-04-04-Systematic-Intraday-Trend-Following-Strategy]] | [Unknown](https://quantifiedstrategies.substack.com/p/systematic-intraday-trend-following)
**Date**: 2026-04-04
**Tags**: #article #substack #strategy #trend-following #intraday

## One-Sentence Summary

> Systematic Intraday Trend-Following Strategy
Backtested Strategy
QuantifiedStrategies.com
Feb 23, 2026
14
1
Share
Today, we dive into a systematic intraday trend-following strategy developed by Carlo ...

## Key Insights

1. **原文来源**: [Unknown](https://quantifiedstrategies.substack.com/p/systematic-intraday-trend-following)

## Full Content

Systematic Intraday Trend-Following Strategy
Backtested Strategy
QuantifiedStrategies.com
Feb 23, 2026
14
1
Share
Today, we dive into a systematic intraday trend-following strategy developed by Carlo Zarattini at Concretum.
The strategy relies on a simple, yet powerful, quantified intraday momentum principle: strength tends to generate more strength throughout the trading day.
Rather than predicting market direction, the system reacts to price movements. When momentum builds, traders and algorithms often amplify the move through herding, liquidity chasing, and risk adjustments.
The objective isn’t to pick tops or bottoms; it’s to participate in the trend.
By following a rule-based framework, this intraday trend strategy removes discretion and emphasizes consistent, repeatable behavior.
Why Systematic Intraday Trend-Following Works
Markets are adaptive, but human behavior evolves slowly. Traders chase winners, institutions add to strength, and short sellers are often forced to cover when prices accelerate. These feedback loops generate temporary trends that systematic strategies can exploit.
Intraday momentum strategies focus on capturing the middle of these moves - not the exact start or end. Missing the extremes is deliberate; the key is to trade the portion of the move where probabilities are in your favor, and randomness plays a smaller role.
Related reading:
Gold Trend-Following Strategy
Trading Rules
For a detailed breakdown of the exact trading rules, we recommend reviewing the
Python code
.
In general, the trading rules are based on the following:
Dynamic Boundaries:
The trading zone adjusts throughout the day, based on the average price movement from the open over the past 14 days.
Overnight Gap Adjustments:
Boundaries are adjusted to account for overnight price gaps, which often reflect sudden shifts in supply and demand.
Entry Signals:
A long position is taken when the price breaks above the Upper Boundary, signaling strong buying pressure. A short position is entered when the price drops below the Lower Boundary, signaling unusual selling activity.
Stop Loss:
The Volume Weighted Average Price (VWAP) serves as a protective stop.
Dynamic Position Sizing:
Position sizes are adjusted based on daily market volatility to manage risk efficiently.
Semi-Hourly Execution:
Trades are executed only at the top or bottom of each hour to filter out noise and short-term price spikes.
Systematic intraday trend-following example
A key feature of this model is that its noise thresholds are dynamic, adjusting throughout the trading day. As a result, the price movement required to signal a demand–supply imbalance is not fixed; it changes depending on the time of day, for example, between the first 30 minutes after the open and the later hours of the session.
Generally, the average intraday move from the opening price grows as the day progresses, typically peaking around 16:00. As illustrated in the simplified example in Figure 1, a decline of just − 0.30% from the open at 10:30 was sufficient to indicate abnormal selling pressure - about half the move needed to trigger the same signal at 15:30.
The authors highlighted this behavior with two trade examples in their research paper:
Systematic intraday trend-following trade examples
Backtest Results
The authors backtested the strategy on SPY, the ETF that tracks the S&P 500. A commission of $0.0035 per share was included, reflecting the entry-level rate charged by Interactive Brokers.
Systematic Intraday Trend-Following Strategy
Total Return:
The strategy achieved a remarkable total return of 1,985%.
Annualized Return:
It maintained a consistent 19.6% annualized return throughout the period.
Risk-Adjusted Performance:
With a Sharpe Ratio of 1.33, the strategy far outperformed a passive buy-and-hold approach on SPY, which generated only 0.45.
Market Neutrality:
With a beta slightly below zero, the strategy’s returns are largely independent of broader market movements, providing strong diversification benefits.
Volatility Advantage:
Performance improves in high-volatility environments, with the Sharpe Ratio climbing to 3.50 whenever the VIX exceeds 40.
The authors used a 14-day lookback period, but their results show that a wide range of lookback lengths also produced profitable outcomes.
Systematic intraday trend-following results
The paper, first published in the summer of 2024, presented results up to early 2024. Since then, the strategy has continued to deliver strong performance in out-of-sample testing, according to the authors.
Systematic intraday trend-following backtest
Summary
We have not conducted our own backtests of this strategy. It’s important to note that slippage is not accounted for, and when trading stocks, futures, or ETFs, as this strategy may require, slippage can be significant.
As a result, the real-time performance of this systematic intraday trend-following strategy may be lower than the backtested results suggest.
14
1
Share
Previous
Next

---



---

*Imported from Substack on 2026-04-25*
