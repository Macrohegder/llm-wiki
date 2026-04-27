---
title: "Paradigms of Trading Strategy Formulation"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/paradigms-of-trading-strategy-formulation/"
date: "2015-09-02"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Paradigms of Trading Strategy Formulation

**来源**: [QuantInsti](https://blog.quantinsti.com/paradigms-of-trading-strategy-formulation/)  
**日期**: 2015-09-02  
**作者**: QuantInsti

---

## 原文

Paradigms of Trading Strategy Formulation

It requires hard work and consistent efforts to make profit in stock trading. One might hear a lot of success stories about making profits in stock trading but a clear distinction between luck and discipline is essential in picking up such stories. In this post we aim at providing you throughquantitative trading strategiessome proven methods that generate significant profits.

There is need for a disciplined approach in building a trading strategy. It can be categorized into following steps.

Hypothesis formation

Back-testingand optimization

Coding strategy in trading platform

Simulator testing

Trading live in the market

Hypothesis formation is about what you think the market behavior is. If you believe market is trending bullish you would want to go long, if you think market is trending bearish you would want to go short. One such hypothesis in technical trading is “if daily price is greater than the N day moving average it’s time to buy and if price is less than the N day moving average price then it’s time to sell.

Once the hypothesis is formulated the next steps are to back-test the strategy and optimize the parameters. The “N” day moving average can be any number say 20, 40 or 200 days moving average.

Back-testing is essential to observe which of the moving average windows provided the best returns.

For a moving average example optimization involve choosing the best moving average period, the stop loss limit that should be set and the profit limit after which the position should be squared off. It is wise enough to divide the data into two parts and apply back-test on the first half. With the parameters set execute those optimized parameters on the second half of the data. If the results are consistent with those of back-test results on the first half then trade with the same set of parameters otherwise choose the next best set.

Since quantitative trading involves programming you have to choose one of the coding language and a trading platform to execute it. Many of theretail tradersuse C++, C# or Java for trade execution. After fine tuning the parameters in back-testing it’s quite tempting to jump the ship and start trading in the live market. It should be noted that past performance is not an indicator for the future. So the best way to look forward at your strategy is by testing it on simulated (virtual trading) environment. This will give you a clear picture of how your strategy performs in the live market.

Once you are confident about the back-test results and virtual trading, it is show-time for live trading. Following is the list of parameters that are to be estimated when you execute live trading.

CAGR (Compounded Annual Growth Rate)

Hit ratio

Average profit per trade

Average loss per trade

Maximum drawdown

Maximum consecutive loss

Volatility returns

Sharpe ratio

It is important to consider market scenario while choosing the trading period for back-testing. Selecting a trading duration that has a typical trend would not give the complete picture. An ideal market scenario has four phases i.e. consolidation, bullish, distribution and bearish. Consolidation is a phase where the stock moves within a defined pattern within a barrier level. Distribution phase is an accumulation phase that signifies the end ofbearish trendand the beginning of bullish trend. So care has to be taken that the back-testing window you choose for testing the strategies includes all the possible market scenarios.

Trading in the stock markets always involve an element of risk. There is a saying, “No pain, No gain”. A wise advice would be choose what pain you can live with, rather than choosing what gain you want to make. To quantify the statement you should balance the risk reward ratio. You should ask yourself “What is your risk appetite? Do you prefer low risk- low return or high risk high return? Do you want higher returns with high leverage and prone to maximum drawdowns or do you prefer nominal returns with little or no leverage?” Clarity of thought is important in making trade related decisions and answering these questions gives you a clear picture of what your approach towards trading should be.

As Warren Buffet says, “Don’t make the same mistake twice!”. One and only mantra for success is to improve day by day.

Webinar Video

https://www.youtube.com/watch?v=MwD7WL9pbUo

Next Step

After reading this article, you’ll know fundamentals of trading strategy formation. You can startdesigning a trading strategy using R(open source platform) with the help of thisexample. We also have an interactive self-paced 10 hours long datacamp course ‘Model a Quantitative Trading Strategy in R‘ that will allow you to test your skills.

---

*Imported from QuantInsti Blog on 2026-04-27*
