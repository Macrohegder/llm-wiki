# Increasing Robustness & Smoothing Returns: Re-engineering The 2-ETF Trading Strategy

**Source**: [[2026-04-25-Increasing-Robustness-&-Smoothing-Returns:-Re-engineering-The-2-ETF-Trading-Strategy]] | [TradeQuantiX](https://www.tradequantixnewsletter.com/p/this-strategy-is-stable-during-adverse)
**Date**: 2026-04-25
**Tags**: #article #substack #strategy

## One-Sentence Summary

> Premium Content Vault
Increasing Robustness & Smoothing Returns: Re-engineering The 2-ETF Trading Strategy
Developing My Own Version Of The Simple 2-ETF Strategy Shared By The Algomatic Trading Databa...

## Key Insights

1. **原文来源**: [TradeQuantiX](https://www.tradequantixnewsletter.com/p/this-strategy-is-stable-during-adverse)

## Full Content

Premium Content Vault
Increasing Robustness & Smoothing Returns: Re-engineering The 2-ETF Trading Strategy
Developing My Own Version Of The Simple 2-ETF Strategy Shared By The Algomatic Trading Database
TradeQuantiX
Jun 17, 2025
∙ Paid
16
4
Share
Welcome to the “Systematic Trading with TradeQuantiX” newsletter, your go-to resource for all things systematic trading. This publication will equip you with a complete toolkit to support your systematic trading journey, sent straight to your inbox. Remember, it’s more than just another newsletter; it’s everything you need to be a successful systematic trader.
Introduction:
Recently, the newsletter
The Algomatic Trading Database
shared a 2 ETF strategy that beat the Nasdaq 100. The Algomatic Trading Database found the system concept on X and decided to test the idea himself, sharing his results in his newsletter.
This strategy consisted of an allocation of 33% to the TQQQ ETF (3x leveraged Nasdaq 100) and a 67% allocation to the BTAL ETF (market neutral, short-beta exposure).
What interested me about this strategy was that it outperformed the Nasdaq 100 on both an absolute and a risk-adjusted basis, meaning it had lesser drawdowns while also achieving higher compound annual growth. Hence, I was inclined to do my own research on the concept. You can check out the original article here:
Algomatic Trading Database
Strategy #2: This Simple 2-ETF Strategy Has Outperformed the Nasdaq for 13 Years
A once‑a‑year rebalance between an anti‑beta ETF and a 3× Nasdaq fund has compounded at 19.6 % since 2012 with a –15.7 % max drawdown…
Read more
a year ago · 36 likes · 11 comments · Algomatic Trading
In this article, I would like to take the original strategy concept and decompose it. I will discuss what I think is great about it, as well as some of the drawbacks and risks associated with the strategy. Then, I will create my own version of this strategy which addresses some of the risks I will outline.
The Algomatic Trading Database Original Strategy:
Let’s first start by sharing what the original strategy results looked like:
Looks like a pretty good starting point! Outperformance to the Nasdaq 100 over the long term with lesser drawdowns? Sign me up!
Well, not so fast. We have to do our own research on the idea first. Never blindly trust a trading system found online or even in a book. Do your own research!
That’s exactly what we will do in this article.
Before I start working on the strategy, let me first discuss some aspects of this strategy that I think are great.
Original Strategy Benefits:
One of the key features that makes this strategy interesting is its simplicity, holding only two ETFs. It doesn’t get much simpler than that.
Additionally, the fact that it only rebalances yearly makes it extremely easy to execute and more tax-efficient.
It also utilizes a technique, often referred to as return stacking, which makes this strategy capital-efficient. Rather than buying the QQQ ETF, it buys a 3x leveraged version of that ETF called the TQQQ, but with one-third the position size; this results in exposure equivalent to 100% allocation to QQQ. This allows us to have equivalent exposure to the Nasdaq 100 while also freeing up a bunch of capital to be used for other diversifying assets. It’s the equivalent of using margin without having to pay any margin loans. This is a technique which emphasizes capital efficiency and diversification.
Another aspect I like is the strategic use of the BTAL ETF. This is a market-neutral, short-beta ETF, and thus will be inherently uncorrelated to the TQQQ ETF. The BTAL ETF aims to perform well when the broader market declines by employing a strategy that goes long on low-beta U.S. equities (stocks with lower volatility relative to the market) and short high-beta U.S. equities (stocks with higher volatility).
BTAL can therefore be used as a hedging tool or diversifier within portfolios, as its market-neutral approach can help reduce volatility and provide returns uncorrelated with traditional stock markets.
This BTAL ETF exposure is the main driver of the original strategy’s improved risk-adjusted performance compared to the Nasdaq 100. When the Nasdaq 100 is experiencing a drawdown, the BTAL ETF is likely performing in a completely different, uncorrelated manner, leading to a smoother equity curve.
Using the capital efficiency of return stacking with the TQQQ ETF and using the spare capital to allocate to the BTAL ETF, a diversifying asset with a non-correlated return stream, is why the system results in improved risk-adjusted metrics when compared to the Nasdaq 100.
Original Strategy Drawbacks and Risks:
While there are many aspects of this strategy that I like, there are some risks and drawbacks inherent to the original strategy that I would like to address as well.
The first is the risk inherently baked into using leveraged ETFs. It is likely obvious, but the risk of a leveraged ETF is the fact that it uses leverage. In this case, the strat

---

*Imported from Substack on 2026-04-25*
