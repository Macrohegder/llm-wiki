---
tags:
  - concept
aliases:
  - "RSI"
  - "相对强弱指标"
related:
  - "[[concept:Mean Reversion]]"
  - "[[concept:IBS (Internal Bar Strength)]]"
---

# RSI (Relative Strength Index)

> 类型：#concept | 相关：[[strategy:RSI-2 Mean Reversion (SPY)]] [[strategy:IBS+RSI Classical Mean Reversion (S&P 500)]]

---

## 定义
RSI 是 J. Welles Wilder 于 1978 年提出的动量振荡指标，测量价格变动的速度和幅度，通常在 0-100 之间波动。经典用法是 14 周期，但在短期均值回归中，2 周期 RSI 效果显著。

## 数学表达
$$
RSI = 100 - rac{100}{1 + RS}
$$
其中 $RS = rac{平均上涨幅度}{平均下跌幅度}$

## 应用场景
- 适用策略类型：均值回归（短周期）、超买超卖判断（传统）
- 常见误区：在强趋势中使用固定 70/30 阈值会错过行情
- 与其他概念的区别：[[concept:Williams %R]] — 同样测量超买超卖，但计算方式不同

## 关键参数对比
| 周期 | 特点 | 常见用法 |
|------|------|---------|
| RSI(2) | 极端敏感 | 均值回归（<10 买入，>80 卖出） |
| RSI(14) | 平滑 | 势头判断（>70 超买，<30 超卖） |
| RSI(21) | 中等 | 均值回归 + 势能过滤（<45 买入） |

## 参考资料
- [[source:RSI 2 Strategy Explained: Larry Connors' 2-Period RSI Trading Rules]]
- [[source:S&P 500 Mean Reversion Using IBS and RSI: Classical Approach Analysis]]
- 外部链接：Wilder, J.W. (1978). *New Concepts in Technical Trading Systems*

## 笔记历史
- 2026-04-18 创建
