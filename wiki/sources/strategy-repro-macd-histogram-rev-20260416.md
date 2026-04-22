---
id: strategy-repro-macd-histogram-rev-20260416
title: "Strategy Repro: MACD Histogram Mean Reversion"
source: "Quantified Strategies"
url: https://quantifiedstrategies.substack.com/p/macd-histogram-strategy
reproduced_at: 2026-04-16
status: completed
rating: green
---

# MACD Histogram Mean Reversion — 策略复现报告

## 原文摘要

> 

## 复现方法

| 项目 | 设置 |
|------|------|
| 标的 | QQQ |
| 回测区间 | 2019-01-01 ~ 2025-12-31 |
| 资金 | $100,000 |
| 优化方法 | OAT + GA |
| 优化目标 | Sharpe Ratio |

## 最优参数

| 参数 | 最优值 |
|------|--------|
| `decline_days` | 3 |
| `signal_period` | 12 |
| `slow_period` | 34 |

## 回测结果

| 指标 | 数值 |
|------|------|
| **Sharpe Ratio** | 1.038 |
| 交易次数 | 92 |
| 最大回撤 | -40.25% |
| 年化收益 | 38.79% |
| 总收益 | 192.41% |

## 结论

- 评级：**GREEN** ✅
- 最佳品种：**QQQ** (Sharpe=1.038)
- 策略复现完成，参数经 OAT 优化后表现稳健

## 复现产物

- YAML: `strategies/inbox/macd_histogram_rev_20260416.yaml`
- 代码: `generated/macd_histogram_rev_20260416_strategy.py`
- 评估报告: `reports/eval_macd_histogram_rev_20260416_20260416_064027.json`

## 复现状态

- **复现完成**: 2026-04-16
- **策略 ID**: `macd_histogram_rev_20260416`
- **评级汇总**: Green=1 | Yellow=1 | Red=0 | Total=2

- **最佳品种**: QQQ (Sharpe=1.038)

### 各品种回测结果

| 品种 | 评级 | Sharpe | 交易次数 | 最大回撤 | 年化收益 | 总收益 |
|--------|-------|--------|----------|----------|----------|----------|
| SPY | Yellow | 0.815 | 136 | -31.84% | 28.78% | 177.68% |
| QQQ | Green | 1.038 | 92 | -40.25% | 38.79% | 192.41% |

### 最优参数 (最佳品种)

| 参数 | 最优值 |
|--------|--------|
| `decline_days` | 3 |
| `signal_period` | 12 |
| `slow_period` | 34 |

*评估报告*: `eval_macd_histogram_rev_20260416_20260416_064027.json`
