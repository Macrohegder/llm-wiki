---
id: kama-atr-rty-trend
status: reproduced
reproduction_id: strategy-repro-kama-atr-rty-20260430
source: Alpha Algo Trading Research
title: "From the Lab: A Day Trading Trend Model for RTY"
url: "https://alphaalgotradingresearch.substack.com/p/from-the-lab-a-day-trading-trend-model-for-rty"
paywall: true
created: 2025-07-01
reproduced: 2026-04-30
---

# From the Lab: A Day Trading Trend Model for RTY

## 原文信息

- **来源**: Alpha Algo Trading Research
- **标题**: From the Lab: A Day Trading Trend Model for RTY
- **URL**: https://alphaalgotradingresearch.substack.com/p/from-the-lab-a-day-trading-trend-model-for-rty
- **发布时间**: 2025-07-01
- **类型**: 付费文章

## 策略概述

KAMA（Kaufman Adaptive Moving Average）+ ATR 趋势跟踪策略，专为 RTY（Russell 2000 期货）设计的日内趋势模型。

### 核心逻辑

1. **趋势判断**: KAMA 方向确定趋势
2. **入场触发**: 价格突破 KAMA + ATR 倍数确认
3. **止损**: ATR 硬止损
4. **跟踪止损**: ATR 动态跟踪
5. **日内平仓**: 15:00 ET 强制平仓

### 原文参数（推断）

| 参数 | 推断值 |
|------|--------|
| KAMA 周期 | 10 (fast=2, slow=30) |
| ATR 周期 | 14 |
| ATR 入场倍数 | 1.5x |
| ATR 硬止损 | 2.0x |
| ATR 跟踪止损 | 3.0x |

## 复现状态

- **状态**: ✅ 已复现
- **复现日期**: 2026-04-30
- **复现报告**: [[strategy-repro-kama-atr-rty-20260430]]
- **数据周期**: 1 分钟 → BarGenerator 合成 15 分钟
- **数据范围**: 2024-06-04 ~ 2025-12-16 (RTY.CME)

### 复现结果

| 品种 | 评级 | Sharpe | 交易次数 | 最大回撤 | 年化收益 |
|------|------|--------|---------|---------|---------|
| RTY.CME | 🟢 Green | 1.78 | 206 | -4.78% | 36.6% |

### 优化后参数

| 参数 | 优化值 |
|------|--------|
| KAMA 周期 | 9 |
| KAMA fast | 1 |
| KAMA slow | 18 |
| ATR 周期 | 5 |
| ATR 入场倍数 | 2.54 |
| ATR 硬止损 | 3.07 |
| ATR 跟踪止损 | 5.85 |

## 多品种扩展测试

见复现报告 [[strategy-repro-kama-atr-rty-20260430]] 中的多品种结果。

## 标签

#strategy #trend-following #intraday #KAMA #ATR #RTY #futures #paid-article
