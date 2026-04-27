---
title: "Python Trading Strategy in Quantiacs Platform"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/python-trading-strategy-quantiacs-platform/"
date: "2017-05-23"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Python Trading Strategy in Quantiacs Platform

**来源**: [QuantInsti](https://blog.quantinsti.com/python-trading-strategy-quantiacs-platform/)  
**日期**: 2017-05-23  
**作者**: QuantInsti

---

## 原文

Python Trading Strategy In Quantiacs Platform

ByMilind Paradkar

Algorithmic trading has seen great traction in recent years and the numbers of students, engineering graduates, and finance professionals looking to explore this lucrative domain has been growing exponentially with each passing year.

Are you among the ones looking to learn quant skills and also make money with your trading ideas? Let us explore the Quantiacs platform which allows one to create, run and implement yourhttps://blog.quantinsti.com/python-trading-library/Python trading strategy. Quantiacs offers great earning opportunities for successful quants.

Quantiacs Toolbox

The Quantiacs toolbox is free and open-source. Quantiacs provides up to 25 years of free data for 49 futures and S&P 500 stocks. The toolkit allows the user to create a trading strategy and backtest it with data all the way back to 1990.  In addition to futures data, Quantiacs has recently added macroeconomic data which can be used in conjunction with the price time series data to improve the trading algorithms. Quantiacs supports both Python and Matlab. In this post, we will explore the Python toolbox and illustrate a toy strategy using it.

Quantiacs Python Toolbox

Quantiacs has created a simple yet powerfulPython frameworkwhich can be used to create different types of algorithmic strategies. It provides for defining trading system settings like loading market data, trading costs, custom fields, capital etc. Others features of the Python toolbox include evaluating the trading system, optimization, visualization of results etc. Let us explore some features of the Python framework here.

Loading the market data:

Quantiacs trades in both stock and futures markets. Here is what the data fields look like for a stock:

Source: Quantiacs.com

We can load the stock data in Python using the quantiacsToolbox.loadData function.

As can be seen, the data is in the form of a Python dictionary. Let us check the data type of the key-value pairs.

To create aPython tradingstrategy we will have to manipulate the numpy array and it is required that you have a good understanding of Python numpy arrays and the myriad functions that it supports. Here’s alist of some useful functions.

Candle High-Low Python Strategy

Now let us take a very simple candle high-low strategy and try to code it using the Quantiacs toolbox. The step-by-step process has been illustrated below.

Step 1: Define the Settings

We test our sample strategy on Apple Inc. (AAPL) and Amazon Inc. (AMZN) stocks. The backtest period is defined in settings['beginInSample'] and  settings['endInSample']  variables. We also define the lookback days, capital and the slippage.

Step 2: Python Trading Strategy

We have kept our strategy simple. In the first step, we define the number of candles which represent the number of the previous prices that will be considered for generating a buy/sell signal. We then compute the price difference of the last ‘n’ candles. If all the price differences are positive we go short expecting a mean reversion behaviour. If all the price differences are negative we go long.

The long position is indicated by the value 1, while the short position takes the value of -1.

Step 3: Run the Strategy

To execute our strategy, we use the quantiacsToolbox.runts command and specify the respective Python file.

Step 4: Visualize the results

Upon execution, the Python framework displays a very informative chart which includes the markets, an option to select the exposure type, various performance metrics etc.

As can be seen, the Quantiacs Python framework is easy to use and can be used to develop varied trading strategies.

Next Step

Python algorithmic trading has gained traction in the quant finance community as it makes it easy to build intricate statistical models with ease due to the availability of sufficient scientific libraries like Pandas, NumPy, PyAlgoTrade, Pybacktest and more.

In case you are looking to master the art of using Python to generate trading strategies, learnhow to backtest a trading strategy, deal with time series, generate trading signals, predictive analysis and much more, you can enroll for our course onPython for Trading!

For a broader foundation that goes beyond Python alone covering market microstructure, risk management, and strategy execution analgorithmic trading courseprovides the complete framework.

Disclaimer: All investments and trading in the stock market involve risk. Any decisions to place trades in the financial markets, including trading in stock or options or other financial instruments is a personal decision that should only be made after thorough research, including a personal risk and financial assessment and the engagement of professional assistance to the extent you believe necessary. The trading strategies or related information mentioned in this article is for informational purposes only.

Download Python Code

Candle High Low Strategy - Python Code

Login to Download

---

*Imported from QuantInsti Blog on 2026-04-27*
