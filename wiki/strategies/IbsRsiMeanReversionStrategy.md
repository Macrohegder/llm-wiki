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

# IbsRsiMeanReversion

> 类型: #mean_reversion | 周期: daily | 方向: long_only | 来源: QuantifiedStrategies

---

## 代码实现
- **cta_developer**: `cta/strategies/ibs_rsi_mean_reversion_strategy.py`
- **类名**: `IbsRsiMeanReversionStrategy`

- **核心指标**: RSI, IBS

- **原文链接**: https://quantifiedstrategies.substack.com/p/s-and-p-500-mean-reversion-using-112

## 一句话摘要
IBS + RSI Mean Reversion Strategy

## 批量挖掘结果

### CN期货

| 品种 | Sharpe | 交易数 | 年化收益% | 最大回撤% |
|------|--------|--------|-----------|-----------|
| T888 | 🟢 1.148 | 130 | 102.11% | -73.23% |
| TL888 | 🟢 1.038 | 94 | 283.47% | -243.67% |
| TF888 | 🟡 0.745 | 128 | 42.78% | -76.29% |
| IC888 | 🟡 0.557 | 246 | 786.58% | -1958.36% |
| IH888 | 🔴 0.469 | 56 | 243.29% | -760.06% |

### ETF

| 品种 | Sharpe | 交易数 | 年化收益% | 最大回撤% |
|------|--------|--------|-----------|-----------|
| SPY | 🟡 0.603 | 268 | 90.31% | -197.51% |
| IWM | 🔴 0.499 | 276 | 75.67% | -201.55% |
| GLD | 🔴 0.498 | 94 | 55.83% | -178.21% |
| QQQ | 🔴 -0.009 | 232 | -2.14% | -542.97% |
| TLT | 🔴 -0.054 | 110 | -2.69% | -153.20% |

## 相关策略


## 相关概念

- [[mean-reversion]]
- [[RSI-(Relative-Strength-Index)]]
- [[IBS-(Internal-Bar-Strength)]]
