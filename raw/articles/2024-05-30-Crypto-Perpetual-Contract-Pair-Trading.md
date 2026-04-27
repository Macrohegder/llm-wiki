---
title: "Crypto Perpetual Contract Pair Trading"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/crypto-perpetual-contract-pair-trading-project-rong-fan/"
date: "2024-05-30"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Crypto Perpetual Contract Pair Trading

**来源**: [QuantInsti](https://blog.quantinsti.com/crypto-perpetual-contract-pair-trading-project-rong-fan/)  
**日期**: 2024-05-30  
**作者**: QuantInsti

---

## 原文

Crypto Perpetual Contract Pair Trading

Statistical arbitrage is a classic quantitative trading strategy, and pairs trading is one of them. Digital currency perpetual contracts are non-delivery perpetual futures. This project describes using data from the Binance exchange to find perpetual contract pairs whose pairing spreads conform to the mean reversion trend. Based on this backtest, find the relatively optimal trading parameters.

This article is the final project submitted by the author as a part of his coursework in ouralgo trading course, the Executive Programme in Algorithmic Trading (EPAT) at QuantInsti. Do check ourProjects pageand have a look at what our students are building.

About the Author

Rong Fanholds dual master's degrees in Computer Science and Lightning Science & Technology. With over a decade of experience in the Software Development Life Cycle (SDLC) domain, Rong has published more than 10 academic papers, amassing over 100 citations onGoogle Scholar. He also holds certifications in Professional Project Management and Professional Scrum Master.

Rong has a deep interest in investment and trading. Since 2017, he has managed a value investment-style portfolio that has achieved an approximate compound annual growth rate of 20%, consistently outperforming the S&P 500. In March 2022, he earned a certificate from the Wharton School's "Economics of Blockchain and Digital Assets Certificate Program." That same year, he published an e-book titled “Blockchain Value Investing” (Traditional Chinese Edition) on Kindle.

In 2023, Rong achieved his 'Certificate of Excellence' from QuantInsti's Executive Programme in Algorithmic Trading (EPAT) which he pursued with an aim to systematically learn quantitative methods and apply them to practical investment strategies.

Related terms and explanations

Digital currency perpetual contract

A perpetual contract is a cryptocurrency derivative that is essentially a futures contract that has no expiry date and is settled in cash. It allows traders to speculate on their price movements without owning a specific asset. Trading perpetual contracts has many advantages, such as high leverage, low fees, and a wide range of underlying.

How does the contract anchor the spot price?

For traditional delivery contracts, since the delivery price is fixed at the spot price, once the futures price deviates significantly from the spot price, arbitrage trading will automatically bring the spot price closer. Perpetual contracts have no delivery, so it is impossible to rely on spot arbitrage to increase the recent spot price.

The practice of digital currency exchanges is to pay funding fees between long and short parties every 8 hours. Its basic idea is that within a period of time, if the price of the perpetual contract is higher than the spot price, it means that the bulls have strong momentum, so the longs will pay funding fees to the shorts, and conversely, the shorts will pay funding fees to the longs.

Assuming that the funding rate is 0.01%, then each trader calculates the funds he will pay or receive based on the number of positions. Since the total amount of long and short positions is always equal, the funding fee is not charged by the exchange, but transferred between the long and short parties.

Perpetual futures are derivative contracts with no expiration date, allowing traders to speculate on asset prices indefinitely.

Perpetual futures are particularly popular among traders in the cryptocurrency market.

The funding rate mechanism helps keep the perpetual contract price close to the spot price of the underlying asset.

Leverage is a key feature of perpetual contracts, allowing traders to control larger positions with less capital, but it also comes with greater risk.

T-Value

Definition: T-value is a statistic that represents the difference between the sample mean and the expected mean under the null hypothesis, in units of standard deviation.

Function in ADF test: T-value and P-value are used together to determine the unit root. A larger T-value indicates a stronger rejection of the null hypothesis, providing information that corroborates the P-value.

P-Value

Definition: P-value is a probability value that represents the probability of an observed statistic or more extreme situation occurring if the null hypothesis is true.

Role in ADF test: In the ADF test, the P-value is used to determine the existence of unit root. If the P-value is less than the significance level (usually chosen to be 0.05), then we can reject the null hypothesis that there is no unit root in the time series, indicating that the data is stationary.

Null hypothesis

An assumption in statistics that usually means there is no effect or no relationship. In specific statistical testing, the null hypothesis is a contrasting or control hypothesis that assumes that any observed effect or relationship is due to random factors.

Instatistical arbitrage, it is sometimes tested whether asset prices follow a mean reversion model. The null hypothesis may be that asset prices do not follow mean reversion, while rejection of the null hypothesis indicates that a mean reversion relationship exists, providing an arbitrage opportunity.

ADF test

The enhanced Dickey-Fuller test (Augmented Dickey Fuller) is a modified version of the standard Dickey-Fuller (standard Dickey-Fuller). ADF test in pairs trading is used to check the cointegration between two stocks.

The difference

The main difference between the two tests is that ADF is used with a larger set of time series models, which can be more complex.

The ADF test is an alternative to DF because even if there are missingvalues, it can also be used.

Unit Root

It is a property in time series data that indicates that the roots in the series (with respect to time) remain constant. In statistics, the presence of a unit root indicates that a time series is non-stationary. Specifically, if a time series has a unit root, its mean and variance may increase over time rather than tending to a fixed value.

In statistical arbitrage and time series analysis, understanding the properties of the unit root is crucial to verify the stationarity of the data and to perform effective analysis and model building.

Stationarity

The stationarity of a time series means that a set of time series data looks flat and the statistical characteristics of each order (such as mean, variance, covariance) do not change with time. Typically, stationarity is verified using the Augmented Dickey-Fuller (ADF) test.

Stability renderings

correlation coefficient: 0.99, cointegration test p-value: 0.2596837

co-integration test p value:, co-integration test p-value: 0.0

Stable test sample code

Output

t statistic = -3.3175906010162217{'1%': -3.4381962830171444, '5%': -2.8650034233058093, '10%': -2.568614210583549}

Since the t-stat value is below the critical value of 5%, the spread is considered stationary or cointegrated.

Cointegration

If two or more series are combined and the resulting series is stationary, they are said to be cointegrated. This article only discusses pairs trading, so only two-time series are considered. Non-stationary time series x, y, and the linear combination composed of x, y may also be stationary. In this case, the model is likely to have pseudo (false) regression.

Recognizing the importance ofStationary Time Seriesis crucial for detecting true cointegration between series. When combined series become stationary, they offer a solid foundation for pairs trading and help prevent false regression. Dive deeper to discover how mastering stationarity can enhance your trading models and lead to more accurate results.

Therefore, the classical model is based on stationary data and requires testing for stationarity on a single series and then testing for cointegration.

Cointegration example code

Strategy theory and text description

2.1 Mean Reversion Theory

2.1.1 Mean ReversionThe trend of mean reversion is that the price moves in a certain relationship around a fixed mean, so first we must make sure that the contract we select must have a stable mean, and the price fluctuations must be around the mean.

2.1.2 Pair tradingWhy do we do mean reversion portfolio arbitrage instead of doing mean reversion arbitrage individually for a certain contract? The reason is that the time series of a single futures contract price does not mean reversion in most cases, but the difference (diff) between the prices of two products with a strong correlation is more likely to show a stable mean reversion phenomenon.

Based on the two-time series, take a price difference (diff) sequence, subtract the latest price of the second contract 1-hour kline from the latest price sequence K1 of the first contract hour Kline, and get a price difference sequence diff, then we can think the price difference between the two contracts should regress to some extent around the mean of the diff sequence.

We then calculate some theoretical spreads as trading signals. Take two extreme values ​​as the position opening judgment signal, such as the two price differences divided into points of 99% and 1% as the position opening judgment price difference, and use the two values ​​closest to the mean as the position closing signal, such as 52% and 48% The price difference (diff) between the two quantile points is used as the closing judgment price.

The Diff calculation formula is as follows:

Diff = Underlying A - a * Underlying B - constant

2.1.2.1 Example of Pair TradingThe prices of soybean oil and soybean meal themselves may not have a strong mean reversion phenomenon, but what about the price difference between soybean oil and soybean meal? Since the correlation between the two is very strong, they are likely to exhibit a strong mean reversion phenomenon. If their price differences are in line with the mean. Return, then it is feasible to conduct cross-variety arbitrage between the two.

Starting from the next section, we will list the steps, text description, code, and execution results.

Pair trading of digital currency perpetual contracts

3.1 Prepare data

Use the Python CCXT package to execute the Binance exchange API to obtain all its perpetualContractOHLC data.

3.1.1 Data specifications

3.1.2 Part of the code for data acquisition

3.1.3 Data effects

3.2 Stationarity test

The statistical properties of time series data with stationarity do not change over time, that is, their mean and variance remain unchanged over time.

3.2.1 Stability test code

3.2.2 Stationarity test results

As of December 2023, according to the data results of 3.1, Binance Exchange has a total of 47 groups of perpetual contracts. After the ADF stability test, a total of 3 groups are stationary (as shown below), and the other parts are not stable.

3.3 Cointegration test

According to the stationarity test results in 3.2.2, ETC, RLC, TRX, BN, TRX, XMR, and XRP are stable time series. Combine them exhaustively and then implement cointegration testing.

3.3.1 Cointegration test code

3.3.2 Cointegration test results

The above figure shows that all pairs conform to the cointegration characteristics.

3.3.3 Test results of cointegration and correlation

After the abovestepDiscover: ETC-USDT, RLC-USDT at the same time conform toCointegration andRelevantrelation. Therefore, Plan to use: ETC-USDT, and RLC-USDT as a trading basis for examples.

3.4 Define statistical arbitrage logic

3.4.1 Introduction to Principles

For the time series pair selected in 3.3.3, the difference (diff) is consistent with mean regression, so we can take a sequence of differences. Subtract the 1-hour close of the first contract from the 1-hour close of the second contract to obtain a price difference sequence diff. We can think that the price difference between the two contracts should regress to some extent around the mean of the diff sequence.

Diff = ETC - a * RLC - constant

Next, the values ​​of a and constant need to be calculated.

After calculation in the above example, it is published as follows

a = 11.46constant = 5.8468Diff = ETC - 11.46 * RLC - constant

3.4.2 Position opening and closing signals

We then calculate some theoretical spreads as trading signals. Take two extreme values ​​as the position opening judgment signal, such as the two price differences divided into points of 99% (top_percentile) and 10% (bottom_percentile) as the position opening judgment price difference, and use the two values ​​closest to the mean as the position closing signal. For example, the two price differences between the 55% and 45% quantile points are used as the take-profit and exit judgment prices. If the loss is 20%, the stop-loss exit will be used.

3.5 Perform backtesting

3.5.1 Pair diff graph

Whether the diff of Pair means reversion is the prerequisite for subsequent operations. Now draw the diff of ETC and RLC as follows.

3.5.2 Stability test of Pair diff

3.5.2.1 Test code

symbol, adf_statistic, p_value, critical_values, is_stationary =self.analyze_service_instance.stationary_test(df_merged['diff'], "etc_rlc_diff")

3.5.2.2 Test results

As can be seen from the above figure, the pair diff sequence complies with the stationarity test, that is, it complies with mean regression.

3.5.3 Backtesting framework

PyAlgoTrade is a Python library for backtesting stock trading strategies. It is designed to help users evaluate and test their trading strategies using historical data. With PyAlgoTrade, you can verify how your strategy performed under past market conditions, which is crucial for understanding and improving your trading strategy.

PyAlgoTrade offers the tools tobacktestand refine amean reversion strategy in Python, ensuring strong performance in different market conditions.

Define the parameters of the backtesting framework according to the following trading logic

When diff >= top_percentile, go short etc, and go long rlc, for example: the default value of top_percentile: 99%.

When diff <= bottom_percentile, go long etc and go short rlc. For example: the default value of bottom_percentile: 10%.

When there is a position and the diff falls within the following range: [take_profit_left_percentile, take_profit_right_percentile], take profit and exit. For example: take_profit_left_percentile default value: 45%, take_profit_right_percentile default value: 55%.

When there is a position and portfolio_value_change_rate <= stop_loss_portfolio_value_change_percentage, stop loss and exit. For example stop_loss_portfolio_value_change_percentage default value: -30%.

Define the backtest class of PyAlgoTrade

The code is as follows:

3.6 Backtest results

Default parameters

top_percentile = 0.99

bottom_percentile = 0.1

take_profit_left_percentile = 0.45

take_profit_right_percentile = 0.55

stop_loss_portfolio_value_change_percentage = -0.2

Initial capital: 10,000

Sharpe Ratio: 1.11

Return drawdown ratio: 18.03

Market value at the end of the period: $82320

This is a good result. Next, we can try to adjust the parameters for further optimization.

3.7 Optimization

Given a parameter range, traverse and repeatedly perform a single backtest to find the optimal parameters, using the Sharpe ratio as the criterion.

top_percentiles = 0.9, 0.95, 0.99

bottom_percentiles = 0.01, 0.1, 0.15

take_profit_left_percentiles = 0.40, 0.45, 0.47

take_profit_right_percentiles = 0.52, 0.55, 0.6

stop_loss_portfolio_value_change_percentages = -0.2, -0.3

trade_ratios = 0.35, 1

Parameter explanation

top_percentiles: When diff percentile > this value, open a position

bottom_percentiles: When the diff percentile < this value, open a positiontake_profit_left_percentiles: When the diff percentile is within the following range, take profit to exist, [take_profit_left_percentiles, take_profit_right_percentiles]

stop_loss_portfolio_value_change_percentages: When the portfolio loss exceeds this proportion, exit to stop loss

trade_ratios: The proportion of funds used to open each position.

Maximum Sharpe ratio: 1.14

Final portfolio value: $90717.54 (Initial value: $10000)

4 Summary

4.1 Technical aspects

Since statistics and backtesting framework Python are mainstream, using C# in backtesting requires a lot of reinvention, so it is impossible. But when the premise of obtaining valid parameters, it is feasible to use C# as the live trading language, as long as the live trading logic and backtesting logic are completely consistent. In order to prevent inevitable code deviation, it is still recommended to use the same language and framework to write real code.

Our course provides detailed insights intobacktesting Pythonframeworks, helping participants streamline their strategy development and ensure consistency between backtesting and live trading environments. Enroll today to enhance your trading skills with Python-based solutions.

4.2 Effect of pair trading

Using the parameters in Figure 3.7.1, we can get the trading effect Sharpe ratio: 1.14, and the final market value of the investment portfolio can reach: $90717.54 (initial value: $10000). However, since market styles frequently switch, backtesting is required every once in a while to obtain optimal parameters.

4.3 Things to note

Pairs trading is a low-risk trade, not risk-free, so a stop loss is required.

The contract may encounter risks such as delisting, so it is necessary to pay appropriate attention to the fundamentals.

The calculation of Diff needs to pay attention to the coefficient issue

The return drawdown ratio (RDR) is an effective strategy evaluation metric used to evaluate the document characteristics of the strategy.

It is reasonable to observe the price trend of pairs and use the latest data (for example: data in the last year) for backtesting.

References

Liao Xuefeng - Perpetual Contract

Shini - Using mean reversion for spread arbitrage

QuantInsti - Arbitrage Strategies: Understanding Working of Statistical Arbitrage

QuantInsti - Pairs Trading - correlation, cointegration, examples, and strategy Steps

Using ADF Test to Find Pairs Trading Strategy

Making a career in Algorithmic Trading

Investopedia - Perpetual Contract

How to use Granger test and cointegration to analyze data (organizing part)

This project has detailed crypto perpetual contract pair trading, showcasing the use of statistical arbitrage with Binance data. It gives an end-to-end pair trade from idea to backtest, and optimization. We've covered the entire process, from idea to backtesting and optimization, highlighting the importance of robust crypto trading strategies in cryptocurrency trading, which you can further explore through a dedicatedcrypto trading course.

Feel free to explore ourtrading projectspage to discover more innovative solutions by our talented participants. Use this guide as a valuable resource in your trading journey.

As part of QuantInsti'salgo trading course, the Executive Programme in Algortihmic Trading (EPAT), this project reflects the expertise our students achieve. If you too want to learn various aspects of Algorithmic trading then check out EPAT, it equips you with the required skill sets to build a promising career in algorithmic trading. Enroll now!

Disclaimer: The information in this project is true and complete to the best of our Student’s knowledge. All recommendations are made without guarantee on the part of the student or QuantInsti®. The student and QuantInsti®disclaim any liability in connection with the use of this information. All content provided in this project is for informational purposes only and we do not guarantee that by using the guidance you will derive a certain profit.

---

*Imported from QuantInsti Blog on 2026-04-27*
