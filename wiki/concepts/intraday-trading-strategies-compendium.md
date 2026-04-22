---
id: intraday-trading-strategies-compendium
title: "日内交易策略汇编 (Intraday Trading Strategies Compendium)"
date: "2026-04-22"
tags:
  - concept/intraday-trading
  - concept/day-trading
  - concept/market-microstructure
  - synthesis
---

# 日内交易策略汇编

> 本页面汇总 llm-wiki 知识库中所有**日内策略 (Intraday/Day Trading)**文章的核心结论，按策略类型分类。

---

## 一、知识库内已收录的日内策略

| 策略名 | 来源 | 日期 | 类型 | 关键机制 | 回测表现 | 状态 |
|--------|------|------|------|----------|----------|------|
| **Session High Retest** | Delphic Alpha | 2026-04-22 | 突破/趋势 | 回撤深度过滤 + 品种分裂 | Portfolio Sharpe 1.15 | 深度处理 |
| **Systematic Intraday Trend-Following** | QuantifiedStrategies / Concretum | 2026-02-23 | 趋势 | 动态边界 + VWAP + 半小时执行 | SPY Sharpe 1.33，年化 19.6% | 深度处理 |
| **Simplest Intraday Momentum** | Trading & Investing Strategies | 2026-03-28 | 动量/新闻 | VWAP 控制 + StochRSI 时机 | 付费文章，规则不全 | 已录入 |
| **Effective Intraday Momentum (VSO)** | quantmacro 论文综述 | 2025-03-14 | 动量 | 波动率锥 (VolSinceOpen) + VWAP 止损 | SPY，胜率约 43% 但凸性高 | 已录入 |
| **Opening Range Breakout (ORB)** | QuantifiedStrategies | 2025-12-14 | 突破 | n 分钟后突破开盘区间 | 结论：ORB 已不好用 | 已录入 |
| **Late Lunch Intraday System** | Algomatic Trading | 2025-10-19 | 趋势 | 午后时段 + ATR 风险 | DAX40，胜率 55%，PF 1.19 | 已录入 |
| **Simple Intraday Signal** | QuantSeeker | 2026-02-08 | 信号 | OHLC 模式预测次日回报 | SPY 26 年，付费 | 已录入（预览） |

---

## 二、按策略类型分类

### 2.1 趋势类 (Trend-Following)

#### Session High Retest
- **核心**: 开盘涨→回撤→回测高点→突破延续
- **关键发现**: 品种分裂
  - 金属/NQ 适合**浅回撤** (≤ 38.2%)
  - 股指 (ES/FDAX/NKD/YM) 适合**深回撤** (≥ 50%)
- **持仓**: 长仅，持有至 RTH close
- **最佳品种**: FDAX (Sharpe 4.56, deep, 150 bps)
- 原文: [[2026-04-22-session-high-retest-intraday-strategy]]

#### Systematic Intraday Trend-Following
- **核心**: 动态边界根据日内波动率季节性调整
- **关键发现**: 10:30 时 -0.30% 即可触发，15:30 时需 -0.60%
- **持仓**: 双向，VWAP 止损，半小时执行
- **最佳环境**: VIX > 40 时 Sharpe 达 3.50
- 原文: [[2026-02-23-systematic-intraday-trend-following-strategy]]

#### Late Lunch System (DAX40)
- **核心**: 午后时段捕捉次级方向推动
- **关键发现**: 避开早盘噪音，利用欧盘向美盘流动性转移
- **持仓**: ATR 风险定位，无过夜风险
- 原文: raw/articles/2026-04-05-Strategy-10-The-Late-Lunch-Intraday-System-DAX40.md

### 2.2 动量/突破类 (Momentum/Breakout)

#### Effective Intraday Momentum (VSO)
- **核心**: VolSinceOpen 波动率锥，考虑日内波动率非均匀分布
- **关键发现**: 胜率仅约 43%，但凸性极高（平均赢利远大于平均亏损）
- **持仓**: 双向，VWAP 跟踪止损，EOD 平仓
- 原文: raw/articles/20250314-paper-review-effective-intraday-momentum.md

#### Opening Range Breakout (ORB)
- **核心**: 开盘 n 分钟后突破开盘区间
- **结论**: **ORB 已不好用** — 这是一个重要发现
- 原文: raw/articles/2026-04-04-OPENING-RANGE-BREAKOUT-STRATEGY-ORB-FOR-DAY-TRADING-5-MINUTE-BACKTEST-AND-SYSTEM.md

### 2.3 新闻/事件驱动类 (Event-Driven)

#### Simplest Intraday Momentum Strategy
- **核心**: VWAP 控制过滤 + StochRSI 时机
- **应用场景**: 新闻驱动的日内动量（收益、油价、政策公告）
- **关键**: 价格 > VWAP 表明机构买盘接力；StochRSI < 20 表明短期回撤
- 原文: raw/articles/2026-03-28-simplest-intraday-momentum-strategy.md

### 2.4 信号/预测类 (Signal/Predictive)

#### Simple Intraday Signal Predicts Next-Day Returns
- **核心**: 基于 OHLC 的日内信号预测次日回报
- **关键发现**: 对交易成本敏感，但在特定条件下可存活
- 原文: raw/articles/2026-02-08-a-simple-intraday-signal-that-predicts-next-day-returns.md

---

## 三、日内策略通用设计原则

### 3.1 时间窗口设计
- **开盘窗口** (9:30–10:00): 波动率最高，适合突破类策略
- **午间窗口** (11:00–14:00): 波动率最低，适合趋势继续/回撤
- **收盘窗口** (14:30–16:00): 波动率回升，适合趋势突破

### 3.2 过滤器设计
- **VWAP**: 机构控制标识（> VWAP 买方控制，< VWAP 卖方控制）
- **波动率过滤**: 高波动率环境通常表现更好（VIX > 20 或 > 40）
- **回撤深度**: 根据品种特性选择浅/深回撤（见 Session High Retest）
- **时间过滤**: 避开特定时段（如移动交易窗口 Orb 失效）

### 3.3 执行机制
- **执行频率**: 5min / 30min / 半小时 各有不同噪音特性
- **执行延迟**: 信号产生到实际执行的延迟会消耗 alpha（尤其是日内策略）
- **滑点**: 日内策略对滑点极敏感，回测必须考虑实际填单成本

### 3.4 风险管理
- **止损方法**: VWAP / 固定金额 / ATR 倍数 / 无止损持有至 close
- **仓位大小**: 动态仓位（基于当日波动率或 ATR），确保风险一致
- **过夜风险**: 日内策略的主要优势之一是无过夜风险

---

## 四、关键数据需求

| 数据类型 | 最小频率 | 用途 | 来源示例 |
|----------|----------|------|---------|
| 日内价格数据 | 5 分钟 | 突破/趋势检测 | RTH 期货数据、美股分钟数据 |
| VWAP | 实时 | 过滤器/止损 | 大多数交易平台提供 |
| 每日波动率 | 日线 | 仓位调整 | ATR(14) |
| VIX | 日线 | 环境过滤 | CBOE VIX |
| 历史日内模式 | 日线 | 动态边界 | 14 天回看 |

---

## 五、相关概念
- [[concept:intraday-strategy-design-checklist]] — 日内策略设计检查清单
- [[concept:market-microstructure]] — 市场微观结构
- [[concept:volatility-seasonality]] — 波动率季节性
- [[concept:VWAP-strategy]] — VWAP 策略应用

---

*Last updated: 2026-04-22*
