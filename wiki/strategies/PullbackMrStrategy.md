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

# PullbackMr

> 类型: #mean_reversion | 周期: daily | 方向: long_only | 来源: QuantifiedStrategies

---

## 代码实现
- **cta_developer**: `cta/strategies/pullback_mr_strategy.py`
- **类名**: `PullbackMrStrategy`

- **核心指标**: RSI, SMA

## 一句话摘要
Pullback Mean Reversion Strategy (QuantifiedStrategies) (自包含版)

## 批量挖掘结果

### CN期货

| 品种 | Sharpe | 交易数 | 年化收益% | 最大回撤% |
|------|--------|--------|-----------|-----------|
| IC888 | 🟢 1.017 | 68 | 1386.42% | -1260.06% |
| T888 | 🟢 0.984 | 56 | 185.56% | -328.06% |
| AU888 | 🟢 0.925 | 79 | 633.14% | -1296.38% |
| IF888 | 🟢 0.894 | 50 | 833.56% | -949.01% |
| IM888 | 🟢 0.818 | 50 | 950.94% | -1195.20% |

### Crypto

| 品种 | Sharpe | 交易数 | 年化收益% | 最大回撤% |
|------|--------|--------|-----------|-----------|
| BTC | 🟡 0.656 | 162 | 1522.81% | -2353.53% |
| ETH | 🟡 0.514 | 124 | 3821.63% | -5460.41% |
| SOL | 🔴 0.171 | 86 | 1641.89% | -6749.22% |

### ETF

| 品种 | Sharpe | 交易数 | 年化收益% | 最大回撤% |
|------|--------|--------|-----------|-----------|
| GLD | 🟢 1.227 | 71 | 269.40% | -436.73% |
| SPY | 🟡 0.797 | 90 | 132.50% | -306.85% |
| IWM | 🟡 0.727 | 86 | 112.21% | -373.74% |
| QQQ | 🟡 0.622 | 52 | 108.56% | -224.63% |
| TLT | 🔴 0.449 | 56 | 28.42% | -62.16% |

## 相关策略


## 相关概念

- [[mean-reversion]]
- [[RSI-(Relative-Strength-Index)]]
