---
title: "Cash to Future Arbitrage"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/cash-to-future-arbitrage/"
date: "2020-01-29"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Cash to Future Arbitrage

**来源**: [QuantInsti](https://blog.quantinsti.com/cash-to-future-arbitrage/)  
**日期**: 2020-01-29  
**作者**: QuantInsti

---

## 原文

Cash to Future Arbitrage

Arbitrage between cash and derivatives (futures) is more prevalent now. This EPAT project will help you understand and learn how you can build-up a module on Cash future Arbitrage. This, in turn, would help you bet on cash future spread to maximize intraday profits.

This article is the final project submitted by the authors as a part of their coursework in the Executive Programme in Algorithmic Trading (EPAT®) at QuantInsti®. Do check ourProjects pageand have a look at what our students are building.

About the Author

Chandrashekhar Satoskaris an arbitrage trader at Religare Securities Ltd. He holds bachelors in Commerce from Mumbai University and has completed his Master’s in Business Administration (M.B.A.) from Vinayaka Mission's Research Foundation. He is currently working as a Bullion, Equity & Derivative Trader in Westbury Tradecom Limited.

Project Motivation

As an EPAT alumni, I am very much interested in building-up a module on Cash future Arbitrage which will help the traders or jobbers to bet on cash future spread just like intraday spread betting to maximize intraday profits. For backtesting the above strategy, I am taking the help of Excel for the same.

Arbitrage

There are two types of arbitrage:

Whenever Futures price is greater than the Spot price, it is known as "Contango"or called as futures trading @ Premium

Whenever Futures price is less than (discount) Spot price it is known as “Backwardation”or called asfutures trading@ Discount.

There are also two types of arbitrageurs:

One set is more like day traders or jobbers, playing on spreads between cash and futures and capturing jobbing differences wherever possible.

The other set is more like medium-term investors, who are interested in a fixed income stream for a medium-term without taking any credit risk or underlying view.

Data Mining

We can get data from many API or interactive brokers. For data mining, I am using ZERODHA PI software which gives per minute data which helps to collect data for backtesting the module.

Data Analysis

Following are the steps for data analysis:

1. First, get rates ofSPOTandFUTUREas per time frame -Here I am using 1 min. time frame

2. Calculate the difference between future and spot known asSPREAD.

3. Calculate theBollinger bandof the spread which we get to identify upper and lower limits of spread and also will get mean for the same.

4. CalculateCCI (Commodity Channel Index)of spread to identify trends of spread

5. CalculateMACD (Moving Average Conversion Diversion)of CCI which will help to identify spread conversion diversion signal from MACD

6. After the above calculation time to generate a signal for the strategy,

WheneverSpread is greaterthan or equal to Upper Bollinger band and the value of MACD is less than MACD signal value then will Buy Spot and Sell Future i.e. Fresh Up.

WheneverSpread is lessthan or equal to Lower Bollinger band and the value of MACD is greater than MACD signal value then will Buy Future and Sell Spot i.e. Unwind.

If the aboveconditions do not match, then we will keep the cell blank.

7. Calculate BPS (basis Points):BPS = Spread / Price*100

8. Now we will define the status column to identify what is the current status of the trade i.e. Fresh UP or Unwind:

We will take one trade at a time - this means if one trade going on ignores all trading signals till FA END (Take P&L from Fresh UP) or UN END (Take P&L from Unwind) come.

We will not take a new unwind signal after 3.15 pm because in the Indian market carryingshort sellingis not allowed

If the previous status is BLANK (NO Trade) then keep cell as blank

If the previous status is FRESH UP and Spread is Less than or equal to Lower Bollinger band and the value of MACD is greater than MACD signal value then FA END (will take P&L from Fresh UP).

If the previous status is Unwind and Spread is greater than or equal to Upper Bollinger band and the value of MACD is less than MACD signal value then UN END (will take P&L from Unwind).

9. After we know the status of trade time to execute the trade quantities as per given fund size, I took 1 cr of fund for backtesting the above strategy.

So we use this formula:

If the current status is FRESH UP or UNWIND then ROUNDDOWN 				(TotalFund/Price)/Lot Size of Particular stock * Lot Size

10. Now we define the buy price or sell price so we take from Spot price or future price

If the current status isFresh upthen will take spot price as a buy price and sell price as a future price

If the current status isUnwindthen will take future price as a buy price and sell price as a spot price)

11. Now defineBuy valueandSell valueso the formula is,

Buy Value = Price * Lot Size

Sell Value = Price * Lot Size

12. CalculateGross profit: It is the difference between Fresh UP Spread and FA END Spread or Unwind Spread and Un END spread

13. CalculateNet Profit: Net Profit = Gross profit – Trading Expenses

14. Calculatereturn NP in BPs: Return NP = Net Profit / Total fund*100

15. Calculate Strategy results such as:

Positive results,

Negative results,

Positive trades,

Negative trades,

Average returns.

Challenges

Forecast Fresh UP or Unwind Signal on an intraday basis

Drawback: Short selling is not allowed

Buyer and Seller must have a Unique ID to enter a trade in any particular stock if the same trade will square off automatically and will be released into Trading Expenses.

Key Findings

To develop intraday trading for jobbers and traders and generate returns with using of big funds

Trade whenever Spread touches upper or lower Bollinger band with MACD or crossed over MACD signal line

Don’t initiate the trade after 3.15 pm because there are low chances to earn good returns

If you properly follow the above steps there are chances to earn a good amount of money in intraday

Whenever taking the new trade look into Nifty/Banknifty SPOT and Future premium/discount which would be your additional tool to trade.

Try to search the stocks with upcoming results, Corporate actions, Budget’s month, RBI policy etc. which will create more trading opportunity with a chance to earn an additional alpha.

Conclusion

The above trading strategy is a low-risk strategy that seeks to generate additional alpha in intraday trading using the

Bollinger band,

Commodity Channel Index, and

Different time frame applies for different stocks so select the right time frame to right stocks while backtesting and trading.

Above strategy, overall performance ratio will be around 70% but do backtest as per your end. Trading is tough, I hope this strategy helps all traders to trade from my experience no trading strategy lasts forever, I find myself reinventing my trading styles and try to develop new strategies.

Good Luck and Happy Trading!

If you want to learn various aspects of Algorithmic trading then check out theExecutive Programme in Algorithmic Trading (EPAT). The course covers training modules like Statistics & Econometrics, Financial Computing & Technology, and Algorithmic & Quantitative Trading. EPAT equips you with the required skill sets to build a promising career in algorithmic trading.

Disclaimer: The information in this project is true and complete to the best of our Student’s knowledge. All recommendations are made without guarantee on the part of the student or QuantInsti®. The student and QuantInsti®disclaim any liability in connection with the use of this information. All content provided in this project is for informational purposes only and we do not guarantee that by using the guidance you will derive a certain profit.

---

*Imported from QuantInsti Blog on 2026-04-27*
