# 2025-04-22-simple-alpha-atlas-what-actually-works-across-markets-daily

**Source**: [[2025-04-22-2025-04-22-simple-alpha-atlas-what-actually-works-across-markets-daily]] | [Delphic Alpha]()
**Date**: 2025-04-22
**Tags**: #article #substack

## One-Sentence Summary

> Substack article about trading strategies.

## Key Insights

1. **原文来源**: Delphic Alpha

## Full Content

---
title: "Simple Alpha Atlas: What Actually Works Across Markets (Daily)"
author: Delphic Alpha
url: https://delphicalpha.substack.com/p/the-alpha-atlas-what-actually-works
date: 2025-04-22
topics:
  - Alpha Research
  - Multi-Asset
  - Trend Following
  - Mean Reversion
  - Cross-Sectional Momentum
  - Backtest Validation
source: Substack
---

## Summary

Delphic Alpha 对 **12 个 alpha、5 个资产类别、29 个品种、2021-2026 年**进行了零优化、零交易成本的系统测试，揭示了哪些简单策略在哪些市场真的有效。

### 测试设计
- **4 个信号族**，每个 3 个回顾期（5d/20d/120d）：
  - **TR-BO** (Trend Breakout): 突破 N 日高低点
  - **TR-MA** (Trend Moving Average): N 日均线上下
  - **CS** (Cross-Sectional Momentum): 相对强弱排名做差价
  - **MR** (Mean Reversion): Z-score 逆向，买超卖卖超买
- **5 个资产类别**：股指期货、债券期货、商品期货、G7 外汇、加密货币

### 核心结果（热力图要点）

| 市场 | 最佳策略 | Sharpe | 说明 |
|-------|-----------|--------|------|
| **FX** | 5日均值回归 (MR) | **1.29** | 结构性最稳定的 edge，IC 约 0.05 |
| **Crypto** | 120日突破 (TR-BO) | **0.88** | 需要耐心抓住趋势变化 |
| **Equities** | 120日均值回归 (MR) | **0.63** | 机构再平衡创造可预测的反趋势流动 |
| **Commodities** | 120日突破 (TR-BO) | **0.53** | 边际真实但弱，需要更大宽度 |
| **Bonds** | 20日均线 (TR-MA) | **0.51** | 几乎没有稳定的 alpha |

### 关键洞察

1. **没有通用 alpha**：必须匹配信号类型与市场微观结构
   - 流动性高、信息密集的市场（FX、股票）倾向均值回归
   - 物理/动量驱动的市场（商品、加密货币）倾向趋势跟踪

2. **红色单元格也是钱**：Sharpe 为 -1.44 意味着反向交易的 Sharpe 为 +1.44。每个深红色单元都是一个强 alpha——只需翻转信号方向

3. **过拟合税：76% 的回测 Sharpe 是噪声**
   - 样本外验证（IS→OOS）斜率仅 0.24
   - FX 均值回归是唯一在样本外表现最一致的 edge
   - 债券趋势最差：加息周期看起来像趋势，但并非如此

4. **多资产、多 alpha 组合才是产品**
   - 相关性低至中等，跨资产部署是免费的风险调整收益
   - 同时运行 5d/20d/120d 三个周期是对某个周期失效的便宜保险

### 行动要点
- 给回测 Sharpe 打 **75% 折扣**后再决定是否交易
- 如果你在 FX 上跑趋势跟踪，你在跟市场的本性对着干
- 商品趋势令人失望时，问题不是信号不够好，而是品种不够多——增加 breadth 才是最高杠杆的改进

---

## Full Content

Trend-following works in commodities. Mean reversion works in equities. Everyone knows this.

But does everyone test it? I did. 12 alphas, 5 asset classes, 5 years, zero optimization, andno transaction costs. Here’s what the data actually says — and what you can do with it.

The Setup

12 alphasacross4 signal families, each with 3 lookback horizons (5, 20, 120 days):

Trend Breakout (TR-BO):Long above N-day high, short below N-day low.

Trend Breakout (TR-BO):Long above N-day high, short below N-day low.

Trend Moving Average (TR-MA):Long above N-day SMA, short below.

Trend Moving Average (TR-MA):Long above N-day SMA, short below.

Cross-Sectional Momentum (CS):Rank by relative strength, bet the spread.

Cross-Sectional Momentum (CS):Rank by relative strength, bet the spread.

Mean Reversion (MR):Fade the Z-score. Buy oversold, sell overbought.

Mean Reversion (MR):Fade the Z-score. Buy oversold, sell overbought.

5 asset classes, 29 instruments:

Equity Index Futures:ES, NQ, YM, NKD, FTSE, DAX

Equity Index Futures:ES, NQ, YM, NKD, FTSE, DAX

Bond Futures:TN, UB, US, ZN, ZF

Bond Futures:TN, UB, US, ZN, ZF

Commodity Futures:Gold, Silver, Crude, Copper, Wheat, Corn

Commodity Futures:Gold, Silver, Crude, Copper, Wheat, Corn

G7 FX:EUR, GBP, JPY, AUD, CAD, CHF vs USD

G7 FX:EUR, GBP, JPY, AUD, CAD, CHF vs USD

Crypto:BTC, ETH, SOL, XRP, DOGE, ADA

Crypto:BTC, ETH, SOL, XRP, DOGE, ADA

Period: March 2021 to February 2026. Same parameters everywhere. No fitting. 60 alpha–asset combinations.

The Heatmap: Where Alpha Lives

Read this chart carefully — it’s the most information-dense image in this post. Each cell is an annualized Sharpe ratio. Green = money. Red = pain.But red is also money:a Sharpe of −1.44 means thereversetrade has a Sharpe of +1.44. Every deep-red cell is a strong alpha hiding in plain sight — you just need to flip the sign.

FX mean reversion dominates.The 5-day Z-score hits Sharpe 1.29. But look at the 5-day MA: −1.44. That’s thesame edgeseen from the other side — trend-following fails in FXbecauseFX mean-reverts. Flip the trend signal and you get a second alpha with an even higher Sharpe.

FX mean reversion dominates.The 5-day Z-score hits Sharpe 1.29. But look at the 5-day MA: −1.44. That’s thesame edgeseen from the other side — trend-following fails in FXbecauseFX mean-reverts. Flip the trend signal and you get a second alpha with an even higher Sharpe.

The heatmap is symmetric in disguise.Cross-sectional momentum in FX: −1.40. Flip it (buy relative losers, sell winners) and you have a Sharpe 1.40 contrarian alpha. The “worst” cells are the best trades — you’re just looking at them backwards.

The heatmap is symmetric in disguise.Cross-sectional momentum in FX: −1.40. Flip it (buy relative losers, sell winners) and you have a Sharpe 1.40 contrarian alpha. The “worst” cells are the best trades — you’re just looking at them backwards.

Crypto rewards patience.120-day breakout at 0.88. Short-term crypto signals are noise. The money is in catching regime shifts and holding.

Crypto rewards patience.120-day breakout at 0.88. Short-term crypto signals are noise. The money is in catching regime shifts and holding.

Equities revert.120-day MR at 0.63. Trend-following equity indices is a losing game over this period — but that means fading the trend is a winn

---

*Imported from Substack on 2026-04-25*
