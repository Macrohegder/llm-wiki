---
tags:
  - strategy
  - cta-developer
logic-type: "mean_reversion"
timeframe: "daily"
direction: "long_only"
source: "QuantifiedStrategies"
status: "production"
markets-tested: ['etf', 'cn_futures']
created: "2026-06-14"
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
| BZ888 | 🟡 2.565 | 26 | 98.21% | -9.19% |
| PT888 | 🟡 2.417 | 4 | 199.21% | -0.57% |
| AD888 | 🟡 2.406 | 35 | 295.49% | -38.55% |
| LG888 | 🟢 2.334 | 55 | 76.28% | -10.35% |
| OP888 | 🟡 2.063 | 21 | 74.30% | -10.82% |

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
