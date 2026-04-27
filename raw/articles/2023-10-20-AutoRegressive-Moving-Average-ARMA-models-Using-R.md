---
title: "AutoRegressive Moving Average (ARMA) models: Using R"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/autoregressive-moving-average-arma-model-r/"
date: "2023-10-20"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# AutoRegressive Moving Average (ARMA) models: Using R

**来源**: [QuantInsti](https://blog.quantinsti.com/autoregressive-moving-average-arma-model-r/)  
**日期**: 2023-10-20  
**作者**: QuantInsti

---

## 原文

AutoRegressive Moving Average (ARMA) models: Using R

ByJosé Carlos Gonzáles Tanaka

In theAutoRegressive Moving Average (ARMA) models: A Comprehensive Guideof my ARMA article series, I covered the theoretical aspects of Autoregressive Moving Average models (ARMA). In theAutoRegressive Moving Average (ARMA) models: Using Python, I simulated different ARMA models, their autocorrelations and their partial autocorrelations. We also provided a strategy based on these models. In this article, we'll do the same as in part 2 but the implementation will be made in R. Let's enjoy!

We cover:

Simulation of ARMA models

Autocovariance and autocorrelation functions in R

Estimation of the best ARMA model with real-world data in R

Simulation of ARMA models

Because there is no second without a third, we have this article to use the ARMA models in R. Let’s code.

Import libraries

First, we install and import the necessary libraries

Create an empty dataframe in R

Then we create an empty dataframe with 1000 rows as previously done in Python.

Simulate ARMA models using R

Next, we simulate the ARMA models as we did before. However, we’re going to make a change. This time we’re going to use the Autoregressive integrated moving average (ARIMA) function provided by the forecast library to create the models.

This is an opportunity to see a different code here in R!

Suggested Reads:

Autocorrelation and Autocovariance: Calculation, Examples, and More

How to Get Historical Market Data Through Python Stock API

Autocovariance and autocorrelation functions in R

Last but not least, this time we’re going to plot the Autocorrelation function (ACF) and Partial Autocorrelation Function (PACF) of only theAutoregressive(AR) models.

Check the plots

We leave it as an exercise to plot the same graphs for the MA processes.

Quantitative Trading Strategies and Models

Elevate Your Trading with Quantitative Trading Strategies and Models Course

Estimation of the best ARMA model with real-world data in R

We’ll now create the strategy (covered in Pythonhere) in R.

I’ve made some minor modifications here to what we did in Python in myprevious post,AutoRegressive Moving Average (ARMA) models: Using Python.

We use Microsoft stock from the 90s up to September 9th, 2023.

We create a long-only strategy (We leave it as an exercise to go short, too)

For each day estimation, we use the whole previous historical data span to estimate the model, i.e., we make rolling forecasts each day.

Estimate the model with a function called “auto.arima”, which automatically estimates a range of ARMA models without a loop.

We set:

Maximum p and q equal to 5

We set stationary to True since we will use returns as the model data input.

We do not estimate seasonal components, so we set it to False.

We don’t allow drift in the data since returns are stationary

We don't compute a mean so we set it to False.

We set stepwise to True so it searches over all models and makes a stepwise selection.

Check the graph

Some suggestions:

You see an equal performance w.r.t. the buy and hold performance. You might need to change the training span to improve it.

You can change to short the stock if there’s an improvement.

We use all the historical data span for each data. You can change that, too.

You can change the R code to go long only and see if there’s an improvement in the Apple stock strategy performance.

Conclusion

We have tried to help you develop a basic understanding of the ARMA model over three posts. We simulated various models in two different ways (through a loop in Python and through a library function in R).

Besides, you learned how to plot the autocovariance and autocorrelation functions in subplots. Finally, you know now how to develop a strategy both in Python and R. Both languages are useful to work with financial market data.

This model is an econometric model. Do you want to learn more about this topic and other algo trading models? Don’t hesitate to subscribe to our courseAlgorithmic Trading for Beginners! You’ll learn a lot!

File in the download

R code for ARMA models in R

Login to Download

Disclaimer: All investments and trading in the stock market involve risk. Any decision to place trades in the financial markets, including trading in stock or options or other financial instruments is a personal decision that should only be made after thorough research, including a personal risk and financial assessment and the engagement of professional assistance to the extent you believe necessary. The trading strategies or related information mentioned in this article is for informational purposes only.

---

*Imported from QuantInsti Blog on 2026-04-27*
