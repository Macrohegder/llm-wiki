---
tags:
  - strategy
  - cta-developer
logic-type: "trend_following"
timeframe: "daily"
direction: "long_only"
source: "unknown"
status: "production"
markets-tested: []
created: "2026-06-14"
---

# CtaTrend

> 类型: #trend_following | 周期: daily | 方向: long_only | 来源: unknown

---

## 代码实现
- **cta_developer**: `cta/strategies/cta_trend_strategy.py`
- **类名**: `CtaTrendStrategy`

- **核心指标**: ATR

## 一句话摘要
海龟交易法则的趋势跟踪策略

## 批量挖掘结果

### CN期货

| 品种 | Sharpe | 交易数 | 年化收益% | 最大回撤% |
|------|--------|--------|-----------|-----------|
| TL888 | 🟢 0.829 | 55 | 539.84% | -1073.46% |
| IM888 | 🟡 0.766 | 83 | 2209.17% | -2135.53% |
| T888 | 🟡 0.585 | 115 | 157.09% | -454.79% |
| TF888 | 🔴 0.492 | 115 | 94.10% | -286.68% |
| AU888 | 🔴 0.460 | 82 | 493.61% | -1592.23% |

## 相关策略


## 相关概念

- [[trend-filter]]
