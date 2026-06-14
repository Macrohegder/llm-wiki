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

# IbsMeanReversion

> 类型: #mean_reversion | 周期: daily | 方向: long_only | 来源: QuantifiedStrategies

---

## 代码实现
- **cta_developer**: `cta/strategies/ibs_mean_reversion_strategy.py`
- **类名**: `IbsMeanReversionStrategy`

- **核心指标**: RSI, IBS

## 一句话摘要
IBS均值回归策略 (IBS Mean Reversion Strategy)

## 批量挖掘结果

### CN期货

| 品种 | Sharpe | 交易数 | 年化收益% | 最大回撤% |
|------|--------|--------|-----------|-----------|
| 159397 | 🟡 3.628 | 1 | 11.72% | -1.59% |
| 511360 | 🟡 3.522 | 25 | 7.74% | -2.68% |
| 159650 | 🟡 3.243 | 1 | 17.77% | -4.42% |
| 511200 | 🟡 3.058 | 1 | 13.47% | -1.92% |
| BZ888 | 🟡 1.875 | 2 | 110.29% | 0.00% |

### ETF

| 品种 | Sharpe | 交易数 | 年化收益% | 最大回撤% |
|------|--------|--------|-----------|-----------|
| SPY | 🟡 0.618 | 90 | 80.38% | -137.26% |
| IWM | 🔴 0.376 | 76 | 39.83% | -144.45% |
| QQQ | 🔴 0.217 | 66 | 47.91% | -328.51% |
| TLT | 🔴 0.181 | 61 | 17.41% | -143.88% |
| GLD | 🔴 0.051 | 52 | 9.25% | -437.00% |

## 相关策略


## 相关概念

- [[mean-reversion]]
- [[RSI-(Relative-Strength-Index)]]
- [[IBS-(Internal-Bar-Strength)]]
