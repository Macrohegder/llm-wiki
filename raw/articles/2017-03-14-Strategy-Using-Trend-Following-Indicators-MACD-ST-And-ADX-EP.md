---
title: "Strategy Using Trend-Following Indicators: MACD, ST And ADX [EPAT PROJECT]"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/strategy-using-trend-following-indicators-macd-st-adx/"
date: "2017-03-14"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Strategy Using Trend-Following Indicators: MACD, ST And ADX [EPAT PROJECT]

**来源**: [QuantInsti](https://blog.quantinsti.com/strategy-using-trend-following-indicators-macd-st-adx/)  
**日期**: 2017-03-14  
**作者**: QuantInsti

---

## 原文

Strategy Using Trend-Following Indicators: MACD, ST And ADX [EPAT PROJECT]

This article is the final project submitted by the author as a part of his coursework in Executive Programme in Algorithmic Trading (EPAT™) at QuantInsti®. Do check ourProjects pageand have a look at what our students are building.

About the Author

Gopal, a management professional, has over 2 decades of experience in IT industry with a strong Global Delivery background, with passion in Quantitative Finance and gadgets.  He is highly process driven with a focus on achieving quality using automation. He heads delivery at PreludeSys India Ltd.Gopalholds an MBA from Symbiosis Centre For Distance Learning. He has successfully completed the course work for theExecutive Programme in Algorithmic Trading(EPAT™) in November 2016.

‘Trend is a friend’ goes a famous saying.  According to the Pundits, the success rate in the stock market is 5%. Of course, everyone wants to be in that 5%! To be in that 5% bracket is difficult if not impossible. All we need is an appropriate strategy(ies). Even with a strategy in place, it is important to understand whether the market condition will help the strategy. The decisive factor to being a successful trader is being current in the market.

My strategy is based on training that I had a couple of years ago from a respectable and well known technical analyst.  I have used that strategy and enhanced it based on the feedback that I received from my mentor Mr. Abhishek Kulkarni.

Motivation for using this strategy

I have been following charts for a few years now. As part of my learning, I have used several technical and trend indicators. I am fascinated by how technical analysts use these indicators in response to the market.

As my strength is programming, I have used a strategy, which is not too heavy on concepts. During assignments stage, I have used R to implement thepairs trading strategy.

Details about the strategy

The strategy that I have arrived at works on trending markets - both bear and bull. It uses a couple of technical indicators to identify the momentum and trades both on the long and the short side of the market.

Thetrend following indicatorsthat I have used are Moving Average Convergence Divergence (MACD) indicator, a trend-following momentum indicator and Super Trend (ST) indicator, a trend following indicator.

A brief note on the use of MACD and ST as trend indicators

Moving Average Convergence Divergence (MACD)

MACD is calculated using two exponentialmoving average(EMA) - short term and long term. An exponential moving average of MACD is used as a signal line to indicate the upward or downward momentum.

There are two entry points to be considered while using MACD.  One, when the MACD line crosses the signal line.  Second, when MACD is in the positive territory - which implies that, the smaller moving average is above the chosen larger moving average.

SuperTrend (ST)

The Super Trend indicator, which is a trending indicator has been used to determine whether the price is in an upward or downward trend. If the price is above the indicator line then the price point acts as a point of support. If the price is below the indicator line, it acts as a point of resistance.

I have optimized the strategy by managing the position size through a weightage of 1 unit for MACD and 2 units for SuperTrend. I expect that the MACD will provide quick entry and exit positions.  When used with SuperTrend, it will provide more clarity to run the trend.

Choice of stocks

There is no stock-specific criterion for using this strategy.  However, for any strategy to work efficiently, liquid stocks are preferred. Hence, the focus of this strategy is on Nifty 50 stocks.

Data usage

I have backtested this strategy on a daily time frame working off the daily data downloaded from Yahoo.

I have tested my strategy from the year 2012 onwards.  Obviously, some of the stocks I have used did not have data from 2012.  That is a known caveat, with which I backtested my trend following indicators strategy.

I have used Python for implementing my strategy along with packages like Numpy, Panda, Matplotlib, TA-Lib.TA-Libhelps in calculating MACD with the necessary parameters.

As there is no readily available method to calculate SuperTrend price points, I have coded the method and used the same in the program.

When I presented this topic to my mentor Abhishek, he suggested I improvise the strategy by using the Average Directional Index (ADX) indicator.  ADX is another readily available method in TA-LIB package to determine the trend of the price.

The strategy to BUY/SELL based on MACD and ST will be done only when the stock is trending. Trending of stocks will be decided based on ADX. Any BUY/SELL decision will be made only when the ADX data is above the pre-determined threshold. The moment ADX moves below the threshold, all the open positions will be closed when the market opens the next day.

Implementation of the strategy

The Python packages that I have used in this strategy include:

I created a method to calculate the SuperTrend indicator.  One can optimize this further by passing the data in an array.  However, for simplicity purpose, I am passing each record to identify the upper band, lower band, and the supertrend.

If the period decided for backtesting is very much in the past, there is a chance that some stocks might not have been traded in the market during that time frame. This is a known caveat.

The following Python codes get the latest Nifty50 list from nseindia.com and convert the output into a data frame.

To set the dates for data retrieval and retrieve the historical data from yahoo finance:

After going through the data and analyzing the same, I discovered that the ‘Adjusted Close' data provided by yahoo is skewed when there is a corporate action on the stock.  For this, I have made a small adjustment programmatically. If there is a huge variance in the daily return - say the variance is less than 0.75 or above 1.50, then I update the 'Adjusted Close' data with 'Close' data.

The following Python codes get the technical indicators data into a data frame for further processing.

Though Average True Range (ATR) indicator is not used directly in the strategy, it is needed to calculate the SuperTrend. I have used the following code to get that into the data frame.

Now calculate SuperTrend and add that to the data frame.

To identify the crossover, I have prepared the data frame with previous periods data for each day's trading data - 2 periods data neededthe trend indicators,for MACD and ST to avoid back-testing bias. For ADX, previous day's data is enough.

To generate MACD and ST trading signals and add the signal to the data frame. (I have posted detailed inline comments, followed by the for loop code.)

ADX indicator provides an important data point for the strategy to determine whether the stock is trending. BUY or SELL will happen only when ADX is above the threshold. The moment ADX drops below the threshold all open positions will be closed.

When there is an MACD crossover or ST crossover, ADX is used to decide on trading the stock. Two indicators have been used in the strategy. One is a signal (macdsig/supersig) and the other one is a strategy (macdstr/superstr).

When there is a positive crossover of MACD / ST and ADX is trending, then the signal and strategy are set to '1'. When there is a negative crossover of MACD / ST and ADX is trending, then the signal and strategy are set to '-1'.

When there is no crossover, the signal is set to '0', but strategy variable is used to decide whether to continue the trade or close the trade (no matter buy or sell). This strategy variable is set to continue the same value from the previous day when the ADX is above the threshold (trending). If not trending, the strategy value is set to 0, thus giving a complete signal to close all the open trades.

To calculate the daily return for MACD crossover and ST crossover separately - Based on the analysis and to get near-to-accurate returns, I have used 'Adjusted Close' and 'Close' data alternatively based on the daily activity.

After all the data preparatory work is completed, the actual processing of the strategy and signal will be implemented.

I have included a column in the data frame for output with the commission, to help find the profit post-commission.  I have considered 1% for the first trade and 2% when there is a counter trade.

Here the processing of the signals and strategy is implemented.The trend indicators,MACD and ST are separately processed, but the same logic is used. While processing, separate columns in the data frame are used to calculate the accurate profit/loss.

The logic used is

When the signal and the strategy are same and positive, BUY.

If the running trade is SOLD, then cover and buy.

If not, just buy.

When the signal and strategy are same and negative, SELL.

If the running trade is BOUGHT, then sell and go short.

If not, just go short.

When the signal and strategy are same (0) and it is NO SIGNAL, Close the open positions.  If the running trade is BOUGHT, then sell and if it is SOLD, then cover.

All the other calculations are done at each row level and stored in additional columns in the data frame - Cumulative returns, Annualized returns, Annualized standard deviation, Annualized Sharpe ratio. The above data is used to calculateThe trend indicators,MACD and ST separately.

The combined calculation:

Print the same on the console or file depending on where it is routed.

Additionally, the trade success details are also calculated for further analysis of the strategy – CAGR, the Success ratio of trades, and Average profit to loss.

To print out the data:

To plot the chart using Matplotlib:

It took a lot of time to complete the strategy as (1) I was super busy at work (2) Had to undergo a cornea transplant surgery.

I was frequently in touch with my mentor Abhishek, sharing the work-in-progress code. He has been kind enough to give feedback regularly. The QuantInsti® team was encouraging and provided guidance with various sample projects.

I do not think this experience as a blog will be complete without showing the output.

Going through this project and coding this strategy was a great learning experience. Stackoverflow, Pandas documentation were the favorite websites that I was visiting for technical know how. I have tried to keep the code simple and straight. I have optimized the code and have improvised by reducing the looping of the data frame to the minimum. I have kept the code dynamic, so that any code written in between to include new columns in the data frame, will not affect the other parts of the program.

I am sure the Python Pundits can polish the code further. I appreciate your time reading this strategy. If any of you find a simpler way to do what I have done, please feel free to write to me.

Another project work by anEPATianon Pairs Trading that makes use of a simple mean reversion strategy on ETF pairs. The objective of this project is to see if arbitrage opportunity exists between the large and mid-cap financial ETFs.Click hereto read more.

Update:We have noticed that some users are facing challenges while downloading the market data from Yahoo and Google Finance platforms. In case you are looking for an alternative source for market data, you can use Quandl for the same.

Disclaimer:The information in this project is true and complete to the best of our Student’s knowledge. All recommendations are made without guarantee on the part of the student or QuantInsti®. The student and QuantInsti® disclaim any liability in connection with the use of this information.All content provided in this project is for informational purposes only and we do not guarantee that by using the guidance you will derive certain profit.

Files in the download:

Login to Download

---

*Imported from QuantInsti Blog on 2026-04-27*
