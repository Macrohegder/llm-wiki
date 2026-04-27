---
title: "How to optimise a trading strategy based on indicators?"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/indicator-trading-strategies/"
date: "2023-09-21"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# How to optimise a trading strategy based on indicators?

**来源**: [QuantInsti](https://blog.quantinsti.com/indicator-trading-strategies/)  
**日期**: 2023-09-21  
**作者**: QuantInsti

---

## 原文

How to optimise a trading strategy based on indicators

ByChainika Thakar

Technical indicators are powerful tools used by traders to analyse market data and make informed decisions about buying, selling, or holding financial instruments. For those who want to learn how to automate these indicator-based decisions, theAutomated Trading for Beginnerslearning track is a great place to start. These technical indicators are mathematical calculations based on historical price, volume, or open interest data and provide valuable insights into market trends, momentum, volatility, and potential entry or exit points for trades.

In this comprehensive guide, we will explore various types of technical indicators, how to read them effectively, and steps to integrate indicators into trading strategies with real-world examples.

We will also examine the pros and cons of using indicators in trading strategies to help traders make well-informed decisions.

All the concepts covered in this blog are taken from this Quantra learning track onTechnical Indicators Strategies in Python. You can take aFree Previewof the course.

This blog covers:

What are trading indicators?

General steps to utilise stock indicators for optimising trading strategies

Example of optimising trading strategy using Python

Pros of using indicators for optimising trading strategies

Cons of using indicators for optimising trading strategies and ways to overcome

FAQsDo indicator based trading strategies work?What indicators do most traders use?What is the best exit indicator?

Do indicator based trading strategies work?

What indicators do most traders use?

What is the best exit indicator?

What are trading indicators?

Trading indicatorsare mathematical calculations based on historical price, volume, or open interest data, designed to provide traders with insights into market trends, price movements, and potential entry or exit points for trades.

These indicators are widely used in technical analysis, a method of analysing and predicting future price movements based on past market data. Traders use trading indicators to identify patterns,trends, and potential reversals in the market, which can help inform their trading decisions.

General steps to utilise stock indicators for optimising trading strategies

Utilising stock indicatorsto optimise trading strategies involves a systematic approach to analysing market data and making informed trading decisions.

Here are the general steps to effectively utilise stock indicators for this purpose:

Select Relevant Indicators:Choose indicators that align with your trading style and goals. Common indicators include moving averages, Relative Strength Index (RSI), MACD, Bollinger Bands, and Stochastic Oscillator. Each indicator serves a specific purpose, such as trend identification, momentum measurement, or overbought/oversold conditions.

Understand Indicator Interpretation:Familiarise yourself with how each selected indicator works. Understand its calculations, components, and what signals it generates. Learn about its strengths and limitations in various market conditions.

Define Trading Strategy:Determine the overarching trading strategy you want to optimise. Are you aiming for trend-following, reversal, or breakout strategies? Defining your strategy helps you choose the most suitable indicators.

Backtesting:Apply your selected indicators to historical price data to see how they would have performed in the past. This process, known as backtesting (This course onbacktesting trading strategiesby Quantra is just what you need to get the best out of your trading.), helps you evaluate the effectiveness of your strategy and indicators over different market conditions.

Parameter Optimization:Some indicators have adjustable parameters that affect their sensitivity. Use backtesting to optimise these parameters for historical data, seeking the best settings that generate profitable signals.

Evaluate Signals:Analyse how the indicators generate buy and sell signals in response to historical price movements. Assess the accuracy of these signals and their consistency in different market scenarios.

Risk Management:Incorporate risk management techniques into your strategy. Determine how much capital you're willing to risk per trade and set stop-loss orders accordingly.

Demo Testing:Implement your strategy in a demo or simulated trading environment to observe its performance in real-time market conditions without risking real capital.

Real-Time Testing:Once you're confident in your strategy's effectiveness, implement it in live markets with a small amount of capital to verify its performance in actual trading situations.

Continual Monitoring and Adjustment:The market is dynamic, so regularly monitor your strategy's performance. If it's not delivering expected results, adjust your indicators, parameters, or even the entire strategy based on new data and insights.

Combine Indicators:Consider combining multiple indicators for a more comprehensive analysis. Confirm signals from different indicators before making a trade decision to reduce the likelihood of false signals.

Stay Informed:Keep up-to-date with market news, economic events, and global developments. External factors can impact market behaviour beyond what indicators can predict.

Example of optimising trading strategy using Python

First of all we will use an indicator to create a trading strategy using the TA-Lib library. You canuse a pair of indicatorssuch as Ichimoku and RSI for generating trading signals.

Here, let us create an inidcator based trading strategy. This strategy will be based on the MACD technical indicator. Later, we will optimise the same.

Step 1: Import libraries

You will have to import the TA-Lib library for creating a strategy based on technical indicators. Hence, first of all you have to make sure that you haveinstalled TA-Lib.

Step 2: Fetch daily stock price of Apple Inc. (ticker: AAPL)

The data is retrieved for the date range from '2015-01-01' to '2023-08-07'. The downloaded data will include columns like 'Open', 'High', 'Low', 'Close', 'Volume', and 'Adj Close'.

Step 3: Calculate MACD

Now, we will calculate the Moving Average Convergence Divergence (MACD) technical indicator using the talib.MACD function from the talib library. MACD is a trend-following momentum indicator that helps to identify changes in the strength, direction, and momentum of a stock price’s trend.

Parameters used in MACD function are as follows:

data['Close']: This is the closing price of the stock, which is used to calculate the MACD.

fastperiod=12: The fast period represents the number of days used for the fast Exponential Moving Average (EMA). In this case, it is set to 12.

slowperiod=26: The slow period represents the number of days used for the slow Exponential Moving Average (EMA). In this case, it is set to 26.

signalperiod=9: The signal period represents the number of days used for the signal line, which is an Exponential Moving Average of the MACD line. In this case, it is set to 9.

The above mentioned parameters are standard ones or are set by default. We have used these for illustrative purposes.

Step 4: Plot the MACD and signal line

Now, we will plot the MACD and signal line. This visualisation can be helpful for traders and investors to make informed decisions about buying or selling Apple stock based on the MACD indicator's signals and trend analysis.

Let us see how it is done and what the graph represents.

Output:

In the output above, the plot visualises the Moving Average Convergence Divergence (MACD) indicator for Apple stock over the specified date range (from January 1, 2015, to December 28, 2022).

In the graph above, you will see three lines:

Theblue linerepresents the MACD line, which is the difference between the 12-day Exponential Moving Average (EMA) and the 26-day EMA. It fluctuates above and below the zero line, capturing the short-term and long-term trends in the stock price.

Thered linerepresents the signal line, which is a 9-day Exponential Moving Average of the MACD line. It smooths out the MACD line and helps identify potential trend changes when it crosses above or below the MACD line.

Thegrey barsrepresent the MACD histogram, which is the difference between the MACD line and the signal line. When the MACD line is above the signal line, the histogram is positive, indicating a bullish trend. Conversely, when the MACD line is below the signal line, the histogram is negative, indicating abearish trend.

By observing the plot, you can analyse the interactions between the MACD line and the signal line. For instance:

Bullish Signal:When the MACD line crosses above the signal line, it generates a bullish signal, suggesting a potential upward trend in the stock's price.

Bearish Signal:On the other hand, when the MACD line crosses below the signal line, it generates a bearish signal, indicating a potential downward trend in the stock's price.

Let us visualise the cumulative returns with the above strategy.

Output:

The cumulative returns graph generated using the provided code illustrates the performance of a trading strategy based on the Moving Average Convergence Divergence (MACD) indicator applied to Apple's stock price data.

The graph showcases how the strategy's returns evolved over time.

Positive values above the zero line indicate periods of maximum gains, while negative values below the line indicate losses.

The starting point is typically set at zero, representing the initial investment.

Step 5: Optimise the above trading strategy

Here we are optimising the trading strategy using the Moving Average Convergence Divergence (MACD) indicator for Apple stock (ticker symbol 'AAPL') over a specific date range.

The strategy involves finding the best combination of parameters (fast_period, slow_period, and signal_period) for the MACD indicator to achieve the highest possible returns.

Output:

Best Parameters: Fast Period=16, Slow Period=20, Signal Period=6 Total Profit/Loss with Best Parameters: 1.95

In the output above, you can see that the set parameters are as follows:

Fast Period: The fast period is set to 16, which represents the number of days used for the fast Exponential Moving Average (EMA) in the MACD calculation.

Slow Period: The slow period is set to 20, representing the number of days used for the slow Exponential Moving Average (EMA) in the MACD calculation.

Signal Period: The signal period is set to 6, which is the number of days used for the signal line, an Exponential Moving Average of the MACD line.

The cumulative returns are shown increasing over a period of time and they do not fall below zero at all with this optimised strategy.

After exploring various combinations of fast_period, slow_period, and signal_period, the output shows that the best parameters were:

Fast Period=16

Slow Period=20

Signal Period=6.

By using the best parameters, the total returns (increased return) achieved by the MACD strategy on the historical Apple stock data was calculated to be 1.95.

This figure of 1.95 represents the cumulative gains achieved by executing the optimised MACD trading strategy over the specified date range (from January 1, 2015, to August 07, 2023) based on the given historical stock price data.

Step 6 - Comparison of actual and optimised strategy with regard to cumulative returns

Output:

In the comparison graph above, we can see that, with the optimised strategy, there have been-

Higher Peaks:The optimised strategy consistently outperformed the actual strategy till early 2019. This is indicating superior performance during specific periods. Also, starting from the end of the year 2022 and from the year 2023, the optimised strategy’s performance is consistently better than the actual strategy’s.

Smaller Drawdowns:The optimised strategy shows smaller declines during unfavourable market conditions, leading to shallower valleys in its line. This can be seen from the year 2019 to the end of the year 2022.

Crossover Points:The lines have been crossing over each other at different points, indicating shifts or potential reversals in strategy performance.

The graph offers a visual representation of how the optimised strategy compares to the actual strategy in terms of cumulative returns.

To conclude it all, the comparison graph provides insights into whether the optimisation process has effectively enhanced the strategy's cumulative returns and overall gain. It helps you understand whether the efforts to fine-tune the MACD parameters have yielded a more successful trading strategy.

It's important to interpret the comparison graph in conjunction with otherperformance metrics,risk analysis, and considerations such as transaction costs, and market conditions.

Note: Please note that these results are based on historical data and past performance, and they do not guarantee similar performance in the future. The total profit/loss may vary depending on different market conditions, economic factors, and other external influences. When making investment decisions, it is crucial to consider a comprehensive analysis, risk tolerance, and professional financial advice.

Pros of using indicators for optimising trading strategies

Using indicators for creating and optimising trading strategies offers several advantages that can enhance a trader's decision-making process and improve overall trading performance. Here are some of the key pros of using indicators for optimising trading strategies:

Objective Decision Making

Indicators provide objective and quantifiable data, removing emotional biases from trading decisions. Traders can base their actions on specific signals generated by the indicators rather than making impulsive choices driven by fear or greed.

Identifying Trends and Patterns

Indicators can help identify market trends, price patterns, and potential reversal points. They allow traders to spot opportunities that may not be immediately apparent through visual analysis of price charts alone.

Confirmation of Signals

Combining multiple indicators can strengthen trading signals. When different indicators provide similar signals or confirm a trading setup, it increases the trader's confidence in the trade's potential success.

Risk Management

Indicators aid in risk management by providing valuable information for setting stop-loss and take-profit levels. Traders can use indicators to establish appropriate risk-reward ratios and manage their position sizes accordingly.

Time-Saving

Indicators automate the analysis process, saving traders significant time and effort. Instead of manually scanning multiple charts, indicators can quickly identify potential trading opportunities.

Scalability and Adaptability

Indicators can be used across various markets, timeframes, and trading styles. Whether a trader is interested in day trading, swing trading, or long-term investing, indicators can be adjusted to suit different strategies.

Backtesting and Historical Analysis

Indicators allow traders tobacktesttheir strategies using historical data. This enables them to evaluate the effectiveness of their approach and make necessary adjustments before executing trades in live markets.

Market Sentiment Analysis

Some indicators, like the Relative Strength Index (RSI Indicator), provide insights into market sentiment, indicating whether an asset is overbought or oversold. This can be valuable information for traders to gauge potential price reversals.

Automation and Algorithmic Trading

Indicators can be integrated into algorithmic trading systems, allowing traders to automate their strategies and execute trades based on predefined rules.

Versatility in Strategy Development

Indicators offer a wide range of technical analysis tools, from trend-following indicators like moving averages to oscillators like MACD and Stochastic Oscillator. This versatility enables traders to create diversetrading strategiesto suit different market conditions.

While using indicators in trading strategies has many advantages, it is essential to acknowledge their limitations.

Cons of using indicators for optimising trading strategies and ways to overcome

By addressing the cons associated with using technical indicators through appropriate strategies and techniques, traders can effectively utilise indicators in their trading plans and enhance their decision-making process.

Cons of Using Technical Indicators

Ways to overcome each

1. Lagging Signals

Combine indicators withprice action analysisto validate signals. Consider using leading indicators or other forms of analysis for real-time insights.

2. False Signals

Avoid relying on a single indicator; instead, use multiple indicators to cross-validate signals. Consider using filters or additional confirmation criteria before entering trades based on indicator signals.

3. Over-Optimization

Avoid excessive tweaking or optimization of indicator parameters based on historical data. Focus on robustness and simplicity in strategy development. Backtest strategies over various market conditions to ensure generalizability.

4. Market Adaptability

Use indicators suitable for different market conditions. Adapt strategies based on market trends and volatility. Incorporate fundamental analysis and market sentiment to complement technical indicators.

5. False Sense of Security

Recognize that no single indicator guarantees accurate predictions. Practice risk management and avoid overconfidence. Continuously analyse and refine strategies based on market feedback.

6. Noise and Choppy Markets

Use indicators in trending markets where they are more effective. Avoid using indicators as the sole basis for decision-making in choppy or sideways markets. Consider other forms of analysis or trading styles during such periods.

7. Learning Curve

Devote time to understand each indicator thoroughly, its strengths, and limitations. Practice using indicators on historical data or demo accounts before applying them in live trading.

8. Data Overload

Avoid using too many indicators on a single chart, as it can lead to confusion and conflicting signals. Select a few indicators that complement each other and align with your trading strategy and timeframe.

9. Emotional Bias

Create a well-defined trading plan with predefined entry, exit, and risk management rules. Follow the plan consistently to reduce the influence of emotions on trading decisions.

Now, let us check out answers to some frequently asked questions.

Do indicator based trading strategies work?

Indicator-based trading strategies can be effective when combined with proper risk management and thorough analysis. Success hinges on the trader's expertise and adaptable strategy.

What indicators do most traders use?

Moving Averages, Relative Strength Index (RSI), Moving Average Convergence Divergence (MACD), Bollinger Bands, and Stochastic Oscillator are commonly used by traders.

What is the best exit indicator?

The best exit indicator depends on traders' individual strategies and risk appetite. Notable options include Moving Averages, Parabolic SAR, and support/resistance levels.

Bibliography

4 effective trading indicators every trader should know

How to combine the best indicators and avoid wrong signals

Conclusion

Trading indicators are tools used in technical analysis to predict market movements. Moreover, reading indicators involves combining price analysis with signals.

Pros of using indicators include improved decision-making, but they have limitations which can be overcome if acknowledged and learnt about. It must be noted that the indicators work best when combined with other analyses. Traders choose based on their preferences and strategies.

If you wish to learn more about using technical indicators for trading strategies, you must enrol into our course onTechnical Indicators Python.

In this course, you'll gain proficiency in using technical indicators to generate trading signals and recognize price trends. You'll practise implementing indicator-based strategies, live trading, and evaluating their effectiveness. By the end of the course you'll be equipped to apply these skills to real-world scenarios and solve practical trading challenges.

Disclaimer: All data and information provided in this article are for informational purposes only. QuantInsti®makes no representations as to accuracy, completeness, currentness, suitability, or validity of any information in this article and will not be liable for any errors, omissions, or delays in this information or any losses, injuries, or damages 	arising from its display or use. All information is provided on an as-is basis.

---

*Imported from QuantInsti Blog on 2026-04-27*
