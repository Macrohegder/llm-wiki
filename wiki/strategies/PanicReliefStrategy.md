---
tags:
  - strategy
  - cta-developer
logic-type: "mean_reversion"
timeframe: "daily"
direction: "long_only"
source: "unknown"
status: "production"
markets-tested: ['etf', 'crypto', 'cn_futures']
created: "2026-06-14"
---

# PanicRelief

> 类型: #mean_reversion | 周期: daily | 方向: long_only | 来源: unknown

---

## 代码实现
- **cta_developer**: `cta/strategies/panic_relief_strategy.py`
- **类名**: `PanicReliefStrategy`

## 一句话摘要
恐慌 relief 策略 (自包含版)

## 批量挖掘结果

### CN期货

| 品种 | Sharpe | 交易数 | 年化收益% | 最大回撤% |
|------|--------|--------|-----------|-----------|
| BZ888 | 🟡 1.817 | 1 | 17.20% | 0.00% |
| BR888 | 🟢 1.684 | 50 | 594.12% | -296.36% |
| LC888 | 🟡 1.547 | 12 | 405.21% | -130.24% |
| PR888 | 🟡 1.483 | 6 | 539.00% | -121.61% |
| PL888 | 🟡 1.288 | 3 | 111.75% | -47.14% |

## 相关策略


## 相关概念

- [[mean-reversion]]
