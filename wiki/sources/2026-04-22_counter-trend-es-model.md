---
title: "From the Lab: A Counter Trend ES Model That Buys Panic and Sells Euphoria"
source: "Alpha Algo Trading Research"
author: "Alpha Algo"
source_url: "https://algotr.substack.com/p/from-the-lab-a-counter-trend-es-model"
created: 2026-04-22
tags:
  - es
  - counter-trend
  - intraday
  - mean-reversion
  - atr
  - sma200
rating: 3
rating_notes: "日线简化版 Sharpe 0.57，仅4年数据验证，原文15分钟级应有更好表现"
---

# From the Lab: A Counter Trend ES Model

## 核心逻辑

在日线 SMA200 趋势背景下，做反趋势交易：

- **日线趋势向下**（close < SMA200）→ 在日线内部找 **做多** 信号
  - 当日收盘处于日线区间上40%（close position > 0.6）→ 买入
- **日线趋势向上**（close > SMA200）→ 在日线内部找 **做空** 信号
  - 当日收盘处于日线区间下40%（close position < 0.4）→ 卖出
- **离场**：硬止损（1x ATR）+ 追踪止损（3x ATR）

## 原文成绩（15分钟ES，1997-2026）

| 指标 | 值 |
|------|-----|
| 交易次数 | 1,482 |
| 净利 | $197,087.50 |
| Profit Factor | 1.64 |
| 胜率 | 48.99% |
| 平均每笔 | $132.99 |
| Max DD（闭仓） | $8,437.50 |
| Ret/DD | 2,335.85% |
| 回测时长 | 28.5年 |
| 市场时间 | 2.10% |

## vnpy 回测结果（日线，ES 2022-04~2026-04）

| 指标 | 值 |
|------|-----|
| Sharpe Ratio | 0.57 |
| EWM Sharpe | 1.25 |
| 总收益率 | 43.06% |
| 年化 | 10.58% |
| Max DD% | -17.75% |
| 交易次数 | 173 |
| 盈利天数 | 129 / 260 |
| 亏损天数 | 131 / 260 |

## 品种适用性

原文测试了 NQ、YM 也很稳定。策略核心逻辑（SMA200 + 反趋势位置入场）应适用于大部分股指期货。

## 关键参数

| 参数 | 默认值 | 说明 |
|------|--------|------|
| sma_period | 200 | 日线趋势判断周期 |
| atr_period | 14 | ATR 计算周期 |
| atr_entry_mult | 1.5 | 入场距离（ATR倍数） |
| atr_stop_mult | 1.0 | 硬止损距离 |
| trail_atr_mult | 3.0 | 追踪止损距离 |

## 局限

- 日线级别简化版无法复现原文15分钟级的精细入场（stop order、intraday exhaustion 确认）
- 只有4年数据（vs 原文30年）
- 双向交易，有多次连续亏损
