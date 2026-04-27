---
title: "Does Wall Street’s #1 Trading Strategy ‘Buy Top Stocks, Sell Bottom Stocks’ Still Work? (See My Fully Tested Results)"
author: "SetupAlpha"
source: "Substack"
url: "https://setup4alpha.substack.com/p/cross-sectional-momentum-trading-strategy-buy-top-stocks-sell-bottom-stocks"
date: "2026-04-27"
topics: ["systematic-trading", "algorithmic-trading"]
---

# Does Wall Street’s #1 Trading Strategy ‘Buy Top Stocks, Sell Bottom Stocks’ Still Work? (See My Fully Tested Results)

**来源**: [SetupAlpha](https://setup4alpha.substack.com/p/cross-sectional-momentum-trading-strategy-buy-top-stocks-sell-bottom-stocks)  
**日期**: 2026-04-27  
**作者**: SetupAlpha

---

## 摘要

Does Wall Street’s #1 Trading Strategy ‘Buy Top Stocks, Sell Bottom Stocks’ Still Work? (See My Fully Tested Results)
I Backtested the Classic Academic Momentum Strategy to 2025
SetupAlpha
Oct 26, 2025
∙ Paid
17
2
Share
Hi,
Would you actually put
your own money
on this classic ‘
buy winners, sell losers
’ system today?
Today, you will learn 4 things (+ 1 Gift):
What is Cross-Sectional Trading Strategy (Buy Top, Sell Bottom)
Does the strategy still work?
The specific market cases where it is profitable (and where it fails).
The full strategy rules (step-by-step) and RealTest code you can download now.
Plus extra gift strategy for the paid users 👇
Let’s jump in.
About the context… Last month, my colleague sent me this paper (
https://papers.ssrn.com/sol3/papers.cfm?abstract_id=299107
).
The ...

---

## 原文

Does Wall Street’s #1 Trading Strategy ‘Buy Top Stocks, Sell Bottom Stocks’ Still Work? (See My Fully Tested Results)
I Backtested the Classic Academic Momentum Strategy to 2025
SetupAlpha
Oct 26, 2025
∙ Paid
17
2
Share
Hi,
Would you actually put
your own money
on this classic ‘
buy winners, sell losers
’ system today?
Today, you will learn 4 things (+ 1 Gift):
What is Cross-Sectional Trading Strategy (Buy Top, Sell Bottom)
Does the strategy still work?
The specific market cases where it is profitable (and where it fails).
The full strategy rules (step-by-step) and RealTest code you can download now.
Plus extra gift strategy for the paid users 👇
Let’s jump in.
About the context… Last month, my colleague sent me this paper (
https://papers.ssrn.com/sol3/papers.cfm?abstract_id=299107
).
The strategy is very simple:
buy the best stocks from the past year,
sell the worst stocks, rebalance every quarter.
From 1993 to 2001, it delivered 32.24% annual returns. Sharpe ratio 1.26.
But what about 2001 to 2025?
The paper was published in October 2001. Right at the end of their testing period.
Which made me wonder what if I run it forward?
What if I test it through 2025?
So I rebuilt the strategy in RealTest.
And what I found wasn’t what I expected.
I tested multiple academic papers. Stick around till the end.
The concept (
Cross-sectional Momentum
)
Simple idea:
Stocks that went up keep going up,
Stocks that went down keep going down.
Not forever. Just long enough to capture the drift.
The academic logic is clean: earnings surprises take time to propagate. Information diffuses slowly. Investors underreact, and the stock drifts in one direction as the news spreads.
If you want the full explanation,
this 5-minute video
breaks it down.
The strategy from the paper:
Take all NYSE stocks above $5
Rank them by 252-day performance (one year)
Buy top 10
Sell bottom 10
Rebalance quarterly
Why 252 days? Because stocks exhibit mean reversion over short periods like a month, but momentum over longer periods like a year. The strategy tries to capture that medium-term persistence.
I coded it exactly as specified. Full costs included: IB commissions plus 0.1% slippage. Norgate data with all delisted stocks to avoid survivorship bias.
First, the results from 1993 to 2001. The paper’s period.
Test 1: The golden years
1993-2001 results: 32.24% annual return, 1.26 Sharpe ratio, -33.34% max drawdown
Amazing results.
But now let me run it through 2025.
It broke. Completely.
Test 2: Maybe rebalancing frequency matters?
My first thought was maybe quarterly rebalancing is too slow. Maybe monthly captures momentum shifts faster before the edge decays.
So I changed the rebalance period from 3 months to 1 month.
Worse results. More turnover, higher costs, lower returns. That wasn’t it.
Test 3: More diversification?
Maybe 10 positions isn’t enough. Maybe I need more diversification to reduce single-stock risk.
I changed it to 20 positions. Top 20 long, bottom 20 short.
Diversification (positions) didn’t help either.
Test 4: Different lookback periods
Maybe the 252-day lookback (one year) is the problem. Maybe a different ranking period works better.
I tested five different lookback periods:
20 days (1 month)
60 days (3 months)
126 days (6 months)
200 days (common technical analysis period)
252 days (original one year)
Testing different lookback periods. 200 days had the highest return.
But “highest” is relative. It was still poor compared to buy-and-hold SPY.
Reading more papers
At this point, I went back to reading. I had to be missing something.
I found this paper:
Fact, Fiction, and Momentum Investing
by Novy-Marx (2012).
And there’s also this collection from Alpha Architect:
Quantitative Momentum Investing Philosophy
.
These papers mention something interesting. They suggest using filters beyond just price. Market cap filters. Liquidity filters. Remove the most liquid stocks.
The idea: large, liquid stocks are efficiently priced. Information gets arbitraged away instantly. Small, illiquid stocks have slower information diffusion. Momentum persists longer.
I don’t have clean historical market cap data for all delisted stocks. But I do have volume data. So what if I filter by volume instead?
Test 5: Long-only
I made some changes:
Switched to long-only (no short side, because shorting illiquid small-caps is expensive) (This papers suggests long-side only
https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2420743
)
Added volume filter
Rebalancing quarterly (3 months)
Used 6-month lookback for ranking
Top 5 positions instead of 10 (more concentrated)
This was a lot better.
Test 6: Skip the most recent month
The papers mention that academic momentum strategies skip the most recent month to avoid short-term reversal effects.
The code
ROC(c,RankLen)[20]
calculates the rate of change over RankLen days but skips the most recent 20 days.
I tested with and without that skip.
The results? Not much difference either way.
Test 7: Rebalancing frequency comparison
The papers suggest testing monthly, quarterly, semi-annually, or annually.
I tested all of them with the volume filter applied.
1-month rebalancing:
3-month rebalancing:
12-month rebalancing:
The 3-month and 6-month rebalancing periods performed best. Monthly was too frequent (higher costs). Annual was too slow.
Test 8: How much does volume matter?
I wanted to see the relationship between volume and performance.
I ran a test looking at average gain versus average 20-day volume.
Higher volume = lower momentum returns.
Lower volume = higher momentum returns.
Higher volume = lower momentum returns.
Lower volume = higher momentum returns.
So I tested using only stocks with average 20-day volume below 1 million shares.
Only stocks with volume below 1M shares. This works?
The volume filter changed everything.
Is it perfect now? No.
Does one volume filter prove the system is bulletproof? Absolutely not.
But it’s the difference between a broken strategy and one that actually works. And that’s worth paying attention to.
Test 9: Parameter robustness check
I wanted to make sure this wasn’t curve-fitted to one specific combination.
So I tested five different ranking periods:
20 days (one month)
60 days (quarter)
126 days (half year)
200 days (common TA period)
252 days (original one year)
And rebalancing frequencies (1, 3, 6, 12 months) with the volume filter applied.
The 60-200 day lookback periods all perform well.
That’s a good sign. The edge is consistent across a range of parameters, not dependent on one specific number.
Test 10: Number of positions
Does it matter if I hold 5 positions versus 10 or 20?
I tested 1,5,8,10,20,40,50 positions. (by Sharpe Ratio)
Testing 1, 5, 8, 10, 20, 30, 40, 50 positions.
No huge difference.
Test 11: Different universe
Full NYSE universe.
I also tested this on SPY constituents instead of the full NYSE universe.
Look, this strategy isn’t perfect, but it holds serious potential.
That’s why I’m sharing this with you. You’ve now seen my process - the tests I run, the things that didn’t work, the adjustments that did.
Your next step is to download this strategy and play around with it yourself.
Get Trading Strategy Rules Step-by-Step + RealTest Code below! ⬇️
Plus this strategy:
This post is for paid subscribers
Subscribe
Already a paid subscriber?
Sign in

---

*由 Substack Strategy Tracker 自动抓取*

---

*Imported from Substack on 2026-04-27*
