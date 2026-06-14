---
tags:
  - strategy
  - cta-developer
logic-type: "trend_following"
timeframe: "daily"
direction: "long_only"
source: "微信公众号"
status: "production"
markets-tested: []
created: "2026-06-14"
---

# Tango

> 类型: #trend_following | 周期: daily | 方向: long_only | 来源: 微信公众号

---

## 代码实现
- **cta_developer**: `cta/strategies/tango_strategy.py`
- **类名**: `TangoStrategy`

- **核心指标**: ADX, EMA

- **原文链接**: https://mp.weixin.qq.com/s/H3ADkPe-PxicX5rcgvGV-g

## 一句话摘要
TANGO Trading System (ADX趋势过滤 + 均线回踩突破 + 三K线止损)

## 批量挖掘结果

### CN期货

| 品种 | Sharpe | 交易数 | 年化收益% | 最大回撤% |
|------|--------|--------|-----------|-----------|
| 159400 | 🟡 3.828 | 14 | 12.09% | -1.38% |
| 551030 | 🟡 2.357 | 16 | 8.26% | -2.50% |
| 511200 | 🟡 1.909 | 21 | 6.35% | -5.03% |
| 159206 | 🟡 1.171 | 32 | 540.74% | -267.33% |
| 511220 | 🟢 1.098 | 272 | 13.92% | -21.69% |

## 相关策略


## 相关概念

- [[trend-filter]]
