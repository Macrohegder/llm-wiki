---
title: "Index Tracking Trading Strategy with Example"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/etf-msci-futures-excel-model/"
date: "2015-12-14"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Index Tracking Trading Strategy with Example

**来源**: [QuantInsti](https://blog.quantinsti.com/etf-msci-futures-excel-model/)  
**日期**: 2015-12-14  
**作者**: QuantInsti

---

## 原文

Trading with ETF as a Lead Indicator

Index tracking trading model

Index tracking trading is a strategy where you observe price on the previous ‘n’candlestickand make your bets accordingly. The intuition is that MSCI FUTURES follows the ETF. Hence if ETF is performing well we assume MSCI FUTURES perform well too thus making buying and selling decision accordingly.

Who can use it?

People interested in algorithmic trading and those who want to learn about ETF as a lead indicator.

How it helps?

This excel model will help you to:

Build a strategy with ETF as a lead indicator

Understand the trading logic of strategy implementation

Optimize trading parameters

Why should you download the trading model?

As the trading logic is coded in the cells of the sheet, you can better the understanding by downloading and analyzing the files at your own convenience. Not just that, you can play around the numbers to obtain better results. You might find suitable parameters that provide higher profits than specified in the article.

Explanation of the model

In this example we consider the MSCI FUTURES data. We track an ETF and assume that the MSCI has a strong positive beta with the ETF. We observe the 5 minute intervals prices of ETF and MSCI and buy/sell MSCI based on the ETF returns. If the ETF returns arepositivewe buy one lot of MSCI FUTURES. If the ETF returns arenegativewe sell one lot of MSCI FUTURES. The ETF we track is Indian SP Equity. In essence we go long (buy) on MSCI futures if the ETF is bullish and go short (sell) on MSCI FUTURES if the ETF is bearish.

The data used for MSCI FUTURES contract is the data separated by5 minute interval from 2ndFeb 2015 to 4thof March 2015.

Assumptions

For simplification purpose, we ignore bid ask spreads.

Prices are available at 5 minutes interval and we trade at the 5 minute closing price only.

Since this is discrete data, squaring off of the position happens at the end of the candle i.e. at the price available at the end of 5 minutes.

Only the regular session (T) is traded

Transaction cost is $1.10 for MSCI FUTURE.

Margin for each trade is $1500.

Trading quantity is 1 lot (MSCI order size 50) and trading hours are 11:30 a.m. to 5:55 p.m. SGT.

Input parameters

Please note that all the values for the input parameters mentioned below are configurable.

Price at the end of 5 minute interval is considered.

We use ETF as a lead indicator

The market data and trading model are included in the spread sheet from the 12throw onwards. So when the reference is made to column D, it should be obvious that the reference commences from D12 onwards.

Explanation of the columns in the Excel Model

Column Crepresents the price for ETF.

Column Drepresents the price for MSCI FUTURES.

Column Erepresents log returns of ETF data.

Column Frepresents log returns of MSCI data.

Column Grepresents average returns of ETF data.

Column Hrepresents average returns of MSCI data.

Column Icalculates thetrading signal.The formula=IF(G13="", "", IF(G13>H13, "Buy", IF(G13<H13, "Sell", "I12")))means if the entry in cell G13 is blank then keep I13 blank otherwise if G13 (MSCI FUTURES data) is greater than H13 then buy signal for the MSCI FUTURES contract is generated else if G13 is lower than H13 then sell signal for the MSCI FUTURES contract is generated.

Column Jrepresentstrade price.This is the price at which the trading signal is generated. The formula=IF(I13="", "", IF(I13=I12, J12, D13))means if the entry in cell I13 is blank then the entry is blank. Otherwise if I13=I12, then the trade price is given by the entry in J12. If I13 is neither blank nor equal to I12 then the trade price is given by D13.

Column Krepresents theMark To Market.The formula=IF(OR(I13="", I12=""), 0, IF(I13=I12, K12, IF(I13="Buy", K12+J12-J13, IF(I13="Sell", K12+J13-J12, 0))))means if the cells I12 or I13 are blank then the MTM is zero. Otherwise if I13=I12 then MTM is K12 else if I13 is not equal to I12 and if I13 = “Buy” the MTM is given by K12+J12-J13 if I13 is not equal to I12 and if I13=”Sell” then MTM is given by K12+J13-J12.

Column Lrepresents theprofit/loss status of the trade.The formula=IF(OR(I13="", I12=""), "", IF(K13<K12, "Loss", IF(K13>K12, "Profit", IF(I13<>I12, "NPNL", ""))))means if either I13 or I12 is blank then the profit entry is also blank. Otherwise if K13 is less than K12 the entry is loss, if K13 is greater than K12 the entry is profit. The next part I13<>I12 means if I13 is not equal to I12 then it’s No Profit No Loss (NPNL). This makes sense since we have already calculated profit from previous squared off position.

Column Mcalculates the tradeprofit/loss.The formula=IF(L22="", 0,K22-K21 )means if L23 is blank meaning no profit no loss then the trade profit/loss is zero. If L23 is not blank then the profit is calculated as the difference in MTM values.

Outputs

The output table has some performance metrics tabulated.

Number of profitable trades is 118 and the number of loss making trades is 77.

Total trades are 277 and the total profit is $1970. Average profit per trade is $7.24. Net profit per trade is $5.04. This is calculated as average profit per trade minus twice the transaction costs. Number of trading intervals is 23. Monthly returns calculated as the product of total trades and net profit per trade divided by the product of margin for each trade and the number of days interpolation

Now it is your turn!

First, download the model

Modify the parameters and study the backtesting results

Run the model for other historical prices

Modify the formula and strategy to add new parameters and indicators! Play with logic! Explore and study!

Comment below with your results and suggestions

Click to download the excel (If you have not logged inyet, first login/sign up!)

Login to Download

---

*Imported from QuantInsti Blog on 2026-04-27*
