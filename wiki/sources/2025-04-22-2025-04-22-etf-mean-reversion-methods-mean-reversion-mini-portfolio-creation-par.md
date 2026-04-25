# 2025-04-22-etf-mean-reversion-methods-mean-reversion-mini-portfolio-creation-part-2

**Source**: [[2025-04-22-2025-04-22-etf-mean-reversion-methods-mean-reversion-mini-portfolio-creation-part-2]] | [TradeQuantiX]()
**Date**: 2025-04-22
**Tags**: #article #substack #mean-reversion

## One-Sentence Summary

> Substack article about trading strategies.

## Key Insights

1. **原文来源**: TradeQuantiX

## Full Content

---
title: "ETF Mean Reversion Methods: Mean Reversion Mini-Portfolio Creation - Part 2"
author: TradeQuantix
url: https://www.tradequantixnewsletter.com/p/etf-mean-reversion-methods-mean-reversion
date: 2025-04-22
topics:
  - Mean Reversion
  - ETF
  - Portfolio Construction
  - Systematic Trading
  - Multi-Strategy
source: Substack
---

## Summary

本文是 TradeQuantix ETF 均值回归系列第二部分，核心论述：**四个普通系统组合成一个 mini-portfolio，其风险调整后收益远超任何单一系统**。

### Part 1 回顾：四个独立均值回归系统
- **Z_Reversion**: 使用 Z-score 衡量超卖
- **Vol_Reversion**: 使用波动率通道
- **Vol_Reversion_2**: 与 Vol_Reversion 进出时机不同
- **RSI_Reversion**: 使用预计算 RSI 入场水平， timing 机制不同

每个系统分 **3 次 sub-entry** 建仓，交易多资产 ETF 组合（股票、债券、黄金、比特币），类似"全天候组合"。

### 核心观点：Portfolio Effect 是唯一圣杯
- 单一系统的回测再好看，也可能是过拟合；组合多个真正低相关的系统才能分散风险
- 风险分散不仅跨资产、跨时间、跨价格，还要跨**思想/实现方式**（diversification of ideas and implementation）
- 作者用 TMF（债券）近期表现差的例子说明：单个 sub-entry 可能在回撤，但组合后整体几乎不受影响

### 关键数据
- 杠杆/非杠杆 ETF 版本：2000 年以来（除 2000 年一次较大回撤外）**没有一年亏损**
- 月回报热力图显示：不是少数几个月carry全部收益，而是持续稳定的正回报流
- **回撤相关性平均 ~0.34 或更低**，收益相关性在 0.06~0.79 之间——真正的低相关

### 动态排名机制（可选）
- 按滚动 **1 年 Sharpe（收益/年化日波动）** 对每个 equity curve（单系统-单资产-单次 sub-entry）排名
- 每季度更新排名
- `ExcludeWorstX` 参数可屏蔽最差的 N 条 equity curve，但作者警告：**这是 exposure 管理工具，不是 performance optimizer**，过度优化会引入多层过拟合

### 关于 3 次 Sub-entry 的说明
- 2 次太少，5 次以上需要更多资金和自动化；3 次是**80/20 甜蜜点**
- 每次 1/3 等权分配：最简单、最稳健，避免引入又一个可优化参数

### 结论
1. 四系统组合 > 单一系统，因为 portfolio effect
2. 低相关性来自：不同超卖测量方式、不同进出机制、不同资产、不同 sub-entry
3. 季度排名机制让组合具备适应性，但不要把它变成新的优化表面
4. Part 3 预告：样本内/外验证、稳健性测试、2025年8月以来的实盘表现

---

## Full Content

Welcome to the “Systematic Trading with TradeQuantiX” newsletter, your go-to resource for all things systematic trading. This publication will equip you with a complete toolkit to support your systematic trading journey, sent straight to your inbox. Remember, it’s more than just another newsletter; it’s everything you need to be a successful systematic trader.

I recently launched aportfolio tracking website (updated daily) that tracks my systematic trading portfolio performance, along with many supporting metrics. You can check in on my personal systematic trading portfolio performance anytime here:TQX Portfolio Tracker

Introduction:

In Part 1, we covered four independent mean reversion systems, each measuring oversold conditions in a completely different way.

Z_Reversion:uses z scores.

Vol_Reversion:uses volatility bands.

Vol_Reversion_2:enters and exits at different times and with different methods than Vol_Reversion.

RSI_Reversion:utilizes pre-calculated RSI entry levels and enters with a different timing mechanism than the other three systems.

Each system scales into positions across three sub-entries, and all four systems trade a multi-asset ETF universe spanning equities, bonds, gold, and bitcoin. This takes an “All Weather Portfolio” like approach to the trading universe.

If you haven’t read Part 1 yet, see the link below.

ETF Mean Reversion Methods: Four Systems Built for the Dip - Part 1

I’ve spent a lot of time in the past trying to build mean reversion systems on the entire US stock universe. I figured if I could find that perfect signal, it should work across everything. People say the US is a very mean reverting market, and maybe that’s the case, but I’ve always struggled to develop a system I’ve determined to be robust.

So, what happens when you stop evaluating systems in isolation and start combining them into mini-portfolios?

As I hinted at in the part 1 article, we will be combining these four systems into a mean reversion mini-portfolio.

Why use the term “mini-portfolio”? (warning, I use the term “mini-portfolio” a lot in the next few paragraphs)

Well, because I like to think of my own systematic trading portfolio as a portfolio of many smaller portfolios.

Trend mini-portfolio

Trend mini-portfolio

Momentum mini-portfolio

Momentum mini-portfolio

Mean reversion mini-portfolio

Mean reversion mini-portfolio

Hedging mini-portfolio

Hedging mini-portfolio

The portfolio effect is super powerful when it comes to creating superior risk adjusted returns. One strategy may have mediocre performance on its own, but combined into a portfolio of many other strategies, that portfolio of mediocre strategies can look fantastic.

I like to look at mini-portfolios of similar methodologies first. I’ll get all the allocations and volatilities properly adjusted relative to each other. Then I’ll combine the mini-portfolio into the overall systematic trading portfolio. This just helps me build up my portfolio one block at a time. This is why I use the term “mini-portfolio”.

Take any one of these four systems and run it standalone. The stats look okay, nothing special. That’s fine. Because the real story isn’t the individual systems. The real story is what happens when you put them together to make the mean reversion mini-portfolio.

This part 2 article covers the mini-portfolio construction of these four mean reversion systems. I’ll show how four similar systems combined t

---

*Imported from Substack on 2026-04-25*
