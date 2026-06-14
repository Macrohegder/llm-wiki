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

# MacdHistogram

> 类型: #mean_reversion | 周期: daily | 方向: long_only | 来源: QuantifiedStrategies

---

## 代码实现
- **cta_developer**: `cta/strategies/macd_histogram_strategy.py`
- **类名**: `MacdHistogramStrategy`

- **核心指标**: MACD

## 一句话摘要
MACD柱状图策略 (自包含版)

## 批量挖掘结果

### CN期货

| 品种 | Sharpe | 交易数 | 年化收益% | 最大回撤% |
|------|--------|--------|-----------|-----------|
| 159262 | 🟡 2.381 | 4 | 88.53% | 0.00% |
| LG888 | 🟡 2.314 | 15 | 17.99% | -0.17% |
| 588170 | 🟡 2.089 | 8 | 121.16% | -2.58% |
| BZ888 | 🟡 2.013 | 8 | 147.14% | -4.66% |
| OP888 | 🟡 1.901 | 8 | 18.56% | -0.44% |

### Crypto

| 品种 | Sharpe | 交易数 | 年化收益% | 最大回撤% |
|------|--------|--------|-----------|-----------|
| SOL | 🟢 0.814 | 110 | 6973.42% | -3728.60% |
| BTC | 🟡 0.671 | 180 | 922.54% | -1333.52% |
| ETH | 🟡 0.504 | 154 | 2909.63% | -3909.97% |

### ETF

| 品种 | Sharpe | 交易数 | 年化收益% | 最大回撤% |
|------|--------|--------|-----------|-----------|
| QQQ | 🟢 1.056 | 108 | 204.66% | -155.28% |
| SPY | 🟢 0.872 | 78 | 84.17% | -105.85% |
| IWM | 🟡 0.790 | 84 | 69.30% | -142.84% |
| TLT | 🔴 0.327 | 98 | 16.05% | -75.60% |
| GLD | 🔴 0.318 | 72 | 41.11% | -376.04% |

## 相关策略


## 相关概念

- [[mean-reversion]]
- MACD (暂无专门概念页)
