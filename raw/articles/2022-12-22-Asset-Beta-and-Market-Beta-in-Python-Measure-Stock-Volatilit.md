---
title: "Asset Beta and Market Beta in Python | Measure Stock Volatility"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/asset-beta-market-beta-python/"
date: "2022-12-22"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Asset Beta and Market Beta in Python | Measure Stock Volatility

**来源**: [QuantInsti](https://blog.quantinsti.com/asset-beta-market-beta-python/)  
**日期**: 2022-12-22  
**作者**: QuantInsti

---

## 原文

Asset Beta and Market Beta in Python

ByChainika Thakarand Jay Maniar

‘Beta’ in the stock market and how we can use beta effectively to hedge against market risk. We will also see how to calculate the beta of any stock in python. So let us begin, by understanding a few basic questions that should come to our mind before we start coding in python.

Let us find it all out with this blog that covers:

What is beta?

Example of beta

What is asset beta?

Formula of asset beta

Equity beta

Formula for calculating beta

Types of beta values

How to calculate beta?

Limitations of beta

What is beta?

The volatility that a benchmark portfolio (S&P 500 index) or a market portfolio exhibits is known as systematic risk.

Beta is the historical measure ofrisk of any individual stockor portfolio against the risk of the market portfolio. In other words, it measures the volatility of any security with respect to the overall market volatility.

Example of beta

Let us consider the following example to understand beta intuitively.

Consider the daily returns of Google Inc. If it is said the beta of the Google stock is 1.5, then it means that Google is 50% more volatile than the market. So if the intraday return of the market is a positive 10%, then the intraday return on Google stock would be 15%.

In other words, the returns on Google stock will outperform the market by 50% and the alpha on Google would be 5%.

Now, if the market declines by 5%, then Google will decline by 7.5% or 50% more than the market. Google’s change in market value is multiplied by its beta to estimate its movement in future. Hence, Google is a high beta stock.

Similarly, if the beta of any stock is say 0.75, then it will be less volatile than the market. If the intraday gains of the market are 10%, a low-beta stock will gain only 7.5%. Low-beta stocks are very useful to mitigate market risk.

This is because, if the market declines by 5%, then the stock will decline by only 3.75%. This is less than the benchmark decline as opposed to the decline by Google where the market fell by 5%.

To begin, let us import the data in python and plot the daily returns of Google and the S&P 500 index.

Output:

What is asset beta?

Asset beta, also known as the volatility of returns, is the beta of a company without the impact of debt. It compares the risk of a company to the risk of the market.

Formula of asset beta

Here is the formula for asset beta:

Equity beta

Equity beta is a measurement that compares the volatility of a particular stock against the volatility of the market. In other words, it is a measure of risk, and it includes the impact of a company’s capital structure and leverage. Equity beta allows investors to gauge how sensitive security might be to macro-market risks.

For example, a company with a beta of 1.5 has returns that are 150% as volatile as the market it’s being compared to.

Formula for calculating beta

Beta is calculated using regression analysis. Numerically, it represents the tendency for a stock’s returns to respond to the volatility of the market. The formula for calculating beta is the covariance of the return of an asset with the return of the benchmark divided by the variance of the return of the benchmark over a certain period.

$$Beta = \frac{Variance}{Covariance}$$

Types of beta values

Let us now see the types of beta values which are:

Beta Value Equal to One

Beta Value Between Zero to One

Beta Value Greater Than One

Negative Beta Value

Beta Value Equal to One

Beta value of one indicates that the stock price is strongly correlated with the market. Adding a stock to a portfolio with a beta of one doesn’t add any additional risk to the portfolio. Simultaneously, it also doesn’t increase the likelihood that the portfolio will provide a higher return than what was expected before adding the stock with a beta of one.

Beta Value Between Zero to One

A beta value between zero to one means that the stock is less volatile than the market. The risk factor would be lower in a portfolio with low beta stock as compared to a portfolio without such stocks.

Beta Value Greater Than One

A beta that is greater than one indicates that the stock is more volatile than the market. This implies that adding the stock to the portfolio will increase the portfolio’s risk, but at the same time, the tendency for higher expected returns also increases.

Negative Beta Value

The stock with a negative beta could be thought of as the opposite of benchmark trends. These stocks tend to do better when the entire market goes down and do worse when the market is up. Put options, inverse ETFs, and gold tend to have negative betas.

How to calculate beta?

One of the most common ways to calculate beta is using theCapital Asset Pricing Modelor CAPM.

Have a look at the CAPM model:

E (Ra) = Rf + Ba [ E (Rm) - Rf]

Where,E (Ra) = Expected returns of assetRf = risk-free returnBa = Asset’s betaE (Rm) = Expected market return

CAPM model states that the expected return of an asset ‘E (Ra)’ is equal to the risk-free return in the market plus the difference between the expected return of the market and risk-free rate ‘[E (Rm) - Rf]’ multiplied by the asset’s beta ‘Ba’.

If we have all the values except the asset’s beta, we can calculate the beta using:

Ba = [E (Ra) - Rf] / [ E (Rm) - Rf]

We can even find the beta by performing ‘regression analysis'.

When one tries to capture a mathematical relationship between ‘x’ and ‘y’ variables, by fitting a line, polynomial, or a curve through scatter plots, such that one can make a reasonably good prediction of  ‘y’ for the given ‘x’, then the mathematical process of deriving such an equation between x and y is called the regression analysis.

This equation can also be arrived at by using amachine learning-based regression model.

If we try to fit a line through this scatter plot that “best fit” explains the observed values of ‘y’ in terms of observed values of ‘x’, we get a simple linear regression model.

Linear regression assumes a linear relationship between the dependent and independent variables. The following regression equation describes that relation:

Yi = b0 + b1 Xi + ei

We refer to the intercept ‘b0’ and slope coefficient ‘b1’ as the regression coefficients, Xi as the independent variable and ei as the random error.

Now, consider this equation:

Rasset = ex-post alpha + beta of asset *  Rbenchmark + ei

To understand the coefficients more intuitively, if we consider the returns for Google vs. S&P 500 index, then the slope coefficient in a regression line is called the stock’s beta, as it measures the relative amount of systematic or non-diversifiable risk in Google’s returns.

If the slope of Google returns is more than 1, its returns tend to increase or decrease more than the market returns. A slope or beta of 1 would have the same level of systematic risk as that of the market on average, and a slope or beta of less than 1 implies that the change in returns is relatively low as compared to the change in the market returns.

The intercept term is the ex-post alpha i.e., the measure of excess returns of Google as compared to market index returns. If the intercept term is negative, it means Google has underperformed S&P on a risk-adjusted basis and a positive intercept means it has generated excess returns on a risk-adjusted basis.

All the points on the regression equation line, predict the ‘y’ values for the corresponding ‘x’ values. However, the optimal regression line is the one for which the sum of the squared differences (vertical distances) or the sum of squared errors or SSE between the ‘y’ values predicted by the regression equation/line and the actual ‘y’ values is minimal.

Thus, the regression line minimises the SSE. This is the reason why simple linear regression is also called Ordinary Least Squares or OLS, and the estimated (predicted) values by the regression equation i.e. the predicted y-values are called least squares estimates.

The slope coefficient ‘b1’ of the regression line is calculated as the covariance of x and y divided by the variance of x (covxy /σ2x ), and the intercept coefficient is the line's intersection with the y axis at x = 0.

Consider the following code to calculate Google’s beta against S&P 500.

Output:

alpha: 0.0009286480528358054
beta: 1.0083060312551573

Output:

We have calculated the beta of Google as 1.00. You may try this with other stocks.

We can even hedge Google's beta with respect to the S&P 500 beta. This is known as beta hedging.

Limitations of beta

Even though the beta is a widely used measure of systematic risk it is exposed to certain limitations.

One of the most prominent limitations is that it does not incorporate new information.

Consider a utility company: let's call it Company X. Company X has been considered a stock with a low beta. When it entered the merchant energy business and assumed more debt, X's historical beta no longer captured the substantial risks the company took on.

At the same time, many stocks that are relatively new to the market have insufficient price history to establish a reliable beta.

Another drawback is that even though past data can be a good predictor of future performance, it does not guarantee the same performance.

I must mention in the end that despite the most prominent limitation being the historical data, the risk measurement is best done with the historical data. Also, the analysis done on the historical data has proved to be quite useful for traders and investors alike.

Conclusion

We learned all about the basics of beta and the calculation of beta in this blog. Beta is an efficient and reliable tool for measuring the risk of your investment against market risk. Calculating beta helps a trader get a fair idea of the risk that a particular stock or portfolio is exposed to.

Some stocks increase the potential risk of a portfolio while others reduce the risk. Whereas, some stocks are neutral. Also, there are some stocks which move in the opposite direction from the market having a negative beta.

If you wish to learn more about beta stocks, you can enrol in our course onVolatility Trading Strategies for Beginners. This course will help you be more confident about trading without fearing volatility. Also, this course will help to set dynamic stop loss and take profit levels, hedge your portfolio using VIX and select stocks in your portfolio.

Download Data File

Beta.py

Login to Download

Note: The original post has been revamped on23rdDecember2022 for accuracy, and recentness.

Disclaimer: All investments and trading in the stock market involve risk. Any decision to place trades in the financial markets, including trading in stock or options or other financial instruments is a personal decision that should only be made after thorough research, including a personal risk and financial assessment and the engagement of professional assistance to the extent you believe necessary. The trading strategies or related information mentioned in this article is for informational purposes only.

---

*Imported from QuantInsti Blog on 2026-04-27*
