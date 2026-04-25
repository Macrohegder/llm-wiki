# How Correlation Between Strategies Affects Your Portfolio Risk

**Source**: [[2026-04-25-How-Correlation-Between-Strategies-Affects-Your-Portfolio-Risk]] | [Algomatic Trading](https://algomatictrading.substack.com/p/how-correlation-between-strategies)
**Date**: 2026-04-25
**Tags**: #article #substack #strategy

## One-Sentence Summary

> How Correlation Between Strategies Affects Your Portfolio Risk
Why combining strategies doesn't automatically reduce risk and what to do about it
Algomatic Trading
Apr 12, 2026
12
2
Share
You’ve built...

## Key Insights

1. **原文来源**: [Algomatic Trading](https://algomatictrading.substack.com/p/how-correlation-between-strategies)

## Full Content

How Correlation Between Strategies Affects Your Portfolio Risk
Why combining strategies doesn't automatically reduce risk and what to do about it
Algomatic Trading
Apr 12, 2026
12
2
Share
You’ve built a strategy that works. Great.
Now you build another one. Also works.
You put them both in your portfolio and assume the risk has been cut in half.
It hasn’t.
Not automatically, anyway.
Whether combining strategies actually reduces your risk or just gives you the illusion of diversification comes down almost entirely to one thing: correlation.
Get this right and your equity curve gets smoother, your drawdowns get shallower, and you can size up with more confidence.
What Correlation Actually Means in This Context
In trading, correlation describes how similarly two strategies behave over time. Specifically: when one strategy is losing money, what is the other one doing?
A correlation of +1.0 means they move together perfectly, up together, down together. A correlation of 0 means they’re completely independent. A correlation of -1.0 means they move in opposite directions, when one is losing, the other is gaining.
For portfolio purposes, lower correlation is almost always better. You want strategies that have their bad periods at different times. That’s the entire game.
But if you calculate the total correlation with two strategies for let’s say 10 years back in a backtest you will probably get a very high number if it’s between two profitable strategies because overtime they both move up and to the right, that’s why it’s specifically useful to use drawdown correlation in systematic trading and not the performance correlation.
The basic steps to calculate drawdown correlation:
Calculate the running drawdown for each strategy at every point in time meaning how far each strategy is currently sitting below its peak equity at that date
You now have two drawdown series (e.g. Strategy A is -8%, Strategy B is -3% on day X)
Run a standard Pearson correlation on those two drawdown series instead of on the return series
However, there are purposes for using very similar strategies as well, let’s say you only have a single mean-reversion strategy on Nasdaq, if that strategy would fail and eventually start to decay rapidly you want to be able to turn that strategy off and replace it with a similar type but another strategy that works. For this reason I actually believe similar strategies have a purpose as well as long as they are robust.
A Simple Example: The Same Strategy Twice
Imagine you run a mean-reversion strategy on the S&P 500. It goes through a rough time in a trending market, say a sustained uptrend where every pullback just keeps going. That’s a normal rough patch for that type of strategy.
Now imagine you add a second strategy, also mean-reversion, also on a major equity index. When the S&P is trending hard, European indices probably are too. Both strategies hit their rough patches at the same time. Your drawdown is just as deep as if you’d run one strategy. You’ve doubled your capital at risk but got almost nothing in return for it.
High correlation between your strategies means your worst periods stack on top of each other. The losses don’t cancel, they compound.
Join 7,500+ traders learning systematic trading. Premium members get full access to all my Substack strategies.
Subscribe
What Good Diversification Looks Like
Contrast that with pairing a mean-reversion strategy with a trend-following strategy. They have fundamentally different requirements from the market. Mean-reversion needs range-bound, choppy conditions. Trend-following needs sustained directional movement.
In a trending market, your mean-reversion strategy struggles, but your trend-following strategy thrives. In a choppy, directionless market, the opposite is true. The bad periods don’t overlap. Your overall equity curve smooths out considerably.
The total return of the portfolio isn’t necessarily higher, but the journey to get there is much more consistent, and the maximum drawdown is often dramatically lower. That matters enormously when you’re trying to stay in the game long enough for the edge to play out.
How to Actually Measure It
The standard way is to calculate the Pearson correlation coefficient between the daily or weekly returns of each strategy. In ProRealTime, you can export your strategy equity data and run this in a spreadsheet/python.
A rough guide for interpreting the results:
0.7 to 1.0: High correlation. These strategies are too similar. Adding the second one adds risk, not diversification.
0.3 to 0.7: Moderate correlation. Some benefit, but limited.
0.0 to 0.3: Low correlation. Solid diversification. This is what you’re aiming for.
Below 0: Negative correlation. Excellent. Each strategy partially hedges the other.
Example correlation matrix with a heatmap that I use with python
Don’t stop at pairs either. Once you have three or more strategies, build a full correlation matrix, every strategy against every other. Something might 

---

*Imported from Substack on 2026-04-25*
