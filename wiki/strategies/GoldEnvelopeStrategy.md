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

# GoldEnvelope

> 类型: #mean_reversion | 周期: daily | 方向: long_only | 来源: QuantifiedStrategies

---

## 代码实现
- **cta_developer**: `cta/strategies/gold_envelope_strategy.py`
- **类名**: `GoldEnvelopeStrategy`

- **核心指标**: SMA

## 一句话摘要
Gold Envelope Trading Strategy (Quantified Strategies) (自包含版)

## 批量挖掘结果

### CN期货

| 品种 | Sharpe | 交易数 | 年化收益% | 最大回撤% |
|------|--------|--------|-----------|-----------|
| IC888 | 🟡 0.506 | 52 | 971.85% | -3157.25% |
| IF888 | 🔴 0.337 | 74 | 812.66% | -3324.96% |
| AU888 | 🔴 0.316 | 51 | 207.32% | -1439.64% |
| IH888 | 🔴 0.133 | 78 | 162.05% | -2701.36% |

### ETF

| 品种 | Sharpe | 交易数 | 年化收益% | 最大回撤% |
|------|--------|--------|-----------|-----------|
| GLD | 🟡 0.708 | 58 | 143.52% | -420.84% |
| IWM | 🔴 0.438 | 98 | 93.91% | -344.10% |
| SPY | 🔴 0.374 | 64 | 75.34% | -292.52% |
| QQQ | 🔴 0.272 | 54 | 89.99% | -413.45% |
| TLT | 🔴 -0.754 | 51 | -87.51% | -556.58% |

## 相关策略


## 相关概念

- [[mean-reversion]]
