---
title: "RSI Indicator Formula and Calculation: Trading Strategies and Python Implementation"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/rsi-indicator/"
date: "2025-03-05"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# RSI Indicator Formula and Calculation: Trading Strategies and Python Implementation

**来源**: [QuantInsti](https://blog.quantinsti.com/rsi-indicator/)  
**日期**: 2025-03-05  
**作者**: QuantInsti

---

## 原文

RSI Indicator: Calculation, Python Implementation and Trading Strategy

ByRekhit Pachanekar

The origin of the Relative Strength Index (RSI) indicator is quite interesting. Created in 1986 by J. Welles Wilder, who was an engineer, land developer first and then a commodities trader, the RSI indicator has come a long way since its origin. Even though J. Welles Wilder was working on commodities when he came up with the RSI indicator, the indicator is quite popular in the technical analysis community with traders using it on all asset classes.

Prerequisites

This blog is beginner-friendly, but having a basic understanding of Python will enhance your learning experience.Start withBasics of Python Programmingto grasp core programming concepts, and if you're new to technical indicators,How to Install TA-Lib in Pythonwill help you integrate them into your trading strategies.To visualize market trends effectively, explorePlotly Python – An Interactive Data Visualization.For a structured learning experience, considerPython for Trading: Basicon Quantra, which covers essential Python concepts specifically for financial markets.

In this blog article, we will not only look at the calculation but also various trading strategies which can be used using the RSI indicator.

We will be covering the following points in this blog article:

History of RSI Indicator

RSI Formula and Calculation

RSI Indicator in Python Using a Real-World Example, With Visualisation in Plotly

Strategies based on RSI indicator

Backtesting an RSI indicator-based trading strategy

Limitations of RSI

History of RSI Indicator

The RSI indicator was created by Welles Wilder Jr in 1978 and published in his book, “New Concepts in Technical Trading Systems.” Interestingly, Mr. Wilder had been working in the real estate industry with two other partners. After a successful project, he sold his share in the firm and was, as Mr Wilder puts it, retired at 38.

At this point in time, Wilder started trading commodities and coming from an engineering background, he looked at technical analysis to understand when to buy and sell. Not getting a clear answer through the tools available at that point of time, he set about creating his own indicators, and the RSI indicator was one of them.

As the name suggests, the RSI indicator value tells us the relative strength of the asset. In other words, the RSI tells us how well the stock is performing (or not) with respect to itself in the past. RSI is counted as a robust technical indicator which can be used to analyse the market and is an important part of the trader’s arsenal as it helps them to make better decisions in timing the market. If you'd like to buildtechnical indicators in Pythonand see RSI coded side-by-side with Bollinger Bands, moving averages, and volume indicators, our dedicated tutorial walks through each with full Python code and charts. Inquant trading, RSI is commonly coded as a systematic signal generator, enabling rule-based entry and exit decisions that remove emotion from the trading process. Of course, like otherindicators, it is always advisable to use more than one indicator as it helps us avoid the limitations and over-dependency on just one.

If you already know how to find the RSI indicator values, jump to the RSI-based strategies here.

RSI Formula and Calculation

Let’s understand how to calculate and graph the RSI indicator now. While you can easily calculate the RSI indicator value with the Python code, but for explanation purposes we will do it manually here:

We will take the closing price of the stock, Apple from Jan 8, 2025, to Feb 13, 2025. The closing price is mentioned in column (1).

We then compare the closing price of the current day with the previous day’s closing price and note them down. Thus, from the table, for 2025-01-10, we get the change in price as (236.59 - 242.43) = -5.84.

Similarly, for 2025-01-13, Change in price = (Current closing price - Previous closing price) = (234.14 - 236.59) = -2.45. We will then tabulate the results in the column mentioned as “Change (2)”. In this manner, we calculated the change in price.

We will now create two sections categorising if the price increased or decreased, with respect to the previous day’s closing price.

If the price has increased, we note down the difference in the “Gain” column and if it’s a loss, then we note it down in the “Loss” column.

For example, on 2025-01-15, the price had increased by 4.58. Thus, this value would be noted in the “Gain” column.

If you look at the data for 2025-01-10, there was a decrease in the price by 5.84. Now, while the value is written as negative in the “change” column, we do not mention the negative sign in the “Loss” column. And only write it as 5.84. In this manner, the table for the columns “Gain (3)” and “Loss (4)” is updated.

In the RSI indicator, to smoothen the price movement, we take an average of the gains (and losses) for a certain period. While we call it an average, a little explanation would be needed. For the first 14 periods, it is a simple average of the values.

To explain it, we will look at the average gain column.

Thus, in the table, the first 14 values would be from (2025-01-10) to (2025-01-30) which is, (0 + 0 + 0 + 4.58 + 0 + 1.72 + 0 + 1.19 + 0 + 0 + 7.07 + 8.39 + 1.10 + 0)/14 = 1.72.

Now, since we are placing more emphasis on the recent values, for the next set of values, we use the following formula,

[(Previous avg. gain)*13)+ current gain)]/14.

Thus, for (2025-01-31), we will calculate the average gain as [(1.72*13)+0.00]/14 = 1.6.

Similarly, we will calculate the average loss too. Based on these formulae, the table is updated for the columns “Avg Gain (5)” and “Avg Loss(6)”

Now, to make matters simple, we add a column called “RS” which is simply, (Avg Gain)/(Avg Loss). Thus, for 2025-01-31, RS = (Avg Gain)/(Avg Loss) = 1.60/2.05 = 0.78. In this manner, the table for the column “RS (7)” is updated. In the next step, we finally work out the RSI values.

RSI formula,

RSI = [100 - (100/{1+ RS})]

For example, for (2025-01-31),

RSI = [100 - (100/{1+ RS})] = [100 - (100/{1+ 0.78})] = 43.8

In this manner, the table is updated as follows:

This is how we get the value of RSI. The RSI indicator graph is always created with respect to the closing price.

For example, if we take into account the values of RSI in the above table, the graph should be as follows:

Usually, a period of 14 is taken to calculate the RSI indicator but there are different variations of it depending on the asset class or the time period of the data as well.

One of the reasons why the RSI indicator is popular is because its value is always between 0 and 100. This makes it easy to read and form opinions about the asset. The creator mentioned that a value below 30 indicates “oversold” while a value over 70 indicates “overbought”. Further, the level of 50 can be considered a mid-point.

However, it is not as easy as it looks, and if we try to enter and exit the market based on this factor alone, we would not be able to trade effectively as there are numerous occasions where this advice can fail. You can see in the graph below that the closing price continued to rise even after entering the overbought zone from December 2 to December 17, 2024.

Let us see the implementation of the RSI indicator in Python.

RSI Indicator in Python Using a Real-World Example, With Visualisation in Plotly

While it seemed complicated to calculate the RSI indicator values manually, Python has really made it simple (and faster) to calculate the RSI values of any asset, as well as visualise it. For the demonstration, we will be using Apple’s OHLCV data from the period Jan 2022 to February 14, 2025. Further, we will use the Close price data and calculate the 14-period RSI values of the asset. We will then use the python Plotly library for visualising the close price and RSI values together.

The code is given below:

That’s it. Now you can check how many times the Apple stock price crossed the overbought and oversold thresholds of 30 and 70.

We have various strategies based on the RSI indicator, let’s check them out now.

Strategies based on RSI indicator

There are mainly three ways you can create a trading strategy using the RSI indicator.

RSI as Trend Indicator

RSI as Divergence Indicator

RSI as Double Top and Double Bottom Pattern Indicator

RSI as a Trend Indicator

RSI works as a reference when you want to gauge if the market is going through a bullish or bearish trend. While the general assumption that an indicator above 70 indicates overbought and below 30 indicates oversold holds true for most of the cases, there are others who insist that it can be held true for values above 66.6 and below 33.3 as well.

If the RSI closes above 66.6 but goes below the value, it does not mean that the trend has reversed and you should short the stock immediately. Instead, we look for the graph and as long as it stays above 33.3, we can say that the market is still bullish when it comes to the asset.

You can see in the graph below that the RSI indicator crossed the overbought zone in January 2024 and since then, the price continued to rise indicating a bull run.

Similarly, if the RSI goes below 33.3 and rises up but doesn’t cross the 66.6 barriers (or 70, as is assumed), we can conclude that the market is bearish.

However, one should not take this as a sole indication to buy (or sell) the asset in question. We will go forward to the next topic to understand the whole picture.

RSI as Support and Resistance

As we have understood how to set up the RSI trend indicator, we can see that as the number of periods of gains increases when compared to the number of periods of losses, the RSI values will keep increasing. Thus, it gives a strong indication of a longer-term trend than the closing prices where the daily price fluctuations could show us a different story.

Just like the closing prices, we can use the RSI indicator values to draw a trendline of the support and resistance levels and thus, a breakout from this trend can be easily observed in the RSI values a market position taken. You can see in the following graph how both the RSI and closing price have a breakout.

The deal here is to correctly identify if the breakout is sustainable for a long period or a false signal.

RSI and divergence

RSI indicator can also be used to predict a divergence in the trend before the price trend actually reverses.

Divergence can usually be spotted when, for example, if the price line is moving higher but the RSI indicator slumps due to the fact that the relative strength of the asset weakens when compared to the previous periods’ growth.

For example, let’s say that the price has been closing higher than the previous days but the gain is not as substantial as compared to the average gain of the period. Then, the RSI will close lower than the previous day's value. In this regard, we can get a signal that the market will get a check on the price in a few days and thus trade accordingly. You can see that in the following graph where the RSI shows a downward trend while the prices keep rising. Eventually, the closing prices decrease too.

The same is true when the closing price has been bearish for a while but the RSI starts posting higher values, it means that the prices will pick up.

RSI double bottom and double top signal.

We can identify the double bottom and double top pattern using the RSI indicator. The gist of the double bottom pattern identification is as follows.

The RSI indicator closes below 30 before rising higher and above the 30 barriers.

It again heads south but closes above 30 before rising again sharply.

This is seen as a “W” formation on the chart. Traders usually use this pattern as a confirmation that the market is headed for the bullish direction. You can see in the following graph that the RSI indicator breached the 30 barrier on April 26 before rising up sharply and then closed below, but above the 30 barrier on May 1. It then rose again.

Similar to the double bottom, the pattern formation for the double top is as follows:

The RSI indicator breaches the 70 levels before dropping again below the 70 levels.

It again rises but closes below 70 and then drops sharply again.

This is seen as an “M” formation on the price chart. Traders usually use this pattern as a confirmation that the market is headed for the bearish direction. You can see in the graph given below, the RSI level breaches 70 on March 28. Later, it falls below the 70 thresholds and while it does rise higher, it does not cross the 70 threshold till August 2022.

Backtesting an RSI indicator-based trading strategy

We will backtest a simple trading strategy where we will buy when the RSI indicator falls below 30 and sell when the RSI indicator is above 70.

Let’s look at the code now:

You can see that the strategy gave a decent return by looking at the cumulative returns graph. You can also check other performance metrics like Sharpe ratio, Max. Drawdowns as well. To know how to backtest a strategy in detail, check out the blog,Backtesting: How to Backtest, Strategy, Analysis, and More.

Limitations of RSI

The fundamental property of RSI which states that a level above 70 is overbought can be proved wrong in a strong bull market where the company is progressing rapidly and posting good returns to its shareholders. In this scenario the RSI can stay above 70 for a long time, which can be disastrous for short sellers.

Nvidia’s stock price kept climbing for a month after crossing the overbought zone of 70, before declining.

It is a similar case for a bear market where the RSI can stay below 30 and not rise above that level for an extended period of time.

2. The RSI can give false signals too. There are times when a divergence is indicated but the stock continues in its trend.

Here, while the RSI indicator value dropped below 70 for a brief period, it quickly renounced and crossed 70 again.

Thus, it is always said that we should use the RSI with one or more indicators which will give us a holistic view of the market and help us extract maximum information from the price action of a particular asset.

Conclusion

Once we know how to calculate and plot the RSI indicator, it can be relatively easier to understand if an asset is overbought or oversold and make decisions accordingly. We also saw how to backtest a trading strategy based on the RSI indicator and analyse its performance. While a general level of 70 indicates overbought and 30 being oversold exists in the market, we have seen that it can be detrimental to rely on this bit of information entirely. Hence we should use multiple indicators and backtest the strategy before moving to live trading.

Continue Learning

Now that you've built a strong foundation, deepen your understanding of market behavior and trading strategies.As you read above, in the limitations that RSI (Relative Strength Index) is not an effective indication for short sellers. To understand how short sellers navigate such conditions, check out our Qauntra course onShort Selling in Trading.

To enhance your trading strategy, explore various indicators and their applications:

Five Indicators to Build Trend-Following Strategies– Learn the key indicators used in trend-following models.

Trading Index (TRIN): Formula, Calculation & Strategy in Python– Understand how TRIN helps gauge market sentiment.

How to Optimise a Trading Strategy Based on Indicators– Learn techniques to refine your indicator-based strategies.

Bollinger Bands Explained– Explore how Bollinger Bands can be used for volatility-based trading strategies.

Using Moving Average Crossover to Trade Nifty Options– Understand how moving averages can be applied to options trading.For those looking for a structured and professional approach to algorithmic trading, theExecutive Programme in Algorithmic Trading (EPAT)provides an in-depth curriculum covering Python, its basics and its quant ecosystem including key data science stack, strategy development & backtesting and hands-on Python tutorials.

File in the download:

RSI Indicator Blog Code - Python notebook

Feel free to make changes to the code as per your comfort.

Login to Download

Note: The original post has been revamped on 5thMarch 2025 for recentness, and accuracy.

Disclaimer: All investments and trading in the stock market involve risk. Any decision to place trades in the financial markets, including trading in stock or options or other financial instruments is a personal decision that should only be made after thorough research, including a personal risk and financial assessment and the engagement of professional assistance to the extent you believe necessary. The trading strategies or related information mentioned in this article is for informational purposes only.

---

*Imported from QuantInsti Blog on 2026-04-27*
