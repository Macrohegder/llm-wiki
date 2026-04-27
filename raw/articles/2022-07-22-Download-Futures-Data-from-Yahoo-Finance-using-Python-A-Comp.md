---
title: "Download Futures Data from Yahoo Finance using Python: A Complete Guide"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/download-futures-data-yahoo-finance-library-python/"
date: "2022-07-22"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Download Futures Data from Yahoo Finance using Python: A Complete Guide

**来源**: [QuantInsti](https://blog.quantinsti.com/download-futures-data-yahoo-finance-library-python/)  
**日期**: 2022-07-22  
**作者**: QuantInsti

---

## 原文

Download Futures Data with Yahoo Finance Library in Python

ByJosé Carlos Gonzáles Tanaka

The first thing you must do to code a futures strategy is to learn to download futures data in Python! This blog explains the complete process and helps you gain an understanding of the various steps required.

Futures tradingis inherently leveraged. One has to be cautious while using leverage in a portfolio. A good way to manage leverage is to trade algorithmically, and that is where this blog will be of importance.

It covers:

Yahoo! Finance Library Installation

Import Libraries

Download Futures Data

Plot the Close Prices

Download Data for Multiple Futures

Plot Multiples Futures Data

Yahoo! Finance Library Installation

Python is one of the easiest programming languages in the world. Python makes it easy for new learners to acquire programming skills quicker. It is also quite easy toset up your own Python trading system.

We are going to use aJupyter notebook. Let’s code! In case you haven’t already installed this famous library in your machine, here you have the code:

Import Libraries

So now, we want to import a library for data visualisation. We can use “matplotlib”. This library is the most used library in Python for this purpose.

In case you are new to this library, do you think we are going to leave you alone on this? No way! Please have a look atmatplotlibbefore you dive into our next code.

We now want to import the two libraries. Here’s the code:

Download Futures Data

Before you dig into the manypossibilities that futures tradinghas to offer, do note that, in the yahoo finance library, you will find continuous futures data. Futures are offered in the market for specific dates and due dates.

However, you can join all the futures in a single data line and this is called Futures continuation. You should also be aware ofcontinuous futures contract.

For now, you just need to call the download method, and inside the parenthesis pass the ticker_symbol (of the futures contract) as “ticker_symbol = F”, the start date, and the end date to specify the span of the dataset. The list provided in thisarticlewill help you to find the correct symbol for the futures asset you want to download.

For illustration, let us fetch the continuous platinum futures with the symbol “PL=F”. We select the 2017-2021 span. We change the index column to datetime type keeping in mind that this will later be used for graphical visualisation and manipulation. Lastly, we present the last five rows of the dataframe.

Adj Close

Volume

2021-12-27

968.90

968.90

968.90

968.90

968.90

2021-12-28

979.10

979.10

979.10

979.10

979.10

2021-12-29

968.20

968.20

968.20

968.20

968.20

2021-12-30

967.30

971.00

955.80

963.60

963.60

2021-12-31

962.50

965.30

949.60

964.40

964.40

This is a futures contract for which the underlying asset is a commodity. There are futures for currencies, stocks, interest rate futures,index futures, etc.

Plot the Close Prices

Now let’s plot the Gold Futures close prices so we can have a better idea of its price trends:

Download Data for Multiple Futures

Let’s do something else. Let’s download the Gold (GC) and Copper (HG) Futures data for the period 2020-2021. To fetch more than one asset, you just need to put the futures tickers inside brackets. We use brackets since to download two or more assets you need to pass the ticker names together as a list.

Data columns will be presented by asset and then by type of price. For this, we just grouped the data first by ‘tickers’ with the group_by method. Let’s code:

Adj Close

Volume

2021-12-27

1810.00

1812.10

1807.00

1808.10

1808.10

2021-12-28

1812.00

1818.00

1805.50

1810.20

1810.20

2021-12-29

1803.20

1805.10

1791.40

1805.10

1805.10

2021-12-30

1801.70

1816.00

1796.00

1812.70

1812.70

2021-12-31

1825.10

1827.80

1821.40

1827.50

1827.50

Adj Close

Volume

2021-12-27

2021-12-28

2021-12-29

2021-12-30

2021-12-31

Plot Multiples Futures Data

Time to visualise right? Since both futures data have different value ranges, we are going to plot one of them on a secondary axis:

Conclusion

You have learnt here how to download data for single and multiple futures assets. And you also know now how to plot them. In case you want to fetch futures data for more than two contracts, you just need to increase the tickers list in the yahoo finance download method by the futures you want to. Try doing it!

If you too want to take the next step in your algorithmic trading journey, subscribe to our great course onFutures Tradingand learn how you can deploy interesting strategies on the data that we fetched.

Ready? Set? Go Algo!

Disclaimer: All investments and trading in the stock market involve risk. Any decision to place trades in the financial markets, including trading in stock or options or other financial instruments is a personal decision that should only be made after thorough research, including a personal risk and financial assessment and the engagement of professional assistance to the extent you believe necessary. The trading strategies or related information mentioned in this article is for informational purposes only.

---

*Imported from QuantInsti Blog on 2026-04-27*
