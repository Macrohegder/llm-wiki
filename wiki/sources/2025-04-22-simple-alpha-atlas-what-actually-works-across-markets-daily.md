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

Equities revert.120-day MR at 0.63. Trend-following equity indices is a losing game over this period — but that means fading the trend is a winning one.

Equities revert.120-day MR at 0.63. Trend-following equity indices is a losing game over this period — but that means fading the trend is a winning one.

Commodity trend is real but thin.Best Sharpe 0.53. It works — just not as dramatically as the CTA marketing suggests.

Commodity trend is real but thin.Best Sharpe 0.53. It works — just not as dramatically as the CTA marketing suggests.

Bonds: almost nothing works.Sharpes cluster near zero in both directions. There’s no strong alpha to flip either — bonds are just hard.

Bonds: almost nothing works.Sharpes cluster near zero in both directions. There’s no strong alpha to flip either — bonds are just hard.

Action point:Don’t skip the red cells. A Sharpe of −1.44 on FX trend-followingisa Sharpe of +1.44 on FX mean-reversion. The heatmap gives you 60 alphas, not 60 — because every negative cell is a positive alpha with the sign flipped. Scan for the deepest reds. Those are your strongest signals.

Why These Alphas Work (and Don’t)

Grinold’s Fundamental Law:IR ≈ IC × √Breadth. IC is how right your signal is per trade. Breadth is how many trades you make per year. You need both.

FX MR (Sharpe 1.29):IC ≈ 0.05 — the highest in the study. FX markets are liquid, mean-reverting at short horizons, and the IC barely fluctuates year-to-year. This is a structurally stable edge.

FX MR (Sharpe 1.29):IC ≈ 0.05 — the highest in the study. FX markets are liquid, mean-reverting at short horizons, and the IC barely fluctuates year-to-year. This is a structurally stable edge.

Crypto Breakout (0.88):IC ≈ 0.03. Moderate signal, but crypto’s tendency to trend for months at a time makes even a weak IC compound into a decent Sharpe.

Crypto Breakout (0.88):IC ≈ 0.03. Moderate signal, but crypto’s tendency to trend for months at a time makes even a weak IC compound into a decent Sharpe.

Equity MR (0.63):IC ≈ 0.025. Institutional rebalancing creates predictable countertrend flows in index futures. Slow but reliable.

Equity MR (0.63):IC ≈ 0.025. Institutional rebalancing creates predictable countertrend flows in index futures. Slow but reliable.

Commodity Trend (0.53):IC ≈ 0.02. Weak per-bet. The edge is real — physical supply/demand imbalances do create trends — but you need a broad commodity universe to make the Fundamental Law work in your favor.

Commodity Trend (0.53):IC ≈ 0.02. Weak per-bet. The edge is real — physical supply/demand imbalances do create trends — but you need a broad commodity universe to make the Fundamental Law work in your favor.

Bond Trend (0.51):IC ≈ 0.02, and unstable. Rate cycles create episodic trends that look systematic in backtests but don’t persist.

Bond Trend (0.51):IC ≈ 0.02, and unstable. Rate cycles create episodic trends that look systematic in backtests but don’t persist.

Action point:If your commodity trend alpha disappoints, the fix isn’t a better signal — it’s more instruments. The IC is weak but positive. Adding breadth (more commodity contracts, more commodity-like markets) is the highest-leverage improvement you can make.

The Cheat Sheet: Best Alpha per Market

Cut to the chase:

FX:5-day mean reversion (Sharpe 1.29)

FX:5-day mean reversion (Sharpe 1.29)

Crypto:120-day breakout (Sharpe 0.88)

Crypto:120-day breakout (Sharpe 0.88)

Equities:120-day mean reversion (Sharpe 0.63)

Equities:120-day mean reversion (Sharpe 0.63)

Commodities:120-day breakout (Sharpe 0.53)

Commodities:120-day breakout (Sharpe 0.53)

Bonds:20-day MA (Sharpe 0.51)

Bonds:20-day MA (Sharpe 0.51)

Notice the pattern: liquid, information-rich markets (FX, equities) revert. Physical and momentum-driven markets (commodities, crypto) trend. This isn’t a coincidence — it’s microstructure. And remember: if a marketstronglytrends, the reverse-trend signal (mean reversion) will show a largenegativeSharpe — which is just a largepositiveSharpe for the opposite trade. The best alphas often hide in the worst-looking cells.

Action point:Pick the alpha family that matches your market’s microstructure, not the one you wish worked. If you trade FX and you’re running trend-following, you’re fighting the market’s natural behavior.

The Regime Problem

Crypto 2022–2023:Sharpes of 1.71 and 1.09. The crash-then-recovery was a textbook trending environment.

Crypto 2022–2023:Sharpes of 1.71 and 1.09. The crash-then-recovery was a textbook trending environment.

Equities:The most consistent — positive in 4 of 6 years, peaking at 1.89 in early 2026.

Equities:The most consistent — positive in 4 of 6 years, peaking at 1.89 in early 2026.

FX:Swings from −1.42 (2025) to strongly positive in other years. High alpha, high variance.

FX:Swings from −1.42 (2025) to strongly positive in other years. High alpha, high variance.

Commodities:Negative in several years. Not the all-weather edge it’s marketed as.

Commodities:Negative in several years. Not the all-weather edge it’s marketed as.

The year-to-year variancewithineach asset class dwarfs the differencesbetweenthem. The best market in one year can be the worst the next.

Action point:Never allocate 100% to one market based on a backtest. The Sharpe you see is an average over regimes. In any given year, that average is meaningless. Spread your capital across asset classes and alpha families — the diversificationisthe alpha.

Rolling Sharpe: How Stable Is the Edge?

These panels answer the question every trader asks:is the alpha dying?FX mean reversion (red) stays consistently above zero. Crypto (purple) spikes and fades. No single market or alpha family delivers a steady paycheck — which is why you need all of them running simultaneously.

Cross-Asset Correlations

Low to moderate correlations across the board. Equity and bond returns move together (macro sensitivity). Crypto is its own animal. This confirms that multi-asset deployment isn’t just a good idea — it’s free risk-adjusted return.

Per-Class Equity Curves

Risk-adjusted equity curves by alpha family (5d, 20d, 120d lookbacks):

Equity Index Futures

Bond Futures

Commodity Futures

FX (G7)

Crypto

The Overfitting Tax: How Much of This Is Real?

Everything above uses the full sample. But the only question that matters:how much survives out of sample?

I split at March 2024 — 3 years in-sample, 2 years out-of-sample — and compared every alpha’s Sharpe across the two periods.

The dashed line is “what you backtest = what you get.” The red line is reality.

Slope:0.24. For every 1.0 Sharpe in your backtest, expect to keep 0.24.76% of your backtest Sharpe is noise.

FX (red):Most coherent IS→OOS. Mean-reversion alphas persist. This is the most “real” edge in the study.

FX (red):Most coherent IS→OOS. Mean-reversion alphas persist. This is the most “real” edge in the study.

Crypto (purple):Mixed. A few breakout signals survive; many flip sign.

Crypto (purple):Mixed. A few breakout signals survive; many flip sign.

Equities (blue):Honest but uninspiring. IS near zero predicts OOS near zero.

Equities (blue):Honest but uninspiring. IS near zero predicts OOS near zero.

Commodities (green):Concerning — several positive IS Sharpes go negative OOS.

Commodities (green):Concerning — several positive IS Sharpes go negative OOS.

Bonds (orange):Worst offenders. The rate-hiking cycle looked like a trend. It wasn’t.

Bonds (orange):Worst offenders. The rate-hiking cycle looked like a trend. It wasn’t.

Action point:Haircut every backtest Sharpe by 75% before you size a position. If it’s not positive after the haircut, don’t trade it. If a signal requires optimization to show an edge, the edge is probably in the optimization, not the market.

What to Do With This

This study gives you a map. Here’s how to use it:

Start with the highest-IC market for your signal type.If you’re building mean-reversion alphas, start with FX. If you’re building trend alphas, start with crypto or commodities. Don’t try to force a signal type into a market that doesn’t support it.

Start with the highest-IC market for your signal type.If you’re building mean-reversion alphas, start with FX. If you’re building trend alphas, start with crypto or commodities. Don’t try to force a signal type into a market that doesn’t support it.

Use the Fundamental Law to diagnose underperformance.If your Sharpe is lower than expected, decompose it. Is the IC too low (bad signal)? Or is the breadth too low (too few instruments)? The fix is completely different in each case.

Use the Fundamental Law to diagnose underperformance.If your Sharpe is lower than expected, decompose it. Is the IC too low (bad signal)? Or is the breadth too low (too few instruments)? The fix is completely different in each case.

Build multi-asset, multi-alpha portfolios.The correlations are low. Running all 12 alphas across all 5 asset classes gives you ~60 bets with moderate IC and massive breadth. The portfolio Sharpe will be substantially higher than any individual cell in the heatmap.

Build multi-asset, multi-alpha portfolios.The correlations are low. Running all 12 alphas across all 5 asset classes gives you ~60 bets with moderate IC and massive breadth. The portfolio Sharpe will be substantially higher than any individual cell in the heatmap.

Haircut everything by 75%.Your backtest Sharpe is not your live Sharpe. Size positions to the post-haircut number. If a strategy needs leverage to work after the haircut, it doesn’t work.

Haircut everything by 75%.Your backtest Sharpe is not your live Sharpe. Size positions to the post-haircut number. If a strategy needs leverage to work after the haircut, it doesn’t work.

Diversify across time horizons.The 5-day, 20-day, and 120-day alphas have different regime sensitivities. Running all three is cheap insurance against any one horizon going cold.

Diversify across time horizons.The 5-day, 20-day, and 120-day alphas have different regime sensitivities. Running all three is cheap insurance against any one horizon going cold.

Rerun this on your own data.The methodology is deliberately simple. You can replicate this with any set of instruments, any lookback periods, any time range. The value isn’t in my specific numbers — it’s in the framework. Build your own heatmap. Find your own alpha atlas.

Rerun this on your own data.The methodology is deliberately simple. You can replicate this with any set of instruments, any lookback periods, any time range. The value isn’t in my specific numbers — it’s in the framework. Build your own heatmap. Find your own alpha atlas.

Key Takeaways

There is no universal alpha.Match the signal family to the market’s microstructure.

There is no universal alpha.Match the signal family to the market’s microstructure.

FX mean reversion is the best simple alpha in this study.Sharpe 1.29 from a 5-day Z-score. Highest IC, most stable OOS.

FX mean reversion is the best simple alpha in this study.Sharpe 1.29 from a 5-day Z-score. Highest IC, most stable OOS.

Commodity trend is overrated as a standalone.Sharpe 0.53 with weak IC. The edge is real but needs breadth to compound.

Commodity trend is overrated as a standalone.Sharpe 0.53 with weak IC. The edge is real but needs breadth to compound.

76% of your backtest is noise.Haircut aggressively. Size conservatively.

76% of your backtest is noise.Haircut aggressively. Size conservatively.

The portfolio is the product.No single alpha or market is the answer. Diversification across both is where the Sharpe lives.

The portfolio is the product.No single alpha or market is the answer. Diversification across both is where the Sharpe lives.

The alpha atlas doesn’t show you one treasure. It shows you that the treasure is the map itself.

Disclaimer: This post is for educational and informational purposes only. Nothing here constitutes financial advice, investment advice, or a recommendation to buy, sell, or hold any security, derivative, or cryptocurrency. The analysis uses historical data with no transaction costs — actual trading results will differ materially due to slippage, commissions, market impact, and execution risk. Past performance does not predict future results. All Sharpe ratios, returns, and statistics are hypothetical and based on backtested data that was not traded live. Do your own research, understand your risk tolerance, and consult a qualified financial advisor before making any investment decisions. The author may hold positions in the instruments discussed.