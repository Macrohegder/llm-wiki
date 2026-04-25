---
tags:
  - concept
aliases:
  - "仓位管理"
  - "资金管理"
related:
  - "[[concept:Mean Reversion]]"
  - "[[concept:Risk Management]]"
---

# Position Sizing

> 类型：#concept | 相关：[[strategy:Williams %R 5-Day Oversold (QQQ)]] [[strategy:RSI-2 Mean Reversion (SPY)]]

---

## 定义
Position Sizing 是指每次交易分配多少资金到单个策略/信号的决策过程。好的仓位管理比策略选择本身更重要，它决定了策略在实战中能否存活下来。

## 应用场景
- 适用策略类型：所有策略，尤其是高回撤策略
- 常见误区：固定仓位（10%、20%）而非根据策略特性动态调整
- 与其他概念的区别：[[concept:Risk Management]] — Position Sizing 是 Risk Management 的子集

## 关键方法
| 方法 | 说明 | 适用场景 |
|------|------|---------|
| 固定比例 | 每次投入资金的 X% | 简单但忽略策略风险差异 |
| Kelly Criterion | 基于胜率和盈亏比计算最优仓位 | 理论最优，实战中通常用 Half-Kelly |
| ATR 仓位 | 根据波动率调整仓位 | 跟踪策略常用 |
| 分散投资 | 同时运行多个低相关策略 | 均值回归策略必备 |

## 参考资料
- [[source:Profitable Williams %R Strategy For Mean Reversion Trading (Only 2 Rules)]]
- [[source:RSI 2 Strategy Explained: Larry Connors' 2-Period RSI Trading Rules]]

## 笔记历史
- 2026-04-18 创建
