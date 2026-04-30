---
date: "2026-04-27"
author: "Quantified Strategies"
source: "quantifiedstrategies"
url: "https://quantifiedstrategies.substack.com/p/larry-connors-b-strategy-a-simple"
status: "ready-for-reproduction"
concrete_score: 75
tags:
  - strategy/mean-reversion
  - asset/equity
  - indicator/Bollinger-Bands
  - indicator/percent-b
---

# Larry Connors %B Strategy

> 来源：[https://quantifiedstrategies.substack.com/p/larry-connors-b-strategy-a-simple](https://quantifiedstrategies.substack.com/p/larry-connors-b-strategy-a-simple) | 摄入日期：2026-04-27

---

## 核心观点

Larry Connors 的 %B 策略是一种**简单的均值回归策略**，利用 Bollinger Bands 的 %B 指标识别短期超卖机会。%B 将价格相对于布林带的位置归一化为 0-1 值：>1 表示突破上轨，<0 表示跌破下轨。策略在上升趋势中的极端超卖时刻（%B < 0）入场，捕捉短期反弹。

---

## 策略规则

| 维度 | 描述 |
|------|------|
| **趋势过滤** | 价格高于 200 日移动平均线（长期上升趋势） |
| **入场条件** | %B 跌破 0（价格低于下轨，超卖） |
| **出场条件** | 快速反弹后出场（通常几天内） |
| **止损设置** | 原文未明确 |
| **仓位管理** | 原文未明确 |
| **时间框架** | 日线 |
| **适用品种** | 股票（SPY/S&P 500），均值回归主要在股票市场有效 |
| **交易方向** | 仅做多 |

---

## 回测数据（原文）

| 指标 | 数值 |
|------|------|
| 交易次数 (1993-至今) | 63 |
| 平均单笔收益 | 1.3% |
| 市场暴露时间 | 4% |
| 胜率 | 未明确，但"many winners and occasionally a nasty loser" |

---

## 关键洞察

1. **均值回归适用于股票** — 作者明确指出均值回归主要在股票市场有效，其他资产类别效果不佳
2. **信号稀疏** — 63 笔交易跨越 30+ 年，平均每年仅约 2 笔信号
3. **高单笔收益** — 1.3% 平均收益对于短期交易相当可观
4. **恐惧与贪婪创造短期低效** — 行为金融学基础

---

## 复现建议

- **品种**: SPY, QQQ, 其他主要股票 ETF
- **参数**: bb_period=20, bb_std=2, trend_ma_period=200
- **注意**: 原文提到 "Exit after a quick recovery (often within a few days)"，需要定义具体的出场规则（如 %B 回到 0.5、持有 N 天、或固定止盈）
- **风险提示**: "many winners and occasionally a nasty loser" — 需要严格止损防止大亏

---

## 提取的实体
- [[entity: Larry Connors]] — 短线交易专家，均值回归策略先驱

## 提取的概念
- [[concept: Percent B (%B)]] — Bollinger Bands 的归一化指标
- [[concept: Mean Reversion]] — 价格向均值回归的假设
- [[concept: Bollinger Bands]] — 基于标准差的波动率通道

## 个人批注
- concrete_score 75，规则基本完整但出场条件模糊。
- 63 笔交易/30 年 = 信号极其稀疏，可能不适合作为核心策略，但可作为组合中的卫星策略。
- 建议复现时测试不同出场规则（固定持有期 vs %B 阈值 vs 固定止盈）。

## 原文备份
详见 raw/articles/quantifiedstrategies-2026-04-27-Larry-Connors-pctB-Strategy.md
