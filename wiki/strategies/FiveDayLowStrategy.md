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

# FiveDayLow

> 类型: #mean_reversion | 周期: daily | 方向: long_only | 来源: QuantifiedStrategies

---

## 代码实现
- **cta_developer**: `cta/strategies/five_day_low_strategy.py`
- **类名**: `FiveDayLowStrategy`

- **核心指标**: RSI, ATR

## 一句话摘要
5日低点均值回归策略 (5-Day Low Mean Reversion Strategy)

## 批量挖掘结果

### CN期货

| 品种 | Sharpe | 交易数 | 年化收益% | 最大回撤% |
|------|--------|--------|-----------|-----------|
| BZ888 | 🟡 2.607 | 36 | 228.19% | -35.71% |
| 513920 | 🟢 1.772 | 109 | 0.00% | -0.00% |
| 159566 | 🟢 1.621 | 127 | 0.00% | -0.00% |
| 513630 | 🟢 1.317 | 107 | 0.00% | -0.00% |
| 159206 | 🟡 1.307 | 43 | 0.00% | -0.00% |

### Crypto

| 品种 | Sharpe | 交易数 | 年化收益% | 最大回撤% |
|------|--------|--------|-----------|-----------|
| XAU | 🟢 0.800 | 61 | 0.00% | -0.00% |
| BTC | 🔴 0.444 | 488 | 0.67% | -3.05% |
| ETH | 🔴 0.211 | 601 | 0.23% | -3.29% |
| SOL | 🔴 -0.010 | 457 | -0.01% | -1.40% |

### ETF

| 品种 | Sharpe | 交易数 | 年化收益% | 最大回撤% |
|------|--------|--------|-----------|-----------|
| SPY | 🟢 1.078 | 272 | 0.58% | -0.46% |
| QQQ | 🟢 1.001 | 224 | 0.60% | -0.88% |
| IWM | 🟡 0.770 | 268 | 0.18% | -0.35% |
| GLD | 🟡 0.767 | 169 | 0.21% | -0.38% |
| TLT | 🔴 0.096 | 251 | 0.01% | -0.27% |

## 相关策略


## 相关概念

- [[mean-reversion]]
- [[RSI-(Relative-Strength-Index)]]
