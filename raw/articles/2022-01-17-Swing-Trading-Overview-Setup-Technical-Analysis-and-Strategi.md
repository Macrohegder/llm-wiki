---
title: "Swing Trading: Overview, Setup, Technical Analysis and Strategies"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/swing-trading/"
date: "2022-01-17"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Swing Trading: Overview, Setup, Technical Analysis and Strategies

**来源**: [QuantInsti](https://blog.quantinsti.com/swing-trading/)  
**日期**: 2022-01-17  
**作者**: QuantInsti

---

## 原文

Swing Trading: Overview, Setup, Technical Analysis and Strategies

ByRekhit PachanekarandVibhu Singh

Are you a 100-metre sprint runner or a marathon runner? Or somewhere in between? Or both? When it comes to trading, swing trading lies somewhere between sprint and marathon.

So if you don't like running too fast or running for a longer distance, and you want to apply the same philosophy in trading, then swing trading is for you.

In this blog, we will focus on concepts of swing trading and create a swing trading strategy.

We will cover the following topics:

What is swing trading?

Swing trading vs Day trading

Swing trading setups

Which asset to trade in swing trading?

Which market to trade in swing trading?

Role of technical analysis in swing trading

How to create a swing trading strategy?

Advantages of swing trading

Disadvantages of swing trading

What is swing trading?

What is the first thing that comes to your mind when you look at these stock prices? Yes, the Apple stock price is going upward or rising and the Yes bank stock price is going downward or falling. But if you observe closely, the prices are moving upward and downward in a zig-zag pattern. These patterns are called swings.

When the price reaches a high level and then starts declining, it is called a swing high. Similarly, when the price reaches a low level and then starts moving upward, it is called a swing low.

Swing trading is the art of identifying these swing highs and swing lows and taking a trading position. Swing traders looking to automate their indicator calculations can follow our step-by-step guide ontechnical analysis in Python, which covers RSI, moving averages, and Bollinger Bands with full Python code and visualisations. The goal is to identify an overall trend and capture larger gains within it. For example, in the Apple stock price, you can take a long position when the price makes a new low which is around April 2020 and capture the gains.

Swing trading vs Day trading

Most people are confused between swing trading and day trading. Let’s understand the difference between these two and some of the properties of swing trading.

The main difference between swing trading and day trading is the holding period.Day tradingis the buying and selling of the security in a single trading day. For example, you open a buy position when the market opens and close the position at the end of trading day.

However, in swing trading you hold the position from days to weeks. What that means is you open a position today and close the position in a few weeks.

On the basis of timeframe, we can divide the trading style in two more types.

Positional trading:This is a long-term trading style where the holding period varies from months to years.

Scalping:Scalping is considered as short term trading where you open the position and close it within seconds to minutes.

Trading Style

Holding Period

Scalping

Seconds to minutes

Day Trading

Day only

Swing Trading

Days to weeks

Positional Trading

Months to Years

Day Trading

Swing Trading

Trading positions last a few hours or less. All trading positions should be closed at the end of the trading day.

Trading positions last days to weeks.

There is no overnight risk.

Overnight holding risks

Highly leveraged

Less leveraged compared to day trading

Capitalise on small price movements

Captures bigger price movements

Swing Trading Setups

You have understood that you need to find the swing highs and swing lows and capture the gains.

But how do you find the swing highs and lows?Will you visually inspect the swings or use candlestick patterns or some technical indicators?

The visual inspection can be erroneous so we won’t do that. Usingcandlestick patternsis also not an apt method as it is a kind of discretionary trading.

For example, the support and resistance levels for different traders can be different. Since it could lead to subjective analysis which is difficult to ascertain if it is successful or not, we won’t go down that road too.

We will go with the methods that have some mathematical backing. We will use technical indicators to identify swing lows and highs. Once we identify the entry points we also need to plan for an exit. We can use stop loss and take profit for exiting the strategy.

You will also need to select the asset on which you want to implement the swing trading strategy.

Which asset to trade in swing trading?

You can pick the assets from:

stocks,

commodities,

futures,

bonds, and

currencies andcryptocurrencies.

To build on your basics, consider an intermediatecrypto trading coursethat focuses on strategies like calendar anomalies, Ichimoku Cloud, and Aroon.

As a swing trader, you must create a diversified portfolio. You should have at least ten different positions, and they should be in different sectors. And if you can, incorporate other asset classes in your swing trading.

For example, include the following (assuming these securities meet the fundamental and technical criteria of your strategy):

technology stocks,

developed market equities,

emerging market equities,

ETFs, and

Physical Gold.

But too much of a good thing can harm you. It’s possible to diversify too much — holding, say 30 or more positions. A swing trader needs concentration to make large profits. The more positions you hold, the closer the returns of the portfolio will be to the market.

All of these positions represent different ways to diversify your portfolio. Holding more than one position reduces idiosyncratic risk (a fancy way of saying the risk attributable to an individual position). And diversification allows your portfolio to withstand market volatility — the gains from a few positions can offset the losses from others.

Which market to trade in swing trading?

Swing trading can be used in any market as long as there are identifiable swings in the assets’ price graph. But it is seen that swing trading is most beneficial when the market is trending.

Think about it. You might have a long-only swing trading strategy. And you identified a swing low too late and the price already increased by the time you entered the trade. But since you have an idea that the market is trending, the risk of taking a loss is minimised.

Role of technical analysis in swing trading

We briefly talked about identifying swing lows and highs in the earlier section. How do you identify these swings? The answer is technical indicators.

But can any technical indicator be used?Not exactly?

Since we want to trade the swings in a trending market, we will use trending indicators to identify these swing lows. One of the simplest technical indicators to use is the moving averages.

You can also use:

Moving average convergence-divergence (MACD) indicator,

Williams’ fractal,

Stochastic indicator,

RSI indicator,

On balance volume (OBV) etc.

Now you must be thinking,should you use only one technical indicator?

Actually, you can use a combination of two or three indicators if you want to be sure of the trading signals generated. If you are using two indicators and both give you the buy signal, you will have more confidence in going long, than if only one was used.

However, if you use more indicators, your trading signals might reduce. This is why we try to limit the number of technical indicators to use for swing trading.

How do you trade the swings?

Let’s try to list down the steps you need to create a swing trading strategy.

How to create a swing trading strategy?

Before you create a swing trading strategy, you should decide which assets you want to trade. Preferably, you can select trending stocks such as Apple, Tesla. Not limited to stocks, you can also look at commodities as well.

Once you have selected the stocks, you can decide on the technical indicators which you will use. In our course on swing trading, we have used the MACD and the Williams fractal as our choice.

A strategy should always be thoroughly backtested before you plan on going live. Make sure that you have historical data of the assets you plan on trading. For example, if you want to trade Apple, you can download the daily historical data for the past 10 -15 years. You can even look at minute timeframe data if you want a closer look at the asset prices.

Once you have the required historical data, you can set the rules of the strategy. The first thing you will do is plan your entry rule.

If you are using the MACD indicator, your entry rule would be to buy when the MACD line crosses the signal line and goes above the signal line.

Apart from the entry rule, the exit rules are equally important. One exit rule will be dependent on your choice of indicators. If you are using the MACD indicator, you can exit when the MACD line goes below the signal line.

You should also have exit rules based on the take-profit and stop-loss levels. Swing traders look for small profits which add up in the long run. So if your asset gives 4% returns, the swing trader will exit the trade.

Also, if your asset price goes in the negative and crosses 2% loss, the swing trader will exit the trade. The take profit and stop loss levels can be decided on your risk to reward ratio. For this example, it was a 1:2 risk-reward ratio. This ratio is subjective and depends on the individual's risk appetite.

Apart from the above exit criteria, swing traders will typically exit the trade after a month, irrespective of the profit or loss. Recall that swing traders don’t stay in a trade for a long time.

Thus, in this way, you can define the entry and exit rules for your own swing trading strategy.

However, swing trading carries some risks too. Let’s find out the advantages and disadvantages in the next section.

Advantages of swing trading

The advantages of Swing Trading are as follows:

Swing trading carries less risk if you are trading in a trending market

It is a simple strategy that is used by beginners

Unlike day traders, you don’t have to close the trade by end of the day

You don’t have to sit in front of the computer all day long to keep a track of the market

Disadvantages of swing trading

The disadvantages of Swing Trading are as follows:

There is a gap risk. For example, if negative news about the company is disclosed after market hours, there can be a steep decline the next day and result in considerable loss

The technical indicators used should be studied in detail to examine their inherent shortcomings

Conclusion

Swing trading strategies are used by beginners as well as experienced traders. The underlying logic is relatively simpler to understand and implement.

But like any other trading strategy, swing trading strategies are not risk-free and you have to be careful on the choice of technical indicators as well as the parameters set for entering and exiting the trade.

As a start, you can always check the swing trading strategies course on Quantra to understand as well as learn to implement it in the live markets. To find out more about swing trading strategies, explore our course onSwing Trading Strategies.

Disclaimer: All investments and trading in the stock market involve risk. Any decision to place trades in the financial markets, including trading in stock or options or other financial instruments is a personal decision that should only be made after thorough research, including a personal risk and financial assessment and the engagement of professional assistance to the extent you believe necessary. The trading strategies or related information mentioned in this article is for informational purposes only.

---

*Imported from QuantInsti Blog on 2026-04-27*
