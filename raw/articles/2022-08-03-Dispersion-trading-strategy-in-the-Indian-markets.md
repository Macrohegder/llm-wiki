---
title: "Dispersion trading strategy in the Indian markets"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/dispersion-trading-strategy-indian-markets-project-karthik-kaushal/"
date: "2022-08-03"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Dispersion trading strategy in the Indian markets

**来源**: [QuantInsti](https://blog.quantinsti.com/dispersion-trading-strategy-indian-markets-project-karthik-kaushal/)  
**日期**: 2022-08-03  
**作者**: QuantInsti

---

## 原文

Dispersion trading strategy in the Indian markets

This project is an evidence on opportunities in thestatistical arbitrage style of trading. This strategy is built on the idea that there exists some repeatable patterns in the volatility of an index and its constituent stocks.

We model the spread between the implied volatility and the implied volatility of the basket of stocks weighted by their actual weights on the index. We chose BANKNIFTY as the index and its constituent stocks to backtest this strategy which is also called as dispersion trading.

In the end, we show that there is a positive expectation on the p&l of this strategy. The backtest is on one month of intraday data and can be extended to a longer period.

The course dives deep intobacktesting strategieslike dispersion trading, helping you understand how to validate such models with historical data. By mastering backtesting, you can fine-tune your approach to improve risk management and optimize overall performance.

This article is the final project submitted by the author as a part of his coursework in the Executive Programme in Algorithmic Trading (EPAT) at QuantInsti. Do check ourProjects pageand have a look at what our students are building.

About the Author

Karthik Kaushalis an options trader, has an experience of 3 years. He started his career as a data engineer in EY. Later he followed his passion and made a professional transition to financial markets.

This got him a small stint at aproprietary trading deskbased out of Mumbai primarily trading options in the Indian markets. Currently he works at True beacon for their options trading desk. His role involves deploying sizeable institutional capital on systematic volatility based strategies.

Apart from traditional markets he also trades crypto options in his personal book. He holds a bachelor degree in electrical and electronics engineering from National institute of engineering in Mysore.

Strategy Idea

We calculate the volatility of the index and its constituent stocks at a suitable intraday frequency.

Once we have the volatility for each stock component and Index, we will calculate the correlation between the volatility of the index and weighted (weights explaining the index spot price) average of that of the constituent stocks as well.

Now depending on the correlation we would take positions when the correlation crosses a predetermined threshold. When it crosses we enter into a buy/sell first OTM strangle and a straddle in the index and take a counter position in the index constituents. As long as we are in the position we keep hedging the delta at the frequency chosen.

We will exit all the positions after the correlation gets back to the exit threshold. The entry and exit thresholds are determined/optimized when we back-test the system.

Dataset

Currently we have the intraday 30 min data for the options & futures of index and stocks provided as a part of EPAT project. We have to preprocess and calculate IV and correlation based on that.

Motivation

Dispersion trading is strategy based on high quantitative rigor and promising theories. I did go through few academic papers where it is being applied to multiple markets across the world which shows the robustness of the strategy when executed diligently.

Project outline

I have back-tested the dispersion trading strategy on BANKNIFTY and its constituent stocks.

I have back-tested for a period of 1 month in January 2017 at a frequency of 15 minutes. The BANKNIFTY index majorly had AXISBANK, HDFCBANK, ICICIBANK, INDUSINDBANK, KOTAKBANK, SBIN and YESBANK and few other stocks which had negligible weightage,

Following are weights of the stocks on the index.

AXISBANK

HDFCBANK

ICICIBANK

KOTAKBANK

11.23%

INDUSINDBANK

YESBANK

Strategy Idea

We calculate the average implied volatility of stocks and index using the first OTM strike price contracts with the following formula.

Average IV = {(IV of Put * Distance of stock price from the strike price of the 1st OTM Call) + ((IV of Call * Distance of stock price from the strike price of the 1st OTM Put)}/ (Distance between strikes).

Then we calculate the weighted average of the average IV of stocks by their weights on the index and calculate the ratio - IV of BANKNIFTY/ weighted average IV of the stocks.

This ratio is also calleddirty correlationand is calculated for every 15 minutes. Based on this we calculate a moving Z score on a look-back period of 30.

If the Z score is greater than 1 we expect the BANKNIFTY IV to come down or the weighted average IV of the stocks to go up and hence, we short first OTM Strangle of BANKNIFTY and buy first OTM strangle of all stocks. The contrary is for Z score less than -1.

After we enter as per above rules, at every 15 minutes we hedge the deltas - we calculate the delta of all our positions and bring it to close to zero.

It may be done by calculating the delta of each stock and index in our portfolio and if the this delta per quantity for each stock is greater than 0.1 or less than -0.1 we hedge it appropriately by taking positions in the futures.

If the Z score reaches a magnitude less than 0.8 we square of all the positions and calculate the PnL.

Position sizing

The back-test has considered 4 lots of BANKNIFTY – 4 lots on PE and 4 lots on CE and with respect to this the exposure to the constituent stocks is calculated with its respective weights on BANKNIFTY.

The margin required is around 15-20 lakhs (without leverage) for this arrangement including the margin for hedging and MTM handling.

For example, if Z>1 with BANKNIFTY current price at 18050. Following will be the trades taken which is logged by the back-test code (Ignore the decimals in the quantity as it can be rounded off to integers).

To illustrate one instance, the AXISBANK quantity is around 380 for CE as the weights of AXISBANK is around 9.6%. So the contract value is 380*460 = 174,800 which is 9.6% of the value of 100 quantity BANKNIFTY 18100 CE (100*18100 = 1810000).

Backtest result

The above results are just for one month, so the period is too small for drawing conclusions. The intention was to just demonstrate the potential of this strategy.

Improvements and suggestions

We can test the strategy for a different frequency.

We can optimize the hedging thresholds and its frequency as well.

We can optimize/vary the z score thresholds for entry and exit for each of the frequency we test the strategy.

And of course the back-test period should be increased to a large extent.

The complete Python code and related information is provided in the Python code below. You can download and refer to it.

If you want to learn various aspects of Algorithmic trading then check out thisalgo trading coursewhich covers training modules like Statistics & Econometrics, Financial Computing & Technology, and Algorithmic & Quantitative Trading. EPAT equips you with the required skill sets to build a promising career in algorithmic trading. Enroll now!

File in the download

Complete Python Code of the project

Login to Download

Disclaimer: The information in this project is true and complete to the best of our Student’s knowledge. All recommendations are made without guarantee on the part of the student or QuantInsti®. The student and QuantInsti®disclaim any liability in connection with the use of this information. All content provided in this project is for informational purposes only and we do not guarantee that by using the guidance you will derive a certain profit.

---

*Imported from QuantInsti Blog on 2026-04-27*
