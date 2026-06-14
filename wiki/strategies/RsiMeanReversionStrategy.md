---
tags:
  - strategy
  - cta-developer
logic-type: "mean_reversion"
timeframe: "daily"
direction: "long_only"
source: "unknown"
status: "production"
markets-tested: ['cn_futures', 'etf', 'crypto']
created: "2026-06-14"
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
| OP888 | 🟡 3.291 | 12 | 90.84% | -6.62% |
| PT888 | 🟡 2.360 | 2 | 5.92% | -0.31% |
| 563360 | 🟡 2.021 | 2 | 1.58% | -0.11% |
| PD888 | 🟡 1.821 | 4 | 9.55% | -1.26% |
| AD888 | 🟡 1.727 | 7 | 197.11% | -45.15% |

### Crypto

| 品种 | Sharpe | 交易数 | 年化收益% | 最大回撤% |
|------|--------|--------|-----------|-----------|
| BTC | 🔴 -0.052 | 62 | -0.09% | -3.14% |
| ETH | 🔴 -0.076 | 110 | -0.09% | -2.01% |
| SOL | 🔴 -0.526 | 56 | -1.84% | -16.57% |

### ETF

| 品种 | Sharpe | 交易数 | 年化收益% | 最大回撤% |
|------|--------|--------|-----------|-----------|
| GLD | 🟢 0.891 | 58 | 1.77% | -2.90% |
| SPY | 🔴 0.372 | 90 | 1.37% | -8.41% |
| TLT | 🔴 0.315 | 60 | 1.20% | -8.77% |
| QQQ | 🔴 0.277 | 54 | 0.67% | -3.88% |
| IWM | 🔴 0.170 | 59 | 0.31% | -4.57% |

## 相关策略


## 相关概念

- [[mean-reversion]]
- [[RSI-(Relative-Strength-Index)]]
