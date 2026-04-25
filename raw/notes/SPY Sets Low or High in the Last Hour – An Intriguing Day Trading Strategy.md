---
title: "SPY Sets Low or High in the Last Hour – An Intriguing Day Trading Strategy"
source_url: "https://quantifiedstrategies.substack.com/p/spy-sets-low-or-high-in-the-last"
pub_date: "Jul 05, 2024"
has_strategy_logic: false
strategy_score: 2
source_file: "Sources/Substack/Intraday/2026-04-04-SPY-Sets-Low-or-High-in-the-Last-Hour-An-Intriguing-Day-Trading-Strategy.md"
tags: [intraday, day-trading, substack]
---

# SPY Sets Low or High in the Last Hour – An Intriguing Day Trading Strategy

**来源**: [https://quantifiedstrategies.substack.com/p/spy-sets-low-or-high-in-the-last](https://quantifiedstrategies.substack.com/p/spy-sets-low-or-high-in-the-last)
**发布日期**: Jul 05, 2024
**是否含具体策略逻辑**: 否 (概念/综述类)
**原文**: [[2026-04-04-SPY-Sets-Low-or-High-in-the-Last-Hour-An-Intriguing-Day-Trading-Strategy.md]]

## 摘要

SPY Sets Low or High in the Last Hour – An Intriguing Day Trading Strategy
QuantifiedStrategies.com
Jul 05, 2024
1
Share
We try to find something tradeable out of these simple numbers but it’s not easy. However, the “boring” buying on weakness and selling on strength seems to work pretty well. Entry is at the open next day and exit is at 1130 the same day (only day trades). Buying on the close gives approximately the same results. However, drawdowns are a lot bigger. So using this approach you don’t get paid for holding overnight (from yesterday’s close).
The equity curve for all trades going long if low is in the last hour and going short if high is in the last hour looks like the image shown below.
1
Share
Previous
Next

## 核心策略笔记

**标的**: SPY
**策略类型**: 买弱卖强 / 日内均值回归

### 交易规则
1. 观察SPY当日最后一小时 (15:00-16:00 ET) 是否创当日新高/新低:
   - 若最后一小时创**当日低点** → 次日开盘 **做多**
   - 若最后一小时创**当日高点** → 次日开盘 **做空**
2. **出场**: 次日 **11:30** 平仓 (纯日内交易，不隔夜)

### 对比测试
- 若改为**收盘买入**而非次日开盘买入，结果近似但**回撤显著更大**
- **结论**: 从昨日收盘持有隔夜并无额外收益补偿，不值得承担隔夜风险

### 核心逻辑
- "低买高卖"的朴素版本在SPY上表现优于复杂筛选
- 尾盘弱势往往伴随次日早盘反弹 (均值回归)
- 尾盘强势往往伴随次日早盘回落
