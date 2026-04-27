---
title: "Measuring Risk and Return of a Portfolio: A Comprehensive Guide to Portfolio Analysis"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/portfolio-analysis-calculating-risk-returns/"
date: "2023-04-10"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Measuring Risk and Return of a Portfolio: A Comprehensive Guide to Portfolio Analysis

**来源**: [QuantInsti](https://blog.quantinsti.com/portfolio-analysis-calculating-risk-returns/)  
**日期**: 2023-04-10  
**作者**: QuantInsti

---

## 原文

Portfolio Analysis: Calculating Risk and Returns, Strategies and More

ByChainika Thakar&Mandeep Kaur

The process of trading with a portfolio of stocks requires a number of steps like stock selection, the formation ofstrategies while creating a portfolioand so on. In this blog, we will cover all about portfolio analysis, the tools to compute risks over returns and the relationship between the risks and returns.

Let us find it all out with this blog that covers:

What is a portfolio?

What is a portfolio analysis?

What are the tools of portfolio analysis?

What do you mean by risks in trading?

Relationship between risk and return (risk-return trade off)

How to avoid the risks in trading?

Common mistakes made by traders during portfolio analysisOverreacting to short-term market fluctuationsNot investing according to your risk appetiteFailing to rebalance portfolios with proper techniquesNot diversifying the portfolio

Overreacting to short-term market fluctuations

Not investing according to your risk appetite

Failing to rebalance portfolios with proper techniques

Not diversifying the portfolio

Strategy for allocation of stocks in a portfolioExpected return on a single stockRisk (or variance) on a single stockExpected return on an n-stock portfolio

Expected return on a single stock

Risk (or variance) on a single stock

Expected return on an n-stock portfolio

What is a portfolio?

A portfolio is a collection of financial instruments such as stocks, bonds, cash equivalents, or funds held by an individual, investment company or financial institution. An investment portfolio can be regarded as a pie which is divided into various parts, each representing a financial instrument with the objective of achieving a particular level of risk and return.

Investors should construct a portfolio according to the investment objectives, risk tolerance, and time frame.

Example:Suppose you want to invest $100,000 in the financial market then your portfolio may look like this.

Investor’s portfolio

Investment

Percentage

Security

Returns

Government Bonds

$25,000

Banks’ Fixed Deposits

$15,000

Average

Shares

$35,000

Mutual Funds

$25,000

Average

Average

1,00,000

What is a portfolio analysis?

Portfolio analysis is one of the areas of investment management that enables market participants to analyze and assess the performance of a portfolio (equities, bonds, alternative investments, etc.).

Portfolio analysis is intended to measure performance on a relative and absolute basis along with its associated risks.

Portfolio Performance Evaluation

6 min read

What are the tools of portfolio analysis?

There are some tools orcalculation ratiosto be used for conducting the portfolio analysis. These tools and ratios are also core components of a well-structuredalgorithmic trading course, where portfolio analysis is taught alongside strategy building and risk management. These tools are:

1) Holding Period Return

It calculates the overall return during the investment holding period.

Holding Period Return ={(Ending Value–Beginning Value)+Dividends Received}/Beginning Value

2) Arithmetic Mean

It calculates the average returns of the overall portfolio.

$$Arithmetic Mean = (R_1 + R_2 + R_3 +……+ R_n) / n$$

where,R = Returns of Individual Assets

3) Sharpe Ratio

It calculates the excess returns over and above the risk-free return per unit of portfolio risk.

Sharpe Ratio Formula = (Expected Return – Risk-Free rate of return) / Standard Deviation

4) Alpha

It calculates the difference between the actual portfolio returns and the expected returns.

Alpha of portfolio = Actual rate of return of portfolio – Expected Rate of Return on Portfolio

5) Tracking Error

It calculates thestandard deviationof the excess return concerning the benchmark rate of return.

$$Tracking Error Formula = R_p-R_b$$

$$where,R_p = Return of Portfolio,R_b = Return on Benchmark$$

6) Information Ratio

It calculates the success of the active investment manager’s strategy by calculating excess returns and dividing it by the tracking error.

$$Information ratio Formula = (R_p – R_b) / Tracking error$$

$$where,R_p = Return of Portfolio,R_b = Return on Benchmark$$

7) Sortino Ratio

It calculates the excess return over and above the risk-free return per unit of negative asset returns.

$$Sortino Ratio Formula = (R_p – R_f) / σ_d$$

$$where,R_p = Return of Portfolio,R_f= Risk-Free Rate,σ_d = standard deviation of negative asset returns$$

What do you mean by risk in trading?

While finding out the trading risks one needs to know the different variables at play in the market.

These variables can be economic factors such as decisions on the interest rates by the central bank or a trade war.

While making our trading decisions, we must ensure that we are taking into consideration those economic factors which can affect our assets.

Here, we are considering the power of these factors to create possible price fluctuations of these assets and if they actually do affect the prices a lot then we must know the frequency of these factors.

Finding out these important points will help us with identifying factors that act as a potential threat to the portfolio. This way, we can be prepared to tackle the risky scenarios in the market with the help of practices such as hedging, investing in options, diversification of assets into low risk and high risk etc. To better understand how options are used for risk management, learningoptions trading basicscan provide a solid foundation.

Relationship between risk and return (risk-return trade off)

The correlation between the risks and the performance of investments (or the returns) is known as the risk-return tradeoff. The risk-return tradeoff states the higher the risk, the higher the reward and vice versa.

Hence, the low levels of risks are associated with low potential returns and high levels of risks with high potential returns. According to the risk-return tradeoff, invested money can render higher profits only if the investor will accept a higher possibility or probability of losses.

How to avoid the risks in trading?

The mostpopular risk management techniquesand elements to make your trades successful while evading risks are as follows:

Portfolio optimisation - Portfolio optimisation is the process of constructing portfolios to maximize expected return while minimizing risk.

Hedging - It is an investment strategy designed to offset a potential loss. In other words, hedging is investing to reduce the risk. Hedging against market price risk means protecting yourself from adverse movements in prices by attaining a price lock.

1% and 2% investing rule - 1% and 2% rule in trading imply the maximum amount of the risk which is feasible per trade should be either 1% or 2%.

Quantitative Portfolio Management

Additional 27% off

This helps you to avoid an excessive loss that may happen otherwise. Hence, no more than 1% or 2% of capital should be risked on a single trade. This is usually possible withday trading.

Monitoring the trade while utilising advanced technology - It is very important that you monitor your trades. Monitoring the trade can be done byalgorithmic trading.

Avoiding unclear trade setups - An unclear trade setup takes place when one of your indicators agrees to a certain trading position but others do not. For instance, if you are using moving average indicators (like EMA) or Bollinger bands, etc., one of them may show a clear trade setup but does not agree with the trade setups of other indicators which creates confusion.

Stop loss - Stop loss is a buy or sell order which gets triggered when the stock price reaches a specified price known as the stop price. Stop loss is extremely useful for the investor who doesn’t want to monitor the security on a continuous basis.

Common mistakes made by traders during portfolio analysis

Let us now find out the common mistakes committed by the traders while doing portfolio analysis. These mistakes are:

Overreacting to short-term market fluctuations

Although, algorithmic trading takes care of the “overreacting” part and “emotions” of the traders by automating the trade related actions and by taking positions with logic.

But, in case you are too fearful of the trades going against your favour, you may try intervening with the algorithms a lot and you may end up creating a new strategy every now and then.

This can lead to losses because in this case, you will be letting your emotions take over and not logic.

Not investing according to your risk appetite

Your risk appetite plays a huge role when it comes to allocating your capital across your portfolio. Most beginner investors tend to not factor in their risk tolerance level when creating a portfolio. This can prove to be a poor decision.

For instance, it doesn’t make sense for a conservative investor to invest in significantly riskier options like small-cap companies now, does it?

So, paying heed to some solid portfolio management advice, it is a good idea to first do a risk analysis on yourself to determine your risk tolerance. Once you’ve done that, you can move on to building a portfolio based on your risk appetite.

Failing to rebalance portfolios with proper techniques

Portfolio management is not a one-time action since the stocks need to be regularly monitored so that you keep getting expected returns. Many new traders might tend to think that once they have successfully constructed a portfolio, they do not need to do anything. But, in actuality, rebalancing the portfolio helps maintain such a combination of invested stocks which reap favourable returns.

For example, if one or more stocks in your portfolio are underperforming, it makes very little sense to hold onto them.

Therefore, you need to monitor the progress of your portfolio and may even have to make changes to its composition to accurately reflect your strategy.

Not diversifying the portfolio

While professional investors may be able to generate alpha (or excess return over a set benchmark) by investing in a few concentrated positions, beginners may not be as good at it.

Hence, it is wiser to stick to the principle of diversification. For example, when creating a stock portfolio, include all major sectors. It is preferable to avoid putting more than 5% to 10% in any one stock.

Strategy for allocation of stocks in a portfolio

Now, we will find out some strategies for allocating stocks in a portfolio which are:

Expected return on a single stock

The expected return of a portfolio provides an estimate of how much return one can get from their portfolio. And variance gives the estimate of the risk that an investor is taking while holding that portfolio. The returns and the risk of the portfolio depend on the individual stocks' returns and risks and their weightage/allocation in the portfolio.

Theparameters of the riskand return of any stock explicitly belong to that particular stock, however, the investor can adjust the return-to-risk ratio of his/ her portfolio to the desired level using certain measures. One such measure is to adjust the weights of the stocks in the investor’s portfolio.

Here we will discuss how the weights of individual stocks impact these two parameters of theportfolio. Consider a stock ABC. Let ri be the expected return on the stock and rx be any return having a probability of px. The expected return, ri, can be computed using the below equation. Learn more about howquantitative portfolio managementcan help enhance your skills.

Let us assume that ABC can generate the returns as per column A with corresponding probabilities given in column B. The expected return from ABC can be computed as shown in column C, which is the product of columns A and B.

Let us look at the code to compute the expected return of this stock. We start by importing the pandas library.

Output:

rx    px  px.rx
1   5  0.15   0.75
2   6  0.20   1.20
3   8  0.30   2.40
4   9  0.20   1.80
5  12  0.10   1.20
6  15  0.05   0.75
Expected Return is:  8.1 %

The expected return on the stock is 8.10% as per the calculations shown above. The returns in column A can be computed usingCapital Asset Pricing Model (CAPM).

Risk (or variance) on a single stock

The variance of the return on stock ABC can be calculated using the below equation.

The following table gives the computation of the variance using the same example taken above.

We can compute the variance of a single stock using python as:

Output:

rx    px  px.rx  rx-ri  variance
1   5  0.15   0.75   -3.1    1.4415
2   6  0.20   1.20   -2.1    0.8820
3   8  0.30   2.40   -0.1    0.0030
4   9  0.20   1.80    0.9    0.1620
5  12  0.10   1.20    3.9    1.5210
6  15  0.05   0.75    6.9    2.3805
The variance of the portfolio is:  6.39

Hence, the variance of the return of the ABC is 6.39. The standard deviation of the returns can be calculated as the square root of the variance.

Having computed the expected return and variance for one stock, we will now see how to calculate the return and variance of the portfolio. We use the expected return and variance of the portfolio to optimize it. We can adjust the weights of the stocks to maximize the return and minimize the standard deviation.

Expected return on an n-stock portfolio

Let us take an n-stock portfolio. Assume that the expected return from ith stock is ri. The expected return on the portfolio will then be:

The weight of any stock is the ratio of the amount invested in that stock to the total amount invested. For the below portfolio, the weights are shown in the table.

Let us see how we can compute the weights using Python for this portfolio.

Output:

stock  amount   weights
A     A     100  0.222222
B     B      60  0.133333
C     C     200  0.444444
D     D      50  0.111111
E     E      40  0.088889
The sum of weights is: 1

The sum of the weights of all the stocks in the portfolio will always be 1. Next, we will see the expected return on this portfolio.

The expected return of the portfolio can be computed as:

Output:

stock  amount   weights  stock_ret      wiri
A     A     100  0.222222          5  1.111111
B     B      60  0.133333         10  1.333333
C     C     200  0.444444          7  3.111111
D     D      50  0.111111          6  0.666667
E     E      40  0.088889          6  0.533333
The expected return from the portfolio is: 6.76

Covariances and correlation of returns

Before moving on to the variance of the portfolio, we will have a quick look at the definitions of covariance and correlation. Covariance (or correlation) denotes the directional relationship of the returns from any two stocks.

The magnitude of the covariance denotes the strength of the relationship. If covariance (or correlation) is zero, there is no relation and if the sign of covariance (or correlation) is negative, it indicates that if one stock moves in one direction the other will move in the other direction.

The equations to compute the covariance and correlation are given below.

Box method for Variance of a portfolio

For the variance of the portfolio, we will use the box method. For an n-stock portfolio, we will create an nXn matrix with all the stocks on X and Y axes as illustrated below. Each cell contains the product of the weights of the corresponding column and the covariance of the corresponding stocks.

Let us look at the stepwise procedure to use the box method for variance computation.

Output:

A     B     C     D     E    weight
A  6.39 -5.74  3.65 -1.36  9.25  0.222222
B  5.74  5.14  9.36  5.78 -8.52  0.133333
C  3.65  9.36  3.58  7.85  1.11  0.444444
D -1.36  5.78  7.85  4.87  7.25  0.111111
E  9.25 -8.52  1.11  7.25  4.63  0.088889

Output:

A         B         C         D         E   row_sum
A  0.315556 -0.170074  0.360494 -0.033580  0.182716  0.655111
B  0.170074  0.091378  0.554667  0.085630 -0.100978  0.800770
C  0.360494  0.554667  0.707160  0.387654  0.043852  2.053827
D -0.033580  0.085630  0.387654  0.060123  0.071605  0.571432
E  0.182716 -0.100978  0.043852  0.071605  0.036583  0.233778
The variance of the portfolio is: 4.31

The variance of the portfolio will be the sum of all the cells of this table. Hence, the variance of a two stock portfolio will be:

Special case of fully diversified portfolio

Now we will take a special case in which there are n stocks and the weights of all the stocks are equal. Hence, the weight of each stock will be 1/n. Using the above box method, we can write the sum of all the diagonal elements as:

After removing n diagonal elements, we are left with n2 – n elements. The sum of the remaining elements can be written as:

Hence, the variance of such a portfolio will be:

For a fully diversified portfolio, we can assume that we have added every possible stock in our portfolio. Therefore, n will tend to infinity and 1/n will tend to zero. So, the variance of a fully diversified portfolio will be the average of the covariances. So, we can say that diversification eliminates all risks except the covariance of the stocks, which is the market risk.

Conclusion

In this blog, we discussed the portfolio analysis including how the risks and returns are related to each other. Also, we discussed some measures that can help compute expected returns on a stock portfolio. You can also learn about an important concept in financial risk management known asVaR calculation.

If you want to learn various aspects of Algorithmic trading then check out the learning track onAlgorithmic trading for Beginners. The courses covered under this learning track are the best for any beginner aspiring to become an algorithmic trader. The courses cover training modules like Statistics & Econometrics, Financial Computing & Technology, and Algorithmic & Quantitative Trading.

Thesealgo trading coursesprovide foundational skills and insights that equip you to confidently enter the world of algorithmic trading. Each course offers practical learning tools and examples, making it easier to understand the strategies and technology driving modern trading.

Note: The original post has been revamped on 10th April 2023 for accuracy, and recentness.

Disclaimer: All data and information provided in this article are for informational purposes only. QuantInsti®makes no representations as to accuracy, completeness, currentness, suitability, or validity of any information in this article and will not be liable for any errors, omissions, or delays in this information or any losses, injuries, or damages arising from its display or use. All information is provided on an as-is basis.

---

*Imported from QuantInsti Blog on 2026-04-27*
