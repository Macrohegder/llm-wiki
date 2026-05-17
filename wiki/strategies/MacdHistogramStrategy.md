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
| T888 | 🟢 1.300 | 118 | 103.30% | -86.39% |
| TF888 | 🟢 1.161 | 126 | 67.03% | -71.00% |
| IC888 | 🟡 0.687 | 50 | 429.50% | -1076.42% |
| TL888 | 🟡 0.623 | 52 | 149.70% | -331.63% |
| IH888 | 🔴 0.138 | 82 | 67.49% | -842.04% |

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
