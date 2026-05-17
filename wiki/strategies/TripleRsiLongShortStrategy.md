---
tags:
  - strategy
  - cta-developer
logic-type: "mean_reversion"
timeframe: "daily"
direction: "long_short"
source: "unknown"
status: "production"
markets-tested: ['etf', 'crypto', 'cn_futures']
created: "2026-05-18"
---

# TripleRsi LS

> 类型: #mean_reversion | 周期: daily | 方向: long_short | 来源: unknown

---

## 代码实现
- **cta_developer**: `cta/strategies/triple_rsi_longshort_strategy.py`
- **类名**: `TripleRsiLongShortStrategy`

- **核心指标**: RSI

## 批量挖掘结果

### CN期货

| 品种 | Sharpe | 交易数 | 年化收益% | 最大回撤% |
|------|--------|--------|-----------|-----------|
| TF888 | 🟢 1.496 | 56 | 80.61% | -51.16% |
| T888 | 🟢 1.290 | 54 | 100.19% | -81.33% |
| AU888 | 🟢 1.222 | 66 | 181.97% | -121.78% |
| IH888 | 🔴 0.434 | 72 | 279.91% | -719.52% |
| IF888 | 🔴 0.368 | 60 | 495.63% | -1959.28% |

### Crypto

| 品种 | Sharpe | 交易数 | 年化收益% | 最大回撤% |
|------|--------|--------|-----------|-----------|
| BTC | 🟢 1.067 | 72 | 1262.73% | -970.64% |
| SOL | 🟡 0.756 | 109 | 12979.78% | -6743.36% |
| ETH | 🔴 0.375 | 131 | 3940.65% | -6923.26% |

### ETF

| 品种 | Sharpe | 交易数 | 年化收益% | 最大回撤% |
|------|--------|--------|-----------|-----------|
| TLT | 🟢 1.666 | 50 | 53.92% | -17.06% |
| IWM | 🟡 0.752 | 78 | 75.78% | -127.45% |
| GLD | 🔴 0.415 | 50 | 23.22% | -66.51% |
| SPY | 🔴 0.268 | 82 | 36.68% | -275.40% |
| QQQ | 🔴 0.105 | 63 | 19.84% | -352.48% |

## 相关策略


## 相关概念

- [[mean-reversion]]
- [[RSI-(Relative-Strength-Index)]]
