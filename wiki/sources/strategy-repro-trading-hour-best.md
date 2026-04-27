---
id: strategy-repro-trading-hour-best
title: "Strategy Repro: What Trading Hour Is The Best"
source: "Quantified Strategies"
url: https://quantifiedstrategies.substack.com/p/what-trading-hour-is-the-best
reproduced_at: 2026-04-25
status: failed
rating: red
source_note: 2022-03-09-What-Trading-Hour-Is-The-Best
---

# 最佳交易时间策略 — 复现报告

## 原文摘要

> 分析不同交易时间段的策略表现差异，寻找日内最优交易时段。策略基于特定时间窗口的价格行为规律。

## 复现方法

| 项目 | 设置 |
|------|------|
| 标的 |（未指定）|
| 回测区间 | 2019-01-01 ~ 2025-12-31 |
| 资金 | $100,000 |
| 优化方法 | OAT + GA |

## 回测结果

- **无有效回测结果**
- Pipeline queue 无 result 数据
- Eval JSON 为空结果集（0笔交易）

## 结论

- 评级：**RED** 🔴（无有效回测数据）
- 该策略的YAML描述可能不适合标准的日线回测框架
- 需要根据原文内容重新设计策略逻辑
- 可能需要在更低级别数据（如小时级）上建模

## 复现产物

- YAML: `strategies/inbox/what_trading_hour_is_the_best.yaml`

## 复现状态

- **复现完成**: 2026-04-25（标记为失败）
- **策略 ID**: `what_trading_hour_is_the_best`
- **评级汇总**: Green=0 | Yellow=0 | Red=0 | Total=0

- **最佳品种**: 无

*评估报告*: `eval_what_trading_hour_is_the_best_20260425_052047.json`
