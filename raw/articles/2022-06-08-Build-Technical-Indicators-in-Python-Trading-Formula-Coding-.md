---
title: "Build Technical Indicators in Python: Trading, Formula, Coding and More"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/build-technical-indicators-in-python/"
date: "2022-06-08"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Build Technical Indicators in Python: Trading, Formula, Coding and More

**来源**: [QuantInsti](https://blog.quantinsti.com/build-technical-indicators-in-python/)  
**日期**: 2022-06-08  
**作者**: QuantInsti

---

## 原文

Building Technical Indicators in Python

ByChainika ThakarandDanish Khajuria

A technical Indicator is essentially a mathematical representation based on data sets such as price (high, low, open, close, etc.) or volume of security to forecast price trends.

There are several kinds of technical indicators that are used to analyse and detect the direction of movement of the price. For instance,momentum trading,mean reversion strategyetc. Traders use indicators usually to predict future price levels while trading.

Let us find out how to build technical indicators using Python with this blog that covers:

What are technical indicators?

Why use Python technical indicators?

Technical indicators for tradingMoving averagePython code for Moving AverageBollinger BandsCalculation for Bollinger BandsPython code for Bollinger BandsRelative Strength IndexCalculation for RSIPython code for RSIMoney Flow IndexPython code for MFIAverage True RangePython code for ATRForce IndexCalculation for Force IndexPython code for Force IndexEase of MovementCalculation for EVMPython code for EVM

Moving averagePython code for Moving Average

Python code for Moving Average

Bollinger BandsCalculation for Bollinger BandsPython code for Bollinger Bands

Calculation for Bollinger Bands

Python code for Bollinger Bands

Relative Strength IndexCalculation for RSIPython code for RSI

Calculation for RSI

Python code for RSI

Money Flow IndexPython code for MFI

Python code for MFI

Average True RangePython code for ATR

Python code for ATR

Force IndexCalculation for Force IndexPython code for Force Index

Calculation for Force Index

Python code for Force Index

Ease of MovementCalculation for EVMPython code for EVM

Calculation for EVM

Python code for EVM

What are technical indicators?

Technical Indicatorsdo not follow a general pattern, meaning, they behave differently with every security. What can be a good indicator for a particular security, might not hold the case for the other. Thus, using atechnical indicatorrequires jurisprudence coupled with good experience.

Algo Trading for Complete Beginners

Self-paced course

As these analyses can be done inPython, a snippet of code is also inserted along with the description of the indicators. Sample charts with examples are also appended for clarity. We have also previously covered the most popular blogs for trading, you can check it outTop Blogs on Python for Trading.

Are you interested in creating your ownPython trading botand delving into the exciting world of algorithmic trading? Check out this comprehensive video, on how to build, backtest, and go live with Algorithmic Trading using Python.

Why use Python technical indicators?

Technical indicators are a set of tools applied to a trading chart to help make the market analysis clearer for the traders.

For example, technical indicators confirm if the market is following a trend or if the market is in a range-bound situation.

Also, indicators can provide specific market information such as when an asset is overbought or oversold in a range, and due for a reversal.

We will use python to code these technical indicators. Python is used to calculate technical indicators because its simple syntax and ease of use make it very appealing.

Python can help you with obtaining historical data and performance check usingstock market data analysis. Python also has many readily available data manipulation libraries such asPandasandNumpyand data visualizations libraries such asMatplotlibandPlotly. Python also has a popular library for performing technical analysis, such asTA-lib, which is commonly used incourses for technical analysis.

Technical indicators for trading

Now, let us see the Python technical indicators used for trading. There are a lot of indicators that can be used, but we have shortlisted the ones most commonly used in the trading domain. Also, the indicators’ usage is shown with Python to make it convenient for the user.

Here is the list of Python technical indicators, which goes as follows:

Moving average

Bollinger Bands

Relative Strength Index

Money Flow Index

Average True Range

Force Index

Ease of Movement

Moving average

Moving average, also called Rolling average, is simply the mean or average of the specified data field for a given set of consecutive periods. As new data becomes available, the mean of the data is computed by dropping the oldest value and adding the latest one.

So, in essence, the mean or average is rolling along with the data, hence the name ‘Moving Average’.

Also, moving average is a technical indicator which is commonly used with time-series data to smoothen the short-term fluctuations and reduce the temporary variation in data.

There are three popular types of moving averages available to analyse the market data:

Simple Moving Average,

Exponential Moving Average, and

Weighted Moving Average.

Read more on Python for Trading

Python code for Moving Average

Let us see the working of the Moving average indicator with Python code:

Output:

The image above shows the plot of the close price, the simple moving average of the 50 day period and exponential moving average of the 200 day period.

Bollinger Bands

Bollinger band is a volatility or standard deviation based oscillator which comprises three components. The middle band is a moving average line and the other two bands are predetermined, usually two, standard deviations away from the moving average line.

As the volatility of the stock prices changes, the gap between the bands also changes. During more volatile markets the gap widens and amid low volatility conditions, the gap contracts.

Calculation for Bollinger Bands

Bollinger bands involve the following calculations:

Middle Band: 30 Day moving average

Upper Band: Middle Band  + 2 x 30 Day Moving Standard Deviation

Lower Band: Middle Band  – 2 x 30 Day Moving Standard Deviation

As with most technical indicators, values for the look-back period and the number of standard deviations can be modified to fit the characteristics of a particular asset or trading style.

Read more on Python for Trading

Python code for Bollinger Bands

Let us find out the Bollinger Bands with Python as shown below:

Output:

The image above shows the plot of Bollinger Bands with the plot of the close price of Google stock.

Algo Trading for Complete Beginners

Self-paced course

As depicted in the chart above, when the prices continually cross the upper band, the asset is usually in an overbought condition, conversely, when prices are regularly crossing the lower band, the asset is usually in an oversold condition.

Relative Strength Index

Relative strength index (RSI) is a momentum oscillator to indicate overbought and oversold conditions in the market. It oscillates between 0 and 100 and its values are below a certain level.

Usually, if the RSI line goes below 30, it indicates an oversold market whereas the RSI going above 70 indicates overbought conditions. Typically, a lookback period of 14 days is considered for its calculation and can be changed to fit the characteristics of a particular asset or trading style.

Calculation for RSI

Average gain   =  sum of gains in the last 14 days/14Average loss  =  sum of losses in the last 14 days/14Relative Strength (RS)  = Average Gain / Average LossRSI =  100 – 100 / (1+RS)

Python code for RSI

We can also calculate the RSI with the help of Python code. Let us see how.

Output: The following two graphs show the Apple stock's close price and RSI value.

In the output above, we have the close price of Apple over a period of time and theRSI indicatorshows a 14 days RSI plot.

Whenever the RSI shows the line going below 30, the RSI plot is indicating oversold conditions and above 70, the plot is indicating overbought conditions.

Money Flow Index

The Money Flow Index (MFI) is the momentum indicator that is used to measure the inflow and outflow of money over a particular time period.

Algo Trading for Complete Beginners

Self-paced course

MFI is calculated by accumulating the positive and negative Money Flow values and then it creates the money ratio.

Python code for MFI

Let us find out the calculation of the MFI indicator in Python with the codes below:

Output:

Read more on Python for Trading

The output shows the chart with the close price of the stock (Apple) and Money Flow Index (MFI) indicator’s result. You must see two observations in the output above:

Oversold levels occur below 20 and overbought levels usually occur above 80. These levels may change depending on market conditions. Level lines should cut across the highest peaks and the lowest troughs.

If the underlying price makes a new high or low that isn't confirmed by the MFI, this divergence can signal a price reversal.

But, it is also important to note that, oversold/overbought levels are generally not enough of the reasons to buy/sell. The trader must consider some other technical indicators as well to confirm the asset’s position in the market.

This fact holds true especially during the strong trends.

Average True Range

The Average True Range (ATR) is a technical indicator that measures the volatility of the financial market by decomposing the entire range of the price of a stock or asset for a particular period.

Python code for ATR

Let us see the ATR calculation in Python code below:

Output:

The above two graphs show the Apple stock's close price and ATR value.

The ATR is a moving average, generally using 14 days of the true ranges.

In the output above, you can see that the average true range indicator is the greatest of the following: current high less the current low; the absolute value of the current high less the previous close; and the absolute value of the current low less the previous close.

Force Index

The force index was created by Alexander Elder. The force index takes into account the direction of the stock price, the extent of the stock price movement, and the volume. Using these three elements it forms an oscillator that measures the buying and the selling pressure.

Each of these three factors plays an important role in the determination of the force index. For example, a big advance in prices, which is given by the extent of the price movement, shows a strong buying pressure. A big decline in heavy volume indicates strong selling pressure.

Calculation for Force Index

Example: Computing Force index(1) and Force index(15) period.

The Force index(1) = {Close (current period) - Close (prior period)} x Current period volume

The Force Index for the 15-day period is an exponential moving average of the 1-period Force Index.

Read more on Python for Trading

The force index uses price and volume to determine a trend and the strength of the trend. A shorter force index can be used to determine the short-term trend, while a longer force index, for example, a 100-day force index can be used to determine the long-term trend in prices.

A force index can also be used to identify corrections in a given trend. To do so, it can be used in conjunction with a trend following indicator. For example, one can use a 22-day EMA for trend and a 2-day force index to identify corrections in the trend.

We can also use the force index to spot the breakouts. The breakouts are usually confirmed by the volume and the force index takes both price and volume into account. Sudden spikes in the direction of the price moment can help confirm the breakout.

Python code for Force Index

Let us now see how using Python, we can calculate the Force Index over the period of 13 days.

In the Python code below, we have taken the example of Apple as the stock and we have used the Series, diff, and the join functions to compute the Force Index. The Series function is used to form a series, a one-dimensional array-like object containing an array of data.

The diff function computes the difference between the current data point and the data point “n” periods/days apart. The join function joins a given series with a specified series/dataframe.

Output:

Ease of Movement

Developed by Richard Arms, Ease of Movement Value (EMV) is an oscillator that attempts to quantify both price and volume into one quantity. As it takes into account both price and volume, it is useful when determining the strength of a trend.

When the EMV rises over zero it means the price is increasing with relative ease. Whereas the fall of EMV means the price is on an easy decline.

Calculation for EVM

To calculate the EMV we first calculate the distance moved.

Algo Trading for Complete Beginners

Self-paced course

It is given by:Distance moved = ((Current High + Current Low)/2 - (Prior High + Prior Low)/2)

We then compute the Box ratio which uses the volume and the high-low range:Box ratio = (Volume / 100,000,000) / (Current High – Current Low)

EMV = Distance moved / Box ratio

To compute the n-period EMV we take the n-period simple moving average of the 1-period EMV.

Ease of Movement (EMV) can be used to confirm a bullish or a bearish trend.

A sustained positive Ease of Movement together with a rising market confirms a bullish trend.

A negative Ease of Movement value with falling prices confirms abearish trend.

Apart from using it as a standalone indicator, Ease of Movement (EMV) is also used with other indicators in chart analysis.

Python code for EVM

Now, we will use the example of Apple to calculate the EMV over the period of 14 days with Python.

In the Python code below, we use the series, rolling mean, shift, and the join functions to compute the Ease of Movement (EMV) indicator.

The Series function is used to form a series, a one-dimensional array-like object containing an array of data. The rolling mean function takes a time series or a data frame along with the number of periods and computes the mean.

The shift function is used to fetch the previous day’s high and low prices. The join function joins a given series with a specified series/dataframe.

Output:

The above two graphs show the Apple stock's close price and EMV value.

You will find it very useful and knowledgeable to read through this curated compilation of some of our top blogs on:

Machine LearningSentiment TradingAlgorithmic TradingOptions TradingTechnical Analysis

Conclusion

Python technical indicators are quite useful for traders to predict future stock values. Every indicator is useful for a particular market condition. For example, the Average True Range (ATR) is most useful when the market is too volatile.

Hence, ATR helps measure volatility on the basis of which a trader can enter or exit the market.

Wondering how to use technical indicators to generate trading signals? You can learn all about in this course ontechnical indicators python. You will learn to identify trends in an underlying security price, how to implement strategies based on these indicators, live trade these strategies and analyse their performance. Check it out now!

File in the download:

Complete Python code - Python technical indicators

Login to Download

Note: The original post has been revamped on 8th June 2022 for accuracy, and recentness.

Disclaimer: All investments and trading in the stock market involve risk. Any decision to place trades in the financial markets, including trading in stock or options or other financial instruments is a personal decision that should only be made after thorough research, including a personal risk and financial assessment and the engagement of professional assistance to the extent you believe necessary. The trading strategies or related information mentioned in this article is for informational purposes only.

---

*Imported from QuantInsti Blog on 2026-04-27*
