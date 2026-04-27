---
title: "How to Get Started with R quantmod Package?"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/a-guide-on-r-quantmod-package-how-to-get-started/"
date: "2015-10-12"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# How to Get Started with R quantmod Package?

**来源**: [QuantInsti](https://blog.quantinsti.com/a-guide-on-r-quantmod-package-how-to-get-started/)  
**日期**: 2015-10-12  
**作者**: QuantInsti

---

## 原文

A Guide On R Quantmod Package: How To Get Started?

“Thequantmodpackage forRis designed to assist the quantitative trader in the development, testing, and deployment of statistically based trading models.”

It is a rapid prototyping environment where enthusiasts can explore various technical indicators with minimum effort. It offers charting facilities that are not available elsewhere in R. Quantmod package makes modelling easier and analysis simple. This article is intended to present some functions of quantmod using sample market data. The features of quantmod are presented in three sections, downloading data, charting, technical indicators and other functions.

Without much ado, we will see the usage of quantmod package.

Downloading data

Once the quantmod package is installed and the library is loaded, run the following command to get the data of Apple Inc. stock into the R console.

getSymbols(‘AAPL’)

To see the starting point of the data, type the following command.

head(AAPL) # You should see the following result.

AAPL.Open AAPL.High AAPL.Low AAPL.Close AAPL.Volume AAPL.Adjusted

2007-01-03     86.29     86.58   81.90     83.80   309579900     11.19449

2007-01-04     84.05     85.95   83.82     85.66   211815100     11.44295

2007-01-05     85.77     86.20   84.40     85.05   208685400     11.36147

2007-01-08     85.96     86.53   85.28     85.47   199276700     11.41757

2007-01-09     86.45     92.98   85.15     92.57   837324600     12.36603

2007-01-10     94.75     97.80   93.45      97.00   738220000     12.95782

Visualize the charts

The beauty of quantmod lies in its ability to visualize the charts. Type the following command.

chartSeries(AAPL, TA=NULL) # this should produce the following chart.

As one can see, the x-axis shows the time period, while the y-axis shows price range for the AAPL stock. In the command above we set TA=”Null”. It means do not include any Technical Analysis parameter. The following command produces the same graph along with volume parameter.

barChart(AAPL)

The noting difference between this graph and the previous one is the representation of AAPL's volume. Rest of the syntax is meant to decorate the chart appearance.

We shall choose the closing price for reference and calculate various technical indicators based on it. Following command selects the closing price of Apple Inc.

Apple_closeprice = Cl(AAPL) # We assign the closing price to a new variable called Apple_closeprice.

plot(Apple_closeprice) # Plotting the close price

Plotting histogram is simple.

hist(AAPL[,4]) #This command plots the histogram of closing price of apple stock.

hist(NSEI[,4], main = "Apple Close") #The histogram of closing price of apple stock with the heading “Apple Close”

hist(NSEI[,4], main = "Apple Close", breaks =25) # Introducing more price ranges.

Technical indicators

chartSeries(AAPL)

addMACD() # adds moving average convergence divergence signals to the apple stock price

addBBands() # Adds Bollinger bands to the apple stock price.

addCCI() # Add Commodity channel index.

addADX() #Add Directional Movement Indicator

addCMF() #Add Chaiken Money Flow

Similarly, othertechnical indicatorscan be calculated. Following is the list of technical indicators that quantmod supports.

addCMO # Add Chaiken Money Flow

addDEMA # Add Double Exponential Moving Average

addDPO # Add Detrended Price Oscillator

addEMA # Add Exponential Moving Average

addEnvelope # Add Price Envelope

addEVWMA # Add Exponential Volume Weigthed Moving Average

addMACD # Add Moving Average Convergence Divergence

addMomentum # Add Momentum

addROC # Add Rate of Change

addRSI # Add Relative Strength Indicator

addSAR # Add Parabolic Stop and Reverse

addSMA # Add Simple Moving Average

addSMI # Add Stocastic Momentum Index

addTRIX # Add Triple Smoothed Exponential Oscillator

addVo # Add Volume

addWMA # Add Weighted Moving Average

We will have a look at the data handling features of quantmod. We saw earlier that the apple data downloaded has the following structure.

AAPL.Open AAPL.High AAPL.Low AAPL.Close AAPL.Volume AAPL.Adjusted

2007-01-03     86.29     86.58   81.90     83.80   309579900     11.19449

2007-01-04     84.05     85.95   83.82     85.66   211815100     11.44295

2007-01-05     85.77     86.20   84.40     85.05   208685400     11.36147

2007-01-08     85.96     86.53   85.28     85.47   199276700     11.41757

2007-01-09     86.45     92.98   85.15     92.57   837324600     12.36603

2007-01-10     94.75    97.80   93.45     97.00   738220000     12.95782

Useful functions

Quantmod provides functions to explore features of the data frame. The following command shows that the object type holding apple data is xts and zoo.

class(AAPL)

One would want to explore whether the data extracted contains the open price, volume etc. Have a look at the following commands.

is.OHLC(AAPL) # Checks whether the xts data object has the open,high, low and close price?

The output is TRUE implying that the data object contains open, high, low and close.

has.Vo(AAPL) # Checks whether the data object has volume

seriesHi(AAPL) # To check the highest point of price.

Lag(Cl(AAPL)) #One period lag of the closing price

Next(OpCl(AAPL)) #The next periods open to close - today!

AAPL ['2007'] #Fetches all Apple’s 2007 OHLC

AAPL ['2008::'] # Apple data, from 2008 onward

dailyReturn(AAPL) # Returns by day

weeklyReturn(AAPL) # Returns by week

monthlyReturn(AAPL) # month, indexed by yearmon  daily,weekly,monthly,quarterly, and yearly

allReturns(AAPL) # note the plural

Next Step

If you’re new to this and not able to grab all the technical aspects of this article, you may like to take a look at a few articles explaining basic concepts likedesigning a quant trading strategy in R. You can also take a look at a basicexample of trading strategy coded in R.

Disclaimer: All investments and trading in the stock market involve risk. Any decisions to place trades in the financial markets, including trading in stock or options or other financial instruments is a personal decision that should only be made after thorough research, including a personal risk and financial assessment and the engagement of professional assistance to the extent you believe necessary. The trading strategies or related information mentioned in this article is for informational purposes only.

---

*Imported from QuantInsti Blog on 2026-04-27*
