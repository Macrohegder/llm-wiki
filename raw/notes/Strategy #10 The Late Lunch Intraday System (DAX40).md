---
title: "Strategy #10: The Late Lunch Intraday System (DAX40)"
source_url: "https://algomatictrading.substack.com/p/strategy-10-the-late-lunch-intraday"
pub_date: "2026-04-05"
has_strategy_logic: true
strategy_score: 7
source_file: "Sources/Substack/Intraday/algomatictrading-2026-04-05-Strategy-10-The-Late-Lunch-Intraday-System-DAX40.md"
tags: [intraday, day-trading, substack]
---

# Strategy #10: The Late Lunch Intraday System (DAX40)

**来源**: [https://algomatictrading.substack.com/p/strategy-10-the-late-lunch-intraday](https://algomatictrading.substack.com/p/strategy-10-the-late-lunch-intraday)
**发布日期**: 2026-04-05
**是否含具体策略逻辑**: 是 (需补充核心笔记)
**原文**: [[algomatictrading-2026-04-05-Strategy-10-The-Late-Lunch-Intraday-System-DAX40.md]]

## 摘要

Strategy #10: The Late Lunch Intraday System (DAX40)
Calm mid-day trends. Fixed risk. Simple timing.
Algomatic Trading
Oct 19, 2025
∙ Paid
14
4
Share
Most traders think all the action happens at the open.
But some of the most stable intraday trends unfold quietly, when the morning noise fades and liquidity returns.
This is what I call the
Late Lunch System
, a clean, intraday approach that rides mid-day directional moves with fixed ATR-based risk sizing.
No prediction. No chasing breakouts. Just structured exposure inside a narrow time window.
The Problem…
Most intraday traders burn out fast.
They scalp noise, over-leverage small moves, and end up feeding spreads instead of compounding returns.
Common pitfalls:
Overtrading:
Sitting through the open and reacting to every tick.
Unscaled risk...

## 核心策略笔记

**来源**: Algomatic Trading
**标的**: DAX (CFDs & Futures)
**时间框架**: 30分钟线
**数据周期**: 2006-2025
**成本假设**: 2点价差已计入

### 策略理念
避开早盘波动集群，捕捉午间更平滑的趋势延续。不预测突破，只在市场结构支持延续时进行结构化敞口。

### 三大组件
1. **时间过滤**: 避开早盘噪音，定位午间趋势窗口
2. **方向性偏向**: 单一规则确保与当前微观趋势一致
3. **固定ATR仓位**: 基于日ATR调整头寸，使每笔交易的风险占组合权益比例恒定

### 回测结果
| 指标 | 数值 |
|------|------|
| 胜率 | **55%** |
| Profit Factor | **1.19** |
| 最大回撤 | **-10.4%** |
| CAGR | **4.7%** |
| 平均持仓时间 | ~11小时 (当日平仓) |
| MAR Ratio | **0.45** |

### 特点
- 无隔夜敞口，完全日内
- 设计为与均值回归/波段策略互补，而非单独使用
- 代码逻辑在付费墙后
