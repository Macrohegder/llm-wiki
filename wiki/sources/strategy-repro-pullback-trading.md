---
id: strategy-repro-pullback-trading
title: "Strategy Repro: Pullback Trading Strategies"
source: "Quantified Strategies"
url: https://quantifiedstrategies.substack.com/p/pullback-trading-strategies-backtest
reproduced_at: 2026-04-25
status: completed
rating: yellow
---

# Pullback Trading — 回调交易策略复现报告

## 原文摘要

> 回调交易(Pullback Trading)策略在趋势中寻找回调低点入场，使用SMA判断趋势方向，RSI识别回调结束点。策略测试了多种标的的回调交易规则设置。

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
| SMA Long Period | 118 |
| SMA Short Period | 11 |
| RSI Period | 3 |
| RSI Entry Threshold | 23 |
| RSI Exit Threshold | 34 |
| 固定仓位 | 1 |

## 回测结果

| 指标 | 数值 |
|------|------|
| **Sharpe Ratio** | 0.895 |
| 交易次数 | 96 |
| 最大回撤 | -2.62% |
| 年化收益 | - |
| 总收益 | - |

## 结论

- 评级：**YELLOW** 🟡
- 96笔交易（充足），Sharpe=0.895 接近Green阈值
- 最大回撤仅-2.62%，风险控制出色
- 可能需要调整品种范围或优化参数以提升Sharpe

## 复现产物

- YAML: `strategies/inbox/pullback_trading_strategy.yaml`
- 代码: `generated/pullback_trading_strategy_strategy.py`
- 评估报告: `reports/eval_pullback_trading_strategy_20260423_011217.json`

## 复现状态

- **复现完成**: 2026-04-25
- **策略 ID**: `pullback_trading`
- **评级汇总**: Green=0 | Yellow=1 | Red=0 | Total=1

- **最佳品种**: SPY (Sharpe=0.895)

### 各品种回测结果

| 品种 | 评级 | Sharpe | 交易次数 | 最大回撤 | 年化收益 | 总收益 |
|--------|-------|--------|----------|----------|----------|----------|
| SPY | YELLOW | 0.895 | 96 | -2.62% | - | - |

### 最优参数

| 参数 | 最优值 |
|--------|--------|
| SMA Long Period | 118 |
| SMA Short Period | 11 |
| RSI Period | 3 |
| RSI Entry Threshold | 23 |
| RSI Exit Threshold | 34 |

*评估报告*: `eval_pullback_trading_strategy_20260423_011217.json`
