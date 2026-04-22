---
id: 2026-04-16-Bollinger-Band-Breakout-Strategy
title: "Bollinger Band Breakout Strategy"
source: "quantifiedstrategies."
url: https://quantifiedstrategies.substack.com/p/bollinger-band-breakout-strategy
date: 2026-04-16
tags: #strategy #trading
rating: yellow
---

# Bollinger Band Breakout Strategy

## 一句话摘要

Bollinger Band Breakout Strategy QuantifiedStrategies.com Apr 15, 2026 ∙ Paid 1 Share The Bollinger Bands breakout strategy aims to capitalize on price movements that occur when the bands are breached

## 关键要点

- 待补充

## 相关实体
- 

## 相关概念
- 

## 复现状态

- **复现完成**: 2026-04-22 09:04
- **策略 ID**: `bollinger_band_breakout`
- **评级汇总**:  Green=0 |  Yellow=1 |  Red=5 | Total=6

- **最佳品种**: SPY (Sharpe=0.905)

### 各品种回测结果

| 品种 | 评级 | Sharpe | 交易次数 | 最大回撤 | 年化收益 | 总收益 |
|--------|-------|--------|----------|----------|----------|----------|
| SPY |  Yellow | 0.905 | 78 | -11.13% | 6.88% | 42.25% |
| QQQ |  Red | 0.851 | 14 | -12.21% | 8.91% | 44.20% |
| BTCUSDT_SWAP_OKX.GLOBAL |  Red | 0.539 | 405 | -61.36% | 16.07% | 99.68% |
| ETHUSDT_SWAP_OKX.GLOBAL |  Red | 0.740 | 33 | -22.29% | 9.88% | 61.25% |
| SOLUSDT_SWAP_OKX.GLOBAL |  Red | 0.666 | 22 | -24.64% | 8.59% | 44.19% |
| DOGEUSDT_SWAP_OKX.GLOBAL |  Red | 0.475 | 119 | -48.19% | 15.27% | 86.71% |

### 最优参数 (最佳品种)

| 参数 | 最优值 |
|--------|--------|
| fixed_size | 15 |
| lookback | 18 |
| std_dev | 0.7 |
| use_long_only | 1.1800000000000002 |

*评估报告*: `eval_bollinger_band_breakout_20260422_090413.json`

## 评价

| 指标 | 评分 | 备注 |
|--------|-------|-------|
| 数据质量 | ⭐⭐⭐☆☆ | 待评估 |
| 可操作性 | ⭐⭐☆☆☆ | 待评估 |
| 新题性 | ⭐⭐☆☆☆ | 待评估 |
| 风险透明度 | ⭐⭐☆☆☆ | 待评估 |

**总体**: 🟡 **Yellow** — 自动录入，内容待审阅。
