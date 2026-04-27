---
title: "10 ways your Trading Strategy can fail"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/ways-trading-strategy-fail/"
date: "2020-12-14"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# 10 ways your Trading Strategy can fail

**来源**: [QuantInsti](https://blog.quantinsti.com/ways-trading-strategy-fail/)  
**日期**: 2020-12-14  
**作者**: QuantInsti

---

## 原文

10 ways your Trading Strategy can fail

BySunil Guglani

Algorithmic trading tries to eliminate emotions when we trade. We come up withtrading strategiesthat set rules to buy and sell assets and test them thoroughly before deploying . However, there are some common errors that we make during the process. Ignoring them can cause our strategies to fail miserably.

Together this article covers ten commonly encountered ways in which we make mistakes through a series of examples/quizzes. The examples are based on various aspects of algo trading like look-ahead bias, overfitting, miscalculation of performance parameters, etc.

In this article, we cover the following:

Quiz 1-2

Quiz 3-4

Quiz 5

Quiz 6

Quiz 7

Quiz 8

Mistake 9

Mistake 10

The link for the complete blog is present in a Google Colab format towards the end of the blog, in case you wish to try it out yourself.

Quiz 1-2

Below is a trading strategy that has been tested on historical data. Is there any logical/technical error in it?

If so, what is it?

(Period: 1-Jan-2019 to 28-Jun-2019, Interval: 1 minute, Script: BANKNIFTY)

Idea behind the strategy

if (sma_short/sma_long)>long_ratio then buy at the opening and sell at the closing of the next minute

if (sma_short/sma_long)<short_ratio then short at the opening and buy at the closing of the next minute

Note: For demonstration purposes, returns are only calculated in percentage, without accounting for the minimum tradeable units of the instrument.

Sum of returns in % 187.41
Average returns per transaction in % 0.24
Max loss for a transaction -0.58
Max returns for a transaction 2.96
Total transactions count 772
Losing transaction count 31
Winning transaction count 741
Win/Lose ratio  24.0 2

Our backtesting results have the below characteristics

The Win/Lose ratio is greater than 23.9. It is considered to be high.

Average returns per transaction are mostly low and positive. There are a high number of transactions.

The Sum of returns in % calculated is high.

The transaction cost which is usually significant has not been included.

Since we have worked with minutely data, we assume that all our orders would be market orders. Hence we need to consider the effect of slippages.

We have not accounted for the bid-ask spread when orders get filled. Therefore we will try to forecast slippages(bid-ask spread). We now include it and assume it to be 0.00001% of the price of the instrument.(value arbitrarily selected for the sake of demonstration). Volume of the instrument is negatively correlated with the bid-ask spread.Therefore we will consider Volume also as a factor to calculate slippages.

We have not considered transaction costs. We consider it to be 0.00001% of the transaction value by accounting for factors like exchange fees, broker fees, taxes, etc.

For those looking to dive deeper intobacktesting trading strategies, our course provides detailed instruction on handling real market data, slippages, and transaction costs, enabling you to build and optimize robust strategies. Enroll now to enhance your backtesting skills.

We now incorporate the above mentioned factors and modify our code as shown below.

Modified code

Sum of returns in % 70.81
Average returns per transaction in % 0.09
Max loss for a transaction -0.72
Max returns for a transaction 2.81
Total transactions count 772
Losing transaction count 31
Winning transaction count 741
Win/Lose ratio  4.0 2

Observations after incorporating the changes

The Sum of returns in % has reduced from +187% to +70%.

The Win/Lose ratio has reduced from 29 to nearly 4.02.

The performance of the strategy has reduced across all the parameters.

Don't be surprised!

This is often the case with backtesting strategies which are cost sensitive. Hence, always include additional costs before reaching a conclusion.

Quiz 3-4

Below is a trading strategy that has been tested on historical data. Is there any logical/technical error in it?

If so, what is it?

(Period: 01-Jan-2008 to 31-Aug-2020, Interval: 1 day, Script: NIFTY)

Here are the key features of a strategy we have tested.

Refer below to view the transactions that occurred on this Short only strategy

Returns are calculated as (sell_price-buy_price)*100/sell_price

Assumptions

Assumption 1.: minimum number of tradeable units is 1.

Assumption 2.: The returns are expected to be reinvested.

Assumption 3.: Slippages are nil and transaction cost is 0.

Observations and Correction

The above calculation does not consider the previous returns in reinvestment.

The above calculation calculates returns by considering, the units can be bought in fractions. This is not true for all instruments.

After incorporating the following

Investments based on whole units

Returns are calculated on Ending Capital

The backtest results are

Observations after incorporating the changes

There is a significant difference in the Absolute Returns and pct returns when minimum tradeable units and reinvestment are taken into account.

It is easy to overlook these while backtesting.

Quiz 5

Below is a trading strategy that has been tested on historical data. Is there any logical/technical error in it?

If so, what is it?

(Period: 15-Jun-2019 to 28-Jun-2019, Interval: 1 minute, Script: BANKNIFTY)

Idea behind the strategy

Consider a scenario where the strategy is predicting direction of next minute using a ML model. The backtest of the strategy is as follows:

Accuracy: 1.00 (+/- 0.00)

Observation and Correction

"By partitioning the available data into two sets, we drastically reduce the number of samples which can be used for learning the model, and the results can depend on a particular random choice for the pair of (train, validation) sets.A solution to this problem is a procedure called cross-validation (CV for short). A test set should still be held out for final evaluation, but the validation set is no longer needed when doing CV.In the basic approach, called k-fold CV, the training set is split into k smaller sets (other approaches are described below, but generally follow the same principles). The following procedure is followed for each of the k “folds”.A model is trained using of the folds as training data; the resulting model is validated on the remaining part of the data (i.e., it is used as a test set to compute a performance measure such as accuracy)."

(Reference:Scikit)

Modified Code

We now incorporate the above mentioned factors and modify our code as shown below.

array([0.50996016, 0.5059761 , 0.5059761 , 0.5059761 , 0.50730412])

Accuracy after: 0.51 (+/- 0.00)

Observations after incorporating the changes

The accuracy of the model was 100% before, but after verifying through cross validation, it reduced to almost 51%.

Quiz 6

Below is a trading strategy that has been tested on historical data. Is there any logical/technical error in it?

If so, what is it?

(Period: last 5 years, Interval: 1 day, Script: AAPL(Apple))

Idea behind the strategy

if sma_short>sma_long then buy in the opening of the market and sell at the closing of the market of the same day.

Total percentage returns are:  166.26

Observations and Corrections

sma_short and sma_long are being calculated using the Close price of the day. And they are using current day's close. Whereas we are taking buy position in current day's opening.

At the opening of the day the algo wouldn't know the close of the day. The algo should have taken previous day's sma_short and sma_long.

This is very common mistake by algo traders. That is why we get different results in real trading as compared to backtesting.

This is also termed asLOOK AHEAD BIAS.

Modified Code/Logic

Total percentage returns are:  74.32000000000001

Observations after incorporating the changes

The percentage returns have reduced significantly after making the correction in the code.

Quiz 7

Below is a trading strategy that has been tested on historical data. Is there any logical/technical error in it?

If so, what is it?

(Period: last 10 years, Interval: 1 day, Script: All constituents of NIFTY50)

Idea behind the strategy

This logic is applicable for all the constituents of NIFTY50:

This ismean reversion tradinglogic with assumption that NIFTY50 are quality stocks. On every dip they can be bought, and every rise they will be squared off. The logic is based on using Bollinger band indicator for calculations.

Long Entry Criteria: if ((sma-bb_width std)>Close_price) then take long position*

Long Exit Criteria: exit the long postion when ((sma+bb_width std)<Close_price)*

Definition of the parameters

bb_width is the number of std distance from sma.

(sma-bb_width std) becomes the lower level*

(sma+bb_width std) becomes the upper level*

[*********************100%***********************]  1 of 1 completed
ADANIPORTS.NS      116.92
[*********************100%***********************]  1 of 1 completed
ASIANPAINT.NS      135.63
[*********************100%***********************]  1 of 1 completed
AXISBANK.NS      79.37
[*********************100%***********************]  1 of 1 completed
BAJAJ-AUTO.NS      115.91
[*********************100%***********************]  1 of 1 completed
BAJFINANCE.NS      154.49
[*********************100%***********************]  1 of 1 completed
BAJAJFINSV.NS      103.56
[*********************100%***********************]  1 of 1 completed
BPCL.NS      119.7
[*********************100%***********************]  1 of 1 completed
BHARTIARTL.NS      50.31
[*********************100%***********************]  1 of 1 completed
BRITANNIA.NS      79.0
[*********************100%***********************]  1 of 1 completed
CIPLA.NS      65.09
[*********************100%***********************]  1 of 1 completed
COALINDIA.NS      -28.4
[*********************100%***********************]  1 of 1 completed
DIVISLAB.NS      110.52
[*********************100%***********************]  1 of 1 completed
DRREDDY.NS      90.94
[*********************100%***********************]  1 of 1 completed
EICHERMOT.NS      84.07
[*********************100%***********************]  1 of 1 completed
GAIL.NS      -9.43
[*********************100%***********************]  1 of 1 completed
GRASIM.NS      40.4
[*********************100%***********************]  1 of 1 completed
HCLTECH.NS      124.44
[*********************100%***********************]  1 of 1 completed
HDFCBANK.NS      88.0
[*********************100%***********************]  1 of 1 completed
HDFCLIFE.NS      8.27
[*********************100%***********************]  1 of 1 completed
HEROMOTOCO.NS      45.15
[*********************100%***********************]  1 of 1 completed
HINDALCO.NS      63.03
[*********************100%***********************]  1 of 1 completed
HINDUNILVR.NS      94.55
[*********************100%***********************]  1 of 1 completed
HDFC.NS      80.14
[*********************100%***********************]  1 of 1 completed
ICICIBANK.NS      127.03
[*********************100%***********************]  1 of 1 completed
ITC.NS      97.53
[*********************100%***********************]  1 of 1 completed
IOC.NS      39.71
[*********************100%***********************]  1 of 1 completed
INDUSINDBK.NS      56.45
[*********************100%***********************]  1 of 1 completed
INFY.NS      54.26
[*********************100%***********************]  1 of 1 completed
JSWSTEEL.NS      124.39
[*********************100%***********************]  1 of 1 completed
KOTAKBANK.NS      165.26
[*********************100%***********************]  1 of 1 completed
LT.NS      25.05
[*********************100%***********************]  1 of 1 completed
M&M.NS      50.65
[*********************100%***********************]  1 of 1 completed
MARUTI.NS      37.22
[*********************100%***********************]  1 of 1 completed
NTPC.NS      3.16
[*********************100%***********************]  1 of 1 completed
NESTLEIND.NS      152.55
[*********************100%***********************]  1 of 1 completed
ONGC.NS      -5.96
[*********************100%***********************]  1 of 1 completed
POWERGRID.NS      60.58
[*********************100%***********************]  1 of 1 completed
RELIANCE.NS      64.54
[*********************100%***********************]  1 of 1 completed
SBILIFE.NS      25.99
[*********************100%***********************]  1 of 1 completed
SHREECEM.NS      127.22
[*********************100%***********************]  1 of 1 completed
SBIN.NS      121.19
[*********************100%***********************]  1 of 1 completed
SUNPHARMA.NS      101.83
[*********************100%***********************]  1 of 1 completed
TCS.NS      148.12
[*********************100%***********************]  1 of 1 completed
TATAMOTORS.NS      31.6
[*********************100%***********************]  1 of 1 completed
TATASTEEL.NS      -2.09
[*********************100%***********************]  1 of 1 completed
TECHM.NS      101.33
[*********************100%***********************]  1 of 1 completed
TITAN.NS      142.86
[*********************100%***********************]  1 of 1 completed
UPL.NS      136.17
[*********************100%***********************]  1 of 1 completed
ULTRACEMCO.NS      98.88
[*********************100%***********************]  1 of 1 completed

WIPRO.NS      53.01

**********************CONSOLIDATED DATA**********************
total_returns:     3950.1899999999996
tot_trx_count:     683
avg returns per transaction:     5.78

Observations and Corrections

As per the logic, the algorithm will run on NIFTY50 scripts. And it is tested on current list of NIFTY50 constituents.

Whereas NIFTY50 index has regular addition and deletion in the constituents. To understand the performance of the algorithm better removed/delisted scripts needs to be considered.

This is a common mistake by algo traders. This error is termed as "survivorship bias". If our data is biased (by not including companies that are non-existent due to mergers & acquisitions, delisting, bankruptcies, etc.) then backtesting results will be unreliable.

We will now test the algorirthm on few scripts which were removed from NIFTY 50 index in the recent past.

Modified Code/Logic

[*********************100%***********************]  1 of 1 completed
DLF.NS      60.04
[*********************100%***********************]  1 of 1 completed
SUZLON.NS      -60.41
[*********************100%***********************]  1 of 1 completed
RCOM.NS      -93.82
[*********************100%***********************]  1 of 1 completed
MMTC.NS      -78.29
[*********************100%***********************]  1 of 1 completed
MOSERBAER.NS      0.0
[*********************100%***********************]  1 of 1 completed
ABAN.NS      -72.45
[*********************100%***********************]  1 of 1 completed
HDIL.NS      -79.73
[*********************100%***********************]  1 of 1 completed

Failed download:
- LANCORHOL.NS: No data found, symbol may be delisted
LANCORHOL.NS      0.0
[*********************100%***********************]  1 of 1 completed
JAICORPLTD.NS      11.02
[*********************100%***********************]  1 of 1 completed
UNITECH.NS      -97.22

**********************CONSOLIDATED DATA**********************
total_returns:     -410.86
tot_trx_count:     29
avg returns per transaction:     -14.17

Observations after incorporating the changes

The total_returns and average returns per transaction have reduced significantly after making the correction in the code.

Quiz 8

Below is a trading strategy that has been tested on historical data. Is there any logical/technical error in it?

If so, what is it?

(Period: last 10 years, Interval: 1 day, Script: All constituents of NIFTY50)

Idea behind the strategy

This is strategy is based on momentum logic by using Heikin Ashi candles

Long Entry Criteria : (Current candle and previous candle is green) and (last two candles dont have lower wick)

Long Exit Criteria: (Current candle and previous candle is red)

Short Entry Criteria : (Current candle and previous candle is red) and (last two candles dont have upper wick)

Short Exit Criteria : (Current candle and previous candle is green)

Assumption : There were no changes in the NIFTY50 index constituents within the testing period

[*********************100%***********************]  1 of 1 completed
ADANIPORTS.NS      90.6
[*********************100%***********************]  1 of 1 completed
ASIANPAINT.NS      136.18
[*********************100%***********************]  1 of 1 completed
AXISBANK.NS      48.25
[*********************100%***********************]  1 of 1 completed
BAJAJ-AUTO.NS      -4.88
[*********************100%***********************]  1 of 1 completed
BAJFINANCE.NS      239.41
[*********************100%***********************]  1 of 1 completed
BAJAJFINSV.NS      246.14
[*********************100%***********************]  1 of 1 completed
BPCL.NS      185.62
[*********************100%***********************]  1 of 1 completed
BHARTIARTL.NS      56.11
[*********************100%***********************]  1 of 1 completed
BRITANNIA.NS      152.19
[*********************100%***********************]  1 of 1 completed
CIPLA.NS      9.49
[*********************100%***********************]  1 of 1 completed
COALINDIA.NS      55.52
[*********************100%***********************]  1 of 1 completed
DIVISLAB.NS      99.99
[*********************100%***********************]  1 of 1 completed
DRREDDY.NS      22.99
[*********************100%***********************]  1 of 1 completed
EICHERMOT.NS      118.89
[*********************100%***********************]  1 of 1 completed
GAIL.NS      30.42
[*********************100%***********************]  1 of 1 completed
GRASIM.NS      26.7
[*********************100%***********************]  1 of 1 completed
HCLTECH.NS      82.47
[*********************100%***********************]  1 of 1 completed
HDFCBANK.NS      67.14
[*********************100%***********************]  1 of 1 completed
HDFCLIFE.NS      9.0
[*********************100%***********************]  1 of 1 completed
HEROMOTOCO.NS      6.52
[*********************100%***********************]  1 of 1 completed
HINDALCO.NS      47.57
[*********************100%***********************]  1 of 1 completed
HINDUNILVR.NS      108.26
[*********************100%***********************]  1 of 1 completed
HDFC.NS      35.84
[*********************100%***********************]  1 of 1 completed
ICICIBANK.NS      43.77
[*********************100%***********************]  1 of 1 completed
ITC.NS      44.63
[*********************100%***********************]  1 of 1 completed
IOC.NS      8.03
[*********************100%***********************]  1 of 1 completed
INDUSINDBK.NS      15.41
[*********************100%***********************]  1 of 1 completed
INFY.NS      81.48
[*********************100%***********************]  1 of 1 completed
JSWSTEEL.NS      161.82
[*********************100%***********************]  1 of 1 completed
KOTAKBANK.NS      118.92
[*********************100%***********************]  1 of 1 completed
LT.NS      92.08
[*********************100%***********************]  1 of 1 completed
M&M.NS      6.78
[*********************100%***********************]  1 of 1 completed
MARUTI.NS      86.9
[*********************100%***********************]  1 of 1 completed
NTPC.NS      83.01
[*********************100%***********************]  1 of 1 completed
NESTLEIND.NS      101.06
[*********************100%***********************]  1 of 1 completed
ONGC.NS      133.02
[*********************100%***********************]  1 of 1 completed
POWERGRID.NS      -7.81
[*********************100%***********************]  1 of 1 completed
RELIANCE.NS      44.67
[*********************100%***********************]  1 of 1 completed
SBILIFE.NS      -5.24
[*********************100%***********************]  1 of 1 completed
SHREECEM.NS      179.74
[*********************100%***********************]  1 of 1 completed
SBIN.NS      2.54
[*********************100%***********************]  1 of 1 completed
SUNPHARMA.NS      0.99
[*********************100%***********************]  1 of 1 completed
TCS.NS      86.24
[*********************100%***********************]  1 of 1 completed
TATAMOTORS.NS      116.43
[*********************100%***********************]  1 of 1 completed
TATASTEEL.NS      31.09
[*********************100%***********************]  1 of 1 completed
TECHM.NS      98.37
[*********************100%***********************]  1 of 1 completed
TITAN.NS      102.53
[*********************100%***********************]  1 of 1 completed
UPL.NS      69.46
[*********************100%***********************]  1 of 1 completed
ULTRACEMCO.NS      98.67
[*********************100%***********************]  1 of 1 completed
WIPRO.NS      38.97
[*********************100%***********************]  1 of 1 completed
DLF.NS      17.99
[*********************100%***********************]  1 of 1 completed
SUZLON.NS      259.86
[*********************100%***********************]  1 of 1 completed
RCOM.NS      692.95
[*********************100%***********************]  1 of 1 completed
MMTC.NS      417.74
[*********************100%***********************]  1 of 1 completed
MOSERBAER.NS      0.0
[*********************100%***********************]  1 of 1 completed
ABAN.NS      395.31
[*********************100%***********************]  1 of 1 completed
HDIL.NS      363.58
[*********************100%***********************]  1 of 1 completed
JAICORPLTD.NS      21.09
[*********************100%***********************]  1 of 1 completed
UNITECH.NS      490.94

**********************CONSOLIDATED DATA**********************
total_returns:     6363.4400000000005
tot_trx_count:     2046
avg returns per transaction:     3.11

Observations and Corrections

If we look at the method to derive HA candles, they are nowhere same as the actual actual ohlc of the normalcandlestick. The ohlc of HA candles are derived using last two candles of normal candlesticks. In other words the price series is smoothened using HA candles. but it doesnt exactly match with the actual price series.

Therefore it is not correct to use ohlc of HA for taking the trade positions. Similar issue is with few other charts like Kagi and Renko.

We will now test the algorirthm using the close price of the normal candle.

Modified Code/Logic

[*********************100%***********************]  1 of 1 completed
ADANIPORTS.NS      26.92
[*********************100%***********************]  1 of 1 completed
ASIANPAINT.NS      112.26
[*********************100%***********************]  1 of 1 completed
AXISBANK.NS      50.76
[*********************100%***********************]  1 of 1 completed
BAJAJ-AUTO.NS      -11.1
[*********************100%***********************]  1 of 1 completed
BAJFINANCE.NS      240.83
[*********************100%***********************]  1 of 1 completed
BAJAJFINSV.NS      157.16
[*********************100%***********************]  1 of 1 completed
BPCL.NS      164.16
[*********************100%***********************]  1 of 1 completed
BHARTIARTL.NS      34.61
[*********************100%***********************]  1 of 1 completed
BRITANNIA.NS      127.12
[*********************100%***********************]  1 of 1 completed
CIPLA.NS      5.25
[*********************100%***********************]  1 of 1 completed
COALINDIA.NS      28.22
[*********************100%***********************]  1 of 1 completed
DIVISLAB.NS      120.58
[*********************100%***********************]  1 of 1 completed
DRREDDY.NS      14.0
[*********************100%***********************]  1 of 1 completed
EICHERMOT.NS      85.79
[*********************100%***********************]  1 of 1 completed
GAIL.NS      20.58
[*********************100%***********************]  1 of 1 completed
GRASIM.NS      18.74
[*********************100%***********************]  1 of 1 completed
HCLTECH.NS      58.67
[*********************100%***********************]  1 of 1 completed
HDFCBANK.NS      47.68
[*********************100%***********************]  1 of 1 completed
HDFCLIFE.NS      1.21
[*********************100%***********************]  1 of 1 completed
HEROMOTOCO.NS      -9.66
[*********************100%***********************]  1 of 1 completed
HINDALCO.NS      60.85
[*********************100%***********************]  1 of 1 completed
HINDUNILVR.NS      64.7
[*********************100%***********************]  1 of 1 completed
HDFC.NS      33.27
[*********************100%***********************]  1 of 1 completed
ICICIBANK.NS      86.76
[*********************100%***********************]  1 of 1 completed
ITC.NS      42.14
[*********************100%***********************]  1 of 1 completed
IOC.NS      10.3
[*********************100%***********************]  1 of 1 completed
INDUSINDBK.NS      5.56
[*********************100%***********************]  1 of 1 completed
INFY.NS      57.15
[*********************100%***********************]  1 of 1 completed
JSWSTEEL.NS      116.84
[*********************100%***********************]  1 of 1 completed
KOTAKBANK.NS      119.89
[*********************100%***********************]  1 of 1 completed
LT.NS      76.64
[*********************100%***********************]  1 of 1 completed
M&M.NS      8.48
[*********************100%***********************]  1 of 1 completed
MARUTI.NS      74.97
[*********************100%***********************]  1 of 1 completed
NTPC.NS      79.83
[*********************100%***********************]  1 of 1 completed
NESTLEIND.NS      77.82
[*********************100%***********************]  1 of 1 completed
ONGC.NS      72.84
[*********************100%***********************]  1 of 1 completed
POWERGRID.NS      -8.71
[*********************100%***********************]  1 of 1 completed
RELIANCE.NS      27.15
[*********************100%***********************]  1 of 1 completed
SBILIFE.NS      -3.83
[*********************100%***********************]  1 of 1 completed
SHREECEM.NS      166.49
[*********************100%***********************]  1 of 1 completed
SBIN.NS      -1.36
[*********************100%***********************]  1 of 1 completed
SUNPHARMA.NS      8.34
[*********************100%***********************]  1 of 1 completed
TCS.NS      98.93
[*********************100%***********************]  1 of 1 completed
TATAMOTORS.NS      75.38
[*********************100%***********************]  1 of 1 completed
TATASTEEL.NS      4.36
[*********************100%***********************]  1 of 1 completed
TECHM.NS      64.16
[*********************100%***********************]  1 of 1 completed
TITAN.NS      117.78
[*********************100%***********************]  1 of 1 completed
UPL.NS      51.98
[*********************100%***********************]  1 of 1 completed
ULTRACEMCO.NS      57.4
[*********************100%***********************]  1 of 1 completed
WIPRO.NS      35.72
[*********************100%***********************]  1 of 1 completed
DLF.NS      10.26
[*********************100%***********************]  1 of 1 completed
SUZLON.NS      254.99
[*********************100%***********************]  1 of 1 completed
RCOM.NS      672.45
[*********************100%***********************]  1 of 1 completed
MMTC.NS      397.08
[*********************100%***********************]  1 of 1 completed
MOSERBAER.NS      0.0
[*********************100%***********************]  1 of 1 completed
ABAN.NS      379.98
[*********************100%***********************]  1 of 1 completed
HDIL.NS      324.72
[*********************100%***********************]  1 of 1 completed
JAICORPLTD.NS      20.94
[*********************100%***********************]  1 of 1 completed
UNITECH.NS      436.89

**********************CONSOLIDATED DATA**********************
total_returns:     5472.920000000001
tot_trx_count:     1933
avg returns per transaction:     2.83

Observations after incorporating the changes

The total_returns and avg returns per transaction have reduced significantly after making the correction in the code.

Mistake 9

Interfering with the trading system or parameters of the algo.

Unlike the above mentioned scenarios, this is not a quiz. However this is a very common mistake.

If we have gone through all the steps of the algorithmic trading cycle thoroughly and tested for all the possible errors that could lead to system failure, then it is prudent to trust the algorithm and not adjust the working of the algorithm.

Steps or phases in the algorithmic trading process are as follows:

Formulate the Trading Concept/Logic

Filtering criteria to choose the scripts

Verification of Logic (at High Level)

Optimization of Parameters/retrain the model

Development and Backtesting of the algorithm

Paper Trading or Forward Testing or Simulation Trading in the real environment

Deployment in the real environment

Periodically (maybe monthly basis) go back to step 4 (iteration)

Periodically (in the longer interval maybe yearly) go back to step 1 to verify the base logic and check any scope of improvements

If the algorithmic trading stages mentioned above are followed properly and the potential mistakes or errors are cross-checked to the satisfactory level, then it is not recommended to alter the algo trading setup unless you discover any potential error within the functional/technical/process domain.

We will get an opportunity to make changes because Algo trading cycle has the step to optimize the parameters and verify/update the base logic in the periodic basis. :)

Mistake 10

Concept Drift - Not retraining/reverifying the model regularly

Consider a scenario where you have developed a Machine Learning prediction model to predict the direction of the instrument. It had a fantastic performance in train/test datasets using the cross-validation method.

And in a live trading environment too, the performance was the same as in the test dataset. But after 3 months, you observed that the accuracy of the prediction is not as accurate as it used to be initially.

What could be possible factors behind this?

Have you considered the environmental changes that can impact the relationship between the labels and the target variable of your model?

Over a period of time, the weightage and importance of the labels to predict the target variable will change.

To resolve this issue

We may require to retrain the model with the new dataset. The new dataset may require to cut down the older period data and include the latest and more relevant data.

It may also be required to rebuild the model with more relevant labels with correct weightage and importance.

This phenomenon is termed as "Concept Drift" it is also interchangeably called "Model Drift".

Please note this issue is not limited to Machine Learning model, any mathematical/statistical model can have this issue. But the method to resolve the issue is the same.

Not mitigating this issue may lead to failure of the trading/prediction model in a big manner.

Summary

We have seen how minor looking errors can impact the performance of the algorithmic trading strategy in the backtesting trading environment. We have also seen, what are the preventive steps we can take to avoid those errors.

To summarize,we have learnt following errors and their corrections with the help of examples:

Not accounting for the transaction cost

Not considering the slippages

Miscalculation of returns by not considering the units to be whole numbers

Miscalculation by not compounding the returns

Overfitting

Look Ahead bias

Survivorship bias

Referring to the wrong price of the instrument for taking positions

Interfering with the trading system or parameters of the algo

Concept Drift - Not retraining/reverifying the model regularly

Taking the preventive steps during the backtesting stage will significantly reduce the performance gaps betweenbacktestand real trading

Surprise Quiz

Yes, we've got a surprise for you.

To show how easy it is to commit and overlook one of these mistakes, we have deliberately left one of these in the above quizzes for you to figure out.

And we have not explained that error in the observation/explanation section of the quiz.

If you work it out then do let us know in the comments section detailing how have we managed to fail our backtesting in this example.

Need some help?Okay, I will tell you where you need to look for the error. Please click on the linkQuiz with hidden error.

A special thanks toVivek Krishnamoorthy,Ashutosh DaveandMario Pfor their valuable inputs.

File in the download

10 ways your trading strategy can fail - Python notebook

Login to Access&nbspthe&nbsplink

Disclaimer: All investments and trading in the stock market involve risk. Any decisions to place trades in the financial markets, including trading in stock or options or other financial instruments is a personal decision that should only be made after thorough research, including a personal risk and financial assessment and the engagement of professional assistance to the extent you believe necessary. The trading strategies or related information mentioned in this article is for informational purposes only.

---

*Imported from QuantInsti Blog on 2026-04-27*
