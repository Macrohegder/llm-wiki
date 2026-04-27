---
title: "Portfolio Variance Explained: Calculation, Covariance Matrix, and Python Examples"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/calculating-covariance-matrix-portfolio-variance/"
date: "2025-01-22"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Portfolio Variance Explained: Calculation, Covariance Matrix, and Python Examples

**来源**: [QuantInsti](https://blog.quantinsti.com/calculating-covariance-matrix-portfolio-variance/)  
**日期**: 2025-01-22  
**作者**: QuantInsti

---

## 原文

Portfolio Variance/Covariance Analysis

By Tsotne KutaliaHow would you measure the risk of holding a single asset like a company stock? How would you compare two assets in terms of their risks? How would you select an asset to be added to your existing portfolio?

Before 1950s, investors would seek answers in financial reports such as balance sheet or income statement and get some qualitative perceptions about the performance of a given asset. Otherwise, they would read news related to a particular asset and brainstorm about the likelihood of the price rise or fall.

Then came Harry Markowitz, a young PhD student in Chicago University and wrote a thesis named“Portfolio Selection”later famously named“Modern Portfolio Theory”or simplyMPT. 
  He suggested investors to observe the relationships between the expected return (μ) and standard deviation (σ) of 
  returns. This was a milestone in the world of investments and gave birth toquantitative financeas a discipline.

This blog is self-sufficient in the sense that we will build the topic from the ground up. The following sections are covered.

Understand the return of a single assetWhat is return on an asset?Estimating variance and standard deviation as risk measures

What is return on an asset?

Estimating variance and standard deviation as risk measures

Understand relationships between two assetsCovariance coefficientVariance and standard deviation of a portfolio with two assets

Covariance coefficient

Variance and standard deviation of a portfolio with two assets

Understand multi-asset portfolioVariance-Covariance matrix for a multi asset portfolioVariance and standard deviation of a portfolio of multi assets

Variance-Covariance matrix for a multi asset portfolio

Variance and standard deviation of a portfolio of multi assets

Conclusion

Prerequisites:

To fully understand the concepts in this blog, it's essential to have a strong foundation in statistics and portfolio management.

Start by learning key statistical concepts such asRandom Variables,Standard Deviation, andCovariance, which are crucial for risk assessment.

Additionally, understanding theStandard Normal Distributionwill help in analyzing asset returns.

A basic introduction to portfolio management principles will further strengthen your understanding. For a structured explanation, check out thisvideo tutorial.

Understand the return of a single asset

What is return on an asset?

Suppose that at a given moment an asset is worth $100 and you buy it. Next moment (say in one week) the price rises to $110. The return on your investment then is

In other words, by holding this asset, you would gain 10% on your investment. Generally speaking, the return on an asset in one period is computed by the formula

Since it is unknown what value \( R_t \) will take, we regard it as a random variable. For simplicity, we can refer to a random variable as a variable whose value is unknown in advance.

Example 1.1:

The example includes the Exon Mobil Corp. (XOM) stock prices. The returns are computed according to (1.1.1) in excel. The last column (D) contains the formula for the column C. The first column contains the dates sorted in descending order in format MM/DD/YYYY. So the monthly returns are provided.

The same computations can be carried out in python as follows:

Estimating variance and standard deviation as risk measures

From the realizations of returns (i.e. observed historical value of return - the random variable R), it is possible to estimate the expected return of a given asset. Assuming equal weights for each realization of return, the expected return, denoted by R is given by

This mean value of returns is one characteristic of numerical data measuring the central tendency of the data. The estimated variance of the random variable R on the other hand, measures the variability of the data around the mean is given by the following formula

The variance of returns, as shown in (1.2.2) is the average squared deviation from the expected return. It measures how much volatile the stock returns are with respect to the mean. Thus, the variance is taken as the measure of risk of an asset. In other words, the risk is the average squared deviation from the expected returns.

However, the squared difference between the individual asset returns and the mean has no any meaningful interpretation. In order to bring the quantity back into the original units, we compute the square root of the variance to obtain the standard deviation of returns

Standard deviation is a risk measure. Lower the value of s, less risky a given asset is considered to be and vise versa.

Example 2.1

The expected daily return of the stock happens to be around 1.35% computed by (1.2.1).  Now we measure by how much the individual returns are scattered around this value on average. According to (1.2.2)

And the corresponding standard deviation computed by (1.2.3) is s = √s2= 0.00385.

The same quantities can be computed in python with the following simple fragment of the code:

As a result, we obtain σ2= 0.00148 and σ = 0.038473 as monthly variance and standard deviation respectively.

Understand relationships between two assets

Covariance coefficient

So far, we discussed the expected return and standard deviation of a single random variable. Now consider two random variables, X and Y, observed as pairs (x1, y1), (x2, y2), ..., (xn, yn). So the sample size is n, i.e. we have n pairs. The covariance coefficient between two random variables measures their linear dependence and is computed by

If sxy> 0, the two variables are positively related, i.e. they move in the same direction. Simply put, increasing the value of X is followed by an increase in Y and vice versa - decreasing the value of X causes the value of Y to drop. Suppose X is a real estate area measured in square feet and Y is the corresponding price measured in thousands of dollars. Then it is expected that the covariance between these variables will be positive, implying that larger real estate costs more and smaller one is worth less.

As long as sxy< 0, the two variables are negatively related, i.e. they move in the opposite direction. Simply put, increasing the value of X is followed by a decrease in Y and vice versa - decreasing the value of X causes the value of Y to rise. Suppose X is a price of a certain product measured in dollars and Y is the corresponding demand measured in units sold. Then it is expected that the covariance between these variables will be negative, implying that higher price results in lower demand and lower price results in higher demand.

sxy= 0 expresses the statistical independence of X and Y. In other words, changing the value of X has no effect on the value of Y.

Having discussed the covariance coefficient for two abstract random variables X and Y for simplicity, we now repeat the same formula for the random variables which represent the returns of two assets in a given portfolio: R1and R2, i.e. consider a portfolio of two assets with respective returns R1and R2. Then the sample covariance coefficient computed based on the realizations is identical to (2.1.1 a)

We would interpret the positive and negative (and zero) covariances similarly to X and Y. Think of the case sR1R2> 0 as if the assets (like stocks) are selected from the same industry. Thus, similar factors affect both. So, increasing the value of one stock, cause the value of another to rise. The example of this case would be two stocks from tech industry, or both stocks from automobile industry, etc. Opposite holds true for sR1R2< 0. In particular, in this case, increasing the value of one stock results in a fall of another. You can think of this case as if the stocks were selected for complement industries like airlines and oil production. The following example illustrates the case.

Example cont’d:

Consider a portfolio consisting of two assets. Exon Mobil Corp. (XOM) and American Airlines Group Inc. (AAL) stocks. These companies are from negatively related industries. In other words, American Airlies Inc. depends on the oil price. Higher the oil price (i.e. higher the XOM price ) lower the AAL price is and vice versa. In other words, airlines and oil producing industries move in opposite directions. Their monthly prices for the last 12 months are given below

Let us denote their returns by R1and R2, respectively. Computations of returns are carried out by (1.1.1) and we obtain

In order to compute the covariance coefficient, one needs to first deriveR1andR2.

and by (2.1.1 b) the covariance is computed asIn excel, this is done by a single functionImage 2.1.3As a result, we obtain s=-0.00066, a negative value. Let us think about this for a moment. American Airlines (AAL) is a consumer of oil as energy. If the oil price rises, benefiting Exon Mobil (XOM), the AAL price drops. The opposite happens when the oil price drops. So, we can conclude that AAL and XOM move in opposite directions.Variance and standard deviation of a portfolio with two assetsPortfolio Variance and Covariance MatrixSuppose we have a portfolio consisting of two assets with the corresponding returns R1and R2. Let the weights vector be w = [w1, w2]. The variance of such portfolio is computed byHere the last term makes a big difference. What we see is that the portfolio variance is not just the weighted sum of two variances, but it also has the third terms which contains the covariance coefficient. This is important.Suppose you manage to find two assets with the same expected return and negative covariance between the returns. Instead of putting all your investment into one of the assets, you could split it into these two assets, and while you maintain the same expected return, the negative last term of (2.2.1) would make your overall risk lower. From (2.2.1), we can derive the standard deviation of the portfolio as

and by (2.1.1 b) the covariance is computed as

In excel, this is done by a single function

As a result, we obtain s=-0.00066, a negative value. Let us think about this for a moment. American Airlines (AAL) is a consumer of oil as energy. If the oil price rises, benefiting Exon Mobil (XOM), the AAL price drops. The opposite happens when the oil price drops. So, we can conclude that AAL and XOM move in opposite directions.

Variance and standard deviation of a portfolio with two assets

Suppose we have a portfolio consisting of two assets with the corresponding returns R1and R2. Let the weights vector be w = [w1, w2]. The variance of such portfolio is computed by

Here the last term makes a big difference. What we see is that the portfolio variance is not just the weighted sum of two variances, but it also has the third terms which contains the covariance coefficient. This is important.

Suppose you manage to find two assets with the same expected return and negative covariance between the returns. Instead of putting all your investment into one of the assets, you could split it into these two assets, and while you maintain the same expected return, the negative last term of (2.2.1) would make your overall risk lower. From (2.2.1), we can derive the standard deviation of the portfolio as

Note that in (2.2.1), if sxy=0 i.e. you find independent assets), then the portfolio variance will just be the weighted sum of two variances

Let us now define the covariance matrix as follows

where the elements of the matrix represent the covariances measured between all pairs of individual returns.

Now let us consider the covariance coefficient by (2.1.1 b). If we compute the covariance of a random variable X with respect to itself, we would obtain

So, this is essentially the variance of R1computed by (1.2.2) and thus, (2.2.3 a) becomes

and hence, it is called the variance-covariance matrix. On the diagonal, you notice the variances of the random variables.

As long as we have the definition of the covariance matrix and the weights vector, we can rewrite (2.2.1) in terms of matrices as follows

Out of which the portfolio standard deviation can be computed by simply taking the square root. More completely defined, the portfolio standard deviation is

Example cont’d:

Suppose we put equal weights into the portfolio w = [w1, w2] = [0.5 0.5]. The variance-covariance matrix then is

Then by (2.2.4) the variance of the portfolio returns becomes

In Excel, the computations are illustrated below

The same computations can be carried out via python as illustrated below

Understand multi asset portfolio

Variance-covariance matrix for a multi – asset portfolio

Suppose we have a portfolio of N assets, if we compute the covariance terms between all the pairs, sRiRj

then we can generalize the variance-covariance matrix in (2.2.3 b) into a form

in which the squared terms on the diagonal refer to the variances of each asset returns (i.e. of R1, R2, ..., RN). All terms in general are computed by the formula (2.1.1 b).

Example Cont’d:

We proceed to construct the covariance matrix for a portfolio consisting of more than 2 assets. First, we add another stock – Amazon.com Inc. (AMZN) to the existing portfolio. So, it now becomes N=3 asset portfolio. The returns for all stocks are computed by (1.1.1) according to the method we discussed above. Then the covariance matrix elements can be computed by (2.1.1 b). In excel this is done by covariance function of Data Analysis package in Data tab.

The resulting covariance matrix is given below

The same matrix can be constructed via python as follows

Variance and standard deviation of a portfolio of multi  - assets

In this section, we generalize the discussion of section 2.2. Now suppose we have a multi-asset portfolio with weights vector w = [w1w2... wN]. Then the variance of the portfolio can be written as

which is essentially (2.2.1) generalized. We can rewrite this formula into a matrix form

out of which we derive the standard deviation as

Example Cont’d:

Suppose we split the investment into the weights w = [w1w2w3] = [0.4 0.3 0.3]. The computations based on (3.2.1 b) is illustrated below

Python analogue for computation of variance and standard deviation is given below

Conclusion

Risk of an asset or a portfolio is measured by the variance and standard deviation of its return. They measure by how much on average the returns deviate from the mean value. Higher (lower) the variance or standard deviation, higher (lower) the risk is.

Covariance coefficient measures the dependence between two asset returns. If it is positive (negative), increasing the return of one of them, causes another to also increase (decrease) and if it is negative, then increasing the return of one of them, causes another to decrease (increase). It is a good idea to seek assets with negative covariance, since this will reduce overall risk of a portfolio. This is called the diversification effect.

As long as covariances between each pair in the portfolio is known (or at least estimated), it is possible to compute the risk of the entire portfolio using the variance/covariance matrix examined above.

For more learning, you should explore the course titled "Quantitative Portfolio Management"

Files in the download:

Excel file

The Excel file illustrates construction of portfolio variance-covariance matrix step by step. There you can find an example of a portfolio consisting of two and three assets separately.

Python notebook

The Python code snippet illustrates the construction of a variance-covariance matrix for a portfolio consisting of three assets. The code file can be used as a template with slight modifications.

Login to Download

Bibliography:

Bodie Z.,  Kane A.,  Marcus A.J., (2008) Investments. The McGraw-Hill/Irwin series in finance, insurance and real estate)

Continue Learning

Deep Dive into portfolio optimization and risk management strategies. Learn variousPortfolio Optimization Methodsto balance risk and return.

Enhance your knowledge of asset pricing models withModern Portfolio Management Using the Capital Asset Pricing Model and Fama-French Three Factor Model.

If you’re interested in simulation-based approaches, explorePortfolio Optimization Using Monte Carlo Simulationto model risk and returns dynamically.

Additionally, understanding performance evaluation is key, andPortfolio Analysis – Performance Measurement and Evaluationcovers essential metrics to assess portfolio efficiency.

For a structured, hands-on learning experience, considerPortfolio Management and Position Sizing using Quantitative Methodson Quantra.This course covers position sizing techniques like Kelly Criterion, CPPI, and Volatility Targeting, along with Mean-Variance Optimization and the Fama-French Three Factor Model.

All investments and trading in the stock market involve risk. Any decision to place trades in the financial markets, including trading in stock or options or other financial instruments is a personal decision that should only be made after thorough research, including a personal risk and financial assessment and the engagement of professional assistance to the extent you believe necessary. The trading strategies or related information mentioned in this article is for informational purposes only.

---

*Imported from QuantInsti Blog on 2026-04-27*
