---
title: "Reading Bar Charts for Trading: Time, Tick, Volume, Dollar, Information"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/bar-types-trading/"
date: "2020-01-16"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Reading Bar Charts for Trading: Time, Tick, Volume, Dollar, Information

**来源**: [QuantInsti](https://blog.quantinsti.com/bar-types-trading/)  
**日期**: 2020-01-16  
**作者**: QuantInsti

---

## 原文

Reading Bar Charts for Trading: Time, Tick, Volume, Dollar, Information

ByRekhit Pachanekar

Ever since the advent ofcandlestick patterns, every beginner trader has taken an effort to understand them as well as study the candle-stick patterns. But is the OHLC data charted at a fixed time interval, the only way to analyse a company’s stock price? Is the OHLC data the only measure of a company’s performance?

Turns out, there are certain features which are missed when it comes to the OHLC data based on the fixed time interval. In a world where the sooner you find a breakout, the better, the time-based approach to study the stock charts can hamper your performance. But what are the solutions, or better yet, the alternatives?

Well, today we will try to find the answer to those very things. We will cover the following topics:

What are Bars in Trading?

Time and Tick bars

Volume bars

Dollar bars

Bonus content: Information and Imbalance bars

Before we start our journey into the world of bars, let us refresh our understanding of them.

What are Bars in Trading?

Here’s how they look like:

Why are there two types? It’s simple! If the open price was higher than the close price (Red candlestick), then it would be the diagram on the left. In contrast, if the closing price was higher than the open price (Green candlestick), then it will be in shape of the second diagram.

Here, since we know that the open price is always on the left side, it is somewhat easier to read. While it was only in the black colour, modern-day charting software incorporate the red and green colour too.

All right, let’s start with the first bars!

Time and Tick bars

Ok, time bars are the ones you have heard about the most, ever since time immemorial, or since you started reading stock charts. Simply put, after each time interval, say 5 minutes, we take all the OHLC, ie the Open, High, Low, Close prices and plot them in the shape of a bar. These are called Time bars.

Here is an example of a Time bar based chart for Tesla in the period 13 December to 12 January.

But here’s the thing, as we said earlier, time bars do not give us the full picture. Consider a typical trading day which begins at 9:30 am and ends at 4:00 pm. As we know, there is a lot of trading activity which happens at the start and end of the day. Also, the trading activity winds down to a low during the lunch hours.

Thus, if we had time bars, it would not be able to capture this information at all. As long as a transaction happens, the time bar will be created according to the time interval specified. This means that if there was a time bar at 5 min interval, and if there were 1000 transactions occurring at the first five minutes of the day, signifying high market activity, only one time bar would be created. If during 1:30 - 1:35, only 5 transactions happen, one time bar will be created here too.

But why is this important?

The market activity tells us how active the market participants are in buying/selling the stock. Since some strategies work on price moves, it would be great if we came to know of the price moves as they happen and not after the time interval specified for the bar charts.

This is where tick charts come in. Instead of the time interval, we specify the number of transactions after which a bar should be created. Now, as we all know, Tesla Inc. has been one of the most volatile stocks in recent times. Did you know it went past $500 on Jan 13! Now if we knew that the number of transactions is increasing in an exponential manner, it would help us act sooner. In that sense, tick bars would start filling up our screen faster than the time bars and thus give us that edge we need.

The tick charts have better statistical properties than time bars. This helps us when we are creating trading strategies.

Is tick bar the best way to create the bars? Well, not exactly. Consider a case where we said one tick bar represents 100 transactions. Now, in the first tick bar, there were 100 transactions but the total volume traded was 1000. But in the second tick bar, there were some big movements and in 100 transactions, the volume touched 100000. That’s 100 times more than the first tick bar.

Tick Bar 1

Tick Bar 2

Volume

Volume

This huge change in the volume probably signifies something. And this is not captured since a tick bar captures a fixed number of transactions.

So what should we do? Do we have another type of bar?

Volume Bars

As you saw before, the limitation of tick bars was that it was giving equal weightage to a transaction, be it of 1000 volume or just 10. In that sense, while it does give us a better picture of the market activity than the time bar, it doesn’t help us if we want to know the size of the orders.

Think about it, as a trader, you would want to know how quickly the shares are changing hands. Thus, what we do is take the volume data and create a volume bar which is created after a fixed number.

Don’t worry, here’s an example which shows its advantage over the time bar.

Let’s suppose we create a volume after 1000 shares traded. Now, let’s take the example of Tesla. From January 7, Tesla started delivering its Model 3 vehicles to the customers in China. Adding to this, Tesla announced a price cut on its Model 3 thanks to the subsidies announced by the Chinese Government. This led to positive sentiment and traders pushed up the stock price of Tesla above $500 on January 14.

But what does that have to do with Volume bars?

Consider this, if you know that there is positive sentiment about a certain stock and know that the price could trend up, wouldn’t you like to ride the trend. But what can you use as confirmation? Simple, look at the volume of shares traded. But here’s the thing, if you were looking for 5-minute time-interval based time bars and you receive positive news at the second minute, it means you would wait till the fifth minute to confirm your idea. In the meantime, if you had used volume bars, it would have created 3 bars by the fifth minute if we had 3000 shares traded. That’s an edge which volume bars could give a trader.

Well, that sounds simple, doesn’t it?

Now let’s see, time bars are the most simple, but do not give us information related to market activity. Tick bars, on the other hand, help us with the market activity. But tick bars do not give us an idea on how much volume is traded, which is aptly shown by volume bars.

Volume bars are actually awesome, except for one small thing. Consider the Stock of Tesla again. On January 2, 2017, the stock price of Tesla was $320. If you had bought 1000 shares, it would have been $320,000. Now, on Jan 13, 2020, if we were to buy 1000 shares, it would amount to $524 * 1000 = $524,000. That is a lot of difference. Thus, if you are thinking about historical analysis, wouldn’t it make sense to keep everything at the same value.

As you might have guessed, the efficient way to represent the trades is to use the dollar value traded.

The Dollar Bars

Instead of a fixed volume, we create a data bar after a fixed value of shares are traded. Thus, we get a better understanding of the market.

In fact, dollar bars are the best when it comes to statistical analysis as their returns are the most normally distributed when compared to the other bars.

As you might have guessed, the dollar bars and volume bars would stay the same until the price of the share changes.

But are these the only way to display price information? Well, there are a few more.

Information and Imbalance

You must be thinking, how do I graph information on a bar chart? Well, one way is to use the market imbalance. The simplest way is to find the difference between the buy and sell orders. If this difference is more than a certain predefined threshold, we will create more bars to capture that information. Here, the bars could be the dollar, volume or ticks.

The idea of this is to squeeze more information when there are differences in the buy and sell orders. Think about it, when we find more buy orders, it could be that there could be a price rise and vice versa. This will help us make more informed trades in the long run.

Here’s another interesting example. Sometimes institutional investors, actually most of the time, break a large order of say, 10000 shares, into smaller orders of 10 so that the volume of orders is not affected sharply. But we can create a condition where we can identify these kinds of orders and thus create more bars when this condition arises.

Of course, there can be other instances too where you can create more bars to take advantage of market imbalances. Can you think of any?

Conclusion

Great! We have not only understood howtrading candlestick patternswork, but also how we use certain market imbalances to improve our forecasting prowess. Of course, if you want to get into the nitty-gritty of it, you can check out the course onFinancial Data Science and Feature Engineering. The course has the codes and a lot more when it comes to data cleaning and engineering.

Disclaimer: All data and information provided in this article are for informational purposes only. QuantInsti® makes no representations as to accuracy, completeness, currentness, suitability, or validity of any information in this article and will not be liable for any errors, omissions, or delays in this information or any losses, injuries, or damages arising from its display or use. All information is provided on an as-is basis.

---

*Imported from QuantInsti Blog on 2026-04-27*
