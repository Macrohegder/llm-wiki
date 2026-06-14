---
tags:
  - strategy
  - cta-developer
logic-type: "mean_reversion"
timeframe: "daily"
direction: "long_only"
source: "QuantifiedStrategies"
status: "production"
markets-tested: ['cn_futures', 'etf', 'crypto']
created: "2026-06-14"
---

# GoldEnvelope

> 类型: #mean_reversion | 周期: daily | 方向: long_only | 来源: QuantifiedStrategies

---

## 代码实现
- **cta_developer**: `cta/strategies/gold_envelope_strategy.py`
- **类名**: `GoldEnvelopeStrategy`

- **核心指标**: SMA

## 一句话摘要
Gold Envelope Trading Strategy (Quantified Strategies) (自包含版)

## 批量挖掘结果

### CN期货

| 品种 | Sharpe | 交易数 | 年化收益% | 最大回撤% |
|------|--------|--------|-----------|-----------|
| 513630 | 🟡 2.321 | 13 | 260.12% | -82.55% |
| AD888 | 🟡 2.212 | 6 | 272.44% | -37.81% |
| OP888 | 🟡 2.182 | 7 | 148.31% | -34.78% |
| 513920 | 🟡 1.987 | 15 | 246.49% | -69.06% |
| 511220 | 🟡 1.972 | 1 | 41.23% | -47.73% |

### Crypto

| 品种 | Sharpe | 交易数 | 年化收益% | 最大回撤% |
|------|--------|--------|-----------|-----------|
| XAU | 🟡 1.241 | 10 | 237.31% | -192.23% |
| BTC | 🔴 0.158 | 200 | 378.43% | -3139.98% |
| ETH | 🔴 0.120 | 180 | 2307.62% | -9845.71% |
| QQQ | 🔴 0.000 | 0 | 0.00% | 0.00% |
| SOL | 🔴 0.000 | 0 | 0.00% | 0.00% |

### ETF

| 品种 | Sharpe | 交易数 | 年化收益% | 最大回撤% |
|------|--------|--------|-----------|-----------|
| GLD | 🟡 0.708 | 58 | 143.52% | -420.84% |
| IWM | 🔴 0.438 | 98 | 93.91% | -344.10% |
| SPY | 🔴 0.374 | 64 | 75.34% | -292.52% |
| QQQ | 🔴 0.272 | 54 | 89.99% | -413.45% |
| TLT | 🔴 -0.754 | 51 | -87.51% | -556.58% |

## 相关策略


## 相关概念

- [[mean-reversion]]
