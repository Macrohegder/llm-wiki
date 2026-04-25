---
title: "Intraday Trading Strategies: Backtest Results and Practical Examples"
source_url: "https://quantifiedstrategies.substack.com/p/intraday-trading-strategies-backtest"
pub_date: "Jun 11, 2024"
has_strategy_logic: true
strategy_score: 3
source_file: "Sources/Substack/Intraday/2026-04-04-Intraday-Trading-Strategies-Backtest-Results-and-Practical-Examples.md"
tags: [intraday, day-trading, substack]
---

# Intraday Trading Strategies: Backtest Results and Practical Examples

**来源**: [https://quantifiedstrategies.substack.com/p/intraday-trading-strategies-backtest](https://quantifiedstrategies.substack.com/p/intraday-trading-strategies-backtest)
**发布日期**: Jun 11, 2024
**是否含具体策略逻辑**: 是 (需补充核心笔记)
**原文**: [[2026-04-04-Intraday-Trading-Strategies-Backtest-Results-and-Practical-Examples.md]]

## 摘要

Intraday Trading Strategies: Backtest Results and Practical Examples
QuantifiedStrategies.com
Jun 11, 2024
1
Share
Intraday trading strategies refers to a style of trading where a trader buys and sells a financial instrument within the same trading day. The financial instrument can be stocks, futures, or forex. Intraday trading can be scalping — a trading method that tries to profit from small price fluctuations that happen all through the trading day. It can also be day trading — a trading method that aims to capture the major price movements of each trading day but ensures to close all positions before the market closes for the trading day.
In this post, we take a look at intraday trading and the strategies used for it and we end the article by backtesting intraday trading strategies.
We...

## 核心策略笔记

**标的**: WTI原油期货 (NYMEX)
**数据周期**: 2000-2021
**时间框架**: 小时线

### 交易规则
1. 使用小时线
2. 当K线出现**连续第三个更低低点和更低高点**时，在 **10:30 NY时间** 入场做多
3. 在 **16:00 NY时间** 收盘平仓

### 要点
- 纯趋势跟踪/动量型日内策略
- 仅在特定时间点执行，避免过度交易
- 基于连续K线结构确认短期超卖后的反弹
