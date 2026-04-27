---
title: "Download Cryptocurrency Data in Python by Using Crypto Compare API"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/download-cryptocurrency-data-python-cryptocompare-api/"
date: "2022-07-20"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Download Cryptocurrency Data in Python by Using Crypto Compare API

**来源**: [QuantInsti](https://blog.quantinsti.com/download-cryptocurrency-data-python-cryptocompare-api/)  
**日期**: 2022-07-20  
**作者**: QuantInsti

---

## 原文

Download Cryptocurrency Data in Python by using Crypto Compare API

ByJosé Carlos Gonzáles Tanaka

How to use Cryptocompare API to download cryptocurrency data in Python? Cryptocompare is a cryptocurrency market data provider. And this blog explains how you can go about it with super easy simple steps and readies you to apply it whenever you want!

If you are taking your first step toward Algorithmic Trading or within the cryptocurrency world, then this article is for you!

We cover:

Why CryptoCompare?

Import Libraries

Set API Key

Fetch All Cryptocurrency Tickers

Download Historical Data With a Specific Frequency

Download Bitcoin Hourly Historical Data

Plot the Data

Why CryptoCompare?

CryptoCompare allows users to get live prices, graph them and make market research analysis from most of the important crypto exchanges. It also allows us to get limited free data for downloading. That’s what we’re going to do in this article.

Import Libraries

First, let’s install the cryptocompare library in ourJupyter notebook:

Now, we are going to import the following libraries: cryptocompare, pandas, datetime (only its datetime method) and matplotlib.

Are you familiar with the last two code lines of the ‘matplotlib’ library? Don’t worry at all! Please check our great article on the ‘matplotlib’ library to know everything about it.

Set API Key

The API Key is used to have a valid authentication for the user. It serves to identify your account and access an automated program.

To download the data, you will need to authenticate yourself on cryptocompare.com. First, you write your ‘cryptocompare_API_key’ and then you set the API key to the market provider. As the following:

Fetch All Cryptocurrency Tickers

You can do this easily. First, you get the ticker list, which is a dictionary. Then you transform the dictionary into a dataframe. Super easy, right?

ticker

ImageUrl

ContentCreatedOn

LIBERA

949640

/coins/libera/overview

/media/40484629/libera.png

1656515116

LIBERA

MINIFOOTBALL

949643

/coins/minifootball/overview

/media/40484630/minifootball.png

1656515517

MINIFOOTBALL

949646

/coins/cpo/overview

/media/40484632/cpo.png

1656516143

949648

/coins/cpad/overview

/media/40484634/cpad.png

1656516578

949651

/coins/sco/overview

/media/40484635/sco.png

1656517570

Download Historical Data With a Specific Frequency

Contrary to theyahoo finance library, in cryptocompare.com you have for each frequency a specific method to download data. Let’s explain to you this:

You can fetch the historical data for the ticker symbol you want. The historical data in daily, hourly and minute frequency levels are available.

Syntax:

# For daily data
cryptocompare.get_historical_price_day(ticker_symbol, currency, limit=limit_value, exchange=exchange_name, toTs=data_before_timestamp)

# For hourly data
cryptocompare.get_historical_price_hour(ticker_symbol, currency, limit=limit_value, exchange=exchange_name, toTs=data_before_timestamp)

# For minute data
cryptocompare.get_historical_price_minute(ticker_symbol, currency, limit=limit_value, exchange=exchange_name, toTs=data_before_timestamp)

Where:ticker_symbol: Ticker symbol whose data is requiredcurrency: Currency in which the price is quotedlimit_value: The maximum number of bars to fetch (max. value is 2000)exchange_name: The exchange to use when fetching the datadata_before_timestamp: Return the data before this timestamp (UNIX epoch time or a datetime object)

Returns:A dictionary containing the historical data.

Download Bitcoin Hourly Historical Data

For illustration purposes, let's extract the hourly historical data for the ‘BTC’ before 01-May-2021.

First, you define the ticker symbol, and then you specify that the asset price will be in dollars. Besides, since Cryptocompare establishes a limit to download data, we set the limit number of data points to return as ‘limit_value’.

We choose the ‘CCCAGG’ as the crypto exchange, which means we are going to download the aggregate prices that Cryptocompare has.

Next, we are going to use the ‘get_historical_hour’ function to download hourly Bitcoin prices.

Then, since the download information comes as a dictionary type, we transform it into a dataframe. In addition, we set the ‘time’ column as our index. Finally, the method provides the ‘time’ column as seconds, that’s why we not only change its string type to a datetime type, but also specify the ‘unit’ argument as ‘s’.

volume from

volume to

06/02/2021 21:00

4029627

4009247

4014136

126494

5.08675E+13

4009247

06/02/2021 22:00

4050397

3999196

4009247

168823

6.79449E+13

4004380

06/02/2021 23:00

4004419

3913217

4004380

429818

1.69581E+14

3926701

07/02/2021 0:00

3965158

3880271

3926701

398299

1.5625E+14

3960394

07/02/2021 1:00

3963317

3855738

3960394

262588

1.02679E+14

3870644

Plot the Data

So easy to get up to here, right? Let’s do the easiest from the easiest!

We code it:

And we plot it!

Conclusion

You now know how to download cryptocurrency data from Cryptocompare.com in Python. We promised you easiness and simplicity. You had it all in this short but useful tutorial. You can tweak the code to download more than one cryptocurrency.

We are glad you got this last section. And we are even more excited to tell you that you can take a step forward in your learning and enrol in ourCrypto trading courseon Quantra. It offers different strategies to backtest so,

What are you waiting for?Ready?Set?Go Algo!

Disclaimer: All investments and trading in the stock market involve risk. Any decision to place trades in the financial markets, including trading in stock or options or other financial instruments is a personal decision that should only be made after thorough research, including a personal risk and financial assessment and the engagement of professional assistance to the extent you believe necessary. The trading strategies or related information mentioned in this article is for informational purposes only.

---

*Imported from QuantInsti Blog on 2026-04-27*
