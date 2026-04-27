---
title: "Risk Parity Portfolio: Strategy, Example & Python Implementation"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/risk-parity-portfolio/"
date: "2025-09-02"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Risk Parity Portfolio: Strategy, Example & Python Implementation

**来源**: [QuantInsti](https://blog.quantinsti.com/risk-parity-portfolio/)  
**日期**: 2025-09-02  
**作者**: QuantInsti

---

## 原文

Building a Robust Portfolio with Risk Parity

ByMohak Pachisia

Most investors focus on picking stocks, butasset allocation, how you distribute your investments, matters even more. While poor allocation can cause concentrated risks, a methodical approach to allocation would lead to a more balanced portfolio, better aligned with the portfolio objective.

This blog explains whyRisk Parityis a powerful strategy. Unlike equal-weighting or mean-variance optimisation, Risk Parity allocates based on each asset’s risk (volatility), aiming to balance the portfolio so thatno single asset dominates the risk contribution.

A practical Python implementation shows how to build and compare anEqual-Weighted Portfolio vs. a Risk Parity Portfoliousing the Dow Jones 30 stocks.

Key results:

Risk Parity outperformswith higher annualized return (15.6% vs. 11.5%), lower volatility (9.9% vs. 10.7%), better Sharpe ratio (1.57 vs. 1.07), and smaller max drawdown (-4.8% vs. -5.8%).

While compelling, Risk Parity depends on historical volatility, it needs frequent rebalancing, and may underperform in certain market conditions.

To get the most out of this blog, it’s helpful to be familiar with a few foundational concepts.

Pre-requisites

First, a solid understanding of Python fundamentals is essential. This includes working with basic programming constructs as well as libraries frequently used in data analysis. You can explore these concepts in-depth throughBasics of Python Programming.

Since the blog builds on financial data handling, you’ll also need to be comfortable with stock market data analysis. This involves learning how to obtain market datasets, visualise them effectively, and perform exploratory analysis in Python. For this, check outStock Market Data: Obtaining Data, Visualization & Analysis in Python.

By covering these prerequisites, you’ll be well-prepared to dive into the concepts discussed in this blog and apply them with confidence.

Table of contents

What is Asset Allocation?

How Can We Solve This Allocation Imbalance?

Risk Parity Allocations Process in Python

Frequently Asked Questions

A Note on Limitations

Ever wondered where your portfolio's risk is coming from?

Most investors focus heavily on picking the right stocks or funds, but what if thewayyou allocate your capital is more important than the assets themselves? Research consistently shows thatasset allocationis the key driver of long-term portfolio performance. For example, Vanguard has published multiple papers reinforcing that asset allocation is the dominant factor in portfolio performance.

In this post, we take a closer look atRisk Parity, a smart and systematic approach to portfolio construction that aims to balance risk, not just capital. Instead of letting one asset class dominate your portfolio's risk, Risk Parity spreads exposure more evenly, potentially leading to greater stability across market cycles.

Quantitative Portfolio Management is a 3-step process.

Asset selection

Asset Allocation

Portfolio rebalance and monitoring

In modern portfolio theory, research has shown that “Asset Allocation” has played a major role in portfolio performance. We will understand Asset Allocation in-depth and then move to understanding one of the possible ways to allocate assets, the Hierarchical Risk Parity method.

What is Asset Allocation?

Let us take an example of a novice investor. This investor has a portfolio of 5 stocks and has invested $30,000 in them.

How he/she bought specific proportions of the stocks could depend on subjective analysis or on the funds they have now to buy shares. And this leads to a random exposure of different stocks. As given below, let’s assume that the novice investor is buying stocks, and this is how the allocation looks:

Note: Some of the numbers below could be approximations, for demonstration purposes.

Stocks

Prices

Shares

Exposure

As a result, the proportion of each stock bought would widely vary.

Note: The number of shares is not a whole number. The calculations are approximations only for demonstration purposes.

Stocks

Prices

Shares

Exposure

% weights

We clearly see that NVDA has a significantly higher weightage of 39% while APPL has merely a weightage of 6%. There is a great disparity in the allocation of funds across the different stocks.

Case 1: NVDA underperforms; it will have a significant impact on your portfolio. Which could lead to large drawdowns, and this is high idiosyncratic risk.

Case 2: APPL outperforms, due to a much lower weightage of the stock in your portfolio. You won’t benefit from it.

How Can We Solve This Allocation Imbalance?

Quantitative Portfolio Managers do not allocate funds based on subjectivity. It is industry practice to adopt logical, tested, and effective ways to do it.

Uneven fund allocation can expose your portfolio to concentrated risks. To address this, several systematicasset allocation strategieshave been developed. Let’s explore the most notable ones:

1. Equal Weighting:

Approach: Assigns equal capital to each asset.

Note: The number of shares is not a whole number. The calculations are approximations only for demonstration purposes.

Stocks

Prices

Shares

Exposure

% weights

Pros:Simple, intuitive, and reduces concentration risk.

Cons:Ignores differences in volatility or asset correlation. May overexpose to riskier assets.

Real world example:MSCI World Equal Weighted Index

2. Mean-Variance Optimisation (MVO)

Approach: Based on Modern Portfolio Theory, it aims tomaximise expected returnfor a given level of risk. Though it looks simple, this approach is followed by several fund managers; its effectiveness comes with periodically rebalancing the portfolio exposures :

Expected returns

Asset volatilities

Covariances between assets

Note: The number of shares is not a whole number. The calculations are approximations only for demonstration purposes.

Stocks

Expected Return (%)

Volatility (%)

Optimised Weight (%)

Exposure ($)

Shares

Monte Carlo simulationis often used to test portfolio robustness across different market scenarios. To understand this method better, please readPortfolio Optimisation Using Monte Carlo Simulation.

The plot below shows an example of how portfolios with different expected returns and volatilities are created using the Monte Carlo Simulation method. Thousands, if not more, combinations of weights are considered in this process. The portfolio weights with the highest Sharpe ratio (marked as+) are often taken as the portfolio with the most optimal weightages.

Note: This is only for demonstration purposes, not for stocks used for our example.

Pros:Theoretically optimal: When inputs are accurate, MVO can construct the most efficient portfolio on the risk-return frontier.

Cons: Highly sensitive to input assumptions, especially expected returns, which are difficult to forecast.

3. Risk-Based Allocation: Risk Parity

Approach: Instead of allocating capital equally or based on returns, Risk Parity allocates based onrisk contributionfrom each asset. The goal is for each asset to contribute equally to the total portfolio volatility. The process to achieve this includes the following steps.

Estimate each asset’s volatility

Compute the inverse of volatility (i.e., lower volatility → higher weight).

Normalise the inverse of volatility to get final weights.

What is volatility?

Volatility refers to the degree of variation in the price of a financial instrument over time. It represents the speed and magnitude of price changes, and is often used as a measure of risk.

In simple terms,higher volatility means greater price fluctuations, which can imply more risk or more opportunity.

Formula for Standard Deviation:

$$\sigma = \sqrt{\frac{1}{N-1}\sum_{i=1}^N (r_i - \bar{r})^2}$$

Inverse of Volatility:

The inverse of volatility is simply the reciprocal of volatility. It is often used as a measure of risk-adjusted exposure or to allocate weights inversely proportional to risk in portfolio construction.

σ=Volatility

Then theInverse of Volatilityis:  1/σ

Normalise the inverse of volatility to get final weights :

To determine the final portfolio weights, we take the inverse of each asset's volatility and then normalise these values so that their sum equals 1. This ensures assets with lower volatility receive higher weights while maintaining a fully allocated portfolio.

Example of Risk Parity weighted approach(applying the above approach):

The number of shares is not a whole number. The calculations are approximations only for demonstration purposes.

Stocks

Prices

Volatility (%)

1 / Volatility

Risk Parity Weight (%)

Exposure ($)

Shares

0.0417

18.50%

22.20%

0.0556

24.60%

0.0357

15.80%

0.0333

18.90%

30,000

Result:No single asset dominates the portfolio risk.

Volatility is an example based on an assumed % standard deviation.

“Risk Parity Weight” is proportional to 1 / volatility, normalised to 100%.The exposure is calculated as: Risk Parity Weight × Total Capital.

Shares = Exposure ÷ Price.

Does not rely on expected returns.

Simple, robust, and uses observable inputs.

Reduces portfolio drawdowns during volatile periods.

May overweight low-volatility assets (e.g., bonds), underweight growth assets.

Ignores correlations between assets (unlike HRP).

Other Allocation Methods to Know:

Method

Core Idea

Hierarchical Risk Parity (HRP)

Uses clustering to detect asset relationships and allocates risk accordingly.

Solves problems of MVO like overfitting and instability.

Minimum Variance Portfolio

Allocates to minimise total portfolio volatility.

Can be very conservative — often heavy on low-volatility assets.

Maximum Diversification

Maximises the diversification ratio (return per unit of risk).

Intuitive for reducing dependency on any one asset.

Black-Litterman Model

Enhances MVO by combining market equilibrium with investor views.

Helps stabilise MVO with more realistic inputs.

Factor-Based Allocation

Allocates to risk factors (e.g., value, momentum, low volatility).

Popular in smart beta and institutional portfolios.

Risk Parity Allocations Process in Python

Step 1: Let’s start by importing the relevant libraries

Step 2: We fetch the data for 30 stocks using their Yahoo Finance ticker symbols.

These 30 stocks are the current 30 constituents of the Dow Jones Industrial Average Index.

We fetch the data from one month before 2024 begins. And target a window of the entire year 2024. This is done because we use a 20-day rolling period to compute volatilities and rebalance the portfolios. 20 trading days roughly translates to one month.

Only the “Close” prices are extracted, and the data frame is flattened for further analysis.

Step 3: We create a function to compute the returns of portfolios that are either equally weighted or weighted using the Risk Parity approach.

Purpose:To compute a portfolio's cumulative NAV (Net Asset Value) using equal-weighted or risk-parity rebalancing at fixed intervals.

price_df: DataFrame containing historical price data of multiple assets, indexed by date.

rebalance_period (default = 20):Number of trading days between each portfolio rebalancing.

method (default = 'equal'):Portfolio weighting method - either 'equal' for equal weights or 'risk_parity' for inverse volatility weights.

Step-by-Step Logic

Daily Returns Calculation:The function starts by computing daily returns usingpct_change()on the price data and dropping the first NaN row.

Daily Returns Calculation:The function starts by computing daily returns usingpct_change()on the price data and dropping the first NaN row.

Rolling Volatility Estimation:A rolling standard deviation is computed over the rebalance window to estimate asset volatility. To avoid look-ahead bias, this is shifted by one day using.shift(1).

Rolling Volatility Estimation:A rolling standard deviation is computed over the rebalance window to estimate asset volatility. To avoid look-ahead bias, this is shifted by one day using.shift(1).

Start Alignment:The earliest date all rolling volatility is available is identified. The returns and volatility DataFrames are trimmed accordingly.

Start Alignment:The earliest date all rolling volatility is available is identified. The returns and volatility DataFrames are trimmed accordingly.

NAV Initialisation:A new Series is created to store the portfolio NAV, initialised at 1.0 on the first valid date.

NAV Initialisation:A new Series is created to store the portfolio NAV, initialised at 1.0 on the first valid date.

Rebalance Loop:The function loops through the data in windows ofrebalance_perioddays:

Rebalance Loop:The function loops through the data in windows ofrebalance_perioddays:

Volatility and Weights on Rebalance Day:On the first day of each window:

Volatility and Weights on Rebalance Day:On the first day of each window:

For'equal': assigns equal weights to all assets.

For'equal': assigns equal weights to all assets.

For'risk_parity': assigns weights inversely proportional to asset volatility.

For'risk_parity': assigns weights inversely proportional to asset volatility.

Cumulative Returns & NAV Computation:The window’s cumulative returns are calculated and combined with weights to compute the NAV path.

Cumulative Returns & NAV Computation:The window’s cumulative returns are calculated and combined with weights to compute the NAV path.

NAV Normalisation:The NAV is normalised to match the last value of the previous window, ensuring smooth continuity.

NAV Normalisation:The NAV is normalised to match the last value of the previous window, ensuring smooth continuity.

Final Output:Returns a time series of the portfolio’s NAV, excluding any missing values.

Step 4: Portfolio Construction

We now proceed to construct two portfolios using the historical price data. This involves calling the portfolio construction function defined earlier. Specifically, we generate:

An Equal-Weighted Portfolio, where each asset is assigned the same weight at every rebalancing period.

A Risk Parity Portfolio, where asset weights are determined based on inverse volatility, aiming to equalise risk contribution across all holdings.

Both portfolios are rebalanced periodically based on the specified frequency.

Step 5: Portfolio Performance Evaluation

In this step, we evaluate the performance of the two constructed portfolios: Equal-Weighted and Risk Parity, by computing key performance metrics:

Daily Returns:Calculated from the cumulative NAV series to observe day-to-day performance fluctuations.

Annualised Return:Derived using the compound return over the entire investment period, scaled to reflect yearly performance.

Annualised Volatility:Estimated from the standard deviation of daily returns and scaled by the square root of 252 trading days to annualise.

Sharpe Ratio:A measure of risk-adjusted return, computed as the ratio of annualised return to annualised volatility, assuming a risk-free rate of 0.

Maximum Drawdown:The maximum observed peak-to-trough decline in portfolio value, indicating the worst-case historical loss.

These metrics offer a comprehensive view of how each portfolio performs in terms of both return and risk. We also visualise the cumulative NAVs of both portfolios to observe their performance trends over time.

Frequently Asked Questions

What exactly is Risk Parity?

Risk Parity is a portfolio allocation strategy that assigns weights such that each asset contributes equally to the total portfolio volatility, rather than simply allocating equal capital to each asset. The goal is to prevent any single asset or asset class from dominating the portfolio’s overall risk exposure.

How does it differ from Equal Weighting or Mean-Variance Optimisation?

Equal Weighting:This method allocates the same amount of capital to each asset. It is simple and intuitive, but does not consider the risk (volatility) of each asset, potentially leading to concentrated risk.

Mean-Variance Optimisation (MVO):Based on Modern Portfolio Theory, MVO seeks to maximise expected return for a given level of risk by considering expected returns and covariances. However, it is highly sensitive to the accuracy of input forecasts.

Risk Parity:Instead of focusing on returns or allocating equal capital, Risk Parity adjusts weights based on the volatility of each asset, allocating more capital to lower-volatility assets to equalise their risk contributions.

Why is asset allocation so important?

Research has shown that asset allocation is the primary driver of long-term portfolio returns, far more significant than selecting individual securities. A well-thought-out allocation helps manage risk and enhances the likelihood of meeting investment goals.

How is volatility calculated in Risk Parity?

Volatility is typically measured as the standard deviation of past returns over a rolling window (for example, a 20-day rolling standard deviation). In Risk Parity, assets with lower volatility are assigned higher weights to balance their contribution to total portfolio risk.

Is there Python code to implement this?

Yes. The blog provides complete Python code examples using libraries such as pandas for data handling, yfinance for fetching historical prices, and custom functions to rebalance portfolios either by equal weights or by inverse volatility (Risk Parity).

Does Risk Parity always outperform other strategies?

No. While Risk Parity often leads to more stable performance and better risk-adjusted returns, especially in diversified or volatile markets, it may underperform simpler strategies like Equal-Weighted portfolios during strong bull markets that favour high-risk assets.

What are the limitations of Risk Parity?

It relies on the historical volatility to set target weights, which may not accurately reflect  the future behaviour of assets, especially during abrupt changes or crises.

It typically requires frequent rebalancing, which can increase transaction costs and potential slippage.

It may under-allocate to high-growth assets in trending markets, limiting upside in strong rallies.

Are there more advanced methods beyond standard Risk Parity?

Yes. For example,Hierarchical Risk Parity (HRP)uses clustering to understand asset relationships and aims to allocate risk more efficiently by addressing some of the weaknesses of traditional mean-variance approaches, such as instability due to input sensitivity.

Conclusion

The comparative analysis highlights the clear advantages of using aRisk Parityapproach over a traditionalEqual-Weightedportfolio. While both portfolios deliver positive returns, Risk Parity stands out with:

Higher Annualised Return(15.60% vs. 11.47%)

Lower Volatility(9.90% vs. 10.72%)

Superior Risk-Adjusted Performance, as seen in theSharpe Ratio(1.57 vs. 1.07)

Smaller Max Drawdown(-4.76% vs. -5.83%)

These results demonstrate that by aligning portfolio weights with asset risk (rather than capital), the Risk Parity portfolio may enhance return potential along with better downside protection and smoother performance over time.

TheNAV chartfurther reinforces this conclusion, showing a more consistent and resilient growth trajectory for the Risk Parity strategy.

In summary, for investors prioritising stability over growth, Risk Parity offers a compelling alternative to conventional allocation methods.

A Note on Limitations

Although the Risk Parity portfolio delivered stronger returns during the period taken in our example, its performance advantage is not assured in every market phase. Like any strategy, Risk Parity comes with limitations. It relies heavily on historical volatility estimates, which may not always accurately reflect future market conditions, especially during sudden regime shifts or extreme events.

It tends to shine in portfolios that mix high‑ and low‑volatility assets, like stocks and bonds, where equal capital allocation would otherwise concentrate risk.However, if low‑volatility assets underperform or if all assets have similar risk profiles,

Additionally, the strategy often requires frequent rebalancing, which can increase transaction costs and introduce slippage. In strong directional markets, particularly those favouring higher-risk assets, simpler strategies like Equal-Weighted may outperform due to their greater exposure to momentum.

Hence, while Risk Parity provides a systematic way to balance portfolio risk, it should be used with an understanding of its assumptions and practical limitations.

Next Steps:

After reading this blog, you may want to enhance your understanding of portfolio design and explore techniques that provide more structure to risk-return trade-offs.

A good place to begin is withPortfolio Variance/Covariance Analysis, which explains how asset correlations impact portfolio volatility. This will provide you with the foundation to understand why diversification works and where it doesn’t.

From there,Portfolio Optimisation Using Monte Carlo Simulationintroduces a more dynamic approach. By running thousands of simulated outcomes, you can test how different allocations behave under uncertainty and identify combinations that balance risk and reward.

To round it off,Portfolio Optimisation Methodswalks through a range of optimisation frameworks, covering classical mean-variance models as well as alternative methods, so you can compare their strengths and apply them in different market conditions.

Working through these next steps will equip you with practical techniques toanalyse, simulate, and optimise portfolios, a skill set that’s critical for anyone looking to manage capital with confidence.

You can explore all of these in detail in thePortfolio Management & Position Sizing Learning Track, which includes theQuantitative Portfolio Managementcourse for a comprehensive understanding of portfolio construction and optimisation.

For those looking to expand beyond portfolio theory into the broader realm ofsystematic trading, check theExecutive Programme in  Algorithmic Trading - EPAT. Its comprehensive curriculum, led by top faculty like Dr. Ernest P. Chan, offers a leading Python algorithmic trading course for career growth. EPAT covers core trading strategies that can be adapted and extended to High-Frequency Trading. Get personalised support for specialising in trading strategies with live project mentorship.

Disclaimer: This blog post is for informational and educational purposes only. It does not constitute financial advice or a recommendation to trade any specific assets or employ any specific strategy. All trading and investment activities involve significant risk. Always conduct your own thorough research, evaluate your personal risk tolerance, and consider seeking advice from a qualified financial professional before making any investment decisions.

---

*Imported from QuantInsti Blog on 2026-04-27*
