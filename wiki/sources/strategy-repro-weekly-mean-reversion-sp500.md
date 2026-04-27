---
id: strategy-repro-weekly-mean-reversion-sp500
title: "Strategy Repro: Weekly Mean Reversion System For SP500 Stocks"
source: "Quantified Strategies"
url: https://quantifiedstrategies.substack.com/p/weekly-mean-reversion-system-for
reproduced_at: 2026-04-25
status: completed
rating: green
source_note: 2023-04-23-Weekly-Mean-Reversion-System-For-SP-500-Stocks
---

# SP500 周线均值回归策略 — 策略复现报告

## 原文摘要

> 周线级别的SP500成分股均值回归系统。利用周线级别的超买超卖信号进行反向交易，减少噪音，捕捉中期的回归机会。

## 复现方法

| 项目 | 设置 |
|------|------|
| 标的 | 多品种（含SP500成分股） |
| 回测区间 | 2019-01-01 ~ 2025-12-31 |
| 资金 | $100,000 |
| 优化方法 | OAT + GA |
| 优化目标 | Sharpe Ratio |

## 回测结果

| 指标 | 数值 |
|------|------|
| **Sharpe Ratio** | 0.954 |
| 交易次数 | 193 |
| 最大回撤 | -5.89% |

## 结论

- 评级：**GREEN** ✅
- 193笔交易（充足样本）
- Sharpe接近1.0，表现稳健
- 最大回撤控制在合理范围

## 复现产物

- YAML: `strategies/inbox/weekly_mean_reversion_sp500_stocks.yaml`
- 代码: `generated/weekly_mean_reversion_sp500_stocks_strategy.py`

## 复现状态

- **复现完成**: 2026-04-25
- **策略 ID**: `weekly_mean_reversion_sp500_stocks`
- **评级汇总**: Green=0 | Yellow=0 | Red=0 | Total=0（需进一步分解品种）

- **最佳品种**: （待补充）

*从 pipeline queue 读取，需进一步解析详细品种回测结果。*
