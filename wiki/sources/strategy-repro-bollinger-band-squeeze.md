---
id: strategy-repro-bollinger-band-squeeze
title: "Strategy Repro: Bollinger Band Squeeze Trading Strategy"
source: "Quantified Strategies"
url: https://quantifiedstrategies.substack.com/p/bollinger-band-squeeze-trading-strategy
reproduced_at: 2026-04-25
status: completed
rating: red
source_note: 2026-04-22-Bollinger-Band-Squeeze-Trading-Strategy
---

# Bollinger Band Squeeze — 布林带收缩策略复现报告

## 原文摘要

> 布林带收缩(Bollinger Band Squeeze)策略识别布林带宽度收缩至低水平时预示即将发生价格突破。策略在RBollinger带宽低于阈值时建仓，配合RSI过滤器判断突破方向。

## 复现方法

| 项目 | 设置 |
|------|------|
| 标的 | SPY, QQQ, IWM, GLD |
| 回测区间 | 2019-01-01 ~ 2025-12-31 |
| 资金 | $100,000 |
| 优化方法 | OAT + GA |
| 优化目标 | Sharpe Ratio |

## 最优参数 (QQQ)

| 参数 | 最优值 |
|------|--------|
| BB Period | 18 |
| BB Std Dev | 1.4 |
| RSI Period | 6 |
| 带宽阈值 | 28 |
| 固定仓位 | 15 |

## 回测结果

| 指标 | 数值 |
|------|------|
| **Sharpe Ratio** | 0.766（QQQ） |
| 交易次数 | 48 |
| 最大回撤 | -13.65% |
| 年化收益 | 8.20% |
| 总收益 | 40.66% |

## 结论

- 评级：**RED** 🔴（全品种按严格标准）
- QQQ 品种表现相对最好（Sharpe=0.766, 48笔交易），但未达到Green阈值
- SPY 和 GLD 交易次数过少（4笔和1笔）
- 布林带收缩策略在日线上交易信号稀疏，可能需要更小的周期或增加入场条件

## 复现产物

- YAML: `strategies/inbox/bollinger_band_squeeze.yaml`
- 代码: `generated/bollinger_band_squeeze_strategy.py`
- 评估报告: `reports/eval_bollinger_band_squeeze_20260423_011450.json`

## 复现状态

- **复现完成**: 2026-04-25
- **策略 ID**: `bollinger_band_squeeze`
- **评级汇总**: Green=0 | Yellow=0 | Red=4 | Total=4

- **最佳品种**: QQQ (Sharpe=0.766)

### 各品种回测结果

| 品种 | 评级 | Sharpe | 交易次数 | 最大回撤 | 年化收益 | 总收益 |
|--------|-------|--------|----------|----------|----------|----------|
| SPY | RED | 1.095 | 4 | -3.32% | 2.61% | 16.06% |
| QQQ | RED | 0.766 | 48 | -13.65% | 8.20% | 40.66% |
| IWM | RED | 0.407 | 34 | -9.19% | 2.04% | 12.55% |
| GLD | RED | 1.154 | 1 | -9.58% | 8.39% | 41.63% |

### 最优参数 (最佳品种 QQQ)

| 参数 | 最优值 |
|--------|--------|
| BB Period | 18 |
| BB Std Dev | 1.4 |
| RSI Period | 6 |
| 带宽阈值 | 28 |

*评估报告*: `eval_bollinger_band_squeeze_20260423_011450.json`
