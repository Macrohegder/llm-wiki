---
title: "Dynamic Selection of Pairs for Statistical Arbitrage"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/selection-pairs-statistical-arbitrage-project-divyant-agarwal/"
date: "2022-02-07"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Dynamic Selection of Pairs for Statistical Arbitrage

**来源**: [QuantInsti](https://blog.quantinsti.com/selection-pairs-statistical-arbitrage-project-divyant-agarwal/)  
**日期**: 2022-02-07  
**作者**: QuantInsti

---

## 原文

Dynamic Selection of Pairs for Statistical Arbitrage

An incredible project that dives deep and helps you learn, model and understand the creation and execution of a Statistical Arbitrage trading strategy. It also helps you the knowledge of how one can quantitatively analyse the modelling results.

The complete python code of this project is also available in a downloadable format at the end of the article.

This article is the final project submitted by the author as a part of his coursework in the Executive Programme in Algorithmic Trading (EPAT) at QuantInsti. Do check ourProjects pageand have a look at what our students are building.

About the Author

Divyant Agarwalis a finance professional and is a commerce graduate. Divyant is actively pursuing his CFA, FRM and CMT. Besides this, he has completed the Executive Programme in Algorithmic Trading (EPAT) and possesses core competencies in Machine Learning, Technical Analysis and Options Trading.

Objective

The objective of this project is to model aStatistical Arbitrage tradingstrategy and quantitatively analyse the modelling results. The biggest assumption inpairs tradingis that the correlation between the stocks is real and the stocks will return to that correlated relationship after any divergence.

Just because the two stocks are correlated does not mean that they will continue to be correlated in the future. Motivation lies in the fact that the correlation might not continue to be present between these stocks so the pairs should not be fixed and rather should always be dynamically selected based on the past period’s correlation.

Project Strategy

The idea is to take reverting positions on assets that are stationary over a period of time.

Stationarity refers to the fact that if the asset prices do not deviate much but stay around the mean then we can take long positions if the price moves too much below the mean and we can take short positions if the price is too much above the mean in the expectation that the prices will come back towards the mean.

Examples of the same can be seen below:

In the above figure, we can see the weekly closing prices of State Bank of India stock for a 10 year period. We can see that the prices are stationary in nature and move around the mean of INR 240.

The stock deviates 100 points from the mean and then reverts back to it. A trading opportunity using the logic of mean reversion and stationarity could be used to take positions in this stock i.e. we could go long around INR 140 and go short around INR 340. LearnMean Reversion Strategyin detail in the Quantra course.

When trading in the market, it is difficult to find naturally occurring price series which are stationary. Usually, such tendencies are found in the prices of commodities like wheat, corn and currencies.

However, the focus of this project is to trade in stocks in the Indian markets and as stated, it is difficult to find naturally occurring price series which are stationary (especially for stocks). So a better approach is to find pairs of stocks that tend to move together i.e. their spread (difference between the prices) follow stationarity.

Understanding thestationary data definitionis key to identifying profitable trading opportunities. While naturally stationary stock prices are rare, finding pairs with stationary spreads can lead to more reliable strategies. Dive deeper into this concept to see how it can enhance your trading approach and boost your market analysis.

Spread and Hedge Ratio

What is the definition of spread?

Spread refers to the difference between the prices of two stocks. The spread is calculated as –

Spread = Price of stock A – n * log Price of stock B

where, n refers to hedge ratio

Hedge Ratio

The hedge ratio is the ‘Beta coefficient’which could be found by regressing the closing prices of the two stocks. Assume, we have the prices for the last 10 days for two stocks A and B –

If we do a linear regression between Stock A and Stock B where stock B is the dependent variable (on the y-axis) and stock A is the independent stock (on the x-axis), the beta coefficient of the variable is the hedge ratio.

In the above case, we can see that the linear regression equation is –

Y = 0.4972 X + 81.44

Hence0.4972is the hedge ratio.

Now that we have the hedge ratio, we can calculate the spread using the following formula

Spread = Stock B price – hedge ratio * Stock A price

Hence, we get the following table –

Now that we have calculated the spread, we have to check whether the spread is stationary or not.

Stationarity test

Hypothesis formulation

We can check the stationarity of a spread using the ADF test. Let’s discuss the ADF test in detail.

We can describe  the current  price changes  from the past price data using a linear  model

Δp(t) = λp(t − 1) + μ + βt+ α1Δp(t − 1) + ... + αkΔp(t − k) + Єt

Where,p= price  of the  instrumentΔp(t) =p(t) − p(t − 1)Δp(t − 1) = p(t − 1) − p(t − 2), and so onλ = regression coefficient

In this test, the null hypothesis is thatλ = 0 (Not stationary)& the alternative hypothesis isλ < 0 (Stationary)

The intuition behind the hypothesis is that if λ = 0 then the next move is not dependent on the past movement. Hence the spread is not stationary.

But if λ < 0, it means that the next move is dependent on the past value. Hence the spread is stationary.

Test critical

The critical value can be found from the χ2 (chi–square) table values.

The values are as follows for the popular confidence intervals are –

Probability

Critical Value

Test statistic

The test statistic refers to the value that we are getting from the model. It is calculated using the following formula –

Comparing Test-statistic with Test critical and conclusion

If test statistic > test critical – we reject the null hypothesis and conclude that data is ‘stationary’

If test statistic < test critical – we fail to reject the null hypothesis and conclude that is ‘not stationary’

Hence if the spread is stationary we will include the pair to track else we discard the pair for the time being.

The code is as follows:

In the Python file submitted along with the document, this is the first-class object that has been created. The name of the class object is ‘pair selection’ and the purpose of this class object is to take a pair and based on the data given to calculate the appropriate spread and based on the ADF test conclude whether the pair was stationary over the period or not.

The spread calculation has been done in the function ‘spread_calculation’. The calculated spread is updated to the data frame object where the data is stored and it returns the hedge ratio as the output. This approach aligns with the principles ofmean reversion strategies, where spreads and stationarity are key factors in identifying potential trading opportunities.

Once the spread is calculated, we use the ADF test as defined above and conclude with 95% whether the pair is stationary or not for the given time frame.

Defining entry and exit

Once a pair has been selected, we will use the pair to take long and short positions of the spread.

If the spread is below the mean, we take a long position on the spread

If the spread is above the mean, we take a short position on the spread

Meaning of going long on the spread

Suppose when one stock (A) underperforms the other stock (B) this means that the spread between the two stocks is less than the average value of the spread. A signal to go long means we buy the underperforming stock which in this case is stock A and short the outperforming stock B.

Meaning of going SHORT on the spread

Suppose when one stock (A) outperforms the other stock (B) this means that the spread between the two stocks is more than the average value of the spread.

A signal to go short means we short the outperforming stock which in this case is stock A and buy the underperforming stock which in this case is B. This is based on the assumption that, as discussed earlier, the spread between the stock will revert back to the average value of the spread.

To take positions based on spreads, we need a quantitative way of defining:

How much below the mean will we go long?

How much above the mean will we go short?

What will be our stop loss?

What will be the target?

To answer these questions objectively, I have used the Bollinger bands.

What are Bollinger Bands?

Bollinger Bands are a band of three lines (moving average, upper band, lower band). The values can be calculated using the following formulas –

Moving Average = ∑(value at t – n, value at t-(n-1),…, value at t) / n

Upper Band = moving average of the last 20 days + (2 * standard deviation of the last 20 days)

Lower Band = moving average of the last 20 days - (2 * standard deviation of the last 20 days)

All three are calculated over the same time period.

In the above figure, it can be seen that Bollinger bands around the prices of the stock Reliance Ltd. which is calculated by adding and subtracting 2 times the Standard deviation from themoving averageof the last 20 days.

How do we trade using the Bollinger bands?

Long entry– We will take a long position if the spread crosses the lower band of the Bollinger band from below.

Short entry– We will take a short position if the spread crosses the upper band of the Bollinger band from above.

Take Profit –If the spread reaches the mean of the band after taking a long/short position, we will square off the position.

Stop Loss –If the spread crosses out of the lower band/upper band again after taking a long/short position, we consider that as the stop loss and the position is squared off.

Explanation for the code

Calculation of spread and Bollinger bands –Calculated in the class named‘indicator_calculation’

a. Spread calculation – We are taking the hedge ratio calculated in the class named‘pair_selection’and calculating the spread in the function‘spread’at each point using the formula

Spread = Stock A price – (Hedge Ratio * Stock B price)

b. Bollinger bands – Calculated in the function‘bollinger_bands’using the formulas described  above

Calculation of returns for the positions taken –

To calculate the returns for the positions taken we have multiple functions in the class named‘backtester’.The functions are explained below -

a.signal_calc()– The aim of this function is to generate long and short positions based on the conditions that we had discussed above in the Section

b.status_calc()– This function is like the housekeeper of the current position. It updates the values based on previous values.

If the current position is that of a long/short position in a trade then it will constantly keep checking at every closing whether the stop loss/target was hit or not.

If the stop loss/target is hit, the function will close the position and look for a new possible trade by checking the values calculated in the previous function.

c.quantity_calc()– This function is used to calculate the quantity traded i.e. how much quantity of first stock to go long on and how much quantity of the second stock to go short on. This is calculated based on the hedge ratio.

The calculation of the quantity to trade is kept very simple by multiplying the hedge ratio by 1000. To summarise the same,

If we are long on the spread,

Quantity bought for first stock = 1000

Quantity sold for the second stock = 1000 * hedge ratio

If we are short on the spread,

Quantity sold for the first stock = 1000

Quantity bought for the second stock = 1000 * hedge ratio

d.traded_value()– This function calculates traded value by multiplying the price with quantity.

e.returns()– This function calculates the returns based on traded values

If we are long on the spread,

Return on stock 1 = (Traded Value at t / Traded Value at (t-1))-1

Return on stock 2 = 1-(Traded Value at t / Traded Value at (t-1))

If we are short on the spread,

Return on stock 1 = 1-(Traded Value at t / Traded Value at (t-1))

Return on stock 2 = (Traded Value at t / Traded Value at (t-1))-1

Total returns on the trade = Returns on stock 1 + Returns on stock 2

Backtesting

Selecting pairs

Selecting pairs is a very critical step in this approach and requires a detailed analysis and backtesting. This point will be discussed in greater detail later in this read.

List of stocks

As a starting point, I have selected nine sectors from the Indian stock market and have included the top five stocks from each sector provided that the stock traded in the selected period (i.e. 2008 to 2014)

Given below are the sectors and the stocks chosen –

Sector

Stocks

Hindustan Unilever Ltd.

ITC Ltd.

Nestle Ind Ltd.

Tata Consumer Products Ltd.

Britannia Industries Ltd.

Finance

HDFC Bank Ltd.

ICICI Bank Ltd.

State Bank of India Ltd.

Kotak Mahindra Bank Ltd.

Axis Bank Ltd.

Maruti Ltd.

Tata Motors Ltd.

M&M Ltd.

Bajaj Auto Ltd.

Eicher Motors Ltd.

Tech Mahindra Ltd.

Wipro Ltd.

Infosys Ltd.

HCL Technologies Ltd.

Tata Consultancy Services Ltd.

TV18 Broadcast Ltd.

Zee Entertainment Ltd.

PVR Ltd.

Saregama India Ltd.

Sun TV Network Ltd.

Vedanta Ltd.

Tata Steel Ltd.

Adani Enterprises Ltd.

JSW Steel Ltd.

Hindalco Industries Ltd.

Pharma

Dr Reddy’s Laboratories Ltd.

Sun Pharmaceutical Industries Ltd.

Lupin Ltd.

Cipla Ltd.

Divis Laboratories Ltd.

Infrastructure

DLF Ltd.

Phoenix Mills Ltd.

Oil & Gas

Bharat Petroleum Corp Ltd.

Indian Oil Corporation Ltd.

Oil & Natural Gas Corporation Ltd.

Reliance Ltd.

List of possible pairs

Note: When creating pairs, we have to keep one thing in mind that is we can create pairs with stocks within a sector only

Initially, we create all the possible pairs for all the stocks selected. If we have selected fives stocks in a sector, we have ten possible pairs.

For the first stock, we have four possible pairs

For the second stock, we have three possible pairs left (one is already created)

For the third stock, we have two possible pairs left (two are already created)

For the fourth stock, we have one possible pair left (three are already created)

For the fifth stock, all pairs are already created.

So,(4+3+2+1) = 10possible pairs.

The code for the above step is:

So, we have a total of 77 pairs from the above-selected sectors.

len(possible_pair)

Output: 77

Time Period

This backtesting project is done for the period of 2008 to 2014 March. We are checking the stationarity of the pairs for the three months and then if the pair is stationary for the period, we are trading that pair for the next three months.

Example: We check the stationarity of all the pairs discussed above for the period of January 2018 to March 2018. The stock pairs which are stationary in that period, we use them for the trading in the next 3 months.

The process

Once we have selected the pairs and the time, we backtest by calling all the class methods defined above. The code for the same is:

To carry out the process, we have created a function named‘strategy’in which the following steps are carried out:

Pass all the possible pairs and select the time period as an input to this function

Check if a pair is co-integrated (class name–pair_selection)

If yes, calculate the hedge ratio and spread else, ignore the pair(if condition).

Calculate the Bollinger bands to define the entry and exit (class name – indicator_calculation)

Backtest the pairs (class name – backtester)

Result

From the above strategy function we will get a log of all the trades which include the following columns :

Month of trade

Year of trade

Returns

The sample of the result is as follows:

If we take the cumulative returns of the trades above, we get the following graph as the output:

The caveat with the result generated is:

The returns are generated assuming that the returns generated are invested in the next trade in full amount. This is not true and is discussed in greater detail in Section IV (1)

The returns are too volatile and approaches are discussed in Section IV to make the returns less volatile and consistent.

Improvements in the model

This part of the project discusses the practical issues and how we can improve the model.

Calculation of returns

The problem with the approach that we have used to calculate the returns is naïve as the assumption is that whatever return that we get from one trade is invested in the next trade but that is not true.

Example:

From the generated trade logs, we can see that in the month of April 2008 there were a total of 5 trades generated and we have taken the returns cumulatively.

In reality, these trades are generated on different days and the holding period depends on the behaviour of the spread with respect to the Bollinger bands i.e. it is variable.

So, you cannot take the profits of one trade and invest it in the next one. One step towards reality would be if one could calculate the trades in one month and invest equally in each pair (retrospectively). This is outside the scope of this read.

Selecting pairs (revisited)

As discussed earlier, we are discussing this step again but with the approach to understand how we can select pairs in a better manner.

So from the logs generated, I have created a summary of the returns which contain the following columns:

pairs – Unique pairs which were traded

returns – Sum of all the returns for a particular pair for the period

For example, if the pair ‘SBIN.NS and AXISBANK.NS’ have been traded in two months.

Return

SBIN.NS, AXISBANK.NS

SBIN.NS, AXISBANK.NS

The sum of returns would be calculated as (0.04 + 0.03) = 0.07

ret_dir – Count of all the trades where the returns were positive for that pair

number_of_trades – Count of total trades

number of correct trades – Count of correct trades/number of trades for each pair

Following is the sample of the output :

Next, we sort the values of the ‘Number of correct trades’ and export the result to a spreadsheet for further analysis

We get an output as follows:

We can then remove the pairs which have an accuracy(number of correct trades) of less than 50% or negative returns as these pairs are not statistically co-integrated in the real sense.

These stock pairs were co-integrated for a short period of 3 months but are not cointegrated in the long term, hence not a suitable pair for us.

Changing the instruments

For this project, I have chosen stocks in the Indian markets. The next step forward is to change the instruments to exchange-traded funds, currencies, commodities. The instruments could be chosen based on multiple factors –

Qualitative Selection– This refers to selecting instruments like ETFs and currencies which tend to move together. These assets move together because they are exposed to common economic factors.

Example 1 – iShares MSCI Australia ETF(EWA) and iShares MSCI Canada ETF(EWC) – Both are dominated by commodities stocks

Example 2 - HDFC Gold ETF and UTI Gold ETF – Both ETFs have gold as the underlying holding

Quantitative Selection –

Same sectors –Stocks that are exposed to similar sectoral factors.Example 1 – Bajaj Finance and Bajaj Finserv – Bajaj Finserv is the parent company

Similar Market Capitalisation –Stocks of the same size.Example 1 – Ambuja and ACCMarket Cap of Ambuja – INR 32,805 cr.Market Cap of ACC – INR 53,235 cr.

Similar Ratios –Stocks which are similar performance ratios

Note – There are many choices of pairs but easy to lose cointegration

Bibliography

Dr. Ernest P. Chan, “Algorithmic trading winning strategies and their rationale”

Vidyamurthy, Ganapathy, Pairs Trading: Quantitative Methods and Analysis (New Jersey: John Wiley & Sons, Inc., 2004)

To understand more about statistical arbitrage and ways to implement its strategies, here is an introductory video that explains it all!

If you want to learn various aspects of Algorithmic trading then check out thisalgo trading coursewhich covers training modules like Statistics & Econometrics, Financial Computing & Technology, and Algorithmic & Quantitative Trading.

EPAT equips you with the required skill sets to build a promising career in algorithmic trading.Enroll now!

File in the download:Backtesting of pair trades - jupyter notebook

Login to Download

Disclaimer: The information in this project is true and complete to the best of our Student’s knowledge. All recommendations are made without guarantee on the part of the student or QuantInsti®. The student and QuantInsti®disclaim any liability in connection with the use of this information. All content provided in this project is for informational purposes only and we do not guarantee that by using the guidance you will derive a certain profit.

---

*Imported from QuantInsti Blog on 2026-04-27*
