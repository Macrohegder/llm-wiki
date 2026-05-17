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
| TF888 | 🟢 0.968 | 144 | 67.02% | -66.25% |
| AU888 | 🟢 0.829 | 123 | 138.37% | -205.70% |
| T888 | 🟢 0.810 | 132 | 63.68% | -128.93% |
| IC888 | 🟡 0.539 | 248 | 460.56% | -879.35% |
| IF888 | 🔴 0.357 | 180 | 541.62% | -1726.76% |

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
