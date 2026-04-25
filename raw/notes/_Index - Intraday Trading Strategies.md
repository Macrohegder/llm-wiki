---
title: "Intraday Trading Strategies 索引"
description: "Substack 日内交易策略文章汇总与核心笔记索引"
date: 2026-04-19
tags: [intraday, day-trading, index, substack, quantified-strategies]
---

# Intraday Trading Strategies 索引

**总来源**: Substack (QuantifiedStrategies / AlgomaticTrading / QuantSeeker)
**导入日期**: 2026-04-19
**原文存放**: `Sources/Substack/Intraday/`
**笔记存放**: `Notes/Trading/Intraday Strategies/`

---

## 一、含具体策略逻辑的策略 (12篇)

| 策略名称 | 来源 | 标的 | 策略类型 | 关键指标 | 笔记状态 |
|---------|------|------|---------|---------|---------|
| [[Crude Oil Day Trading Strategy]] | QuantifiedStrategies | WTI原油 (USO) | 日内动量 | 年1.85%，夏普更高 | ✅ 已提取 |
| [[Intraday Trading Strategies Backtest Results and Practical Examples]] | QuantifiedStrategies | WTI原油期货 | 趋势跟踪 | 小时线，10:30入场 | ✅ 已提取 |
| [[LONDON BREAKOUT STRATEGY RULES AND BACKTEST PERFORMANCE]] | QuantifiedStrategies | 外汇/欧洲股指 | 突破 | 伦敦03:00-08:00区间突破 | ✅ 已提取 |
| [[Reversal Day Strategy For The Markets]] | QuantifiedStrategies | GLD | 均值回归 | RSI<35，Profit Factor>1.8 | ✅ 已提取 |
| [[Systematic Intraday Trend-Following Strategy]] | QuantifiedStrategies | SPY | 动量/趋势 | 年19.6%，夏普1.33 | ✅ 已提取 |
| [[The End-of-Day Reversal Edge]] | QuantifiedStrategies | 美股 | 尾盘反转 | 15:30-16:00多空，超过大盘10倍 | ✅ 已提取 |
| [[Strategy #10 The Late Lunch Intraday System (DAX40)]] | AlgomaticTrading | DAX | 日内趋势 | 胜率55%，MAR 0.45 | ✅ 已提取 |
| [[Best Day Trading Strategies Proven Techniques and Insights]] | QuantifiedStrategies | Russell 2000 | 月末季节性 | 月末开盘做空 | ✅ 已提取 |
| [[OPENING RANGE BREAKOUT STRATEGY (ORB) FOR DAY TRADING (5-MINUTE BACKTEST AND SYS]] | QuantifiedStrategies | S&P 500 | 开盘突破 | 结论: 已失效 | ✅ 已提取 |
| [[SPY Sets Low or High in the Last Hour – An Intriguing Day Trading Strategy]] | QuantifiedStrategies | SPY | 均值回归 | 买弱卖强，11:30出场 | ✅ 已提取 |
| [[Overnight Edge in SPY A Simple Close-to-Close Strategy]] | QuantifiedStrategies | SPY | 隔夜/close-to-close | CAGR 5.8%，回撤16% | ✅ 已提取 |
| [[Percentage of Profitable Day Traders vs Losers]] | QuantifiedStrategies | 通用 | 统计研究 | 1%-20%盈利率 | ✅ 已提取 |

---

## 二、概念/综述/付费墙类文章 (24篇)

| 策略名称 | 来源 | 状态 | 说明 |
|---------|------|------|------|
| [[Best Time Frame in Trading Day Trading, Swing Trading, Trend Trading, and Positi]] | QuantifiedStrategies | 概念 | 时间框架对比 |
| [[Best Time Frame in Trading Day Trading, Swing Trading, Trend Trading and Positio]] | QuantifiedStrategies | 概念 | 时间框架对比 |
| [[Day Trading Price Action Strategy — An Overview and Backtest Insights]] | QuantifiedStrategies | 概念 | 价格行为策略概述 |
| [[Day Trading Price Action Strategy — Comprehensive Overview and Backtest Analysis]] | QuantifiedStrategies | 概念 | 价格行为策略概述 |
| [[Day Trading Price Action Strategy — Overview and Backtest Analysis]] | QuantifiedStrategies | 概念 | 价格行为策略概述 |
| [[Day Trading Price Action Strategy — Overview and Backtest]] | QuantifiedStrategies | 概念 | 价格行为策略概述 |
| [[Day Trading Price Action Strategy — What Is It (Backtest)]] | QuantifiedStrategies | 付费墙 | 无完整内容 |
| [[Intraday Trading Strategies — Backtests Analysis and Evaluation]] | QuantifiedStrategies | 概念 | 日内回测分析 |
| [[Intraday Trading Strategies – Backtests Analysis]] | QuantifiedStrategies | 概念 | 日内回测分析 |
| [[Intraday Trading Strategies (Backtests And Examples)]] | QuantifiedStrategies | 付费墙 | 无完整内容 |
| [[Is It Possible to Make Money Day Trading Personal Statistics And Profits — Real ]] | QuantifiedStrategies | 概念 | 个人统计 |
| [[Overnight Trading Strategies for Making Money and Insights]] | QuantifiedStrategies | 概念 | 隔夜策略概述 |
| [[A Simple Intraday Signal That Predicts Next-Day Returns]] | QuantSeeker | 付费墙 | 仅预览/OHLC信号 |

---

## 三、核心策略快速对比

### 按标的分类
- **SPY / S&P 500**: 系统化日内趋势跟踪、ORB、尾盘反转、隔夜边际、最后一小时均值回归
- **WTI原油**: 开盘半小时动量策略、连续K线趋势跟踪
- **GLD**: 反转日均值回归
- **DAX**: 午间趋势系统 (Late Lunch)
- **Russell 2000**: 月末季节性日内空头
- **外汇/欧洲股指**: 伦敦突破

### 按策略类型分类
| 类型 | 策略 |
|------|------|
| 动量/趋势 | 原油开盘半小时、SPY系统化趋势、Late Lunch DAX |
| 突破 | 伦敦突破、ORB (已失效) |
| 均值回归 | GLD反转日、SPY尾盘买弱卖强、End-of-Day反转 |
| 季节性 | Russell 2000月末空头 |
| 隔夜/close-to-close | SPY隔夜边际 |

---

## 四、重要结论与警示

1. **大多数日内策略对成本极敏感** — 佣金、滑点、价差会显著削弱回测收益
2. **ORB在S&P 500上已失效** — 过去广为人知的边际已经衰减
3. **日内交易者生存率极低** — 80%-99%交易者亏损，量化是提升存活率的关键
4. **滑点是日内策略的隐形杀手** — 尤其是高频策略，回测中常被忽略
5. **流动性决定可执行性** — 小盘股效果更好但难以扩展规模

---

*本索引由 Hermes Agent 自动生成。笔记文件后缀名可能因文件名长度被截断，建议使用 Obsidian 链接或搜索查找。*
