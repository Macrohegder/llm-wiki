---
title: "Value at Risk (VaR) Calculation: Formulas, Portfolio Tools, and Methods in Python and Excel"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/calculating-value-at-risk-in-excel-python/"
date: "2025-01-28"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Value at Risk (VaR) Calculation: Formulas, Portfolio Tools, and Methods in Python and Excel

**来源**: [QuantInsti](https://blog.quantinsti.com/calculating-value-at-risk-in-excel-python/)  
**日期**: 2025-01-28  
**作者**: QuantInsti

---

## 原文

Calculations of Value at Risk in Excel and Python

By Tostne Kutalia

What is the largest amount I might lose on an investment? This is the question every investor asks at some point in time. In other words, given the pre-specified level of certainty (i.e. probability), an investor wants to be assured that the investment loss does not surpass a certain level. Value at Risk (VaR) is a statistical measure of largest possible loss (corresponding to a certain confidence level) which addresses this problem. The main advantage of VaR is that it summarizes risk in a single, easy-to-understand number.

Prerequisite knowledge needed to make most of this blog post:

You have explored the fundamentals of risk measurement in my earlier blog onValue at Risk.

You have a solid grasp of probability distributions and understand how they underlie financial risk calculations.

In this blog we will examine the following topics:

What is VaR and why use it as a risk measure?

Non-parametric/parametric VaR as a statistical measure

Non-parametric VaR

Parametric VaR

Portfolio VaR and main VaR tools. Definitions and interpretations.

Portfolio VaR

Marginal VaR

Increment VaR

Component VaR

Conclusion

Executive summary

After completing the blog, one should be able to compute the largest loss that a portfolio can incur. This quantity is called Value at Risk (VaR). Once computed, it can change over time. In fact, suppose you have a portfolio of $1,000,000 and the largest possible loss you may expect (VaR) is $150,000. Then you continue trading by adding or removing some positions from the portfolio. Your VaR obviously changes.

So, you need some tools to measure the effects of your actions (trades) on the existing portfolio VaR.

You need to know by how much the existing VaR changes if you change a certain position by some amount. In other words, suppose you buy $10,000 more of an existing asset in the portfolio. Marginal VaR is the tool which measures by how much your portfolio VaR will respond to this particular trade. In simpler words, Marginal VaR measures how sensitive entire portfolio VaR is with respect to a given asset.

Suppose you intend to change several positions in the portfolio. The incremental VaR is yet another tool which measures by how much your portfolio VaR will rise or fall.

Existing VaR consists of individual VaRs. Put another way, $150,000 VaR of a portfolio consisting of three assets, consists of three components. The first component is the contribution of the first asset into this VaR – say $80,000. Same for the second and third components. Let them be $50,000 and $20,000. This tool is named a component VaR and it disassembles the portfolio VaR into individual components.

What is VaR and why use it as a risk measure?

Formally defined, VaR is a statistical measure of downside risk based on current positions. It measures the worst loss a given portfolio may incur over a fixed period of time under fairly normal conditions. Over the last few decades, VaR became an essential risk measuring tool reported to regulators. It is of great interest for senior managers and shareholders.

VaR is computed based on a pre-specified confidence level, usually 90%, 95% or 99%. In order to get an intuitive insight into the essence of VaR, let us denote the confidence level as c and L as the loss, measured as a positive number. VaR (also reported as a positive number) is the cutoff level of loss in absolute value, such that

Computing probability obviously assumes some kind of knowledge of the shape of distribution of losses. The following image illustrates the VaR as a threshold level as given in (1.1).

There are two general approaches of computing VaR.

Non-parametric/parametric VaR as a statistical measure

Non-parametric VaR

This is the most general method of computation which makes no assumption about the shape of the distribution of returns. 
    LetW0denote the initial investment andRbe the rate of return of a portfolio.Ris random. Assuming the position is fixed till the end of the investment horizon, the portfolio value will be:

If we define the lowest rate of return by R* that can be realized by the confidence level c (i.e. R* is the (1-c)th percentile of returns R), the lowest value to which the portfolio can drop is

VaR measures the worst loss at a given confidence level, it is expressed as a positive number. There are two quantities relative to which VaR is computed. VaR is defined as a dollar loss relative to the mean:

and VaR is defined as an absolute VaR. i.e. dollar loss relative to zero:

From the probability distribution of the future portfolio value f(w), at a given confidence level c, we compute the worst possible realisation W* such that the probability of exceeding this value is c, i.e.

Put another way, the probability of the portfolio value being lower than W*, p=P(W≤W*), is 1-c.

which is essentially the same expression as (1.1). Simply put, loss being greater than VaR is realized with probability 1-c, which means that the portfolio value will drop below W* by the same probability.

Example:

Suppose we have yearly data of returns. 252 returns in dollars in total.

Let us take c=95%. So, the confidence level is c=95%.

The negative dollar returns are regarded as losses.

First, we compute the portfolio values based on returns by (2.1.1).

Sorting the returns in ascending order and finding the 5th percentile will give us the estimated value of dollar returns left to which is the first 252 ∙0.05=12.6 numbers.

Then by (2.1.3) we compute the VaR to the mean and by (2.1.4) VaR relative to zero. These numbers are $229,731.72 and $326,554.42 respectively. The computations are shown in the attached Excel file

In Image 2.1.1 the C column contains the values of portfolio changing due to fluctuations in portfolio returns. Some sample calculation formulas are given in column D. Initially, computations start by $1,000,000 from below and ends up above in the second row due to descending order of dates.

Below is the analogous python code.

Parametric VaR

Computation ofVaRtakes a simpler form if we know the probability distribution of returns or at least we assume that the distribution belongs to the parametric family such as normal distribution. In such case, theVaRcan be directly computed based on thestandard deviationand a multiplicative factor corresponding to a given confidence level. Generally,R*is negative. For more convenience, we can write it as−|R*|. Assuming it is normally distributed, we can associate it with a standard normally distributed random variable computed as

where μ and σ represent the expected value and standard deviation or R* respectively. So, we have

Essentially, all integrals in (2.2.2) represent the same quantity – the probability of the portfolio value at the end of the investment horizon ending up within the range of \( (-\infty, W^*) \) is \( 1 - c \). This quantity obviously coincides with the probability that the portfolio return will fall within \( (-\infty, -|R^*|) \). Having converted \( R^* \) into \( z \) standard normal quantity by (2.2.1), we clearly see that above mentioned integrals yield the same result as a standard normally distributed random variable falling within the interval \( (-\infty, -z) \).

From this we clearly see that from \( c \) we can compute \( z \) and respectively, we can recover \( R^* = -z\sigma + \mu \). Here we assume that the parameters \( \mu \) and \( \sigma \) are expressed on an annual basis. If we express the time interval in \( \Delta t \) in years, then VaR relative to the mean can be expressed as follows:

and VaR computed as an absolute dollar loss (i.e. relative to zero) is

Example:

Suppose we have yearly data of returns. 252 returns in dollars in total. Let us take \( c = 95\% \). So, the confidence level is \( c = 95\% \). First, we compute the portfolio values based on returns by (2.1.1). Next, the dollar returns are computed. The negative dollar returns are regarded as losses. The mean and standard deviation of portfolio returns are computed first. \( z_{0.95} = 1.645 \). This is the standard normal quantile corresponding to 95% confidence level. In other words, there is 95% probability that the standard normal random variable takes the value less than this number: \( P(Z < z_{0.95}) = 95\% \).

Next, \( VaR(mean) = \$450,598.39 \) and \( VaR(zero) = \$474,751.86 \) are computed by (2.2.3) and (2.2.4) respectively. The attached Excel file contains the computations.

Below is the analogous python code.

Portfolio VaR and main VaR tools

Portfolio VaR

Portfolio VaR can be computed from the combination of risks associated to underlying assets. The portfolio rate of return is given by

whereNdenotes the number of assets in the portfolio andRiis the rate of return corresponding to theithasset. 
    We can rewriteRpin (3.1.1 a) by the vector notation:

HerewTrepresents the transposed vector of weights andRis the vertical vector of rates of return of individual assets. We denote byμpthe expected rate of return of the portfolio

and byσp2we denote the portfolio variance

whereσijrepresents the covariance betweenithandjthasset returns (i.e. betweenRiandRj). A more convenient way of expressingσp2in terms of individual asset variances and weights is in matrix form

Denoting the covariance matrix as Σ, this can more compactly be written in terms of matrices as

The portfolio variance can be rewritten in terms of dollar exposures x as

where W denotes the initial portfolio value. Assuming the individual asset returns are normally distributed, the portfolio return itself, which is the linear combination of jointly normal random variables, is also normally distributed. So, if we define by W the initial portfolio value, the portfolio VaR becomes

wherezis the standard normal quantile corresponding to a certain confidence level. e.g. P(Z < Z0.95) = 95%. In this case Z0.95= 1.645.

Other common confidence levels used are 90% and 99%. Correspondingzvalues are given below for convenient reference:

Example:

Given one-year monthly data of AMZN, TSLA and AAPL within the time interval of 11/30/2023-11/29/2024, we compute the portfolio VaR and related quantities explained below. First, we compute the asset returns as

for each moment t. The variance/covariance matrix for these asset returns is given below

=0.0758 0.0472 0.0209 0.0472 0.3775 0.0445 0.0209 0.0445 0.0511

Now considering the weights vector

the estimated annualized variance of the portfolio returns is computed by (3.1.3 b) as follows

and thus, annualised standard deviation is

out of which we can directly compute the portfolio VaR assuming the initial portfolio value W = $1,000,000 and the confidence level of 95% (i.e. z = N-1(0.95) ≈ 1.64).

the portfolio VaR by (3.1.5) is

Alternatively, we could have first computed the portfolio standard deviation in terms of dollar exposures and then compute VaR. First, we need the vector

and the variance of the portfolio in terms of dollars by (3.1.4) is computed as shown below

and correspondingly, the (full computation of) standard deviation is

and the portfolio VaR by (3.1.5) becomes

We interpret this quantity as the largest possible loss by 95% confidence level, which can be incurred by the portfolio of $1,000,000 over a one-year horizon under normal circumstances. In simpler words, there is only 5% probability that the actual loss incurred by the portfolio will surpass this amount.

Individual VaRs computed by the formula (3.1.6) are

Note that the sum of the individual VaRs is $595,863.36 which is obviously not equal to the portfolio VaR. Portfolio VaR is less since it takes advantage of the diversification effect.

Marginal VaR

VaR of an asset is a static quantity which measures the uncertainty in the return of a given asset, taken in isolation. However, when considering this asset as a part of a portfolio, what matters is its contribution to the portfolio risk.

Let us begin by an existing portfolio consisting of N assets. Now we consider adding one unit of an assetiinto the portfolio. 
    In order to measure the impact of this trade on overall portfolio risk, we use the tool called Marginal VaR. 
    First, we define the derivative of portfolio variance with respect to theithasset weight as:

From which we derive

This quantity measures the sensitivity of the portfolio risk with respect to a given asset weight. Converting this expression into a VaR number yields the Marginal VaR for asset i

As long as beta of a given asset is defined as

the relationship between the Marginal VaR and the beta of a given asset can be expressed as follows

Example cont’d:

Now we can compute the marginal VaRs for each asset within the portfolio. First, we compute betas by (3.2.4)

Correspondingly marginal VaRs are computed by (3.2.3 b)

These quantities are interpreted as a change in portfolio VaR as a result of an additional dollar exposure to a given asset. In other words, each additional $1 into the first asset (AMZN) will increase the portfolio VaR by $0.3047.

Incremental VaR

Suppose that we begin with the initial portfolio VaRp. Then add new positions captured by the vector a. Elements of this vector represent the changes in each position. As a result, we obtain a new VaR and we denote it by VaRp+a. Thus the incremental VaR is defined as the difference between the new and old VaRs as follows

From this formula, it is clear that calculation of an incremental VaR, i.e. the effect of a new position to the existing portfolio VaR requires us to compute the VaR of the updated portfolio as well as the VaR of an existing portfolio. However, there is a shortcut. In particular, we can use the approximation technique. Expanding the VaRp+aaround the original point VaRpyields

where we ignore the rest of the terms assuming a is sufficiently small. From which we have

Example Cont’d:

Let us begin with the initial portfolio of $1 000 000 with positions vector x = [x1x2x3] = [400,000 300,000 300,000]. The VaR of such portfolio was computed in Example 2.1 to be $450,598.39. Now consider a vector a = [10,000 5,000 0] of changes in positions in each asset. i.e. we put an additional $10,000 into AMZN, $5,000 into TSLA and we do not change our position in AAPL. If we computed the VaR of the new portfolio by (3.1.5), that would become

So the incremental VaR computed precisely by (3.3.1 a) turns out to be

Applyingthe approximation technique (3.3.1 b), we would obtain

So the approximation yields almost the same result as precise method. The accuracy of approximation higher for smaller values in vector a.

Component VaR

In order to manage portfolio risk, it would be helpful to have a risk decomposition of the current portfolio. This task is not simple. The reason is that the portfolio volatility is not a linear function of its components. Adding up the individual asset VaRs will not yield the portfolio VaR as it ignores the diversification effect. Instead, it would be really useful to have additive decomposition of VaR that recognizes the power of diversification.

In section 2.2 we covered marginal VaR stating that it measures the contribution of each asset to the existing portfolio risk. Multiplying the marginal VaR by the current dollar position in asset gives a quantity which we call the Component VaR of an asset i.

Roughly speaking, the component VaR of the given asset i indicates how the portfolio VaR would change if the component (i.e. the given asset) was removed from the portfolio. It should be noted that the quality of approximation improves when the VaR components are small. Thus, the decomposition is more accurate for large portfolios having many small positions. Adding up the Component VaRs of individual assets obviously yields the portfolio VaR, i.e.

here the term in the parenthesis is the beta of the portfolio with respect to itself which is unity.

Example Cont’d:

The initial portfolio with $1 000 000 distributed into the positions x=400,000   300,000   300,000 had a VaR of $450,598.39. We can split this amount into the components by (3.4.2)

Not surprisingly, the sum of components VaRs is equal to the total portfolio VaR. In other words, the total contribution of a given asset into the portfolio risk is the CVaR which corresponds to that asset. If we removed this asset from the portfolio, its risk would drop by the amount of CVaR.

Conclusion

As a result, we can conclude that VaR, when applied correctly gives a very useful and intuitive measure of risk. It is the largest possible loss that a portfolio may incur with a given confidence level. There are various ways to compute VaR. If the distribution of portfolio return is unknown, a non-parametric approach can be taken. Otherwise, as long as the distribution of returns belongs to any parametric family, one can compute VaR in a simpler way.

In addition, there are useful VaR tools such as Marginal VaR (MVaR), Incremental VaR (VaR) and Component VaR (CVaR) which are used to measure the effects of a change in a given asset into the on the entire portfolio.

In particular, Marginal VaR, defined as a derivative of a portfolio standard deviation with respect to a position taken in a certain asset, measures the effect of a single dollar change in the given asset on the entire portfolio risk.

Incremental VaR on the other hand indicates by how much a given portfolio VaR would change as a result of changes in the positions.

Finally, we described Component VaRs as tools to decompose the total portfolio VaR into the components. It measures the contribution of a given asset into the entire portfolio risk.

Files in the download:

The workings of the examples discussed above are provided in both Excel and Python formats within the attached .zip file for your reference.

Login to Download

Bibliography:

Jorion, P. (2001).Value At Risk: The new benchmark for managing Financial risk.New York: McGraw Hill.

Continue learning:

If you’re looking to enhance your understanding of more advanced risk metrics, see my post onConditional Value at Risk (CVaR) or Expected Shortfall. It covers how to calculate tail risk beyond VaR, offering a more comprehensive view of potential losses.

Learnquantitative portfolio managementtechniques such as Factor Investing, Risk Parity and Kelly Portfolio, and Modern Portfolio Theory using Python.

Learn, create andbacktest various position sizing techniquessuch as Kelly, Optimal f, and volatility targeting on a trading strategy, using Python.

For a structured, hands-on learning experience, considerPortfolio Management and Position Sizing using Quantitative Methodson Quantra. This course covers position sizing techniques like Kelly Criterion, CPPI, and Volatility Targeting, along with Mean-Variance Optimization and the Fama-French Three Factor Model. You'll also explore factor timing, beta, covariance, and performance ratios, all while implementing strategies using Python libraries like NumPy, Pandas, Matplotlib, Seaborn, Sklearn, OLS, cvxpy, and TA-Lib.

Note: The original post has been revamped on 28thJan 2025 for recentness, and accuracy.

All investments and trading in the stock market involve risk. Any decision to place trades in the financial markets, including trading in stock or options or other financial instruments is a personal decision that should only be made after thorough research, including a personal risk and financial assessment and the engagement of professional assistance to the extent you believe necessary. The trading strategies or related information mentioned in this article is for informational purposes only.

---

*Imported from QuantInsti Blog on 2026-04-27*
