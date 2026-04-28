---
id: simple-trend-following-dual-stop
title: "Simple Trend Following with Dual Stop"
source: "Trading & Investing Strategies"
url: https://www.quantseeker.com/p/weekly-research-recap-bf1
article_date: 2026-01-13
process_date: 2026-04-28
tags: #strategy #trend-following #moving-average #dual-stop #trailing-stop
rating: yellow
reproduced: true
reproduction_date: 2026-04-28
---

# Simple Trend Following with Dual Stop

## 一句话摘要

价格穿越移动平均线入场，双止损系统出场（固定止损 + 移动止损，取更紧者触发）。付费文章，核心参数缺失，经推断实现。

## 原文策略规则（已确认）

### 入场条件
- 价格 **上穿** 移动平均线 → 做多

### 出场条件（双止损系统）
1. **固定止损**：入场价下方固定百分比（如 1%）
2. **移动止损（Trailing Stop）**：随价格上涨而上移，回撤固定百分比触发
3. **实际出场**：两个止损中 **更紧的那个** 被触发时平仓
4. 补充：MA 反向穿越也可作为出场信号

### 缺失参数（付费墙内容）
- MA 周期（SMA/EMA？具体周期？）
- Trailing Stop 算法细节
- 固定止损具体百分比
- Pine Script 源码

## 推断实现参数

| 参数 | 推断依据 | OAT 优化范围 |
|------|----------|-------------|
| MA 类型 | SMA（最常见） | — |
| MA 周期 | 趋势跟踪常用 20-200 | 10-200 |
| 固定止损 | 原文提到 "1% below entry" | 0.5%-3% |
| 移动止损 | 常见 2%-5% 回撤 | 1%-5% |

## OAT 优化结果

| 品种 | 数据区间 | Sharpe | 年化收益 | 最大回撤 | 交易数 | 最优 MA | 固定止损 | 移动止损 |
|------|----------|--------|----------|----------|--------|---------|----------|----------|
| **SPY** | 2014-2025 | 0.72 | 2.78% | -6.57% | 293 | 26 | 1.06% | 3.25% |
| **QQQ** | 2015-2025 | **1.02** | **5.66%** | -4.37% | 263 | 33 | 1.30% | 2.19% |
| **IWM** | 2014-2025 | 0.17 | 0.39% | -6.46% | 560 | 62 | 0.70% | 1.79% |
| **GLD** | 2015-2025 | **1.01** | **2.93%** | -3.47% | 202 | 97 | 1.18% | 2.60% |

### 关键发现
- **QQQ** 和 **GLD** 表现优秀（Sharpe > 1.0，回撤 < 5%）
- **SPY** 中等可用（Sharpe 0.72）
- **IWM** 失效（Sharpe 0.17，560 笔交易仅赚 4.5%）
- MA 周期跨品种差异大：SPY 26 → QQQ 33 → IWM 62 → GLD 97
- 小盘股和趋势弱品种不友好
