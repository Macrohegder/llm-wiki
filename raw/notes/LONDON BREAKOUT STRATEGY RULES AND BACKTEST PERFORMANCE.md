---
title: "LONDON BREAKOUT STRATEGY: RULES AND BACKTEST PERFORMANCE"
source_url: "https://quantifiedstrategies.substack.com/p/london-breakout-strategy-rules-and"
pub_date: "Nov 23, 2025"
has_strategy_logic: true
strategy_score: 5
source_file: "Sources/Substack/Intraday/2026-04-04-LONDON-BREAKOUT-STRATEGY-RULES-AND-BACKTEST-PERFORMANCE.md"
tags: [intraday, day-trading, substack]
---

# LONDON BREAKOUT STRATEGY: RULES AND BACKTEST PERFORMANCE

**来源**: [https://quantifiedstrategies.substack.com/p/london-breakout-strategy-rules-and](https://quantifiedstrategies.substack.com/p/london-breakout-strategy-rules-and)
**发布日期**: Nov 23, 2025
**是否含具体策略逻辑**: 是 (需补充核心笔记)
**原文**: [[2026-04-04-LONDON-BREAKOUT-STRATEGY-RULES-AND-BACKTEST-PERFORMANCE.md]]

## 摘要

LONDON BREAKOUT STRATEGY: RULES AND BACKTEST PERFORMANCE
QuantifiedStrategies.com
Nov 23, 2025
1
1
Share
Also known as the London daybreak strategy, the London breakout strategy is a day trading strategy that seeks to trade the upward or downward breakout of the day’s trading range that’s formed before the opening of the London session. This breakout usually happens within the first three hours into the London session. if the breakout is to the upside, traders take long positions, and if it is to the downside, traders take short positions.
We backtest the following trading rules:
➨ We use the high and low from 0300 to 0800 London time to determine the high and low (resistance and support).
➨ When the price breaks above the high, we go long (between 0800 and 1100 London time).
➨ When the pr...

## 核心策略笔记

**别称**: London Daybreak Strategy
**更多详情**: https://www.quantifiedstrategies.com/london-breakout-strategy/

### 交易规则
1. 取 **伦敦时间 03:00-08:00** 的高低点作为阻力/支撑区间
2. 在 **08:00-11:00** 伦敦时间:
   - 价格突破上轨 → 做多
   - 价格突破下轨 → 做空
3. **时间出场** (无止损或止盈目标): 分别测试在 12:00/13:00/14:00/15:00/16:00/17:00 伦敦时间平仓

### 特点
- 纯突破型日内策略
- 完全依赖时间出场，无固定止损止盈
- 利用伦敦开盘前的盘整区间突破
