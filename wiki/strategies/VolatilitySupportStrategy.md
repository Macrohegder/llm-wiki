---
tags:
  - strategy
  - cta-developer
logic-type: "mean_reversion"
timeframe: "daily"
direction: "long_only"
source: "QuantifiedStrategies"
status: "production"
markets-tested: ['cn_futures', 'etf', 'crypto']
created: "2026-06-14"
---

# VolatilitySupport

> 类型: #mean_reversion | 周期: daily | 方向: long_only | 来源: QuantifiedStrategies

---

## 代码实现
- **cta_developer**: `cta/strategies/volatility_support_strategy.py`
- **类名**: `VolatilitySupportStrategy`

## 一句话摘要
波动率支撑策略 (自包含版)

## 批量挖掘结果

### CN期货

| 品种 | Sharpe | 交易数 | 年化收益% | 最大回撤% |
|------|--------|--------|-----------|-----------|
| 159400 | 🟡 3.898 | 9 | 24.64% | -3.27% |
| 551030 | 🟡 3.221 | 9 | 18.29% | -3.85% |
| 551550 | 🟡 2.868 | 8 | 15.90% | -3.18% |
| 159650 | 🟢 2.431 | 51 | 13.56% | -4.50% |
| 159363 | 🟢 2.353 | 55 | 1136.25% | -186.64% |

### Crypto

| 品种 | Sharpe | 交易数 | 年化收益% | 最大回撤% |
|------|--------|--------|-----------|-----------|
| BTC | 🔴 0.359 | 283 | 1205.42% | -4943.22% |
| SOL | 🔴 0.131 | 459 | 1240.40% | -7745.71% |
| ETH | 🔴 -0.091 | 463 | -417.56% | -8251.57% |

### ETF

| 品种 | Sharpe | 交易数 | 年化收益% | 最大回撤% |
|------|--------|--------|-----------|-----------|
| GLD | 🟢 1.478 | 143 | 407.45% | -420.55% |
| QQQ | 🟢 0.970 | 107 | 418.45% | -447.61% |
| SPY | 🟢 0.963 | 141 | 213.02% | -337.70% |
| IWM | 🟢 0.941 | 191 | 226.26% | -446.83% |
| TLT | 🔴 -0.054 | 123 | -7.36% | -443.94% |

## 相关策略


## 相关概念

- [[mean-reversion]]
