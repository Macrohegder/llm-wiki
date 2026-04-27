---
title: "Using Moving Average Crossover To Trade Nifty Options"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/moving-average-crossover-trade-nifty-options/"
date: "2018-03-07"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Using Moving Average Crossover To Trade Nifty Options

**来源**: [QuantInsti](https://blog.quantinsti.com/moving-average-crossover-trade-nifty-options/)  
**日期**: 2018-03-07  
**作者**: QuantInsti

---

## 原文

Using Moving Average Crossover To Trade Nifty Options

ByAbhishek Kulkarni

This blog is a step-by-step guide to help you learn how to use moving average crossover strategy to trade in Nifty Options. Before getting into the crossover strategy, make sure you are comfortable withoptions trading basics, particularly how call and put options work on Nifty. You will also explore an learn how you can perform the back-testing of crossover signals using Python programming to get optimum results from your trading strategy.

This blog covers:

Moving Average Crossover

How does a Moving Average Crossover strategy work?

Packages required

Step-by-step guide

Conclusion

Moving Average Crossover

Trading strategies can be broadly categorized into momentum and mean reverting strategies. Inmomentum trading strategiesthe principle is “trend is a friend” and the gist involves buying high and selling higher.

Whereas, inmean reversion strategies, the principle is “whatever goes up has to come down”. This implies buying when the asset is oversold and selling when it is overbought.Moving averagecrossover belongs to the former category.

There is a plethora of information on moving average crossover strategy with different names such as “Golden Cross” and “Death Cross”.

The strategy involves moving average indicator of different durations.

An average of the shorter look-back window is calledSMA,and

The one with the longer look-back window is calledLMA.

Popularly used SMA-LMA pairs include 20-40, 20-60 and 50-200. An SMA-LMA plot along with the adjusted close price for Nifty looks as follows:-

Trading rules are simple.

Buy the asset when the SMA crosses above LMA, and

Sell the asset when LMA crosses below SMA.

How does a Moving Average Crossover strategy work?

Crossover strategy is widely used to trade in the equity segment. In this post, we will exploreback-testingof crossover signals to trade Nifty options using Python.

Instead of buying the asset, we shall buy a call option when:

SMA(today) > LMA(today) and

SMA(yesterday) < LMA(yesterday).

Similarly sell the call option when:

SMA(today) < LMA(today) and

SMA(yesterday) > LMA(yesterday).

Packages required

Python packages are required to perform this activity.

Following are the packages required:-

Pandas-Datareader

Pandas

Datetime

Suggested reads

Before we begin, here is a list of free resources to help you get prepared:

Pandas tutorial

Popular Python Trading Platforms For Algorithmic Trading

How To Install Python Packages

Free book on Python Basics

Free course on Python for Trading

Step-by-step guide

With the following process, you would understand how you can use moving average crossover strategy to trade in Nifty Options.

It consists of a total of 7 steps:

Step 1 - Importing the packages

In the first step, we import the necessary Python packages.

Step 2 -Download Nifty OHLC data

With this step, we proceed towards downloading the Nifty OHLC data using Pandas-Datareader and the corresponding option data using NSEpy.

Step 3 - Create a new dataframe

In this step, we create a new dataframe that contains relevant information from the previous two dataframes.

Step 4 - Define two moving averages

Here, we define two moving averages, 'm' and 'n'. The dataframe 'df' contains new columns namely “SMA” and “LMA” along with the lagged version of these values.

Note: The first nan values are removed in this step.

Step 5 - Define the buying and selling logic

Now, we proceed towards defining the buying and selling logic as explained above.

We shall use “Last” as our trading price. We shall select only those values that have finite “Last” and nonzero “Number of Contracts”.

One lot of nifty option is 75, thus we will multiply the “Trade Price” column by 75.

To reiterate, we apply moving average indicators on the underlying index value and trade on “last” price of the option.

Step 6 - Computing the cumulative returns

After completing the 5th step, in this step, we proceed with computing the cumulative returns of the strategy that we have created.

Step 7 - A graph of the cumulative PnL

Show the graph of cumulative PnL.

Conclusion

The strategy might be tweaked for different look-back periods of SMA-LMA.

Instead of selling the call, a long position input might be considered when a sell signal is generated. Also note that though we are attempting to capture delta of the option, the strategy is solely based on average value of prices.

Let us know if you come up with interesting returns on the back-test.

It is always better to keep learning to grow your trading -learn trading optionssystematically, learning to create option pricing models, option greeks and various strategies, etc. With our learning trackQuantitative Approach in Options Trading, you can learn how to use quantitative techniques inOptions Tradingwithin a few hours, so do check it out.

Disclaimer: All investments and trading in the stock market involve risk. Any decisions to place trades in the financial markets, including trading in stock or options or other financial instruments is a personal decision that should only be made after thorough research, including a personal risk and financial assessment and the engagement of professional assistance to the extent you believe necessary. The trading strategies or related information mentioned in this article is for informational purposes only.

File in the download

crossover options python code

Login to Download

---

*Imported from QuantInsti Blog on 2026-04-27*
