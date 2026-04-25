---
title: "Overnight Edge in SPY: A Simple Close-to-Close Strategy"
source_url: "https://quantifiedstrategies.substack.com/p/overnight-edge-in-spy-a-simple-close"
pub_date: "Fri, 10 Apr 2026 08:36:57 GMT"
has_strategy_logic: true
strategy_score: 4
source_file: "Sources/Substack/Intraday/quantifiedstrategies-2026-04-11-Overnight-Edge-in-SPY-A-Simple-Close-to-Close-Strategy.md"
tags: [intraday, day-trading, substack]
---

# Overnight Edge in SPY: A Simple Close-to-Close Strategy

**来源**: [https://quantifiedstrategies.substack.com/p/overnight-edge-in-spy-a-simple-close](https://quantifiedstrategies.substack.com/p/overnight-edge-in-spy-a-simple-close)
**发布日期**: Fri, 10 Apr 2026 08:36:57 GMT
**是否含具体策略逻辑**: 是 (需补充核心笔记)
**原文**: [[quantifiedstrategies-2026-04-11-Overnight-Edge-in-SPY-A-Simple-Close-to-Close-Strategy.md]]

## 摘要

Overnight Edge in SPY: A Simple Close-to-Close Strategy QuantifiedStrategies.com Apr 10, 2026 1 1 Share Today, we present an overnight edge in SPY , which is a simple close-to-close strategy. Most traders focus on what happens during the trading day. But what if the real edge lies outside regular hours? In this article, Håkan and I (Oddmund) look at one of the simplest strategies you can test: holding SPY from the close to the next close. What Is An Overnight Trading Strategy? An overnight trading strategy holds from the close until the next open or close. Technically, it includes both the overnight gap and the next trading session if you hold until the next close. This article focuses from close to close. The rules are as simple as they come: Buy SPY at the close Sell SPY at the next clos...

## 核心策略笔记

**⚠️ 注意: 这不是纯日内策略，属于隔夜/close-to-close策略，但列入参考。**

### 交易规则 (基础版)
1. 收盘买入 SPY
2. 次日收盘卖出 SPY

*(注: 文章提到实际交易规则基于VIX指标、趋势指标和价格行为，但具体过滤条件在原文中被截断/付费)*

### 回测结果
| 指标 | 数值 |
|------|------|
| 平均收益/笔 | **0.25%** |
| CAGR | **5.8%** |
| 资金占用 | **10%** |
| 最大回撤 | **16%** |
| 交易成本 | 0.06%/笔 |

### 背景
- 研究表明股票指数长期收益的很大一部分来自**隔夜收益**而非日内价格变动
- 该策略2022年首次发表，此后表现良好
- 本质是捕获收盘到次日收盘的间隙+次日交易时段收益
