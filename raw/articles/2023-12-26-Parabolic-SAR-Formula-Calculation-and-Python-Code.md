---
title: "Parabolic SAR: Formula, Calculation, and Python Code"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/parabolic-sar/"
date: "2023-12-26"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Parabolic SAR: Formula, Calculation, and Python Code

**来源**: [QuantInsti](https://blog.quantinsti.com/parabolic-sar/)  
**日期**: 2023-12-26  
**作者**: QuantInsti

---

## 原文

Parabolic SAR: Formula, Calculation, and Python Code

In the dynamic realm of financial markets, technical analysis plays a pivotal role in guiding trading decisions and unravelling market trends. Among the arsenal of technical indicators, the Parabolic SAR (Stop and Reverse) stands out as a powerful tool for traders seeking to decipher trend directions and potential reversal points. The Parabolic SAR has gained prominence in trading stocks, commodities, and forex.

This indicator encapsulates key components such as trend direction and an acceleration factor (the rate at which SAR increases or decreases), making it an adaptable and versatile tool. The inclusion of an acceleration factor allows the SAR to dynamically respond to market shifts, a trait especially beneficial in capturing the momentum of trends.

Let us dive into the details of Parabolic SAR with this blog that covers:

What is Parabolic SAR?

Importance of Parabolic SAR in technical analysis for trading

How is Parabolic SAR calculated?

Parabolic SAR trading strategy using Python

Cons of Parabolic SAR

What is Parabolic SAR?

Parabolic SAR, which stands for "Stop and Reverse," is a technical analysis indicator used in financial markets to find out the potential trend reversals as well as for setting stop loss levels. It was developed by J. Welles Wilder, the same person who created other popular indicators like the Relative Strength Index (RSI Indicator), Average Directional Index (ADX) and Average True Range (ATR). If you want to see how Parabolic SAR fits alongside other widely used indicators like moving averages, RSI, and Bollinger Bands, our guide ontechnical analysis using Pythoncovers all of them with complete Python code in one place.

Here are the key components of parabolic SAR:

Trend direction

Acceleration factor

Trend Direction

As the line of the Parabolic SAR adorns price charts either above or below, they provide visual cues for discerning the underlying trend – an uptrend when below and a downtrend when above.

To put it in a nutshell, you can see how I have summarised it below along with the chart.

When the Parabolic SAR line is below the price, it suggests an uptrend (buy signal or going long).

When the Parabolic SAR line is above the price, it suggests a downtrend (sell signal or going short).

Acceleration Factor

The indicator incorporates an acceleration factor, denoted as AF, which determines the rate at which the SAR moves in response to changes in SAR.

The AF starts at a specified value (commonly 0.02) and can increase each time the trend extends, usually by 0.02.

How is Parabolic SAR calculated?

The Parabolic SAR is calculated for each period based on the formula:

SARn = SARn-1 + AF * (EP - SARn-1)

Where,

SARn is the current period's SAR.

SARn-1 is the SAR from the previous period.

AF is the acceleration factor.

EP (Extreme Point) is the extreme point in the current trend. If the current trend is an uptrend, then the extreme will be the highest point in the trend before it goes down again and if the current one is a downtrend, it will be the lowest point in a downtrend before the trend goes back up.

Example

Assumptions:

We are looking at a daily chart of a stock.

Current market price is $51.

The SARn-1= $50. The starting SAR is usually the previous day’s closing price.

The Acceleration Factor (AF) is 0.02.

The Extreme Point (EP) is $52 (highest point in the current uptrend). Here we have assumed an uptrend.

SARn = ?

Let us calculate the SARn now.

Calculation:

SARn = SARn-1 + AF * (EP - SARn-1)

SARn = 50 + 0.02 x (52-50)

SARn = 50+0.02×2= $50.04

In this example, the new Parabolic SAR value (SARn) is calculated to be $50.04.

Interpretation:

The Parabolic SAR is used to determine potential reversals in the price direction.

If the current SAR value is below the current market price, it suggests an uptrend.

If the SAR is above the market price, it suggests a downtrend.

So, if the stock's current market price is $51, which is higher than the calculated SAR ($50.04), it indicates that the uptrend is likely to continue. This is an indication to go long.

Hence, traders might use this information to make informed decisions.

However, it's essential to consider other factors and use the Parabolic SAR in conjunction with othertechnical indicatorssuch as moving average, MACD etc. for a more comprehensive analysis.

Importance of Parabolic SAR in technical analysis for trading

The Parabolic SAR (Stop and Reverse) is an important tool in technical analysis for several reasons:

Trend Identification:One of the primary uses of the Parabolic SAR is to identify the direction of the underlying trend. The dots of the SAR appear either above or below the price chart, signalling the potential trend direction (up or down).

Trend Reversal Signals:The Parabolic SAR is designed to provide signals for potential trend reversals. When the SAR dots switch sides (e.g., from below to above the price or vice versa), it suggests a change in trend direction.

Trailing Stop-Loss Management:Traders often use the Parabolic SAR to set trailing stop-loss orders. In an uptrend, the stop-loss moves up with the SAR dots, helping traders lock in profits as the price moves higher. In a downtrend, the stop-loss moves down.

Dynamic Support and Resistance:The SAR dots can act as dynamic support or resistance levels. In an uptrend, the SAR provides support, and in a downtrend, it acts as resistance. Traders may use these levels for decision-making and risk management.

Simple to Use:The Parabolic SAR is relatively easy to understand and use. Its visual representation on price charts makes it accessible to traders with varying levels of experience.

Adaptive to Market Conditions:The acceleration factor in the Parabolic SAR formula allows the indicator to adapt to changing market conditions. As trends extend, the SAR accelerates, capturing the momentum of the trend.

Complementary to Other Indicators:Traders often use the Parabolic SAR in conjunction with other technical indicators to confirm signals and build a more comprehensive analysis. Combining indicators can enhance the reliability of trading decisions.

Risk Management:The Parabolic SAR assists in risk management by providing a mechanism for setting stop-loss levels. This can help traders limit potential losses and protect gains in trending markets.

Versatility Across Timeframes:The Parabolic SAR can be applied to various timeframes, from short-term intraday trading to long-term investing. Its adaptability makes it a versatile tool for traders with different time horizon preferences.

Parabolic SAR Trading strategy using Python

The Parabolic SAR trading strategy using Python combines the power of technical analysis with the flexibility of programming. Leveraging the popular TA-Lib library, this strategy involves calculating and visualising the Parabolic SAR indicator to make informed buy and sell decisions. Python's versatility enhances the implementation of this dynamic trading approach.

Step 1: Import Necessary Libraries

Import the required libraries.

Step 2: Define a Function to Get Historical Price Data

This function uses the yfinance library to download historical price data for a given stock (ticker) within a specified date range (start_date to end_date).

Step 3: Define a Function to Implement the Parabolic SAR Trading Strategy

This function implements the Parabolic SAR trading strategy. It calculates the Parabolic SAR values using the high and low prices, generates buy (1) and sell (-1) signals based on the relationship between the closing price and the SAR, and computes positions based on the signal changes.

Step 4: Define a Function to Plot the Strategy Results

This function plots the strategy results. It visualises the close prices, buy and sell signals, and the Parabolic SAR values. Green '^' markers represent buy signals, red 'v' markers represent sell signals, and the dashed line represents the Parabolic SAR.

Step 5: Define the Stock and Time Period

Specify the stock symbol (ticker) and the start and end dates for the historical price data.

Step 6: Get Historical Price Data

Call the get_price_data function to fetch historical price data for the specified stock and time period.

Step 7: Implement the Parabolic SAR Strategy

Call the parabolic_sar_strategy function to apply the Parabolic SAR trading strategy to the historical price data.

Step 8: Plot the Results

Call the plot_strategy function to visualise the results of the Parabolic SAR trading strategy.

Output:

Above you can see the price data with the application of Parabolic SAR trading strategy. The plotted results are for the specified stock and time period.

You can see that there are several buy and sell signals based on the technical analysis of Parabolic SAR.

The “sell signals” come about when the price closes below the parabolic SAR. This is happening on Oct 1 2023 (2023-10-01) and in between October 15 2023 and November 1 2023 (2023-10-15 and 2023-11-01) and so on.

Hence you should “go short” when the parabolic indicator suggests a downtrend.

Conversely, the “buy signals” come about when the price closes above parabolic SAR.

In the graph above, this is shown between Oct 1 2023 (2023-10-01) and October 15 2023 (2023-10-15).

In this case, you should “go long” as the indicator suggests an uptrend.

If you had bought the stock between 1st and 15th October 2023 at $175 and sold it on December 1 2023 at $190, it is clear that you will make a gain of $15.

Cons of Parabolic SAR

Now, let us see some drawbacks of using Parabolic SAR below.

Whipsaws in Choppy Markets:Parabolic SAR can generate false signals in choppy or sideways markets, leading to whipsaws. Traders may experience losses when the price lacks a clear trend.

Late Entry in Strong Trends:In strong trending markets, the Parabolic SAR may provide late entry signals, resulting in missed opportunities for capturing the entire trend.

Dependence on Parameter Settings:The effectiveness of Parabolic SAR is influenced by the values chosen for its parameters, such as the acceleration factor. In certain market conditions, default settings may not be optimal, requiring adjustments.

Not Suitable for Ranging Markets:Parabolic SAR is designed for trending markets and may not perform well in ranging or sideways markets where the price fluctuates within a certain range.

Sensitivity to Price Volatility:The SAR's sensitivity to price volatility can lead to frequent changes in direction, especially when the market experiences sudden and sharp price movements.

Lack of Directional Bias Information:While Parabolic SAR identifies the direction of the trend, it does not provide information about the strength or duration of the trend. Traders may need additional indicators for a more comprehensive analysis.

How to utilise Parabolic SAR to maximum potential?

Traders need to be aware of both the strengths and limitations of the Parabolic SAR and consider using it in conjunction with othertechnical indicatorsto enhance the robustness of their trading strategies. Additionally, risk management and a clear understanding of market conditions are crucial when using any trading tool. You can learn all about in this course ontechnical indicators python.

Conclusion

Parabolic SAR (Stop and Reverse) is a valuable tool in technical analysis, aiding traders in trend identification and providing signals for potential reversals. Its simplicity and adaptability across timeframes make it accessible, especially for those new to technical analysis.

The indicator's inclusion of an acceleration factor allows it to dynamically respond to changing market conditions, offering a trailing stop-loss mechanism in trending markets. However, challenges arise in choppy markets with false signals and potential late entries in strong trends.

Dependency on parameter settings, unsuitability for ranging markets, and sensitivity to price volatility underscore the importance of using Parabolic SAR judiciously. Combining it with other indicators and practising effective risk management enhances its utility in crafting comprehensive trading strategies.

If you wish to learn more about parabolic SAR, you can explore our Learning Track onTechnical analysis using quantitative methods. With this, you will get a series of curated courses to help you develop proficiency in Technical Analysis in trading.

Technical indicators such as Parabolic SAR are quite helpful in conducting the analysis since the indicator provides a glimpse into what to expect in a trend. This way you can decide the entry and exit points and can take informed trading decisions.

Updated byChainika Thakar(Originally written ByVibhu Singh)

Note: The original post has been revamped on 26th December 2023 for accuracy, and recentness.

Disclaimer: All data and information provided in this article are for informational purposes only. QuantInsti®makes no representations as to accuracy, completeness, currentness, suitability, or validity of any information in this article and will not be liable for any errors, omissions, or delays in this information or any losses, injuries, or damages arising from its display or use. All information is provided on an as-is basis.

---

*Imported from QuantInsti Blog on 2026-04-27*
