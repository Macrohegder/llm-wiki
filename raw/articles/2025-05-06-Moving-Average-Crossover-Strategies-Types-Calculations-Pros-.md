---
title: "Moving Average Crossover Strategies: Types, Calculations, Pros & Cons for Trading"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/moving-average-trading-strategies/"
date: "2025-05-06"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Moving Average Crossover Strategies: Types, Calculations, Pros & Cons for Trading

**来源**: [QuantInsti](https://blog.quantinsti.com/moving-average-trading-strategies/)  
**日期**: 2025-05-06  
**作者**: QuantInsti

---

## 原文

Moving Average Crossover Strategies

ByRekhit PachanekarandChainika Thakar

You might think, "What good are moving averages in the world of AI and LLMs?"

Well, moving averages serve as a foundation for many technical indicators and they can be used as features in ML models too.  The moving average helps traders identify trends that increase the number of favourable trades.

Prerequisites

Before you dive into this blog, it's important to build a foundation in Python programming and data visualisation, especially within the context of financial markets.

Begin withthe Basics of Python Programmingto get familiar with Python syntax, data types, and logic structures. Then, set up your environment for technical analysis by followingHow to Install TA-Lib in Python, a widely used library for financial indicators like moving averages.

To create dynamic visualisations, explorePlotly Python – An Interactive Data Visualizationand learn how to present technical indicators in an engaging and informative way.

To build these skills in a more structured, guided format, check out the following Quantra courses focused on Python basics:

Python for Trading: Basic– A free, beginner-friendly course to help you get started with Python in the context of trading.

These courses provide a solid foundation for interacting with financial datasets and using Python to build your own indicators and strategies.

This blog covers the following:

What is a moving average?

Calculation of a moving average indicator

Example of a moving average indicator

Lookback periods for calculating the moving average indicator

Types of moving averages

Moving average trading strategies

Advantages of using moving averages in trading

Disadvantages of using moving averages in trading

FAQsWhich moving average is best for trading?Does moving average trading provide good results?How are moving averages used?

Which moving average is best for trading?

Does moving average trading provide good results?

How are moving averages used?

What is a moving average?

Moving averages are the averages of a series of numeric values. They have a predefined length for the number of values to average. This set of values moves forward as more data is added over time.

Given a series of numbers and a fixed subset size, the first element of the moving average series is obtained by taking the average of the initial fixed subset of the number series.

The subset is then modified by shifting it forward by one value. In other words, as we get newer data, the first element of the subset is excluded and the most recent element is added, this keeps the length fixed.

Calculation of a moving average indicator

Let us see the example mentioned below which shows the calculation of simple moving averages. The average is calculated for five data points. You can call this the lookback period.

Number series

7  12  2  14  15  16  11  20  7

1st value of the MA series

(7 + 12 + 2 + 14 + 15) / 5 = 10

2nd value of the MA series

(12 + 2 + 14 + 15 + 16) / 5 = 11.8

3rd value of the MA series

(2 + 14 + 15 + 16 + 11) / 5 = 11.6

It can be seen that the subset for calculating averages moves forward by one data entry, consequently, the name moving average (also called running average or rolling average). A moving average series can be calculated for any time series.

You can use multiple moving averages as well. You might have heard of moving averages of 50 and 200 look back periods. Here, the one with shorter lookback period is considered faster moving average, while the moving average with the longer lookback period is considered slower moving average.

Depending on the trader’s preference, the lookback periods can be in minutes, hours etc.

Example of a moving average indicator

Let us now see the example of moving average trading with code as well as a chart showing 10 day, 20 day and 50 day moving average.

The chart above shows the closing price of Tesla (blue line), the 10 day moving average (orange line), the 20 day moving average (green line) and the 50 day moving average (red line). It can be observed that the 50 day moving average is the smoothest and the 10 day moving average has the maximum number of peaks and troughs or fluctuations. As the lookback period increases, the moving average line moves away from the price curve. The red line (10 day moving average) is closest to the blue line (price curve) and the purple line (50 day moving average) is farthest away.

Lookback periods for calculating a moving average

The most commonly used lookback periods for calculating a moving average in the moving average trading are 10, 20, 50, 100, and 200.

These lookback periods can be one minute, daily, weekly, etc., depending on the trader as to whether the trader wishes to go for a long term trading or a short term one.

Types of moving averages

There are many different types of moving averages depending on the computation of the averages. The five most commonly used types of moving averages are the simple (or arithmetic), the exponential, the weighted, the triangular and the variable moving average.

The significant difference between the different moving averages is the weight assigned to data points in the moving average period.

Simple moving averages apply equal weights to all data points. Exponential and weighted averages apply more weight to recent data points. Triangular averages apply more weight to data in the middle of the moving average period. The variable moving average changes the weight based on the volatility of prices.

Simple Moving Average (SMA)

A simple (or arithmetic) moving average is an arithmetic moving average calculated by adding the elements in a time series and dividing this total by the number of time periods. As the name suggests, the simple moving average is the simplest type of moving average. We saw this in the earlier example.

The formula for calculating the SMA is straightforward:

SMA = (Sum of data points in the moving average period)/(Total number of periods)

Weighted Moving Average (EMA and LWMA)

The weighted moving average refers to the moving averages where each data point in the moving average period is given a particular weightage while computing the average. The exponential moving average is a type of weighted moving average where the elements in the moving average period are assigned an exponentially increasing weightage.

The EMA is calculated as shown below:

Weighting multiplier = 2 / (moving average period +1)

EMA = (Closing price - EMA of previous day/bar) x multiplier) + EMA of previous day/bar

Rewritten as:

EMA = (Closing price) x multiplier + (EMA of previous day/bar) x (1 - multiplier)

A linearly weighted moving average (LWMA), also generally referred to as weighted moving average (WMA), is computed by assigning a linearly increasing weightage to the elements in the moving average period.

If the moving average period contains ten data entries, then the most recent element (the tenth element) will be multiplied by ten, the ninth element will be multiplied by nine and so on till the first element which will have a multiplier of one.

The sum of all these linearly weighted elements will then be added and divided by the sum of the multipliers. In the case of 10 elements the sum will be divided by 55 (n(n+1)/2). The chart shown below plots the SMA (orange line), EMA (green line) and LWMA (red line) for a 30 day period.

As can be seen in the chart above, like the exponential moving average, the weighted moving average is faster to respond to changes in the price curve than the simple moving average.

But it is slightly slower to react to fluctuations than the EMA.

The slow reaction to fluctuations is because LWMA lays slightly greater stress on the recent past data than the EMA. In the case of EMA, the weights for each new data point keep increasing in an exponential manner.

Mentioned below are the weightage given to elements when calculating the EMA and WMA for a 4 day period:

Elements

Most recent element:

2/(4+1) = 40%

4/10 = 40%

2nd most recent element:

40% x 60% = 24%

3/10 = 30%

3rd most recent element:

24% x 60% = 14.4%

2/10 = 20%

4th most recent element:

14.4% x 60% = 8.6%

1/10 = 10%

5th most recent element:

8.6% x 60% = 5.2%

0/10 = 0%

6th most recent element:

5.2% x 60% = 3.1%

0/10 = 0%

7th most recent element:

3.1% x 60% = 1.9%

0/10 = 0%

And so on…

Here’s an extract from John J. Murphy’s work, “Technical Analysis of the Financial Markets” published by the New York Institute of Finance in 1999. It goes as follows: “The exponentially smoothed moving average addresses both of the problems associated with the simple moving average. First, the exponentially smoothed average assigns a greater weight to the more recent data. Therefore, it is a weighted moving average.

But while it assigns lesser importance to past price data, it does include in its calculation all the data in the life of the instrument. In addition, the user is able to adjust the weighting to give greater or lesser weight to the most recent day's price, which is added to a percentage of the previous day's value. The sum of both percentage values adds up to 100.”

Triangular Moving Average (TMA)

The triangular moving average is a double smoothed curve, which also means that the data is averaged twice (by averaging the simple moving average). TMA is a type of weighted moving average where the weightage is applied in a triangular pattern. Follow the steps mentioned below to compute the TMA:

First, calculate the simple moving average (SMA):

SMA = (D1 + D2 + D3 + . . . . . . + Dn) / n

Next, calculate the average of the SMAs:

TMA = (SMA1 + SMA2 + SMA3 + . . . . . . + SMAn) / n

Consider the chart above that comprises of the daily closing price curve (blue line), the 30 day SMA (red line) and the 30 day TMA (green line). It can be observed that the TMA is much smoother than the SMA. The TMA moves in longer and steadier waves than the SMA.

The lag in TMA is greater than other moving averages, like the SMA and the EMA, because of the double averaging. It can be observed that the TMA takes longer to react to price fluctuations.

The trading signals generated by the TMA during a trending period will be farther away from the peak and trough of the period when compared to the ones generated by the SMA, hence lesser profits will be made by using the TMA.

However, during a consolidation period, the TMA will not produce as many trading signals as those generated by the SMA, which would avoid the trader from taking unnecessary positions reducing the transaction costs.

Moving average trading strategies

Let us now discuss some known moving average trading strategies. As you go through each moving average trading indicator, you will see how each holds relevance while trading.

Triple Moving Average Crossover Strategy

The triple moving average strategy involves plotting three different moving averages to generate buy and sell signals. This moving average strategy is better equipped at dealing with false trading signals than the dual moving average crossover system. By using three moving averages of different lookback periods, the trader can confirm whether the market has actually witnessed a change in trend or whether it is only resting momentarily before continuing in its previous state. The buy signal is generated early in the development of a trend and a sell signal is generated early when a trend ends.

The third moving average is used in combination with the other two moving averages to confirm or deny the signals they generate. This reduces the probability that the trader will act on false signals.

The shorter the moving average period, the more closely it follows the price curve. When security begins an uptrend, faster moving averages (short term) will begin rising much earlier than the slower moving averages (long term). Assume that a security has risen by the same amount each day for the last 60 trading days and then begins to decline by the same amount for the next 60 days. The 10 day moving average will start declining on the sixth trading day, the 20 day and 30 day moving averages will start their decline on the eleventh and the sixteenth day respectively.

The probability of a trend to persist is inversely related to the time that the trend has already persisted. Because of this reason, waiting to enter a trade for too long results in missing out on most of the gain, whereas entering a trade too early can mean entering on a false signal and having to exit the position at a loss.

To illustrate this moving average strategy we will use the 10 day, 20 day and 30 day simple moving averages as plotted in the chart below.

The duration and type of moving averages to be used depend on the time frames that the trader is looking to trade in. For shorter time frames (one hour bars or faster), the exponential moving average is preferred due to its tendency to follow the price curve closely (e.g. 4, 9, 18 EMA or 10, 25, 50 EMA).

For longer time frames (daily or weekly bars), traders prefer using simple moving averages (e.g. 5, 10, 20 SMA or 4, 10, 50 SMA). The moving average periods vary depending on the trader’s strategy and the security being traded.

Consider point ‘A’ on the chart above, the three moving averages change direction around this point.

The red line represents the fast moving average (10 day SMA), the green line represents the medium moving average (20 day SMA) and the purple line represents the slow moving average (30 day SMA).

A signal to sell is triggered when the fast moving average crosses below both the medium and the slow moving averages. This shows a short term shift in the trend, i.e. the average price over the last 10 days has fallen below the average price of the last 20 and 30 days.

The signal to sell is confirmed when the medium moving average crosses below the slow moving average, the shift in momentum is considered to be more significant when the medium (20 day) moving average crosses below the slow (30 day) moving average.

The triple moving average crossover system generates a signal to sell when the slow moving average is above the medium moving average and the medium moving average is above the fast moving average.

When the fast moving average goes above the medium moving average, the system exits its position. For this reason, unlike the dual moving average trading system, the triple moving average system is not always in the market. The system is out of the market when the relationship between the slow and medium moving averages do not match that between the medium and fast moving averages.

Let us create a triple moving average strategy for Apple Inc. with 5, 10, and 15 day simple moving average.

Rules for Triple Moving Average:

Buy when:

Fast moving average is higher the medium and slow moving average

Medium moving average is higher than slow moving average

Sell when:

Fast moving average is lower than slow and medium moving average

Medium moving average is lower than fast moving average

More aggressive traders would not wait for the confirmation of the trend and instead enter into a position based on the fast moving average crossing over the slow and medium moving averages.

One may also enter positions at different times, for example, the trader could take a certain number of long positions when the fast MA crosses above the medium MA, then take up the next set of long positions when the fast MA crosses above the slow MA and finally more long positions when the medium crosses over the slow MA. If at any time a reversal of trend is observed he may exit his position.

Moving Average Ribbon

The Moving Average Ribbon is an extended version of the moving average crossover system. This moving average strategy is created by placing a large number of moving averages onto the same chart (the chart shown below uses 8 simple moving averages). One must factor in the time horizons and investment objectives while selecting the lengths and type of moving averages.

When all the moving averages move in the same direction, the trend is said to be strong. Trading signals are generated in a similar manner to the triple moving average crossover system, the trader must decide the number of crossovers to trigger a buy or sell signal. Traders look to buy when the faster moving averages cross above the slower moving averages and look to sell when the faster moving averages cross below the slower moving averages.

Moving Average Convergence Divergence (MACD)

The MACD, short for moving average convergence divergence, is a trend following momentum indicator. It is a collection of three time series calculated as moving averages from historical price data, most often closing prices. The MACD line is the difference between a fast (short term) exponential moving average and a slow (long term) exponential moving average of the closing price of a particular security. The signal line is the exponential moving average of the MACD line. In this moving average strategy, the trader looks for crossovers between the MACD and the signal line.

The MACD strategy is denoted by the three parameters which define the strategy, i.e. the time periods of the three moving averages - MACD(a,b,c), where the MACD series is the difference between EMAs with time periods ‘a’ and ‘b’. The signal line, which is the EMA of the MACD series, has a time period of ‘c’.

The most commonly used MACD strategy uses the 12 day and 26 day EMA for the MACD series and a 9 day EMA for the signal series, represented by MACD(12, 26, 9). The chart shown below is plotted based on these input parameters

MACD line = 12 day EMA of  closing price - 26 day EMA of closing price Signal line = 9 day EMA of MACD line Histogram = MACD line - Signal line

The upper half of the chart contains the daily closing price (blue line), 12 day EMA (red line) and the 26 day EMA (green line).

The lower half of the chart consists of the MACD Series (blue line), which is calculated by subtracting the slow moving average (26 day EMA) from the fast moving average (12 day EMA).

The signal series (red line) is calculated by taking a 9 day EMA of the MACD series and lastly the MACD histogram (black vertical lines) is plotted by subtracting the signal series from the MACD Series.

There are many different interpretations of the MACD chart. The most commonly used signal trigger is when the MACD line crosses over the Signal line. When the MACD line crosses above the signal line, it is recommended to buy the underlying security and when the MACD line crosses below the signal line, a signal to sell is triggered. These events are taken as signs that the trend in the underlying security is about to escalate in the direction of the crossover. Another crossover that is taken into consideration by traders is called the zero crossover. This occurs when the slow and fast moving averages of the price curve crossover each other, or when the MACD series changes sign.

A change from positive to negative is considered to be a bearish sign while a change from negative to positive is considered as a bullish sign. The zero crossover provides confirmation about a change in trend but it is less reliable in triggering signals than the signal crossover.

Traders also monitor the divergence between the MACD line and the signal line, which can be observed through the histogram. When the histogram starts falling (moves towards the zero line), it indicates that the trend is weakening, this happens when the MACD and signal lines are converging.

Whereas, when the signal line and MACD line are diverging, or the histogram is rising (moves away from the zero line), it is an indication that the trend is growing stronger.

Advantages of using moving averages in trading

The known advantages of using moving averages in trading are:

You can trade on the basis of the trends in the market. With the analysis, you can find if it is an uptrend (the price moves above the moving average) or a downtrend (the price moves below the moving average).

With a lot of other factors in consideration such as the length of the trading period, moving average crossover, etc. you can find out the trading positions. You can also find entry points when the prices are strongly trending.

Can be used as support/resistance points.

The moving average trading helps to level the price data over a specified period by creating a constantly updated average price. Hence, the indicator is responsive to new and updated information which means better predictions.

Disadvantages of using moving averages in trading

Now we will discuss some disadvantages of moving average trading that you can weigh against the advantages for a successful trading experience.

Here are some disadvantages of moving average trading:

If the price action becomes fluctuating, the price may swing back and forth, generating multiple trend reversals or trade signals. When this occurs, it's best to step aside or utilise another indicator to help clarify the trend. The same thing can occur with moving average crossovers.

Moving averages work quite well in strong trending conditions but poorly in fluctuating or ranging conditions. Adjusting the time frame can help with this problem temporarily, though, at some point, these issues are likely to occur regardless of the time frame chosen for the moving averages.

Moving average trading does not work in sideways market. In case of a sideways market, the price of a security trades within a fairly stable range without forming any particular trends for some period of time. In a sideways market, the moving averages may generate false signals because of overlapping of price line.

You can avoid moving average trading during the situations mentioned above in which moving average trading is not as successful.

Conclusion

Moving average trading is the most sought after trading since the moving averages help the trader learn about the changing trends in the market and trade on the basis of the same.

While trading with moving averages, one must take into account a lot of market related factors such as any predicted fluctuation in price, a trend reversal etc. before taking the trading position. Being knowledgeable about the pros and cons of moving average trading also gives a reality check to the trader so that the predictions andtrading strategiesare based on the right analysis.

In case you want to find out more about moving average trading and wish to learn with a full-fledged course, do explore our course on Technical Analysis Indicators. This course will make you familiar with the moving average technical indicator while helping you compare other indicators simultaneously. Also, if you wish to go with the moving average trading, you will be able to learn more about each type of moving average and the strategies in depth.

Next Steps

Once you're comfortable with moving averages and how to code them, it’s time to explore broader trend-following and indicator-based trading systems.

Start withFive Indicators to Build Trend-Following Strategiesto explore tools like Bollinger Bands, RSI, MACD, and ADX. These indicators can be combined with moving averages to improve the precision of your entry and exit signals.

Deepen your understanding of trend strength and market breadth usingTrading Index (TRIN): Formula, Calculation & Strategy in Pythonand learn how to fine-tune and evaluate your strategies inHow to Optimise a Trading Strategy Based on Indicators.

For those seeking advanced, structured learning, explore these Quantra courses:

Technical Analysis Indicators and Strategies in Python– Learn to build, combine, and backtest technical indicators, including moving average crossovers.

Backtesting Trading Strategies– Master the essentials of validating your trading models using historical data.

Position Sizing Strategies – Learn to manage risk effectively with sizing methods tied to volatility and capital exposure.

Finally, if you're serious about a career in quantitative or algorithmic trading, consider enrolling in thebest algorithmic trading course, the industry-leading Executive Programme in Algorithmic Trading (EPAT).

File in the download:

Moving Average Crossover Strategies - Python Notebook

Login to Download

Note: The original post has been revamped on 06thMay 2025 for recentness, and accuracy.

Disclaimer: All investments and trading in the stock market involve risk. Any decision to place trades in the financial markets, including trading in stock or options or other financial instruments is a personal decision that should only be made after thorough research, including a personal risk and financial assessment and the engagement of professional assistance to the extent you believe necessary. The trading strategies or related information mentioned in this article is for informational purposes only.

---

*Imported from QuantInsti Blog on 2026-04-27*
