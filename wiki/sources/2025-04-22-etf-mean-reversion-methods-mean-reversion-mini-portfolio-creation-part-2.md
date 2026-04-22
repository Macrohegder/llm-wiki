---
id: 2025-04-22-etf-mean-reversion-methods-mean-reversion-mini-portfolio-creation-part-2
title: "ETF Mean Reversion Methods: Mean Reversion Mini-Portfolio Creation - Part 2"
source: "TradeQuantix"
url: https://www.tradequantixnewsletter.com/p/etf-mean-reversion-methods-mean-reversion
date: "2025-04-22"
tags:
  - strategy/mean-reversion
  - asset/multi-asset
  - topic/portfolio-construction
  - topic/position-sizing
rating: green
status: ingested
---

# ETF Mean Reversion Methods: Mean Reversion Mini-Portfolio Creation - Part 2

> 来源: [TradeQuantix](https://www.tradequantixnewsletter.com/p/etf-mean-reversion-methods-mean-reversion) | 摄入日期: 2025-04-22

## 一句话摘要

四个普通的均值回归系统组合成一个 mini-portfolio，其风险调后收益远超任何单一系统。Portfolio Effect 是唯一圣杯。

## 核心观点

1. **四系统构成**:
   - **Z_Reversion**: Z-score 衡量超卖
   - **Vol_Reversion**: 波动率通道
   - **Vol_Reversion_2**: 与 Vol_Reversion 进出时机不同
   - **RSI_Reversion**: 预计算 RSI 入场水平，timing 机制不同

2. **Sub-entry 设计**:
   - 每个系统分 **3 次 sub-entry** 建仓
   - 每次 **1/3 等权**
   - 3 次是 80/20 甜蜜点：比 2 次更能平滑捕捉超卖，比 5 次更简单可执行

3. **交易宇宙**: 多资产 ETF 组合（股票、债券、黄金、比特币），类似"全天候组合"

4. **关键数据**:
   - 回撤相关性平均 **~0.34 或更低**
   - 收益相关性在 0.06~0.79 之间
   - 非杠杆 ETF 版本：2000 年以来（除 2000 年一次较大回撤外）**没有一年亏损**
   - 月回报热力图显示持续稳定的正回报流，非少数几个月贡献全部收益

5. **动态排名机制 (可选)**:
   - 按滚动 **1 年 Sharpe**（收益/年化日波动）对每条 equity curve 排名
   - 每季度更新排名
   - `ExcludeWorstX` 可屏蔽最差的 N 条 equity curve
   - 作者警告: 这是 **exposure 管理工具**，不是 performance optimizer，过度优化会引入多层过拟合

6. **组合哲学**:
   - 不仅跨资产、跨时间、跨价格，还要跨**思想/实现方式**
   - 单一系统回测再好也可能过拟合；组合真正低相关的系统才能分散风险
   - TMF(债券)近期表现差的例子：单个 sub-entry 可能在回撤，但组合后整体几乎不受影响

## 提取的实体
- [[entity:TradeQuantix]]

## 提取的概念
- [[concept:Portfolio Effect]]
- [[concept:Mean Reversion Mini-Portfolio]]
- [[concept:Sub-entry Scaling]]
- [[concept:Equity Curve Ranking]]
- [[concept:Diversification of Ideas]]

## 复现状态
- 待复现。Part 1 有四系统详细规则，Part 2 主要是组合逻辑。GitHub 代码对付赁读者开放。

## 评价

| 指标 | 评分 | 备注 |
|--------|-------|-------|
| 数据质量 | ⭐⭐⭐⭐☆ | 图表丰富，相关性矩阵透明 |
| 可操作性 | ⭐⭐⭐☆☆ | 代码在 GitHub，但需付费会员 |
| 新题性 | ⭐⭐⭐☆☆ | Portfolio effect 不是新概念，但实现细节实用 |
| 风险透明度 | ⭐⭐⭐⭐☆ | 明确讨论了过拟合风险、相关性、排名层风险 |

**总体**: 🟢 **Green** — 规则清晰、组合逻辑严谨、风险透明度高，值得参考。

## 原文备份
详见 raw/articles/2025-04-22-etf-mean-reversion-methods-mean-reversion-mini-portfolio-creation-part-2.md
