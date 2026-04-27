---
title: "Volatility And Measures Of Risk-Adjusted Return With Python"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/volatility-and-measures-of-risk-adjusted-return-based-on-volatility/"
date: "2023-01-18"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Volatility And Measures Of Risk-Adjusted Return With Python

**来源**: [QuantInsti](https://blog.quantinsti.com/volatility-and-measures-of-risk-adjusted-return-based-on-volatility/)  
**日期**: 2023-01-18  
**作者**: QuantInsti

---

## 原文

Volatility And Measures Of Risk-Adjusted Return With Python

ByChainika Thakar

Volatility is an important factor to consider for traders since volatility can greatly impact the returns of an investment. A volatile stock or the market can be taken care of with the help of measures to adjust the risk.

In this post, we will see how to compute historical volatility in Python and the different measures of risk-adjusted return based on it.

This blog covers:

What is meant by volatility?

Historical volatility

What is a risk-adjusted return in trading?

Purpose of risk-adjustment

Risk-adjusted return ratios in python

Pros of using the risk-adjusted return ratios

Cons of using the risk-adjusted return ratios

What is meant by volatility?

The upward and downward movement of a security over a period is called volatility. Volatility is one of the factors that define the risk of security. In general, the higher the volatility, the riskier the security. If the price of a security fluctuates slowly over a longer span of time, it is considered to be less volatile.

Conversely, If the price of a security fluctuates rapidly over a small span of time, it is considered to be more volatile. Volatility is measured best by calculating the standard deviation of the annualised returns over a period of time.

Volatility measures the dispersion of returns for given security. It plays a key role inoptions trading.

The main two volatilities are-

Implied volatility and

Historical volatility.

Implied volatility

Let us first talk about implied volatility. Implied volatility is the expected future volatility of the stock. Implied volatility shows the stock’s potential movement, but it doesn’t forecast the direction of the move. If the implied volatility is high, then it means that the market has priced in the potential for large price movements in either direction for the stock.

If the implied volatility is low, the price won’t move as much or may not make any unpredictable changes.

Implied volatility is one of the important deciding factors in the pricing ofoptions. As implied volatility increases, the value of options will increase. That is because an increase in implied volatility suggests an increased range of potential movement for the stock.

To gain a more comprehensive understanding of volatility and its impact on pricing, explore strategies like implied volatility analysis and GARCH modeling in our advancedoption volatilitycourse, designed to help refine your trading skills.

The implied volatility is derived from theBlack-Scholesformula by entering all the parameters needed to solve for the options price through the Black-Scholes Model and then taking the actual market price of the option and solving back for the implied volatility parameter. (Learn more about howadvanced volatility tradingcan help enhance your skills.)

Historical volatility

We will discuss historical volatility here since historical data can best determine a strategy’s performance based on past data.

Historical volatility is derived from time series of past price data, whereas implied volatility is derived using the market price of a traded derivative instrument like an options contract.

Let us see an example by computing the historical volatility of risk-adjusted return for NIFTY.

First, we use the log function from NumPy to compute the logarithmic returns using the NIFTY closing price. Then we use the rolling_std function from Pandas plus the NumPy square root function to calculate the annualised volatility.

The rolling function uses a window of 252 trading days. Each day in the selected lookback period is assigned an equal weight. The user can choose a longer or a shorter period as per his need.

Output:

The output above shows that the volatility was the highest between 2020-07 and 2021-06.

Watch this concise video to grasp options trading volatility, emphasizing gaining an edge, managing risk, estimating volatility, and practical application.

What is a risk-adjusted return in trading?

Risk-adjusted return is a calculation of the return (or potential return) on the trading of a financial instrument such as a stock. Risk-adjusted returns are often represented as a ratio. Learn more aboutVaR calculationthat helps measure market risk and determines the value of a portfolio over a period of time.

Purpose of risk-adjustment

Risk-adjusted return is a critical element to successful long-term investing and the one often overlooked and usually misunderstood by traders new in the field. Risk-adjusted returns are perhaps the most important yet least understood part of investing.

It is always better to weigh the return potential of any investment against the risks it takes so that the risk-return ratio is well understood before making the investment decision.

Risk-adjusted return ratios in python

Let us now find out the various measures along with the formula of each for risk-adjusted return in Python. The following are the measures:

Sharpe ratio

Information ratio

Modigliani ratio (M2 ratio)

Treynor Ratio

Jensen’s Alpha

R-squared

Sortino Ratio

​​Sharpe ratio

The Sharpe ratio introduced in 1966 by Nobel laureate William F. Sharpe is a measure for calculating risk-adjusted return. The Sharpe ratio is the average return earned in excess of the risk-free rate per unit of volatility.

Here is the formula for Sharpe ratio:

$$Sharpe \ ratio = \frac{(Mean \ return − Risk \ free \ rate)}{Standard \ deviation \ of \ return}$$

Following is the code tocompute the Sharpe ratioin python.

Information ratio (IR)

The information ratio is an extension of the Sharpe ratio which adds the returns of a benchmark portfolio to the inputs. It measures a trader’s ability to generate excess returns relative to a benchmark.

Formula for Information ratio is as follows:

$$Information \ ratio = \frac{(Portfolio \ return − Benchmark \ rate \ of \ return)}{Tracking \ error}$$

The "tracking error" mentioned above in the formula is thestandard deviationof the excess return with respect to the benchmark rate of return.

Following is the code to compute the Information ratio in python.

Modigliani ratio (M2 ratio)

The Modigliani ratio measures the returns of the portfolio, adjusted for the risk of the portfolio relative to that of some benchmark.

To calculate the M2 ratio, we first calculate the Sharpe ratio and then multiply it by the annualised standard deviation of a chosen benchmark. We then add the risk-free rate to the derived value to give an M2 ratio.

The Modigliani ratio goes as follows:

$$Modigliani \ ratio = SR * Standard \ deviation \ of \ benchmark + (rf)$$

Following is the code to compute the Modigliani ratio in python.

Treynor ratio

The Treynor ratio was developed by Jack Treynor, an American economist who was one of the inventors of the Capital Asset Pricing Model (CAPM).

The Treynor ratio is a risk/return measure that allows traders to adjust a portfolio's returns for systematic risk. A higher Treynor ratio result means a portfolio with the probability of higher returns.

The formula for the Treynor Ratio is:

$$Treynor \ ratio = \frac{Portfolio \ return - Risk \ free \ rate}{Beta \ of \ the \ portfolio}$$

Following is the python code for the Treynor ratio.

Jensen’s alpha

The Jensen's alpha, is a risk-adjusted performance measure that represents the average return on a portfolio or investment, above or below that predicted by the capital asset pricing model (CAPM).

Given are the portfolio's or investment's beta and the average market return.

The formula for Jensen's alpha is:

$$Alpha = R(i) - (R(f) + B x (R(m) - R(f)))$$

where,

R(i) = the realized return of the portfolio or investment

R(m) = the realized return of the appropriate market index

R(f) = Risk free rate

B = the beta of the portfolio of investment with respect to the chosen market index

In python, we will calculate Jensen’s alpha as follows:

R-squared

The R squared is the proportion of the variation in the dependent variable that is predictable from the independent variable(s).

It is a statistical ratio whose main purpose is either the prediction of future outcomes or the testing of hypotheses, on the basis of the related information. It provides a measure of how well-observed outcomes are replicated by the model, based on the proportion of total variation of outcomes explained by the model.

The formula for R-squared is as follows:

$$R^2 = 1 - \frac {Unexplained \ variation}{Total \ variation}$$

Let us see how R-squared can be calculated using Python and here is the code for the same:

Sortino ratio

The Sortino ratio is similar toSharpe ratio, except the Sharpe ratio involves both upward and downward volatility while the Sortino ratio represents only downward volatility.

Just like the Sharpe ratio, the higher the Sortino ratio, the better the return for unit risk.

Since most investors are only concerned about the downward volatility, the Sortino ratio represents a more realistic picture of the downward risk.

The choice of using the Sortino or Sharpe ratio for evaluating an investment is solely based on the individual, whether he/she wants to analyze the total volatility or the downside volatility. Both are commonly used for different applications.

Sortino ratio is given by the equation:

$$Sortino \ ratio = \frac{(Expected \ return - Risk \ free \ rate)}{Standard \ deviation \ of \ negative \ asset \ return}$$

Let us now see how to calculate the Sortino ratio in python. Here is the python code for the same:

Thus, this is how we compute historical volatility in python, and we also went through the different measures of risk-adjusted return based on it.

You can learn tooptimise your portfolioin Python usingMonte Carlo Simulation.

Pros of using the risk-adjusted return ratios

Let us now find out the pros of using the measures meant for risk-adjusted return. The measures of risk-adjusted return help in the following way:

You can evaluate a portfolio consisting of various financial instruments, each carrying risk in accordance with its position in the market.

For example, a stock’s price might crash because of a scenario such as a change of management, while other stocks in the portfolio may move according to the market.

Measures of risk-adjusted return help make more precise comparisons among the risky assets.

One of the reasons for incurring losses is poorrisk management.

Hence, by understanding the risk-return tradeoff with the help of the above-mentioned  measures, traders can plan their portfolios and make much smarter financial decisions.

Cons of using the risk-adjusted return ratios

The cons of using the measures meant for risk-adjusted return should be known to the trader for being aware of the negative consequences in case one does not take care of the following factors:

Calculating returns for investment often involves looking at past performance, which can be misleading if you don’t consider the effects of inflation or other factors over time.

The market prices of financial instruments can change quickly and unpredictably, which means that the result of risk-adjusted return becomes obsolete as soon as there is a change in the market price.

Risk-adjusted returns do not reveal the expected returns in the future.

Conclusion

Measures of risk-adjusted return help traders to plan their investments well in order to make smart financial decisions. Volatility can help the trader to pull good returns if the trader knows how to adjust the risk that comes with a volatile scenario. With the risk-adjusted return, the probability of ending up with good returns, even in a volatile situation increases.

Also, you can use the Python codes in your strategy which are provided above for each measure of adjusting the risk.

To learn more about volatility and risk-adjusted return, you can enrol in our course onVolatility Trading Strategies. In this course, you will learn four different ways to measure volatility, namely ATR, standard deviation, VIX and Beta. This will help to set dynamic stop-loss and take-profit  levels, hedge your portfolio using VIX and select stocks in your portfolio.

Note: The original post has been revamped on 18th January 2023 for accuracy, and recentness.

Disclaimer: All investments and trading in the stock market involve risk. Any decision to place trades in the financial markets, including trading in stock or options or other financial instruments is a personal decision that should only be made after thorough research, including a personal risk and financial assessment and the engagement of professional assistance to the extent you believe necessary. The trading strategies or related information mentioned in this article is for informational purposes only.

---

*Imported from QuantInsti Blog on 2026-04-27*
