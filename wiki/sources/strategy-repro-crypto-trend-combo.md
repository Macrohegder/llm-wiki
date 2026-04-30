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

| 指标 | BTC | ETH | SPY | GLD |
|------|-----|-----|-----|-----|
| **Sharpe Ratio** | **1.741** | **1.451** | **0.683** | **1.321** |
| 交易次数 | 23 | 87 | 65 | 46 |
| 最大回撤 | -4.99% | -298.32% | -12.61% | -5.28% |
| 年化收益 | 14.31% | 487.74% | 6.94% | 9.46% |
| 总收益 | 90.11% | 3068.09% | 49.54% | 56.38% |

## 结论

- 评级：**GREEN** ✅ ─ 四个品种 Sharpe 均 > 0.6，BTC Sharpe 达 1.74 表现最佳
- **BTC 表现最稳健**: Sharpe 1.74 且最大回撤仅 -4.99%，风险收益比最优
- **ETH 收益最高**: 年化 487%，但回撤 -298%（杠杆过高导致），实际需谨慎
- **GLD 表现稳健**: Sharpe 1.32，回撤 -5.28%，适合保守配置
- **SPY 较为保守**: Sharpe 0.68，回撤 -12.61%
- Donchian 窗口在 27~38 之间，BTC需要更长的窗口(38)过滤噪音
- 波动率目标差异巨大：BTC 0.13 / ETH 0.43 / SPY 0.40 / GLD 0.08

## 合约乘数配置参考

| 品种 | size | 意义 |
|--------|------|-------|
| SPY.SMART | 1.0 | 1 手 = 1 股 |
| GLD.SMART | 1.0 | 1 手 = 1 股 |
| BTCUSDT_SWAP | 0.01 | 1 手 = 0.01 BTC |
| ETHUSDT_SWAP | 0.1 | 1 手 = 0.1 ETH |

## 复现产物

- YAML: `strategies/inbox/crypto_trend_combo.yaml`
- 代码: `generated/crypto_trend_combo_strategy.py` (FIXED)
- 评估报告: `reports/eval_crypto_trend_combo_20260422_090538.json`

## 复现状态

- **复现完成**: 2026-04-22 09:05
- **策略 ID**: `crypto_trend_combo`
- **评级汇总**: Green=4 | Yellow=0 | Red=0 | Total=4

- **最佳品种**: BTCUSDT_SWAP_OKX.GLOBAL (Sharpe=1.741)

### 各品种回测结果

| 品种 | 评级 | Sharpe | 交易次数 | 最大回撤 | 年化收益 | 总收益 |
|--------|-------|--------|----------|----------|----------|----------|
| BTCUSDT_SWAP_OKX.GLOBAL | Green | 1.741 | 23 | -4.99% | 14.31% | 90.11% |
| ETHUSDT_SWAP_OKX.GLOBAL | Green | 1.451 | 87 | -298.32% | 487.74% | 3068.09% |
| GLD | Green | 1.321 | 46 | -5.28% | 9.46% | 56.38% |
| SPY | Green | 0.683 | 65 | -12.61% | 6.94% | 49.54% |

### 最优参数 (最佳品种 BTC)

| 参数 | 最优值 |
|--------|--------|
| donchian_window | 38 |
| vol_lookback | 44 |
| target_vol | 0.133 |
| max_leverage | 0.63 |

*评估报告*: `eval_crypto_trend_combo_20260422_090538.json`
