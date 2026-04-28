---
id: 2026-04-22-Bollinger-Band-Squeeze-Trading-Strategy
title: "Bollinger Band Squeeze Trading Strategy"
source: "QuantifiedStrategies"
url: https://quantifiedstrategies.substack.com/p/bollinger-band-squeeze-trading-strategy
date: "2026-04-22"
tags:
status: reproduced
reproduction_id: strategy-repro-bollinger-band-squeeze
  - strategy/volatility-breakout
  - asset/equity
  - topic/backtesting
rating: yellow
status: ingested
---

# Bollinger Band Squeeze Trading Strategy

> 来源: [QuantifiedStrategies](https://quantifiedstrategies.substack.com/p/bollinger-band-squeeze-trading-strategy) | 摄入日期: 2026-04-22

## 一句话摘要

布林带挤压策略是一种基于波动率的方法，目标是在市场平静期后捕捉爆发性价格移动。挤压本身不预测方向，只预示大幅波动即将到来。

## 核心观点

1. **挤压定义**: 上下布林带显著收窄，反映低波动率阶段
2. **三阶段**: Contraction (收窄) → Breakout (突破) → Expansion (扩张)
3. **基础规则**: 收盘突破上轨做多，收盘突破下轨做空，止损放在对侧带附近
4. **回测设置**: 使用周线、10周数据、10周布林带宽度、10-bar RSI for volatility bands
5. **测试结果**: 对消费股 (PEP) 回测表现良好，但完整规则付费

## 提取的实体
- [[entity:John Bollinger]] (布林带原理提出者，未直接提及)
- [[entity:QuantifiedStrategies]]

## 提取的概念
- [[concept:Bollinger Band Squeeze]]
- [[concept:Volatility Breakout]]
- [[concept:Coiled Spring Pattern]]
