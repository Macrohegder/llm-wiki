---
title: "Turning data into insights and building strategy using Python"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/data-insights-trading-strategy-python-project-lokesh-kumar/"
date: "2020-09-28"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Turning data into insights and building strategy using Python

**来源**: [QuantInsti](https://blog.quantinsti.com/data-insights-trading-strategy-python-project-lokesh-kumar/)  
**日期**: 2020-09-28  
**作者**: QuantInsti

---

## 原文

Turning data into insights and building strategy using Python

This article will help you learn how to analyse data to acquire insights via Livestock market dataand datasets. It will also help you to learn how you can create your own trading strategy using Python programming.

The complete data files and python code used in this project are also available in a downloadable format at the end of the article.

This article is the final project submitted by the author as a part of his coursework in the Executive Programme in Algorithmic Trading (EPAT®) at QuantInsti®. Do check ourProjects pageand have a look at what our students are building.

About the Author

Lokesh Kumaris a risk manager at one of the largest US Bank located in Mumbai. He has over 6 years of experience in the banking and financial sector, having worked in the field of regulatory models, credit decision models, macroeconomic research and analytics.

Lokesh holds BA Economics Honors from the University of Delhi and an MSc in Financial Economics from Madras School of Economics. Additionally, he holds a certification in risk management (FRM – US GARP). He is also an EPAT alumnus.

Motivation for the study

I am an economics student and risk manager. I have been doing data analysis, statistical, econometric, machine learning modelling using various statistical software (R, SAS, STATA, EVIEWS) for the last 6 years but never got a chance to work on Indian equity data.

This project proved to be a stepping stone to follow my interest and make a career in the Indian equity market. In addition, I have been tracking the Indian financial market and news across the globe for 5 years.

The data for the analysis includes these variables.

2 (liquid, volatile, positive annual return) stocks from each sector.

The frequency of data is daily.

Models

Momentum, Mean Reversion and Pair Trading: Analysis – Excess Return, Sharpe Ratio, Maximum drawdown, drawdown duration, In-sample and out-of-sample testing, Absolute return, relative return, profitability analysis.

Backtest models

Evaluating strategy performance

Project Abstract

This project examines stock prices behaviour and movement. We analyzed 20 stocks from an exhaustive list of stocks from Nifty sectoral indices for the period October 2010 to December 2018; considering 2 stocks from each sector based on high annualized average rolling return and volatility.

We explored the stock prices and volume data and built 3 strategies – Volume and Price based trading, Mean Reversion and Trend following- RSI. We found that there is no one particular strategy which works for all the stocks.

We evaluated the strategy performance and found a high return and hit ratio. We also did an out of sample test for the small sample period January 2019 to March 2019 to observe if we could have used these strategies in the live market then how much profit we could have generated.

Introduction

The objective is to determine the entry & exit point, long & short the trade with high confidence using a different modelling approach. We focused on building strategies which generate high returns and are easily implementable.

First, we explored the volume and price relationship as there are many technical indicators available based on volume and price. An uptrend is strong and healthy if volume increases as price increases, and decreases when the market moves into a counter-trend. If you wish to learn more about using technical indicators for trading strategies, you must enrol into our course onTechnical Indicators Python.

Second, we explored the cross-sectionalmean reversion strategywhich attempts to exploit temporary mispricing between two securities from the same sector.

Third, we explored thetrend following strategywhere you follow the trend i.e. long when the price is going up and short when the price is going down. We computed the relative strength index (RSI) which evaluates overbought and oversold conditions in stock prices.

Data Mining

We used 2 stocks from each sector of India’s equity market.  We first looked at Nifty sectoral indices and the list of stocks included in each index. The indices comprise the most liquid, large capitalized stocks which reflect the behaviour and performance of each sector.

We analyzed a total of 126 stocks based on average annualized rolling return and rolling volatility using the 20 days rolling window.

We finalized the 2 stocks from each sector based on high volatility, high and positive return.

We extracted the stock prices and volume data from yahoo finance for the period from January 2010 to December 2018.

The final dataset consists of 20 stocks for the period from October 2010 to December 2018. The data was available from October 2010 for all 20 stocks.

The list of stocks used for the analysis:

Sr. No.

Symbol

Company Name

Industry

APOLLOTYRE

Apollo Tyres Ltd.

AUTOMOBILE

ASHOKLEY

Ashok Leyland Ltd.

AUTOMOBILE

PRESTIGE

Prestige Estates Projects Ltd.

CONSTRUCTION

OBEROIRLTY

Oberoi Realty Ltd.

CONSTRUCTION

JUBLFOOD

Jubilant Foodworks Ltd.

CONSUMER GOODS

United Breweries Ltd.

CONSUMER GOODS

Power Finance Corporation Ltd.

FINANCIAL SERVICES

RECLTD

REC Ltd.

FINANCIAL SERVICES

NIITTECH

NIIT Technologies Ltd.

MINDTREE

MindTree Ltd.

TVTODAY

TV Today Network Ltd.

MEDIA & ENTERTAINMENT

INOXLEISUR

Inox Leisure Ltd.

MEDIA & ENTERTAINMENT

WELCORP

Welspun Corp Ltd.

METALS

HINDALCO

Hindalco Industries Ltd.

METALS

AUROPHARMA

Aurobindo Pharma Ltd.

PHARMA

BIOCON

Biocon Ltd.

PHARMA

INDIANB

Indian Bank

PUBLIC BANK

BANKBARODA

Bank of Baroda

PUBLIC BANK

FEDERALBNK

Federal Bank Ltd.

PRIVATE BANK

AXISBANK

Axis Bank Ltd.

PRIVATE BANK

Data Analysis

We computed the descriptive statistics of stocks returns, hit ratio and cumulative profit/loss.

Following is the technical description of each strategy used in the project:

InVolume and price-based trading strategy, we generated a short signal if the current volume is less than the last 3 days ofmoving averagevolume and the current price is less than the last 3 days of moving average price. We tried different short time frames such as 3,4,5,14 but 3 days was giving best results and also tried to generate long signal but that was not giving positive results in any of the stocks so we went ahead with short sell trade only.

InMean-reversion pair trading strategy, we considered 2 similar stocks from each sector, computed the price ratio and checked if the price ratio (spread or PS1/PS2) is cointegrated then the stocks are mean-reverting and can apply the pair-trading strategy.

We found many of the price ratios were not cointegrated. We checked cointegration using the Augmented Dicky Fuller (ADF) test. We created the signals – long entry in S1 when the spread goes below the lower band and long exit in S1 when the spread goes above the moving average, a short entry in S1 when the spread goes above the upper band and short exit in S1 when the spread goes below the moving average, and take the reverse position in S2.

We tried different time frames such as 5, 14, 21 days to compute rolling return and volatility but 5 days was giving best results and also tried +/- 1 or +/- 2 standard deviations to compute upper and lower band, and finalized +/- 1 standard deviation based on the results.

InTrend-following RSI strategy, the value of 70 or above indicates that the security is overbought so short the stock and value of 30 or below indicate that the security is oversold so long the stock. We use the 21 days period to compute RSI. However, we explored different time frames such as 5, 14, 21,30, 60 days but 21 days was giving the best results.

Key Findings

We provide the summary statistics of 20 stocks. Negative skewness indicates that the distribution of returns is negatively biased.

Excess Kurtosis (Kurtosis greater than 3) indicates the distribution of returns has fatter tails (higher extreme outcomes).

Symbol

Std. Deviation

Minimum

Maximum

Percentile 25th

Percentile 50th

Percentile 75th

Skewness

Kurtosis

APOLLOTYRE

-29.37

ASHOKLEY

-15.09

PRESTIGE

-13.35

OBEROIRLTY

-11.70

JUBLFOOD

-11.91

-12.67

-15.52

RECLTD

-13.55

NIITTECH

-12.60

MINDTREE

-18.36

TVTODAY

-18.15

INOXLEISUR

-15.21

WELCORP

-31.45

HINDALCO

-10.17

AUROPHARMA

-18.44

BIOCON

-12.46

INDIANB

-13.11

BANKBARODA

-17.89

FEDERALBNK

-13.04

AXISBANK

Volume/Price Based Short Sell Strategy

We deploy this strategy on all 20 stocks. The data shows that this strategy leads to a 55% hit ratio and a 9.7% annualized return on an average. Cumulative PnL shows that the amount invested (INR 1) in October 2010 turned out to be (INR 2.291) in December 2018 on an average.

Symbol

# Positive Trades

# Total Trades

Hit Ratio

Cumulative PnL

Avg. Annualized Return

APOLLOTYRE

ASHOKLEY

PRESTIGE

OBEROIRLTY

JUBLFOOD

RECLTD

NIITTECH

MINDTREE

TVTODAY

INOXLEISUR

WELCORP

HINDALCO

AUROPHARMA

BIOCON

INDIANB

BANKBARODA

FEDERALBNK

AXISBANK

Mean Reversion Pair Trading Strategy

We found only 2 pair of stocks cointegrated in our analysis. The p-value is less than a 10% significance level for PFC & RECLLTD and less than 1% significance level for TVTODAY & INOXLEISUR.

The data shows that this strategy leads to a 52% hit ratio and 13.7% annualized return on an average. Cumulative PnL shows that the amount invested (INR 2) in October 2010 became (INR 5.677) in December 2018 on an average.

Symbol

# Positive Trades

# Total Trades

Hit Ratio

Cumulative PnL

Avg. Annualized Return

RECLTD

TVTODAY

INOXLEISUR

Trend Following RSI Strategy

We developed this strategy for NIITTECH because the volume and price based short selling strategy failed to generate good returns and the IT pair was not cointegrated.

The data shows that this strategy leads to a 69% hit ratio and 6.5% annualized return on an average. Cumulative PnL shows that the amount invested (INR 1) in October 2010 turned out to be (INR 1.652) in December 2018 on an average.

Symbol

# Positive Trades

# Total Trades

Hit Ratio

Cumulative PnL

Avg. Annualized Return

NIITTECH

Out of Sample Backtest

We have optimized the strategy based on historical data from October 2010- December 2018 period.

We run an out of sample backtest and see how the strategy performs if we could have used those strategies in the market to generate profits. The out of sample backtest period used in the analysis is January 2019 to March 2019.

Volume/Price Based Short Sell Strategy

According to historical data results, we test this strategy on those stocks which have generated more than 10% return in the past and observed how this strategy could have performed if we have invested our money in the market for the period January 2019 to March 2019.

The data shows that this strategy leads to a 55% hit ratio and 25.3% annualized return on an average.

Symbol

# Positive Trades

# Total Trades

Hit Ratio

Cumulative PnL

Avg. Annualized Return

APOLLOTYRE

ASHOKLEY

PRESTIGE

OBEROIRLTY

-15.4%

JUBLFOOD

-20.5%

TVTODAY

WELCORP

INDIANB

-11.3%

Mean Reversion Pair Trading Strategy

The data shows that this strategy leads to a 45% hit ratio and 5.4% annualized return on an average.

Symbol

# Positive Trades

# Total Trades

Hit Ratio

Cumulative PnL

Avg. Annualized Return

RECLTD

TVTODAY

-38.1%

INOXLEISUR

Trend Following RSI Strategy

The data shows that this strategy leads to a 50% hit ratio and 4.5% annualized return on an average.

Symbol

# Positive Trades

# Total Trades

Hit Ratio

Cumulative PnL

Avg. Annualized Return

NIITTECH

Limitations

We haven’t included transaction costs in order to compute return.

Implementation Methodology

This is a completely live project and can be easily implementable in the trading system.

Volume and Price based Short Selling Strategy

If current day volume goes below last 3 days of average volume and current day closing price goes below last 3 days of average closing price, buy the stock at the open price and sell the stock at the close price on the next day.

Mean Reversion Pair Trading Strategy

If current-day spread (price ratio of stock1/stock2) goes below lower band (5 days moving average of spread – 5 days moving standard deviation of spread), make a long entry in stock1 the next day.

If current-day spread (price ratio of stock1/stock2) goes above 5 days moving average of spread, make a long exit in stock1 on the next day.

If current-day spread (price ratio of stock1/stock2) goes above the upper band (5 days moving average of spread + 5 days moving standard deviation of spread), make a short entry in stock1 the next day.

If current-day spread (price ratio of stock1/stock2) goes below 5 days moving average of spread, make a short exit in stock1 on the next day. And take the reverse position in stock2 simultaneously.

If the long and short signal is fresh, trade at an open price otherwise trades at a close price.

Trend Following RSI Strategy

If current-day RSI goes below 30, long the stock the next day.

If current-day RSI goes above70, short the stock the next day.

If the long and short signal is fresh, trade at an open price otherwise trades at a close price.

Conclusion

We explored the stock prices and volume data and built 3 strategies – Volume and Price based trading, Mean Reversion and Trend following- RSI.

We find that there is no one particular strategy which works for all the stocks. We evaluated the strategy performance and found high overall return and hit ratio.

However, we can explore a lot of other strategies which we learnt in the course and generate a much higher return than what these strategies accomplished.

If you want to learn various aspects of Algorithmic trading then check out theExecutive Programme in Algorithmic Trading (EPAT). The course covers various training modules and equips you with the required skill sets to build a promising career in algorithmic trading.

Bibliography

NSE Sectoral Indices

QuantInsti EPAT Projects

Files in the download

Project code strategy in Python

Project code data extract in R

Login to Download

Disclaimer: The information in this project is true and complete to the best of our Student’s knowledge. All recommendations are made without guarantee on the part of the student or QuantInsti®. The student and QuantInsti®disclaim any liability in connection with the use of this information. All content provided in this project is for informational purposes only and we do not guarantee that by using the guidance you will derive a certain profit.

---

*Imported from QuantInsti Blog on 2026-04-27*
