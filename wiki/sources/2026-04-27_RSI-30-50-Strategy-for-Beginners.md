---
date: "2026-04-27"
author: "Quantified Strategies"
source: "quantifiedstrategies"
url: "https://quantifiedstrategies.substack.com/p/rsi-30-50-strategy-for-beginners"
status: "ready-for-reproduction"
concrete_score: 85
tags:
  - strategy/mean-reversion
  - asset/equity
  - indicator/RSI
  - topic/pullback-trading
---

# RSI 30-50 Strategy for Beginners

> 来源：[https://quantifiedstrategies.substack.com/p/rsi-30-50-strategy-for-beginners](https://quantifiedstrategies.substack.com/p/rsi-30-50-strategy-for-beginners) | 摄入日期：2026-04-27

---

## 核心观点

RSI 30-50 策略是一种**趋势中的回调买入**方法。关键洞察：在上升趋势中，RSI 跌入 30-50 区间代表健康的回调而非趋势反转。与经典的 RSI 超买/超卖反转交易不同，此策略利用 RSI 作为**回调工具**，在趋势延续时入场。

---

## 策略规则

| 维度 | 描述 |
|------|------|
| **趋势过滤** | 价格高于上升的 200 日移动平均线 → 仅在此条件下交易 |
| **入场条件** | RSI(5) 跌破 30（表明市场正在回调） |
| **出场条件** | RSI 回升至 50 时卖出 |
| **止损设置** | 原文未明确，建议设置固定百分比或 ATR 止损 |
| **仓位管理** | 原文未明确，建议单次全仓或固定比例 |
| **时间框架** | 日线（原文使用日线回测） |
| **适用品种** | 股票（SPY/S&P 500），上升趋势品种 |
| **交易方向** | 仅做多（Long Only） |

---

## 回测数据（原文）

| 指标 | 数值 |
|------|------|
| 交易次数 | 196 |
| 平均单笔收益 | 0.9% |
| 胜率 | 81% |
| 盈亏比 (Profit Factor) | 3.0 |
| CAGR | 5.3% |
| 市场暴露时间 | 11% |
| 风险调整回报 | 44% (CAGR / 暴露时间) |
| 最大回撤 | -15% |

---

## 关键洞察

1. **资产选择 > 策略本身** — 作者强调选择正确的交易品种比策略规则更重要
2. **RSI 参数** — 使用 5 日 RSI（短周期更敏感，适合捕捉短期回调）
3. **趋势过滤是核心** — 只在上升趋势中操作，避免抄底下跌趋势
4. **高胜率低暴露** — 81% 胜率但仅 11% 时间在市场，说明信号稀疏但质量高

---

## 复现建议

- **品种**: SPY, QQQ, GLD, 其他主要 ETF
- **数据**: 日线数据足够
- **参数**: rsi_period=5, trend_ma_period=200, entry_threshold=30, exit_threshold=50
- **注意**: 原文未提供完整代码，出场规则"RSI reaches 50"需要明确定义是收盘突破还是盘中触及

---

## 提取的实体
- [[entity: Larry Connors]] — 短线均值回归交易先驱
- [[entity: MetaStock]] — 早期回测软件

## 提取的概念
- [[concept: RSI Pullback]] — 利用 RSI 识别趋势中的回调机会
- [[concept: Trend Filter]] — 用长期均线过滤交易方向
- [[concept: Risk-Adjusted Return]] — 考虑资金利用效率的回报指标

## 个人批注
- 策略规则简单明确，concrete_score 85。核心参数只有 RSI(5) + MA(200)。
- 风险：未明确止损规则，15% 最大回撤可能来自单次未止损的亏损。
- 建议复现时添加固定百分比止损（如 -3%）或 ATR 止损来改进风险管理。

## 原文备份
详见 raw/articles/quantifiedstrategies-2026-04-27-RSI-30-50-Strategy-for-Beginners.md
