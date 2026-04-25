---
tags:
  - concept
aliases:
  - "Williams Percent R"
  - "Williams R"
  - "%R"
related:
  - "[[concept:Mean Reversion]]"
  - "[[concept:RSI (Relative Strength Index)]]"
---

# Williams %R

> 类型：#concept | 相关：[[strategy:Williams %R 5-Day Oversold (QQQ)]]

---

## 定义
Williams %R 是 Larry Williams 开发的动量指标，测量收盘价在过去 N 日高低区间中的位置，取值 -100 到 0。接近 -100 表示超卖，接近 0 表示超买。

## 数学表达
$$
\%R = rac{H_n - C}{H_n - L_n} 	imes (-100)
$$
其中 $H_n$=n 日最高价，$L_n$=n 日最低价，C=当日收盘价

## 应用场景
- 适用策略类型：均值回归（尤其适合短期超卖信号）
- 常见误区：在趋势市场中，%R 可能长期停留在极端区域
- 与其他概念的区别：[[concept:RSI (Relative Strength Index)]] — 同源不同形，数值区间和解读方向相反

## 关键参数
| 回望周期 | 特点 | 常用阈值 |
|------|------|---------|
| 5 日 | 极端敏感 | <-90 买入 |
| 10 日 | 中等 | <-80 买入 |
| 14 日 | 标准 | <-20 超卖，>-20 超买（传统） |

## 参考资料
- [[source:Profitable Williams %R Strategy For Mean Reversion Trading (Only 2 Rules)]]
- 外部链接：Williams, L. (1979). *How I Made One Million Dollars Last Year Trading Commodities*

## 笔记历史
- 2026-04-18 创建
