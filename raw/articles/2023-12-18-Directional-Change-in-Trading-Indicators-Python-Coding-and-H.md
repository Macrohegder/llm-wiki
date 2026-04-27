---
title: "Directional Change in Trading: Indicators, Python Coding, and HMM Strategies"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/directional-change-trading/"
date: "2023-12-18"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Directional Change in Trading: Indicators, Python Coding, and HMM Strategies

**来源**: [QuantInsti](https://blog.quantinsti.com/directional-change-trading/)  
**日期**: 2023-12-18  
**作者**: QuantInsti

---

## 原文

Directional Change in Trading: Indicators, Python Coding, and HMM Strategies

ByJosé Carlos Gonzáles Tanaka

Usually,regime detectionis made with anHMM estimationover price returns or price return volatility. However, Chen and Tsang (2021) propose to use the Directional Change indicators as input for a HMM to detect regime shifts. They show that the HMM applied to the Directional Change indicators detects regime shifts better than with an HMM applied to price return volatility. Here we apply Directional Change in Trading with a simple strategy to see how well we increase our equity! Let’s find out!

You can find the risk-constraint Kelly criterion code onGitHubas well.

In this blog, we cover:

What does Directional Change in Trading mean?

Directional Change Indicators

Total Price movement

Time for Completion of a Trend

Time-Adjusted Return of DC

Learn how to code the Directional change in Python

A Hidden Markov model estimation based on the DC indicators

An HMM-DC-based trading strategy

What does Directional Change in Trading mean?

Whenever we try to find regime changes in a financial time series, we usually study the time series distribution to find those regimes and their respective changes. There’s another approach we should consider:Use the concept of directional change (DC) to detect regime changes.

Guillaume et al. (1997) were the first researchers who conceptualized the DC indicator. In the well-known paper, these authors used this indicator to find patterns in Forex data.The DC indicator is also known as the Zig Zag indicator.This indicator is used, instead of time series data points, to find the regime changes.

To build the DC indicator, we need to make a recursive procedure. The following is a modification of the explanation given by Tsang (2010). We’re going to go step by step so you can follow us clearly!

Let’s explain the DC with the graph. Suppose the asset price time series is given by the yellow line.

The “trough” point is C.

The horizontal axis is time.

Whenever the market conditions change, the asset price will have a “Downward Run” (AB+BC) or an “Upward Run” (CD+DE).

A Downward run comprises a “Downturn Event” (AB) and a subsequent “Downward Overshoot Event” (BC).

An Upward Run comprises an Upturn Event (CD) followed by a subsequent Upward Overshoot Event (DE).

In a Downward Run, the trough can be understood as a “last low” and this is constantly updated by the following formula: MIN(current price, last low). On the other hand, an Upward Run, a “last high” is also created and constantly updated by the following formula: MAX(current price, last high).

Now,how do you define the “Threshold”?

We can say that a Downward Run ends whenever the asset price gets higher than the last low by theta, where theta is a percentage return of the asset price defined arbitrarily by the trader. In the above figure, the Last Low is given by point C, the trough.

The red arrow CD is what we call an Upward Directional Change event.

The trough, point C, is a signal which confirms the Downward Run end and it starts an Upward Run.

The asset price given in point D is called the Upward DC Confirmation Point for the Upward Run period.

Next, the same threshold theta, allows us to confirm an Upward Run has ended when the asset price gets lower than the Last High by theta. In the above figure, the Last High is given by point E, the peak.

Once the asset price gets lower than the peak by theta, then we confirm an Upward Run that has happened from point C to point E. The peak is meant to be the ending point for the Upward Run.

Point F is called the Downward DC Confirmation Point for the Downward Run.

The red arrow EF is called the Downward Directional Change event.

All of the above makes the time definition different. Following the above figure, time periods will be given by:

OC: Downturn Run, where:

O,OB: is where the Downward Directional Change Event (AB) happens. This interval is the time between the peak and the Downturn Confirmation point. It’s also called the Downward DC Event Interval (DEI).

OB,C: is where the Downward Overshoot Event (BC) happens. It’s also known as Downward Overshoot Interval (DOI). Situated between the previous Downturn Confirmation Point and the next Peak.

C,OE: Upturn Run, where:

C,OD: is where the Upward Directional Change Event (CD) happens. This interval is the time between the trough and the Upturn Confirmation point. It’s also called the Upward DC Event Interval (UEI)

OB,C: is where the Upward Overshoot Event (BC) happens. It’s also known as Upward Overshoot Interval (UOI). Situated between the previous Upturn Confirmation Point and the next trough.

You can get a summary with the following figure provided by Chen and Tsang (2021):

Directional Change Indicators

In order to provide an algorithmic trading strategy, we need to use math formulas to compute the DC indicators.

We’re going to use the following figure (modified by me and provided by Chen and Tsang, 2021) to learn more about the DC indicators.

Let’s review some concepts:

DC Event: The Directional Change event. This can be an upward or downward DC event as explained in the previous section.

OS Event: The Overshoot event. This can be an upward or downward overshoot event as explained in the previous section.

In order to provide the indicators’ definition, we follow the nomenclature given by Chen and Tsang (2021).

Total Price movement

This indicator measures the absolute percentage price return in a trend.

The formula is the following:

Where,TMV_EXT(n): The total price movement computed at the extreme point called “n”.P_EXT(n): Peak price at the “n” period.P_EXT(n-1): Trough price at the “n-1” period.

Theta:Threshold defined arbitrarily by the researcher.

This TMV indicator will measure the asset price return volatility. The higher the TMV indicator value, the higher the asset price return volatility we must interpret.

Time for Completion of a Trend

This indicator measures the total time spent to complete a TMV trend. As shown in the previous figure, this indicator will be equal to 6, because the trough is located at time 3 and the peak is located at time 9. The same type of reasoning must be applied for a downward turn.

The formula is:

Where:T(n): Time for completion of a trend.t_EXT(n): A point in time where a peak has occurred.t_EXT(n-1): A point in time where a trough has occurred.

Time-Adjusted Return of DC

Also known as the “R” indicator. This indicator allows us to know the absolute return in an upward or downward trend. It’s a measure of the percentage price return provided by the TMV indicator per time unit.

The formula is the following:

Where,R(n): The time-adjusted return of DCTMV_EXT(n): The total price movement indicator extreme point “n”.T(n): The time for completion of a trend indicator

Theta:The threshold value chosen arbitrarily by the trader.

According to Tsang (2017), the three indicators can serve as a measure of any asset’s volatility. A high value of any of the 3 indicators will indicate a high-volatile period.

Learn how to code the Directional change in Python

To do this, we’ll base our code snippet on the pseudo-code provided by Aloud et al. (2012).

First, we import the necessary libraries

Then, we provide the DC indicators’ computations inside a function to be used later.

Let’s explain the function:

First, we create the necessary columns and set its initial values. We also set a default value for the “event” variable.

Next, we build the for loop. On each day, we check if we are on a downward or upward event.

In case we are in a downward event today, then we check if today’s close price is less than the low price or higher than the low price by the theta threshold.

In case the former happens, it means we’re still in the same event and we update the low price value with the close price and its index value, too.

In case the latter happens, we recognize the low price index as the day when an upward day happens. We then update the rest of the columns.

In case we are in an upward event today, then we check if today’s close price is higher than the high price or lower than the high price by the theta threshold.

In case the former happens, it means we’re still in the same event and we update the high price value with the close price and its index value, too.

In case the latter happens, we recognize the high price index as the day when a downward day happens. We then update the rest of the columns.

Once the loop ends, we then forward-fill the low and high prices’ values and their corresponding indexes.

In addition, using the Event column, we build the 3 DC indicators.

You might ask: How to choose the theta threshold?

Well, Glattfelder et al. (2010) highlighted the fact that the power law is present in the DC indicators. We can say, consequently, that no matter what threshold we choose, we’ll find each DC indicator having the same statistical properties. Even though the paper is based on high-frequency data, we follow Chen and Tsang (2021) and proceed to choose theta as 0.4% for all our below computations.

A Hidden Markov model estimation based on the DC indicators

Let’s now use our DC function to estimate a Hidden Markov model with the R indicator.

I know, you’re asking: Why a Hidden Markov model? Let’s create suspense about it. Don’t worry, I’m going to tell you later why we use this model.

The Hidden Markov model is an unsupervised machine learning model. It’s useful to find hidden states from the same data.

What is a hidden state?

Well, we can make the analogy by saying that a hidden state is like an unknown regime found in the same asset price time series. We say “hidden” because you’ll find those regimes without knowing a priori which regime we’re situated on each day. As you know, any asset price time series doesn’t tell you which regime the same has.

With the Hidden Markov model, we’re going to provide the regimes that happened to be on each day.

Let’s code!

Let’s download the GBPUSD data from 2003 to October 2023. Then, we compute the close-to-close log returns.

Next, we get the DC indicators based on our above function. We also drop NaN values.

Just to check the R indicator, we plot it

We check how many downward and upward trends have been found

Output:
 0.0    2824
-1.0    1167
 1.0    1165

There are almost 800 trends found. We should say something here. Chen and Tsang (2021) create a trading algorithm with 5-minute frequency data and estimate an HMM in a second-frequency R indicator time series. They then compute the average of the R indicator time series found inside each 5-minute period.

In this article, we don’t follow the same procedure because we are working with daily frequency data to compute the R indicator. That’s why we forward-fill the R indicator time series so we could have a complete time series.

Next, we fit an HMM to the R indicator time series and get the hidden states (regimes) with the “predict” function, which is based on the Viterbi algorithm. Finally, we count the number of days we find for each regime.

Output:
0    3223
1    1933

As explained previously, the R indicator can be interpreted as a volatility measure. A high R would mean a high volatility. Here we compute the R mean as per each regime

Output:
R-based volatility for state 0, 1 and 2 are -4.68 and -6.80, respectively.

Just to check, we compute the volatility of the returns as per each regime computed with the above model.

Output:
Volatility for states 0 and 1 are 11.56 and 8.10, respectively.

As you can see, regime 1 has a high volatility compared to regime 0 for both the R indicator and the volatility of returns.

An HMM-DC-based trading strategy

Let’s have some fun! We propose in this section to create 3 strategies

A Buy-and-hold strategy

A 3-day simplemoving average strategy(SMA)

A HMM-DC-based 3-day-SMA strategy.

This strategy will try to find a better edge than what the second strategy can find. We will use 2 regimes.

Chen and Tsang (2021) also use the “Alpha Engine” from Golub et al. (2018) to create a trading algorithm. Here we take a simpler approach. We use the second strategy as a base model and do the following as a risk management process. We will leverage 2x the equity whenever the next forecast regime has an in-sample low volatility compared to the other regime, otherwise, we trade 1x the capital.

The forecast next-day regime will be obtained with a daily HMM estimation using the R indicator time series as input for the machine learning model.

Chen and Tsang (2021) used a Naive Bayes Classifier to forecast the next-day regime. We’re going to do something different. We’re going to compute the next-day regime with the same HMM model methods.

Chen and Tsang (2021) proposed to compare the HMM-DC-based regime forecasts with an HMM applied to the volatility of returns to see how useful the DC indicators are to the volatility of returns. This comparison will not be made here. We’re just going to apply the former.

We will use the same GBPUSD forex data from 2003 to October 2023. We’ll create a for loop to estimate daily the HMM. Following Chen and Tsang (2021), we will use the R indicator time series as input for the HMM.

Ready for the fun? Let’s go!

The first two strategies' cumulative returns can be vectorized later. We proceed to create the “for” loop for the second strategy.

First, we’re going to start the backtesting loop from the very first day of 2018. We also count the number of days in which we have different leverage trade sizes.

Output:
3656

Second, we define the new columns to be added to the data dataframe, together with the 4-day SMA signal.

Next we create the for loop for the HMM-DC-based strategy.

Here are some explanations:

Subset the data from the very first row to the previous day,

Use the subset data to create a HMM object with 2 regimes.

Estimate the HMM with the R indicator time series. We set

n_components to 2 since we want 2 regimes.

The covariance_type to diagonal since we want each regime to have its own volatility without a covariance between them.

The HMM model is estimated by iteration. We set n_iter to 200 as the maximum iterations allowed. We consider this value enough for the computations.

Set the seed to 100. This is arbitrarily chosen.

Compute the next-day regime forecast.

Compute the R volatility per each regime.

Obtain the correct leverage as per each regime: Whenever the next-day forecasted regime has a lower in-sample volatility compared to the other regime, then we trade 2x the total equity available, otherwise, we trade with no leverage.

Since our starting year for backtesting is 2018, we subset the data beginning from that same year.

Output:
1.0    788
2.0    714
0.0      1

Here comes the interesting part (but with some suspense!). We compute the 3 strategies’ cumulative returns.

Finally, we make the suspense end! Let’s plot the 3 strategies' cumulative returns.

Looks interesting, right? But it’s always important to check the summary statistics. See below

Let’s make a table with some statistics obtained with the above pyfolio functions.

Two things to say:

We can see that the 3-day SMA strategy gets to outperform the buy-and-hold strategy. We could have even created a sell-and-hold strategy and the SMA would also outperform it. It gets to outperform with all the metrics.

However, our main strategy gets to outperform the other two. The cumulative returns are bigger compared to the 4-day SMA. The Sharpe ratio and Sortino ratio are lower  and the maximum drawdown is worse.

Some pointers to be considered in this strategy:

Due to the increased leverage, the drawdown is higher with respect to the other 2 basic strategies. An improved risk management process might be needed to decrease such high risk.

We backtested using a 3-day SMA. We can optimize the window size to improve the results, but be careful of overfitting.

We could have used stop loss and take profit targets to handle the risk better.

Depending on the random seed, we might have different HMM estimation results. Be careful about that.

Maybe, you can change the theta threshold to find an improved edge.

You should incorporate slippage and transaction costs to make the results more real.

References

Aloud, Monira & Tsang, Edward & Olsen, Richard & Dupuis, Alexandre, (2011). "A directional-change event approach for studying financial time series," Economics - The Open-Access, Open-Assessment E-Journal (2007-2020), Kiel Institute for the World Economy (IfW Kiel), vol. 6, pages 1-17.

Chen, J. & Tsang Edward P.K. (2021). “Detecting Regime Change in Computational Finance”, CRC Press.

Golub, Anton & Glattfelder, James & Olsen, Richard. (2017). “The Alpha Engine: Designing an Automated Trading Algorithm”. SSRN Electronic Journal. 10.2139/ssrn.2951348.

Guillaume, D.M., Dacorogna, M. M., Davé, R. R., Müller, U.A., Olsen, R. B., & Pictet, O.V. (1997). “From the bird's eye to the microscope: A survey of new stylized facts of the intra-daily foreign exchange markets”,  Finance Stochastics 1, 95–129 (1997).

J. B. Glattfelder & A. Dupuis & R. B. Olsen, (2010). "Patterns in high-frequency FX data: discovery of 12 empirical scaling laws," Quantitative Finance, Taylor & Francis Journals, vol. 11(4), pages 599-614.

Tsang, Edward P. K. (2017). “Directional Changes: A New Way to Look at Price Dynamics”, Conference: International Conference on Computational Intelligence, Communications, and Business Analytics. 45-55. 10.1007/978-981-10-6427-2_4.

Tsang, Edward P. K. (2010). “Directional Changes, Definitions”, Working Paper, Centre for Computational Finance and Economic Agents (CCFEA), University of Essex.

Conclusion

The results look quite good. You can use a more complex strategy or a strategy with more edge than what our second strategy had. This would improve the strategy metrics!

The DC indicators are a good way to find patterns in data and the HMM can be of great help to get a slightly improved edge in our trading systems. Don’t forget to apply properrisk management in tradingfor every algorithm you develop. Remember: It’s not about returns, they’re almost unpredictable. It’s about managing risk.

You too can learn how to conductTechnical Analysis using Quantitative Methodsin our course on Quantra which includes a series of curated courses to help you develop proficiency. Get started now!

File in the download:

Directional Change in Trading - Python code

Login to Download

Author:José Carlos Gonzáles Tanaka

Disclaimer: All investments and trading in the stock market involve risk. Any decision to place trades in the financial markets, including trading in stock or options or other financial instruments is a personal decision that should only be made after thorough research, including a personal risk and financial assessment and the engagement of professional assistance to the extent you believe necessary. The trading strategies or related information mentioned in this article is for informational purposes only.

---

*Imported from QuantInsti Blog on 2026-04-27*
