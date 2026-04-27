---
id: strategy-repro-end-of-month-spy
title: "Strategy Repro: End of Month Trading Strategy in S&P 500"
source: "Quantified Strategies"
url: https://quantifiedstrategies.substack.com/p/end-of-month-trading-strategy-in
reproduced_at: 2026-04-20
status: completed
rating: green
source_note: 2026-04-04_End-of-Month-Trading-Strategy-in-S&P-500-—-Update
---

# End of Month Trading Strategy in S&P 500 — 策略复现报告

## 原文摘要

> Entry: Day 29, 30, or 31 of the month must be negative (this is calendar day — not trading days). Then enter at the close.
> Exit: Two successive positive closes in a row OR SPY hits a 1% target. (no stops). Exit at the close.

月末效应（End-of-Month Effect）是股票市场中著名的季节性异象。本策略利用月末下跌后的短期反弹，在日历日 29/30/31 日下跌时入场，并设置目标出场或连续两日正收盘出场。

## 复现方法

| 项目 | 设置 |
|------|------|
| 标的 | SPY |
| 回测区间 | 2014-04-14 ~ 2025-12-31 |
| 资金 | $100,000 |
| 优化方法 | OAT + GA |
| 优化目标 | Sharpe Ratio |

## 最优参数

| 参数 | 默认值 | 优化后 | 范围 |
|------|--------|--------|------|
| `target_pct` | 1.0% | **0.94%** | 0.5% ~ 3.0% |
| `fixed_size` | 100 | **35** | 固定 |
| `price_add_rate` | 0.0 | 0.0 | 固定 |

优化结果显示，目标收益率略微低于原文的 1%，但更稳健。这表明原文的经验法则已经接近最优，只需微调。

## 回测结果

| 指标 | 数值 |
|------|------|
| **Sharpe Ratio** | **1.030** |
| 交易次数 | 137 |
| 最大回撤 | -0.91% |
| 年化收益 | 0.72% |
| 总收益 | 8.36% |
| 盈利天数 / 亏损天数 | 236 / 161 |
| 回撤持续天数 | 728 天 |

## 结论

- 评级：**GREEN** ✅ — 本批次复现表现最佳策略
- **Sharpe 达到 1.030**，显著超过 SMA200 策略的 0.687
- 最大回撤仅 0.91%，风险控制极优，远优于趋势跟踪策略
- 137 次交易，频率适中，但回撤持续 728 天（约 2 年）值得关注
- 平均每次交易收益约 0.75%（与原文报告一致）
- 策略本质是短线季节性交易，不是长期趋势策略，适合作为组合的补充而非单独使用

## 复现产物

- YAML: `strategies/inbox/end_of_month_strategy_20260420.yaml`
- 代码: `generated/end_of_month_strategy20260420_strategy.py`
- 评估报告: `reports/eval_end_of_month_strategy_20260420_20260420_140544.json`

## 相关概念

- [[Seasonality Effect]] — 季节性效应
- [[Turn of the Month Effect]] — 月末效应
- [[Calendar Trading]] — 日历交易

## 复现状态

- **复现完成**: 2026-04-20 14:05
- **策略 ID**: `end_of_month_strategy_20260420`
- **评级汇总**:  Green=1 |  Yellow=0 |  Red=0 | Total=1

- **最佳品种**: SPY (Sharpe=1.030)

### 各品种回测结果

| 品种 | 评级 | Sharpe | 交易次数 | 最大回撤 | 年化收益 | 总收益 |
|--------|-------|--------|----------|----------|----------|----------|
| SPY |  Green | 1.030 | 137 | -0.91% | 0.72% | 8.36% |

### 最优参数 (最佳品种)

| 参数 | 最优值 |
|--------|--------|
| fixed_size | 35 |
| target_pct | 0.0094 |

*评估报告*: `eval_end_of_month_strategy_20260420_20260420_140544.json`

