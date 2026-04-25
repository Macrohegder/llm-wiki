# Most Systematic Traders Use Regime Filters Improperly

**原文链接**: https://www.tradequantixnewsletter.com/p/most-systematic-traders-use-regime

**发布时间**: Nov 17, 2025

**抓取时间**: 2026-04-25 09:04:58

---

## 摘要

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
Regime filters are a common component within trading systems. I would say about half of my trading systems have some sort of regime filter built in. While not a required component, regime filters can be a nice overlay on top of an already well-built system, if done ri...

---

## 全文

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
I’m here to tell you that does not exist. Just like the Holy Grail trading system does not exist, and getting rich quick does not exist; regime filters that make strategies perfect do not exist. In fact, any regime filter that makes a strategy perfect in a backtest will probably make that strategy worse in live trading.
If you ever find yourself developing a strategy and you just can’t get the strategy to work, but then you slap a regime filter on top of it, do some optimization, and then the strategy looks tradeable, I would take a step back and consider what you actually just did.
A regime filter is not a Band-Aid; it’s simply a finishing touch on an already high quality system.
It is not the fix to a failing system.
If the underlying system is failing, but the regime filter appears to fix it, I would probably not trade that system.
I’ve learned this lesson the hard way in the past, by using ever more restrictive regime filters to fix a failing system. You find yourself always chasing performance. You fix the system by increasing the restrictiveness of the regime filter, but going forward in time, the system continues to degrade, so you make the regime filter even more restrictive. Rinse and repeat, always chasing the performance in the backtest, but never actually achieving it in your actual account.
Long story short, regime filters can help you sidestep some unfavorable market times, but the system should still be tradeable without a regime filter. Now, that doesn’t mean the system is amazing without the regime filter, but it should still be tradeable. If a system has a 30% drawdown without a regime filter and a 20% drawdown with the regime filter, I would generally think that’s acceptable.
Heck, even if the system without the regime filter had a 40% to 50% drawdown but with the regime filter had a 20% to 30% drawdown, I might even consider that acceptable. Now, you’re probably saying,
“40% to 50% drawdown? That’s not tradeable!”
And yeah, I get your point, but consider buy-and-hold, that has a 60%+ drawdown, and there are hundreds of millions of people trading that strategy, so I would consider that tradeable.
But if the system without the regime filter has an 80% drawdown and then with the regime filter only has a 20% drawdown, that might be pretty worrisome.
I guess the point that I’m getting at is the regime filter should not be the only reason that the system works. The system should work and have some sort of edge without it. The regime filter is just a helping hand to better keep the system on the right side of macro events, on average.
The Three Baseline Systems:
Now that you understand my thought process on regime filters, let’s test some out on a few systems. I will test these regime filters on three different systems. All three of these systems have been developed in a previous article, and I’m going to leverage them as our regime filter test dummy systems.
These three systems are the US momentum system, the US trend system, and the ASX trend system. See the links below to learn more about these systems, if interested:
US Momentum:
Portfolio Development Series - Part 4
TradeQuantiX
·
August 4, 2025
Read full story
US Trend:
Trading System Investigation Series 3
TradeQuantiX
·
June 3, 2025
Read full story
ASX Trend:
Portfolio Development Series - Part 5
TradeQuantiX
·
August 25, 2025
Read full story
I’ll note, the US systems already have a simple regime filter built into them, but the ASX system does not. So first, let me show the US systems with and without the regime filter so that we can better understand the starting point for comparisons later on. The ASX system does not have a regime filter, so there will be no with and without regime filter comparison.
US Momentum System With Regime Filter (Index > 200 day moving average):
Note:
This system splits its capital across the S&P 100, Russell 1000, and Nasdaq 100 universes. The yellow, red, and green equity curves represent the equity curves of these three universes, the dark blue is the result of these three universes combined together. I consider this as one system with intentional diversification between universes within it.
US Momentum System Without Regime Filter :
US Trend System With Regime Filter (SPX or NDX Close > Close 200 Days Ago):
Note:
This system splits its capital between two different ranking mechanisms (momentum and low-volatility, two real market effects). The red and green equity curves represent the equity curves of these two ranking mechanisms, the dark blue is the result of these two ranking mechanisms combined together. I consider this as one system with intentional diversification between ranking mechanisms within it.
US Trend System Without Regime Filter:
ASX Trend System Without Regime Filter (baseline system does not use a regime filter):
You’ll notice all the systems still work fine without a regime filter. That’s because these systems are robust and built on sound fundamental principles.
The index filter is just a small and simple addition to try and improve performance a little more by putting the system on the right side of the general market trend.
Regime Filter Testing:
Using the three systems above, I will test out multiple different regime filters and show the impact on the three systems. I chose three different systems on two different markets because regime filters behave differently depending on the context of the underlying system. Hence, testing across three systems will give a better feel for the significance of the regime filter.
The regime filters that I plan to test are listed below. Each regime filter implemented will be tested in two ways. The first is applying the regime filter to both the entry and exit logic. Meaning only enter if the regime filter says so, then if the regime filter turns off, exit the position.
The second way is to only apply the regime filter to the entry and let the system exit naturally. This means only enter if the regime filter says so, but if the regime filter turns off, then do nothing and let the system exit its positions via trailing stop or other system specific method of exiting individual positions.
The regime filters to test are listed below:
Enter if VIX < x, Exit if VIX > x
Enter if VIX < x, No index based exit
Enter if Index > MA, Exit if Index < MA
Enter if Index > MA, No index based exit
Enter if Index within x% of recent high, Exit if Index below x% of recent high
Enter if Index within x% of recent high, No index based exit
Enter if Index return is greater than x% in y timeframe, Exit if Index return is less than x% in y timeframe
Enter if Index return is greater than x% in y timeframe, No index based exit
Enter if x% of stocks > MA (breadth filter), Exit if x% of stocks < MA (breadth filter)
Enter if x% of stocks > MA (breadth filter),  No breadth based exit
One at a time, I tested and applied these regime filters to the three test systems. Below, I’ll go one by one and show the result of the regime filters on the three test systems and compare them back to the baseline so you can understand how each regime filter stacks up.
I’m about to show a lot of plots and tables, so let me quickly share how its all organized. I will show the regime filter tests in the same order as listed above. Then I will show a table showing the sensitivity of that regime filters to different parameter values, with the bottom rows in the table reserved to show the baseline results for benchmarking.
Then below the table I will show 1-2 equity curves for the system. These equity curves will be the system with the relevant regime filter applied, corresponding with one of the parameters in the table. I chose to show the equity curves that I thought where interesting and/or representative of the index filters results on the system. I will show these tables and equity curves for each of the three systems. Then I will move onto the next regime filter and repeat.
It’s also worth noting, the baseline results in the bottom of the table for US systems are the results with the regime filters. I figured since the nominal design of the US systems had regime filters, it would be more meaningful to compare those results to the results of implementing different regime filters.
On the other hand, the ASX system baseline result does not have a regime filter because the nominal design did not use a regime filter. So, for the ASX system we will be looking to see if a regime filter can improve the system and for the US systems we will be looking to see if a different regime filter is potentially “better” than the one already used.
Enter if VIX < x, Exit if VIX > x:
US Momentum System:
US Trend System:
ASX Trend System:
Enter if VIX < x, No index based exit:
US Momentum System:
US Trend System:
ASX Trend System:
Enter if Index > MA, Exit if Index < MA:
US Momentum System:
US Trend System:
ASX Trend System:
Enter if Index > MA, No index based exit:
US Momentum System:
US Trend System:
ASX Trend System:
Enter if Index within x% of recent high, Exit if Index below x% of recent high:
Note:
HHV value is the lookback value. The index filter was coded as such, where 0.8 was hardcoded and the lookback (HHV_Value) was what was optimized:
Extern($$SPX, C > HHV(C, HHV_Value) * 0.8)
US Momentum System:
US Trend System:
ASX Trend System:
Enter if Index within x% of recent high, No index based exit:
Note:
HHV value is the lookback value. The index filter was coded as such, where 0.8 was hardcoded and the lookback (HHV_Value) was what was optimized:
Extern($$SPX, C > HHV(C, HHV_Value) * 0.8)
US Momentum System:
US Trend System:
ASX Trend System:
Enter if Index returns greater than x% in y timeframe, Exit if Index returns less than x% in y timeframe:
Note:
ROC value is the lookback value. The index filter was coded as such, where 0 was hardcoded and the lookback (ROC_Value) was what was optimized:
Extern($$SPX, ROC(C, ROC_Value) > 0)
US Momentum System:
US Trend System:
ASX Trend System:
Enter if Index returns greater than x% in y timeframe, No index based exit:
Note:
ROC value is the lookback value. The index filter was coded as such, where 0 was hardcoded and the lookback (ROC_Value) was what was optimized:
Extern($$SPX, ROC(C, ROC_Value) > 0)
US Momentum System:
US Trend System:
ASX Trend System:
Enter if x% of stocks > MA (breadth filter), Exit if x% of stocks < MA (breadth filter):
Note:
Breadth value is the lookback value. The index filter was coded as such, where 0.35 was hardcoded and the lookback (Breadth_Value) was what was optimized:
Filter12_BreadthFilter1:	#Sum InOEX
Filter12_BreadthFilter2:	#Sum If(InOEX, C>MA(C, Breadth_Value), 0)
Filter12:	Filter12_BreadthFilter2 / Filter12_BreadthFilter1 > 0.35
US Momentum System:
US Trend System:
ASX Trend System:
Enter if x% of stocks > MA (breadth filter),  No breadth based exit:
Note:
Breadth value is the lookback value. The index filter was coded as such, where 0.35 was hardcoded and the lookback (Breadth_Value) was what was optimized:
Filter12_BreadthFilter1:	#Sum InOEX
Filter12_BreadthFilter2:	#Sum If(InOEX, C>MA(C, Breadth_Value), 0)
Filter12:	Filter12_BreadthFilter2 / Filter12_BreadthFilter1 > 0.35
US Momentum System:
US Trend System:
ASX Trend System:
Summarizing Regime Filter Results:
You’ll notice after going through all of that work to test multiple different regime filters on three different systems that there was no Holy Grail solution that stuck out.
In fact there were many regime filters that actually made the system worse. On the other hand there were a few regime filters that made the risk adjusted metrics of the system slightly better.
While none of these regime filters hit it out of the park in terms of improvement, the real takeaway here is that all of these regime filters lead to a different performance profile of the underlying system. Rather than randomly testing 10s of regime filters and optimizing them to death, what is likely more fruitful is to diversify across regime filters.
If you look back up at the equity curves you can see that some regime filters kick on more often and others kick on less often.
Some regime filters kick on too early while others kick on too late.
One regime filter may have been the best during 2008 but another may be better during 2020.
You never know which will be the best in the future.
Hence why I think the more fruitful opportunity from this study is to be able to diversify across different regime filters, rather than picking the Holy Grail absolute best regime filter.
Let’s discuss this more in the next section.
How To Properly Implement Regime Filters:
Continue reading this post for free, courtesy of TradeQuantiX.
Claim my free post
Or purchase a paid subscription.
Previous
Next

---

*由 Substack Strategy Tracker 自动抓取*
