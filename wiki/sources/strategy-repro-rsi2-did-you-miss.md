---
id: strategy-repro-rsi2-did-you-miss
title: "Strategy Repro: Did You Miss This? (RSI-2 Strategy)"
source: "Quantified Strategies"
url: https://quantifiedstrategies.substack.com/p/did-you-miss-this
reproduced_at: 2026-04-25
status: completed
rating: green
---

# RSI-2 隐藏策略 — 策略复现报告

## 原文摘要

> "Did You Miss This?" 文章揭示了隐藏在经典RSI-2策略中的参数技巧。标准的2周期RSI策略在参数微调后，在不同品种上展现出截然不同的表现。通过OAT优化每个品种的独立参数，可以获得比统一参数更好的结果。

## 复现方法

| 项目 | 设置 |
|------|------|
| 标的 | SPY, QQQ, IWM, GLD |
| 回测区间 | 2019-01-01 ~ 2025-12-31 |
| 资金 | $100,000 |
| 优化方法 | OAT + GA |
| 优化目标 | Sharpe Ratio |

## 最优参数 (品种独立优化)

| 参数 | GLD | IWM | SPY | QQQ |
|------|------|------|------|------|
| RSI Period | 2 | 2 | 2 | 2 |
| 超卖阈值 | 8 | 4 | 5 | 2 |
| 超买阈值 | 96 | 82 | 80 | 88 |
| 固定仓位 | 2 | 2 | 15 | 15 |

## 回测结果

| 指标 | GLD | IWM |
|------|------|------|
| **Sharpe Ratio** | 1.479 | 1.170 |
| 交易次数 | 38 | 58 |
| 最大回撤 | -0.52% | -0.42% |
| 年化收益 | 0.81% | 0.50% |
| 总收益 | 4.01% | 3.09% |

## 结论

- 评级：**GREEN** ✅（GLD 和 IWM）
- 2个Green品种（GLD Sharpe=1.479, IWM Sharpe=1.170）
- GLD 表现最优——Sharpe接近1.5，回撤极低
- 参数依赖性强——不同品种的最优参数差异巨大（超卖阈值从2到8，超买阈值从80到96）
- 仓位大小对结果有显著影响（GLD/IWM用2，SPY/QQQ用15）

## 复现产物

- YAML: `strategies/inbox/rsi_2_strategy.yaml`
- 代码: `generated/rsi_2_strategy.py`
- 评估报告: `reports/eval_rsi_2_20260423_011301.json`

## 复现状态

- **复现完成**: 2026-04-25
- **策略 ID**: `rsi_2` (did_you_miss_this)
- **评级汇总**: Green=2 | Yellow=1 | Red=1 | Total=4

- **最佳品种**: GLD (Sharpe=1.479)

### 各品种回测结果

| 品种 | 评级 | Sharpe | 交易次数 | 最大回撤 | 年化收益 | 总收益 |
|--------|-------|--------|----------|----------|----------|----------|
| SPY | YELLOW | 0.885 | 50 | -6.87% | 5.17% | 31.76% |
| QQQ | RED | 0.483 | 12 | -6.93% | 1.88% | 9.34% |
| IWM | GREEN | 1.170 | 58 | -0.42% | 0.50% | 3.09% |
| GLD | GREEN | 1.479 | 38 | -0.52% | 0.81% | 4.01% |

### 最优参数 (最佳品种 GLD)

| 参数 | 最优值 |
|--------|--------|
| RSI Period | 2 |
| 超卖阈值 | 8 |
| 超买阈值 | 96 |
| 固定仓位 | 2 |

*评估报告*: `eval_rsi_2_20260423_011301.json`
