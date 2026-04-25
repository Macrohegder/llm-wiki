---
date: "2026-04-04"
author: ""
source: "Substack"
url: "https://quantifiedstrategies.substack.com/p/profitable-williams-r-strategy-for"
asset: "equity"
strategy: "mean-reversion"
status: "processed"
tags:
  - strategy/mean-reversion
  - asset/equity
  - topic/backtesting
  - topic/risk-management
  - status/processed
---

# Profitable Williams %R Strategy For Mean Reversion Trading (Only 2 Rules)

> 来源：[Substack](https://quantifiedstrategies.substack.com/p/profitable-williams-r-strategy-for) | 发布时间：Mar 01, 2026 | 摄入日期：2026-04-04

---

## 核心观点
1. Williams %R(5) 极简均值回归策略，仅 2 条规则，在 QQQ 上胜率达 72%。
2. 入场：5 日 Williams %R 收盘价低于 -90 时买入；出场：收盘价高于昨日最高价时退出。
3. QQQ 回测：CAGR 11.5%，市场占用率仅 21%，年均约 15 笔交易。
4. 不使用硬止损：均值回归中止损可能在价格反弹前触发，建议用小仓位 + 多类别分散代替。
5. 此策略专为股票型 ETF 设计，在商品/金属上无效，资产类别选择至关重要。

## 关键数据/图表
| 指标 | 数值 |
|------|------|
| 回测标的 | QQQ (至今) |
| CAGR | 11.5% |
| 胜率 | 72% |
| 市场占用率 | 21% |
| 年均交易次数 | ~15 次 |
| 平均每笔收益 | 0.9% |
| 单笔最大亏损 | 18% (20 年数据中仅 1 次超过 10%) |
| 回望周期 | 5 日 |

## 提取的实体
- [[entity:QuantifiedStrategies.com]] — 文章来源
- [[entity:QQQ]] — Nasdaq 100 ETF，测试标的

## 提取的概念
- [[concept:Williams %R]] — 威廉指标，测量价格在高低区间的位置
- [[concept:Mean Reversion]] — 价格偏离后向均值回归
- [[concept:Position Sizing]] — 无止损策略的风控核心

## 与已有知识的关联
- 相关策略：[[strategy:Williams %R 5-Day Oversold (QQQ)]]
- 相关综合研究：[[syntheses:均值回归策略对比研究]]

## 个人批注
- “无止损”设计是均值回归策略的典型特征，但对心理承受力要求极高，必须配合严格的仓位管理。
- 11.5% CAGR + 21% 占用率 = 有效年化约 55%，资金效率极高。

## 原文备份
详见 raw/articles/2026-04-04_Profitable-Williams-%R-Strategy-For-Mean-Reversion-Trading-(Only-2-Rules).md
