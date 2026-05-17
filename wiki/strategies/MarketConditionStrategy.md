---
tags:
  - strategy
  - cta-developer
logic-type: "mean_reversion"
timeframe: "daily"
direction: "long_only"
source: "unknown"
status: "production"
markets-tested: []
created: "2026-05-18"
---

# MarketCondition

> 类型: #mean_reversion | 周期: daily | 方向: long_only | 来源: unknown

---

## 代码实现
- **cta_developer**: `cta/strategies/market_condition_strategy.py`
- **类名**: `MarketConditionStrategy`

- **核心指标**: RSI, ADX

## 一句话摘要
市场状态策略 (自包含版)

## 批量挖掘结果

### CN期货

| 品种 | Sharpe | 交易数 | 年化收益% | 最大回撤% |
|------|--------|--------|-----------|-----------|
| AU888 | 🟢 1.126 | 189 | 367.27% | -331.12% |
| IF888 | 🟢 0.843 | 108 | 1127.38% | -1138.78% |
| T888 | 🔴 0.493 | 220 | 73.89% | -264.19% |
| TF888 | 🔴 0.481 | 271 | 50.47% | -180.13% |
| IH888 | 🔴 0.373 | 250 | 386.03% | -1599.57% |

### Crypto

| 品种 | Sharpe | 交易数 | 年化收益% | 最大回撤% |
|------|--------|--------|-----------|-----------|
| ETH | 🟡 0.715 | 110 | 0.27% | -0.50% |
| BTC | 🔴 -0.010 | 316 | -0.01% | -3.34% |
| SOL | 🔴 -0.164 | 209 | -0.07% | -0.99% |

### ETF

| 品种 | Sharpe | 交易数 | 年化收益% | 最大回撤% |
|------|--------|--------|-----------|-----------|
| IWM | 🟢 0.959 | 268 | 0.25% | -0.39% |
| SPY | 🟢 0.919 | 144 | 0.28% | -0.42% |
| QQQ | 🟡 0.797 | 142 | 0.31% | -0.59% |
| GLD | 🟡 0.596 | 211 | 0.16% | -0.36% |
| TLT | 🔴 0.002 | 259 | 0.00% | -0.24% |

## 相关策略


## 相关概念

- [[mean-reversion]]
- [[RSI-(Relative-Strength-Index)]]
