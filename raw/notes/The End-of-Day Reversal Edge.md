---
title: "The End-of-Day Reversal Edge"
source_url: "https://quantifiedstrategies.substack.com/p/the-end-of-day-reversal-edge"
pub_date: "Feb 12, 2026"
has_strategy_logic: true
strategy_score: 5
source_file: "Sources/Substack/Intraday/2026-04-04-The-End-of-Day-Reversal-Edge.md"
tags: [intraday, day-trading, substack]
---

# The End-of-Day Reversal Edge

**来源**: [https://quantifiedstrategies.substack.com/p/the-end-of-day-reversal-edge](https://quantifiedstrategies.substack.com/p/the-end-of-day-reversal-edge)
**发布日期**: Feb 12, 2026
**是否含具体策略逻辑**: 是 (需补充核心笔记)
**原文**: [[2026-04-04-The-End-of-Day-Reversal-Edge.md]]

## 摘要

The End-of-Day Reversal Edge
QuantifiedStrategies.com
Feb 12, 2026
8
3
Share
Today, we present an interesting end-of-day reversal effect. This post is based on research by Baltussen, G., Da, Z., & Soebhag, A. (2024). The article is called
End‑of‑Day Reversal
.
What Is the End-of-Day Reversal?
The idea is simple. Stocks that have performed poorly during the day tend to rebound in the final 30 minutes of trading.
Conversely, stocks that have been strong earlier in the session tend to flatten out or underperform into the close. This pattern appears repeatedly in U.S. equity data and has been documented since the early 1990s.
The setup works like this. During the trading day, you measure each stock’s return from the previous close until 3:30 p.m. Eastern Time. You then rank stocks based on tha...

## 核心策略笔记

**研究来源**: Baltussen, G., Da, Z., & Soebhag, A. (2024), *End-of-Day Reversal*
**标的**: NYSE / NASDAQ / AMEX 普通股 (CRSP share codes 10 & 11)
**筛选条件**: 股价 > $5，市值高于NYSE第10规模百分位
**周期**: 1993-2019

### 交易规则
1. 测量每只股票从前收盘至 **15:30 ET** 的日内收益
2. 按收益排序分组:
   - **最差 performers (最大输家)** → 15:30-16:00 做多
   - **最强 performers (最大赢家)** → 15:30-16:00 做空
3. 构建多空对冲组合 (dollar-neutral decile-spread)

### 回测结果
- 多空价差组合复合收益超过大盘 (Ken French CRSP市场因子) **10倍以上**
- 尽管每天仅投资 **0.5小时**

### 逻辑解释
- **散户反向行为**: 大跌股票在尾盘显得"便宜"，吸引散户抄底
- **空头回补**: 日内做空者在收盘前降低风险，买入平仓推高价格

### ⚠️ 风险与限制
- **交易成本极高**: 最后30分钟价差扩大、滑点严重、高频竞争
- **流动性限制**: 历史收益在小盘/低流动性股票中更强，大资金难以实施
- **效果衰减**: 近年来该异象已有所减弱，但未完全消失
