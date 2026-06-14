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

# Rsi2

> 类型: #mean_reversion | 周期: daily | 方向: long_only | 来源: QuantifiedStrategies

---

## 代码实现
- **cta_developer**: `cta/strategies/rsi2_strategy.py`
- **类名**: `Rsi2Strategy`

- **核心指标**: RSI, RSI2, OU

## 一句话摘要
RSI-2 Mean Reversion Strategy (自包含版)

## 批量挖掘结果

### CN期货

| 品种 | Sharpe | 交易数 | 年化收益% | 最大回撤% |
|------|--------|--------|-----------|-----------|
| 588220 | 🟡 2.102 | 6 | 194.06% | -54.26% |
| IM888 | 🟡 1.496 | 14 | 1500.48% | -299.38% |
| 159566 | 🟡 1.446 | 4 | 302.33% | -106.51% |
| PR888 | 🟡 1.373 | 1 | 300.96% | -179.38% |
| 159530 | 🟡 1.334 | 4 | 51.55% | -14.32% |

### ETF

| 品种 | Sharpe | 交易数 | 年化收益% | 最大回撤% |
|------|--------|--------|-----------|-----------|
| GLD | 🟡 1.015 | 1 | 388.46% | -529.45% |
| QQQ | 🟡 0.855 | 1 | 402.15% | -602.27% |
| SPY | 🟡 0.750 | 1 | 194.38% | -354.00% |
| TLT | 🟡 0.530 | 14 | 19.41% | -96.76% |
| IWM | 🔴 0.407 | 1 | 118.07% | -459.26% |

## 相关策略


## 相关概念

- [[mean-reversion]]
- [[RSI-(Relative-Strength-Index)]]
- [[RSI-(Relative-Strength-Index)]]
