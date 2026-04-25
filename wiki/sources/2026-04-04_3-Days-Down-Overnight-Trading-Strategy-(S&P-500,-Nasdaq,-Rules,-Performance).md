---
date: "2026-04-04"
author: ""
source: "Substack"
url: "https://quantifiedstrategies.substack.com/p/3-days-down-overnight-trading-strategy-1db"
asset: "equity"
strategy: "mean-reversion"
status: "processed"
tags:
  - strategy/mean-reversion
  - asset/equity
  - topic/backtesting
  - status/processed
---

# 3 Days Down Overnight Trading Strategy (S&P 500, Nasdaq, Rules, Performance)

> 来源：[Substack](https://quantifiedstrategies.substack.com/p/3-days-down-overnight-trading-strategy-1db) | 发布时间：Aug 10, 2024 | 摄入日期：2026-04-04

---

## 核心观点
1. 简单的隔夜均值回归策略：SPY 连跌 3 天后于第 3 天收盘价买入，次日开盘价出场。
2. 持仓时间极短（仅一个隔夜），属于"股市中最低垂手可得的果实"。
3. 1993 年至今 SPY 回测由 Amibroker 完成，表明该效应在 S&P 500 中持久存在。
4. 该策略的魔力在于极致简洁，无需任何指标，仅依靠连续下跌的心理学偏差。
5. 文章提到网站上有更复杂的修正版本可供参考。

## 关键数据/图表
| 组件 | 参数 |
|------|------|
| 入场条件 | SPY 连跌 3 天（收盘价计算） |
| 入场时间 | 第 3 天收盘价 |
| 出场时间 | 次日开盘价 |
| 回测工具 | Amibroker |
| 回测区间 | 1993-今 |

## 提取的实体
- [[entity:SPY]] — S&P 500 ETF，策略主要测试标的
- [[entity:QuantifiedStrategies.com]] — 文章来源

## 提取的概念
- [[concept:Overnight Edge]] — 隔夜效应/风险溢价
- [[concept:Mean Reversion]] — 短期连续下跌后的心理学偏差反转
- [[concept:Behavioral Finance]] — 投资者过度反应导致的价格反弹

## 与已有知识的关联
- 相关策略：[[strategy:3 Days Down Overnight (SPY)]]
- 相关综合研究：[[syntheses:均值回归策略对比研究]]

## 个人批注
- 隔夜策略对执行要求高，需要在收盘前完成信号判断。
- 该策略产生的交易次数少、每次利润小，适合作为组合中的辅助策略。

## 原文备份
详见 raw/articles/2026-04-04_3-Days-Down-Overnight-Trading-Strategy-(S&P-500,-Nasdaq,-Rules,-Performance).md
