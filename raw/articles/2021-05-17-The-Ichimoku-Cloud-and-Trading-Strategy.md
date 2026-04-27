---
title: "The Ichimoku Cloud and Trading Strategy"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/ichimoku-cloud-trading-strategy/"
date: "2021-05-17"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# The Ichimoku Cloud and Trading Strategy

**来源**: [QuantInsti](https://blog.quantinsti.com/ichimoku-cloud-trading-strategy/)  
**日期**: 2021-05-17  
**作者**: QuantInsti

---

## 原文

The Ichimoku Cloud and Trading Strategy

ByVibhu Singhand Ashish Garg

The Ichimoku cloud indicator is atechnical indicatorof Japanese origin and was aproprietary indicatorwith its Japanese formulator for around 30 years.

It involves calculating five lines of short to medium duration on the high, low and close of a security’s prices and plotting an area, between two of these five lines, better known asIchimoku cloud.

These lines help in determining the direction,momentumand support-resistance levels for thetime seriesdata. The Ichimoku cloud indicator also generates buy and sell trading signals and is usually plotted along withcandlestickto enable better decision making and clearer plots.

Calculations for the lines are simple and the time period chosen is somewhat arbitrary:

Tenkan Sen or Conversion Line: (20-period-high + 20-period-low)/2

Kijun Sen or Base Line: (60-period-high + 60-period-low)/2

Senkou Sen A or Leading Span A: (Base Line + Conversion Line)/2

Senkou Sen B or Leading Span B: (120-period-high + 120-period-low)/2

Chikou Span or Lagging Span: (Close of 30 periods ago)

The Direction Of The Price Action

The Ichimoku cloud is formed between the Leading Span A and Leading Span B and helps in determining the strength and direction of theprice action trading.

For example, the direction or trend of the price action is up when the prices are above the Ichimoku cloud. Similarly, the direction of the price action is down when prices are below the Ichimoku cloud and the direction is flat when the prices are somewhere in the Ichimoku cloud.

The Strength Of The Price Action

The Strength can be estimated using the difference between the Leading Span A and B lines. When the Leading Span A is increasing and above the other span line, the increase in the difference signifies strength in the uptrend.

It also means that the Ichimoku cloud is getting thicker. Similarly, the growth of the Leading span B over the other span line signifies strength in the downtrend and the thickness of the Ichimoku cloud increases again though in the opposite direction.

Python Code And Trading Strategy

ThePythoncode below loads the OHLC data for a cryptocurrency namedBitcoin.It then calculates, plots the various components and the Ichimoku cloud using thepandasandmatplotlibfunctionality.

Conclusion

Ichimoku cloud is also known asIchimoku Kinko Hyo. Ichimoku cloud is atechnical indicatorto gaugemomentum, trend and strength of the price action using five lines and a cloud. The indicator has crossover points, just like MACD, to determine buy and sell signals.

Other classicmomentum tradingindicators can also be used in conjunction with the Ichimoku cloud to produce clearer buy and sell signals. o complement the Ichimoku system with traditional quantitative indicators, our tutorial on how to buildtechnical indicators in Pythoncovers moving averages, Bollinger Bands, RSI, ATR, and volume-based indicators with full code examples.

New-age traders, programmers, analysts, who wish to ride the risingcryptocurrencymarkets should leverage the power of fast computing to identify rare trading opportunities and to automate your trading. Learn to use quantitative techniques taught by market practitioners in ourLearning Track: Cryptocurrency Trading for Quants.

File in the download:Ichimoku Cloud And Trading Strategy Python code

Login to Download

Disclaimer: All investments and trading in the stock market involve risk. Any decisions to place trades in the financial markets, including trading in stock or options or other financial instruments is a personal decision that should only be made after thorough research, including a personal risk and financial assessment and the engagement of professional assistance to the extent you believe necessary. The trading strategies or related information mentioned in this article is for informational purposes only.

---

*Imported from QuantInsti Blog on 2026-04-27*
