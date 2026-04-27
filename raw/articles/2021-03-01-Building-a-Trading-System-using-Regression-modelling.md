---
title: "Building a Trading System using Regression modelling"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/regression-trading-system/"
date: "2021-03-01"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Building a Trading System using Regression modelling

**来源**: [QuantInsti](https://blog.quantinsti.com/regression-trading-system/)  
**日期**: 2021-03-01  
**作者**: QuantInsti

---

## 原文

Building a Trading System using Regression Modelling

ByPavan Dutt

Building a trading system is the most significant phase in algorithmic trading. This is the phase that could transform our ideas or learnings into some real action. In simple terms, you are defining rules on when to open a trade and when to close the trade. Most of the automated trading systems provide an edge by eliminating human emotions and Bias in trading.

The ideal approach to build a trading system are:

Identifying the most suitable trading theme

Creating a strategy draft

Programming your trading logic

Backtestingand forward testing

Optimizing the results

Strategy validation

Live implementation

Validating the results

This article is a step-by-step illustration of building a simple template of a trading system using Regression modelling. We will cover the following topics in this blog:

Identifying the most suitable trading theme

Creating a strategy draft

What is regression analysis?

Prediction based trading setup using rolling regression

Let us now move to the first part of building the trading system.

Identifying the most suitable trading theme

There are many famous trading approaches which includemomentum trading,volatility trading strategy,mean reversion trading,trend following strategy, behavioural trading,Statistical arbitrage.

Each has its favourable market conditions, risk appetite, rewards. For example, since Tesla’s share price is increasing, it is said to be trending. Thus, you will try a trend following strategy here.

It is essential to know your area of interest and risk appetite before moving towards trading system development so that you can accept the system drawdowns.

In a nutshell, it is knowing what you based on what you can afford to lose before getting started.

Creating a strategy draft

After choosing your trading style, we will figure out the strategic approach which best suits your trading theme.

There are many ways we can analyzestock marketpatterns. Some of the popular ways to analyze them are price action based analysis, sentiment analysis and/or machine learning-based modelling. LearnPrice Action Trading Strategiesin detail in the Quantra course.

For the purpose of this article, we are building a trend following system based on regression modelling.

What is regression analysis?

Regression analysis is a supervised machine learning technique mainly used to forecast and trend projection and dependency between two stocks/assets in financial markets. The goal is to find the regression curve, which is least distant from all the data points.

Variables in Regression Analysis

Regression modelling typically has two kinds of variables:

Independent variables:These variables are independent of the output variable

Dependent variable:This variable is dependent on independent variables

Types of Regression Analysis

There are different types of regression analysis; some of the common types are:

Linear regression

Logistic regression

Polynomial regression

Lasso regression

Ridge regression.

As we want to keep the strategy simple, we will focus on linear regression analysis.

Linear Regression Analysis

Linear regression can be of two types:

Simple linear regression: If there is only one independent variable and a dependent variable, the linear regression equation is the line (linear/straight line) which is least distant from known dependent variables.

Multiple linear regression:  If there are more than one independent variables and a dependent variable, the regression equation is obtained by a linear combination of the dependent variables.

Prerequisites before coding

Before coding, make sure that you are familiar with basic concepts and python concepts like:

Pandas data frame and matplotlib

Statistical concepts

Ordinary least square method (for building regression model)

Rolling regression

Finance & performance metrics

Understanding, ROC (rate of change calculation), portfolio simulation

Understanding logic for calculation of different metrics like win ratio, CAGR (compound annual growth return), drawdown, etc.

Regression modelling in Python

We are using yfinance API for data fetching. This analysis is done using hourly data.

Understanding the data API

We are using yahoo finance python package (some other alternatives would be alpha vantage,quandl python api, pandas datareader).

The main functions are as follows:

yahoo finance.download (ticker, startdate, enddate): This gives us the daily data

yahoo finance.download (ticker,startdate,enddate,period=”60m”): This gives us the hourly data. Example: We are using Nifty 50 data from 1-1-2020 till 20-01-2021

Simple linear regression

We will build a regression model using the Ordinary least square method.

R-squaredis the most popular metric for depicting how good the linear regression model is. It typically gives an idea of how close the actual data is with respect to the regression line. R-squared value lies between 0 to 1, More the value of R2, more the fit is healthy.

Thecoefficient of Openmeans that Open and close are strongly positively correlated.

Prob of f statisticis the probability that the null hypothesis, “Regression coefficients are non-significant”. Since the probability is zero, this indicates that our independent variables are significant for performance.

So far we have used a simple linear regression model using OLS. The model seems to be good, and now we will look forward to extending these concepts in building a trading system.

One of the methods which you can try for improving your system is to use the concept of rolling regression.

Rolling regression

Rolling regression is fitting a regression line for every candle using previous n candles as a reference. This will let us develop a walk forward kind of trading model.

Like moving averages, the rolling regression uses previous n candles for reference to fit the regression model.

We will compute the rolling linear regression for our strategy simulation.

Prediction based trading setup using rolling regression

The strategy is pretty straight forward, the calculation is done to find the regression fit on every candle (can be on any time frame daily, weekly, intraday).

We fit regression line for every candle (with open as the independent variable and close as the dependent variable for previous n candles).

We predict the closing price of the current candle by passing the current candle's opening price as input.

If the predicted closing price > opening price, it is predicted that the price may rise and we go long.

If the predicted closing price < opening price, it is predicted that the price may fall and we go short.

Data used for simulation Nifty 1 hour charts from 1 Jan 2020, till 1 Jan 2020.

Note that slippages are not included.

The strategy is an intraday strategy because it is only taking candles open price into consideration (current candles open price is constant).

We see that the strategy has decent performance for the period of January 2020 to January 2021. You can go through the Python code by pressing the download button below.

Conclusion

We have seen the prediction based models in this article. The concept of linear regression, when applied on the historical data of the same dataset is called autoregression.

Autoregression is the foundation for various time series analysis models. You can learn about them in the Quantra courseFinancial Time Series Analysis for Trading.

File in the Download

Code for linear regression based trading system

Login to Download

All investments and trading in the stock market involve risk. Any decisions to place trades in the financial markets, including trading in stock or options or other financial instruments is a personal decision that should only be made after thorough research, including a personal risk and financial assessment and the engagement of professional assistance to the extent you believe necessary. The trading strategies or related information mentioned in this article is for informational purposes only.

---

*Imported from QuantInsti Blog on 2026-04-27*
