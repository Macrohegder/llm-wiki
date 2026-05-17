---
tags:
  - strategy
  - cta-developer
logic-type: "trend_following"
timeframe: "daily"
direction: "long_only"
source: "QuantifiedStrategies"
status: "production"
markets-tested: ['etf', 'crypto', 'cn_futures']
created: "2026-05-18"
---

# DonchianAdxBreakout

> 类型: #trend_following | 周期: daily | 方向: long_only | 来源: QuantifiedStrategies

---

## 代码实现
- **cta_developer**: `cta/strategies/donchian_adx_breakout_strategy.py`
- **类名**: `DonchianAdxBreakoutStrategy`

- **核心指标**: ADX, Donchian

## 一句话摘要
Donchian Channel + ADX Breakout Strategy (唐奇安通道 + ADX 突破策略)

## 批量挖掘结果

### CN期货

| 品种 | Sharpe | 交易数 | 年化收益% | 最大回撤% |
|------|--------|--------|-----------|-----------|
| IC888 | 🟢 0.814 | 52 | 788.10% | -1100.47% |
| AU888 | 🟡 0.691 | 54 | 220.97% | -349.79% |
| T888 | 🟡 0.559 | 78 | 81.37% | -214.37% |
| IH888 | 🔴 0.462 | 57 | 362.89% | -720.78% |
| TF888 | 🔴 0.452 | 102 | 54.25% | -196.02% |

### ETF

| 品种 | Sharpe | 交易数 | 年化收益% | 最大回撤% |
|------|--------|--------|-----------|-----------|
| GLD | 🟡 0.778 | 74 | 147.15% | -227.42% |
| QQQ | 🟡 0.705 | 85 | 186.47% | -206.04% |
| SPY | 🟡 0.536 | 86 | 47.84% | -101.17% |
| IWM | 🔴 0.153 | 75 | 16.89% | -223.52% |
| TLT | 🔴 -0.055 | 52 | -3.99% | -200.68% |

## 相关策略


## 相关概念

- [[trend-filter]]
