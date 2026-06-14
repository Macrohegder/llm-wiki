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

# WilliamsRVolFilter

> 类型: #mean_reversion | 周期: daily | 方向: long_only | 来源: unknown

---

## 代码实现
- **cta_developer**: `cta/strategies/williams_r_vol_filter_strategy.py`
- **类名**: `WilliamsRVolFilterStrategy`

- **核心指标**: RSI, ATR, Williams%R

## 一句话摘要
Larry Williams %R Mean Reversion with Volatility Expansion Filter

## 批量挖掘结果

### CN期货

| 品种 | Sharpe | 交易数 | 年化收益% | 最大回撤% |
|------|--------|--------|-----------|-----------|
| 561380 | 🟢 2.210 | 97 | 833.83% | -293.06% |
| 159363 | 🟢 1.981 | 79 | 1005.38% | -229.39% |
| 588170 | 🟢 1.904 | 53 | 863.28% | -284.29% |
| AD888 | 🟡 1.802 | 33 | 354.21% | -144.05% |
| 159326 | 🟢 1.747 | 109 | 591.50% | -261.22% |

## 相关策略


## 相关概念

- [[mean-reversion]]
- [[RSI-(Relative-Strength-Index)]]
