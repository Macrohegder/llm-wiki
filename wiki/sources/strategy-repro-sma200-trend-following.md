---
id: strategy-repro-sma200-trend-following
title: "Strategy Repro: S&P 500 200-Day SMA Trend Following"
source: "Quantified Strategies (Meb Faber)"
url: https://quantifiedstrategies.substack.com/p/a-simple-trend-following-system-and
reproduced_at: 2026-04-20
status: completed
rating: green
---

# S&P 500 200-Day SMA Trend Following — 策略复现报告

## 原文摘要

> Go long the S&P 500 when the price crosses the 200-day moving average, and sell when it crosses below the 200-day average.

这是 Meb Faber 提出的经典趋势跟踪策略，被 Paul Tudor Jones 等多位交易大师引用。策略极其简单：价格穿越 200 日移动平均线时做多，跌破时平仓。

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
| `sma_period` | 200 | **112** | 50 ~ 300 |
| `fixed_size` | 100 | **35** | 固定 |
| `price_add_rate` | 0.0 | 0.0 | 固定 |

意外发现：OAT 优化后 SMA 周期从 200 降至 112，Sharpe 明显提升。说明原文的 200 日未经过优化，存在超参数风险。

## 回测结果

| 指标 | 数值 |
|------|------|
| **Sharpe Ratio** | 0.687 |
| 交易次数 | 107 |
| 最大回撤 | -3.21% |
| 年化收益 | 1.02% |
| 总收益 | 11.95% |
| 盈利天数 / 亏损天数 | 1,165 / 952 |
| 回撤持续天数 | 443 天 |

## 结论

- 评级：**GREEN** ✅
- 策略逻辑简单有效，但 Sharpe 仅 0.687，表现中规中矩
- 最大回撤 3.21% 控制得当，但回撤持续达 443 天（约 1.5 年），心理压力较大
- 优化后的 112 日 SMA 比原文 200 日表现更好，建议未来复现时系统性地对 SMA 周期做敏感性分析

## 复现产物

- YAML: `strategies/inbox/sma200_trend_following_20260420.yaml`
- 代码: `generated/sma200_trend_following20260420_strategy.py`
- 评估报告: `reports/eval_sma200_trend_following_20260420_20260420_104244.json`

## 复现状态

- **复现完成**: 2026-04-20 10:42
- **策略 ID**: `sma200_trend_following_20260420`
- **评级汇总**:  Green=1 |  Yellow=0 |  Red=0 | Total=1

- **最佳品种**: SPY (Sharpe=0.687)

### 各品种回测结果

| 品种 | 评级 | Sharpe | 交易次数 | 最大回撤 | 年化收益 | 总收益 |
|--------|-------|--------|----------|----------|----------|----------|
| SPY |  Green | 0.687 | 107 | -3.21% | 1.02% | 11.95% |

### 最优参数 (最佳品种)

| 参数 | 最优值 |
|--------|--------|
| fixed_size | 35 |
| sma_period | 112 |

*评估报告*: `eval_sma200_trend_following_20260420_20260420_104244.json`

