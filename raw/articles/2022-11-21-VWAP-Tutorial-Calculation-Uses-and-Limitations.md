---
title: "VWAP Tutorial: Calculation, Uses, and Limitations"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/vwap-strategy/"
date: "2022-11-21"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# VWAP Tutorial: Calculation, Uses, and Limitations

**来源**: [QuantInsti](https://blog.quantinsti.com/vwap-strategy/)  
**日期**: 2022-11-21  
**作者**: QuantInsti

---

## 原文

VWAP Tutorial: Calculation, Uses, and Limitations

ByChainika Thakar

Usually if a trader had to compare two seemingly good securities, an experienced trader would check both the price and the volume of the stock.

Now, you would ask, “Price is obvious, but why the volume?”

Volume is as important as the price because we don’t want to get stuck with a stock which has only a few takers, even if the price is too attractive. Thus, the VWAP was created to take into account both volume as well as price.

With VWAP as the measure of a trade, a potential trader would decide the long and short positions more accurately than if it were just the price taken into consideration.

Let us find out more about VWAP with this blog as it covers:

What is VWAP?

Formula of VWAP

Application of VWAP in Excel

Trading with VWAP - The interpretation

How to use VWAPVWAP as a confirmation of trendVWAP as a trader execution strategyVWAP as an indicatorVWAP as a check of profitability

VWAP as a confirmation of trend

VWAP as a trader execution strategy

VWAP as an indicator

VWAP as a check of profitability

VWAP vs MVWAP

Pros of using VWAP

Cons of using VWAP

What is VWAP?

The volume-weighted average price, also known as VWAP, is the way to measure the average price of a financial instrument adjusted for its traded volume.

In simple terms, the Volume Weighted Average price is the cumulative average price with respect to the volume.

The Volume Weighted Average Price (VWAP) is simple to calculate and has a variety of uses. While ahedge fundor a mutual fund uses the VWAP to guide its decision to buy a substantial number of shares, a retail investor would use it to check if the price is good enough to go long.

Here's a quick tutorial of how VWAP trading strategy works and and understand how it calculates the average price, factoring in trading volume.

Formula of VWAP

The formula for calculating VWAP is the cumulative typical price multiplied by total volume and divided by the cumulative volume. It goes as follows:

VWAP = [Cumulative (Price * Volume)]/[Cumulative Volume]

While the formula is quite easy, let us also find out the VWAP application in Excel by going through an example.

Application of VWAP in Excel

To calculate VWAP, we will take the minute level data of Amazon. You can get sample historical data from Yahoo Finance. We have used the data for the date 29th December 2022. A sample of the data is as follows:

Step 1: Find the average or "Typical Price"

To get a reliable estimate of the price at which a security was traded for a given period, we take the average of the price data, in this case, the average of the high, low, and close price.

For example, the average price at 9:30 = (83.06 + 82.74 + 82.88)/3 = 82.89333333 ~ 82.89

Similarly, for 9:31, the average price = (82.98 + 82.65 + 82.9)/3 = 82.84333333 ~ 82.84

We will create a new column with the heading "Typical Price"

Step 2: Multiply the average price with the volume for that period

Since we are looking for a period of 9:30, the volume traded was 2107565.

Thus, the product of volume and typical price will be = (Average price * Volume) = 82.89333333 * 2107565 = 174703088.1

Similarly, we have populated the product of the typical price and volume in the column with the heading "Volume * Typical Price".

Step 3: Compute the cumulative total of the product of typical price and volume

At 9:30, as it is the first value, the cumulative total remains unchanged. Let's see the cumulative total of the product of typical price and volume for 9:31 now.

For the time, 9:30, the product of typical price and volume was 174703088.1. And for 9:31, the value was 21937660.26.

Hence, for 9:31, the cumulative total would be 174703088.1 + 21937660.26 = 196640748.3.

Accordingly, we will create a new column in the table as shown below.

Step 5: Find the cumulative total volume

Since we found the cumulative total of the typical price and volume, we have to keep a running total of the volume of the security traded.

Hence, for 9:30, it will just be 2107565 as it is the first period of the day.

For 9:31, it will be (Volume at 9:31) + cumulative volume of the previous period, i.e.

(264809 + 2107565) = 2372374

Step 6: Find VWAP

We simply divide the cumulative total of the product of typical price and volume by the cumulative volume.

Thus, for 9:30, VWAP = (174703088.1) / (2107565) = 82.89333333 ~ 82.89

For 9:31, VWAP = (196640748.3) / (2372374) = 82.88775224

We will finally create the column "VWAP" which shows the final calculations

Trading with VWAP - The interpretation

With VWAP, the trader gets the integral information regarding the stock’s price movement that helps them determine the best entry point.

For instance, a trader waits for the price line of a particular stock to go above the VWAP line. In case there is a lot of selling (short positions) in the market for that stock, the stock may fail to break above the VWAP line.

This is because the stocks above VWAP line are considered to be expensive and hence, are at a high value. When the stock price is rising to go above the VWAP line, it implies that lot of traders are buying the stock. This is when the traders go long before the price reaches its peak.

On the other hand, the stocks below VWAP line are known to be undervalued and trend downwards making the traders go short on such stocks.

With the help of trend lines (support and resistance lines) andcandlestick pattern(representing price movement), a trader can find out when the stock moves above or below the VWAP line.

How to use VWAP

So far, we learnt about the calculation and application of VWAP with the help of Excel. Let us also see how VWAP can be used by the trader for a variety of reasons, which are as follows:

VWAP as a confirmation of trend

VWAP as a trader execution strategy

VWAP as an indicator

VWAP as a check of profitability

VWAP as a confirmation of trend

We have mentioned before how VWAP gives us information related to both volume as well as price. It also helps us confirm the presence of a trend that might be emerging.

Let’s understand this with an example of a graph below (showing VWAP and the closing price of a stock) which can be plotted in Excel after your calculation is done.

If you see the graph for VWAP, despite the frequent swings in the closing price, we can clearly see that the VWAP is rising. The rising VWAP indicates that there are more buyers than sellers.

It also indicates a bullish phase, whereas, a declining VWAP indicates a bearish phase.

VWAP as a trade execution strategy

VWAP is also used by institutional buyers who need to buy or sell a large number of shares but do not want to cause a spike in the volume as it attracts attention and affects the price.

To explain this further, let’s say an institution is interested in buying 10,000 shares of Amazon. If they put an order of 10,000 the immediate action would be a spike in the price as the exchange fills the order.

Now, if other traders know that there is a significant demand for the share, they would ask for a higher price for the stock making it more expensive for the institution.

To avoid this scenario, these institutions develop an automated trading strategy to divide the number of shares into smaller amounts and bid for the shares in such a way that their trades do not let the closing prices go far from the VWAP.

Since VWAP acts as a guideline on which certain traders base their trading decisions on, it helps to keep the closing price as close to the VWAP as possible.

VWAP as an indicator

Among intraday traders, the VWAP indicator can be used in a trading strategy too. There are conflicting theories on how exactly you should use the VWAP as an indicator, and thus we will try to understand this aspect in greater detail.

We usually consider scenarios when the closing price crosses the VWAP as a signal, and thus, a VWAP cross can be used to enter or exit the trade depending on your risk profile.

Before we look at the different scenarios, let’s step back and understand that VWAP can actually be self-fulfilling when it comes to traders. As seen previously, certain institutional traders would try to execute trades in such a way that the closing price doesn’t go farther than the VWAP.

This can influence other traders who would look at the closing price and take a trading decision thinking that the closing price is bound to get close to the VWAP eventually.

Hence, when the closing price starts moving up and further from the VWAP, there is pressure among the traders to sell, due to the logic that the other would sell at any time.

This creates a situation where the general belief might be that the stock is overvalued. Similarly, when the closing price starts moving down and further from the VWAP, there is a belief that the stock is undervalued and there is pressure among traders to buy the stock.

In this way, we can call VWAP self-fulfilling. Of course, depending on the mindset of the market, there can be different scenarios and thus, one cannot depend on VWAP alone to make a trading decision.

Let us now look at a few other scenarios.

Some traders prefer the VWAP cross as an indicator and buy the stock when the closing price crosses the VWAP from below and climbs higher, indicating a bullish trend.

One will then either wait for the closing price to reach the high of the day at which point they sell and exit the trade. Other traders will exit as soon as the closing price shows signs of reversing.

Conversely, some traders would short the stock when the closing price crosses the VWAP from above and keeps going down. Once the closing price reaches the low of the day, they would then close the trade.

Now, some traders would prefer a price below VWAP as it would be a good price to buy and a price above VWAP could indicate that it is a good time to sell. Taking the previous example of the VWAP graph, you can see as the price goes above the VWAP there is a small period where the price keeps increasing and then the price decreases.

It is however seen that for the trading strategy, traders consider the crossover of the closing price with the VWAP as a signal. However, one should note that the VWAP is a lagging indicator, which means that it is computed solely based on historical data. Therefore it should not be the sole indicator in a trading strategy.

VWAP as a check of profitability

Once traders have closed their trade, they look at the VWAP to check if their trade was profitable or not. For example, if a trader had bought a share of Amazon at $248 and the VWAP at the end of the day was $250, then the trader actually bought the stock at a good price and can make a profit on this trade.

We have so far seen some of the uses of VWAP. However, while going through the article, did you feel some sort of deja vu or rather did you realise that you have read about similar characteristics for a different indicator?

Do you think VWAP is just another variation of amoving average? To answer this question let’s look at the difference between VWAP and Moving VWAP (MWAP).

VWAP vs MVWAP

The following are the differences between VWAP and MVWAP:

Moving VWAP is a moving average line that visually represents stock price movement. It tracks end of the day VWAP over a certain period of time.

VWAP represents the average price adjusted for the traded volume usually during a particular day.

MVWAP gives an average of the number of VWAP calculations to analyze. This means that MVWAP can run from one day to the next, giving an average of the VWAP value over a period of time.This makes the MVWAP much more customisable as it is tailored to suit specific needs. It can also be made much more responsive to market movements for short-term trades, and also, it can smooth out market noise if a longer period is chosen.

VWAP will provide a running total throughout the day. Thus, the final value of the day is the volume-weighted average price for the day.For example, if using a one-minute chart for a particular stock, there are 390 (6.5 hours X 60 minutes) calculations that will be made for the day, with the last one providing the day's VWAP.

MVWAP looks similar to VWAP but not as smooth as VWAP. It implies that there are more sudden changes in MVWAP, owing to the longer period of data it undertakes.

VWAP is a much smoother line and there are way lesser sudden changes in the data it builds on.

Hence, although there is a thin line between MVWAP and VWAP, but the thin line also represents the significant difference.

Pros of using VWAP

Coming to the pros, I must mention that the volume-weighted adjusted price is the true average price of the stock and does not affect its closing price.

Let us see the reasons that VWAP is so popular for:

VWAP can indicate if the market is bearish or bullish:The market is bearish when the price is below the VWAP and bullish if the price is above the VWAP. A bullish market indicates a buying pressure, and the trend line on the chart moves upward. A bearish market indicates selling pressure, leading to a downward trend on the stock chart.

In VWAP, the indications to buy and sell are prominent:The traders who use the VWAP line as an indicator will be able to buy at a low price, thus, getting more favourable returns when they sell the stock. Hence, VWAP helps the investor make an informed decision.

VWAP can be utilised along with moving average and other trading strategies and indicators:The VWAP is a great indicator when choosing what stocks to buy, but it provides greater value when used with other trading strategies. VWAP can tell you a lot about the current and future state of stock for both long and short positions.

Also, VWAP can be combined with another technical indicator to confirm a trend, using such multiple indicator strategies can considerably reduce the number of false signals.

Cons of using VWAP

VWAP is a lagging indicator and thus, if you try to use it for more than a day, it will not be able to portray the correct trend. Thus, it should be used only by intraday traders.

Furthermore, there are cases where certain stocks (or the market itself) are in a strong bullish phase and thus there will be no crossovers for the entire day, which in turn portrays very little information to the traders as well as institutions.

In a way, the major drawback of VWAP is it cannot be used for more than a day, and thus, it is not able to provide much information from a historical point of view.

Conclusion

VWAP is a combination of both price and volume, and thus offers a valuable set of information to the traders, compared to the moving averages. Calculating VWAP sounds complicated but is quite simplified and that is what we discussed earlier in this blog.

Also, interpreting VWAP when used alongside the closing price is quite simple. Keeping in mind that the VWAP is a tool for making decisions regarding going long or short, one can use the VWAP method successfully.

You can learn more about technical indicators and build your own trading strategies using Python with the courseTechnical Indicator Strategies in Python.

Note: The original post has been revamped on 21st November 2022 for accuracy, and recentness.

Disclaimer: All investments and trading in the stock market involve risk. Any decision to place trades in the financial markets, including trading in stock or options or other financial instruments is a personal decision that should only be made after thorough research, including a personal risk and financial assessment and the engagement of professional assistance to the extent you believe necessary. The trading strategies or related information mentioned in this article is for informational purposes only.

---

*Imported from QuantInsti Blog on 2026-04-27*
