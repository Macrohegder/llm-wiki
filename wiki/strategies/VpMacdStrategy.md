---
tags:
  - strategy
  - cta-developer
logic-type: "trend_following"
timeframe: "daily"
direction: "long_only"
source: "微信公众号"
status: "production"
markets-tested: ['cn_futures']
created: "2026-06-14"
---

# VpMacd

> 类型: #trend_following | 周期: daily | 方向: long_only | 来源: 微信公众号

---

## 代码实现
- **cta_developer**: `cta/strategies/vp_macd_strategy.py`
- **类名**: `VpMacdStrategy`

- **核心指标**: MACD, EMA

## 一句话摘要
VP-MACD 策略 (量价调整MACD)

## 批量挖掘结果

### CN期货

| 品种 | Sharpe | 交易数 | 年化收益% | 最大回撤% |
|------|--------|--------|-----------|-----------|
| 159262 | 🟡 2.324 | 15 | 290.17% | -39.57% |
| 511200 | 🟢 2.085 | 55 | 227.73% | -71.73% |
| 159397 | 🟢 2.059 | 54 | 34.49% | -9.83% |
| 159206 | 🟢 1.958 | 79 | 4200.36% | -604.85% |
| 159509 | 🟢 1.790 | 109 | 987.79% | -265.45% |

## 相关策略


## 相关概念

- [[trend-filter]]
- MACD (暂无专门概念页)
