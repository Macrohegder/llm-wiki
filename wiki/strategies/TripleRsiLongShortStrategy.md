---
tags:
  - strategy
  - cta-developer
logic-type: "mean_reversion"
timeframe: "daily"
direction: "long_short"
source: "unknown"
status: "production"
markets-tested: ['cn_futures', 'etf']
created: "2026-06-14"
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
| PS888 | 🟡 2.378 | 12 | 473.93% | -31.95% |
| PL888 | 🟡 2.165 | 2 | 72.74% | 0.00% |
| 159262 | 🟡 1.962 | 2 | 42.52% | 0.00% |
| LG888 | 🟡 1.916 | 8 | 57.26% | -11.17% |
| PX888 | 🟡 1.914 | 20 | 114.94% | -25.72% |

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
