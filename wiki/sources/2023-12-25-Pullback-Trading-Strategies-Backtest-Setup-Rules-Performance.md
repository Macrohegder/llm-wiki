---
id: 2023-12-25-Pullback-Trading-Strategies-Backtest-Setup-Rules-Performance
title: "Pullback Trading Strategies (Backtest, Setup, Rules, Performance)"
source: "quantifiedstrategies."
url: https://quantifiedstrategies.substack.com/p/pullback-trading-strategies-backtest
date: 2023-12-25
tags: #strategy #trading
rating: green
---

# Pullback Trading Strategies (Backtest, Setup, Rules, Performance)

## 一句话摘要

Pullback Trading Strategies (Backtest, Setup, Rules, Performance) QuantifiedStrategies.com Dec 25, 2023 1 1 Share A pullback trading strategy is a trading strategy that involves buying a stock after i

## 关键要点

- 待补充

## 相关实体
- 

## 相关概念
- 

## 复现状态

- **复现完成**: 2026-04-27 09:04
- **策略 ID**: `pullback_trading_strategy`
- **评级汇总**:  Green=0 |  Yellow=1 |  Red=0 | Total=1

- **最佳品种**: SPY (Sharpe=0.895)

### 各品种回测结果

| 品种 | 评级 | Sharpe | 交易次数 | 最大回撤 | 年化收益 | 总收益 |
|--------|-------|--------|----------|----------|----------|----------|
| SPY |  Yellow | 0.895 | 96 | -2.62% | 1.68% | 12.52% |

### 最优参数 (最佳品种)

| 参数 | 最优值 |
|--------|--------|
| fixed_size | 1 |
| price_add_rate | 0.0 |
| rsi_entry_threshold | 45 |
| rsi_exit_threshold | 65 |
| rsi_period | 5 |
| sma_long_period | 200 |
| sma_short_period | 20 |

*评估报告*: `eval_pullback_trading_strategy_20260427_090458.json`

## 评价

| 指标 | 评分 | 备注 |
|--------|-------|-------|
| 数据质量 | ⭐⭐⭐☆☆ | 待评估 |
| 可操作性 | ⭐⭐☆☆☆ | 待评估 |
| 新题性 | ⭐⭐☆☆☆ | 待评估 |
| 风险透明度 | ⭐⭐☆☆☆ | 待评估 |

**总体**: 🟢 **Green** — 自动录入，内容待审阅。
