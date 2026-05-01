# PivotShift NQ 策略 — Rogue Quant

**来源**: https://roguequant.substack.com/p/this-nasdaq-strategy-has-a-75-win
**作者**: The Rogue Quant
**日期**: 2026-04-30
**订阅状态**: 付费文章（免费预览仅展示部分规则）
**标签**: #量化策略 #技术分析 #PivotShift #QQQ #日线 #均值回归

## 一句话摘要

基于 Pivot High 结构压缩（lower high）的 QQQ 日线均值回归策略，付费文章声称 75% 胜率、1.65 Profit Factor、19 年 152 笔交易。

## 已知规则（免费预览部分）

### 入场条件
1. **确认 Pivot High**: 价格形成局部高点（confirmed pivot high）
2. **结构压缩**: 该 pivot high **未能突破**（fails to clear）最近的 prior pivot low → 形成 lower high，表明上涨动能减弱/结构压缩
3. **12 月过滤器**: 12 月份禁止开新仓（December = no new positions）

### 出场条件
- **Clean Breakout**: 当价格 cleanly breaks out of a recent range 时平仓

### 关键参数（⚠️ 付费墙遮挡 — 以下为合理假设）

| 参数 | 假设值 | 来源 |
|------|--------|------|
| pivot_lookback | 5 | 确认局部高点的回看根数 |
| compression_lag | 10 | 与 prior pivot 的距离 |
| breakout_window | 20 | 突破判断的近期范围 |

### 原文声称绩效

| 指标 | 值 |
|------|-----|
| 胜率 | 75% |
| Profit Factor | 1.65 |
| 总交易数 | 152 笔 |
| 时间跨度 | 19 年 |

## 复现状态

**状态**: 🟡 部分复现（参数假设）

### 复现结果（QQQ.SMART, 2015-12-31 ~ 2026-04-24）

| 指标 | 原文 | 复现 | 差异 |
|------|------|------|------|
| 交易数 | 152 / 19年 | 94 / ~10年 | 比例接近 |
| Sharpe | 未披露 | 0.37 | — |
| 年化回报 | 未披露 | 2.6% | — |
| 最大回撤 | 未披露 | 16.2% | — |
| 胜率 | 75% | 待计算 | — |
| Profit Factor | 1.65 | 待计算 | — |

### 关键差异与不确定性
1. **参数未知**: pivot lookback、compression lag、breakout window 均为假设
2. **"clear" 定义模糊**: 原文 "fails to clear a recent prior pivot low" 语法有歧义，复现采用 "lower high" 解释
3. **数据长度**: 实际可用数据 ~10 年（2015-12 起），非原文 19 年
4. **品种差异**: 原文可能用 NQ 期货，复现用 QQQ ETF

## 策略代码

- 文件: `strategy_factory/generated/pivotshift_nq.py`
- 类名: `PivotShiftNQStrategy`
- 架构: Factor-Signal-Execution 三层 + 中文 Log

## 相关实体
- [[The Rogue Quant]]
- [[QQQ]]
- [[Pivot Shift]]

## 相关概念
- [[结构压缩]]
- [[Lower High]]
- [[均值回归策略]]
- [[日线策略]]

---

*录入: 2026-05-01*
*复现工具: strategy_factory + vnpy BacktestingEngine*
