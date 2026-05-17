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
| IM888 | 🟡 1.496 | 14 | 1500.48% | -299.38% |
| TL888 | 🟡 1.233 | 8 | 174.96% | -88.80% |
| T888 | 🟡 1.118 | 1 | 266.63% | -213.39% |
| TF888 | 🟡 0.999 | 1 | 161.37% | -173.15% |
| AU888 | 🟡 0.778 | 1 | 892.30% | -1710.20% |

### Crypto

| 品种 | Sharpe | 交易数 | 年化收益% | 最大回撤% |
|------|--------|--------|-----------|-----------|
| XAU | 🟡 1.268 | 1 | 387.05% | -300.20% |
| BTC | 🔴 0.476 | 1 | 1526.14% | -3879.31% |
| SOL | 🔴 0.414 | 44 | 5262.30% | -6886.45% |
| ETH | 🔴 0.262 | 44 | 1200.15% | -5181.59% |
| QQQ | 🔴 0.000 | 0 | 0.00% | 0.00% |

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
