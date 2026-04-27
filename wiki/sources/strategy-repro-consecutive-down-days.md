---
id: strategy-repro-consecutive-down-days
title: "Strategy Repro: Consecutive Down Days Strategy"
source: "QuantSeeker (Substack)"
url: https://quantifiedstrategies.substack.com/p/consecutive-down-days-strategy
reproduced_at: 2026-04-19
status: completed
rating: green
source_note: 2026-04-19-Consecutive-Down-Days-Strategy
---

# Consecutive Down Days Strategy — 策略复现报告

## 原文摘要

> Mean reversion strategy: buy after N consecutive down days, but only when price is above long-term moving average (uptrend). Exit on RSI(2) overbought or max holding days.

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
| `decline_days` | 3 |
| `trend_ma_period` | 90 |
| `max_hold_days` | 5 |
| `rsi_exit_threshold` | 25 |
| `fixed_size` | 15 |

## 回测结果

| 指标 | 数值 |
|------|------|
| **Sharpe Ratio** | 1.762 |
| 交易次数 | 174 |
| 最大回撤 | -2.25% |
| 年化收益 | 6.78% |
| 总收益 | 42.26% |

## 结论

- 评级：**GREEN** ✅
- 最佳品种：**SPY** (Sharpe=1.762)
- 策略复现完成，参数经 OAT 优化后表现稳健

## 复现产物

- YAML: `strategies/inbox/consecutive_down_days_20260419.yaml`
- 代码: `generated/consecutive_down_days_strategy.py`
- 评估报告: `reports/eval_consecutive_down_days_20260419_065041.json`

## 复现状态

- **复现完成**: 2026-04-19
- **策略 ID**: `consecutive_down_days`
- **评级汇总**: Green=11 | Yellow=0 | Red=7 | Total=18

- **最佳品种**: SPY (Sharpe=1.762)

### 各品种回测结果

| 品种 | 评级 | Sharpe | 交易次数 | 最大回撤 | 年化收益 | 总收益 |
|--------|-------|--------|----------|----------|----------|----------|
| SPY | Green | 1.762 | 174 | -2.25% | 6.78% | 42.26% |
| QQQ | Green | 1.029 | 142 | -0.29% | 0.30% | 1.53% |
| IWM | Green | 0.771 | 68 | -0.15% | 0.09% | 0.54% |
| XLK | Green | 1.233 | 68 | -0.30% | 0.38% | 2.39% |
| XLI | Green | 1.097 | 341 | -1.21% | 1.30% | 8.54% |
| XLV | Red | 0.353 | 402 | -2.73% | 0.44% | 2.75% |
| XLF | Red | 0.906 | 14 | -0.01% | 0.01% | 0.04% |
| XLE | Red | 0.679 | 18 | -0.13% | 0.08% | 0.52% |
| DIA | Green | 1.187 | 170 | -2.25% | 3.24% | 21.25% |
| VTI | Green | 1.274 | 170 | -2.29% | 2.59% | 16.97% |
| EFA | Green | 0.600 | 36 | -0.53% | 0.22% | 1.47% |
| EEM | Green | 0.734 | 100 | -0.06% | 0.04% | 0.22% |
| XLB | Red | 0.275 | 319 | -0.17% | 0.02% | 0.14% |
| XLP | Red | 0.914 | 8 | -0.00% | 0.01% | 0.05% |
| XLU | Red | 0.352 | 144 | -0.12% | 0.03% | 0.17% |
| XLRE | Red | 0.124 | 98 | -0.07% | 0.01% | 0.04% |
| TLT | Green | 0.845 | 44 | -0.07% | 0.05% | 0.23% |
| GLD | Green | 1.066 | 108 | -4.03% | 2.43% | 12.27% |

### 最优参数 (最佳品种)

| 参数 | 最优值 |
|--------|--------|
| `decline_days` | 3 |
| `trend_ma_period` | 90 |
| `max_hold_days` | 5 |
| `rsi_exit_threshold` | 25 |
| `fixed_size` | 15 |

*评估报告*: `eval_consecutive_down_days_20260419_065041.json`
