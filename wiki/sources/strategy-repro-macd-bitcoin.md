---
id: strategy-repro-macd-bitcoin
title: "Strategy Repro: MACD Trading Strategy For Bitcoin"
source: "Quantified Strategies"
url: https://quantifiedstrategies.substack.com/p/macd-trading-strategy-for-bitcoin
reproduced_at: 2026-04-25
status: completed
rating: red
source_note: 2023-12-27-MACD-Trading-Strategy-For-Bitcoin
---

# MACD Trading Strategy For Bitcoin — 比特币MACD策略复现报告

## 原文摘要

> 将经典MACD交叉策略（快线/慢线/信号线）应用于比特币交易。MACD金叉做多、死叉做空，适用于趋势性强的加密货币市场。

## 复现方法

| 项目 | 设置 |
|------|------|
| 标的 | BTCUSDT.SWAP (OKX) |
| 回测区间 | 2019-01-01 ~ 2025-12-31 |
| 资金 | $100,000 |
| 优化方法 | OAT + GA |
| 优化目标 | Sharpe Ratio |

## 最优参数

| 参数 | 最优值 |
|------|--------|
| Fast Period | 5 |
| Slow Period | 16 |
| Signal Period | 7 |
| 固定仓位 | 2 |

## 回测结果

| 指标 | 数值 |
|------|------|
| **Sharpe Ratio** | 0.944（queue）/ 0.0（eval JSON） |
| 交易次数 | 89 |
| 最大回撤 | -51.76% |
| 年化收益 | - |
| 总收益 | - |

## 结论

- 评级：**RED** 🔴（严格评级）
- Eval JSON 显示 0 笔交易（可能与品种/数据有关），但 pipeline queue 记录 Sharpe=0.944, 89笔交易
- 最大回撤-51.76%意味着策略风险极高
- 比特币的高波动性导致MACD策略的回撤显著
- 需要更多品种验证和更合理的风险管理

## 复现产物

- YAML: `strategies/inbox/macd_trading_strategy_for_bitcoin.yaml`
- 代码: `generated/macd_trading_strategy_for_bitcoin_strategy.py`
- 评估报告: `reports/eval_macd_trading_strategy_for_bitcoin_20260425_053424.json`

## 复现状态

- **复现完成**: 2026-04-25
- **策略 ID**: `macd_trading_strategy_for_bitcoin`
- **评级汇总**: Green=0 | Yellow=0 | Red=1 | Total=1

- **最佳品种**: BTCUSDT (Sharpe=0.944)

### 各品种回测结果

| 品种 | 评级 | Sharpe | 交易次数 | 最大回撤 | 年化收益 | 总收益 |
|--------|-------|--------|----------|----------|----------|----------|
| BTCUSDT | RED | 0.944 | 89 | -51.76% | - | - |

*注：pipeline queue 另有 yellow 评级结果（Sharpe=0.944, 89笔交易），但 eval JSON 过滤后判为 RED。*

### 最优参数

| 参数 | 最优值 |
|--------|--------|
| Fast Period | 5 |
| Slow Period | 16 |
| Signal Period | 7 |

*评估报告*: `eval_macd_trading_strategy_for_bitcoin_20260425_053424.json`
