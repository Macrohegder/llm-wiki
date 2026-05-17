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

# WilliamsRMrSimple

> 类型: #mean_reversion | 周期: daily | 方向: long_only | 来源: QuantifiedStrategies

---

## 代码实现
- **cta_developer**: `cta/strategies/williams_r_mr_simple_strategy.py`
- **类名**: `WilliamsRMrSimpleStrategy`

- **核心指标**: RSI, SMA, Williams%R

## 一句话摘要
Williams %R Mean Reversion Simple Strategy (QuantifiedStrategies) (自包含版)

## 批量挖掘结果

### CN期货

| 品种 | Sharpe | 交易数 | 年化收益% | 最大回撤% |
|------|--------|--------|-----------|-----------|
| IC888 | 🟢 0.908 | 60 | 1051.49% | -2221.74% |
| AU888 | 🟢 0.807 | 91 | 564.45% | -1247.99% |
| IF888 | 🟡 0.780 | 130 | 2088.45% | -2015.97% |
| T888 | 🟡 0.770 | 84 | 142.17% | -329.00% |
| TF888 | 🟡 0.527 | 78 | 77.75% | -342.87% |

### Crypto

| 品种 | Sharpe | 交易数 | 年化收益% | 最大回撤% |
|------|--------|--------|-----------|-----------|
| BTC | 🟡 0.737 | 50 | 909.79% | -1618.46% |
| ETH | 🟡 0.727 | 50 | 2357.74% | -2541.76% |
| SOL | 🟡 0.560 | 52 | 5933.08% | -4579.25% |
| XAU | 🔴 -0.287 | 62 | -60.30% | -275.50% |

### ETF

| 品种 | Sharpe | 交易数 | 年化收益% | 最大回撤% |
|------|--------|--------|-----------|-----------|
| GLD | 🟢 1.023 | 75 | 255.29% | -397.62% |
| IWM | 🟡 0.709 | 64 | 112.06% | -373.97% |
| SPY | 🔴 0.486 | 68 | 75.02% | -304.65% |
| QQQ | 🔴 0.345 | 52 | 107.48% | -393.98% |
| TLT | 🔴 -0.265 | 50 | -21.38% | -273.68% |

## 相关策略


## 相关概念

- [[mean-reversion]]
- [[RSI-(Relative-Strength-Index)]]
