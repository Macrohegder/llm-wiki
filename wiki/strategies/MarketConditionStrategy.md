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
created: "2026-06-14"
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
| BZ888 | 🟡 2.599 | 14 | 78.92% | -7.35% |
| PL888 | 🟡 2.435 | 12 | 84.30% | -6.02% |
| OP888 | 🟡 2.185 | 5 | 27.17% | -1.02% |
| AD888 | 🟡 1.835 | 20 | 126.50% | -47.84% |
| 159399 | 🟡 1.663 | 43 | 0.00% | -0.00% |

### Crypto

| 品种 | Sharpe | 交易数 | 年化收益% | 最大回撤% |
|------|--------|--------|-----------|-----------|
| ETH | 🟡 0.715 | 110 | 0.27% | -0.50% |
| BTC | 🔴 -0.011 | 322 | -0.01% | -3.20% |
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
