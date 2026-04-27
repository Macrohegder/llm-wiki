---
title: "TWAP Algorithm: Understanding Time-Weighted Average Price, TWAP vs VWAP & More"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/twap/"
date: "2020-07-08"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# TWAP Algorithm: Understanding Time-Weighted Average Price, TWAP vs VWAP & More

**来源**: [QuantInsti](https://blog.quantinsti.com/twap/)  
**日期**: 2020-07-08  
**作者**: QuantInsti

---

## 原文

Time-Weighted Average Price (TWAP): Introduction, Some Examples, and Calculations

ByChainika Thakar

This article discusses the time-weighted average price in detail as this execution strategy is quite helpful for large trade orders. If you want to know the what, why and how of TWAP and its difference fromVWAP, then this article will serve your purpose well.

Let us see what this article covers. It consists of:

What is TWAP?

Example of TWAP

How is TWAP calculated?

Why choose TWAP?

TWAP vs VWAP

Pros of TWAP

Cons of TWAP

What is TWAP?

Time-weighted Average Price (TWAP) is a well-known trading algorithm which is based on the weighted average price and is defined by time criterion. TWAP is calculated for executing large trade orders. With the TWAP value, the trader can disperse a large order into a few small orders valued at the TWAP price since it is the most beneficial value.

This is basically done to not let a huge order suddenly increase the value of a particular financial asset in the financial market.

Let us now see an example of TWAP.

Example of TWAP

Let us assume that someone wants to make a strategy to buy 10,000 shares of an asset. In the process of making the strategy, one can choose from two possible strategies. One, a trader can issue orders to purchase 500 shares every 15 minutes for 5 hours.

Two, the trader can implement a strategy in which the order is issued to purchase 1,000 shares every 15 minutes for 2.5 hours.

But, with a strategy going on in the financial market, it is simpler to track the trading pattern by other traders and make a guess about the next strategy until and unless its orders are modified by adjusting the parameters. Further, this modification implies that the orders’ size can be randomized or the time between each order can be delayed.

Now, let us find out how the TWAP value can be calculated for a longer duration.

How is TWAP calculated?

In the case of Time-weighted Average Price, TWAP is calculated by averaging the entire day’s price bar, i.e., open, high, low, and close prices of the day. Then, on the basis of time decided to execute an order, every day’s averaged price is taken for calculating the average of the entire duration’s prices. This is known as the TWAP.

TWAP strategy is the best execution strategy for spreading out the trades over a specific time period and reduce the impact of trade on the market.

Like every trade, the TWAP also performs when all the conditions are met before which the price is calculated from the entry of the order and goes through the close of the market.

Formula to calculate TWAP

The calculation of TWAP goes as follows:

Average of each day’s price= (Open + High + Low + Close)/4

Average of 28 days= (Average of first day’s price + Average of second day’s price +........+ Average of twenty-eighth day’s price)/28

Calculating TWAP in Excel

In the excel sheet, you can calculate the average of each day. You can take the historical data fromNASDAQby simply typing the symbol of the stock you want the data of. Here, we have taken the data of Apple Inc. on which the calculation of the average of each day in the excel sheet is done in the following way:

Above, the calculation was done using the formula =AVERAGE(B2:E2) as shown in the cell. We had taken two months’ data from Apple Inc.

For calculating the average of each row, you simply need to copy and paste the formula for every row in the cell under TWAP.

Further, for averaging the entire period’s average, you simply put the formula =AVERAGE(G2:G23) as shown below:

The average comes out to be $328.15 taken out under the heading Av_row.

After calculating TWAP, your order price will be considered undervalued when it is below TWAP and overvalued when it is above TWAP.

Calculating TWAP using Python

We can calculate TWAP using Python as well. First of all, we will fetch the data of the stock we wish to calculate TWAP of.

Output:

Above we have got the entire data from 2020-05-18 to 2020-06-18 as we did above in the excel sheet.

Now, we will find each row’s average under the column “av_row” since, in TWAP calculation, the first step is to find out the average of OHLC of each trading day.

Output:

Now, we will calculate the average of all trading days’ averaged prices under the column “av_row”.

Output:

328.151

Hence, the average comes out to be $328.151 which is our TWAP value.

Now, let us move forward and see why one should choose TWAP?

Why choose TWAP?

In the case of TWAP, the calculated result is used to find the value of the market price. Also, most traders utilise TWAP because of the following:

Helpful

The way it helps with the execution of order over a period of time in smaller parts instead of one huge order in one go.

or example, suppose your trading algorithm offers you a buy signal and you want to purchase 10,000 shares of the stock. Now, with the option to spread this order in small portions, say, 500 or 1000 each hour/minute, the trader can reduce the impact on the market. Or else, the execution of 10,000 shares at once can put an adverse effect on the price.

Traders with the requirement of high-volume trading use TWAP to execute their orders in smaller parts when the market price is close to the TWAP. This way, the execution becomes smooth.

Successful

The TWAP execution strategy is a success amongst traders who doHigh-Frequency Tradingor other types ofQuantitative tradinglike algorithmic trading. It simply divides the large orders into small portions and makes it easier for investors.

Impact

TWAP signals do not affect the volatility of the financial markets. In the case of the TWAP execution trading strategy, the trader can place a huge volume of trade orders and then transact at a single price. This is true even if it takes a long time to completely execute the trade order. Hence, huge trade orders can be implemented easily.

TWAP signals cover a considerable amount of risk with their calculations.

Key takeaways of TWAP value:

Helps calculate the average price for trading.

Is used for executing small parts of a huge trading order or for high-frequency trading.

Covers a significant amount of risks associated as the calculated price is the most beneficial price for trading.

Minimizesimpact costs.

Now, let us take a look at how TWAP differs fromVWAPwhich is also a calculation of weighted average price.

TWAP vs VWAP

The fact between TWAP and VWAP is that VWAP can not be as simply calculated as TWAP can be.

Mainly, TWAP and VWAP have the following key differences:

Timing- TWAP is calculated by weighing it on the basis of time whereas VWAP is calculated on the basis of volume and time.

Process- It is easier to calculate the value of TWAP as compared to VWAP since VWAP involves a complicated process to calculate the value of the weighted average price.

Small Volume of Transactions- With TWAP, it is easier to calculate the small volume of transactions but not with VWAP.

Perfect! Now let us move to the pros and cons of TWAP.

Pros of TWAP

Simple calculation

Easy to obtain output in python and excel

The perfect solution for executing large orders

Does not put an impact on market price with the execution of the entire large order

Cons of TWAP

Too predictable which can make your strategy vulnerable to other traders

More primitive

Conclusion

In this article, we discussed the basic concept of Time-weighted average price (TWAP) which aimed to help you go through various aspects of TWAP.

If you're starting your journey in quantitative trading check out Quantra's course onQuantitative Trading Strategies and Modelsthat teaches basic technical trading strategies, like the trend based strategy and the Bollinger bands strategy which can be traded on the live markets as well. Enroll now!

Disclaimer: All investments and trading in the stock market involve risk. Any decision to place trades in the financial markets, including trading in stock or options or other financial instruments is a personal decision that should only be made after thorough research, including a personal risk and financial assessment and the engagement of professional assistance to the extent you believe necessary. The trading strategies or related information mentioned in this article is for informational purposes only.

---

*Imported from QuantInsti Blog on 2026-04-27*
