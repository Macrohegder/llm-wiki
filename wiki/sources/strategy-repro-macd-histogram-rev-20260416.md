---
id: strategy-repro-macd-histogram-rev-20260416
title: "Strategy Repro: MACD Histogram Mean Reversion"
source: "Quantified Strategies"
url: https://quantifiedstrategies.substack.com/p/macd-histogram-strategy
reproduced_at: 2026-04-16
status: completed
rating: green
---

# MACD Histogram Mean Reversion — 策略复现报告

## 原文摘要

> 

## 复现方法

| 项目 | 设置 |
|------|------|
| 标的 | QQQ |
| 回测区间 | 2019-01-01 ~ 2025-12-31 |
| 资金 | $100,000 |
| 优化方法 | OAT + GA |
| 优化目标 | Sharpe Ratio |

## 最优参数

| 参数 | 最优值 |
|------|--------|
| `decline_days` | 3 |
| `signal_period` | 12 |
| `slow_period` | 34 |

## 回测结果

| 指标 | 数值 |
|------|------|
| **Sharpe Ratio** | 1.038 |
| 交易次数 | 92 |
| 最大回撤 | -40.25% |
| 年化收益 | 38.79% |
| 总收益 | 192.41% |

## 2026-04-24 扩展测试结论 (扩大参数范围)

- **新增 Green 品种**: QQQ (Sharpe=1.074), GLD (Sharpe=1.013), XLK, XLV, SPY, DIA, XLF, XLY, XLI
- **扩大参数范围效果显著**: fast(2-30), slow(10-60), signal(2-30), decline(2-15)
- **13/14 品种达到 Yellow 以上，9 品种达到 Green**
- **GLD 突破 1.0 Sharpe**: 年化 5.4%，回撤 -6.4%，参数 D8, MACD(29,58,10)
- **参数共性**: decline_days 集中在 12-14，slow_period 普遍 30-60

## 历史复现结论 (2026-04-16)

- 评级：**GREEN** ✅ (QQQ Sharpe=1.038)
- 最佳品种：**QQQ** (Sharpe=1.038)
- 策略复现完成，参数经 OAT 优化后表现稳健

## 复现产物

- YAML: `strategies/inbox/macd_histogram_rev_20260416.yaml`
- 代码: `generated/macd_histogram_rev_20260416_strategy.py`
- 评估报告: `reports/eval_macd_histogram_rev_20260416_20260416_064027.json`
- **扩展测试脚本**: `ib-data/scripts/macd_histogram_mr.py`
- **扩展测试报告 (2026-04-24)**: `ib-data/reports/macd_histogram_etf_20260424_003045.json`
- **历史报告 (2026-04-23)**: `ib-data/reports/macd_histogram_etf_20260423_231835.json`
- **vnpy 风格净值曲线（已修复）**: `llm-wiki/raw/assets/macd_histogram_vnpy_equity_curves_fixed_20260424.png`
- **vnpy 风格净值曲线（旧版，有中断）**: `llm-wiki/raw/assets/macd_histogram_vnpy_equity_curves_20260424.png`
- **vnpy 风格汇总图**: `llm-wiki/raw/assets/macd_histogram_etf_vnpy_style_20260424.png`
- **真实性能图表**: `llm-wiki/raw/assets/macd_histogram_etf_real_performance_20260424.png`

## 复现状态

- **复现完成**: 2026-04-16
- **策略 ID**: `macd_histogram_rev_20260416`
- **评级汇总**: Green=1 | Yellow=1 | Red=0 | Total=2

- **最佳品种**: QQQ (Sharpe=1.038)

### 各品种回测结果

| 品种 | 评级 | Sharpe | 交易次数 | 最大回撤 | 年化收益 | 总收益 |
|--------|-------|--------|----------|----------|----------|----------|
| SPY | Yellow | 0.815 | 136 | -31.84% | 28.78% | 177.68% |
| QQQ | Green | 1.038 | 92 | -40.25% | 38.79% | 192.41% |

### 最优参数 (最佳品种)

| 参数 | 最优值 |
|--------|--------|
| `decline_days` | 3 |
| `signal_period` | 12 |
| `slow_period` | 34 |

*评估报告*: `eval_macd_histogram_rev_20260416_20260416_064027.json`
