---
title: "Augmented Dickey Fuller (ADF) Test for a Pairs Trading Strategy"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/augmented-dickey-fuller-adf-test-for-a-pairs-trading-strategy/"
date: "2022-07-25"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Augmented Dickey Fuller (ADF) Test for a Pairs Trading Strategy

**来源**: [QuantInsti](https://blog.quantinsti.com/augmented-dickey-fuller-adf-test-for-a-pairs-trading-strategy/)  
**日期**: 2022-07-25  
**作者**: QuantInsti

---

## 原文

Augmented Dickey Fuller (ADF) Test for a Pairs Trading Strategy

ByChainika Thakar

Augmented Dickey Fuller Test, denoted by "ADF", serves the purpose of finding out which stocks can be paired together in the pairs trading strategy. For the strategy to work effectively, it is important to find the pair of stocks that are co-integrated.

The statistical calculation for testing the co-integration is done with Augmented Dickey Fuller Test. In this blog, we will be discussing the ADF test for pairs trading strategy.

This blog covers:

What is a pairs trading strategy?

Essential terms used in the Augmented Dickey Fuller TestStationary time seriesNon-stationary time seriesUnit root

Stationary time series

Non-stationary time series

Unit root

What is ADF testing?

What does the ADF test check in pairs trading?

Difference between DF test and ADF test

Working of the Augmented Dickey Fuller test

Formula of ADF test

Calculation of ADF test

ADF Test using Excel

ADF Test using Python

Advantages of ADF testing

Disadvantages of ADF testing

What is a pairs trading strategy?

The origin of the pairs trading strategy was back in the early 1980s. The strategy was initially developed by stock market technical analysts and researchers who were employees of the renowned investment banking and financial company – Morgan Stanley.

In order to implement thepairs tradingstrategy, one needs technical and statistical analysis skills. The pairs trading strategy basically requires two stocks or securities to co-integrate so that they can be considered as a pair for trading.

Hence, a positive correlation is needed.

List of Quant Jobs

15 min read

After the securities show co-integration, from the pair of stocks, you enter a long position in one stock and a short position in the other. The positions are based on the current market price of both the stocks and theirstandard deviation.

Here is a short, educational video that explains the pairs trading method in about 3 minutes. Find out how to combine securities and optimizing your investments using a market-neutral method.

Essential terms used in the Augmented Dickey Fuller Test

Stationary time series

Stationarity means that the statistical properties of a time series i.e. mean, variance and covariance do not change over time which implies that the time series has no unit root.

In the case of stationarity, trading signals are generated assuming that the prices of both stocks will revert to the mean eventually. Hence, we can take the advantage of the prices that deviate from the mean for a short period of time.

Grasping the concept ofStationary Time Seriescan significantly enhance your trading strategy. By understanding how mean reversion works in stationary data, you can identify profitable opportunities when prices temporarily deviate. Explore more to discover how this powerful concept can improve your decision-making and increase the effectiveness of your trading signals.

Non-stationary time series

A time series with a unit root is non-stationary and will have changes in its mean, variance and covariance over time. Due to the non-stationarity of time series, the trading signals cannot be generated.

Below, you can see a plot of an asset which is a non-stationary time series with a deterministic trend represented by the“blue”curve and its detrended stationary time series represented by the“red”curve.

Unit root

​​The unit root is a characteristic of a time series that makes it non-stationary. Technically speaking, a unit root is said to exist in a time series of the value of alpha = 1 in the below equation.

where, Yt is the value of the time series at the time ‘t’ and Xe is an exogenous variable (a separate explanatory variable, which is also a time series).

What is ADF testing?

The Augmented Dickey Fuller test (ADF) is a modification of theDickey-Fuller(DF) unit root.

Dickey-Fuller used a combination of T-statistics and F-statistics to detect the presence of a unit root intime series.

ADF test in pairs trading is done to check the co-integration between two stocks (presence of unit root).

If there is a unit root present in the time series, it implies that the time series is non-stationary and the stocks are not co-integrated. Hence, stocks cannot be traded together.

Alternatively, if the null hypothesis gets rejected and the stocks show co-integration; it implies that the time series is stationary and the stocks can be traded.

Statistical Arbitrage: from A to Z

8 min read

What does the ADF test check in pairs trading?

The main point of conducting an ADF test in pairs trading strategy is to ensure if the pair of stocks considered in the strategy are stationary or not.

Hence, for the pair of stocks to be traded in the pairs trading strategy, it is required that the time series is stationary. A stationary time series makes effective and precise predictions.

Also, a stationary time series means that the pair of stocks isco-integratedand can be traded together by generating trading signals.

Difference between DF test and ADF test

The following are the differences between the Dickey-Fuller test and the Augmented Dickey Fuller test (ADF test).

Dickey-Fuller Test

The Dickey-Fuller Test is a statistical test that is used to determine if there is a unit root in the data i.e., whether the time series is stationary or non-stationary. The test was developed by Robert Dickey and Thomas Fuller in 1979.

Augmented Dickey-Fuller Test

The augmented Dickey-Fuller test is an extension of the standard Dickey-Fuller test, which also checks for both stationarity and non-stationarity in the time series.

The main difference from the Dickey Fuller Test is that the Augmented Dickey Fuller test can also be applied on a large sized set of time series models. The large sized time series models can be more complicated and hence, the DF test was modified into the ADF Test. Also, the ADF Test works on the data with missing values.

Key points

The primary difference between the two tests is that the ADF is utilised for a larger sized set of time series models which can be more complicated.

The ADF test is an alternative to DF because it can be used even when there aremissing valuesin the data.

Working of the Augmented Dickey-Fuller test

Now, let us find the working of an Augmented Dickey-Fuller test. We will begin with the hypothesis and advance to the calculation and its working in both Excel as well as Python.

Hypothesis

The Augmented Dickey-Fuller test is based on two hypothesis:

The null hypothesis states that there exists a unit root in the time series and is non-stationary.

The alternative hypothesis states that there exists no unit root in the time series and is stationary or trend stationary.

To apply this in a mean reversion strategy using Python, the test helps confirm whether the time series is stationary, a crucial factor when building amean reversion strategy in Python.

List of Quant Jobs

15 min read

Formula of ADF test

Let us first see the formula for Dickey Fuller Test (which is the origin of Augmented Dicket Fuller Test), and that is:

where,yt= value in the time series at time t or lag of 1 time seriesdelta yt= first difference of the series at time (t-1)

Now, we will see the formula for Augmented Dickey Fuller test, and it goes as follows:

You can see that the formula for ADF is the same equation as the DF with the only difference being the addition of differencing terms representing a larger time series.

Calculation of ADF test

The test is most easily performed by rewriting the model:

where,

The hypothesis (1) = 0 again corresponds to

H0 : π = 0    HA : π < 0

The t−test for H0 is denoted as the augmented Dickey-Fuller (ADF) test.

ADF Test using Excel

Let us see the step-by-step working of the ADF test in the excel sheet.

Step 1: Get the data for two stocks that you want to perform an ADF test on

In this example, I have taken the two stocks Zymergen Inc (NASDAQ: ZY) and Zynerba Pharmaceuticals Inc (NASDAQ: ZYNE) both belong to the Pharmaceutical industry and are listed on American Stock Exchange “NASDAQ”.

Also, the number of observations that I'm using here is 60.

Take a look at the image below, to understand how the data with close price of each stock is represented side by side in the excel sheet.

Statistical Arbitrage: from A to Z

8 min read

Step 2: Perform a linear regression on the two stocks using a set number of observations

Make sure you also request the residuals to be outputted.

*Note*:When running this in a pairs trading strategy you will have to run the ADF test every day to make sure that the Null hypothesis is rejected (Null hypothesis = there is a unit root).

Here’s how it will be done in the excel sheet.

The X Variable Coefficient of -3.98 is what we will be using for the hedge ratio.

Step 3: Calculate the difference between the residuals in the column “Delta”

List of Quant Jobs

15 min read

Step 4: Calculate the t-1 residual in the next column

Step 5: Perform a linear regression on the Delta and t-1 column

Step 6: Compare the t-test statistic and the critical value

In order to reject the null hypothesis that there is a unit root present, the t-statistic, in this case, must be within the critical value range. The critical values for an ADF test have their own distribution and here’s a snapshot of some of the critical values:

We will be using the Critical value of -2.89 since we have less than 100 observations

The t-stat is -1.109.

Therefore the null hypothesis is rejected and we can say that the data of the pair is co-integrated.

List of Quant Jobs

15 min read

ADF Test using Python

Now, let us find out how the ADF Test can be done using Python with another pair of stocks (Apple and Microsoft) as used above.

Now, we will check the cointegration by running the Augmented Dickey Fuller test. Using the statsmodels.api library, we compute the Ordinary Least Squared regression on the closing price of the stock pair and store the result of the regression in the variable named ‘result’.

Using the statsmodels.tsa.stattools library, we run the adfuller test by passing the residual of the regression as the input and store the result of this computation in the array “c_t”.

This array contains values like the t-statistic, p-value, and critical value parameters. Here, we consider a significance level of 0.1 (90% confidence level). “c_t[0]” contains the t-statistic, “c_t[1]” contains the p-value and “c_t[4]” stores a dictionary containing critical value parameters for different confidence levels.

For co-integration we consider two conditions:

First, we check whether the t-stat is less than or equal to the critical value parameter (c_t[0] <= c_t[4]['10%'])

Second, we find out whether the p-value is lesser than the significance level (c_t[1] <= 0.1).

If any one of these conditions is true, we print that the “Pair of securities is co-integrated”, else print that the “Pair of securities is not co-integrated”.

Output:

Date
2022-07-05    139.324753
2022-07-06    140.663269
2022-07-07    144.039154
2022-07-08    144.718246
2022-07-11    142.582489
Name: AAPL, dtype: float64
Date
2022-07-05    256.347473
2022-07-06    259.624359
2022-07-07    261.760162
2022-07-08    261.038513
2022-07-11    257.966400
Name: MSFT, dtype: float64
Pair of securities is not co-integrated

The output above shows that the pair of securities is not co-integrated and hence, cannot be traded together.

Statistical Arbitrage: from A to Z

8 min read

Advantages of ADF testing

Let us now look at the advantages of using the ADF test.

The first and foremost advantage of implementing the pairs trading strategy is that it can help you to maximise your returns.

ADF test also helps in mitigating the potential risk at the same time since it hedges the portfolio of two stocks.

Disadvantages of ADF testing

ADF testing comes with its own set of cons as well. Let us take a look at these cons.

The biggest con is that the ADF test relies on a high statistical correlation between the securities which might be difficult for the ones who are not great at statistical analysis.

Also, historical trends may be mostly accurate, but they do not guarantee an indication of future trends. Pairs traders usually look for a correlation of 0.80 which can also lower the chances of expected returns.

Conclusion

Augmented Dickey Fuller Test is a statistical test that can be performed in both Excel as well as Python and is relevant for those who employ a pairs trading strategy. ADF test is an effective test for finding out which stocks can be paired together to maximise the returns on the strategy.

If you also wish to find out more about this statistical test, you can enrol in our course onStatistical Arbitrage Tradingand find out all about the ADF test. Learning about the ADF testing can help you find more trading opportunities with different pairs of stocks. Additionally, you will learn how to create trading models using Excel and Python as well as how tobacktestthem.

File in the download

Pairs trading stocks - Excel file

Login to Download

Pairs trading stocks - Python notebook

Login to Download

Note: The original post has been revamped on 25th July 2022 for accuracy, and recentness.

Disclaimer: All investments and trading in the stock market involve risk. Any decision to place trades in the financial markets, including trading in stock or options or other financial instruments is a personal decision that should only be made after thorough research, including a personal risk and financial assessment and the engagement of professional assistance to the extent you believe necessary. The trading strategies or related information mentioned in this article is for informational purposes only.

---

*Imported from QuantInsti Blog on 2026-04-27*
