---
id: 2026-04-30-i-added-one-long-only-strategy-to
title: "I Added One Long-Only Strategy to My Portfolio — Net Profit Jumped $61,875 Without Increasing Drawdown"
author: "Alpha Algo Trading Research"
url: https://algotr.substack.com/p/i-added-one-long-only-strategy-to
source: "algotr.substack.com"
date: 2026-04-30
topics: ["connors", "%b", "mean-reversion", "bollinger-bands", "long-only", "pullback", "portfolio-construction"]
paywall: true
---

> ⚠️ **注意**：本文为付费文章，以下内容仅为免费预览部分。

# I Added One Long-Only Strategy to My Portfolio — Net Profit Jumped $61,875 Without Increasing Drawdown

**作者**: Alpha Algo Trading Research  
**日期**: 2026-04-30  
**来源**: https://algotr.substack.com/p/i-added-one-long-only-strategy-to  
**状态**: 付费文章预览

---

## 文章主旨

作者将 Larry Connors & Cesar Alvarez 2009 年《High Probability ETF Trading》中的 **%B Mean Reversion** 策略改为**纯做多版本**，加入现有的 Turnaround Tuesday 组合后：

- 组合净利润从 $272,827 → **$334,702** (+22.7%)
- Return/DD 从 16.82 → **20.64**
- **最大回撤不变** ($16,218)

## 策略来源

- **原始出处**: Larry Connors & Cesar Alvarez, *High Probability ETF Trading*, 2009
- **核心逻辑**: 在健康上升趋势中，捕捉价格被过度拉伸（stretched lower）后的反弹
- **方向**: 纯做多（long-only）
- **品种**: ES.D (E-mini S&P 500 futures daily bars)

## 独立回测结果（ES.D 日线）

| 指标 | 数值 |
|------|------|
| 净利润 | $61,875.00 |
| 交易次数 | 182 |
| 胜率 | 77.47% |
| 盈亏比 | 1.79 |
| 平均交易 | $339.97 |
| 最大回撤 | $29,137.50 |
| 资金占用时间 | 6.55% |
| 年化收益 | 1.73% |

## 组合效果（加入前后对比）

| | 原组合 (2策略) | 新组合 (3策略) |
|--|--------------|--------------|
| 净利润 | $272,827.25 | **$334,702.25** |
| 交易次数 | 439 | 621 |
| 胜率 | 56.72% | 62.8% |
| 盈亏比 | 2.26 | 2.14 |
| Return/DD | 16.82 | **20.64** |
| 最大回撤 | $16,218 | **$16,218** (不变) |
| 平均交易 | $621.47 | $538.97 |

## 策略间相关性

| 策略对 | 相关性 |
|--------|--------|
| %B Long Only vs V1 ES | -0.07 |
| %B Long Only vs V3 NQ | -0.08 |
| V1 ES vs V3 NQ | 0.27 |

## 关键论点

1. **2009 年出版 = 长期公开样本外测试**: 策略已被公开 17 年，市场有机会将其套利掉，但仍有效
2. **不同种类的均值回归**: Turnaround Tuesday 是日历驱动，%B 是拉伸驱动，触发逻辑不同
3. **纯做多的优势**: 股指均值回归在长端更干净，恐惧比贪婪更容易过度反应
4. **组合层面的判断**: 平均交易下降、盈亏比微降，但净利润和 Return/DD 提升，这才是真正的升级

## 未披露规则（Paywall 后内容）

文章在 "How the strategy works" 部分被截断，以下规则**未在免费部分披露**：
- %B 的具体阈值（如 %B < 0.2? 0.0?）
- 布林带周期参数
- 趋势过滤的具体条件（如 close > SMA200?）
- 出场规则（持有天数 / 目标价 / 止损）

## 复现策略

基于 Connors 2009 年原始 %B 策略的公开知识 + 文章中提到的 "long-only + trend-filtered pullback" 方向，可构建合理复现版本。原始 %B 策略典型参数：
- %B = (Close - Lower Band) / (Upper Band - Lower Band)
- 入场: %B < 阈值 (如 0.2 或 0.0) 且价格在上升趋势中
- 出场: 反弹后固定天数或 %B 回归中性

---
*付费文章完整内容需订阅 Alpha Algo Trading Research 后获取。*
