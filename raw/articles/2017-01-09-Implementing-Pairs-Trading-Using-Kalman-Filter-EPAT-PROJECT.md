---
title: "Implementing Pairs Trading Using Kalman Filter [EPAT PROJECT]"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/implementing-pairs-trading-using-kalman-filter/"
date: "2017-01-09"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Implementing Pairs Trading Using Kalman Filter [EPAT PROJECT]

**来源**: [QuantInsti](https://blog.quantinsti.com/implementing-pairs-trading-using-kalman-filter/)  
**日期**: 2017-01-09  
**作者**: QuantInsti

---

## 原文

Implementing Pairs Trading Using Kalman Filter [EPAT PROJECT]

ByDyutiman Das

This article is the final project submitted by the author as a part of his coursework inExecutive Programme in Algorithmic Trading (EPAT™)at QuantInsti. Do check our Projectspageand have a look at what our students are building.

Introduction

Some stocks move in tandem because the same market events affect their prices. However, idiosyncratic noise might make them temporarily deviate from the usual pattern and a trader could take advantage of this apparent deviation with the expectation that the stocks will eventually return to their long term relationship. Two stocks with such a relationship form a “pair”. We have talked about thestatistics behind pairs tradingin a previous article.

This article describes atrading strategybased on such stock pairs. The rest of the article is organized as follows. We will be talking about the basics of trading an individual pair, the overall strategy that chooses which pairs to trade and present some preliminary results. In the end, we will describe possible strategies for improving the results.

Pair trading

Let us consider two stocks, x and y, such that

y = \alpha + \beta x + e

\alphaand\betaare constants andeis white noise. The parameters {\alpha, \beta} could be obtained from a linear regression of prices of the two stocks with the resulting spread

e{t} = y{t} - (\alpha + \beta x_{t})

Let the standard deviation of this spread be \sigma_{t}. The z-score of this spread is

z{t} = e{t}/\sigma_{t}

Trading Strategy

The trading strategy is that when thez-score is above a threshold, say 2,the spread can be shorted, i.e. sell 1 unit of y and buy \beta units of x. we expect that the relationship between x and y will hold in the future and eventually the z-score will come down to zero and even go negative and then the position could be closed. By selling the spread when it is high and closing out the position when it is low, the strategy hopes to be statistically profitable. Conversely, if the z-score is below a lower threshold say -2, the strategy will go long the spread, i.e. buy 1 unit of y and sell \beta units of x and when the z score rises to zero or above the position can be closed realizing a profit.

There are a couple of issues which make this simple strategy difficult to implement in practice:

The constants \alpha and \beta are not constants in practice and vary over time. They are not market observables and hence have to be estimated with some estimates being more profitable than others.

The long term relationship can break down, the spread can move from one equilibrium to another such that the changing {\alpha,\beta} gives an “open short” signal and the spread keeps rising to a new equilibrium such that when the “close long” signal come the spread is above the entry value resulting in a loss.

Both of these facts are unavoidable and the strategy has to account for them.

Determining Parameters

The parameters {\alpha, \beta} can be estimated from the intercept and slope of a linear regression of the prices of y against the prices of x. Note that linear regression is not reversible, i.e. the parameters are not the inverse of regressing x against y. So the pairs (x,y) is not the same as (y,x). While most authors use ordinary least squares regression, some use total least squares since they assume that the prices have some intraday noise as well. However, the main issue with this approach is that we have to pick an arbitrary lookback window.

In this paper, we have used Kalman filter which is related to an exponential moving average. This is an adaptive filter which updates itself iteratively and produces \alpha, \beta, e and \sigma simultaneously. We use the python package pykalman which has the EM method that calibrates thecovariance matricesover the training period.

Another question that comes up is whether to regress prices or returns. The latter strategy requires holding equal dollar amount in both long and short positions, i.e. the portfolio would have to be rebalanced every day increasing transaction cost, slippage, and bid/ask spread. Hence we have chosen to use prices which is justified in the next subsection.

Stability of the Long Term Relationship

The stability of the long term relationship is determined by determining if the pairs are co-integrated. Note that even if the pairs are not co-integrated outright, they might be for the proper choice of the leverage ratio. Once the parameters have been estimated as above, the spread time series e_{t} is tested for stationarity by the augmented Dickey Fuller (ADF) test. In python, we obtain this from the adfuller function in the statsmodels module. The result gives the t-statistics for different confidence levels. We found that not many pairs were being chosen at the 1% confidence level, so we chose 10% as our threshold.

One drawback is that to perform the ADF test we have to choose a lookback period which reintroduces the parameter we avoided using the Kalman filter.

Choosing Sectors and Stocks

The trading strategy deploys an initial amount of capital. To diversify the investment five sectors will be chosen: financials, biotechnology, automotive etc. A training period will be chosen and the capital allocated to each sector is decided based on a minimum variance portfolio approach. Apart from the initial investment, each sector is traded independently and hence the discussion below is limited to a single sector, namely financials.

Within the financial sector, we choose about n = 47 names based on large market capitalization. We are looking for stocks with high liquidity, small bid/ask spread, ability to short the stocks etc.  Once the stock universe is defined we can form n (n-1) pairs, since as mentioned above (x,y) is not the same as (y,x). In our financial portfolio, we would like to maintain up to five pairs at any given time. On any day that we want to enter into a position (for example the starting date) we run a screen on all the n (n-1) pairs and select the top pair(s) according to some criteria some of which are discussed next.

Choosing Pairs

For each pair, the signal is obtained from the Kalman filter and we check if |e| > nz \sigma, where nz is the z-score threshold to be optimized. This ensures that this pair has an entry point. We perform this test first since this is inexpensive. If the pair has an entry point, then we choose a lookback period and perform the ADF test.

The main goal of this procedure is not only to determine the list of pairs which meets the standards but rank them according to some metrics which relates to the expected profitability of the pairs.

Once the ranking is done we enter into the positions corresponding to the top pairs until we have a total of five pairs in our portfolio.

Results

In the following, we calibrated the Kalman filter over Cal11 and then used the calibrated parameters to trade in Cal12. In the following, we kept only one stock-pair in the portfolio.

In the tests shown we kept the maximum allowed drawdown per trade to 9%, but allowed a maximum loss of 6% in one strategy and only 1% in the other. As we see from above the performance improves with the tightening of the maximum allowed loss per trade. The Sharpe ratio (assuming zero index) was 0.64 and 0.81 respectively while the total P&L was 9.14% and 14%.

The thresholds were chosen based on the simulation in the training period.

Future Work

Develop better screening criterion to identify the pairs with the best potentials. I already have several ideas and this will be ongoing research.

Optimize the lookback window and the buy/sell Z-score thresholds.

Gather more detailed statistics in the training period. At present, I am gathering statistics of only the top 5 (based on my selection criteria). However, in future, I should record statistics of all pairs that pass. This will indicate which trades are most profitable.

In the training period, I am measuring profitability by the total P&L of the trade, from entry till the exit signal is reached. However, I should also record max profit so that I could determine an earlier exit threshold.

Run the simulation for several years, i.e. calibrate one year and then test the next year. This will generate several year’s worths of out-of-sample tests. Another window to optimize is the length of the training period and how frequently the Kalman filter has to be recalibrated.

Expand the methodology to other sectors beyond financials.

Explore other filters instead of just Kalman filter.

Next Steps

If you are a coder or a tech professional looking to start your own automated trading desk. Learn automated trading from live Interactive lectures by daily-practitioners.Executive Programme in Algorithmic Trading (EPAT™)covers training modules like Statistics & Econometrics, Financial Computing & Technology, and Algorithmic & Quantitative Trading.Enroll now!

The work presented in the article has been developed by the author, Mr. Dyutiman Das. The underlying codes which form the basis for this article are not being shared with the readers. For readers who are interested in further readings on implementing pairs trading using Kalman Filter, please find the article below.

Link:Statistical Arbitrage Using the Kalman Filterby Jonathan Kinlay

---

*Imported from QuantInsti Blog on 2026-04-27*
