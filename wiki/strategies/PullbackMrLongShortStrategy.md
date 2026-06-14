---
tags:
  - strategy
  - cta-developer
logic-type: "mean_reversion"
timeframe: "daily"
direction: "long_short"
source: "原创"
status: "production"
markets-tested: []
created: "2026-06-14"
---

# PullbackMr LS

> 类型: #mean_reversion | 周期: daily | 方向: long_short | 来源: 原创

---

## 代码实现
- **cta_developer**: `cta/strategies/pullback_mr_longshort_strategy.py`
- **类名**: `PullbackMrLongShortStrategy`

- **核心指标**: RSI, SMA

## 一句话摘要
Pullback Mean Reversion Long/Short Strategy

## 批量挖掘结果

### CN期货

| 品种 | Sharpe | 交易数 | 年化收益% | 最大回撤% |
|------|--------|--------|-----------|-----------|
| PS888 | 🟡 2.420 | 21 | 857.22% | -195.72% |
| BZ888 | 🟡 1.827 | 1 | 36.33% | -0.80% |
| PR888 | 🟡 1.512 | 24 | 110.99% | -57.58% |
| AD888 | 🟡 1.412 | 3 | 147.82% | -31.61% |
| PX888 | 🟢 1.346 | 50 | 111.14% | -58.23% |

## 相关策略


## 相关概念

- [[mean-reversion]]
- [[RSI-(Relative-Strength-Index)]]
