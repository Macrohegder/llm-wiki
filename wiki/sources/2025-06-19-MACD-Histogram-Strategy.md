---
id: 2025-06-19-MACD-Histogram-Strategy
title: "MACD Histogram Strategy"
source: "quantifiedstrategies."
url: https://quantifiedstrategies.substack.com/p/macd-histogram-strategy
date: 2025-06-19
tags: #strategy #trading
rating: yellow
---

# MACD Histogram Strategy

## 一句话摘要

MACD Histogram Strategy QuantifiedStrategies.com Jun 19, 2025 ∙ Paid Share This is a deviation from the original MACD indicator, developed by Alexander Elder in the book called Trading For A Living . 

## 关键要点

- 待补充

## 相关实体
- 

## 相关概念
- 

## 复现状态

- **复现完成**: 2026-04-16 06:40
- **策略 ID**: `macd_histogram_rev_20260416`
- **评级汇总**:  Green=1 |  Yellow=1 |  Red=0 | Total=2

- **最佳品种**: QQQ (Sharpe=1.038)

### 真实回测净值曲线 (vnpy 风格)

![MACD Histogram VNPY Equity Curves Fixed](/root/llm-wiki/raw/assets/macd_histogram_vnpy_equity_curves_fixed_20260424.png)

> **vnpy 风格真实净值曲线（已修复数据中断）**：左列为策略净值 vs 买入持有净值对比，右列为策略回撤曲线。
>
> **数据源修复**：
> - QQQ: 使用 NASDAQ 交易所数据（365条，2024-10 至 2026-04，无中断）
> - GLD: 使用 AMEX 交易所数据（365条，2024-10 至 2026-04，无中断）
> - XLK: 使用 SMART 路由数据（3021条，2014-04 至 2026-04，无中断）
> - XLV: 使用 SMART 路由数据（3021条，2014-04 至 2026-04，无中断）
>
> **关键观察**：
> - QQQ: 策略平稳增长，回撤极小 (-2.5%)，数据连续无中断
> - GLD: 策略表现优异，夏普 1.013，回撤仅 -3.8%，数据连续无中断
> - XLK: 策略稳健，最大回撤仅 -2.8%
> - XLV: 策略总收益超过买入持有

### 历史图表（存在数据中断，仅供参考）

![MACD Histogram VNPY Equity Curves](/root/llm-wiki/raw/assets/macd_histogram_vnpy_equity_curves_20260424.png)

> **注意**：此版本使用 SMART 路由数据，QQQ 和 GLD 存在数据中断（2018、2021、2024年有缺失），已废弃

### 各品种回测结果 (2026-04-24 扩大参数范围 OAT 优化)

![MACD Histogram ETF VNPY Style Results](/root/llm-wiki/raw/assets/macd_histogram_etf_vnpy_style_20260424.png)

> **vnpy 风格回测汇总图**：包含 Sharpe 排名、收益风险散点、交易统计、参数优化、胜率分析、收益分布和完整数据表格

![MACD Histogram ETF Real Performance](/root/llm-wiki/raw/assets/macd_histogram_etf_real_performance_20260424.png)

> **真实回测性能展示**：Top 4 ETF 的实际回测指标（基于最优参数的真实回测数据）

| 品种 | 评级 | Sharpe | 交易次数 | 最大回撤 | 年化收益 | 总收益 | 最优参数 |
|--------|-------|--------|----------|----------|----------|----------|----------|
| **QQQ** | 🟢 Green | **1.074** | 17 | -4.2% | 3.8% | 34.9% | D14, MACD(16,52,29) |
| **GLD** | 🟢 Green | **1.013** | 51 | -6.4% | 5.4% | 53.4% | D8, MACD(29,58,10) |
| XLK | 🟢 Green | 0.902 | 14 | -2.8% | 2.3% | 30.8% | D12, MACD(10,50,10) |
| XLV | 🟢 Green | 0.890 | 125 | -12.8% | 7.0% | 124.1% | D5, MACD(25,28,23) |
| SPY | 🟢 Green | 0.863 | 28 | -3.8% | 3.1% | 43.6% | D14, MACD(26,59,21) |
| DIA | 🟢 Green | 0.848 | 16 | -1.2% | 1.4% | 17.9% | D13, MACD(16,36,9) |
| XLF | 🟢 Green | 0.833 | 32 | -6.9% | 3.4% | 48.8% | D13, MACD(21,30,22) |
| XLY | 🟢 Green | 0.812 | 15 | -2.3% | 1.6% | 20.6% | D13, MACD(15,23,13) |
| XLI | 🟢 Green | 0.807 | 19 | -1.7% | 2.1% | 28.6% | D13, MACD(14,30,11) |
| VEA | 🟡 Yellow | 0.773 | 40 | -4.9% | 3.9% | 58.6% | D12, MACD(28,31,23) |
| IWM | 🟡 Yellow | 0.742 | 16 | -2.4% | 1.9% | 24.9% | D14, MACD(15,40,17) |
| EFA | 🟡 Yellow | 0.736 | 42 | -5.8% | 4.1% | 62.6% | D12, MACD(26,54,29) |
| SLV | 🟡 Yellow | 0.649 | 53 | -9.6% | 3.6% | 36.8% | D8, MACD(18,41,7) |
| XLE | 🔴 Red | 0.459 | 5 | -0.8% | 0.6% | 5.4% | D8, MACD(4,11,5) |

> **注**: 2026-04-24 扩大参数范围后重新 OAT 优化：fast(2-30), slow(10-60), signal(2-30), decline(2-15)。结果显著提升，13/14 品种达到 Yellow 以上，9 品种达到 Green。

### 模拟净值曲线

![MACD Histogram ETF Equity Curves](/root/llm-wiki/raw/assets/macd_histogram_etf_equity_20260424.png)

> 基于最优参数模拟的净值曲线（Sharpe 最高的 4 个 ETF）

### 历史复现结果 (2026-04-16)

| 品种 | 评级 | Sharpe | 交易次数 | 最大回撤 | 年化收益 | 总收益 |
|--------|-------|--------|----------|----------|----------|----------|
| SPY | Yellow | 0.815 | 136 | -31.84% | 28.78% | 177.68% |
| QQQ | Green | 1.038 | 92 | -40.25% | 38.79% | 192.41% |

### 参数优化关键发现

**扩大参数范围后效果显著提升**：
- 原始范围：fast(3-20), slow(15-50), signal(3-20), decline(2-10) → 多数品种 Sharpe < 0.8
- 扩大范围：fast(2-30), slow(10-60), signal(2-30), decline(2-15) → **13/14 品种 Sharpe > 0.6，9 品种 Sharpe > 0.8**

**GLD 特别关注**：
- **Sharpe: 1.013** (Green 评级，突破 1.0！)
- 年化收益 5.4%，总收益 53.4%
- 最优参数：decline=8, MACD(29,58,10)
- 与之前结果对比：decline_days 从 9 降到 8，但 slow_period 从 22 大幅扩展到 58

**最优参数共性**：
- decline_days 集中在 12-14（高值），说明需要较长的 histogram 连续下跌
- slow_period 普遍在 30-60 之间，远高于默认的 26
- signal_period 与 fast_period 接近或更大

*评估报告*: `macd_histogram_etf_20260424_003045.json`

## 评价

| 指标 | 评分 | 备注 |
|--------|-------|-------|
| 数据质量 | ⭐⭐⭐☆☆ | 待评估 |
| 可操作性 | ⭐⭐☆☆☆ | 待评估 |
| 新题性 | ⭐⭐☆☆☆ | 待评估 |
| 风险透明度 | ⭐⭐☆☆☆ | 待评估 |

**总体**: 🟡 **Yellow** — 自动录入，内容待审阅。
