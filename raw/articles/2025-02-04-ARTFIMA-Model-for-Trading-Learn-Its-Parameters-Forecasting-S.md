---
title: "ARTFIMA Model for Trading: Learn Its Parameters, Forecasting Stock Prices in R, and Backtesting Strategies"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/artfima-model/"
date: "2025-02-04"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# ARTFIMA Model for Trading: Learn Its Parameters, Forecasting Stock Prices in R, and Backtesting Strategies

**来源**: [QuantInsti](https://blog.quantinsti.com/artfima-model/)  
**日期**: 2025-02-04  
**作者**: QuantInsti

---

## 原文

The ARTFIMA Model for Trading

ByJosé Carlos Gonzáles Tanaka

The ARFIMA model is well suited for capturing long-range memory in financial time series. However, it’s not always the case the time series exhibits long memory in their autocorrelation. The ARTFIMA model comes to the rescue to capture not only the long memory but also its short one and the relationships between them.

Needless to say, this model cannot only help capture those effects but also allows us to improve our strategy risk performance. While reading this blog, do not forget that, in finance, we not only care about returns but also about volatility. Let’s dive in!

Prerequisite knowledge needed to make the most of this blog post:

It is expected that you already understand concepts such asAutoRegressive Moving Average (ARMA) models,ARMA models using R, andAutoRegressive Fractionally Integrated Moving Average (ARFIMA) models.

You are expected to know how to use these models to forecast time series. You should also have a basic understanding of R or Python for time series analysis.

This blog covers:

What is an ARTFIMA model?

Parameters of the ARTFIMA Model

Estimation of an ARTFIMA model in R

An event-driven backtesting loop using the ARTFIMA model as a strategy

If you are new to building backtesting loops in Python, the Quantra course onbacktesting trading strategies pythonprovides the foundational framework before you implement more advanced models like ARTFIMA.

What is an ARTFIMA model?

You already know the ARIMA(p,d,q) model. You have a detailed theoretical explanation with backtesting scripts below:

AutoRegressive Moving Average (ARMA) models: A Comprehensive Guide

AutoRegressive Moving Average (ARMA) models: Using Python

AutoRegressive Moving Average (ARMA) models: Using R

Let’s write its equation:

Usually “d” is 0, when we model asset returns, and d=1 when we model asset prices, “d=2” when second differences of the original series are stationary, etc.

An ARFIMA(p,d,q) is the same as an ARIMA(p,d,q). The only difference is that for the ARFIMA model, “d” can take values between zero and one.

You have a detailed explanation in the following blog article:

AutoRegressive Fractionally Integrated Moving Average (ARFIMA) model

Here we provide a brief explanation. The ARFIMA model tries to capture the long memory of the price series, that is, the slowly-decaying autocorrelation function (ACF), which in turn means a high persistence of past values impacting today’s values in the time series.

However, it’s usually the case that short-term dependencies (like daily price correlation) and long-term dependencies (like trends that persist over weeks or months) coexist as phenomena describing financial time series. How to estimate this coexistence in such a way that we capture it and make it ready to improve our trading performance? Let’s see!

Parameters of the ARTFIMA Model

To understand how ARTFIMA works, let’s look at its main parameters and what they represent:

Autoregressive, AR(p), and Moving Average, MA(p), components:The first component captures the impact of previous values on recent ones. The second component relates to previous residual values' impact on the most recent time series values.

Fractional Integration (d):This is where ARFIMA and ARTFIMA shine compared to ARIMA. The fractional integration parameter (d) allows the model to capture long-memory effects, meaning it can model trends that decay slowly over time. While the ARIMA model has only integer values for “d”, the above 2 models can have values between 0 and 1.

Tempering Parameter (λ):A new parameter! Compared to the ARFIMA model, this is the secret sauce of the ARTFIMA model. The tempering parameter controls the rate at which long-memory effects decay. By estimating λ, you can fine-tune how the model balances short-term and long-term dependencies. A higher λ means the model focuses more on short-term fluctuations, while a lower λ emphasizes long-term trends.

The model can be written as follows:

\( X_t \) is our time series to be modeled

\( Y_t \) is an ARIMA(p,q) process

\( d \) is the fractional order of integration

\( \lambda \) is the tempering parameter

\( e \) is the exponential term

\( B \) is the lag operator

Whenever λ = 0, we are in the ARFIMA case. So the ARFIMA model is a sub-model of the ARTFIMA one.

In the ARFIMA model, a “d” value between -0.5 and 0.5 means it is stationary. In the ARTFIMA model, it is stationary for any value ofdthat is not an integer. So wheneverdis a real value, the ARTFIMA model will be stationary.

As a note to have: A larger value of d results in a stronger correlation, causing the ACF to decline more gradually as the lag increases. Conversely, a higher value of the tempering parameter λ leads to a faster decline in the ACF.

Estimation of an ARTFIMA model in R

The ARTFIMA model can be estimated using the Whittleestimation. However, we don’t need to invent the wheel. There’s an R package called “artfima” which can help us run the estimation smoothly. Let’s see!

We will estimate an ARTFIMA(1,d,1).

First, we install and import the necessary libraries:

Step 1: We import the Apple stock daily data from 1990 to 2025-01-26 and pass the data into a dataframe.

Step 2: We estimate an ARFIMA(1,d,1) with the “arfima” function provided by the “arfima” package.

Some things to note:

We’ve used the last 1500 observations of the data sample.

We choose ARTFIMA to set the glp input. This can also be ARIMA and ARFIMA.

We have set arimaOrder(p,d,q) as (1,0,1) so we let the model find d, but specify a single lag for the autocorrelation and and moving-average components.

We set the estimation algorithm as the Whittle.

Output

The relevant parameters to analyze are the following:

AIC and BIC are the Akaike and Bayesian information criteria, respectively.

mean is the average parameter of the model.

d is the fractional order of integration

lambda is the tempering parameter

phi(1) is the first autoregressive slope

theta(1) is the first moving-average slope

Est. represents the estimated value of the above last parameters.

se(est.) represents the estimated standard error of the above last parameters.

An event-driven backtesting loop using the ARTFIMA model as a strategy

We will compare an ARMA-based, ARFIMA-based, and ARTFIMA-based model trading strategy to see which one performs better!

We will use the Apple price time series again from 1990 to 2025-01-26. To estimate these models, we use the “artfima” package.

Step 1: Import the necessary libraries:

Step 2: Download data and create the adjusted close price returns.

Step 3: Create a “df_forecasts” dataframe in which we will save the 3 econometric signals.

Step 4: Set the list of possible lags for the autoregressive (p) and moving average (q) components.

Step 5: Create 3 functions:

The model_func: Use it to estimate the specific econometric model

The my_wrapper_func: Use it to wrap the above function inside this other function to control for model estimation errors or whether the model takes more than 10 minutes to complete.

The get_best_model: Estimate the best model as per the list of lags and the model type.

Step 6: Create a loop to estimate the daily ARIMA, ARFIMA, and ARTFIMA models. The “artfima” package allows us to estimate all the models using the same function. We just need to set “glp” according to each model. This backtesting loop is based on our previous articlesTVP-VAR-SVandARFIMAand their references.

Step 7: Create the ARIMA-based, ARFIMA-based and ARTFIMA-based cumulative returns.

Step 8: Let’s plot the three models’ cumulative returns

In terms of the equity curve's last values, the ARIMA-based strategy performs the best with respect to the other strategies’ performance and the buy-&-hold’s.

Let’s compute the statistics of each strategy:

Statistic

Buy and Hold

ARIMA model

ARFIMA Model

ARTFIMA Model

Annual Return

19.33%

19.30%

12.88%

11.94%

Cumulative Returns

20.60%

20.56%

13.70%

12.69%

Annual Volatility

22.84%

21.94%

16.39%

16.77%

Sharpe Ratio

Calmar Ratio

Max Drawdown

-15.36%

-14.27%

-11.67%

-11.79%

Sortino Ratio

According to the table, with respect to the annual return, the buy- & -hold performs the best, although only slightly compared to the ARIMA model. This latter model performs the best with respect to the risk-adjusted return as provided by the Sharpe ratio. Even in this situation, the last two models, the ARFIMA and ARTFIMA,  perform the best with respect to the annual volatility, it’s much lower for these two models compared to the buy-&-hold and ARIMA models.

Some considerations are to be taken into account. We didn’t

Incorporate slippage and commissions.

Incorporate a risk-management process.

Optimize the span

You can use Akaike to see the performance.

You can also use these models' forecasts as input features for a machine-learning model and predict a signal.

Conclusion

You’ve learned here the basics of the ARTFIMA model, its parameters, its estimation, and an event-driven backtesting loop to test it as a trading strategy. These econometric models always try to capture all the phenomena that happen in a time series we analyze. The ARTFIMA model, which tries to improve the ARFIMA model, uses a tempered parameter to capture the relationship between short- and long-term dependencies.

In case you want to learn more about time series models, you can profit from our courseFinancial Time Series Analysis for Trading. Here you will learn everything about the econometrics of time series. Don’t lose the opportunity to improve your strategy performance!

Continue learning:

Delve deeper into howAutoregressionserves as the foundation for time series analysis, including its application in trading strategies and Python-based examples.

Experiment with different techniques to find alpha by reading aboutMean Reversion StrategiesandMomentum Strategies. As you’ve seen, you can use the ARTFIMA model to predict next-day prices, which can further enhance the edge of these strategies.

Consider pursuing theExecutive Programme in Algorithmic Trading (EPAT)for a structured approach to algo trading and advanced applications — an ideal step for serious learners.

ExploreAll About Time Series: Analysis and Forecastingto gain essential insights into handling stationarity, seasonality, and practical forecasting methods.

Disclaimer: All investments and trading in the stock market involve risk. Any decision to place trades in the financial markets, including trading in stock or options or other financial instruments is a personal decision that should only be made after thorough research, including a personal risk and financial assessment and the engagement of professional assistance to the extent you believe necessary. The trading strategies or related information mentioned in this article is for informational purposes only.

---

*Imported from QuantInsti Blog on 2026-04-27*
