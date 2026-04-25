# Portfolio Development Series - Part 10

**原文链接**: https://www.tradequantixnewsletter.com/p/portfolio-development-series-part-660

**发布时间**: Oct 20, 2025

**抓取时间**: 2026-04-25 09:04:48

---

## 摘要

Premium Content Vault
Portfolio Development Series - Part 10
Developing a U.S. ETF Mean Reversion System
TradeQuantiX
Oct 20, 2025
∙ Paid
13
2
1
Share
Welcome to the “Systematic Trading with TradeQuantiX” newsletter, your go-to resource for all things systematic trading. This publication will equip you with a complete toolkit to support your systematic trading journey, sent straight to your inbox. Remember, it’s more than just another newsletter; it’s everything you need to be a successful systematic trader.
Introduction:
I’ve received a request from several readers to convert the portfolio we developed is part of the Portfolio Development Series to focus solely on U.S. markets. While I’m a big believer in global diversification and trading as many markets as possible, there are reasons to...

---

## 全文

Premium Content Vault
Portfolio Development Series - Part 10
Developing a U.S. ETF Mean Reversion System
TradeQuantiX
Oct 20, 2025
∙ Paid
13
2
1
Share
Welcome to the “Systematic Trading with TradeQuantiX” newsletter, your go-to resource for all things systematic trading. This publication will equip you with a complete toolkit to support your systematic trading journey, sent straight to your inbox. Remember, it’s more than just another newsletter; it’s everything you need to be a successful systematic trader.
Introduction:
I’ve received a request from several readers to convert the portfolio we developed is part of the Portfolio Development Series to focus solely on U.S. markets. While I’m a big believer in global diversification and trading as many markets as possible, there are reasons to create a U.S. only portfolio.
For one, some investors are restricted to trading only U.S. equities. Retirement accounts, for example, are often limited to U.S. only equities, and many major U.S. brokers also impose similar U.S. equities only trading restrictions. Given this, I can understand why there’s significant demand from U.S. investors for a U.S. only systematic trading portfolio.
In this article, let’s take a look and see what we can develop in terms of a U.S. specific systematic trading portfolio.
What Systems To Add To The US Only Portfolio:
Let’s start by reviewing what we’ve built so far in the Portfolio Development series, specifically for U.S. markets. Thus far, we’ve created the following U.S. specific systems:
A U.S. large cap mean reversion system:
Portfolio Development Series - Part 3
TradeQuantiX
·
July 21, 2025
Read full story
A set of U.S. large cap momentum systems:
Portfolio Development Series - Part 4
TradeQuantiX
·
August 4, 2025
Read full story
And a set of U.S. hedging systems (three total):
Portfolio Development Series - Part 8
TradeQuantiX
·
September 30, 2025
Read full story
These three systems provide a solid foundation for a mildly diversified U.S. only systematic trading portfolio.
But let’s expand further.
In previous articles (before the Portfolio Development series), I’ve explored other systems for the U.S. market that may be worth adding to this U.S. only portfolio, including the following:
A U.S. ETF tactical asset allocation system:
Increasing Robustness & Smoothing Returns: Re-engineering The 2-ETF Trading Strategy
TradeQuantiX
·
June 17, 2025
Read full story
And a set of U.S. large cap trend following systems:
Trading System Investigation Series 3
TradeQuantiX
·
June 3, 2025
Read full story
If we start by taking the three U.S. strategies developed as part of the Portfolio Development series and combined those with the two systems from previous articles, we’re working toward a robust five-system portfolio.
And remember, some of these systems contain sub-systems on different markets, or sub-systems looking for different market conditions to be met, so really its like an 11 system portfolio.
But let’s pause and assess what system types we have and what system types we might be missing.
We’re pretty well-covered on the hedging side, with three different shorting/hedging systems to protect us during adverse market events.
On the trend and momentum side, we’re in good shape with two trend following systems on two different large cap universes; and one momentum system across three different U.S. large-cap universes.
However, when it comes to long side mean reversion, we only have one U.S. mean reversion system. All other major system categories (trend following, momentum, hedging/shorting) we have at least two different systems; but for long side mean reversion, we only have one system currently.
This suggests that long side mean reversion is a category where our portfolio may be lacking. So, let’s develop another mean reversion system to enhance and diversify this portfolio further.
Planning The Mean Reversion System:
The existing mean reversion system buys oversold stocks in the Nasdaq 100 and S&P 100. Personally, I’ve never found much success trading mean reversion on small caps, especially in recent years. From my experience, mean reversion systems on small-cap equities have significantly degraded in recent times, with many systems failing outright, particularly during 2022 and 2023.
It could just be me, maybe my ideas are not good enough, but I can’t seem to create a stable system on small caps. I know many other systematic traders who have experienced the same as well. Hence, why up until now I have focused my mean reversion development on on large cap stocks.
I have a theory that the passive flows from large funds find their way into large cap U.S. equities, which tends to make them more mean reverting. With flows buying nearly every dip. There’s always a large institutional bid, hence why they tend to always rebound after a sell off.
Leveraging the same theory, large cap equity ETFs should follow a similar phenomena. Hence, I have just recently started to explore and develop mean reversion systems on U.S. ETFs. I have found a lot of success here and have been able to develop multiple systems with very stable results.
When developing ETF trading systems, there are a few traps to avoid. One issue I see with many ETF mean reversion systems is that they’re often built around only a single ETF, like an S&P 500 mean reversion system, a NASDAQ 100 mean reversion system, or a Bitcoin mean reversion system, etc. I take issue with this approach because it’s easy to overfit a system to a single time series.
If the behavior of the ETF shifts in the future, then the system could suffer significant losses. It’s also extremely easy to overfit to the limited data in just one ETF time series. Hence, why single ETF systems make me nervous.
To help avoid this risk, I prefer to develop ETF mean reversion systems that trade a basket of ETFs. This ensures some level of diversification and reduces the risk of curve-fitting as I have more data points to develop the system with.
After I’ve chosen the basket of ETFs I’d like the system to trade, I like to develop the system using just a few of the ETFs, from say 2000 to 2018. Then, I’ll validate the system on the unseen ETFs and on the unseen timeframe. Then I’ll trade the final system across the entire basket of ETFs. This provides more out-of-sample data for validation and adds diversification within the system.
I also avoid choosing ETFs that all belong to the same asset class. For example, I don’t want to trade only large-cap stock ETFs like the S&P 500 or NASDAQ 100, as these are highly correlated (though they do mean revert well, likely due to the passive flows theory I mentioned a few paragraphs ago).
Instead, I take more of an all-weather portfolio or tactical asset allocation approach. This ensures the ETF basket covers a broad range of asset classes. I include ETFs for assets like bonds and gold for example, to avoid overexposure to a single asset class.
The danger of focusing on one asset class is that during crises, correlations within equities tend to converge to one. Going all in on equities during the COVID crash, for instance, could be catastrophic if the systems timing is off.
By including other asset classes, which behave differently during adverse market moves, the system is more diversified and will likely not be “all in” during a major market crash. For example, equities may be crashing, while gold may be bouncing to the upside, resulting in a winning gold trade and losing equities trade, smoothing the equity curve.
This post is for paid subscribers
Subscribe
Already a paid subscriber?
Sign in
Previous
Next

---

*由 Substack Strategy Tracker 自动抓取*
