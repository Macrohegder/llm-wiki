---
tags:
  - strategy
  - cta-developer
logic-type: "pattern"
timeframe: "daily"
direction: "long_only"
source: "QuantifiedStrategies"
status: "production"
markets-tested: ['etf', 'crypto', 'cn_futures']
created: "2026-06-14"
---

# CandlestickPattern

> 类型: #pattern | 周期: daily | 方向: long_only | 来源: QuantifiedStrategies

---

## 代码实现
- **cta_developer**: `cta/strategies/candlestick_pattern_strategy.py`
- **类名**: `CandlestickPatternStrategy`

## 一句话摘要
蜡烛图模式识别策略 (Candlestick Pattern Strategy) (自包含版)

## 批量挖掘结果

### CN期货

| 品种 | Sharpe | 交易数 | 年化收益% | 最大回撤% |
|------|--------|--------|-----------|-----------|
| 159262 | 🟡 1.536 | 1 | 408.11% | -102.97% |
| 159516 | 🟡 0.590 | 2 | 6.38% | -0.30% |
| 513330 | 🟡 0.501 | 1 | 81.20% | -309.43% |
| 513060 | 🔴 0.441 | 1 | 90.23% | -398.87% |
| 513130 | 🔴 0.413 | 1 | 80.03% | -436.12% |

### Crypto

| 品种 | Sharpe | 交易数 | 年化收益% | 最大回撤% |
|------|--------|--------|-----------|-----------|
| BTC | 🔴 0.000 | 0 | 0.00% | 0.00% |
| ETH | 🔴 0.000 | 0 | 0.00% | 0.00% |
| SOL | 🔴 0.000 | 0 | 0.00% | 0.00% |
| SPY | 🔴 0.000 | 0 | 0.00% | 0.00% |
| XAU | 🔴 -1.037 | 3 | -353.84% | -709.26% |

### ETF

| 品种 | Sharpe | 交易数 | 年化收益% | 最大回撤% |
|------|--------|--------|-----------|-----------|
| TLT | 🟡 1.015 | 3 | 128.37% | -126.71% |
| GLD | 🔴 0.000 | 0 | 0.00% | 0.00% |
| IWM | 🔴 0.000 | 0 | 0.00% | 0.00% |
| QQQ | 🔴 0.000 | 0 | 0.00% | 0.00% |
| SPY | 🔴 0.000 | 0 | 0.00% | 0.00% |

## 相关策略


## 相关概念

- [[swing-trading]]
