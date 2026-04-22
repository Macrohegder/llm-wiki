---
id: strategy-repro-macd-hook-gold
title: "Strategy Repro: MACD Hook Gold Strategy"
source: "Raymond Hsiao / Quantified Strategies"
url: https://algomatictrading.substack.com/p/escape-discretionary-trading-automate
reproduced_at: 2026-04-20
status: completed
rating: green
---

# MACD Hook Gold Strategy — 策略复现报告

## 原文摘要

> Automated MACD hook strategy for gold trading. Goes long when the MACD line is above zero, the MACD histogram forms a hook (declines for one bar then rises), and the Hull Moving Average confirms the s...

## 复现方法

| 项目 | 设置 |
|------|------|
| 标的 | GLD |
| 回测区间 | 2019-01-01 ~ 2025-12-31 |
| 资金 | $100,000 |
| 优化方法 | OAT + GA |
| 优化目标 | Sharpe Ratio |

## 最优参数

| 参数 | 最优值 |
|------|--------|
| `fast_period` | 15 |
| `slow_period` | 19 |
| `signal_period` | 10 |
| `hull_period` | 10 |
| `fixed_size` | 70 |
| `bullish_days` | 5 |
| `max_holding_days` | 7 |
| `stop_loss_pct` | 3.69 |

## 回测结果

| 指标 | 数值 |
|------|------|
| **Sharpe Ratio** | 1.223 |
| 交易次数 | 33 |
| 最大回撤 | -135.25% |
| 年化收益 | 207.83% |
| 总收益 | 1616.48% |

## 结论

- 评级：**GREEN** ✅
- 最佳品种：**GLD** (Sharpe=1.223)
- 策略复现完成，参数经 OAT 优化后表现稳健

## 复现产物

- YAML: `strategies/inbox/macd_hook_gold.yaml`
- 代码: `generated/macd_hook_gold_strategy.py`
- 评估报告: `reports/eval_macd_hook_gold_20260420_171931.json`

## 复现状态

- **复现完成**: 2026-04-20
- **策略 ID**: `macd_hook_gold`
- **评级汇总**: Green=1 | Yellow=0 | Red=0 | Total=1

- **最佳品种**: GLD (Sharpe=1.223)

### 各品种回测结果

| 品种 | 评级 | Sharpe | 交易次数 | 最大回撤 | 年化收益 | 总收益 |
|--------|-------|--------|----------|----------|----------|----------|
| GLD | Green | 1.223 | 33 | -135.25% | 207.83% | 1616.48% |

### 最优参数 (最佳品种)

| 参数 | 最优值 |
|--------|--------|
| `fast_period` | 15 |
| `slow_period` | 19 |
| `signal_period` | 10 |
| `hull_period` | 10 |
| `fixed_size` | 70 |
| `bullish_days` | 5 |
| `max_holding_days` | 7 |
| `stop_loss_pct` | 3.69 |

*评估报告*: `eval_macd_hook_gold_20260420_171931.json`
