---
title: "The Hurst Exponent"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/hurst-exponent/"
date: "2018-10-29"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# The Hurst Exponent

**来源**: [QuantInsti](https://blog.quantinsti.com/hurst-exponent/)  
**日期**: 2018-10-29  
**作者**: QuantInsti

---

## 原文

Hurst Exponent: Calculation, Values and More

ByVibhu Singh,Varun Divakarand Ashish Garg

This blog covers theHurst exponent, a crucial concept in time series analysis, which helps in identifying whether a time series is mean-reverting, random, or trending. Before diving into this topic, it is essential to build a strong foundation in time series concepts.

Pre requisites

Start withIntroduction to Time Series, which explains the fundamentals of time series, its importance in financial markets, and various forecasting techniques.By familiarizing yourself with these foundational concepts, you'll be better equipped to interpret the significance of the Hurst exponent and apply it effectively in trading and investment strategies.

Hurst Exponent Definition

The Hurst exponent is used as a measure of long-term memory of time series. It relates to the autocorrelations (You can read more aboutAutocorrelation and Autocovariance.) of the time series and the rate at which these decrease as the lag between pairs of values increases.

Hurst Value

Hurst Value is more than 0.5

If the Hurst value is more than 0.5 then it would indicate a persistent time series (roughly translates to a trending market).

Hurst Value is less than 0.5

If the Hurst Value is less than 0.5 then it can be considered as an anti-persistent time series (roughly translates to sideways market).

Hurst Value is 0.5

If the Hurst value is 0.5 then it would indicate arandom walkor a market where prediction of future based on past data is not possible.

How To Calculate The Hurst Exponent

To calculate the Exponent, we need to divide the data into different chunks. For example, if you have the return data of BTC/USD for the past 8 days’ data, then you divide it into halves as follows.

Following the example of 8 observations for illustrative purposes only1:

1Length of the subseries in practical applications is usually much longer and affects the mean and standard deviation of the R/S statistic.

Then, we divide the data into 3 different chinks as follows:

Division 1 - one chunk of 8 observations

Division 2 - two chunks of 4 observations each

Division 3 - four chunks of 2 observations each

After dividing the data into chunks, we perform the following calculations on each chunk:

Step 1

First we calculate the mean of the chunk, with say n observations,

M = (1/n) [ h(1)+h(2)+...+h(n) ]

Step 2

Then we calculate thestandard deviation(S) of the n observations

s(n) = STD( h(1)+h(2)+...+h(n))

Step 3

Then we create a mean centered series by subtracting the mean from the observations,

x(1) = h(1) - M x(2) = h(2) - M ... x(n) = h(n) - M

Step 4

Then we calculate the cumulative deviation by summing up the mean centred values,

Y(1) = x(1) Y(2) = x(1) + x(2) ... Y(n) = x(1) + x(2) + ...+ x(n)

Step 5

Next, we calculate the Range (R), which is the difference between the maximum value of the cumulative deviation and the minimum value of the cumulative deviation:

Step 6

And finally, we compute the ratio of the range R to the standard deviation S. This also known asthe rescaled range.

Step 7

Once we have the rescaled range for all the chunks, we compute the mean of each Division and note it along with the number of samples in each chunk of that Division as shown.

Step 8

Next, we calculate the logarithmic values for the size of each region and for each region’s rescaled range.

Result

The Hurst exponent ‘H’ is nothing but the slope of the plot of each range’s log(R/S) versus each range’s log(size).

Here log(R/S) is the dependent or the y variable and log(size) is the independent or the x variable:

Conclusion

This hurst exponent value is indicating that our data is a persistent one, but we have to keep in mind that our data set is too small to draw such a conclusion.

For example, if you want to calculate hurst exponent in python using the ‘hurst’ library, it requires you to give at least 100 data points.

We hope you have learnt how to calculate the Hurst exponent from this blog. In ouradvanced course on cryptocurrencies, we have demonstrated how hurst exponent along with another technical indicator can yield optimized trading signals.

Next steps

Now that you have learnt about Hurst Exponent and Time series, let's dive deeper intoMean Reversionin time series to understand how and why time‐series data exhibit long‐term memory.

Once you’re comfortable with these, progress to advanced or multivariate methods, includingVector Autoregression (VAR),Johansen Cointegration, andTime-Varying-Parameter VAR.

This comprehensive roadmap equips you with the necessary background to fully appreciate this Blog. You are expected to know how to use these models to forecast time series. You should also have a basic understanding of R or Python for time series analysis.

Strengthen your grasp by looking intoAutocorrelation & Autocovarianceto see how data points relate over time, then deepen your knowledge with fundamental models such asAutoregression (AR),ARMA,ARIMAandARFIMA.

If your goal is to discover alpha, you may want to experiment with a variety of techniques, such astechnical analysis,trading risk management,pairs trading basics, andMarket microstructure. By combining these approaches, you can develop and refine trading strategies that better adapt to market dynamics.

Check out this learning track onAlgorithmic Trading in Cryptocurrency and Forex, this covers Hurst exponent strategy. Also, you can check out the new course onQuant Investing for Portfolio Managers, Generalized Hurst Exponent. You will learn the Generalized Hurst Exponent as a tool to analyse market trends, identify momentum, and refine factor timing strategies.

For a structured approach to algo trading and to master advanced statistics for quant strategies consider thebest algorithmic trading course, the Executive Programme in Algorithmic Trading (EPAT). This rigorous course covers time series fundamentals (stationarity, ACF, PACF), advanced modelling (ARIMA, ARCH, GARCH), and practical Python‐based strategy building, providing the in‐depth skills needed to excel in today’s financial markets.

Disclaimer: All investments and trading in the stock market involve risk. Any decisions to place trades in the financial markets, including trading in stock or options or other financial instruments is a personal decision that should only be made after thorough research, including a personal risk and financial assessment and the engagement of professional assistance to the extent you believe necessary. The trading strategies or related information mentioned in this article is for informational purposes only.

---

*Imported from QuantInsti Blog on 2026-04-27*
