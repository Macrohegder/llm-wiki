---
title: "Pandas OHLC: Convert tick by tick data to OHLC data"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/tick-tick-ohlc-data-pandas-tutorial/"
date: "2022-06-06"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Pandas OHLC: Convert tick by tick data to OHLC data

**来源**: [QuantInsti](https://blog.quantinsti.com/tick-tick-ohlc-data-pandas-tutorial/)  
**日期**: 2022-06-06  
**作者**: QuantInsti

---

## 原文

Pandas OHLC: Convert tick by tick data to OHLC data

ByDanish Khajuria

Trade data in its raw form is tick by tick data, where each tick represents a trade. It is very useful, but it has far too much noise. OHLC data created using this method is the standard input format forpython backtesting, once you have this conversion in place, the Quantra course on Backtesting Trading Strategies shows you exactly how to feed it into a complete strategy testing framework. In this blog, we convert this tick by tick (TBT) data into an OHLC (Open, High, Low, and Close) format using the resample function of the Pandas library.

We cover:

What is Tick by Tick Data?

What is OHLC Data?

Converting tick by tick data to OHLC dataStep 1 - Import pandas packageStep 2 - Load the dataStep 3 - Resample the data

Step 1 - Import pandas package

Step 2 - Load the data

Step 3 - Resample the data

What is Tick by Tick Data?

Before we go any further let's understand what tick by tick data is. A single transaction between a buyer and a seller is represented by a tick.

In other words, when a buyer and a seller do the transaction of the number of stocks on an agreed-upon price, it is represented by a tick. Multiple transactions of this type can happen under a second and each of them would be represented by a tick.

The tick by tick data looks like this.

The first column of the data is the date and time at which the trade occurred. The second column is the last traded price (LTP) and the third column is the number of bitcoins traded in that particular transaction that is the last traded quantity (LTQ).

And the last column is the exchange code. For this tutorial, we will use the bitcoin data of the fourth of February 2021. This data was downloaded fromFirstRate Data.

What is OHLC Data?

As we now know, the tick by tick data is very high-frequency data.What if we want to quickly check the moment of the price in 1 min, 10 mins or 1 day?

We would have to check each tick manually to check the price moment. This sounds burdensome, but it can actually be done very quickly if we summarise the data into open, high, low, and close prices.

Now we will walk through the whole process of converting the tick by tick data into OHLC format using the resample function from the pandas library.

Converting tick by tick data to OHLC data

One can convert tick by tick data to OHLC data using the following steps:

Step 1 - Import pandas package

Step 2 - Load the data

Step 3 - Resample the data

Step 1 - Import pandas package

Pandasis a popular Python package that is most widely used to handle tabular data. Pandas is used for important functions such as data wrangling, data manipulation, data analyses etc.

Step 2 - Load the data

Data is stored in my working directory with the name 'BTC_2021-02-04.csv'. We are setting the Date time column as the index. As we saw earlier, the data is without a header. Hence we would add the header to the data while importing it. Thus importing and adding header takes place in the same line of code.

This is what the data frame looks like:-

Step 3 - Resample the data

We will now use the resample method of the pandas library. The resample method allows us to convert tick by tick data into OHLC format. We shall resample the data every 15 minutes and then divide it into OHLC format.

If you want to resample the data into smaller timeframes (milliseconds/microseconds/seconds), use L for milliseconds, U for microseconds, and S for seconds.

A snapshot of tick-by-tick data converted into OHLC format can be viewed with the following line of code:-

You may concatenate ask and bid price to have a combined data frame.

Conclusion

This blog described a quick way of computing the OHLC using TBT data. This can be applied across different assets and one can devise different strategies based on the OHLC data.

We can also plot charts based on OHLC andgenerate trade signals. Some other ways the data can be used are tobuild technical indicatorsin python orcompute risk-adjusted returns.

Want to learn about algorithmic trading? Check out Quantra’s learning track onAlgorithmic Trading for Everyonewhich is a set of 7 courses and covers a wide variety of topics such as Day Trading, Machine Learning, etc. Be sure to check it out!

Note: The original post has been revamped on 6th June 2022 for accuracy, and recentness.

Disclaimer: All investments and trading in the stock market involve risk. Any decision to place trades in the financial markets, including trading in stock or options or other financial instruments is a personal decision that should only be made after thorough research, including a personal risk and financial assessment and the engagement of professional assistance to the extent you believe necessary. The trading strategies or related information mentioned in this article is for informational purposes only.

---

*Imported from QuantInsti Blog on 2026-04-27*
