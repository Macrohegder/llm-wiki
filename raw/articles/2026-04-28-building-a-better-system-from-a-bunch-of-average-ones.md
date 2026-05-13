---
id: bensdorp-7-systems-meta-strategy
title: "Building a Better System From a Bunch of Average Ones"
author: Dave Johnson
source: Trading Time Machine (Substack)
url: https://backtest.substack.com/p/building-a-better-system-from-a-bunch
date: 2026-04-28
tags: [portfolio-construction, strategy-ensemble, correlation, trend-following, mean-reversion, bensdorp]
status: concept-framework
---

# Building a Better System From a Bunch of Average Ones

> 原文作者: Dave Johnson (Trading Time Machine)  
> 发表日期: 2026-04-28  
> 来源: [Substack](https://backtest.substack.com/p/building-a-better-system-from-a-bunch)

## 核心观点

**"你不需要伟大的系统，你需要的是不相关的系统。"**

系统交易中最被低估的理念之一：组合中单个策略的表现并不重要，重要的是它们之间的相关性。

## 背景

WealthLab 社区成员 **DrKoch**（Finantic indicators 扩展开发者）实现了 Laurens Bensdorp 著作《Automated Stock Trading Systems》中的全部 **7 个交易系统**，并将它们组合成一个 Meta Strategy。

原讨论帖: [Laurens Bensdorp's Automated Stock Trading Systems - WealthLab Discussion](https://www.wealth-lab.com/Discussion/Laurens-Bensdorp-s-Automated-Stock-Trading-Systems-9377)

## 七个子系统

| # | 策略名称 | 类型 | 市场条件 |
|---|---------|------|---------|
| 1 | **Short RSI Thrust** | 均值回归(做空) | RSI 极端值 |
| 2 | **Short Mean Reversion High Six Day Surge** | 均值回归(做空) | 抛物线上涨后 |
| 3 | **Long Trend Low Volatility** | 趋势跟踪(做多) | 低波动环境 |
| 4 | **Long Trend High Momentum** | 趋势跟踪(做多) | 突破动量 |
| 5 | **Long Mean Reversion Selloff** | 均值回归(做多) | 急跌超卖 |
| 6 | **Long Mean Reversion High ADX Reversal** | 均值回归(做多) | ADX 确认反转 |
| 7 | **Catastrophe Hedge** | 对冲(做空偏置) | 市场错位/危机 |

覆盖: 多空双向 + 趋势/均值回归 + 平静/波动市场

每个策略都有**差异化条件**(differentiator condition)，确保行为互不相同。

## Meta Strategy 组合效果

**等权组合绩效**:
- **APR**: 16.70%
- **Max Drawdown**: 8.22%
- **Sharpe Ratio**: 2.12

**关键洞察**:
- Catastrophe Hedge 单独看是负收益（牛市中持续亏损），但组合中不可或缺
- Mean Reversion Selloff 多年横盘，但在趋势策略失效时提供收益
- **没有单个策略能接近组合的风险调整后收益**

## 相关性矩阵

七系统间相关性普遍较低。这不是七个相同赌注的不同版本，而是七个真正不同的赌注：

- 趋势策略在牛市中奔跑时，Catastrophe Hedge 在流血（设计如此）
- 趋势策略在震荡市中停滞时，均值回归策略在打印交易
- 看似死重的系统，在整体组合中做着看不见的工作

## 样本外验证

DrKoch 用 **2022 年以后数据**测试（开发时故意排除的时段）。组合在 2022 年这个真正困难的环境中**依然有效**——这不是对特定历史窗口的曲线拟合。

## 核心原则

> **The portfolio is the strategy.**
>
> 组合本身就是策略。单个系统是组件，不相关性是架构。你要构建的权益曲线不是任何单个系统的输出，而是它们如何相互作用的输出。

## 实践启示

1. **孤立回测系统并选择最佳个体指标，你可能在优化错误的东西**
2. **一个 Sharpe  modest 但真正不相关的系统，比高绩效但 mirrors 现有组合的系统贡献更大**
3. **评估新系统的正确问题不是"这有用吗？"而是"当我把它加入现有组合后，整体看起来像什么？"**

## 缺失信息（待补充）

本文是**概念框架/评论文章**，缺少具体可执行参数：

- [ ] RSI 周期参数
- [ ] ADX 阈值
- [ ] 六日 surge 计算方式
- [ ] 入场/出场精确规则
- [ ] 止损/止盈规则
- [ ] 流动性过滤器细节
- [ ] 再平衡频率
- [ ] 交易成本假设

**获取路径**: 需获取 Bensdorp 原书《Automated Stock Trading Systems》或 WealthLab 论坛原帖的完整实现代码。

## 相关概念

- [[diversification]] — 分散化投资
- [[correlation-matrix]] — 相关性矩阵
- [[strategy-ensemble]] — 策略组合/集成
- [[trend-following]] — 趋势跟踪
- [[mean-reversion]] — 均值回归
- [[rebalancing-bonus]] — 再平衡奖金

## 参考策略骨架

基于现有策略库的近似映射：

| Bensdorp 系统 | 已有策略 | 相似度 |
|--------------|---------|--------|
| Short RSI Thrust | `RSI2MR` (short 逻辑扩展) | 高 |
| Long Trend Low Vol | `DAB` / `NR7` | 中 |
| Long Trend High Momentum | `DAB` (breakout) | 中 |
| Long MR Selloff | `RSI2MR` / `PullbackMR` | 高 |
| Long MR High ADX Rev | `StochasticMR` + ADX | 中 |
| Catastrophe Hedge | 需新建 (VIX/波动率做空) | 低 |

## 复现状态

- **状态**: 概念框架已归档，WealthLab 完整代码已提取，vnpy 组合策略已构建
- **七系统 C# 源码**: 已全部从 WealthLab 提取（Strategy ID 42-48）
- **vnpy 移植**: `cta/strategies/bensdorp_meta_strategy.py` — 七系统组合策略
- **已知限制**: 
  - 原策略设计为**美股全市场选股**（7000+ 股票），单品种回测信号稀疏
  - 流动性过滤器（日均成交额 $10M-$100M）在单品种上意义不大
  - 部分子系统依赖 SPY 趋势过滤，需外部数据接入
- **回测结果 (SPY, 2020-2025)**: Sharpe 0.53, 交易数 9, 总收益 2.3%
- **优先级**: 中 — 策略框架已就绪，建议用于**多品种组合**而非单品种
- **后续**: 接入多品种数据（ETF basket / 股票池）验证组合效果
