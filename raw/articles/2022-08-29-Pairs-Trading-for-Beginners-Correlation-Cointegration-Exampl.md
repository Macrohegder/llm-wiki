---
title: "Pairs Trading for Beginners: Correlation, Cointegration, Examples, and Strategy Steps"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/pairs-trading-basics/"
date: "2022-08-29"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Pairs Trading for Beginners: Correlation, Cointegration, Examples, and Strategy Steps

**来源**: [QuantInsti](https://blog.quantinsti.com/pairs-trading-basics/)  
**日期**: 2022-08-29  
**作者**: QuantInsti

---

## 原文

Pairs Trading for Beginners: Correlation, Cointegration, Examples, and Strategy Steps

ByChainika Thakar

A pairs trading strategy is one of the most popular strategies when it comes to finding trading opportunities between the two stocks that are co-integrated.

How do the stocks co-integrate? How to take advantage of their co-integration with a pairs trading strategy? This blog discusses it all as it covers:

What is pairs trading?

History of pairs trading

What is the logic behind pairs trading?

Essential terms used in pairs tradingCorrelationCointegrationZ-score

Correlation

Cointegration

Z-score

Augmented Dickey Fuller Test

Steps for pairs tradingSelect stocks for pairs tradingEntry pointsDefining exit points

Select stocks for pairs trading

Entry points

Defining exit points

Pairs trading strategy

Advantages of pairs trading

Disadvantages of pairs trading

What is pairs trading?

In a pairs trading strategy, usually, a pair of stocks is traded in a market-neutral strategy, i.e. it doesn’t matter whether the market is trending upwards or downwards, the two open positions for each stock hedge against each other. The key challenges in pairs trading are to:

Select a pair which will give you goodstatistical arbitrageopportunities over time

Select the entry/exit points

Moreover, you can check out this informative video below to find out how pairs trading works.

History of pairs trading

Pairs trading was first introduced in the mid-1980s by a group of technical analyst researchers that were employed by Morgan Stanley. The pairs trading strategy uses statistical and technical analysis to seek out potential market-neutral profits. It remains one of the most structured approaches withinquantitative trading, combining statistical rigour with disciplined execution.

Use ADF Test to find pairs to trade

10 min read

What is the logic behind pairs trading?

In the case of a pairs trading strategy, the two stocks or the financial instruments need to be trending at a similar mean price and remain close to each other. But, on certain occasions, one of the instruments may go through a short period of deviation from another in terms of price.

In this short period, the trader can take the opportunity to go long on one of the financial instruments while shorting the other. The positions are based on the current market price of both the stocks and theirstandard deviation.

Essential terms used in pairs trading

Some of the essential terms that are used in pairs trading strategy are-

Correlation

Correlation is quantified by the correlation coefficient ρ, which ranges from -1 to +1. The correlation coefficient indicates the degree of correlation between the two variables.

The value of +1 means there exists a perfect positive correlation between the two variables, -1 means there is a perfect negative correlation and 0 means there is no correlation.

A perfect positive correlation is when one variable moves in either an upward or downward direction and the other variable also moves in the same direction with the same magnitude.

Whereas a perfect negative correlation is when one variable moves in the upward direction and the other variable moves in the downward (i.e. opposite) direction with the same magnitude.

The correlation coefficient for the two variables is given by:

Correlation(X,Y) = ρ = COV(X,Y) / SD(X).SD(Y)

where,cov (X, Y) = the covariance between X & YSD (X) and SD(Y) = the standard deviation of the respective variables

If the correlation is high, say 0.8, traders may choose that pair for pairs trading. This high number represents a strong relationship between the two stocks. So if A goes up, the chances of B going up are also quite high.

Based on this assumption a market neutral strategy is played where A is bought and B is sold; bought and sold decisions are made based on their individual patterns.

Just looking atcorrelationmight give you spurious results. For instance, if your pairs trading strategy is based on the spread between the prices of the two stocks, it is possible that the prices of the two stocks keep on increasing without evermean-reverting.

Statistical Arbitrage: from A to Z

8 min read

Spread = log(a) – nlog(b)

where ‘a’ and ‘b’ = prices of stocks A and B respectively

For each stock of A bought, you have sold n number of stocks of B.

Now, both ‘a’ and ‘b’ increase in such a way that the value of the spread decreases. This will result in a loss since stock A is increasing at a rate lower than stock B and you are short on stock B.

Thus, one should be careful of using only correlation for determining the pairs of the stocks while performing the pairs trading strategy.

Cointegration

​​The most common test for Pairs Trading is the cointegration test. Cointegration is a statistical property of two or more time-series variables which indicates if a linear combination of the variables is stationary.

Let us understand the statement above. The two time series variables, in this case, are the log of prices of stocks A and B. Linear combination of these variables can be a linear equation defining the spread:

As you know,

Spread = log(a) – nlog(b)

where ‘a’ and ‘b’ are prices of stocks A and B respectively.

For each stock of A bought, you have sold n stocks of B.

If A and B are cointegrated, the equation above is stationary. A stationary process has very valuable features which are required to model pairs trading strategies.

For instance, in this case, if the equation above is stationary, that suggests that the mean and variance of this equation remain constant over time.

So if we start with ‘n’, which is called the hedge ratio, so that spread = 0, the property of stationary implies that the expected value of spread will remain as 0. Any deviation from this expected value is a case for statistical abnormality, hence a case for pairs trading!

Z-score

Given a normal distribution of raw data points, the z-score is calculated so that the new distribution is a normal distribution with a mean of 0 and a standard deviation of 1. Having such a distribution ~ N(0, 1) is very useful for creating threshold levels.

For instance, in pairs trading, we have a distribution of spread between the prices of stocks A and B. We can convert these raw scores of spread into z-scores as explained below.

This new distribution will have a mean of 0 and a standard deviation of 1. It is easy to create threshold levels for this distribution such as 1.5 sigma, 2 sigma, 2.5 sigma, and so on.

The formula for z-score is as follows:

z = (x – mean) / standard deviation

where,x = a raw data pointz = the z-score

Mean and standard deviation can be rolling statistics for a period of ‘t’ days or minutes or time intervals.

A must-watch video, that discusses Mean Reversion and Z-score, mean reversion principles which suggests that prices tend to move around the historical mean over time and z-scores can be used to identify the deviation from the mean and generate the appropriate trading signals.

Use ADF Test to find pairs to trade

10 min read

Augmented Dickey Fuller Test

The augmented Dickey-Fuller test is an extension of the standardDickey-Fuller test, which also checks for both stationarity and non-stationarity in the time series.

The main difference from the Dickey Fuller Test is that the Augmented Dickey Fuller test can also be applied to a large sized set of time series models. The large sized time series models can be more complicated and hence, the DF test was modified into the ADF Test. Also, the ADF Test works on the data with missing values.

Steps for pairs trading

Select stocks for pairs trading

For the pair of stocks to be traded in a pairs trading strategy, it is required that the time series is stationary. A stationary time series makes effective and precise predictions.

Also, a stationary time series means that the pair of stocks is co-integrated and can be traded together by generating trading signals. Hence, stocks are needed to be selected for performing the pairs trading.

UnderstandingStationary Time Seriesis key to selecting the right stocks for pairs trading. When time series are stationary, they allow for accurate predictions and ensure the stocks are co-integrated, making them ideal for generating reliable trading signals. Explore further to discover how this concept can enhance your pairs trading strategy.

For any pair of stocks, define the spread as below:

Spread = log(a) – nlog(b)

where ‘a’ and ‘b’ are prices of stocks A and B respectively.

Assumption: n, the hedge ratio is constant.

Calculate ‘n’ using regression so that spread is as close to 0 as possible. Hence, we regress the stock prices to calculate the hedge ratio.

Theory: In regression, we get a term called the residuals which represents the distance of observed value from the curve fitting line or estimated value. These residuals tell us how much the actual value of ‘spread’ deviates from 0 for the calculated ‘n’.

These residuals are studied so that we understand whether or not they form a trend. If they do not form a trend, that means the spread moves around 0 randomly and is stationary.

Run the Dicky Fuller test on the spread values inserting the value of ‘n’.

The Dickey Fuller test is a hypothesis test which gives a p-value as the result. If this value is less than 0.05 or 0.01, we can say with 95% or 99% confidence that the signal is stationary and we can choose this pair.

So far, we have discussed the challenges and statistics involved in selecting a pair of stocks for statistical arbitrage. By using the cointegration tests, we can say within a certain level of a confidence interval that the spread between the two stocks is a stationary signal. In other words, this signal is mean-reverting. The spread is defined as:

Spread = log(a) – nlog(b), where ‘a’ and ‘b’ are prices of stocks A and B respectively. For each stock of A bought, you have sold n stocks of B. n is calculated by regressing prices of stocks A and B.

Having already established that the equation above is mean reverting, we now need to identify the extreme points or threshold levels that when crossed by this signal, trigger trading orders for pairs trading.

To be able to identify these threshold levels, a statistical construct called z-score is widely used in pairs trading.

Statistical Arbitrage: from A to Z

8 min read

Entry points

Let us denote the Spread as ‘s’. Thus,

Spread = s = log(a) – nlog(b)

Calculate z-score of ‘s’, using rolling mean and standard deviation for a time period of ‘t’ intervals. Save this as ‘z’.

Define threshold as anything between 1.5-sigma and 2-sigma. This parameter will change as per thebacktesting resultswithout risking overfitting data.

When z-score crosses an upper threshold, go SHORT:Sell stock ABuy stock B

When the z-score crosses the lower threshold, go LONG:Buy stock ASell stock B

Maintain the hedge ratio to calculate the stock quantity.

We have now understood entry points in pairs trading. Now we will move on to the other end, exit points.

Defining Exit points

Stop loss

Stop loss is defined for scenarios when the expected outcome does not occur. For instance, if we chose entry signals at 2-sigma, we are expecting that the spread will revert back to the mean from this threshold. However, it is possible that the spread continues to blow up.

Say it reaches 2.5-sigma and you incurred losses. To prevent further losses, you place stop loss at say 3-sigma.

In addition to placing a predefined stop-loss criterion such as 3-sigma or extreme variation from the mean, you can check on the cointegration value. If the cointegration is broken while the pair is ON, the strategy warrants cutting the positions since the basic hypothesis is nullified.

Take profit

It is defined as scenarios where you take profit before the prices move in the other direction. For instance, say you are LONG on the spread, that is, you have bought stock A and sold stock B as per the definition of spread in the article.

The expectation is that spread will revert back to the mean or 0. In a profitable situation, the mean would be approaching zero or very close to it. You can keep the take profit scenario as when the mean crosses zero for the first time after reverting from the threshold levels.

Use ADF Test to find pairs to trade

10 min read

There can be many ways of defining take profits depending on your risk appetite and backtesting results.

What often works is your experience and a broad range of potent skill sets that allow you to grasp a hold of the complete scenario before jumping to conclusions. As we mentioned, your appetite for risk andbacktestingresults will work for you. Automation and practical applications are the keys here.

Let us take a recap of what we have understood so far. Pairs Trading is a trading strategy that matches a long position in one stock/asset with an offsetting position in another stock/asset that is statistically related. Pairs Trading can be called amean reversion strategywhere we bet that the prices will revert to their historical trends.

Pairs trading strategy

The first and foremost step of creating a pairs trading strategy is the co-integration of the pair. Once the pair of stocks is co-integrated, they can be considered for the pairs trading strategy. For finding out the co-integration,Augmented-Dickey Fuller Testis used.

In order to do the pairs trading,you must devise a trading strategy. Before implementing the strategy in the live market, you must observe all the parameters of the strategy such as maximum drawdown, the average positive trades, negative trades, the profit and loss, etc.

Advantages of pairs trading

The advantages of pairs trading are as under:

Mitigate Potential Losses and Risks

When the pairs trading strategy performs as per the trader’s expectations, the potential losses are mitigated. It also helps in the mitigation of risks as the pairs strategy involves dealing with two securities so if one is underperforming then there are chances that the other absorbs the losses.

Good returns

Pairs trading strategy helps the trader to get good returns regardless of the conditions of the market. Hence, in the pair trading strategy, the traders earn good returns since the trader takes the opportunity when one of the stocks’ price deviates from the mean.

Hedging

The best advantage of pairs trading is that the trader is completely hedged. Hedging is done in this strategy as the trader sells the overvalued security and purchases the undervalued security, thereby, limiting the chances of loss.

Use ADF Test to find pairs to trade

10 min read

Disadvantages of pairs trading

The disadvantages of pairs trading are:

Reliance of the High Statistical Correlation

Pairs trading relies on the securities having a high statistical correlation. Most of the traders require a correlation of at least 0.80 which is very challenging to recognize.

High Commission

Some traders highly discourage pairs trading because of its higher commission charges. Sometimes even a single Pair trade requires a Pair trader to pay a commission which is nearly double the amount of the commission required in the standard trade.

Price Filling

The generation of profits in pairs trading involves relying on margins that are too less. The transactions are made in large quantities which shows the risk of filling the stock orders at the desired price when positions are open in a pair trading is high. Even a small difference in the purchase price or sale price of the security can prove significant as the volume of transactions is high.

Now that you have a better understanding of Pairs Trading. You can also learn more about Mean Reversion Trading Strategies to use market data and statistical concepts, here is a brief video. A must-do for all quant traders.

Conclusion

Pairs trading is a trading strategy that is based on the assumption that the highly correlated securities will come back to their neutral position after any divergence. This strategy can be incorporated into any kind of trading and in any market such as stocks, forex etc. It is extremely important that the evaluation of the correlation must be made carefully as any wrong assumption or prediction may result in the failure of the pairs trading strategy.

If you are a beginner and wish to explore more about pairs trading strategy, then you must get started with this learning track onmean reversion strategieswhich is apt for pairs trading as a beginner. It offers you several courses and helps develop proficiency in it.

Note: The original post has been revamped on 29th August 2022 for accuracy, and recentness.

Disclaimer: All investments and trading in the stock market involve risk. Any decision to place trades in the financial markets, including trading in stock or options or other financial instruments is a personal decision that should only be made after thorough research, including a personal risk and financial assessment and the engagement of professional assistance to the extent you believe necessary. The trading strategies or related information mentioned in this article is for informational purposes only.

---

*Imported from QuantInsti Blog on 2026-04-27*
