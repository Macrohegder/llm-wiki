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
created: "2026-06-14"
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
| BZ888 | 🟡 2.124 | 20 | 144.69% | -18.45% |
| PL888 | 🟡 2.044 | 14 | 68.61% | -9.80% |
| 513920 | 🟢 1.675 | 60 | 142.06% | -63.44% |
| 159363 | 🟡 1.635 | 23 | 434.71% | -102.67% |
| 159397 | 🟡 1.574 | 10 | 7.75% | -1.66% |

### Crypto

| 品种 | Sharpe | 交易数 | 年化收益% | 最大回撤% |
|------|--------|--------|-----------|-----------|
| BTC | 🟡 0.732 | 182 | 1447.97% | -2779.74% |
| XAU | 🟡 0.664 | 24 | 81.31% | -101.61% |
| SOL | 🔴 0.300 | 137 | 4282.03% | -8153.33% |
| ETH | 🔴 0.114 | 167 | 761.86% | -8023.97% |
| QQQ | 🔴 0.000 | 0 | 0.00% | 0.00% |

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
