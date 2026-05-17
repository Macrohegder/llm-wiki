---
tags:
  - strategy
  - cta-developer
logic-type: "mean_reversion"
timeframe: "daily"
direction: "long_only"
source: "QuantifiedStrategies"
status: "production"
markets-tested: ['etf', 'crypto', 'cn_futures']
created: "2026-05-18"
---

# FiveDayLowRange

> 类型: #mean_reversion | 周期: daily | 方向: long_only | 来源: QuantifiedStrategies

---

## 代码实现
- **cta_developer**: `cta/strategies/five_day_low_range_strategy.py`
- **类名**: `FiveDayLowRangeStrategy`

- **核心指标**: RSI, IBS

- **原文链接**: https://quantifiedstrategies.substack.com/p/the-5-day-low-and-low-of-the-range

## 一句话摘要
5-Day Low of The Range Mean Reversion Strategy (QuantifiedStrategies) — 自包含版

## 批量挖掘结果

### CN期货

| 品种 | Sharpe | 交易数 | 年化收益% | 最大回撤% |
|------|--------|--------|-----------|-----------|
| T888 | 🟡 0.758 | 90 | 66.59% | -119.03% |
| TF888 | 🟡 0.726 | 94 | 52.61% | -72.29% |
| IC888 | 🔴 0.450 | 146 | 533.28% | -1465.60% |
| AU888 | 🔴 0.448 | 97 | 228.57% | -843.21% |
| IF888 | 🔴 0.379 | 128 | 538.54% | -1679.84% |

### ETF

| 品种 | Sharpe | 交易数 | 年化收益% | 最大回撤% |
|------|--------|--------|-----------|-----------|
| QQQ | 🟡 0.645 | 136 | 121.37% | -157.76% |
| SPY | 🟡 0.521 | 142 | 64.37% | -182.37% |
| TLT | 🔴 0.471 | 110 | 25.57% | -107.03% |
| GLD | 🔴 0.314 | 103 | 51.86% | -328.93% |
| IWM | 🔴 0.245 | 162 | 34.86% | -239.76% |

## 相关策略


## 相关概念

- [[mean-reversion]]
- [[RSI-(Relative-Strength-Index)]]
- [[IBS-(Internal-Bar-Strength)]]
