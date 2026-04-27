---
title: "yfinance Library | Download Forex Price Data | Python"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/download-forex-price-data-yfinance-library-python/"
date: "2022-05-30"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# yfinance Library | Download Forex Price Data | Python

**来源**: [QuantInsti](https://blog.quantinsti.com/download-forex-price-data-yfinance-library-python/)  
**日期**: 2022-05-30  
**作者**: QuantInsti

---

## 原文

yfinance library: Download Forex Price Data using Python

ByJosé Carlos Gonzáles Tanaka

You will find many sources to download forex price data on the internet, such asQuandl Python API, Alpha Vantage, brokers' APIs, Yahoo Finance, etc. Today, we will teach you how to fetch forex price data using the yfinance library in Python, allowing you to access a wide range of financial information.

With yfinance, historical forex data download at different frequencies is possible. From getting daily forex data to getting minute forex data using Python, make yfinance library a versatile tool for financial data analysis. If you're looking to incorporate forex data into your Python projects, understanding the capabilities of the yfinance library can be immensely beneficial.

I know what you’re thinking:“There are plenty of websites explaining how to download stock price data with the yahoo finance library but almost nothing on how to download forex price data with it”.

We all know the stock market is a great place to invest in. However, when you have a good strategy, forex assets can help you earn a decent amount of money. As an algo trader exploring this amazing market, the yfinance library will helps us to download forex price data easily.

We cover:

yfinance Library Installation

Import Libraries

Daily Forex Price Data using yfinance

Minute Forex Price Data using yfinance

Daily Data of Two Forex Pairs using yfinance

yfinance Library Installation

It’s so easy! Before we get into the download part, don’t forget to install the yfinance library in your environment. You can do this with the following code:

The versatility of yfinance in Python makes it a robust tool for efficiently obtaining and analyzing financial data. Let's see how!

Import Libraries

Now let’s download the EURUSD pair from the first business day of the year 2019 to March 11, 2022, in just 1000 lines of code. We’re kidding! Let’s start by importing the necessary libraries likenumpy,pandasandmatplotlib- which we are going to use for this article:

Let's see how to download daily data first.

Daily Forex Price Data using yfinance

To download forex price data, we can proceed using the “.download()” method from the yfinance library in the same way you did when you downloadedstock price data.

Inside the parenthesis, you need to provide the asset to the ticker parameter, and the start and end dates to select the period range. Next, we format the dataframe index as a datetime object and, finally, we show the last 5 observations of the sample data.

Datetime

Adj Close

2021-12-27

1.132387

1.133500

1.130416

1.132426

1.132426

2021-12-28

1.132978

1.133600

1.129038

1.133003

1.133003

2021-12-29

1.131337

1.137001

1.127536

1.131478

1.131478

2021-12-30

1.135976

1.135976

1.130071

1.136015

1.136015

2021-12-31

1.132323

1.137915

1.130506

1.132503

1.132503

Contrary to stock prices, Adj Close and Close values are actually the same since in forex there aren’t dividend payments or splits. Both of them can be used interchangeably.

In addition, as you see, the “Volume” time series results to be zero since in Forex spot data, there is no volume provided by any broker.

Plot the Close Price

Let’s plot our EURUSD close prices so we could have a better idea of its behaviour:

As it happens to most asset prices, the EURUSD price series looks like arandom walk.

Did you notice something about the frequency?Yes, even though we didn’t specify anything about this, the download method gives us the price series in daily frequency by default.

Minute Forex Price Data using yfinance

Whenever you want to download forex price data with a different frequency, we make use of the following code:

Datetime

Adj Close

22-04-22 22:25:00

1.080264

1.080264

1.080264

1.080264

1.080264

22-04-22 22:26:00

1.080264

1.080264

1.080264

1.080264

1.080264

22-04-22 22:27:00

1.080264

1.080264

1.080264

1.080264

1.080264

22-04-22 22:28:00

1.080264

1.080264

1.080264

1.080264

1.080264

22-04-22 22:29:00

1.080264

1.080264

1.080264

1.080264

1.080264

We specify the frequency with the parameter “interval”. Besides, we choose the last 5 days by setting “5d” to the period parameter.

Plot the Minute Close Price

Now, you want to graph this data, right?

Once we run the function, we graph our EURUSD minute data:

Easy, right?Now let’s see how to download two forex pairs, from which you can deduce how to download more than this number of pairs.

Daily Data of Two Forex Pairs using yfinance

We will use the same method, but pay attention to the code lines:

GBPUSD = X

Datetime

Adj Close

2021-12-27

1.340520

1.344070

1.339226

1.340430

1.340430

2021-12-28

1.344447

1.346257

1.341832

1.344267

1.344267

2021-12-29

1.343400

1.349928

1.340914

1.343328

1.343328

2021-12-30

1.349764

1.352155

1.345533

1.349879

1.349879

2021-12-31

1.349892

1.354848

1.346747

1.349837

1.349837

EURUSD = X

Datetime

Adj Close

2021-12-27

1.132387

1.133500

1.130416

1.132426

1.132426

2021-12-28

1.132978

1.133600

1.129038

1.133003

1.133003

2021-12-29

1.131337

1.137001

1.127536

1.131478

1.131478

2021-12-30

1.135976

1.135976

1.130071

1.136015

1.136015

2021-12-31

1.132323

1.137915

1.130506

1.132503

1.132503

Do you see?You just need to pass the forex pairs inside a list. Besides, we make use of the “group_by” parameter to specify that, since now you have the columns as a multiindex, we want the first multiindex level to be the asset category, and the second level as the OHLC columns.

Plot the Two Forex Pairs

To plot the two forex pairs for the daily data acquired above, refer the following code and the graph below it:

Conclusion

With this tutorial we have learnt how to download forex price data in Python with the yfinance library. We learnt how to download daily forex data and minute forex data and you will now be able to download forex data using Python with any frequency that you'd like.

Besides, now you know how to plot a single series or two forex price series. You can also deduce how to plot more than two price series. For future applications, you may try Python for forex and backtesting. You can always catch the official yfinance documentationhere.

But, why not learn more about the Forex world? You can join theforex trading courseby Quantra and start having fun in the algo trading domain! The course comes highly recommended for both beginner and expert Forex traders and isavailable for FREE! Enroll now!

In addition to forex data, the yfinance library is a powerful tool for working with futures data. For detailed guidance on utilizing it for this purpose, refer to this comprehensive tutorial onyahoo futures.Ready? Set? Go Algo!

Author:José Carlos Gonzáles Tanaka

Disclaimer: All investments and trading in the stock market involve risk. Any decision to place trades in the financial markets, including trading in stock or options or other financial instruments is a personal decision that should only be made after thorough research, including a personal risk and financial assessment and the engagement of professional assistance to the extent you believe necessary. The trading strategies or related information mentioned in this article is for informational purposes only.

---

*Imported from QuantInsti Blog on 2026-04-27*
