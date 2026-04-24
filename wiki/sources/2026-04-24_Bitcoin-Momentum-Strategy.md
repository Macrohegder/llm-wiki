---
date: "2026-04-24"
author: ""
source: "quantifiedstrategies"
url: "https://quantifiedstrategies.substack.com/p/bitcoin-momentum-strategy"
status: "preview-only"
concrete_score: 5
tags:
  - strategy/trend-following
  - strategy/mean-reversion
  - strategy/seasonal
  - asset/equity
  - asset/commodity
  - asset/crypto
  - topic/backtesting
  - topic/risk-management
---

# Bitcoin Momentum Strategy

> 来源：[https://quantifiedstrategies.substack.com/p/bitcoin-momentum-strategy](https://quantifiedstrategies.substack.com/p/bitcoin-momentum-strategy) | 摄入日期：2026-04-24

---

## 核心观点

（待补充）

## 提取的实体
- [[entity:]]
- [[entity:]]

## 提取的概念
- [[concept:]]
- [[concept:]]

## 策略规则（如适用）
| 维度 | 描述 |
|------|------|
| 入场条件 | |
| 出场条件 | |
| 止损设置 | |
| 仓位管理 | |
| 时间框架 | |
| 适用品种 | |

## 回测数据
| 指标 | 数值 |
|------|------|
| CAGR | |
| Sharpe | |
| 最大回撤 | |
| 胜率 | |
| 交易次数 | |

## 个人批注
- 

## 原文备份
详见 raw/articles/2026-04-24_Bitcoin-Momentum-Strategy.md


## 复现状态

- **复现完成**: 2026-04-24 10:35
- **策略 ID**: `bitcoin_momentum_strategy`
- **评级汇总**: Green=0 | Yellow=1 | Red=0 | Total=1

- **最佳品种**: BTCUSDT_SWAP_OKX.GLOBAL (Sharpe=0.476)

### 各品种回测结果

| 品种 | 评级 | Sharpe | 交易次数 | 最大回撤 | 年化收益 | 总收益 |
|--------|-------|--------|----------|----------|----------|----------|
| BTCUSDT_SWAP_OKX.GLOBAL | yellow | 0.476 | 598 | -54.03% | 13.36% | 83.15% |

### 最优参数 (最佳品种)

| 参数 | 最优值 |
|--------|--------|
| fast_period | 4 |
| slow_period | 18 |
| fixed_size | 1 |
| price_add_rate | 0.0 |

*评估报告*: `eval_bitcoin_momentum_strategy_20260424_103404.json`