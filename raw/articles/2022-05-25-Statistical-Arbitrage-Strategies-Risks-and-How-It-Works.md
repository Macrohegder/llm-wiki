---
title: "Statistical Arbitrage: Strategies, Risks, and How It Works"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/statistical-arbitrage/"
date: "2022-05-25"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Statistical Arbitrage: Strategies, Risks, and How It Works

**来源**: [QuantInsti](https://blog.quantinsti.com/statistical-arbitrage/)  
**日期**: 2022-05-25  
**作者**: QuantInsti

---

## 原文

Arbitrage Strategies: Understanding Working of Statistical Arbitrage

ByChainika Thakar

Statistical arbitrage originated around the 1980s, led by Morgan Stanley and other banks. The statistical arbitrage strategy, also known as StatArb, witnessed wide application in financial markets. The popularity of the strategy continued for more than two decades and different models were created around it to capture big profits.

To define it in simple terms, Statistical arbitrage comprises a set of quantitatively drivenalgorithmic trading strategies. These strategies look to exploit the relative price movements across thousands of financial instruments by analyzing the price patterns and the price differences between financial instruments.

A point to note here is that Statistical arbitrage is not a high-frequency trading (HFT) strategy. It can be categorised as a medium-frequency strategy where the trading period occurs over the course of a few hours to a few days.

Let us find out more about statistical arbitrage as this blog covers:

What is arbitrage?

What is statistical arbitrage?

How does statistical arbitrage work?

Types of statistical arbitrage

Risk of using statistical arbitrage strategies

Statistical arbitrage and pairs trading

How to use statistical arbitrage in pairs trading?

What is arbitrage?

Arbitrage is the process of simultaneously transacting multiple financial securities to make a profit from the difference in prices.

This can be done in various ways such as:

the purchase and sale of the same securities in different markets (Spatial Arbitrage)

simultaneous buying and selling ofspot pricesandfutures contractofsecurity

buying the stock of a company being acquired while selling the stock of the acquiring company (Merger Arbitrage).

Pairs Trading: Learn and apply

10 min read

Arbitrage can be applied to financial instruments such as

stocks,

bonds,

derivatives,

commodities etc.

Arbitrage is a risk-free strategy, although this is not always the case. There is always a possibility ofexecution risk, i.e. risk due to high volatility in the market and a sudden change in price makes it impossible to close the trade at a profitable price. Other risks involved are counterparty risk andliquidityrisk.

Let us take a look at the example now. Suppose a company ABC’s stock trades at $10 per share on the London Stock Exchange and the same stock trades at $10.5 on the New York Stock Exchange, an arbitrage strategy would be to purchase the stock at $10 on the London Stock Exchange (LSE) and sell it for $10.5 on the New York Stock Exchange (NYSE), making a profit of $0.5 per share.

What is statistical arbitrage?

In the world of finance, statistical arbitrage (or stat arb) refers to a group of trading strategies that utilise mean reversion analyses to invest in diverse portfolios of up to thousands of securities for a very short period of time, often only a few seconds but up to multiple days.

Statistical Arbitrage or Stat Arb is atrading strategybased on the statistical mispricing of one or more assets compared to the expected future value of the assets.

Also, one of the StatArb strategies is to code the algorithms to monitor financial instruments or assets that are historically known to be statistically correlated or cointegrated, and any deviations in the relationship indicate trading opportunities.

Statistical arbitrage involves statistics, quantitative methods and a computational approach for data mining which can be traded algorithmically at high frequency.

Hence, statistical arbitrage includes different types of strategies such aspairs trading,index arbitrage, basket trading ordelta-neutral strategies. These strategies vary depending on the number, types, and weights of instruments in a portfolio and its risk-taking capacity.

One of the most popular examples of Stat Arb in pairs trading is Pepsi vs Coca-Cola stocks. Both stocks belong to the same sector, or type of business, and move in tandem as the same market events affect their prices.

For instance, if Pepsi stock rises considerably compared to that of Coca-Cola, then one might short the Pepsi stock and long the Coca-Cola stock in anticipation of favourable returns.

To understand more about statistical arbitrage and ways to implement its strategies, here is an introductory video that explains it all!

Use ADF Test to find pairs to trade

10 min read

How does statistical arbitrage work?

Stat arb works when the securities such as stocks tend to trade in upward and downward cycles and a quantitative method seeks to capitalise on those trends.

The trending behaviour ofquantitative tradinguses software programs to track patterns or trends. Trends uncovered are based on the volume, frequency and the price of a security at which it is traded.

In the image below, you can see the statistical arbitrage between two stocks i.e.: LAD (Lithia Motors Inc.) and TTM (Tata Motors Limited ADR) from automobile industry.

In the image above, the stock prices of LAD and TTM are represented. You can see both the stocks stay quite close to each other during the entire time span, with only a few instances of separation.

It is in those separation periods that an arbitrage opportunity arises based on the assumption that the stock prices will move closer again.

The crux of identifying such opportunities lies in two main factors:

Identifying the pairs which require advancedtime series analysisand statistical tests

Specifying the entry-exit points for the strategy to leverage the market position

There are plenty of in-builtpairs tradingindicators on popular platforms to identify and trade in pairs. However, many a time, transaction cost which is a crucial factor in earning profits from a strategy, is usually not taken into account in calculating the projected returns.

Therefore, it is recommended that traders make their own statistical arbitrage strategies taking into account all the factors at the time of backtesting which will affect the final profitability of the trade.

Types of statistical arbitrage

The different Statistical arbitrage strategies include:

Market Neutral Arbitrage

Cross Asset Arbitrage

Cross Market Arbitrage

ETF Arbitrage

Pairs Trading: Learn and apply

10 min read

Market Neutral Arbitrage

Market neutral implies taking advantage of increasing and decreasing prices in one or more markets while attempting to avoid specific market risks. And, market neutral arbitrage implies using strategies such ashedgingwhich help to take advantage of price discrepancies in stocks based on historical data.

Cross Market Arbitrage

It seeks to exploit the price discrepancy of the same asset across markets. The strategy buys the asset in the lower-valuing market and sells it in the more highly valuing market.

Cross Asset Arbitrage

This model bets on the price discrepancy between a financial asset and its underlying. For example, between a stock index future and the stocks that form the index.

ETF arbitrage

ETF arbitrage can be termed as a form of cross-asset arbitrage which identifies discrepancies between the value of an ETF and its underlying assets.

Risk of using statistical arbitrage strategies

Statistical arbitrage is not completely risk-free since it depends on finding the opportunities from the gap left because of:

Mean Reversion

Deviation of price from the mean before the market price reverts to the mean eventually. The practice of reverting to the mean is commonly known as mean reversion. LearnMean Reversion Strategiesin detail in the Quantra course.

Inefficiencies

Gaps in prices are caused during high-frequency trading so as to exploit any inefficiencies that last for milliseconds or so. This way, a lot of inefficiencies can be captured during the trading process as an overvalued stock can be sold short and an undervalued stock can be bought long.

Price differences

The difference in prices of paired stocks in the case of pairs trading strategy is also one of the most commonly used for statistical arbitrage since the inefficiencies arise when the prices of paired stocks vary from each other.

But, the problem occurs when there are external interventions such as the devaluation of currency etc. Also, when the assumptions of arbitrage strategies are interfered with, for example, if the relationship between the paired stocks changes, the strategy fails.

Statistical arbitrage and pairs trading

StatArb is an evolved version ofpair trading strategies, in which stocks are put into pairs by fundamental or market-based similarities.

When one stock in a pair outperforms the other, the poorer performing stock is bought along with the expectation that it climbs its outperforming partner. The long position is hedged from market changes/movements by shorting the other outperforming stock.

Use ADF Test to find pairs to trade

10 min read

In the statistical arbitrage strategy, the large number of stocks are involved. Also, there is a high portfolio turnover and a high number of trades. This increases the transaction and slippage costs.

Hence, the strategy is often implemented in an automated fashion and great attention is placed on reducing trading costs. Statistical arbitrage strategy has become a major force at both hedge funds and investment banks.

In the image above, you can see the implementation steps of a statistical arbitrage strategy.

StatArb considers not pairs of stocks but a portfolio of a hundred or more stocks—some long, some short—that are carefully matched by sector and region to eliminate exposure tobetaand other risk factors.

How to use statistical arbitrage in pairs trading?

For making statistical arbitrage work in a pairs trading strategy:

First, you have tochoose the stocks for pairing.

After you have chosen the stocks, secondly you will find out the closing prices of both stocks and visualise them.

Now, you will calculate and visualise the pair’s spread and the z-score of the spread

Then, you will check forstationarityof the spread by running the Augmented Dickey-Fuller.

Lastly, thetrading signals can be generatedif the pair is stationary according to the ADF test. After a while, the paired stocks always revert to their mean.

Use ADF Test to find pairs to trade

10 min read

Statistical arbitrage in pairs trading using Python

The first step is to choose the stocks for pairing. We have taken the two stocks Blink Charging Co (ticker symbol: BLNK) and NIO (ticker symbol: NIO).

Let us first fetch the closing prices for both stocks.

Output:

Let us now visualise the data.

Output:

Both the stocks in the image above are seen staying close to each other with regard to closing prices. The periods where there are separations are those timeframes in which the arbitrage opportunities arise with the assumption that the stock prices will converge eventually.

Now, we will calculate the spread with z-score.

Output:

Hedge Ratio =  0.7948421444904515

Output:

Pairs Trading: Learn and apply

10 min read

Output:

t-stat value =  -3.3175906010162217
{'1%': -3.4381962830171444, '5%': -2.8650034233058093, '10%': -2.568614210583549}

Since the t-stat value is below the critical value at 5%, the spread is considered stationary or cointegrated.

This is an excellent example of implementing amean reversion strategy in Python, where the spread between two cointegrated assets helps generate signals (entry and exit points) for trading.

Projects on Statistical Arbitrage by EPAT Alumni

Statistical Arbitrage strategies can be applied to different financial instruments and markets. The Executive Programme in Algorithmic Trading (EPAT) includes a session on “Statistical Arbitrage and Pairs Trading” as part of the “Strategies” module.

Many EPAT participants have successfully built pairs trading strategies during their coursework. Listed below are some of their projects for your reference.

Pairs Trading on ETF – EPAT Project Work

Pair Trading – Statistical Arbitrage On Cash Stocks

Pair Trading Strategy and Backtesting using Quantstrat

Statistical Arbitrage: Pair Trading In The Mexican Stock Market

Implementing Pairs Trading/Statistical Arbitrage Strategy In FX Markets: EPAT Project Work

Conclusion

Statistical arbitrage is a useful strategy that takes advantage of the inefficiencies in the market that can arise in a number of ways such as in case of pairs trading, in case of a stock price deviating from the mean etc.

Taking out significant opportunities from such deviations is what statistical arbitrage is all about. We discussed how one can identify such an opportunity and the example of taking advantage of the arbitrage gap in case of pairs trading.

If you also wish to use statistical arbitrage in your trading journey, you must explore our course onStatistical Arbitrage Tradingwhich explains the concepts in detail along with helping you to identify trading opportunities. Also, this course includes learning to create trading models using spreadsheets and Python, and provides the essential steps onhow to backtest a trading strategyfor a great trading experience!

Note: The original post has been revamped on 25th May 2022 for accuracy, and recentness.

Disclaimer: All investments and trading in the stock market involve risk. Any decision to place trades in the financial markets, including trading in stock or options or other financial instruments is a personal decision that should only be made after thorough research, including a personal risk and financial assessment and the engagement of professional assistance to the extent you believe necessary. The trading strategies or related information mentioned in this article is for informational purposes only.

---

*Imported from QuantInsti Blog on 2026-04-27*
