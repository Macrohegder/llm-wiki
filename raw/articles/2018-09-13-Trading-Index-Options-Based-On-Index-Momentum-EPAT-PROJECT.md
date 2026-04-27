---
title: "Trading Index Options Based On Index Momentum [EPAT PROJECT]"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/trading-index-options-index-momentum/"
date: "2018-09-13"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Trading Index Options Based On Index Momentum [EPAT PROJECT]

**来源**: [QuantInsti](https://blog.quantinsti.com/trading-index-options-index-momentum/)  
**日期**: 2018-09-13  
**作者**: QuantInsti

---

## 原文

Trading Index Options Based On Index Momentum [EPAT PROJECT]

This article is the final project submitted by the authors as a part of their coursework inExecutive Programme in Algorithmic Trading(EPAT™) at QuantInsti®. Do check our Projects page and have a look at what our students are building.

About the Author

With over 10 years of experience in the IT industry,Naveen Edamanais well established in the technical domain currently working as a Principal Consultant at Oracle India Pvt. Ltd. Graduating with honours in Physics, Naveen has previously worked with NIIT, SunTec and Allianz.

Project Abstract

The project goal is to set up and study an Index Option trading model based on Index’s momentum. The trading index options model is designed with following criteria in mind:

Least number of parameters for signal generation

Limiting financial risk due to unexpected events

Low or NIL margin requirement

The trading index options model studied in this project uses daily OHLC data of NIFTY and its Options. Entry and Exit signals are derived using Simple Moving Averages (SMA) on NIFTY OHLC candles. The signals are generated for LONG positions in CALL or PUT options

Introduction/Project Motivation

Options are used for a number of reasons, these include speculations, hedging, spreading and creating synthetic positions. If you are new to options contracts, we recommend going throughoptions trading basicsbefore exploring this index momentum model. A substantial number of option trading models are widely used and are well documented. However, most of the models require two or more positions in a combination of LONG/SHORT for CALL/PUT options with same or multiple strikes prices with/without calendar spread. These combinations could become complex to track & trade manually. Thus, requiring customized/automated software to track the portfolio performance and perform Entry/Exit of positions almost simultaneously or within a small timeframe. Rapid price variations during the timeframe could drastically impact the returns of the model.

In this project, an attempt is made to use Index based Options as a tool to follow Indexmomentumand generate acceptable returns with minimal risk. Following are the objectives the project has:

To build a trading model which is simple to 'Enter & Exit'

Signals are quick to derive and do not require complex calculations - which can be concluded using vanilla OHLC charts with few simple analytical tools

The model should only have limited financial risks, protect the investor from unexpected market movements.

Trading during 10-20 minutes of OPENING and 10-20 minutes to CLOSING of the trading window, should be sufficient for the model to operate

Trading Model - The Strategy

To meet the objectives and criteria set for the project following trading index options model was designed. The trading model:

uses OHLC data for NIFTY-50, Current & Near month OHLC for Nifty-50 Futures & Options

uses 15-Days SMAs on High and Low values of daily OHLC data of NIFTY-50 to generate Entry/Exist signals

also uses pre-set Target/Stoploss limits for Exist signal generation

signals are for Entry into LONG position ONLY, to be executed at last 5-10 minutes to CLOSING for the day

maintains only ONE open position at any point of time

One can alsolearn about sentiment indicators, how to interpret them and devise trading strategies based on these interpretations.

Entry Rules

The trading model rules for Entry into LONG position for either CALL/PUT options are as following:

If the day’s OHLCcandlestickis GREEN in colour, Enter LONG-CALL position if:

Day’s OHLC candlestick (both Body & Tails) is above the HIGH-SMAs
AND
Previous day’s OHLC candlestick is GREEN in colour
AND
(any one of following)
Previous day’s OHLC candlestick’s Body cut across the two SMAs
OR
Previous day’s OHLC candlestick’s Body cut across either of the two SMAs
OR
Previous day’s OHLC candlestick’s Body is below the LOW-SMA but has Upper Tail cut across of the LOW-SMA
OR
Previous day’s OHLC candlestick’s Body is between the two SMAs with Tails (Upper or Lower or Both) cut across the one or both SMAs
OR
Previous day’s OHLC candlestick (both Body and Tails) is between the two SMAs

If the day’s OHLC candlestick is RED in colour, Enter LONG-PUT position if:

Day’s OHLC candlestick (both Body & Tails) is below the LOW-SMAs
AND
Previous day’s OHLC candlestick is RED in colour
AND
(any one of following)
Previous day’s OHLC candlestick’s Body cut across the two SMAs
OR
Previous day’s OHLC candlestick’s Body cut across either of the two SMAs
OR
Previous day’s OHLC candlestick’s Body is above the HIGH-SMA but has Lower Tail cut across of the HIGH-SMA
OR
Previous day’s OHLC candlestick’s Body is between the two SMAs with Tails (Upper or Lower or Both) cut across the one or both SMAs
OR
Previous day’s OHLC candlestick (both Body and Tails) is between the two SMAs

Exit Rules

The trading model rules for Exit from a LONG position for either CALL/PUT options are as following:

If the value of position has hit or exceeded the TARGET, Exit the position and book profit
OR

If the value of the position has hit or fallen below the STOPLOSS limit, Exit the position and book loss
OR

In case of LONG-CALL position, Exit the position if:
Day’s OHLC candlestick is below LOW-SMA
OR
Day’s OHLC candlestick’s Body or Tail (or both) cut across any or both SMAs

In case of LONG-PUT position, Exit the position if:
Day’s OHLC candlestick is above HIGH-SMA
OR
Day’s OHLC candlestick’s Body or Tail (or both) cut across any or both SMAs
OR
Else mark the position expired if the position fails to hit TARGET/STOPLOSS even on/till the expiry date

Target / Stop Loss Rules

The trading model has pre-defined value for Target and Stop Loss Limits. These values are computed at the time of Entry itself. The formula used is:

Profit booking TARGET price = Buy Rate * (1 + pre-fixed target percentage)
and
Stoploss limit = Buy Rate * (1 - pre-fixed target percentage)

Position Sizing Rules

The position sizing (i.e. number of lots or units to be purchased in case of LONG trade), is determined using current account balance. A pre-defined percentage value of the account balance is used to purchase maximum possible lots (one lot = 75 units of an option). The formula used is:

lot count = floor ((account balance * pre-fixed percentage / 100) / option price / lot size)
and
number of units to purchased = lot count * lot size

Strike Price & Expiry Selection Rules

The trading model uses ATM/OTM Strike Prices for position creation. The expiry could be the Current month or Near month, which is selected based on a pre-defined number of days to expiry limit value.

Transaction Cost Rules

The trading model considers brokerage charges and taxes as part of transaction cost both at BUY and SELL side.

Pre-defined Values

The trading model is based on a few pre-defined parameters. They are:

Number of days to expiry limit for considering Current Month or Near Month option strike

Percentage of account balance limit to be used for the purchase of options lots/units

Take profit (target) limit

Stop loss limit

Brokerage charge

Tax percentage

Back Testing & Evaluation For Trading Index Options

To evaluate the trading index options model, the trading strategy is converted into an algorithm using PYTHON language. Using the Python code, backtesting is conducted on the trading model and the effectiveness of the model is evaluated.

Data Gathering

For backtesting, data from 1st January 2007 till 30th Nov 2017, was collected from NSE’s website. Following data are available from the NSE’s website in as bhav / excel files:

Daily OHLC data for NIFTY 50

Daily OHLC data for NIFTY Futures

Daily OHLC data for NIFTY Options (Call & Put)

These downloaded data were uploaded into Oracle database tables, which were then read-in by Python code using Oracle database connector module (cx_Oracle), for test cycles.

Following are the various fields w.r.t NIFTY-50 index available

Following are the various fields w.r.t Futures and Options available

Data Preparation

Data preparation & filter is performed in Python code. Following steps are performed:

Daily OHLC data are fetched from the database for NIFTY, Current month Future & Near month Future, for the period test cycle is performed.

15Day-Simple Moving Average (s) are calculated for the dataset using NIFTY’s-High and Low OHLC values

Candlestick (OHLC) properties – Color and Position w.r.t SMAs- are derived

Candlestick properties are scanned through to identify Trade signals based on Entry Rules

Trading Index Model Testing & Optimized Parameters

The whole dataset was split into four test blocks:

Set 1: From 1st January 2007 till 31st December 2010

Set 2: From 1st January 2011 till 31st December 2015

Set 3: From 1st January 2016 till 30th November 2017

Full set: From 1st January 2007 till 30th November 2017

Using Set 1 & 2 the trading model rules & parameters were optimized and the same were run on other sets for validation.
Based on multiple tests run following optimized rules/parameters where identified:

ATM Strike Prices are observed to give best results

Investment fraction (% of account balance) = 15%

Take profit Target limit = 100%

Stop Loss limit = 75%

Number of days to expiry limit = 20

Set 1 - Test Result

Following are the test results for SET 1 with optimized parameters:

The Plot below shows the Strategy Return vs Nifty Return and the Account Balance for the period.

Set 2 - Test Result

Following are the test results for SET 2 with optimized parameters:

The plot below shows the Strategy Return vs Nifty Return and the Account Balance for the period.

Set 3 - Test Result

Following are the test results for SET 3 with optimized parameters:

The plot below shows the Strategy Return vs Nifty Return and the Account Balance for the period.

Full Set - Test Result

Following are the test results for Full Set with optimized parameters:

The plot below shows the Strategy Return vs Nifty Return and the Account Balance for the period.

Key Findings, Challenges/Limitations of Trading Model

The trading index options model is observed to provide reasonable returns along with minimizing the financial risk. The trading index options model has provided 600% returns in 10 years timeframe with just 119 trades. Even though Success Ratio of the model is not attractive, as the absolute value of the mean of the negative returns is less compared to mean of the positive returns along with lesser standard deviation, provides net value generation.

The trading index options model was also able to protect investor during 2008 market crash as observed from charts of SET 1 / Full set test results. The same is observed during the year 2011, the year 2015 and Nov/Dec-2016 periods.

However, the trading index options model failed to make use of the 2009’s sharp market recovery. Also, it failed to prevent drawdown during the latter part of 2012 and during 2013, when the market had fluctuations.

Even though from the graphs, it looks like the trading index options model has done well with LONG-PUT trades compared to LONG-CALL trades, however, LONG-CALLs have generated 3-time returns generated by LONG-PUT trades. LONG-CALL trades generated net profit was at INR 457,651 while LONG-PUT trades generated a net profit of INR 167,372.

One of the major challenge faced is early exits, resulting in not able to make full utilization of the momentum drive. Below image shows case in which the first trade signal for the year 2017 was generated on 24th Jan 2017, with Target of 100% of Buy Price. The Target was hit on 2nd Feb 2017.

However, the trading index options model generated next trading signal on 6th Mar 2017, missing the whole NIFTY’s momentum gained during the month of Feb 2017, as the profile did not have any open positions.

Attempts to fix this issue did not help much, any follow up LONG-CALL purchases ends up in STOP-LOSS due the Theta decay and dip in NIFTY during 12-17 Feb date ranges.

Similarly, another issue observed is in case of STOP LOSS exits resulting in missing the momentum followed it.

Conclusion

The trading index options model worked in this project requires considerable future enhancements, along with handling early exits due to Target/Stoploss triggers. Using additional analysis tools could help to improve the model.

Read More

You might also find the following of our previous articles interesting to read:

Dispersion Trading Using Options

Index Arbitrage - An Automated Options Trading Strategy

Open Interest In Options Trading Using Python

Covered Call Strategy Using Machine Learning

Next Step

If you want to learn various aspects of Algorithmic trading then check out theExecutive Programme in Algorithmic Trading (EPAT™). The course covers training modules like Statistics & Econometrics, Financial Computing & Technology, and Algorithmic & Quantitative Trading. EPAT™ equips you with the required skill sets to build a promising career in algorithmic trading. Enroll now!

Disclaimer: The information in this project is true and complete to the best of our Student’s knowledge. All recommendations are made without guarantee on the part of the student or QuantInsti®. The student and QuantInsti® disclaim any liability in connection with the use of this information. All content provided in this project is for informational purposes only and we do not guarantee that by using the guidance you will derive a certain profit.

Files in the download:

Trading Using Index Options Based On Index's Momentum - Python File

Login to Download

---

*Imported from QuantInsti Blog on 2026-04-27*
