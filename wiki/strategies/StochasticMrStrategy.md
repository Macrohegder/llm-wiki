---
tags:
  - strategy
  - cta-developer
logic-type: "mean_reversion"
timeframe: "daily"
direction: "long_only"
source: "QuantifiedStrategies"
status: "production"
markets-tested: ['cn_futures']
created: "2026-06-14"
---

# StochasticMr

> 类型: #mean_reversion | 周期: daily | 方向: long_only | 来源: QuantifiedStrategies

---

## 代码实现
- **cta_developer**: `cta/strategies/stochastic_mr_strategy.py`
- **类名**: `StochasticMrStrategy`

- **核心指标**: RSI, ATR, Stochastic

## 一句话摘要
Stochastic Mean-Reversion Strategy (随机均值回归策略) (自包含版)

## 批量挖掘结果

### CN期货

| 品种 | Sharpe | 交易数 | 年化收益% | 最大回撤% |
|------|--------|--------|-----------|-----------|
| 551030 | 🟡 5.216 | 1 | 16.43% | -0.55% |
| 159400 | 🟡 4.431 | 1 | 20.82% | -2.22% |
| 551550 | 🟡 4.186 | 3 | 14.17% | -1.89% |
| 511360 | 🟡 4.053 | 4 | 7.13% | -1.74% |
| 159397 | 🟡 3.548 | 3 | 17.66% | -4.40% |

## 相关策略


## 相关概念

- [[mean-reversion]]
- [[RSI-(Relative-Strength-Index)]]
- [[stochastic-rsi]]
