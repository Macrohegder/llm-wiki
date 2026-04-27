---
title: "Intraday Low-Frequency Trading Strategy"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/intraday-low-frequency-trading-strategy-project-rajtk/"
date: "2020-01-24"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Intraday Low-Frequency Trading Strategy

**来源**: [QuantInsti](https://blog.quantinsti.com/intraday-low-frequency-trading-strategy-project-rajtk/)  
**日期**: 2020-01-24  
**作者**: QuantInsti

---

## 原文

Intraday Low-Frequency Trading Strategy

The opening range breakout is a very commonly used trading strategy used by professional and amateurs traders alike and has the potential to deliver high accuracy trades if done with optimal usage of indicators, pattern recognition, strict entry and exit rules as well as trade control.

After observing and manually trading markets for a while, I noticed that this system is well suited for Indian markets. This is a set of simple strategies involving the capture of the firsttrading candlestick patterns(5-minute OHLC data) and analysing it to generate trades.

This article is the final project submitted by the authors as a part of their coursework in the Executive Programme in Algorithmic Trading (EPAT®) at QuantInsti®. Do check ourProjects pageand have a look at what our students are building.

About the Author

Raj TK (Partner, Trivarga Trading LLP) comes from a non-finance and non-programming background. He felt the need for a structured learning process to interpret themarkets. EPAT provided Raj with the basic understanding of Markets, Market microstructure, Algorithm, strategies and basic programming skills specific to trading. In the past few months after the completion of the EPAT course, he developed an Algorithmic trading system and a back-tester module.

Before he describes in detail the back-tester module, he wants to thank his teachers for their guidance and motivation in this project.

Mr. Nitesh Khandelwal: On his session on ATR, excel programming and for his support in this project.

Dr. Yves Hilpisch: For making Python easy. The last 5 minutes of his second session, where he gave a glimpse of how to take the strategy Live, immensely motivated me in developing my programming skills in Python as well as the trading system and going live in the market.

Data Analysis

Analyzed the 5 / 15 / 30 minutes OHLC charts of Nifty 50 stocks from Yahoo finance and data provided by the broker to understand patterns and derive at range breakout strategies.

Key Findings

Based on the data analysis, observation and prior manual trading experience following strategies emerged:

1) Gap Up Green Candlestick: The Opening candle should be green and should be at least 2 points higher than the previous high and difference between the close and open of the current candle should be at least 0.5 to be a gap up the green candlestick. Capturing the OHLC values of the first candlestick will help in generating trade entries upon range breakout.

2) Gap Up Red Candle Stick:The Opening candle should be red and should be at least 2 points higher than the previous high and the difference between the open and close of the current candle should be at least 0.5 to be a gap up red candlestick. Capturing the OHLC values of the first candlestick will help in generating trade entries upon range breakout.

3) Gap Down Green Candle Stick:The Opening candle should be green and should be at least 2 points lower than the previous low and the difference between the close and open of the current candle should be at least 0.5 to be a gap down green candlestick. Capturing the OHLC values of the first candlestick will help in generating trade entries upon range breakout.

4) Gap Down Red Candle Stick:The Opening candle should be red and should be at least 2 points lower than the previous low and the difference between the open and close of the current candle should be at least 0.5 to be a gap down red candlestick. Capturing the OHLC values of the first candlestick will help in generating trade entries upon range breakout.

5) Gap Up Red candle – trend reversal pattern:The Opening candle should be red and should be at least 2 points higher than the previous high and above the upper Bollinger band. The difference between the close and the low should be lesser than the upper shadow. There is a higher probability of prices going down. Capturing the OHLC values of the first candlestick will help in generating trade entries upon range breakout.

6) Gap Down Green candle – trend reversal pattern:The Opening candle should be green and should be at least 2 points lower than the previous low and below the lower Bollinger band. The difference between the high and the close should be lesser than the lower shadow. There is a higher probability of prices going up. Capturing the OHLC values of the first candlestick will help in generating trade entries upon range breakout.

7) Engulfing pattern – Red Candle:The Opening candle should be red and completely engulfing the previous candle. Larger the opening candle, higher will be the correction towards the buy-side with a very high probability. Capturing the OHLC values of the first candlestick will help in generating trade entries upon range breakout.

8) Engulfing pattern – Green Candle:The Opening candle should be green and completely engulfing the previous candle. Larger the opening candle, higher will be the correction towards the sell-side with a very high probability. Capturing the OHLC values of the first candlestick will help in generating trade entries upon range breakout.

9) Long Shadow – Green Candle:The Opening candle should be green and the difference between the close and open should be greater than 0.5 and the lower shadow should be at least twice the body of the candlestick. Capturing the OHLC values of the first candlestick will help in generating trade entries upon range breakout.

10) Long Shadow – Red Candle:The Opening candle should be red and the difference between the open and close should be greater than 0.5 and the upper shadow should be at least twice the body of the candlestick. Capturing the OHLC values of the first candlestick will help in generating trade entries upon range breakout.

Challenges/Limitations

1) Capturing the first candlestick is critical for the above strategies.2) Average 4-5 trades per month per script.3) The stock should exhibit the above pattern to generate trade signals hence thorough backtesting is needed to select stocks.

Implementation Methodology

1) [Gap Up / Gap Down] / [ Gap Up / Gap Down Reversal pattern] / [Long shadow]

Trade entry:Enter the trade (Buy / Sell-side) when the close of the current candle is completely outside of the initial opening candle.

Stop Loss:First SL to be placed at the low/high of the first candlestick depending on the buy / sell-side trade entry. This gives some room for theprice action tradingand to avoid premature SL trigger.

Trade Insurance:Once the price moves over 1 point from the buy/sell price, modify the SL to 1 point above/below the buy/sell price. This is to minimize the loss, in case the trade moves in the opposite direction.

Trailing SL:As the price moves in the direction of the trade, trail the SL for every 1-point increase in price.

Take profit:Take profit when the difference between the current SMA and previous SMA is greater than 0.2.

No. of Trades:No more than 2 trades in a day and take the trades in the opposite direction in a day upon range breakout.

2) Engulfing pattern

Trade entry:Enter the trade (Buy / Sell-side) when the close of the current candle is completely outside of the initial opening candle.

Stop Loss:First SL to be placed at least 3 points below or above the low/high of the first candlestick depending on the buy / sell-side trade entry. This gives some room for the price action and to avoid premature SL trigger.

Trade Insurance:Once the price moves over 2 points from the buy/sell price, modify the SL to 2 points above/below the buy/sell price. This is to minimize the loss, in case the trade moves in the opposite direction.

Trailing SL:As the price moves in the direction of the trade, trail the SL for every 1-point increase in price.

Take profit:Take profit on Stop Loss trigger

No of Trades:No more than 1 trade in a day

Conclusion

Below are the trade statistics for different scripts.

If you want to learn various aspects of Algorithmic trading then check out theExecutive Programme in Algorithmic Trading (EPAT). The course covers training modules like Statistics & Econometrics, Financial Computing & Technology, and Algorithmic & Quantitative Trading. EPAT equips you with the required skill sets to build a promising career in algorithmic trading.

You can check out our blogCandlestick Patterns - How To Read Candlestick Chartsif you wish to learn more about candlesticks and their patterns.

Disclaimer: The information in this project is true and complete to the best of our Student’s knowledge. All recommendations are made without guarantee on the part of the student or QuantInsti®. The student and QuantInsti®disclaim any liability in connection with the use of this information. All content provided in this project is for informational purposes only and we do not guarantee that by using the guidance you will derive a certain profit.

---

*Imported from QuantInsti Blog on 2026-04-27*
