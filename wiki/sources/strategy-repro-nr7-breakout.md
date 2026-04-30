---
id: strategy-repro-nr7-breakout
title: "Strategy Repro: NR7 Narrow Range Breakout"
source: "Quantified Strategies"
url: https://quantifiedstrategies.substack.com/p/nr7-trading-strategy-enhanced-narrow
reproduced_at: 2026-04-22
status: completed
rating: green
source_note: nr7-breakout-reproduction
tags: [nr7, breakout, quantified-strategies, reproduction, green]
---

# NR7 Narrow Range Breakout — 策略复现报告

## 原文信息
- **来源**: [[nr7-breakout-reproduction]]
- **URL**: https://quantifiedstrategies.substack.com/p/nr7-trading-strategy-enhanced-narrow

## 原文摘要

> Buy when today's range is the narrowest in N days (NR7). Exit when close exceeds previous day's high. Optional trend filter using MA to only trade in uptrends.

## 复现方法

| 项目 | 设置 |
|------|------|
| 标的 | SPY |
| 回测区间 | 2019-01-01 ~ 2025-12-31 |
| 资金 | $100,000 |
| 优化方法 | OAT + GA |
| 优化目标 | Sharpe Ratio |

## 最优参数

| 参数 | 最优值 |
|------|--------|
| `nr_lookback` | 2 |
| `use_trend_filter` | 0.7 |
| `trend_ma_period` | 15 |
| `use_long_only` | 0.94 |
| `fixed_size` | 1 |

## 回测结果

| 指标 | 数值 |
|------|------|
| **Sharpe Ratio** | 1.288 |
| 交易次数 | 460 |
| 最大回撤 | -0.52% |
| 年化收益 | 0.60% |
| 总收益 | 3.67% |

## 结论

- 评级：**GREEN** ✅
- 最佳品种：**SPY** (Sharpe=1.288)
- 策略复现完成，参数经 OAT 优化后表现稳健

## 复现产物

- YAML: `strategies/inbox/nr7_breakout_20260416.yaml`
- 代码: `generated/nr7_breakout_strategy.py`
- 评估报告: `reports/eval_nr7_breakout_20260422_094223.json`

## 复现追踪

| 复现日期 | 复现报告 | 状态 | 最佳品种 |
|----------|----------|------|----------|
| 2026-04-30 | [[strategy-repro-nr7_breakout]] | 🟢 Green | SPY (Sharpe=1.212) |

> **当前有效复现**: [[strategy-repro-nr7_breakout]]
