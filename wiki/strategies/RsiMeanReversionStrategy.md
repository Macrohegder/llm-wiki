---
tags:
  - strategy
  - cta-developer
logic-type: "mean_reversion"
timeframe: "daily"
direction: "long_only"
source: "unknown"
status: "production"
markets-tested: ['etf', 'crypto', 'cn_futures']
created: "2026-05-18"
---

# RsiMeanReversion

> 类型: #mean_reversion | 周期: daily | 方向: long_only | 来源: unknown

---

## 代码实现
- **cta_developer**: `cta/strategies/rsi_mean_reversion_strategy.py`
- **类名**: `RsiMeanReversionStrategy`

- **核心指标**: RSI

## 一句话摘要
RSI均值回归策略 (自包含版)

## 批量挖掘结果

### CN期货

| 品种 | Sharpe | 交易数 | 年化收益% | 最大回撤% |
|------|--------|--------|-----------|-----------|
| T888 | 🟢 0.946 | 52 | 21374.18% | -2707.13% |
| AU888 | 🟢 0.907 | 63 | 1678.54% | -1358.03% |
| IH888 | 🟢 0.820 | 62 | 799.25% | -943.78% |
| IF888 | 🟡 0.770 | 166 | 2030.71% | -2547.63% |
| IC888 | 🔴 0.427 | 58 | 719.85% | -2054.76% |

### Crypto

| 品种 | Sharpe | 交易数 | 年化收益% | 最大回撤% |
|------|--------|--------|-----------|-----------|
| BTC | 🔴 -0.052 | 62 | -0.09% | -3.14% |
| ETH | 🔴 -0.076 | 110 | -0.09% | -2.01% |
| SOL | 🔴 -0.505 | 56 | -2.34% | -21.56% |

### ETF

| 品种 | Sharpe | 交易数 | 年化收益% | 最大回撤% |
|------|--------|--------|-----------|-----------|
| GLD | 🟢 0.891 | 58 | 1.77% | -2.90% |
| SPY | 🔴 0.372 | 90 | 1.37% | -8.41% |
| TLT | 🔴 0.317 | 60 | 0.85% | -6.26% |
| QQQ | 🔴 0.277 | 54 | 0.67% | -3.88% |
| IWM | 🔴 0.170 | 59 | 0.31% | -4.57% |

## 相关策略


## 相关概念

- [[mean-reversion]]
- [[RSI-(Relative-Strength-Index)]]
