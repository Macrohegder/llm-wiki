---
date: "2026-04-04"
author: ""
source: "Substack"
url: "https://quantifiedstrategies.substack.com/p/s-and-p-500-mean-reversion-using-541"
asset: "equity"
strategy: "mean-reversion"
status: "processed"
tags:
  - strategy/mean-reversion
  - asset/equity
  - topic/backtesting
  - status/processed
---

# S&P 500 Mean Reversion Using IBS and RSI: Classical Approach Analysis

> 来源：[Substack](https://quantifiedstrategies.substack.com/p/s-and-p-500-mean-reversion-using-541) | 发布时间：Jun 03, 2024 | 摄入日期：2026-04-04

---

## 核心观点
1. 经典的 IBS + RSI 组合均值回归策略，被评价为"经典方法"。
2. 入场：IBS(0.25) + RSI(21) < 45 同时满足，于收盘价买入。
3. 出场：收盘价高于昨日收盘价。
4. 2000 年至今回测显示策略表现可观，复利运行且未扣除税收。
5. 文章特别强调了参数反转/置换测试的重要性，以验证规则有效性。

## 关键数据/图表
| 组件 | 参数 |
|------|------|
| IBS 阈值 | < 0.25 (日线) |
| RSI 周期 | 21 |
| RSI 阈值 | < 45 |
| 入场触发 | 两条件同时满足，收盘价买入 |
| 出场触发 | 收盘价 > 昨日收盘价 |
| 回测区间 | 2000-今 |
| 回测设定 | 100,000 初始资金，100% 仓位，复利 |

## 提取的实体
- [[entity:QuantifiedStrategies.com]] — 文章来源

## 提取的概念
- [[concept:IBS (Internal Bar Strength)]] — 内部条强度指标
- [[concept:RSI (Relative Strength Index)]] — 21 周期 RSI 应用
- [[concept:Parameter Robustness]] — 参数反转测试验证规则有效性

## 与已有知识的关联
- 相关策略：[[strategy:IBS+RSI Classical Mean Reversion (S&P 500)]]
- 相关综合研究：[[syntheses:均值回归策略对比研究]]

## 个人批注
- IBS 是被低估的简单指标，与 RSI 组合可以过滤掉部分弱势市场中的虚假信号。
- 文章提到的参数置换测试是回测中的关键步骤，很多策略只给出最优参数，却不验证附近区间的稳定性。

## 原文备份
详见 raw/articles/2026-04-04_S&P-500-Mean-Reversion-Using-IBS-and-RSI-Classical-Approach-Analysis.md
