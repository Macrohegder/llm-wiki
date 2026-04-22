---
id: strategy-repro-crypto-trend-combo
title: "Strategy Repro: Catching Crypto Trends (Donchian + Volatility Targeting)"
source: "Zarattini et al. (2025) — Catching Crypto Trends"
url: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5204575
reproduced_at: 2026-04-22
status: completed
rating: green
---

# Catching Crypto Trends — 策略复现报告

## 原文摘要

> We propose a simple, long-only trend-following strategy based on Donchian Channel breakouts with volatility targeting and trailing stops on cryptocurrency markets.

Zarattini et al. (2025) 提出了一个简单的长线跟踪策略，基于 Donchian 通道突破入场，配合波动率目标调仓和 Donchian 中点跟踪止损。本文将其简化为单一模型（原文使用9个 Donchian 通道组成集成）。

## 复现方法

| 项目 | 设置 |
|------|------|
| 标的 | SPY, GLD, ETHUSDT_SWAP |
| 回测区间 | 2019-01-01 ~ 2025-12-31 |
| 资金 | $100,000 |
| 优化方法 | OAT + GA |
| 优化目标 | Sharpe Ratio |

## 关键修复: 合约乘数问题

**问题**: 原始策略代码假设 1 手 = 1 单位，但加密货永续合约的 size 与 ETF 完全不同：
- SPY/GLD (US ETF): `size=1` (1 手 = 1 股)
- BTCUSDT_SWAP: `size=0.01` (1 手 = 0.01 BTC)
- ETHUSDT_SWAP: `size=0.1` (1 手 = 0.1 ETH)

未考虑 size 导致 crypto 回测时实际名义价值与预期相差数十倍，回测结果失真（max_dd=-1261%）。

**修复**: 在策略中添加 `_detect_contract_size()` 方法，根据 `vt_symbol` 自动识别合约乘数，仓位计算改为：
```python
contracts = notional / (price * contract_size)
```

## 最优参数

| 参数 | SPY | GLD | ETH |
|------|-----|-----|-----|
| `donchian_window` | 22 | 36 | 31 |
| `vol_lookback` | 127 | 31 | 47 |
| `target_vol` | 0.366 | 0.084 | 0.377 |
| `max_leverage` | 1.12 | 1.18 | 1.42 |

## 回测结果

| 指标 | SPY | GLD | ETH |
|------|-----|-----|-----|
| **Sharpe Ratio** | **0.719** | **1.262** | **1.577** |
| 交易次数 | 76 | 44 | 80 |
| 最大回撤 | -9.17% | -5.28% | -10.59% |
| 年化收益 | 7.93% | 8.54% | 47.78% |
| 总收益 | 55.15% | 49.25% | 291.11% |

## 结论

- 评级：**GREEN** ✅ ─ 三个品种 Sharpe 均 > 0.7，ETH Sharpe 达 1.58 表现优异
- **GLD 表现最稳健**: Sharpe 1.26 且最大回撤仅 -5.28%
- **ETH 收益最高**: 年化 47.78%，但波动更大，回撤 -10.59%
- **SPY 较为保守**: Sharpe 0.72，适合低风险偏好
- Donchian 窗口在 22~36 之间，显著短于传统 60 日，说明加密货/股票趋势需要更敏捷的入场
- 波动率目标在 0.08~0.38 之间差异很大，不同品种需要不同的风险配置

## 合约乘数配置参考

| 品种 | size | 意义 |
|--------|------|-------|
| SPY.SMART | 1.0 | 1 手 = 1 股 |
| GLD.SMART | 1.0 | 1 手 = 1 股 |
| BTCUSDT_SWAP | 0.01 | 1 手 = 0.01 BTC |
| ETHUSDT_SWAP | 0.1 | 1 手 = 0.1 ETH |

## 复现产物

- YAML: `strategies/inbox/crypto_trend_combo_20260422.yaml`
- 代码: `generated/crypto_trend_combo_strategy.py` (FIXED)
- 评估报告: `reports/crypto_trend_combo_fixed_summary.json`

## 复现状态

- **复现完成**: 2026-04-22 14:34
- **策略 ID**: `crypto_trend_combo_20260422`
- **评级汇总**: Green=3 | Yellow=0 | Red=0 | Total=3

- **最佳品种**: ETH (Sharpe=1.577)

### 各品种回测结果

| 品种 | 评级 | Sharpe | 交易次数 | 最大回撤 | 年化收益 | 总收益 |
|--------|-------|--------|----------|----------|----------|----------|
| ETHUSDT_SWAP | Green | 1.577 | 80 | -10.59% | 47.78% | 291.11% |
| GLD.SMART | Green | 1.262 | 44 | -5.28% | 8.54% | 49.25% |
| SPY.SMART | Green | 0.719 | 76 | -9.17% | 7.93% | 55.15% |

### 最优参数 (最佳品种 ETH)

| 参数 | 最优值 |
|--------|--------|
| donchian_window | 31 |
| vol_lookback | 47 |
| target_vol | 0.377 |
| max_leverage | 1.42 |

*评估报告*: `crypto_trend_combo_fixed_summary.json`
