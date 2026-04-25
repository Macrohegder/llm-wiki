---
title: "Systematic Intraday Trend-Following Strategy"
source_url: "https://quantifiedstrategies.substack.com/p/systematic-intraday-trend-following"
pub_date: "Feb 23, 2026"
has_strategy_logic: true
strategy_score: 14
source_file: "Sources/Substack/Intraday/2026-04-04-Systematic-Intraday-Trend-Following-Strategy.md"
tags: [intraday, day-trading, substack]
---

# Systematic Intraday Trend-Following Strategy

**来源**: [https://quantifiedstrategies.substack.com/p/systematic-intraday-trend-following](https://quantifiedstrategies.substack.com/p/systematic-intraday-trend-following)
**发布日期**: Feb 23, 2026
**是否含具体策略逻辑**: 是 (需补充核心笔记)
**原文**: [[2026-04-04-Systematic-Intraday-Trend-Following-Strategy.md]]

## 摘要

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
Why...

## 核心策略笔记

**作者**: Carlo Zarattini (Concretum)
**核心逻辑**: 日内动量 — "强势生强势" (strength begets strength)。不参与预测，只参与趋势中段。

### 交易规则
1. **动态边界**: 基于过去14天开盘价后的平均价格变动，全天动态调整交易区间
2. **隔夜缺口调整**: 边界针对隔夜跳空进行修正
3. **入场信号**:
   - 价格突破上轨 → 做多 (强势买盘)
   - 价格跌破下轨 → 做空 (异常卖盘)
4. **止损**: VWAP (成交量加权平均价) 作为保护性止损
5. **动态仓位**: 根据日波动率调整头寸大小
6. **执行频率**: 仅在每小时的整点/半点执行，过滤噪音

### 关键特点
- 不同时段触发阈值不同。例如10:30下跌-0.30%即可触发，而15:30可能需要-0.60%，因为日内波动范围随时间推移而扩大。

### 回测结果 (SPY)
| 指标 | 数值 |
|------|------|
| 总收益 | **1,985%** |
| 年化收益 | **19.6%** |
| 夏普比率 | **1.33** (买入持有仅0.45) |
| Beta | 略低于0 (市场无关) |
| VIX>40时夏普 | **3.50** |
| 佣金 | $0.0035/股 (IB入门级) |

### ⚠️ 注意事项
- **未计入滑点**，日内策略滑点可能显著，实盘收益通常低于回测
- 论文发表于2024年夏，作者称样本外(out-of-sample)至今表现依然强劲
