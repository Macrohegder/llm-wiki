---
title: "Algo Trading Stages Explained Simply"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/algo-trading-stages-explained-simply/"
date: "2019-09-12"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Algo Trading Stages Explained Simply

**来源**: [QuantInsti](https://blog.quantinsti.com/algo-trading-stages-explained-simply/)  
**日期**: 2019-09-12  
**作者**: QuantInsti

---

## 原文

Algorithmic Trading Stages Explained Simply

BySunil Guglani (Assistant Vice President at NCDEX)

Are you new to Algo trading? Confused about how to start, where to start?

There are lots ofcoursesand content available on backtesting, technical indicators, Python for finance on the web.

Also, there is a good amount of stuff available on the benefits ofAlgo tradingover manual trading. But if you want to develop your first algo, what are the stages you have to go through, there is limited information on this. Before working through these stages, those who are new to the field can first explore theAutomated Trading for Beginnerslearning track to build a solid conceptual foundation.

Note: These stages are purely based on my experience, it may/may not differ from standard procedures (which I could not find ☺).

I will try to explain this by taking a real trading strategy. Here are the stages I will cover:

Formulate the Trading Concept/Logic

Filtering criteria to choose the scripts

Verification of Logic (at High Level)

Backtesting

Optimization of Parameters

Paper Trading or Forward Testing or Simulation Trading in the real environment

Deployment in the real environment

These stages apply equally well to traders building their first system inalgorithmic trading in India, where retail participation is steadily increasing across equity and derivatives markets.

Formulate the Trading Concept/Logic

First thing first, algo trading is not - rocket science..yes.. it is really not…it is just a puzzle, which you need to solve more effectively, efficiently than a few other people. And we know the puzzle..Buy at low and sell at high.

Not necessary to follow any existing theory or indicators or strategy. You don’t need to be a market expert. You can make your own if you are comfortable. (my first algo was an arbitrage across the exchange. I was an amateur and I didn’t even know the meaning of arbitrage at that time. ☺)

You need to answer following in this stage:

What will be my logic to achieve my goal(Buy at Low and Sell at High)?

What will be the frequency of my trades?

Which segment will it work most effectively(Equity/Commodity/FX/Crypto..)

How much should be backtesting period?

Which automation tools/languages will be most useful for this logic?

Example:I think FMCG (Fast moving consumer goods) stocks are generally less volatile in nature and they revolve around the same price range. It makes me think that they are range bound and so they are mean reverting. Therefore I will try to apply some mean reversion technique in my strategy. Also, intraday prices are highly volatile therefore I will choose daily closing prices for calculation and trade.

Considering my above idea, my answers to the following are :

What will be my logic to achieve my goal (Buy at Low and Sell at High)?

I will be usingmean reversion trading strategy. For this, I will use Bollinger band. Buy: if Close price goes below -2 standard deviation from the mean. square off position: if Close price goes above +2 standard deviation from the mean.

What will be the frequency of my trades?

Daily.

Which segment will it work most effectively (Equity, Commodity, FX or Crypto)?

I will use the equity cash segment.

How much should be backtesting period?

3 years (longer the better).

Which automation tools/languages will be most useful for this logic?

I am comfortable with Python. We should use the tools where we are most comfortable with.

Filtering criteria to choose the scripts

Great. You have achieved a big milestone. You have penned down the core logic and did high level planning for your algo.

If you observe, your logic will work best on some specific conditions and specific scripts. Remember you have already decided the segment in first stage.

The selection/filtration of scripts can be done before or during the trading hours (real-time). It all depends on your core logic.

Example:

As we have decided, we will use FMCG scripts and high liquid stocks only, therefore filtering criteria to be used as follows: a. Industry(FMCG). b. Volume>100000

Verification of Logic (at High Level)

Algo development is an expensive process, it requires a lot of effort and time. It is better to verify your Core logic at High level using a Visualization tool or excel.

It will save a lot of time later. You can use Tableau, power BI or just excel to write the logic and verify your logics. You can also use charting tools like trading view,investing.comor something similar.

It is a 5 year graph of ITC Ltd on daily frequency. And SMA, STD(-2,+2) is applied on the 20 days lookback period. (Courtesy:tradingview.com). The visual below gives us confirmation about our logic.

Backtesting

Backtestingis the way of verification of your logic using historical price information. This stage helps in understanding how well the logic would have worked if you used this in the past. For a comprehensive and structured approach to this stage, the Quantra course onbacktesting trading strategies pythoncovers the full workflow with practical Python examples. This stage gives an indication about the performance of your logic. It also gives you the opportunity to optimise the logic and its parameters.

One should consider the following parameters in this stage:

Various performance parameters

Returns

Max drawdown

Max continuous drawdown

Max profit

Max continuous profit

Number of transactions

Average returns per transaction

Transaction charges

Slippages,etc.

Few more points to focus are:

Stop loss/Trailing stop loss

Target price

Entry Criteria

Exit criteria

A very common mistake algo traders do is using the current price information in generating the trading signals. We should always use historical data in our logic and next price information for buy and sell signals.

Activities to perform are:

We need to perform the following activities in this stage:

Import the necessary libraries

Fetch the historical OHLC data for an instrument.

Write the supporting functions to achieve our logic

Generate the buy/sell signals usingcandlestick patterns

Visualize the output

Checking returns of the strategy

Analysis and visualisation of backtesting output data to understand the scope of optimisation in your algorithm.

Note: To review steps used in backtesting please refer to my article

https://medium.com/@sunil.guglani/how-to-develop-your-first-trading-bot-using-python-by-recognising-candlestick-patterns-a755f7fa6674

Example:

Output is as follows:

Candlestick chart

**************BACKTEST RESULTS OF : ITC ************************

Sum of returns in % 12.582204198954024Average returns per transaction in % 1.7974577427077176Absolute returns 39.50000000000003Absolute returns per trx 5.642857142857147Max drawdown for a trx -36.30000000000001Max returns for a trx 34.200000000000045Losing trx 1Winning trx 6Win/Lose ratio 6.0

Optimization of Parameters

We should keep optimizing our algo parameters on a regular basis. By using historical data and using various methods like ML/backtesting performance.

Things to consider are :

Avoid overfitting of parameters. Overfitting that you optimize the logic and parameters to the extent that the program will work best in some specific situations and scenarios. But it may go bad if the scenario changes.

Paper Trading or Forward Testing or Simulation Trading in the real environment

Paper trading is the way of verification of your logic in the real environment. One doesn’t need to invest actual money in this stage. And It gives very accurate and precise results. One can expect same/similar results in the real environment. But it is time-consuming activity. One can do this by using the feature provided by his/her broker, or you can also develop your framework to test the same.

Deployment in the real environment

Deployment in the real environment requires multiple facets to be managed, which are generally not being considered in backtesting

Functionally following aspects are required to be managed:

Order management

Risk Management

Money/Fund Management

Diversification of assets

Portfolio management

User Management

Slippages

Technically following aspects are required to be managed:

Establish Connection with the broker API.

Passing the buy/sell orders using the broker connection,

Establish Connection with the data API (if data vendor is different from broker)

Accessing the real time and historical data using data API connection.

This concludes the article. If I missed out on anything, feel free to share your thoughts. I will try to incorporate it.

Conclusion:

To summarize the followingalgo trading strategies, Algo can be considered as a software product and all the stages can be easily mapped with “SoftwareProductDevelopment Life Cycle”

All the stages have their own importance and are critical to the success of the algo.

Formulate the trading logic/idea

Filtering criteria to choose the scripts

Verification of Logic( Visualization)

Backtesting

Optimization of Parameters

Paper Trading or Forward Testing or Simulation Trading

Deployment in the real environment

File in the download:

Algorithmic Trading Stages-Python Notebook

Login to Download

Disclaimer: All investments and trading in the stock market involve risk. Any decisions to place trades in the financial markets, including trading in stock or options or other financial instruments is a personal decision that should only be made after thorough research, including a personal risk and financial assessment and the engagement of professional assistance to the extent you believe necessary. The trading strategies or related information mentioned in this article is for informational purposes only.

---

*Imported from QuantInsti Blog on 2026-04-27*
