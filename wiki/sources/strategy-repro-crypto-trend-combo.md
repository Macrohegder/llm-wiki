---
id: strategy-repro-crypto-trend-combo
title: "Strategy Repro: Crypto Trend Combo (Donchian Breakout + Vol Targeting)"
source: "StrategyFactory / Zarattini et al. (2025) - Catching Crypto Trends"
url: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4751350
reproduced_at: 2026-04-22
status: completed
rating: green
---

# Crypto Trend Combo (Donchian Breakout + Vol Targeting) — 策略复现报告

## 原文摘要

> Approximation of the Combo ensemble trend-following model from "Catching Crypto Trends" (Zarattini, Pagani, Barbon 2025). Simplified to single lookback Donchian Channel breakout with trailing stop (Do...

## 复现方法

| 项目 | 设置 |
|------|------|
| 标的 | BTCUSDT_SWAP_OKX.GLOBAL |
| 回测区间 | 2019-01-01 ~ 2025-12-31 |
| 资金 | $100,000 |
| 优化方法 | OAT + GA |
| 优化目标 | Sharpe Ratio |

## 最优参数

| 参数 | 最优值 |
|------|--------|
| `donchian_window` | 38 |
| `vol_lookback` | 44 |
| `target_vol` | 0.13299999999999998 |
| `max_leverage` | 0.63 |

## 回测结果

| 指标 | 数值 |
|------|------|
| **Sharpe Ratio** | 1.741 |
| 交易次数 | 23 |
| 最大回撤 | -4.99% |
| 年化收益 | 14.31% |
| 总收益 | 90.11% |

## 结论

- 评级：**GREEN** ✅
- 最佳品种：**BTCUSDT_SWAP_OKX.GLOBAL** (Sharpe=1.741)
- 策略复现完成，参数经 OAT 优化后表现稳健

## 复现产物

- YAML: `strategies/inbox/crypto_trend_combo.yaml`
- 代码: `generated/crypto_trend_combo_strategy.py`
- 评估报告: `reports/eval_crypto_trend_combo_20260422_090538.json`

## 复现状态

- **复现完成**: 2026-04-22
- **策略 ID**: `crypto_trend_combo`
- **评级汇总**: Green=4 | Yellow=0 | Red=0 | Total=4

- **最佳品种**: BTCUSDT_SWAP_OKX.GLOBAL (Sharpe=1.741)

### 各品种回测结果

| 品种 | 评级 | Sharpe | 交易次数 | 最大回撤 | 年化收益 | 总收益 |
|--------|-------|--------|----------|----------|----------|----------|
| BTCUSDT_SWAP_OKX.GLOBAL | Green | 1.741 | 23 | -4.99% | 14.31% | 90.11% |
| ETHUSDT_SWAP_OKX.GLOBAL | Green | 1.451 | 87 | -298.32% | 487.74% | 3068.09% |
| SPY | Green | 0.683 | 65 | -1261.08% | 694.01% | 4954.48% |
| GLD | Green | 1.321 | 46 | -528.45% | 946.00% | 5638.46% |

### 最优参数 (最佳品种)

| 参数 | 最优值 |
|--------|--------|
| `donchian_window` | 38 |
| `vol_lookback` | 44 |
| `target_vol` | 0.13299999999999998 |
| `max_leverage` | 0.63 |

*评估报告*: `eval_crypto_trend_combo_20260422_090538.json`
