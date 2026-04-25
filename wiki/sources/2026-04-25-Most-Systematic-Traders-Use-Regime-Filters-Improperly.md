# Most Systematic Traders Use Regime Filters Improperly

**Source**: [[2026-04-25-Most-Systematic-Traders-Use-Regime-Filters-Improperly]] | [TradeQuantiX](https://www.tradequantixnewsletter.com/p/most-systematic-traders-use-regime)
**Date**: 2026-04-25
**Tags**: #article #substack

## One-Sentence Summary

> Most Systematic Traders Use Regime Filters Improperly
How Regime Filters Are Use Incorrectly And How To Fix It
TradeQuantiX
Nov 17, 2025
∙ Paid
24
7
Share
Welcome to the “Systematic Trading with Trade...

## Key Insights

1. **原文来源**: [TradeQuantiX](https://www.tradequantixnewsletter.com/p/most-systematic-traders-use-regime)

## Full Content

Most Systematic Traders Use Regime Filters Improperly
How Regime Filters Are Use Incorrectly And How To Fix It
TradeQuantiX
Nov 17, 2025
∙ Paid
24
7
Share
Welcome to the “Systematic Trading with TradeQuantiX” newsletter, your go-to resource for all things systematic trading. This publication will equip you with a complete toolkit to support your systematic trading journey, sent straight to your inbox. Remember, it’s more than just another newsletter; it’s everything you need to be a successful systematic trader.
Introduction:
Regime filters are a common component within trading systems. I would say about half of my trading systems have some sort of regime filter built in. While not a required component, regime filters can be a nice overlay on top of an already well-built system, if done right.
Regime filters can reduce drawdowns and boost risk-adjusted returns, but they are also the easiest component of a trading system to mess up. In fact, they are probably one of the most common components of a trading system that are implemented improperly.
That’s not because regime filters are difficult to implement, in fact, it’s the opposite. Regime filters are actually too easy to implement, and thus many times lead traders down a path of over optimization and curve fitting to historical data.
In this article, I want to dive into regime filters. I want to define what they should be used for, and what they should not be used for. I will also test out some different regime filters on three different example systems to see the effect of the regime filter.
Note:
I use the terms index filter and regime filter interchangeably, so don’t be confused if I keep flip flopping the terminology.
Why Regime Filters Can Be Problematic:
Why are regime filters so easy to mess up?
Let’s first consider a trading system without a regime filter. Let’s say this trading system has over 1000 trades over the course of a 20-year backtest. 1000 trades is a reasonably respectable sample size. Sure, you could definitely still curve fit a system with 1000 trades, but you’re starting to get to a number of trades where you can actually make reasonable decisions based on a sample size this large.
Let’s say you’ve finished developing this system: you’ve chosen the rules, you’ve chosen stable parameters, and you’re almost happy with the system. The last thing you think is missing is some sort of regime or index filter to try to reduce drawdowns just a little bit more.
So, you start trying index filters, you start optimizing parameters, and before you know it, you’ve cut the drawdown in half and somehow managed to keep the returns of the system exactly the same. Does this sound familiar? If the regime filter boosts the performance of the system that dramatically, I would be hesitant and really consider if that performance increase is actually real.
I see this happen all the time, and I used to do this all the time as well. The problem is you took a system that has a large sample size of data points (trades), and throw an index filter on top which has probably only triggered a handful of times in the backtest.
Maybe there’s only been 10 or 15 times the index filter has triggered over the past 20 years. You’re taking a higher confidence 1000 trade sample size system and diluting that confidence with a regime filter overlay that only has a handful of data points. And if you optimize and fiddle with that regime filter, you’ll find its pretty easy to curve fit to 10-15 data points.
When you go live with this strategy, odds are that this regime filter is actually going to make the results worse in the future compared to the strategy without the regime filter. Even though the underlying strategy may not be curve fit, throwing a curve fit overlay on top of the strategy adds noise and reduces the effectiveness of the underlying signal of the strategy.
Imagine trying to trade a trend following strategy, but every day you had to roll the dice, and every time you roll a 6 you had to sell all of your positions. Then, you could only rebuy all your positions when you roll a 6 again. That’s the equivalent of trading a system with a curve fit regime filter built on top of it.
This is why it is critical to get regime filters right, and by the end of this article, I think you’re going to find that there is no secret sauce to regime filters. So, stop overoptimizing them to death, you are not going to find a perfect result that actually continues with that performance into the future.
There Is No Secret Sauce With Regime Filters:
I know you probably want to hear there’s some secret regime filter that filters out all the drawdowns. Or there’s a special regime filter that tells you exactly when to get in to the market to make the most amount of profits.
I’m here to tell you that does not exist. Just like the Holy Grail trading system does not exist, and getting rich quick does not exist; regime filters that make strategies perfect do not exist. In fact, any regime filter that

---

*Imported from Substack on 2026-04-25*
