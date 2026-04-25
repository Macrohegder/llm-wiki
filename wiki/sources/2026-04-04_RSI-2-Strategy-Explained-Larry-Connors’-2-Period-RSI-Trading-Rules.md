---
date: "2026-04-04"
author: "Larry Connors"
source: "Substack"
url: "https://quantifiedstrategies.substack.com/p/rsi-2-strategy-explained-larry-connors"
asset: "equity"
strategy: "mean-reversion"
status: "processed"
tags:
  - strategy/mean-reversion
  - asset/equity
  - topic/backtesting
  - status/processed
---

# RSI 2 Strategy Explained: Larry Connors' 2-Period RSI Trading Rules

> 来源：[Substack](https://quantifiedstrategies.substack.com/p/rsi-2-strategy-explained-larry-connors) | 作者：Larry Connors / QuantifiedStrategies | 摄入日期：2026-04-04

---

## 核心观点
1. RSI(2) 是经典短期均值回归策略，通过极端敏感的2周期 RSI 捕捉快速反弹。
2. 入场：SPY 的 RSI(2) 低于 10 时于收盘价买入；出场：RSI(2) 穿越 80 时退出。
3. 1993 至今回测：CAGR 9%，平均每笔收益 0.9%，市场占用率仅 28%。
4. 最大回撤 34%，这是该策略最大的风险点，需要配合仓位管理使用。
5. 传统 14 周期 RSI 过于平滑，RSI(2) 的极端敏感性正是其在短期回归中的优势所在。

## 关键数据/图表
| 指标 | 数值 |
|------|------|
| CAGR | 9% |
| 平均每笔收益 | 0.9% |
| 最大回撤 | 34% |
| 市场占用率 | 28% |
| 测试标的 | SPY (1993-今) |

## 提取的实体
- [[entity:Larry Connors]] — 策略创始人
- [[entity:QuantifiedStrategies.com]] — 文章来源
- [[entity:SPY]] — 测试标的

## 提取的概念
- [[concept:Mean Reversion]] — 均值回归核心思想
- [[concept:RSI (Relative Strength Index)]] — 2 周期 vs 14 周期的对比
- [[concept:Position Sizing]] — 高回撤策略必须配合仓位管理

## 与已有知识的关联
- 相关策略：[[strategy:RSI-2 Mean Reversion (SPY)]]
- 相关综合研究：[[syntheses:均值回归策略对比研究]]

## 个人批注
- 34% 回撤对于个人交易来说太高，实际使用时应考虑加入 VIX 筛选或降低仓位。
- 该策略很适合与趋势跟踪策略组合，利用其低相关性。

## 原文备份
详见 raw/articles/2026-04-04_RSI-2-Strategy-Explained-Larry-Connors'-2-Period-RSI-Trading-Rules.md
