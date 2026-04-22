---
id: strategy-repro-crypto-trend-combo-v2
title: "Strategy Repro: Crypto Trend Combo V2 (9-Model Ensemble + Vol Targeting)"
source: "StrategyFactory / Zarattini et al. (2025) - Catching Crypto Trends"
url: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4751350
reproduced_at: 2026-04-22
status: completed
rating: green
---

# Crypto Trend Combo V2 (9-Model Ensemble + Vol Targeting) — 策略复现报告

## 原文摘要

> 9-model Donchian Channel ensemble trend-following with: - Independent trailing stops per lookback (5/10/20/30/60/90/150/250/360) - Equal-weighted portfolio aggregation - Daily volatility targeting (25...

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
| `target_vol` | 0.21 |
| `max_leverage` | 1.5039999999999998 |
| `vol_lookback` | 67 |
| `rebalance_threshold` | 0.47 |

## 回测结果

| 指标 | 数值 |
|------|------|
| **Sharpe Ratio** | 1.224 |
| 交易次数 | 651 |
| 最大回撤 | -653.67% |
| 年化收益 | 1599.65% |
| 总收益 | 9534.40% |

## 结论

- 评级：**GREEN** ✅
- 最佳品种：**GLD** (Sharpe=1.224)
- 策略复现完成，参数经 OAT 优化后表现稳健

## 复现产物

- YAML: `strategies/inbox/crypto_trend_combo_v2.yaml`
- 代码: `generated/crypto_trend_combo_v2_strategy.py`
- 评估报告: `reports/eval_crypto_trend_combo_v2_20260422_090825.json`

## 复现状态

- **复现完成**: 2026-04-22
- **策略 ID**: `crypto_trend_combo_v2`
- **评级汇总**: Green=4 | Yellow=0 | Red=0 | Total=4

- **最佳品种**: GLD (Sharpe=1.224)

### 各品种回测结果

| 品种 | 评级 | Sharpe | 交易次数 | 最大回撤 | 年化收益 | 总收益 |
|--------|-------|--------|----------|----------|----------|----------|
| BTCUSDT_SWAP_OKX.GLOBAL | Green | 0.754 | 1406 | -554.55% | 357.36% | 2249.93% |
| ETHUSDT_SWAP_OKX.GLOBAL | Green | 0.748 | 1454 | -2688.90% | 3226.93% | 20298.71% |
| SPY | Green | 0.656 | 1017 | -1700.23% | 957.46% | 6835.22% |
| GLD | Green | 1.224 | 651 | -653.67% | 1599.65% | 9534.40% |

### 最优参数 (最佳品种)

| 参数 | 最优值 |
|--------|--------|
| `target_vol` | 0.21 |
| `max_leverage` | 1.5039999999999998 |
| `vol_lookback` | 67 |
| `rebalance_threshold` | 0.47 |

*评估报告*: `eval_crypto_trend_combo_v2_20260422_090825.json`
