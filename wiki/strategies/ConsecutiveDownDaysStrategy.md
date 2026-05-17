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

# ConsecutiveDownDays

> 类型: #mean_reversion | 周期: daily | 方向: long_only | 来源: QuantifiedStrategies

---

## 代码实现
- **cta_developer**: `cta/strategies/consecutive_down_days_strategy.py`
- **类名**: `ConsecutiveDownDaysStrategy`

- **核心指标**: RSI

## 一句话摘要
连续下跌反转策略 (Consecutive Down Days Mean Reversion) — 自包含版

## 批量挖掘结果

### CN期货

| 品种 | Sharpe | 交易数 | 年化收益% | 最大回撤% |
|------|--------|--------|-----------|-----------|
| T888 | 🟢 0.987 | 78 | 173.46% | -150.50% |
| TF888 | 🟡 0.650 | 132 | 99.45% | -256.13% |
| IF888 | 🟡 0.624 | 66 | 1080.30% | -1814.53% |
| TL888 | 🟡 0.599 | 50 | 207.22% | -356.25% |
| AU888 | 🟡 0.596 | 131 | 448.57% | -1719.70% |

### ETF

| 品种 | Sharpe | 交易数 | 年化收益% | 最大回撤% |
|------|--------|--------|-----------|-----------|
| IWM | 🟢 1.507 | 86 | 193.61% | -135.82% |
| SPY | 🟢 1.191 | 188 | 103.73% | -93.53% |
| QQQ | 🟢 0.922 | 68 | 105.85% | -109.25% |
| GLD | 🟢 0.829 | 138 | 95.00% | -259.45% |
| TLT | 🔴 -0.142 | 58 | -9.93% | -174.63% |

## 相关策略


## 相关概念

- [[mean-reversion]]
- [[RSI-(Relative-Strength-Index)]]
