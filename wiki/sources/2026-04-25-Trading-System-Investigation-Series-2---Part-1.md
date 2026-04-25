# Trading System Investigation Series 2 - Part 1

**Source**: [[2026-04-25-Trading-System-Investigation-Series-2---Part-1]] | [TradeQuantiX](https://www.tradequantixnewsletter.com/p/trading-system-investigation-series-c5e)
**Date**: 2026-04-25
**Tags**: #article #substack #strategy

## One-Sentence Summary

> Premium Content Vault
Trading System Investigation Series 2 - Part 1
A deep dive into a short side day-trade system found online. Is it worth trading?
TradeQuantiX
May 27, 2025
22
4
Share
Welcome to t...

## Key Insights

1. **原文来源**: [TradeQuantiX](https://www.tradequantixnewsletter.com/p/trading-system-investigation-series-c5e)

## Full Content

Premium Content Vault
Trading System Investigation Series 2 - Part 1
A deep dive into a short side day-trade system found online. Is it worth trading?
TradeQuantiX
May 27, 2025
22
4
Share
Welcome to the “Systematic Trading with TradeQuantiX” newsletter, your go-to resource for all things systematic trading. This publication aims to equip you with a complete toolkit to support your systematic trading journey, sent straight to your inbox. Remember, it’s more than just another newsletter; it’s everything you need to be a successful systematic trader.
Thanks for reading Systematic Trading with TradeQuantiX! Subscribe for free to receive new posts and support my work.
Subscribe
Introduction:
Welcome to the Trading System Investigation Series 2, Part 1. In this series, we will investigate an interesting trading system found online. We will examine this system by first attempting to replicate the baseline results as published and understanding the system rules. From there, we will determine if the system is potentially tradable or if it deserves to be thrown in the dumpster.
We will have to figure out if the system is merely an artifact of data mining, has faulty biases built into it, is missing important components (like slippage and commissions), or contains various other issues. Once we understand the premise of the system, validate the results ourselves, and believe the system has promise, we will attempt to improve it by taking it through an in-sample and out-of-sample validation process.
The system we will be investigating in this series is a short-side mean reversion day trading system. This system seeks to profit when a stock is overextended to the upside, aiming to capitalize on the pullback. It holds the position for no longer than one day, selling market-on-close on the same day as entry. We will start by laying out the system rules and understanding its objective.
Subscribe
Baseline System Rules and Objective:
The first step in investigating any system found online or in a book is to understand and attempt to reproduce the system’s results yourself. Many times, you’ll find you can’t reproduce the results, though. It’s very common for trading systems publicly available to have one of the following issues:
Heavy curve fitting
Lookahead bias
Survivorship bias
Failure to account for slippage or commissions
And many other problems
Due to these issues, you’ll often find that when you code up a trading strategy found online, the system doesn’t work at all. Hopefully, that is not the case with this short mean reversion day trading system. The rules of this system as published online are as follows:
Entry Rules:
Stock is within the Russell 1000
Stock has an average volume of 1,000,000 shares or higher over the last 50 days
The stock is $10 or higher
The 39 day percent normalized ATR is within 1% to 8%
The 2 day percent normalized ATR is within 1% to 20%
The 5 day ADX is higher than 35
The day before entry had an up move (measured from open to close) of more than 5%
Place a limit order 5% above yesterday’s close
Position Size Rules:
The system holds a maximum of 10 positions
The system holds equal weight positions (10% each)
If there are more than 10 setups, rank by 10 day percent normalized ATR
Exit Rules:
Cover the position market-on-close on the same day as the entry (no holding positions overnight)
The first thing I notice looking at this list of rules is that there may be excessive complexity within the system. In my opinion, there seem to be a lot of rules. I have a feeling we might be able to get away with fewer rules when we dig in and tear apart the system. Also, a 39 day ATR? That seems oddly specific. I tend to get a little suspicious when very specific parameters like that are used. Why not just round to an even 40? We will get to the bottom of that eventually.
Before we get too bogged down by the number of rules and specificity of some parameters, let’s continue with understanding the system. The premise is as follows: define a trading universe of stocks priced $10 or higher that have had an average volume of over 1,000,000 shares traded per day and within the Russell 1000 index. That’s a relatively liquid basket of stocks, and higher-priced stocks generally means slippage is less of an issue on a percentage basis—so far, so good.
Now, using that stock universe, filter based on stocks whose short-term volatility resides in a range from 1% to 20% and whose long-term volatility resides in the range of 1% to 8%. Also, ensure there is a trend in the stock measured via the ADX filter being greater than 35. Finally, if the stock has a green candle of 5% or greater today, place a limit order 5% higher than today’s close to potentially be executed tomorrow. If that limit order is executed the next day, the system will sell the position market-on-close, ensuring nothing is held overnight.
The general premise behind the system is nothing new or novel, but an idea doesn’t necessarily have to be unique to be pr

---

*Imported from Substack on 2026-04-25*
