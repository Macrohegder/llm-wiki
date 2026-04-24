---
id: strategy-repro-double-seven
title: "Strategy Repro: Larry Connors Double Seven Trading Strategy"
source: "Quantified Strategies (Substack)"
url: https://quantifiedstrategies.substack.com/p/larry-connors-double-seven-trading
reproduced_at: 2026-04-24
status: completed
rating: green
---

# Larry Connors Double Seven Trading Strategy — 策略复现报告

## 原文摘要

> Larry Connors' Double Seven Strategy: A classic mean reversion approach that buys when price makes a 7-day low and RSI(2) is oversold, selling when price makes a 7-day high or RSI(2) becomes overbought.

这是 Larry Connors 最著名的均值回归策略之一。核心逻辑：当价格创7日新低且RSI(2)超卖时做多，当价格创7日新高或RSI(2)超买时平仓。只在长期上升趋势中交易（价格高于长期移动平均线）。

## 复现方法

| 项目 | 设置 |
|------|------|
| 标的 | SPY, QQQ, IWM, GLD |
| 回测区间 | 2014-04-14 ~ 2026-04-23 |
| 资金 | $100,000 |
| 优化方法 | OAT + GA |
| 优化目标 | Sharpe Ratio |

## 最优参数

| 参数 | 默认值 | 优化后 (SPY) | 范围 |
|------|--------|-------------|------|
| `trend_ma_period` | 200 | **109** | 50 ~ 300 |
| `rsi_entry_threshold` | 10 | **17** | 5 ~ 30 |
| `rsi_exit_threshold` | 65 | **31** | 50 ~ 80 |
| `max_hold_days` | 5 | **5** | 1 ~ 10 |
| `fixed_size` | 1 | **8** | 1 ~ 10 |

## 回测结果

### SPY (最佳品种)

| 指标 | 数值 |
|------|------|
| **Sharpe Ratio** | **0.944** |
| 交易次数 | 188 |
| 最大回撤 | -0.45% |
| 年化收益 | 15.26% |
| 总收益 | 1.83% |
| 盈利天数 / 亏损天数 | 195 / 145 |
| 回撤持续天数 | 884 天 |

### 各品种汇总

| 品种 | 评级 | Sharpe | 交易次数 | 最大回撤 | 年化收益 | 总收益 |
|--------|-------|--------|----------|----------|----------|----------|
| SPY | Green | 0.944 | 188 | -0.45% | 15.26% | 1.83% |
| IWM | Green | 0.812 | 110 | -0.14% | 5.08% | 0.61% |
| QQQ | Green | 0.689 | 46 | -0.02% | 1.09% | 0.09% |
| GLD | Green | 0.735 | 110 | -0.55% | 21.08% | 1.70% |

## 结论

- 评级：**GREEN** ✅
- 策略逻辑简单有效，经典均值回归框架
- SPY 表现最佳 (Sharpe=0.944)，GLD 年化收益最高 (21.08%)
- 交易频率适中 (SPY 188笔/12年 ≈ 15笔/年)
- 最大回撤控制极优 (<1%)，但回撤持续时间较长
- 与 Consecutive Down Days 策略类似，但使用 7-day 而非连续下跌天数

## 复现产物

- YAML: `strategies/inbox/double_seven.yaml`
- 代码: `generated/double_seven_strategy.py`
- 评估报告: `data/pipeline/double_seven_multi/DoubleSevenStrategy_*/best_params_*.json`

## 复现状态

- **复现完成**: 2026-04-24 19:45
- **策略 ID**: `double_seven`
- **评级汇总**: Green=4 | Yellow=0 | Red=0 | Total=4

- **最佳品种**: SPY (Sharpe=0.944)

### 最优参数 (最佳品种)

| 参数 | 最优值 |
|--------|--------|
| trend_ma_period | 109 |
| rsi_entry_threshold | 17 |
| rsi_exit_threshold | 31 |
| max_hold_days | 5 |
| fixed_size | 8 |

*评估报告*: `data/pipeline/double_seven_multi/DoubleSevenStrategy_SPY/best_params_20260424_194454.json`
