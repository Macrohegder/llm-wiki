---
id: strategy-repro-stochastic-extremes-gold
title: "Strategy Repro: Stochastic Extremes Gold — Mean-Reversion Gold System"
source: "AlgoMatictrading"
url: https://algomatictrading.substack.com/p/strategy-7-a-mean-reversion-gold-system
reproduced_at: 2026-04-25
status: completed
rating: red
source_note: 2026-04-05-Strategy-7-A-Mean-Reversion-Gold-System-Using-Stochastic-Extremes
---

# Stochastic Extremes Gold — 均值回归黄金系统复现报告

## 原文摘要

> 策略#7：基于随机指标(Stochastic)极值的黄金均值回归系统。在随机指标进入超卖区域（<20）时开多仓，配合趋势过滤和ATR动态止损。

## 复现方法

| 项目 | 设置 |
|------|------|
| 标的 | SPY, QQQ, IWM, GLD |
| 回测区间 | 2019-01-01 ~ 2025-12-31 |
| 资金 | $100,000 |
| 优化方法 | OAT + GA |
| 优化目标 | Sharpe Ratio |

## 最优参数

| 参数 | 最优值 |
|------|--------|
| Stochastic Length | 14 |
| Stochastic %D Period | 3 |
| Stochastic Smooth | 5 |
| 超卖阈值 | 11 |
| 趋势过滤周期 | 82 |
| ATR周期 | 9 |
| 止损百分比 | 1.18% |
| 固定仓位 | 15 |

## 回测结果

| 指标 | 数值 |
|------|------|
| **Sharpe Ratio** | 0.956（GLD） |
| 交易次数 | 1（GLD） |
| 最大回撤 | -301.90%（GLD） |
| 年化收益 | 198.53%（GLD） |
| 总收益 | 1473.21%（GLD） |

## 结论

- 评级：**RED** 🔴（全品种）
- 所有品种交易次数极少（1-5笔），导致统计意义不足
- GLD 虽有0.956的Sharpe，但仅1笔交易，不可信赖
- 策略在OAT优化后仍无法产生足够的交易信号，可能由于超卖阈值过于严格
- 需要进一步放宽入场条件或调整趋势过滤参数

## 复现产物

- YAML: `strategies/inbox/stochastic_extremes_gold.yaml`
- 代码: `generated/stochastic_extremes_gold_strategy.py`
- 评估报告: `reports/eval_stochastic_extremes_gold_20260423_011123.json`

## 复现状态

- **复现完成**: 2026-04-25
- **策略 ID**: `stochastic_extremes_gold`
- **评级汇总**: Green=0 | Yellow=0 | Red=4 | Total=4

- **最佳品种**: GLD (Sharpe=0.956)

### 各品种回测结果

| 品种 | 评级 | Sharpe | 交易次数 | 最大回撤 | 年化收益 | 总收益 |
|--------|-------|--------|----------|----------|----------|----------|
| SPY | RED | 0.624 | 3 | -59.78% | 19.17% | 216.88% |
| QQQ | RED | 0.761 | 1 | -137.85% | 59.42% | 440.93% |
| IWM | RED | 0.223 | 5 | -79.68% | 6.71% | 75.87% |
| GLD | RED | 0.956 | 1 | -301.90% | 198.53% | 1473.21% |

### 最优参数 (最佳品种 GLD)

| 参数 | 最优值 |
|--------|--------|
| Stochastic Length | 14 |
| Stochastic %D Period | 3 |
| Stochastic Smooth | 5 |
| 超卖阈值 | 11 |
| 趋势过滤周期 | 82 |
| ATR周期 | 9 |
| 止损百分比 | 1.18% |

*评估报告*: `eval_stochastic_extremes_gold_20260423_011123.json`
