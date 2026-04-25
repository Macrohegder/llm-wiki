---
date: "2026-04-04"
author: ""
source: "Substack"
url: "https://quantifiedstrategies.substack.com/p/3-best-mean-reversion-strategies-695"
asset: "equity"
strategy: "mean-reversion"
status: "processed"
tags:
  - strategy/mean-reversion
  - asset/equity
  - topic/backtesting
  - status/processed
---

# 3 Best Mean Reversion Strategies: Backtested Buy and Sell Signals Analysis

> 来源：[Substack](https://quantifiedstrategies.substack.com/p/3-best-mean-reversion-strategies-695) | 发布时间：Jul 08, 2024 | 摄入日期：2026-04-04

---

## 核心观点
1. 文章提供了3个免费的均值回归策略，均已在多个 ETF 上回测验证。
2. 策略核心逻辑：25 日 H-L 均值 + IBS 指标 + 下轨道突破。
3. 入场：XLP 收盘价低于 2.25 倍 H-L 均值下轨，且 IBS < 0.6。
4. 出场：收盘价高于昨日最高价。
5. 100,000 美元复利运行至今产生了可观的累计收益。

## 关键数据/图表
| 组件 | 参数 |
|------|------|
| H-L 均值周期 | 25 日 |
| 下轨倍数 | 2.25 × H-L 均值 |
| IBS 阈值 | 0.6 |
| 测试标的 | XLP (Consumer Staples) |
| 出场触发 | 收盘价 > 昨日最高价 |

## 提取的实体
- [[entity:XLP]] — 测试标的（消费必需品 ETF）
- [[entity:QuantifiedStrategies.com]] — 文章来源

## 提取的概念
- [[concept:IBS (Internal Bar Strength)]] — (C-L)/(H-L) 比例指标
- [[concept:Mean Reversion]] — 价格回归均值的核心逻辑
- [[concept:Bollinger Bands]] — 波动率带应用

## 与已有知识的关联
- 相关策略：[[strategy:IBS+Bollinger Mean Reversion (XLP)]]
- 相关综合研究：[[syntheses:均值回归策略对比研究]]

## 个人批注
- 该策略使用 XLP 作为测试标的，因为消费必需品类股票波动率较低、回归特性强。
- IBS + 波动率带的组合是经典的简洁均值回归框架，可迁移到其他低波动率品种。

## 原文备份
详见 raw/articles/2026-04-04_3-Best-Mean-Reversion-Strategies-Backtested-Buy-and-Sell-Signals-Analysis.md
