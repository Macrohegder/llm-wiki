---
title: "Cryptocurrencies Trading Strategy With Data Extraction Technique"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/cryptocurrencies-data-strategy/"
date: "2017-09-26"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Cryptocurrencies Trading Strategy With Data Extraction Technique

**来源**: [QuantInsti](https://blog.quantinsti.com/cryptocurrencies-data-strategy/)  
**日期**: 2017-09-26  
**作者**: QuantInsti

---

## 原文

Cryptocurrencies Trading Strategy With Data Extraction Technique

ByVarun Divakar

There are many sources for getting data for the various cryptocurrencies available on the net. Sources such asQuandl Python API, Coinmarketcap, Poloniex etc. Most of them have an API or .csv feature available with them. Using which you can fetch the data. Today, we will see how to fetch this data with a minute resolution using python.

In this blog, I have used the python library coinmarketcap to fetch the data from the websitehere

I will also discuss how to save the data in a dataframe and csv. In the end, I have explained a simple strategy to trade the coins.

First, let us import the necessary libraries

You can pip install all the libraries above:

pip install pandas

pip install datetime

pip install coinmarketcap

Next, we will fetch the data using the Market function from above. Then we will get the names of various cryptocurrencies listed and save them in a list called coins_list.

Let us just print this list to see all the names in it.

We have a total of 1121 currencies on this list.

Next, we will get the start time and save it. This is the time at which we will run this script.

Next, we create two dictionaries with the names usdprice and usdvol. These will be used to store the data of all the 1121 coins.

Let us say that I want to get the data for the next 3 minutes, so let us save this time as a variable ‘t’.

After this, I will ping the coinmarketcap site every minute to fetch the data and then save it as a dataframe. I will keep doing this for the next ‘t’ minutes.

After this, we create two dictionaries that will have the coin names as their keys and USD price and volume traded as their values. We add these values to the corresponding dictionaries usdprice and usdvol with the time of fetching the data as their keys.

After this, we will calculate the time it has taken for the loop to run through all the currencies. This is important, as the runtime crosses the 1-minute mark, your next data fetch will happen at the next minute. So, if our data processing takes more time, we may need to drop some currencies which are not important or not tracked by us to make the data continuous.

I will explain this in detail now. If you run the code until this point the output would look like this.

You can print the two dictionaries usdvol and usdprice to see how the data looks like.

If we convert this data into a dataframe for a better view:

Now, print the dataframe ‘a’

Now, observe the time stamp on the left, it has a time delta of 2 minutes, this because when we wrote the code, we specified that the data should be fetched whenever a minute is completed. As, we observed the time for the loop was more than a minute so the data was fetched at the beginning of the minute after that. Hence, we need to reduce the currencies to be traded.

Once this is done, we can save this data in an excel for further backtesting.

Once you have your initial data, you can simply append the data fetched every minute to this.

Cryptocurrency Trading Strategy:

In markets likeBitcoin, which are highly volatile, it will be advisable to trade with the trend. But this does not mean that some well thought out and balanced mean-reverting strategies, such as the Long-Short portfolio, IndexArb ( create an index of your own) etc cannot be applied to bitcoin. To know about such strategies you can check out our course onMean Reverting Strategies by Dr. E. P. Chan.

Here, I have used a simple ‘Follow the Herd’ strategy. The basic premise of this strategy is that when markets are highly volatile, it is profitable to follow the existing trend in the market, by observing the direction of the trades happening. The volume data that we saved in the dataframe ‘b’ earlier will help in filtering the real breakout from the fake breakout. We compare the volume traded in a candle with the mean of the past ‘n’ candles to check if the sudden spike in the price is associated with an increase in the volume. If so, then we assume this to be a real breakout and trade along with the direction of the movement. Conversely, if the volume traded is less than the average volume but the return is more than the standard deviation of past ‘n’ returns then we assume this to be a fake breakout and trade against the direction of the movement.

To complement strategies that analyze breakout volumes, consider acrypto trading coursethat covers techniques like calendar anomalies, RSI, and the Ichimoku Cloud for improved trading insights.

Now coming to the strategy. First, let us import the necessary libraries.

Next, we import the data that we stored earlier.

Let us chose a symbol from all the currencies to trade and save it as the variable ‘s’. ( Try some liquid currencies such as BTC, ETH etc, as the strategy is dependent on volume traded)

Next, we create a dataframe ‘data’ that holds the price and volume information of ‘s’.

Next, we decide on the time period to calculate the standard deviation of returns and average volume traded.

In this case, I assumed this window to be 30.

To apply the strategy we need to know the returns, so let us first calculate that, and then compute the standard deviation of returns and average volume.

Next, we generate the column called ‘Signal’ and then we compute the signals where the return is more /less than the standard deviation observed and the volume is also higher than the average volume observed. According to our basic hypothesis, we assume this to be the real signal. That is the market is backing the move with volume.

Next, we create reversal signals, by going against the market trend whenever a breakout is not associated with a corresponding increase in volume.

After this, we create a new dataframe to hold only the alternating signals and drop the rest of them. We do this to reduce the trading noise. In essence, we hold a position until a counter signal is generated. And once we have the new signals ready we calculate the returns of the strategy.

Here we have calculated returns differently from the way did earlier as this return is the return we get when we execute the position based on the signal we generated from the past data. This return will show you the market behaviour after the point of entry.

Finally, we will plot a cumulative sum of the strategy returns to visualize the performance of the strategy.

This is a simple strategy and not advisable to be used for trading without a proper risk management in place. In the above graph, we did manage to capture one breakout successfully. If you want to reduce the number of trades significantly we can try increasing the time period or adding a multiple to the standard deviation factor in the signal. I have tried the same strategy on ETH ( Ethereum) and the result is promising.

This strategy is just for demonstration to people who are new to algorithmic trading and should not be traded without a proper risk management in place.

Next Step

An exhaustive look at some of the best Cryptocurrency trading platforms used by traders operating in international markets in our post 'Top 9 Cryptocurrency Trading Platforms'.

Disclaimer: All investments and trading in the stock market involve risk. Any decisions to place trades in the financial markets, including trading in stock or options or other financial instruments is a personal decision that should only be made after thorough research, including a personal risk and financial assessment and the engagement of professional assistance to the extent you believe necessary. The trading strategies or related information mentioned in this article is for informational purposes only.

Download Python Code

Cryptocurrency Trading Strategy - Python Code

Login to Download

---

*Imported from QuantInsti Blog on 2026-04-27*
