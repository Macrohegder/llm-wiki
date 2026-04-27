---
id: strategy-repro-nr7-breakout
title: "Strategy Repro: NR7 Narrow Range Breakout"
source: "Quantified Strategies"
url: https://quantifiedstrategies.substack.com/p/nr7-trading-strategy-enhanced-narrow
reproduced_at: 2026-04-22
status: completed
rating: green
source_note: strategy-repro-nr7-breakout
tags: [nr7, breakout, quantified-strategies, reproduction, green]
---

# NR7 Narrow Range Breakout — 策略复现报告

## 原文信息
- **来源**: [[strategy-repro-nr7-breakout]]
- **URL**: https://quantifiedstrategies.substack.com/p/nr7-trading-strategy-enhanced-narrow

## 策略说明

买入条件：今日波动范围为 N 日内最窄（NR7）。出场条件：收盘价突破前一日高点。可选趋势过滤器（MA）仅在上升趋势中交易。

## 复现方法

| 项目 | 设置 |
|------|------|
| 标的 | SPY |
| 回测区间 | 2019-01-01 ~ 2025-12-31 |
| 资金 | $100,000 |
| 优化方法 | OAT + GA |
| 优化目标 | Sharpe Ratio |

## 最优参数 (最佳品种 SPY)

| 参数 | 最优值 |
|------|--------|
| `nr_lookback` | 2 |
| `use_trend_filter` | 0.7 |
| `trend_ma_period` | 15 |
| `use_long_only` | 0.94 |
| `fixed_size` | 1 |

## 各品种回测结果

| 品种 | 评级 | Sharpe | 交易次数 | 最大回撤 | 年化收益 | 总收益 |
|------|------|--------|---------|---------|---------|--------|
| SPY | 🟢 Green | 1.288 | 460 | -0.52% | 0.60% | 3.67% |
| QQQ | 🟡 Yellow | 0.902 | 166 | -0.54% | 0.36% | 1.81% |
| BTCUSDT | 🔴 Red | 0.650 | 284 | -19.07% | 11.50% | 71.34% |
| ETHUSDT | 🔴 Red | 0.696 | 441 | -20.11% | 10.84% | 67.22% |
| SOLUSDT | 🔴 Red | 0.343 | 275 | -1.89% | 0.43% | 2.19% |
| DOGEUSDT | 🔴 Red | 0.268 | 379 | -5.96% | 0.96% | 5.48% |

## 结论

- **评级**：GREEN ✅（SPY 表现稳健）
- SPY Sharpe=1.288，最大回撤仅 -0.52%，非常稳健
- 加密货币品种（BTC/ETH/SOL/DOGE）均表现不佳，Sharpe 均 < 0.7
- 策略适合股票指数，不适合数字货币

## 复现产物

- YAML: `strategies/inbox/nr7_breakout_20260416.yaml`
- 代码: `generated/nr7_breakout_strategy.py`
- 评估报告: `reports/eval_nr7_breakout_20260422_094223.json`
