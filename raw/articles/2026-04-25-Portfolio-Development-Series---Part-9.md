# Portfolio Development Series - Part 9

**原文链接**: https://www.tradequantixnewsletter.com/p/portfolio-development-series-part-be4

**发布时间**: Oct 12, 2025

**抓取时间**: 2026-04-25 09:04:44

---

## 摘要

Premium Content Vault
Portfolio Development Series - Part 9
Other Considerations Often Overlooked When Creating A Systematic Trading Portfolio
TradeQuantiX
Oct 12, 2025
∙ Paid
10
8
Share
Welcome to the “Systematic Trading with TradeQuantiX” newsletter, your go-to resource for all things systematic trading. This publication will equip you with a complete toolkit to support your systematic trading journey, sent straight to your inbox. Remember, it’s more than just another newsletter; it’s everything you need to be a successful systematic trader.
Introduction:
Up until this point in the Portfolio Development series, the following broad high level topics have been explored:
Planning out what types of systems will be included in the final portfolio
Developing those systems with high quality dev...

---

## 全文

Premium Content Vault
Portfolio Development Series - Part 9
Other Considerations Often Overlooked When Creating A Systematic Trading Portfolio
TradeQuantiX
Oct 12, 2025
∙ Paid
10
8
Share
Welcome to the “Systematic Trading with TradeQuantiX” newsletter, your go-to resource for all things systematic trading. This publication will equip you with a complete toolkit to support your systematic trading journey, sent straight to your inbox. Remember, it’s more than just another newsletter; it’s everything you need to be a successful systematic trader.
Introduction:
Up until this point in the Portfolio Development series, the following broad high level topics have been explored:
Planning out what types of systems will be included in the final portfolio
Developing those systems with high quality development techniques
Combining those systems into the final portfolio and determining allocations.
These are the general concepts that one needs to understand to create a systematic trading portfolio.
But there are other very specific small details that one needs to consider to really get the most out of their systematic trading portfolio.
In this article, I'm going to go into the nitty-gritty considerations. These are the considerations that should be carefully mapped out to ensure your portfolio performs at its best. Thinking through these topics now will help reduce the number of issues that occur after you launch your newly developed systematic trading portfolio.
This article is not necessarily going to be the most entertaining or action-packed, but it is going to be one of the most important.
I will discuss multiple different high-level concepts that you’ll need to understand and consider. These concepts are:
Practical portfolio design considerations
Non-quantifiable portfolio allocation considerations
Quantifiable portfolio allocation considerations
Portfolio external capital considerations
Portfolio expansion over time
Unforeseen portfolio risks
Portfolio live execution considerations
If you do not consider and find solutions for the topics I am going to discuss, then your portfolio will likely suffer.
Practical Portfolio Design Considerations:
The first genre of aspects to consider is practicality. This includes things like time zone considerations, currency conversions, regulatory items, and mental capacity.
Time Zones:
Let’s start with time zones. If you decide to trade a market different from your home market, realize that there will be a time zone difference. This stock market will open and close at a different time than your home stock market.
It's possible that the market may be in a time zone that does not align with your schedule, making it difficult to run a trading system on said market. For example, if you live in Australia and want to trade the US markets, the US market opens around midnight Australia time and closes around 6 am Australia time.
I don’t know about you, but I don’t prefer the night shift. Depending on how the trading system operates, it could be an absolute nightmare to trade.
There are ways around this, though. What I do is place all of my orders during times when the market is closed. The orders sit with my broker and get executed market-on-open when the other country’s market opens. This allows me to place orders when I have the free time to do so; rather than staying up late to place orders exactly when the market opens.
This method works if you trade the daily timeframe, but if you’re trading intraday, then you either need to stay up all night to babysit your system trading the foreign market, or you need to develop very robust automation.
Remember, while you are developing trading systems, the backtest may look great, but if it’s a nightmare to trade, you may not be able to stick with it.
Personally, I trade the USA, Canadian, and Australian markets. I have found a time that works for me when all of these time zones align such that all of the markets are closed. This allows me to process and place the orders for the next market session. I would recommend you open a time zone converter online and look at the time differences across all the markets you plan to trade; then plan out how you intent to account for the time zone mismatches.
The more markets you add across multiple different countries, the more difficult it's going to be to find off-market times. You may find you have to process and place your trades multiple times a day across all the different markets. That could be pretty annoying to do everyday.
Currency Conversions:
Another thing to consider is currency conversions. If you trade a market other than your home market, it is likely there will be a necessary currency conversion to place that trade. Whatever position size your system spits out must be multiplied by the current currency conversion rate to ensure you end up with the correct exposure.
While a currency conversion isn't difficult, it can be an annoying nuance to do every day if not automated. It's also an aspect that is commonly overlooked, leading traders to be either massively under or overexposed in their position sizes compared to what they should be. So, be sure not to forget about currency conversions.
Below is a plot of USD/CAD. Assuming your base currency is USD, when the price goes up, that means you can buy more CAD with your USD; meaning the value of CAD has dropped. I also have a 1-year rate of change plotted at the bottom as well.
Imagine holding a trade between 2014 and 2016, unhedged from currency fluctuations. CAD dropped nearly 50% in value in relation to USD! If you were holding a trade on the Canadian market, the value of that trade would have also dropped 50% in relation to USD.
Regulatory Items:
Another practical nuance to look out for is regulatory items. These are another minor headache to tackle. Be sure that whatever market you plan to trade, you are legally able to trade.
For example, I am from the United States, and therefore, legally, I cannot trade the Indian markets, even though I would like to. If I had not known this ahead of time, I may have potentially bought data for Indian markets and spent a lot of time developing systems just to be frustrated when I found out that these systems were unusable.
Another example would be developing a shorting system on a market that doesn’t allow you to short. You can't short 95% of the stocks on the Australian market. You're lucky if you can get shorts for the top 50 stocks. So, spending lots of time creating an ASX short system is likely going to result in subpar live results and frustration.
There could also be special tax considerations applicable to trading other markets. For example, the London Stock Market charges a tax on all trades of about 0.5%. If I had created a trading system that had low expectancy on the London markets and I did not consider this tax being taken out of my P&L, this could transform the system from being wildly profitable to a system that loses money. So, spend time upfront figuring out if there is a special tax situation to account for before you spend a bunch of time developing your portfolio.
Here’s an example system where I assume no taxes are applied to every trade (but slippage and commissions are applied):
And here is that same system with a 0.5% tax on every trade per the London Stock Exchange’s rules:
Imagine not knowing that the market you plan to trade has this tax, and your system can’t overcome these extra fees, then its performance is severely degraded. Never assume fees are negligible.
Psychological Considerations:
The last set of practical considerations are psychological ones. You could develop a killer system that has amazing performance, but the only downside is it's extremely difficult to execute.
If you have a busy life and a demanding day job, adding a very demanding trading system into that mix could result in disaster. This is why I personally focus on the edges that are relatively easy to exploit so that I do not have to spend a lot of time worrying about execution.
I'm very grateful for this on busy mornings when I wake up late and need to rush out the door to get to work for my first meeting. The fact that I can crack open my trading systems, generate the orders, and place them with my broker in less than 5 minutes makes my morning trading routine a breeze. This is because I don't use convoluted systems to trade.
I designed the systems such that they work synergistically with my life and routine. I don’t bend my life to fit around how a system needs to be traded. So, consider how you’re actually going to be required to trade your portfolio every day and plan the system design accordingly.
Another consideration is if you do not have any sort of automation, but you decide to trade 10+ trading systems, this could lead to overwhelm and mistakes. With every new market you add, you are essentially adding that much more work to your daily trading process. After awhile, there will come a tipping point where the amount of work required to run your systematic trading setup will be so much that you’ll start becoming prone to errors.
This is why some sort of automation is key. Having a batch script to run all your systems and generate your orders is a relatively simplistic thing to create, but it can have a massive impact on your systematic trading every day. Creating some sort of automation will generally save you time, stress, and reduce silly errors. I have a handful of small utility scripts that I use every day to make my life 10x easier and less prone to error.
Non-Quantifiable Portfolio Allocation Considerations:
In this portfolio development series, we have spent a lot of time discussing how to combine all your systems into a final portfolio. We quantified our allocation decisions, but sometimes there are allocation decisions that are non-quantifiable.
Portfolio Allocation (Over)Optimizing:
Once you have a set of trading systems and you go to combine them into a portfolio, it's very easy to think that simply optimizing the allocations to each system and picking the best result is the way to go. Why would you not want to trade that best set of allocation parameters, right?
I'm gonna tell you this is the wrong way to go about it.
Similar to when we develop trading systems, we don't just pick the best parameter for a certain trading rule. Portfolio construction should be treated the same way.
If you were to simply run an optimizer to find the best allocations to each system, what that would result in is an overallocation to the best backtest and an under allocation to the worst backtest.
On the surface, this sounds fine, but this method of blindly finding the best system allocation percentages has a lot of hidden dangers that need to be considered.
Consider: is your best backtest the result of a genuinely well-designed trading system that exploits an edge extremely efficiently? Or has overfitting found its way into the backtest of this system?
Say I built a small portfolio of three strategies:
Strategy 1: amazing performance, likely an overfit strategy
Strategy 2: okay performance, likely not an overfit strategy
Strategy 3: okay performance, likely not an overfit strategy
When I ran an optimization of allocation parameters, the best results based on this optimization were between a 75%-100% allocation to Strategy 1, and a 0%-25% allocation to Strategies 2 and 3. But that’s not ideal; that removes all diversification.
Also, if Strategy 1 fails in the future, and it probably will because it’s likely curve-fit in this example, that’s going to really hurt because we are overexposed to it.
Whereas if we traded all three strategies with a more equal allocation, we would have a much more robust portfolio. In this instance, if one strategy failed, yea, it might suck, but the entire portfolio isn’t going to zero, because there are two other strategies picking up the slack.
Now, when I say overfitting, that doesn't necessarily mean that the system will completely crash and burn during live out-of-sample. It could, but really what I mean is the backtested performance is overstated.
If your backtest says the system should have a 20% return with a 20% drawdown, but in reality, it's slightly curve-fit, and going forward, the return is more like a 15% return with a 30% drawdown, then you're going to be overstating the returns and underappreciating the risk involved in that system.
Assuming this system had the best overall performance in relation to the other systems being considered in the portfolio, then the results of your portfolio optimizer would heavily over allocate to this slightly curve-fit system. Then, during real-time trading, your live results would suffer due to the degradation from curve fitting.
Not only do you get worse results because the system was slightly curve-fit, but it’s being exacerbated by the fact it was also heavily overallocated to. This is why we can't blindly optimize allocations. Sure, optimizing allocations can be a decent starting point to get an idea what allocation to start with, but we need to add another layer of critical thought on top of this.
Geopolitical Risk:
Continue reading this post for free, courtesy of TradeQuantiX.
Claim my free post
Or purchase a paid subscription.
Previous
Next

---

*由 Substack Strategy Tracker 自动抓取*
