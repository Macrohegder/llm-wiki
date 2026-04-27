---
id: strategy-repro-donchian-adx-breakout
title: "Strategy Repro: Donchian Channel + ADX Breakout"
source: "Quantified Strategies"
url: https://algomatictrading.substack.com/p/strategy-8-the-easiest-trend-system
reproduced_at: 2026-04-22
status: completed
rating: green
source_note: 2026-04-05-Strategy-8-The-Easiest-Trend-System-Youll-Ever-Trade-Donchian-Channel-Breakout
---

# Donchian Channel + ADX Breakout — 策略复现报告

## 原文摘要

> Buy when price breaks above Donchian upper band and ADX is below threshold (low volatility breakout). Exit when price falls below Donchian lower band. Optional trend filter using long-term MA.

## 复现方法

| 项目 | 设置 |
|------|------|
| 标的 | ETHUSDT_SWAP_OKX.GLOBAL |
| 回测区间 | 2019-01-01 ~ 2025-12-31 |
| 资金 | $100,000 |
| 优化方法 | OAT + GA |
| 优化目标 | Sharpe Ratio |

## 最优参数

| 参数 | 最优值 |
|------|--------|
| `donchian_window` | 5 |
| `exit_window` | 5 |
| `adx_window` | 12 |
| `adx_threshold` | 18 |
| `adx_mode` | 1 |
| `use_long_only` | 1.06 |
| `ma_period` | 130 |
| `fixed_size` | 15 |

## 回测结果

| 指标 | 数值 |
|------|------|
| **Sharpe Ratio** | 1.192 |
| 交易次数 | 30 |
| 最大回撤 | -14.21% |
| 年化收益 | 14.76% |
| 总收益 | 91.56% |

## 结论

- 评级：**GREEN** ✅
- 最佳品种：**ETHUSDT_SWAP_OKX.GLOBAL** (Sharpe=1.192)
- 策略复现完成，参数经 OAT 优化后表现稳健

## 复现产物

- YAML: `strategies/inbox/donchian_adx_breakout_20260416.yaml`
- 代码: `generated/donchian_adx_breakout_strategy.py`
- 评估报告: `reports/eval_donchian_adx_breakout_20260422_093345.json`

## 复现状态

- **复现完成**: 2026-04-22
- **策略 ID**: `donchian_adx_breakout`
- **评级汇总**: Green=2 | Yellow=1 | Red=3 | Total=6

- **最佳品种**: ETHUSDT_SWAP_OKX.GLOBAL (Sharpe=1.192)

### 各品种回测结果

| 品种 | 评级 | Sharpe | 交易次数 | 最大回撤 | 年化收益 | 总收益 |
|--------|-------|--------|----------|----------|----------|----------|
| SPY | Red | 1.016 | 10 | -0.48% | 0.55% | 3.37% |
| QQQ | Yellow | 1.029 | 28 | -11.71% | 10.21% | 50.64% |
| BTCUSDT_SWAP_OKX.GLOBAL | Red | 1.169 | 14 | -12.81% | 13.16% | 81.61% |
| ETHUSDT_SWAP_OKX.GLOBAL | Green | 1.192 | 30 | -14.21% | 14.76% | 91.56% |
| SOLUSDT_SWAP_OKX.GLOBAL | Green | 1.104 | 60 | -6.63% | 9.65% | 49.60% |
| DOGEUSDT_SWAP_OKX.GLOBAL | Red | 0.437 | 108 | -5.86% | 1.74% | 9.89% |

### 最优参数 (最佳品种)

| 参数 | 最优值 |
|--------|--------|
| `donchian_window` | 5 |
| `exit_window` | 5 |
| `adx_window` | 12 |
| `adx_threshold` | 18 |
| `adx_mode` | 1 |
| `use_long_only` | 1.06 |
| `ma_period` | 130 |
| `fixed_size` | 15 |

*评估报告*: `eval_donchian_adx_breakout_20260422_093345.json`
