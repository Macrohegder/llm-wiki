---
tags:
  - concept
aliases:
  - "IBS"
  - "Internal Bar Strength"
  - "内部条强度"
related:
  - "[[concept:Mean Reversion]]"
  - "[[concept:RSI (Relative Strength Index)]]"
---

# IBS (Internal Bar Strength)

> 类型：#concept | 相关：[[strategy:IBS+Bollinger Mean Reversion (XLP)]] [[strategy:IBS+RSI Classical Mean Reversion (S&P 500)]]

---

## 定义
IBS 是衡量 K 线在当日高低区间中位置的简单指标，取值 0 到 1。IBS 接近 0 表示收盘价接近当日最低价（超卖），接近 1 表示接近最高价（超买）。

## 数学表达
$$
IBS = rac{C - L}{H - L}
$$
其中 C=收盘价，L=当日最低价，H=当日最高价

## 应用场景
- 适用策略类型：均值回归、短线反弹信号
- 常见误区：单独使用 IBS 会产生较多虚假信号，常需与 RSI 或波动率带组合
- 与其他概念的区别：[[concept:RSI (Relative Strength Index)]] — IBS 只看当日，RSI 看多日动量

## 关键参数
| 应用 | IBS 阈值 | 说明 |
|------|---------|------|
| 经典均值回归 | < 0.25 | 收盘价接近当日最低，可能反弹 |
| IBS + 波动率带 | < 0.6 | 结合下轨道突破使用 |

## 参考资料
- [[source:3 Best Mean Reversion Strategies: Backtested Buy and Sell Signals Analysis]]
- [[source:S&P 500 Mean Reversion Using IBS and RSI: Classical Approach Analysis]]

## 笔记历史
- 2026-04-18 创建
