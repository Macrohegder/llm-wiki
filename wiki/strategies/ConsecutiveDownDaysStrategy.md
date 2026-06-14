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
| 159397 | 🟡 3.523 | 1 | 13.00% | -2.73% |
| 511200 | 🟡 3.159 | 1 | 9.71% | -1.60% |
| 563360 | 🟡 2.001 | 10 | 115.42% | -17.63% |
| 588170 | 🟡 1.906 | 6 | 119.69% | -0.53% |
| BZ888 | 🟡 1.827 | 1 | 36.33% | -0.80% |

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
