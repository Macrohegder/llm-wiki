# Trading System Investigation:               Series 1 - Part 1

**Source**: [[2026-04-25-Trading-System-Investigation:---------------Series-1---Part-1]] | [TradeQuantiX](https://www.tradequantixnewsletter.com/p/trading-system-investigation-series)
**Date**: 2026-04-25
**Tags**: #article #substack #strategy

## One-Sentence Summary

> Premium Content Vault
Trading System Investigation:               Series 1 - Part 1
A deep dive into a short term trading system found online. Is it worth trading?
TradeQuantiX
Sep 30, 2024
37
12
1
Sh...

## Key Insights

1. **原文来源**: [TradeQuantiX](https://www.tradequantixnewsletter.com/p/trading-system-investigation-series)

## Full Content

Premium Content Vault
Trading System Investigation:               Series 1 - Part 1
A deep dive into a short term trading system found online. Is it worth trading?
TradeQuantiX
Sep 30, 2024
37
12
1
Share
Hey, TradetroniX here, welcome to the first article of a four part mini series where we will do some trading system investigation. If you enjoy the content, please feel free to subscribe. Also, if you feel inclined, constructive criticism is always welcome, so let me know if you have any. Finally, the liability notice:  everything discussed is for educational purposes only and not meant to be used as investment advice. With that out of the way I hope you enjoy, now let’s jump into it!
Introduction
One thing that systematic traders stumble across often are online articles or videos sharing trading strategies for free. This is great for the idea generation process, but how do we know if we can actually trade these free strategies? Well, we need to code them up and test them ourselves! Never blindly trust a strategy (free or paid), we must always put in the work to prove these strategies are real, robust, and worthy of our hard earned capital. Most strategies published online are garbage in my experience, but sometimes there is some good stuff out there. The only way to find out is to investigate the trading system ourselves, which is what this mini series is going to do.
Thanks for reading Systematic Trading with TradetroniX! Subscribe for free to receive new posts and support my work.
Subscribe
Today, I am going to go over a strategy shared for free publicly in a webinar by Laurens Bensdorp and Alexei Rudometkin. I will perform the following:
Introduce the rules of the system they shared
Code the system into my backtesting platform (I use Real Test)
Show some trade examples
Discuss strengths/weaknesses of this strategy
Share the code of the system I coded attempting to reproduce the results shown in the free webinar
Then, in article parts 2, 3, and 4, I will continue the investigation of this system with the following items:
Try to improve the strategy with an In Sample and Out of Sample approach
Test the improvements on out of sample data
Discuss robustness of the strategy
Talk about how to modify the trading system to make it fit your needs
And of course, share the final system code
You may be thinking to yourself “huh? this article isn’t starting from an original idea? He’s leveraging something from someone else?”. Yes, that’s correct. Many if the trading systems I trade live are derived from some idea someone else shared. I take those shared ideas, try to emulate them to ensure I understand them, then try to modify the idea to make it unique to me and fit my objectives. Not every idea has to be 100% original. What’s important is you validate the idea is sound, do your own due diligence, and make the idea work for you. This article series is going to go through exactly how to do that.
Before I go any further, let me just say I have the upmost respect for Laurens Bensdorp and Alexei Rudometkin. They are real traders who provide a mentoring service to help beginners become better traders. Any comments I make in this article series are not in any way meant to be disrespectful to either Laurens or Alexei. With that said, lets begin!
The Baseline System Rules and Initial Thoughts
First, let’s introduce the baseline system which was discussed in the webinar.  The idea behind the system is a short term mean reversion approach on the long side. The system buys well performing stocks when they are slightly oversold in the short term, holds the trades for a few days, then exits at a small profit or a small loss, depending on how the trade behaves.
The entry rules are as follows:
Stock is in the S&P 500 universe
Stock is greater than $1
Stock dollar volume is in the top 50% of current S&P 500 stocks
Stock percent volatility (defined by 10 day ATR/C) is between 1% and 40%
Stock has returned at least 10% in the last 100 trading days
3 day RSI is below 20
Stock has had two down days in a row
7 day ADX is greater than 30
Hold up to 10 equally sized positions at a time
If there are more than 10 candidates available for trading, rank by the one year highest rate of change (place orders for the stocks that have gone up the most in one year)
Enter the next day with a limit order 1% below the close of the previous day
The exit rules are as follows:
Intraday initial stop of 2 ATR’s (10 day ATR)
Intraday 2.5 ATR trailing stop  (10 day ATR)
Intraday 4% profit target
My initial thought is this system has a lot of rules. A handful of the rules are used to define the universe the system will trade, which is important. For a short term system like this one, I would expect the expectancy to be on the lower end, so you want to ensure the universe being traded has sufficient liquidity to mitigate slippage. Still, there are many other entry rules and three exit rules. From personal experience, the more rules a system has the easier it 

---

*Imported from Substack on 2026-04-25*
