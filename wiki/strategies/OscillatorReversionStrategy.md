---
tags:
  - strategy
  - cta-developer
logic-type: "mean_reversion"
timeframe: "daily"
direction: "long_only"
source: "微信公众号"
status: "production"
markets-tested: []
created: "2026-06-14"
---

# OscillatorReversion

> 类型: #mean_reversion | 周期: daily | 方向: long_only | 来源: 微信公众号

---

## 代码实现
- **cta_developer**: `cta/strategies/oscillator_reversion_strategy.py`
- **类名**: `OscillatorReversionStrategy`

- **核心指标**: RSI, EMA

- **原文链接**: https://mp.weixin.qq.com/s/WhOGZfvFZkPnJHU6XNByQQ

## 一句话摘要
Oscillator Reversion Strategy (振荡器回归策略)

## 批量挖掘结果

### CN期货

| 品种 | Sharpe | 交易数 | 年化收益% | 最大回撤% |
|------|--------|--------|-----------|-----------|
| 511360 | 🟡 4.470 | 9 | 6.53% | -1.45% |
| PR888 | 🟡 2.202 | 40 | 74.40% | -23.11% |
| PT888 | 🟡 2.077 | 1 | 207.94% | -24.57% |
| 159650 | 🟡 1.912 | 36 | 7.55% | -3.75% |
| 511580 | 🟡 1.739 | 30 | 10.94% | -7.22% |

## 相关策略


## 相关概念

- [[mean-reversion]]
- [[RSI-(Relative-Strength-Index)]]
