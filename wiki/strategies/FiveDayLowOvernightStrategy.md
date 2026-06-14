---
tags:
  - strategy
  - cta-developer
logic-type: "mean_reversion"
timeframe: "daily"
direction: "long_only"
source: "QuantifiedStrategies"
status: "production"
markets-tested: ['etf', 'cn_futures']
created: "2026-06-14"
---

# FiveDayLowOvernight

> 类型: #mean_reversion | 周期: daily | 方向: long_only | 来源: QuantifiedStrategies

---

## 代码实现
- **cta_developer**: `cta/strategies/five_day_low_overnight_strategy.py`
- **类名**: `FiveDayLowOvernightStrategy`

- **核心指标**: RSI

- **原文链接**: https://quantifiedstrategies.substack.com/p/the-5-day-low-overnight-trading-strategy

## 一句话摘要
5-Day Low Overnight Mean Reversion Strategy (QuantifiedStrategies) — 自包含版

## 批量挖掘结果

### CN期货

| 品种 | Sharpe | 交易数 | 年化收益% | 最大回撤% |
|------|--------|--------|-----------|-----------|
| BZ888 | 🟡 3.337 | 20 | 76.39% | -3.16% |
| AD888 | 🟡 2.724 | 13 | 122.32% | -0.60% |
| 159206 | 🟡 2.281 | 16 | 275.59% | -46.74% |
| 159363 | 🟡 2.063 | 23 | 402.69% | -75.47% |
| OP888 | 🟡 2.063 | 21 | 62.86% | -14.16% |

### ETF

| 品种 | Sharpe | 交易数 | 年化收益% | 最大回撤% |
|------|--------|--------|-----------|-----------|
| GLD | 🟡 0.775 | 148 | 85.79% | -146.65% |
| SPY | 🟡 0.716 | 194 | 86.14% | -124.91% |
| IWM | 🟡 0.698 | 230 | 67.63% | -144.21% |
| QQQ | 🔴 0.489 | 168 | 87.78% | -217.47% |
| TLT | 🔴 -0.425 | 166 | -26.43% | -220.07% |

## 相关策略


## 相关概念

- [[mean-reversion]]
- [[RSI-(Relative-Strength-Index)]]
