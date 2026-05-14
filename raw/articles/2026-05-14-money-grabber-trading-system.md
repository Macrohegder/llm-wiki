---
name: Money Grabber Trading System
source: https://mp.weixin.qq.com/s/3xOEr0xW4ezYy9X7nAGaEw
type: CTA_RULE_BASED
timeframe: 1d
status: active
tags: [mean-reversion, atr-channel, adx, swing]
author: Raymond Hsiao (replicated)
alias: MG
---

# Money Grabber Trading System

## 策略概述

基于 ATR 波动通道的**确认后均值回归**策略。不做立刻抄底摸顶，而是等待价格反向运行确认后再进场。

**核心思想**: 价格突破 ATR 通道 → 标记方向 → 等待反向确认 → 进场 → ADX 动态止盈

## 指标定义

- `MidK` = MA(Close, 5)
- `TopK` = MidK + ATR(10) × channel_mult_top
- `BottomK` = MidK - ATR(10) × channel_mult_bottom
- `ADX` = ADX(14)
- `RSI` = RSI(MA(Close, 25), 10)

## 交易规则

### 1. Setup（突破标记）
- 价格跌破 BottomK → BrkFlags = 1（准备做多），记录 BrkPoint = High
- 价格突破 TopK → BrkFlags = -1（准备做空），记录 BrkPoint = Low
- 5 根 K 线内未触发则重置

### 2. 确认进场（Stop Order）
- **做多**: BrkFlags = 1 + High ≥ Lowest(Low, 5) + ATR × 1.75 + RSI ≥ 5
- **做空**: BrkFlags = -1 + Low ≤ Highest(High, 5) - ATR × 1.25（有 Value1 修正）

### 3. 动态止盈（Limit Order，按 ADX 分段）
| ADX | 多头止盈 | 空头止盈 |
|-----|---------|---------|
| ≤ 20（弱趋势）| Entry + ATR × 2.5 | Entry - ATR × 3.0 |
| 20-30（中等）| Entry + ATR × 3.5 | Entry - ATR × 1.0 |
| > 30（强趋势）| Entry + ATR × 0.5 | Entry - ATR × 1.0 |

### 4. 保护性止损（Stop Order）
- 多头: MaxClose > Entry + 1.5×ATR 后，止损移到 Entry + 4.0
- 空头: MinClose < Entry - 2.0×ATR 后，止损移到 Entry - 2.0

## 回测结果

### QQQ (2020-2025) — 最佳参数
```
channel_mult_top: 0.8
channel_mult_bottom: 0.64
adx_weak_threshold: 20
adx_strong_threshold: 40
use_long_only: True
```

| 指标 | 数值 |
|------|------|
| 交易数 | 49 |
| Sharpe | **1.185** |
| 总回报 | **3.09%** |
| 年化收益 | 0.62% |
| 最大回撤 | **-0.36%** |
| EWM Sharpe | 1.67 |

### SPY (2020-2025) — 默认参数
| 指标 | 数值 |
|------|------|
| 交易数 | 73 |
| Sharpe | 0.607 |
| 总回报 | 2.00% |
| 最大回撤 | -1.14% |

### 关键发现
1. **只做多 >> 多空双向** — 长期牛市中做空是负期望
2. **QQQ > SPY** — 科技股波动更大，均值回归空间更足
3. **回撤控制极佳** — QQQ 最大回撤仅 0.36%
4. **收益偏低** — 交易频率不高（~10笔/年），单笔利润有限

## 适用场景

✅ **适合**: 震荡市、来回波动、假突破较多的行情
❌ **不适合**: 单边暴涨/暴跌、强趋势连续行情

## 参数说明

| 参数 | 默认 | 说明 |
|------|------|------|
| atr_period | 10 | ATR 周期 |
| adx_period | 14 | ADX 周期 |
| midk_period | 5 | 中轨 MA 周期 |
| channel_mult_top | 1.5 | 上轨 ATR 倍数 |
| channel_mult_bottom | 1.25 | 下轨 ATR 倍数 |
| entry_atr_mult_long | 1.75 | 做多入场 ATR 倍数 |
| entry_atr_mult_short | 1.25 | 做空入场 ATR 倍数 |
| setup_timeout | 5 | Setup 超时（根 K 线）|
| adx_weak_threshold | 20 | ADX 弱趋势阈值 |
| adx_strong_threshold | 30 | ADX 强趋势阈值 |
| profit_mult_weak_long | 2.5 | 弱趋势多头止盈倍数 |
| profit_mult_medium_long | 3.5 | 中等趋势多头止盈倍数 |
| profit_mult_strong_long | 0.5 | 强趋势多头止盈倍数 |
| protect_atr_mult_long | 1.5 | 保护止损触发 ATR 倍数 |
| protect_stop_offset_long | 4.0 | 保护止损偏移 |
| use_long_only | False | 只做多 |

## 代码位置

- 策略代码: `cta/strategies/money_grabber_strategy.py`
- 别名: `MG` / `MONEYGRABBER` / `MoneyGrabber`
- 注册: `pipeline.py` STRATEGY_MAP
