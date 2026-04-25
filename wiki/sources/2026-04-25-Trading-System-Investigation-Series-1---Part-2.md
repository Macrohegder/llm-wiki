# Trading System Investigation:               Series 1 - Part 2

**Source**: [[2026-04-25-Trading-System-Investigation:---------------Series-1---Part-2]] | [TradeQuantiX](https://www.tradequantixnewsletter.com/p/trading-system-investigation-series-388)
**Date**: 2026-04-25
**Tags**: #article #substack #strategy

## One-Sentence Summary

> Premium Content Vault
Trading System Investigation:               Series 1 - Part 2
A deep dive into a short term trading system found online. Is it worth trading?
TradeQuantiX
Oct 08, 2024
∙ Paid
33
...

## Key Insights

1. **原文来源**: [TradeQuantiX](https://www.tradequantixnewsletter.com/p/trading-system-investigation-series-388)

## Full Content

Premium Content Vault
Trading System Investigation:               Series 1 - Part 2
A deep dive into a short term trading system found online. Is it worth trading?
TradeQuantiX
Oct 08, 2024
∙ Paid
33
3
4
Share
In part 1 of this article series, we introduced the rules to a trading system shared in a free webinar. We then coded the system into my backtesting platform and discussed the shared system performance vs. the performance of my version of the system based on my interpretation of the system rules. We then showed some example trades, and discussed some strengths and weaknesses of the system. If you missed part 1, be sure to check it out here:
In this article, we will continue our investigation of the trading system. via the following steps:
Try to improve the strategy with an In Sample and Out of Sample approach
Ensure the parameter selection is robust
Test the improvements on out of sample data
Share final code and thoughts
Note:
Not every step in my trading system development process will be discussed in this article series, I will discuss my full process in later articles. The purpose of this article series is to simply show how you can quickly leverage a system you found online and make it your own. If you want to learn my full process and robustness techniques as well, you’ll have to subscribe to this newsletter so you’re notified when new articles come out. You won’t want to miss what I’ll have to discuss!
Subscribe
From the discussion in part 1 of this article series, this system can definitely be improved. We have the system coded and more or less matching the published results, but let’s make the system better. You may also remember a discussion about this system having more rules than I would like, so let’s try to simplify the system while we are at it. We will do all of this with an In Sample and Out of Sample approach. The In Sample will be used to test our ideas and make modifications. The Out of Sample will be used to validate the changes to the system did not result in curve fitting or overoptimization to noise in the data.
First let’s define the In Sample and Out Of Sample approach. In Sample will be from 2007 to 2018 on the S&P 500. The Out of Sample will be from 2018 until today (2024), and 1993 to 2007 on the S&P 500 (and other stock universes such as the Russell 1000 or NASDAQ 100).
In part 1 of this article series, I discussed that one weakness of this strategy is it has too many entry and exit rules. So the first order of business is to reduce the complexity of the system without degrading the performance too much. To do this, first I simply removed each of the rules one at a time from the system to see which rules had a large impact on performance and which rules didn’t have a large impact on performance. If I removed a rule and the system performance was not obviously negatively impacted, then the rule was thrown out. This helped me reduce the rules down to the few that actually matter. Since this is a very repetitive and boring process I won’t spent too much time on it, I think you get the idea, but if you want you can perform this exercise yourself with the code provided from part 1 of this article series. After performing this exercise, along with a couple minor changes to the rules along the way, the updated/simplified rules of the system are shown below. Any removed rules from the system are crossed out and any updates are noted in italics along with why that rule was changed.
The updated/simplified entry rules are as follows:
Stock is in the S&P 500 universe
Stock is greater than $10
(changed from $1 in the original code so the system trades more mature, higher prices stocks)
Stock dollar volume is in the top 50% of current SP500 stocks
Stock percent volatility (defined by 10 day ATR/C) is between 1% and 40%
Stock has returned at least 10% in the last 100 trading days
3 day RSI is below 20
Stock has had two down days in a row
10 day ADX is greater than 30
(changed from an ADX of 7 in the original code to remove a parameter, this removes complexity)
Hold up to 10 equally sized positions at a time
If there are more than 10 candidates available for trading, rank by the 100 day rate of change
(Changed from one year highest rate of change to remove a parameter, 100 is also used in a rule above)
Enter the next day with a limit order 1% below the close of the previous day
The updated/simplified exit rules are as follows:
Intraday initial stop of 2 ATR’s (10 day ATR)
2.5 ATR trailing stop (10 day ATR) sold next close
(changed from an intraday execution since intraday panics/sell offs tend to result in worse exit prices)
Intraday 4% profit target
Exit after 10 trading days
(New Rule added to prevent holding stocks for an indefinite period of time)
There, now some of the system complexity has been removed. Turns out some of the rules in the original system were not significant because they really didn’t make a difference to the overall performance. If you don’t believe me try out thi

---

*Imported from Substack on 2026-04-25*
