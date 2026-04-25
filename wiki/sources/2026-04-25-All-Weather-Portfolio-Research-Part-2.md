# All Weather Portfolio Research: Part 2

**Source**: [[2026-04-25-All-Weather-Portfolio-Research:-Part-2]] | [TradeQuantiX](https://www.tradequantixnewsletter.com/p/all-weather-portfolio-research-part-418)
**Date**: 2026-04-25
**Tags**: #article #substack

## One-Sentence Summary

> All Weather Portfolio Research: Part 2
Three TradeQuantiX All Weather Portfolio Versions
TradeQuantiX
Dec 05, 2024
29
9
3
Share
In the last post about All Weather portfolios we looked at a bunch of di...

## Key Insights

1. **原文来源**: [TradeQuantiX](https://www.tradequantixnewsletter.com/p/all-weather-portfolio-research-part-418)

## Full Content

All Weather Portfolio Research: Part 2
Three TradeQuantiX All Weather Portfolio Versions
TradeQuantiX
Dec 05, 2024
29
9
3
Share
In the last post about All Weather portfolios we looked at a bunch of different All Weather portfolio ideas. We coded up 9 examples of All Weather portfolios found online and figured out what we liked and didn’t like about them. In this article, I am going to take this one step further and create my own All Weather portfolios. I will show a total of three variations of an All Weather portfolio. One variation will have a static allocation that is only rebalanced monthly (quarterly, semi-annually, yearly etc. rebalance intervals is also possible), another variation will be a tactical asset allocation with specified fixed allocations to each asset, and the third will be tactical allocation with volatility targeted position sizing. Let’s jump in.
Thanks for reading Systematic Trading with TradeQuantiX! Subscribe for free to receive new posts and support my work.
Subscribe
If you remember from the previous article, there were a lot of things I did not like about the All Weather portfolio I explored. One of the things I did not like was many of these portfolio equity curves just looked like SPY with less returns. I want to try to develop an All Weather portfolio that has a more unique and uncorrelated performance profile to SPY. Another thing I did not like was most of the All Weather portfolios broke or underperformed in 2022. Something changed in the markets that caused many of the All Weather portfolios assets to become positively correlated. The All Weather portfolio I want to make needs to have more diversification, so that it can better handle situations like 2022.
To create a better All Weather portfolio that can conquer more market conditions and have uncorrelated returns to SPY, we need to start by having more ETFs in the portfolio. These ETFs need to represent different asset classes that are generally uncorrelated in nature. These ETFs should not just be chosen because they have performed well historically. In fact, historical performance if an ETF was not considered when creating this list of ETFs. I started by thinking of the most intuitively uncorrelated things that were in ETF form, starting with many of the ETFs used in the part 1 of this article series, then expanding from there. To get a stable return in any environment, we need uncorrelated ETFs. A summary of the final ETFs I have considered for this All Weather portfolio are:
QLD (2x QQQ Nasdaq 100)
GLD (Gold)
TLT (20+ Year Treasury Bonds)
SHY (1-3 Year Treasury Bonds)
XLE (Energy Sector)
DBC (Commodity Index)
DBA (Agriculture Commodity Index)
VEU (Global Equity Excluding USA)
XLP (Consumer Staples Sector)
IYH (Healthcare Sector)
VNQ (Real Estate Index Fund (REIT))
BITO (Bitcoin ETF → GBTC used in backtests due to longer price history)
UUP (US Dollar Index)
If you have other ETF ideas, let me know, let’s add them, the more the merrier. A  correlation matrix of the returns of the ETFs listed above looks like the following:
There are a vast range of correlations in this table. Many of the correlations are at 0.5 or below, with many correlations being negative. The goal of this All Weather portfolio is to have as many non-correlated ETFs as possible to survive times of market volatility and uncertainty. While many ETFs are uncorrelated, some ETFs are relatively correlated, like VNQ and VEU, but even those are only at a 0.66 correlation. Granted 0.66 is considered a somewhat strong correlation, but considering VNQ are REITs and VEU is Global Equities they are fundamentally different assets. So even though the correlation may we somewhat strong, I am using intuition to say there may be times on the future where these ETFs are significantly uncorrelated and may help the overall portfolio. Analysis and numbers are not everything, sometimes intuition gets a say in the analysis.
Some may argue that using intuition to determine what to add to an All Weather portfolio is non-sense, but let me take the example to the extreme to illustrate a point. Assume I had two ETFs that were very strongly correlated over ten years. Say one ETF was for cattle prices and the other was for government bonds. I highly doubt those two assets have any real direct connection in prices to each other. Now assume in that ten year time frame the whole economy was booming and everything was increasing in value. If that is the case, then these two assets would probably be positively correlated because everything was going up. That doesn’t mean the two assets are intrinsically linked in their movements. That example is exactly what has happened the US economy the past 14 years. We have had a massive bull market, so of course a lot of assets are going to go up, leading to a positive correlation, but correlation is not causation and does not mean assets are intrinsically linked. This is why even though some ETFs representing an asset are somewhat correlated, 

---

*Imported from Substack on 2026-04-25*
