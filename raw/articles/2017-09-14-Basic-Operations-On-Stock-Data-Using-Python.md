---
title: "Basic Operations On Stock Data Using Python"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/basic-operations-stock-data-using-python/"
date: "2017-09-14"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Basic Operations On Stock Data Using Python

**来源**: [QuantInsti](https://blog.quantinsti.com/basic-operations-stock-data-using-python/)  
**日期**: 2017-09-14  
**作者**: QuantInsti

---

## 原文

Basic Operations On Stock Data Using Python

ByMilind Paradkar

This article illustrates basic operations that can be performed on stock data using Python to analyze and build algorithmic trading strategies. We run through some basic operations that can be performed on a stock data using Python and we start by reading the stock data from a CSV file.

Python has emerged as thefastest-growing programming languageand this has stemmed from multiple factors like ease to learn, readability, conciseness, strong developer community, application across domains etc.

Python has found wide acceptance in trading too and this has led to Python-based analytics platforms, Python APIs, and trading strategies being built using Python. With these foundational data operations in place, you are ready to move on totechnical analysis in Python, where the same OHLCV data is used to compute indicators like moving averages, RSI, and Bollinger Bands from scratch.

Given the growing popularity and ease to learn, theExecutive Programme in Algorithmic Trading(EPAT) offers a dedicated module which covers Quantitative Trading Strategies taught using Python.

The objective of this post is to illustrate how easy it is to learn Python and apply it to formulate and analyze trading strategies. If you are new to programming this blog might just help youovercome your fear of programming. Also, don’t forget to check out some nice links provided at the end of this blog to learn some exciting trading strategies which have been posted on our blog.

Let us run through some basic operations that can be performed on stock data using Python. We start by reading the stock data from a CSV file. The CSV file contains the Open-High-Low-Close (OHLC) and Volume numbers for the stock. You can download the Apple data from Yahoo Finance using the yfinance library.

# Importing necessary libraries and loading the dataset
import pandas as pd
import yfinance as yf


# Load stock data from a CSV file into a DataFrame
data = yf.download('AAPL', start='2020-01-01', group_by='tickers')['AAPL']


# Display the first few rows of the dataset to understand its structure
print(data.head())


The 'TIME' column seen here specifies the closing time of the day’s trading session. To delete the column we can simply use the 'del' command.# Deleting the "TIME" column
del data['TIME']Now, let us use the type function to check whether the object is a pandas datetime index.type(data.index)I would like to know the number of trading days (the number of rows) in the given data set. It can be done using the count method.# Number of rows in the data set
print(data['Close'].count())What if I want to know the maximum close price that was reached in the given period? This is made possible by using the max method.# Find the highest closing price
# Identify the maximum closing price in the dataset
max_price = data['Close'].max()


# Print the maximum closing price
print(max_price)Is it also possible to know the date on which this maximum price was reached? To find the respective date we apply the index property as shown below.Find the index of the maximum closing price
# Retrieve the index (row position) where the closing price equals the maximum
max_price_index = data[data['Close'] == max_price].index
print(max_price_index)Let us compute the daily percentage change in closing price. We add a new column of 'Percentage_Change' to our existing data set. In the next line of code, we have filtered the per cent change column for all the values greater than 1.0. The result has been presented below.Calculate and filter percentage change in closing prices
# Calculate daily percentage change in closing price
data['Percent_Change'] = data['Close'].pct_change() * 100


# Filter the rows where percentage change is greater than 1%
dt = data[data['Percent_Change'] > 1.0]


# Print the first few rows of the updated dataset
print(data.head())


# Print the filtered rows with significant price changes
print(dt.head())Finally, let us add a couple of indicators. We compute the 20-day simple moving average and the 5-day average volume. We can add more indicators to our data frame and then analyze the stock trend to see whether it is bullish or bearish. You can learn more on how to create variousTechnical Indicators Python.Compute moving average and average trading volume
# Define the number of days for calculating the moving average
ndays = 20


# Calculate the 20-day Simple Moving Average (SMA) for the closing price
SMA = pd.Series(data['Close'].rolling(window=ndays).mean(), name='SMA')


# Add the SMA as a new column to the original DataFrame
data = data.join(SMA)


# Calculate the 5-day average of trade volume
Avg_vol = pd.Series(data['Volume'].rolling(window=5).mean(), name='5day_AvgVol')


# Add the 5-day average volume to the DataFrame
data = data.join(Avg_vol)


# Print the last 7 rows of the final DataFrame with added indicators
print(data.tail(7))In his short post, we covered some simple ways to analyze the data set and build more understanding of the stock data.Can you think of building a trading strategy using similar basic operations and simple indicators?Simple trading strategies can be profitable and many successful traders will vouch for that. As mentioned at the start of the blog, here are the links to some trading strategies in Python that can be explored for your own trading needs.Recommended reads:Trading Using Machine Learning In Python – SVM (Support Vector Machine)Strategy using Trend-following Indicators: MACD, ST and ADXSentiment Analysis on News Articles using PythonPython Trading Strategy in Quantiacs PlatformPython algorithmic trading has gained traction in the quant finance community as it makes it easy to build intricate statistical models with ease due to the availability of sufficient scientific libraries like Pandas, NumPy, PyAlgoTrade, Pybacktest and more.In our upcoming posts, we will provide more ways and methods that can be used for trading using Python. Keep following our posts.In case you are looking to master the art of using Python to generate trading strategies, backtest, deal with time series, generate trading signals, predictive analysis and much more, you can enroll for our course onPython for Trading!Disclaimer: All investments and trading in the stock market involve risk. Any decisions to place trades in the financial markets, including trading in stock or options or other financial instruments is a personal decision that should only be made after thorough research, including a personal risk and financial assessment and the engagement of professional assistance to the extent you believe necessary. The trading strategies or related information mentioned in this article is for informational purposes only.Files in the downloadBasic Operations On Stock Data - Python CodeLogin to Download

# Deleting the "TIME" column
del data['TIME']

Now, let us use the type function to check whether the object is a pandas datetime index.

type(data.index)

I would like to know the number of trading days (the number of rows) in the given data set. It can be done using the count method.

# Number of rows in the data set
print(data['Close'].count())

What if I want to know the maximum close price that was reached in the given period? This is made possible by using the max method.

# Find the highest closing price
# Identify the maximum closing price in the dataset
max_price = data['Close'].max()


# Print the maximum closing price
print(max_price)

Is it also possible to know the date on which this maximum price was reached? To find the respective date we apply the index property as shown below.

Find the index of the maximum closing price
# Retrieve the index (row position) where the closing price equals the maximum
max_price_index = data[data['Close'] == max_price].index
print(max_price_index)

Let us compute the daily percentage change in closing price. We add a new column of 'Percentage_Change' to our existing data set. In the next line of code, we have filtered the per cent change column for all the values greater than 1.0. The result has been presented below.

Calculate and filter percentage change in closing prices
# Calculate daily percentage change in closing price
data['Percent_Change'] = data['Close'].pct_change() * 100


# Filter the rows where percentage change is greater than 1%
dt = data[data['Percent_Change'] > 1.0]


# Print the first few rows of the updated dataset
print(data.head())


# Print the filtered rows with significant price changes
print(dt.head())

Finally, let us add a couple of indicators. We compute the 20-day simple moving average and the 5-day average volume. We can add more indicators to our data frame and then analyze the stock trend to see whether it is bullish or bearish. You can learn more on how to create variousTechnical Indicators Python.

Compute moving average and average trading volume
# Define the number of days for calculating the moving average
ndays = 20


# Calculate the 20-day Simple Moving Average (SMA) for the closing price
SMA = pd.Series(data['Close'].rolling(window=ndays).mean(), name='SMA')


# Add the SMA as a new column to the original DataFrame
data = data.join(SMA)


# Calculate the 5-day average of trade volume
Avg_vol = pd.Series(data['Volume'].rolling(window=5).mean(), name='5day_AvgVol')


# Add the 5-day average volume to the DataFrame
data = data.join(Avg_vol)


# Print the last 7 rows of the final DataFrame with added indicators
print(data.tail(7))

In his short post, we covered some simple ways to analyze the data set and build more understanding of the stock data.

Can you think of building a trading strategy using similar basic operations and simple indicators?

Simple trading strategies can be profitable and many successful traders will vouch for that. As mentioned at the start of the blog, here are the links to some trading strategies in Python that can be explored for your own trading needs.

Recommended reads:

Trading Using Machine Learning In Python – SVM (Support Vector Machine)

Strategy using Trend-following Indicators: MACD, ST and ADX

Sentiment Analysis on News Articles using Python

Python Trading Strategy in Quantiacs Platform

Python algorithmic trading has gained traction in the quant finance community as it makes it easy to build intricate statistical models with ease due to the availability of sufficient scientific libraries like Pandas, NumPy, PyAlgoTrade, Pybacktest and more.

In our upcoming posts, we will provide more ways and methods that can be used for trading using Python. Keep following our posts.

In case you are looking to master the art of using Python to generate trading strategies, backtest, deal with time series, generate trading signals, predictive analysis and much more, you can enroll for our course onPython for Trading!

Disclaimer: All investments and trading in the stock market involve risk. Any decisions to place trades in the financial markets, including trading in stock or options or other financial instruments is a personal decision that should only be made after thorough research, including a personal risk and financial assessment and the engagement of professional assistance to the extent you believe necessary. The trading strategies or related information mentioned in this article is for informational purposes only.

Files in the download

Basic Operations On Stock Data - Python Code

Login to Download

---

*Imported from QuantInsti Blog on 2026-04-27*
