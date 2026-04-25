# All Weather Portfolio Research: Part 3

**Source**: [[2026-04-25-All-Weather-Portfolio-Research:-Part-3]] | [TradeQuantiX](https://www.tradequantixnewsletter.com/p/all-weather-portfolio-research-part-f13)
**Date**: 2026-04-25
**Tags**: #article #substack

## One-Sentence Summary

> All Weather Portfolio Research: Part 3
Implementing Improvements to the TradeQuantiX All Weather Portfolio
TradeQuantiX
Dec 20, 2024
18
14
Share
Welcome to part 3 of this All Weather Portfolio series!...

## Key Insights

1. **原文来源**: [TradeQuantiX](https://www.tradequantixnewsletter.com/p/all-weather-portfolio-research-part-f13)

## Full Content

All Weather Portfolio Research: Part 3
Implementing Improvements to the TradeQuantiX All Weather Portfolio
TradeQuantiX
Dec 20, 2024
18
14
Share
Welcome to part 3 of this All Weather Portfolio series! Before we dive into it, let’s just do a quick recap of the previous two articles in the series. The first part of the All Weather Portfolios research focused on coding up and testing already existing All Weather Portfolios found online. We learned a lot doing this but ultimately, traditional All Weather Portfolios were pretty boring in terms of performance and severely underperformed the past few years. From there, I made my own TradeQuantiX All Weather Portfolios where I attempted to take the traditional All Weather Portfolio and make it interesting again. The TradeQuantiX All Weather Portfolios increased diversification, reduced drawdown, and increased returns. I explored three variations of TradeQuantiX All Weather Portfolios, one with a static allocation and is always invested, a second with static allocation and a market timing switch, and a third with dynamic allocation and a market timing switch. Those three portfolios looked great and were much more interesting than the traditional All Weather Portfolios. If you missed the previous two articles check them out here:
Originally, I had planned for this to be a two part series, but after some more research and some reader suggestions, I have decided to write a third part to this series. In this article I will start with the tactical asset allocation with dynamically adjusting position sizing (the third all weather portfolio in part 2) and take it another step further. A reminder of what that portfolio looks like:
This portfolio has access to 13 ETFs and rebalances monthly. It also only holds ETFs that are above the 200 day moving average and sells ETFs below the 200 day moving average. The 13 ETFs it can hold are:
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
Subscribe
All Weather Portfolio Improvements To Explore:
What I want to do next is explore more ideas to attempt to create the ultimate All Weather Portfolio. The ideas I will explore in this article are:
Continuous Rebalancing:
Currently the rebalance interval is monthly. But what about weekly? Or rebalance only when volatility changes?
Exposure to Country Specific ETFs:
This was a reader suggestion to allow the portfolio to hold ETFs for individual countries (Japan, India, China, etc.) rather than VEU, which is all countries except the US.
Annualize the Weighting for the Ranking Calculation:
This was a suggestion by a reader
Original ranking metric:
Ranking = ROC(C, 120) + ROC(C, 60) + ROC(C, 30)
Proposed ranking metric to give more weight to ETFs performing well recently
Ranking = 2*ROC(C, 120) + 4*ROC(C, 60) + 8*ROC(C, 30)
Add some Managed Futures ETFs:
A reader suggested to add managed futures ETFs like DBMF or KMLM
A few of these ideas are reader suggested, which I think is fantastic. I am ecstatic that my readers are engaged enough to send me suggestions. So thank you, I will always welcome suggestions, constrictive criticism, and improvement ideas.
To explore these ideas, we will look into each one at a time. We will start with the tactical asset allocation with dynamically adjusting position sizing All Weather Portfolio (the third all weather portfolio in part 2) and try each idea one at a time to understand the impact. One thing to be aware of, I plan to use the entire data series to assess these new ideas. I have considered an In Sample and Out of Sample approach, but given we only have a handful of ETFs and 16 years of history where most ETFs exist (which really isn’t that much to see how the portfolio behaves in different market conditions), it’s very difficult to assess this system with In Sample Out of Sample. I would argue I am better off with a very careful development approach of no optimizing, no tinkering, and focusing diligently on robustness tests. Remember, always do your own validation of an idea. Hopefully after this article, you too can conquer any “weather” event in your trading and always keep your trading portfolio bright and sunny.
Subscribe
All Weather Portfolio Improvement #1 - Continuous Rebalancing:
The current version of the TradeQuantiX All Weather Portfolio only rebalances once per month. If volatility expands or contracts severely during the month, the portfolio has to wait until the end of the month to account for the changes. If we can make the portfolio more dynamic to volatility changes, theoretically this should smoothen the equity curve. One thing we need to be careful of, if we are rebalancing every day we could get dest

---

*Imported from Substack on 2026-04-25*
