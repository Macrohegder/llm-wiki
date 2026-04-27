---
title: "Candlestick Trading: A Momentum Strategy with Example"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/candlestick-trading-a-momentum-strategy-with-example-excel-model/"
date: "2022-06-27"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Candlestick Trading: A Momentum Strategy with Example

**来源**: [QuantInsti](https://blog.quantinsti.com/candlestick-trading-a-momentum-strategy-with-example-excel-model/)  
**日期**: 2022-06-27  
**作者**: QuantInsti

---

## 原文

Candlestick Trading: A Momentum Strategy with Example

ByChainika ThakarandAkshay Choudhary

Candlestick trading is a strategy in which the price on the previous ‘n’ candlesticks is observed and then you decide your next trade on the basis of that observation. Hence, if the price is increasing continuously for say, 3 candlesticks, then it is highly probable that it will rise further.

Candlestick charts patternsbasically show the high, low, open and close movements of a tradeable item, which can be a security, a derivative or currency.

Let us find out all about candlestick trading as a momentum strategy with this blog that covers:

What is momentum strategy?

Why does the momentum strategy exist?

Example of candlestick trading - momentum strategy in Excel

What is momentum strategy?

Momentum strategy implies the tendency of financial security to continue the price movement in a particular direction. The price momentum for an asset’s price can be either in an upward or in a downward direction.

For example, when Tesla began delivering cars in China on 14th February 2020, the closing price of Tesla kept rising till 19th February 2020.

On the contrary, the momentum can be in the downward direction as well. An example of a downward momentum is the oil price during the Covid-19 pandemic which kept plummeting with the Russia and OPEC oil war.

Why does the momentum strategy exist?

Momentum strategy seeks to profit from those securities which are trending and are backed by high volume. In simple words, buying high and selling higher is the main aim of this strategy. This can be achieved by taking positions in a stock that is going up or down, and then holding this position until the security shows signs of reversal.

Momentum traders may hold their positions for a few seconds, minutes, hours, months or even a couple of years, depending on how quickly the financial asset changes its direction.

Momentum trading carries a high degree of volatility compared to most other strategies. It is important to time the buys and sells correctly to avoid significant losses. Momentum traders usually make use ofstop losses, portfolio diversifications, and other risk management techniques to minimize the losses.

Now that we know the 'what' and 'why' of momentum trading strategy, watch this brief video to understand how it actually works.

Example of candlestick trading - momentum strategy in Excel

Now, let us see the example of candlestick trading with excel. This excel model will help you in:

Learning how momentum strategy is implemented

Understanding the trading logic of strategy implementation

Optimizing the trading parameters

Understanding intraday returns of momentum trading

​​In this example, we have taken the BTCUSDT data on the Binance exchange. Themomentum trading strategieswill be implemented on this asset. The data used for the BTCUSDT is 5 minutes candle data. The time interval of the data is from 12th December 2021 to 22nd December 2021.

Now, we would like to benefit from the market wave and optimize our bet by specifying stop loss and taking profit limits. This model is flexible and can be varied to achieve different limits to exit the trade depending upon the trader’s risk appetite.

Let us take a look at our assumptions now.

Assumptions

For simplification purposes, we ignore bid-ask spreads.

Prices are available at 5 minutes intervals and we trade at the 5 minute closing price only.

Since this is discrete data, squaring off of the position happens at the end of the candle i.e. at the price available at the end of 5 minutes.

Transaction costs would vary depending on the exchange. For the sake of simplicity, we have assumed it to be 0.

Also, we have some input parameters in place. Let us see those as well.

Input parameters

Please note that all the values for the input parameters mentioned below are configurable.

High/Low of 3 candles (one candle=every 5 minute price) is considered.

A stop loss of 50 and profit limit of 200 is set.

The market data and trading model are included in the spread sheet from the 12th row onwards. So when the reference is made to column D, it should be obvious that the reference commences from D12 onwards.

Column C represents the price for BTCUSDT.

Column D represents 3 candle high meaning the highest price of the previous 3 candles.

Column E represents 3 candle low meaning the lowest price of the previous 3 candles.

Column F calculates the trading signal.

The formula=IF(D13="", "", IF(C13>D13, "Buy", IF(C13<E13, "Sell", "")))means- if the entry in cell D13 is blank then keep F13 blank otherwise- if C13 (BTCUSDT price) is greater than D13 (3 candle high) then buy signal for the BTCUSDT is generated else- if C13 is lower than E13 (3 candle low) then sell signal for the BTCUSDT is generated.

Column G represents entry price. This is the price at which the trading signal is generated.

The formula=IF(H13=H12, G12, IF(OR(H13="Buy", H13="Sell"), C13, ""))means,- if the entry in cell H13 is same as H12 then the value in G13 should be the value in G12 otherwise,- if H13 is either “Buy” or “Sell” then the entry in G13 is the value in C13 (BTCUSDT price) else,- if H13 is neither “Buy” nor “Sell” leave it blank.

Column H represents the status of the trade. Given our assumptions and input parameters there are four status that can occur, “Buy”, “Sell”, “TP (Take Profit)” and “SL (Stop Loss)”.

The formula:

=IF(OR(H17="", H17="TP", H17="SL"), F18, IF(H17="Buy", IF(C18<G17+$C$4, "SL", IF(C18>G17+$C$5, "TP", H17)), IF(H17="Sell", IF(C18>G17-$C$4, "SL", IF(C18<G17-$C$5, "TP", H17)), "")))

Can be simplified as follows:

If the entry in H17 is either blank or TP or SL then choose the value in F18 (F column has either Buy or Sell or blank values). Otherwise, look into the next If condition.

If the entry in H17 is “Buy”, meaning we have a buy position, and if the price of the asset goes below the stop loss limit then we exit the position at stop loss and if the price of the asset goes above the take profit limit then we exit the position at take profit.

Similarly, if the position is “Sell” and the asset price rises above the selling price beyond the stop loss limit then exit the position at stop loss and if the asset price falls below the selling price beyond the take profit limit then exit the position by taking the profit.

Column I represents the profit/loss status of the trade. P/L is calculated only when we have squared off our position. The formula =IF(OR(H13="SL", H13="TP"), IF(H12="Buy", C13-G12, IF(H12="Sell", G12-C13, 0)), 0) can be summarized as follows:-

The first if condition states that proceed to the next if condition only if the corresponding status in column H is either “SL” or “TP” else the entry in the cell is zero.

The next set of if conditions calculate profit assuming either stop loss or take profit has been achieved. If the status in column H is “Buy”, then the profit/loss is calculated as C13-G12.

Remember that the column G has the price at which you traded (in this case “Buy”) and the column C has the market data for BTCUSDT. Hence the profit/loss is simply the difference between the price at which you sold minus the price at which you bought.

If the status in column H is “Sell”, then the profit/loss is calculated as G12-C13 simply meaning the difference between the price at which you sold (shorted) and the price at which you bought later thus squaring off the position.

Column J calculates the cumulative profit.

Outputs

The output table has some performance metrics tabulated. Loss from all the loss making trades is $35405 and profit from trades that hit TP is $41850. Sothe total P/L is $41850 - $35405= $6445.

Loss trades are the trades that resulted in losing money on the trading positions. Profitable trades are successful trades ending in gaining cause. Average profit is the ratio of total profit to the total number of trades which amounts to $13.45 as we have assumed transaction cost to be 0.

File in the download:

Excel Model - Candlestick Trading

Download

Conclusion

Trading candlestick patterns is a useful practice when it comes to observing the historical data before taking a trading position. When the price goes in a particular direction, the momentum can be observed well using the candlestick chart pattern with open, high, low, close values for the particular time period. You can enrol into our course onCandlestick Patterns Coursebased Automated Trading.

If you also wish to work with the momentum trading style, you must explore our course onMomentum Trading Strategies. With this course on momentum trading, you will learn to create time series andcross sectional momentum strategieson stock, stock indices, fixed income, and commodities futures. Also, you will learn to quantitatively analyze time series, portfolio returns and risks, and design and backtest momentum trading systems.

Note: The original post has been revamped on 27th June 2022 for accuracy, and recentness.

Disclaimer: All investments and trading in the stock market involve risk. Any decision to place trades in the financial markets, including trading in stock or options or other financial instruments is a personal decision that should only be made after thorough research, including a personal risk and financial assessment and the engagement of professional assistance to the extent you believe necessary. The trading strategies or related information mentioned in this article is for informational purposes only.

---

*Imported from QuantInsti Blog on 2026-04-27*
