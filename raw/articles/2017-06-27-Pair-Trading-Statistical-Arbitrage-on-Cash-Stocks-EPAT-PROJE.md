---
title: "Pair Trading – Statistical Arbitrage on Cash Stocks [EPAT PROJECT]"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/pair-trading-statistical-arbitrage-on-cash-stocks/"
date: "2017-06-27"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Pair Trading – Statistical Arbitrage on Cash Stocks [EPAT PROJECT]

**来源**: [QuantInsti](https://blog.quantinsti.com/pair-trading-statistical-arbitrage-on-cash-stocks/)  
**日期**: 2017-06-27  
**作者**: QuantInsti

---

## 原文

Pair Trading – Statistical Arbitrage On Cash Stocks [EPAT PROJECT]

This article is the final project submitted by the author as a part of his coursework in Executive Programme in Algorithmic Trading (EPAT™) at QuantInsti®. Do check ourProjects pageand have a look at what our students are building.

About the Author

Jonathan has a strong knowledge of mathematical programming and has worked as a process optimization engineer for 3 years. He started to get involved in trading as a hobby, especially in algorithmic trading due to his passion for math but eventually, it became his full-time job. Jonathan enrolled for Executive Programme in Algorithmic Trading (EPAT™) in November 2016 and found his space in the world on quantitative analysis in finance. Currently, he is taking several courses online in subjects related to Artificial Intelligence and its applications in finance and is about to start an online portal in Financial Engineering to share his experience as a Quant Trader.

Project Objective

The objective of this project is to model astatistical arbitragetrading strategy and quantitatively analyze the modeling results. Motivation relies on diversifying investment throughout five sectors, aka Technology, Financial, Services, Consumer Goods and Industrial Goods. Furthermore, some stocks, generally in the same sector, move in tandem because prices are affected by the same market events. However, the noise might make them temporarily deviate from the usual pattern and a trader can take advantage of this apparent deviation with the expectation that the stocks will eventually return to their long-term relationship.

Within each sector, stocks were selected based on high liquidity, small bid/ask spread and ability to short the stock. However, it is possible to consider other stocks for further analysis. Once the stock universe is defined, pairs can be formed. Every day as we want to enter a position, all the pairs in the universe are evaluated and the top pairs are selected per some criteria.

Trading Strategy Idea

As the universe of pairs is already defined, correlation analysis should be performed for all possible pairs to filter out pairs which have suitable properties for executing statistical arbitrage. With this correlation test, we are looking for a measurement of the relationship between two stock prices. The logic of the strategy is: for any pair that is correlated (from the universe established), if the pair ratio diverges from a certain threshold, then we short the stock that is expensive and buy the cheap stock. Once they converge to the mean, we close the position and profit from the reversal.

The strategy triggers new orders whenever the pair ratio of the prices of the stocks on the universe of filtered pairs diverges from the mean. To ensure the convenience of trading at this point, the pair must be cointegrated. If the pair ratio is cointegrated, the ratio is mean reverting and the greater the dispersion from its mean, the higher the probability of a reversal, which makes the trade more attractive. This analysis allows in determining the stability of the long-term relationship. Spread time series is tested for stationarity by theAugmented Dickey-Fuller(ADF) test. In other words, if pair stocks are cointegrated, it suggests that the mean and variance of this correlation remains constant over time. There is, however, a major issue which makes this simple strategy difficult to implement in practice: long term relationship can break down, and the spread can move from one equilibrium to another.

A training period of minimum 1-year data is chosen for out-of-sample test and the capital allocated to each sector is decided based on a minimum variance portfolio approach. Each sector is traded independently. Yahoo finance has been used for testing this strategy.  To perform the backtesting for each pair, data for the period 1-Jan-2009 to 31-Dec-2014 has been used.

Strategy Details

You can read the complete project work of the author including the Python codes for Pairs Trading by downloading the Ebook provided below.

Highlights from the project include:

Pairs Trading– Statistical Arbitrage on Cash Stocks

Strategy

Code Details and In-Sample Backtesting

Analyzing Model Output

Monte Carlo Analysis and much more...

Next Step

If you want to learn various aspects of Algorithmic trading then check out theExecutive Programme in Algorithmic Trading (EPAT™). The course covers training modules like Statistics & Econometrics, Financial Computing & Technology, and Algorithmic & Quantitative Trading. EPAT™ equips you with the required skill sets to build a promising career in algorithmic trading.Enroll now!

Alternatively, you can also sign up forQuantra’s course on Statistical Arbitrage Trading, this course covers basic concepts of Statistical Arbitrage trading and a step-by-step guide for building a pairs trading strategy using Excel and Python.

Update

We have noticed that some users are facing challenges while downloading the market data from Yahoo and Google Finance platforms. In case you are looking for an alternative source for market data, you can use Quandl for the same.

Files in the download:

EPAT-Project-by-Jonathan-Moreno-Narváez-on-Pair-Trading.pdf

Login to Download

---

*Imported from QuantInsti Blog on 2026-04-27*
