# Portfolio Development Series - Part 8

**Source**: [[2026-04-25-Portfolio-Development-Series---Part-8]] | [TradeQuantiX](https://www.tradequantixnewsletter.com/p/portfolio-development-series-part-140)
**Date**: 2026-04-25
**Tags**: #article #substack

## One-Sentence Summary

> Premium Content Vault
Portfolio Development Series - Part 8
Implementing Hedging Within The Portfolio
TradeQuantiX
Sep 30, 2025
∙ Paid
16
9
3
Share
Welcome to the “Systematic Trading with TradeQuantiX...

## Key Insights

1. **原文来源**: [TradeQuantiX](https://www.tradequantixnewsletter.com/p/portfolio-development-series-part-140)

## Full Content

Premium Content Vault
Portfolio Development Series - Part 8
Implementing Hedging Within The Portfolio
TradeQuantiX
Sep 30, 2025
∙ Paid
16
9
3
Share
Welcome to the “Systematic Trading with TradeQuantiX” newsletter, your go-to resource for all things systematic trading. This publication will equip you with a complete toolkit to support your systematic trading journey, sent straight to your inbox. Remember, it’s more than just another newsletter; it’s everything you need to be a successful systematic trader.
Introduction:
In the previous article in this portfolio development series, we finally combined the four systems we created and evaluated the portfolio’s performance. Even with just four systems, the portfolio performance was very solid, yielding a a fantastic starting portfolio to build from.
While the portfolio didn’t fully meet all the objectives we originally outlined, it came extremely close. Considering the portfolio consists of only four systems, I am not concerned, there is still plenty of room to build on top of the four system portfolio. To further improve the portfolios performance, it was decided that the next step is to add a hedging system, to benefit from adverse market events.
Why Adding Short Side Exposure Is Important:
Currently, the portfolio is long-only, so it’s expected to outperform during bull markets, but go flat or enter drawdown during bear markets. Consider a time period such as the 2008 bear market: many systems within the portfolio went into drawdown, and remained in a drawdown for years.
When looking at a backtest over 30 years, we loose perspective of how long the systems were in a drawdown. Going forward in time into the future, we do not have the luxury of knowing when we will hit new equity highs. We have to remember we are going to live that equity curve everyday, in real time. Would you be able to continue to execute the orders of your system for years while your system remains in drawdown?
Therefore, creating the smoothest equity curve possible is desired. Having short side systems to profit during adverse market events will help with that smoothing effect; as shorting systems are typically uncorrelated to long systems.
So, what kinds of systems could we develop to benefit from adverse market events? There are likely many solutions, but I categorize them into a few different types of approaches.
The first is a system that shorts the market during a downtrend. This could involve shorting via breakouts to the downside or mean-reversion strategies which short local relief rallies within a larger downtrend.
Another approach is to use what I call long-volatility strategies. During adverse market events, volatility typically spikes. A system that goes long volatility can be highly profitable during volatile bear markets. However, these systems are like insurance policies. You pay a premium every month, slowly bleeding cash, until a crisis hits, only then do you receive a payout.
Long-volatility systems work similar to buying insurance. During normal market conditions, you may lose money gradually, but when a crash inevitably occurs, the system spikes with profits, capitalizing on the surge in volatility.
In this article, I’ll explore all three of these concepts. We’ll implement a long volatility system, a system that shorts breakouts to the downside during bear markets, and a system that shorts relief rallies in bear markets using mean reversion.
I can almost guarantee these systems won’t look pretty on their own, but that’s not the point. The goal is to smooth portfolio equity curve during periods of time when the long side systems underperform.
Short Side Mean Reversion:
The first system we’ll cover is a short-side mean-reversion system on equity and bond ETFs. This system trades the SPY, QQQ, and TLT ETFs on the short side.
If you recall the mean-reversion system from Part 3 of this series, we used the concept of scaling in to the position to obtain an average price during oversold conditions. For this short mean reversion system, we’ll follow a similar approach but scale into an overbought position.
The system works by measuring the RSI and placing limit orders at various overbought RSI levels, scaling into the position over a few days. This technique provides more stable results and is less prone to curve fitting, as it doesn’t rely on a single set of parameters that we hope will remain optimal into the future. Instead, it diversifies across multiple parameter sets.
You can also think of this as scaling in by signal strength. As the overbought signal strengthens via the RSI increasing, the system scales in more aggressively, increasing position size with the signal’s intensity.
As a simple way to emulate this scaling in, I developed four versions of this RSI mean reversion shorting system. Each uses a different RSI value for entry and exit. See the end of this article for the code.
You can see the equity curve for this system below. Note the four equity curves on the bo

---

*Imported from Substack on 2026-04-25*
