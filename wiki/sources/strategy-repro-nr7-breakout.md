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

## 复现状态

- **复现完成**: 2026-04-22
- **策略 ID**: `nr7_breakout`
- **评级汇总**: Green=1 | Yellow=1 | Red=4 | Total=6

- **最佳品种**: SPY (Sharpe=1.288)

### 各品种回测结果

| 品种 | 评级 | Sharpe | 交易次数 | 最大回撤 | 年化收益 | 总收益 |
|--------|-------|--------|----------|----------|----------|----------|
| SPY | Green | 1.288 | 460 | -0.52% | 0.60% | 3.67% |
| QQQ | Yellow | 0.902 | 166 | -0.54% | 0.36% | 1.81% |
| BTCUSDT_SWAP_OKX.GLOBAL | Red | 0.650 | 284 | -19.07% | 11.50% | 71.34% |
| ETHUSDT_SWAP_OKX.GLOBAL | Red | 0.696 | 441 | -20.11% | 10.84% | 67.22% |
| SOLUSDT_SWAP_OKX.GLOBAL | Red | 0.343 | 275 | -1.89% | 0.43% | 2.19% |
| DOGEUSDT_SWAP_OKX.GLOBAL | Red | 0.268 | 379 | -5.96% | 0.96% | 5.48% |

### 最优参数 (最佳品种)

| 参数 | 最优值 |
|--------|--------|
| `nr_lookback` | 2 |
| `use_trend_filter` | 0.7 |
| `trend_ma_period` | 15 |
| `use_long_only` | 0.94 |
| `fixed_size` | 1 |

*评估报告*: `eval_nr7_breakout_20260422_094223.json`
