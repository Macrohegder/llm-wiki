---
id: strategy-repro-gold-envelope
title: "Strategy Repro: Gold Envelope Trading Strategy"
source: "Quantified Strategies"
url: https://quantifiedstrategies.substack.com/p/gold-envelope-trading-strategy-rules
reproduced_at: 2026-04-25
status: partial
rating: yellow
---

# Gold Envelope Trading Strategy — 策略复现报告

## 原文摘要

> Gold Envelope（黄金包络线）策略是一种均值回归策略。通过计算价格在移动平均线上下一定百分比的包络带，当价格触及下轨时做多，触及上轨时做空。适合震荡市场环境，在趋势市场中需谨慎使用。

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
| SMA Period | 20 |
| 固定仓位 | 1 |

## 回测结果

| 指标 | 数值 |
|------|------|
| **Sharpe Ratio** | 1.357 |
| 交易次数 | 93 |
| 最大回撤 | -0.22% |
| 年化收益 | 0.27% |
| 总收益 | 1.35% |

## 结论

- 评级：**GREEN** ✅（GLD 品种）
- 最佳品种：**GLD** (Sharpe=1.357)
- 策略在 GLD 上表现稳健，Sharpe > 1.3，交易次数充足（93笔），最大回撤极低（-0.22%）
- 注意总收益较低（1.35%），可能是仓位管理较为保守

## 复现产物

- YAML: `strategies/inbox/gold_envelope.yaml`
- 代码: `generated/gold_envelope_trading_strategy.py`
- 评估报告: `reports/eval_gold_envelope_trading_strategy_20260425_053109.json`

## 复现状态

- **复现完成**: 2026-04-25
- **策略 ID**: `gold_envelope`
- **评级汇总**: Green=1 | Yellow=0 | Red=0 | Total=1

- **最佳品种**: GLD (Sharpe=1.357)

### 各品种回测结果

| 品种 | 评级 | Sharpe | 交易次数 | 最大回撤 | 年化收益 | 总收益 |
|--------|-------|--------|----------|----------|----------|----------|
| GLD | GREEN | 1.357 | 93 | -0.22% | 0.27% | 1.35% |

### 最优参数 (最佳品种)

| 参数 | 最优值 |
|--------|--------|
| SMA Period | 20 |

*评估报告*: `eval_gold_envelope_trading_strategy_20260425_053109.json`
