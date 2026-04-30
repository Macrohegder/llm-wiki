---
id: strategy-repro-bitcoin-momentum
title: "Strategy Repro: Bitcoin Momentum Strategy"
source: "Quantified Strategies"
url: https://quantifiedstrategies.substack.com/p/bitcoin-momentum-strategy
reproduced_at: 2026-04-24
status: completed
rating: yellow
---

# Bitcoin Momentum Strategy — 策略复现报告

## 原文摘要

> Simple Bitcoin momentum/trend-following strategy. Goes long when price is in an uptrend (based on moving average crossover or price momentum). Exits when trend reverses.

QuantifiedStrategies 原文回测显示：257 trades, ~2% avg gain per trade, ~44% annual return, 22% max drawdown。

## 复现方法

| 项目 | 设置 |
|------|------|
| 标的 | BTCUSDT_SWAP_OKX.GLOBAL, ETHUSDT_SWAP_OKX.GLOBAL |
| 回测区间 | 2020-01-01 ~ 2026-04-23 |
| 资金 | $1,000,000 |
| 优化方法 | OAT + GA |
| 优化目标 | Sharpe Ratio |

## 最优参数 (BTC)

| 参数 | 最优值 |
|------|--------|
| `fast_period` | 4 |
| `slow_period` | 18 |
| `fixed_size` | 15 |
| `cond_lookback_1` | 2 |
| `cond_lookback_2` | 1 |
| `cond_lookback_3` | 1 |
| `cond_lookback_4` | 1 |

## 回测结果

| 指标 | BTC |
|------|-----|
| **Sharpe Ratio** | **0.476** |
| 交易次数 | 598 |
| 最大回撤 | -54.03% |
| 年化收益 | 13.36% |
| 总收益 | 83.15% |

## 结论

- 评级：**YELLOW** ⚠️ ─ Sharpe 0.476 低于 0.5 阈值，接近可接受边界
- **BTC 趋势跟踪有效**: 598次交易，年化13.36%，总收益83%
- **最大回撤过大**: -54% 的回撤需要严格的风险管理
- **参数极端**: fast_period=4, slow_period=18，非常短周期的动量捕捉
- **与原文差异**: 原文44%年化/22%回撤，复现结果13%年化/54%回撤，可能因数据区间或参数优化方向不同
- **建议**: 可尝试添加止损或波动率过滤以降低回撤

## 复现产物

- YAML: `strategies/inbox/bitcoin_momentum_strategy.yaml`
- 代码: `generated/bitcoin_momentum_strategy.py`
- 评估报告: `reports/eval_bitcoin_momentum_strategy_20260424_103404.json`

## 复现状态

- **复现完成**: 2026-04-24 10:34
- **策略 ID**: `bitcoin_momentum_strategy`
- **评级汇总**: Green=0 | Yellow=1 | Red=0 | Total=1

- **最佳品种**: BTCUSDT_SWAP_OKX.GLOBAL (Sharpe=0.476)

### 各品种回测结果

| 品种 | 评级 | Sharpe | 交易次数 | 最大回撤 | 年化收益 | 总收益 |
|--------|-------|--------|----------|----------|----------|----------|
| BTCUSDT_SWAP_OKX.GLOBAL | Yellow | 0.476 | 598 | -54.03% | 13.36% | 83.15% |

### 最优参数 (最佳品种)

| 参数 | 最优值 |
|--------|--------|
| fast_period | 4 |
| slow_period | 18 |
| fixed_size | 15 |
| cond_lookback_1 | 2 |
| cond_lookback_2 | 1 |
| cond_lookback_3 | 1 |
| cond_lookback_4 | 1 |

*评估报告*: `eval_bitcoin_momentum_strategy_20260424_103404.json`
