---
title: "Pairs Trading On ETF [EPAT PROJECT]"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/pairs-trading-with-etf/"
date: "2016-12-09"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Pairs Trading On ETF [EPAT PROJECT]

**来源**: [QuantInsti](https://blog.quantinsti.com/pairs-trading-with-etf/)  
**日期**: 2016-12-09  
**作者**: QuantInsti

---

## 原文

Pairs Trading On ETF [EPAT PROJECT]

This article is the final project submitted by the author as part of his coursework inExecutive Programme in Algorithmic Trading (EPAT™)at QuantInsti. You can check out our Projectspageand have a look at what our students are building after reading this article.

About the Author

Edmund Hodid his Bachelors in commerce from University of British Columbia, He completed his Masters in Investment Management from Hong Kong University of Science and Technology. Edmund was enrolled in the 27th Batch ofEPAT™, and this report is part of his final project work.

Project Summary

ETFs are very popular for pairs trading simply because it eliminates the firm-specific factors.   On top of that, most of the ETFs are short-able so we don’t have to worry about the short constraint.   In this project, we are trying to build a portfolio using 3 ETF pairs in oil (USO vs XLE), technology (XLK vs IYW), and financial sectors (XLF vs PSCF).

Over the long run, the overall performance of the miners is highly correlated with the commodities.  In short term, they may have divergences due to individual company’s performance or overall equity market performance, and hence the short term arbitrage opportunities may exist.  In technology sector, we attempt to seek mispricing on both large cap technology ETFs. Last, we attempt to see if arbitrage opportunity exists between the large and mid-cap financial ETFs.

Pair 1 - Oil Sector USO vs XLE

Cointegration Test

The above charts were generated in R Studio.   The in sample data generated between Jan 1st, 2011 and Dec 31, 2014.

First, we plot the price for the pairs and it gives us an impression that both price series are quite similar.  Then we perform the regression analysis for USO vs XLE (return USO = Beta * Return XLE + Residual) and find the beta or hedge ratio to be 0.7493.  Next, we apply the hedge ratio to generate the spread returns.  We can see the spread returns deviate closely around 0, which shows the characteristic of cointegrating pattern.  At last, we apply the Augmented Dickey-Fuller test with a confidence level at 0.2 and check if the pairs pass the ADF test.  The results are as follow:

data:(spread) Dickey-Fuller = -3.0375, Lag order = 0, p-value = 0.1391

alternative hypothesis: stationary

[1] "The spread is likely Cointegrated with a pvalue of 0.139136738842547"

With the p-value of 0.1391, the pairs satisfied the cointegration test, and we will go ahead and back-test the pairs in next section.

Strategy Back-Testing

The above back-testing result were generated in R Studio.  The back-testing period was using the in-sample data similar to the cointegration test.  Our trading strategy is relatively simple as follow:

If the spread is greater than +/- 1.5 standard deviations of its rolling lookback period of 120 days’ standard deviation, then we go short / long accordingly.

At all time, only 1 open position

Close the long/short position when the spread reverts to its mean/moving average.

The above back-testing result were generated in R-Studio using the PerformanceAnalystics package.  During the in sample back-testing period, the strategy achieved a cumulated return of 121.03% where the SPY (S&P500) had a cumulative return of 61.78%.  This translated into an annualized return of 22% and 12.82%, respectively.  In terms of risk analysis, the strategy had much lower annualized standard deviation of 11.63% vs. 15.35% in SPY.  The worst drawdown percentage for the strategy was 6.39% vs. 19.42% in SPY.  The annualized Sharpe ratio was superior in our strategy at 1.89 vs. 0.835 in SPY.  Please note that all of the above calculations did NOT factor into transaction cost.

Out of sample test

For the out of sample period between Jan 1st2015 and Dec 31, 2015, the pairs did not pass the ADF test suggested by a high p-Value at 0.3845.  The phenomenon could be explained by the sharp decline in cruel oil price where the equity market was persisting in an uptrend.  If we look at the spread returns, they first seem to be cointegrating around 0 but with a much larger deviation suggested by the chart below.

The actual spread obviously did not suggest a cointegrating pattern as indicated by the high p-Value.  Next, we will go ahead and back-test the same strategy using the out of sample data despite the pair fails the cointegration test.   The hedge ratio was found to be 1.1841.  The key back-testing results were generated in R-Studio as follow:

USO and XLE Stat Arb          SPYAnnualized Return           0.09862893 -0.007623957

USO and XLE Stat Arb          SPYCumulative Return           0.09821892 -0.007593818

USO and XLE Stat Arb         SPYAnnualized Sharpe Ratio (Rf=0%)            0.5632756 -0.04884633

USO and XLE Stat Arb       SPYAnnualized Standard Deviation            0.1750989 0.1560804

USO and XLE Stat Arb       SPYWorst Drawdown            0.1706643 0.1228571

At a first glance, the strategy seems outperform the SPY in all aspects, but due to the lookback period which was set same as in-sample back-testing data (120 days for consistency), this strategy only had 1 trade during the out of sample period, which may not reflect the situation going forward.  However, this shows that it is not necessary to have a perfect cointegrating pairs in order to extract profit opportunities.  In reality, only a few perfect pairs would pass the test.

Pair 2 – Large Cap Technology XLK vs. IYW

Cointegration Test

It should not be a surprise that XLK and IYW has a strong linear relationship as demonstrated in the regression analysis with a hedge ratio at 0.903.  The two large cap technology ETFs are very similar in nature except for its size, volume, expense ratio, etc.  However, if we take a closer look at the actual return spreads, it doesn’t seem to satisfy the cointegration test.  If we run the ADF test, the result shows they are not likely to be cointegrated with a p-Value at 0.5043.

Augmented Dickey-Fuller Test

data: (spread) Dickey-Fuller = -2.1748, Lag order = 0, p-value = 0.5043

alternative hypothesis: stationary

[1] "The spread is likely NOT Cointegrated with a pvalue of 0.504319921216107"

The purpose to run the strategy in this pair is to see if there is any mispricing (short term deviation) in the pair in order to profit from it.  In the USO and XLE example, we observed that profit opportunity may still exist despite the pair failing the cointegration test.  Here, we will go ahead to test the pair and see if any profit opportunity exists.

Back-testing Result

The back-testing results illustrated that the strategy performed very poorly during the back-testing period between Jan 1st2011 and Dec 31, 2014.  This demonstrates that the two ETFs are highly correlated to each other and it’s very hard to extract profit opportunity from them.  In order for a statistical arbitrage strategy to work, we need a pair with some volatility in their spreads but they should eventually show a mean-reverting pattern.  In next section, we will perform the same analysis on the Financial ETFs.

Pair 3 – Financial Sectors XLF vs. PSCF

Cointegration Test

In this pair, we attempt to seek a trading opportunity between the large financial cap ETF XLF and the small financial cap ETF PSCF.  From the price series they both show very similar pattern.  In terms of regression analysis, they obviously show a strong correlation with a hedge ratio of 0.9682.  The spread return also illustrates some cointegrating pattern with the spread deviating around 0.  The ADF test with test value set at 80% confidence shows the pair is likely to be cointegrated with a p-value at 0.1026.

Back-testing Result

XLF and PSCF Stat Arb       SPYAnnualized Return            0.01212355 0.1282006

XLF and PSCF Stat Arb       SPYCumulative Return            0.04923268 0.6177882

XLF and PSCF Stat Arb       SPYAnnualized Sharpe Ratio (Rf=0%)             0.1942203 0.8347157

XLF and PSCF Stat Arb      SPYAnnualized Standard Deviation            0.06242163 0.153586

XLF and PSCF Stat Arb       SPYWorst Drawdown            0.07651392 0.1942388

Although the pair satisfied the cointegration test with a low p-value, the back-testing results demonstrated a below average performance when we compare to the index return.

Conclusion

In this project, we chose 3 different pairs of ETFs to back test our simple mean-reverting strategy.  The back test results show superior performance on USO/XLE, but not on the other two pairs.  We can conclude that in order for thepair trading strategyto work, we do not need a pair that shows strong linear relationship, but a long term mean reverting pattern is essential to obtain a decent result.  In the pair XLK/IYW, we attempt to seek for mispricing between the two issuers, however, in an efficient ETF market in US, mispricing on such big ETFs is very rare, hence this strategy performs very poorly on this pair.  On the other hand, the correlation and cointegration test on the pair XLF/PSCF illustrate the pair is an ideal candidate to trade the statistical arbitrage strategy, however, the back-testing results show the other way around.  Any statistical arbitrage strategy we are essentially playing with the volatility, but if there is not enough volatility around the spreads to begin with, like the pair in XLK/IYW, the profit opportunity is trivial.   In the pair USO/XLE, the volatility around the spreads is ideal and the cointegration test shows the pair has a mean-reverting pattern, therefore it is not a surprise this pair prevails in the back-testing results.

Read about other strategies in this article onAlgorithmic Trading Strategy Paradigms. If you also want to learn more, you can explore ourAutomated Trading Coursehere.

Files in the download:

Project_Cointegration_Test.RProject_Backtest_Test.R

Project_Cointegration_Test.R

Project_Backtest_Test.R

Login to Download

---

*Imported from QuantInsti Blog on 2026-04-27*
