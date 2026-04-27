---
title: "Automated Trading On Oanda Platform By Dr. Yves Hilpisch"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/automated-trading-oanda-yves-hilpisch/"
date: "2016-06-20"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Automated Trading On Oanda Platform By Dr. Yves Hilpisch

**来源**: [QuantInsti](https://blog.quantinsti.com/automated-trading-oanda-yves-hilpisch/)  
**日期**: 2016-06-20  
**作者**: QuantInsti

---

## 原文

Automated Trading On Oanda Platform By Dr. Yves Hilpisch

ByDr Yves Hilpisch

Python has emerged as one of the most popular languages to code in Algorithmic Trading, owing to its ease of installation, free usage, easy structure, and availability of a variety of modules. Globally, Algo Traders and researchers in Quant are extensively using Python for prototyping, backtesting, building their proprietary risk and order management system as well as in optimisation of testing modules.

This blog post highlights some of the key steps involved in Algorithmic Trading using Python as the programming language. The screenshots are taken from thewebinar of Dr. Yves Hilpisch, in collaboration with QuantInsti. Dr. Hilpisch is a world-renowned authority in the world of Python and is the founder of Python Quants GmbH, with several books on the subject under his belt. He also serves as a faculty at QuantInsti, one of Asia’s pioneer education training firm in Algorithmic Trading.

All examples shown are based on the platform and API ofOanda. Background information about Python and the libraries used can be found in the O’Reilly book Hilpisch, Yves (2014): “Python for Finance – Analyze Big Financial Data”. The post is divided into two parts. The current post highlights the basics of connecting with the Oanda platform using python and backtesting the trading strategies. The next post will cover working with streaming data as well asauto tradingin real-time.

Topics

Connecting to Oanda platform

Data Retrieval

Coding and backtesting a trading strategy

Connecting to Oanda platform

Without data, there is no backtesting, as well as no sensible trading strategies. For people experienced in python, the first step is to import the libraries like numpy and pandas. However, since the platform being used in Oanda, we will also import some special ones like oandapy.

Naturally, Oanda credentials need to be imported. If the file is stored on the disk, a simple python programme to import the credentials looks like the following. It will punch in your account id and token. Once the credentials are in place, connect to oanda with an API object.

Since Oanda has the facility of free and fully functional practice accounts, there are versatile and quite popular.

There are a variety of instruments that can be retrieved using the API object created in Oanda like all that are traded on the platform, eg. SPX 500, S&P 500 as well as commodities and currency pairs.

Data Retrieval

Retrieving the data can be done through

Defining the start and end dates (range) and

Fixing the granularity (time gap).

Selecting the instrument  for which the historical data needs to be obtained.

In the following example, the start date is taken to be 3rdFeb and the end date is assigned as 4thFeb 2016. The granularity is set at “D” meaning the whole day’s data. The instrument DE30_EUR represents German DAX exchange.

Running this code throws up a json object like this

However, for backtesting, we need to play with more such data. Therefore the granularity is changed to one minute, which gives us more clarity. ADatetimeIndex objectneeds to be created.

To store this data, we open an HDFStore, which offers easy, convenient storage of data.

Generally, the data is saved on the disk for easy retrieval. The important thing to note is that the data is retrieved chunk wise, and therefore has to be appended to the data frame object. Note that the granuality is set to M1, which means every minute. There is also the facility to set the Timezone of the data. The code is executed in 1.89 sec as indicated in the last line of the screen capture.

The highlighted portion is an important step to write the data we retrieved from the Oanda API to database object and HDFStore and save it on the disk. This is a binary storage format.

Coding and Backtesting trading strategy

Perhaps the best way to test a strategy is to have a look at its returns. In the following code, we calculate the log return of a strategy for later performance judgement.

A new column of “returns” has been added to the existing data frame object from Oanda API, and using the closeAsk values, log returns are being calculated over the whole period that has been covered in the data set. This is done in a completely vectorised fashion using numpy function.

The strategy used for this backtesting has been quite popular over the years and is also part of research papers, which generate a signal based on two different trends: a shorter simple rolling mean over 5 observations (read minutes) while the other longer trend, over 15 observations. The idea behind the strategy is simple: If the shorter trend crosses the longer trend from below, the market has an upward trend, and if it’s the other way around, the market is on a downhill and a longer trend.

While visualising the data, we come across the following pattern.

The blue line is our basic data gathered from the market above, the green curve is the short term trend and the red curve represents a longer trend. Since this visualisation does not give a complete picture of the trends because of overlaps, we focus on sample 100 observational points.

Here we can see clearly that the spot price (blue curve) shows an upward trend when the shorter trend breaches the longer trend from below, while a downward trend is visible when the green curve crosses the red curve from above.

Once our strategy is mimicking the market, we can generate signals to be issued to the market when certain conditions are met.

In this particular case, we are going for a long-only strategy.

With the code above, we generate a signal saying that when the vectorised t5>t15 stored in dataframe object is met, then we go long and not otherwise.

In the next step, we make use of the ‘returns’ calculated above to evaluate the performance of our trading strategy.

The green curve represents our trading strategy while the blue curve is indicative of the returns from the market. From the graph, it is clear that we are losing money in the extreme left ( a downward trend) and also in the extreme right.

The "number of trades" is calculated to understand the cost of implementing in case we are using do actual trading.

For a rather short period of time, there are 182 trades happening in this strategy. So, although the trading is not high-frequency, it is very active at the same time.

Another statistic of interest might be standard deviation (SD) of returns, which gives us an idea regarding the volatility for minute-bar returns. We see here that SD of the market trading strategy is quite a bit higher than the strategy devised given our trend based investments. This is also true because we have not invested for longer periods of time.

With this, we can see that our strategies are performing well for the random time interval chosen from last year's data. Therefore, our next step would be to work with streaming data and automating in real-time. These topics will be a part of our next blog post.

Next Steps

If you want to ideate and implement Quant Strategies in Python, thisblog postwill help you get there. Do you think python is preferred over other languages in Automated Trading? SeeWhy.

If you are a coder or a tech professional looking to start your own automated trading desk. Learn automated trading from live Interactive lectures by daily-practitioners.Executive Programme in Algorithmic Tradingcovers training modules like Statistics & Econometrics, Financial Computing & Technology, and Algorithmic & Quantitative Trading.Enroll now!

---

*Imported from QuantInsti Blog on 2026-04-27*
