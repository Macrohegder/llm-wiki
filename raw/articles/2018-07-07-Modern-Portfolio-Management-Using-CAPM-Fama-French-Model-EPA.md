---
title: "Modern Portfolio Management Using CAPM & Fama-French Model [EPAT PROJECT]"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/modern-portfolio-capital-asset-pricing-fama-french-three-factor-model/"
date: "2018-07-07"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Modern Portfolio Management Using CAPM & Fama-French Model [EPAT PROJECT]

**来源**: [QuantInsti](https://blog.quantinsti.com/modern-portfolio-capital-asset-pricing-fama-french-three-factor-model/)  
**日期**: 2018-07-07  
**作者**: QuantInsti

---

## 原文

Modern Portfolio Management Using Capital Asset Pricing And Fama-French Three Factor Model [EPAT PROJECT]

This article is the final project submitted by the authors as a part of their coursework in Executive Programme in Algorithmic Trading (EPAT™) at QuantInsti®. Do check ourProjects pageand have a look at what our students are building.

About the Authors

Krishnan Ramchandranhas strong expertise in Global delivery management in the BFSI space and in Capital Markets. An Engineer and an MBA degree holder, he had joined EPAT to improve his knowledge of Capital markets in Quants. His experience includes working with Wall Street firms and leading exchanges in the US and India and Global ICSDs.

Sadagopan Viravalliis a Management Accountant with 22+ years of Consulting experience across Financials Services, Public Services, Telco, High-Tech and Utilities industry segments. A people person, post-EPAT, he aspires to trade in domestic and international markets and work with leading Investment banks/hedge funds whilst formulating Quant strategies & executing them.

Project

QuantInsti’s EPAT course introduced us to the Modern Portfolio Theory (MPT), the Fama-French Three Factor Model, Capital Asset Pricing Model (CAPM), Efficient Frontier (EF) and multiple Quant Techniques. The learning helped us understand the relevance & application of Quantitative Finance techniques to Portfolio Management which has been our motivation to construct “MyPortfolio” in the Indian stock markets.

We leveraged programming inPythonto extract data from Yahoo! Finance and performed backtesting which helped us to arrive at the right combination of stocks/scripts in NSE and thus, structured “MyPortfolio” by applying our learnings in Quantitative Finance techniques. Definitions and concepts have been referred from Investopedia.

In Summary, we have come up with a “Model Portfolio with Multi-cap Investment” approach in the Indian stock markets with weights each for the Large cap, Midcap and Small cap segments and have selected stocks from the corresponding NSE Indexes for Large, Mid and Small cap stocks/scripts. “MyPortfolio” at any point in time shall consist of ~90% of fund allocation towards stocks (i.e. 20-25 multi-cap multi-sector stocks) and the remaining ~10% in Cash (or liquid instruments) to seize any opportunity that may arise in the markets.

Introduction

Our motivation to work on this project is two-fold:

Apply learnings from the EPAT course and arrive at our own portfolio model, and

Create Proof points of applicability and relevance of these portfolio theories in the Indian stock markets

In this project report, we’ll be introduced to the theories & techniques onhow to hedge a portfoliotheory, and thereon be introduced to the Data mining/analysis that we have performed bybacktestingthe algorithm in Python and as a result, arrive at our “MyPortfolio” model and its re-balancing approach on an ongoing basis.

Modern Portfolio Theory

Modern Portfolio Theory (MPT), a hypothesis put forth by Harry Markowitz in his paper "Portfolio Selection," (published in 1952 by the Journal of Finance) is an investment theory based on the idea that risk-averse investors can construct portfolios to optimize or maximize expected return based on a given level of market risk, emphasizing that risk is an inherent part of higher reward. It is one of the most important and influential economic theories dealing with finance and investment.

Also called "portfolio theory" or "portfolio management theory", Modern Portfolio Theory suggests that it is possible to construct an "efficient frontier" of optimal portfolios, offering the maximum possible expected return for a given level of risk. It suggests that it is not enough to look at the expected risk and return of one particular stock. By investing in more than one stock, an investor can reap the benefits of diversification, particularly a reduction in the riskiness of the portfolio. Modern Portfolio Theory quantifies the benefits of diversification, also known as not putting all of your eggs in one basket.

Consider that, for most investors, the risk they take when they buy a stock is that the return will be lower than expected. In other words, it is the deviation from the average return. Each stock has its own standard deviation from the mean, which Modern Portfolio Theory calls "risk."

The risk in a portfolio of diverse individual stocks will be less than the risk inherent in holding any one of the individual stocks (provided the risks of the various stocks are not directly related). Consider a portfolio that holds two risky stocks: one that pays off when it rains and another that pays off when it doesn't rain. A portfolio that contains both assets will always pay off, regardless of whether it rains or shines. Adding one risky asset to another can reduce the overall risk of an all-weather portfolio.

In other words, Markowitz showed that investment is not just about picking stocks, but about choosing the right combination of stocks among which to distribute one's nest egg.

On the more technical side, there are five statistical risk measurements used in Modern Portfolio Theory (MPT); alpha, beta, standard deviation, R-squared and the Sharpe ratio. All of these indicators are intended to help investors determine a potential investment's risk-reward profile.

What is Alpha?

Alpha is used in finance as a measure of performance.Alpha, often considered the active return on an investment, gauges the performance of an investment against a market index or benchmark which is considered to represent the market’s movement as a whole. The excess return on an investment relative to the return of a benchmark index is the investment’s alpha. Alpha is used for mutual funds and all types of investments. It is often represented as a single number (like 3 or -5), but this refers to a percentage measuring how the portfolio or fund performed compared to the benchmark index (i.e. 3% better or 5% worse).

Alpha is often used in conjunction with the beta, which measures volatility or risk. Alpha is also often referred to as “excess return” or “abnormal rate of return.”

What is Beta?

Beta(aka Beta Coefficient) is a measure of the volatility, or systematic risk, of a security or a portfolio in comparison to the market as a whole. Beta is used in the capital asset pricing model (CAPM), which calculates the expected return of an asset based on its beta and expected market returns.

Beta is calculated using regression analysis. Beta represents the tendency of a security's returns to respond to swings in the market. A security's beta is calculated by dividing the covariance the security's returns and the benchmark's returns by the variance of the benchmark's returns over a specified period.

A security's beta should only be used when a security has a high R-squared value in relation to the benchmark. The R-squared measures the percentage of a security's historical price movements that could be explained by movements in a benchmark index. When using beta to determine the degree of systematic risk, a security with a high R-squared value, in relation to its benchmark, would increase the accuracy of the beta measurement.

A beta of 1 indicates that the security's price moves with the market. A beta of less than 1 means that the security is theoretically less volatile than the market. A beta of greater than 1 indicates that the security's price is theoretically more volatile than the market. For example, if a stock's beta is 1.2, it's theoretically 20% more volatile than the market.

What is Standard Deviation?

Standard deviation is a measure of the dispersion of a set of data from its mean. It is calculated as the square root of variance by determining the variation between each data point relative to the mean. If the data points are further from the mean, there is a higher deviation within the data set.

In finance, the standard deviation is a statistical measurement; when applied to the annual rate of return on an investment, it sheds light on the historical volatility of that investment. The greater the standard deviation of a security, the greater the variance between each price and the mean, indicating a larger price range. For example, a volatile stock has a high standard deviation, while the deviation of a stable blue-chip stock is usually rather low.

What is R-Squared?

R-squared is a statistical measure that represents the percentage of a fund or security's movements that can be explained by movements in a benchmark index.

R-squared values range from 0 to 1 and are commonly stated as percentages from 0 to 100%. An R-squared of 100% means all movements of a security are completely explained by movements in the index. A high R-squared, between 85% and 100%, indicates the fund's performance patterns have been in line with the index. A fund with a low R-squared, at 70% or less, indicates the security does not act much like the index. A higher R-squared value indicates a more useful beta figure. For example, if a fund has an R-squared value of close to 100% but has a beta below 1, it is most likely offering higher risk-adjusted returns.

What is the Sharpe Ratio?

The Sharpe ratio is the average return earned in excess of the risk-free rate per unit of volatility or total risk. Subtracting the risk-free rate from the mean return, the performance associated with risk-taking activities can be isolated. One intuition of this calculation is that a portfolio engaging in “zero risks” investment, such as the purchase of U.S. Treasury bills (for which the expected return is the risk-free rate), has aSharpe ratioof exactly zero. Generally, the greater the value of the Sharpe ratio, the more attractive the risk-adjusted return. The Sharpe Ratio was developed by Nobel laureate William F. Sharpe.

The Sharpe ratio has become the most widely used method for calculating risk-adjusted return; however, it can be inaccurate when applied to portfolios or assets that do not have a normal distribution of expected returns. Many assets have a high degree of kurtosis ('fat tails') or negative skewness. The Sharpe ratio also tends to fail when analyzing portfolios with significant non-linear risks, such as options or warrants.

Modern Portfolio Theory states that adding assets to a diversified portfolio that have correlations of less than 1 with each other can decrease portfolio risk without sacrificing return. Such diversification will serve to increase the Sharpe ratio of a portfolio.

Sharpe ratio = (Mean portfolio return − Risk-free rate) Standard deviation of portfolio return

Fama And French Three Factor Model

The Fama and French Three Factor Model is an asset pricing model that expands on thecapital asset pricing model (CAPM)by adding size and value factors to the market risk factor in CAPM. This model considers the fact that value and small-cap stocks outperform markets on a regular basis. By including these two additional factors, the model adjusts for the outperformance tendency, which is thought to make it a better tool for evaluating manager performance. The three factors are Market Risks, Company Size and Value Factors.

BREAKING DOWN Fama And French Three Factor Model

Eugene Fama and Kenneth French, both professors at the University of Chicago Booth School of Business, attempted to better measure market returns and, through research, found that value stocks outperform growth stocks. Similarly, small-cap stocks tend to outperform large-cap stocks. As an evaluation tool, the performance of portfolios with a large number of small-cap or value stocks would be lower than the CAPM result, as the Three Factor Model adjusts downward for small-cap and value outperformance.

Debating the Three Factor Model

There is a lot of debate about whether the outperformance tendency is due to market efficiency or market inefficiency. On the efficiency side of the debate, the outperformance is generally explained by the excess risk that value and small-cap stocks face as a result of their higher cost of capital and greater business risk. On the inefficiency side, the outperformance is explained by market participants mispricing the value of these companies, which provides the excess return in the long run as the value adjusts. Investors who subscribe to the body of evidence provided by the Efficient Markets Hypothesis (EMH), are more likely to side with the efficiency side.

What Does It Mean for Investors?

Fama and French were quick to point out that, while value beats growth and small beats large, over the long term, investors must be able to ride out the extra short-term volatility and periodic underperformance that could occur in a given short-term time frame. Investors with a long-term time horizon of 15 years or more will be rewarded for any pain they might suffer in the short term. Fama-French conducted studies to test their model, using thousands of random stock portfolios and found that when size and value factors are combined with the beta factor, they could then explain as much as 95% of the return in a diversified stock portfolio.

Given the ability to explain 95% of a portfolio’s return versus the market as a whole, investors can construct a portfolio in which they receive an average expected return according to the relative risks they assume in their portfolios. The main factors driving expected returns are sensitivity to the market; sensitivity to size, as in small-cap stocks; and sensitivity to value stocks, as measured by the book-to-market ratio. Any additional average expected return may be attributed to unpriced or unsystematic risk.

Capital Asset Pricing Model - CAPM

The capital asset pricing model (CAPM) is a model that describes the relationship between systematic risk and expected return for assets, particularly stocks. CAPM is widely used throughout finance for the pricing of risky securities, generating expected returns for assets given the risk of those assets and calculating costs of capital.

BREAKING DOWN Capital Asset Pricing Model - CAPM

The formula for calculating the expected return of an asset given its risk is as follows:

The general idea behind CAPM is that investors need to be compensated in two ways: time value of money and risk. The time value of money is represented by the risk-free (rf) rate in the formula and compensates the investors for placing money in any investment over a period of time. The risk-free rate is customarily the yield on government bonds like U.S. Treasuries / Treasury bills.

The other half of the CAPM formula represents risk and calculates the amount of compensation the investor needs for taking on additional risk. This is calculated by taking a risk measure (beta) that compares the returns of the asset to the market over a period of time and to the market premium (Rm-rf): the return of the market in excess of the risk-free rate. Beta reflects how risky an asset is compared to overall market risk and is a function of the volatility of the asset and the market as well as the correlation between the two. For stocks, the market is usually represented as the S&P 500 but can be represented by more robust indexes as well.

The CAPM model says that the expected return of a security or a portfolio equals the rate on a risk-free security plus a risk premium. If this expected return does not meet or beat the required return, then the investment should not be undertaken. The security market line plots the results of the CAPM for all different risks (betas).

Example of CAPM

Using the CAPM model and the following assumptions, we can compute the expected return for a stock:

The risk-free rate is 2% and the beta (risk measure) of a stock is 2.

The expected market return over the period is 10%, so that means that the market risk premium is 8% (10% - 2%) after subtracting the risk-free rate from the expected market return.

Plugging in the preceding values into the CAPM formula above, we get an expected return of 18% for the stock:

18% = 2% + 2 x (10% - 2%)

What Is The Efficient Frontier?

The efficient frontier is the set of optimal portfolios that offers the highest expected return for a defined level of risk or the lowest risk for a given level of expected return. Portfolios that lie below the efficient frontier are sub-optimal because they do not provide enough return for the level of risk. Portfolios that cluster to the right of the efficient frontier are also sub-optimal because they have a higher level of risk for the defined rate of return.

BREAKING DOWN Efficient Frontier

Since the efficient frontier is curved, rather than linear, a key finding of the concept was the benefit of diversification. Optimal portfolios that comprise the efficient frontier tend to have a higher degree of diversification than the sub-optimal ones, which are typically less diversified. The efficient frontier concept was introduced by Nobel Laureate Harry Markowitz in 1952 and is a cornerstone of modern portfolio theory.

Optimal Portfolio

One assumption in investing is that a higher degree of risk means a higher potential return. Conversely, investors who take on a low degree of risk have a low potential return. According to Markowitz's theory, there is an optimal portfolio that could be designed with a perfect balance between risk and return. The optimal portfolio does not simply include securities with the highest potential returns or low-risk securities. The optimal portfolio aims to balance securities with the greatest potential returns with an acceptable degree of risk or securities with the lowest degree of risk for a given level of potential return. The points on the plot of risk versus expected returns where optimal portfolios lie are known as the efficient frontier.

Selecting Investments

Assume a risk-seeking investor uses the efficient frontier to select investments. The investor would select securities that lie on the right end of the efficient frontier. The right end of the efficient frontier includes securities that are expected to have a high degree of risk coupled with high potential returns, which is suitable for highly risk-tolerant investors. Conversely, securities that lie on the left end of the efficient frontier would be suitable for risk-averse investors.

Limitations

The efficient frontier and modern portfolio theory have many assumptions that may not properly represent reality. For example, one of the assumptions is that asset returns follow a normal distribution. In reality, securities may experience returns that are more than three standard deviations away from the mean more than 0.03% of the observed values. Consequently, asset returns are said to follow a leptokurtic distribution or heavy-tailed distribution.

Additionally, Markowitz's theory assumes investors are rational and avoid risk when possible, there are not large enough investors to influence market prices, and investors have unlimited access to borrowing and lending money at the risk-free interest rate. However, the market includes irrational and risk-seeking investors, large market participants who could influence market prices, and investors do not have unlimited access to borrowing and lending money.

Data Mining and Data Analysis

Python program for computing the Beta Values (for Large Cap stocks) and Volatility values (Sharpe Ratio for Mid and Small Cap stocks) and their respective graphs, with backtesting for a period of 8 years between 2010 and 2017. Attached Jupyter file.

Program Output showing Beta Values of NIFTY Large Cap:

BETA for AXISBANK.NS = 0.487182256157 BETA for BANKBARODA.NS = 1.67070112931 BETA for BHEL.NS = 1.13382747476 BETA for BPCL.NS = 0.957108807341 BETA for BHARTIARTL.NS = 2.02794355076 BETA for BOSCHLTD.NS = 0.686452429664 BETA for CIPLA.NS = 0.860547690925 BETA for DRREDDY.NS = 0.140269440021 BETA for GAIL.NS = 0.71714033757 BETA for GRASIM.NS = 0.938693207929 BETA for HCLTECH.NS = -0.0548932753272 BETA for HDFCBANK.NS = 0.40897820724 BETA for HEROMOTOCO.NS = 0.38530167959 BETA for HINDALCO.NS = 0.912377205048 BETA for HINDUNILVR.NS = 0.661294530545 BETA for HDFC.NS = 0.708105900244 BETA for ITC.NS = 0.719982657942 BETA for ICICIBANK.NS = 1.25709428897 BETA for IDEA.NS = 1.65109466247 BETA for INDUSINDBK.NS = 0.145925058723 BETA for INFY.NS = 0.320620838896 BETA for KOTAKBANK.NS = 0.311821916815 BETA for LT.NS = 0.830428969055 BETA for LUPIN.NS = 0.950584724663 BETA for M&M.NS = 0.834359975543 BETA for MARUTI.NS = 0.50516594651 BETA for NTPC.NS = 0.401236034503 BETA for ONGC.NS = 0.299660745978 BETA for POWERGRID.NS = 0.264765108639 BETA for PNB.NS = 2.86309626659 BETA for RELIANCE.NS = 0.71447842214 BETA for SBIN.NS = 1.88517291688 BETA for SUNPHARMA.NS = 0.646032070969 BETA for TCS.NS = 0.0469196060705 BETA for TATAMOTORS.NS = 1.39969079663 BETA for TATAPOWER.NS = 1.36394493718 BETA for TATASTEEL.NS = 1.08812109449 BETA for TECHM.NS = 0.364238635782 BETA for ULTRACEMCO.NS = 0.970703462283 BETA for VEDL.NS = 1.25182933044 BETA for WIPRO.NS = 0.333721019413 BETA for YESBANK.NS = 0.828300147 BETA for ZEEL.NS = 0.155813374019

Program Output: Volatility for MID and SMALL CAP Stocks

VOL_JPASSOCIAT.NS 4.431737 VOL_GNFC.NS 3.574764 VOL_PNCINFRA.NS 2.278846 VOL_STRTECH.NS 2.229402 VOL_INOXWIND.NS 2.090468 VOL_INFIBEAM.NS 2.008561 VOL_GSFC.NS 1.991663 VOL_RAIN.NS 1.894089 VOL_BBTC.NS 1.829212 VOL_MOIL.NS 1.827504 VOL_FCONSUMER.NS 1.822743 VOL_DBL.NS 1.742365 VOL_ITI.NS 1.710671 VOL_AVANTIFEED.NS 1.693155 VOL_KWALITY.NS 1.641093 VOL_JETAIRWAYS.NS 1.639408 VOL_JUSTDIAL.NS 1.637007 VOL_DELTACORP.NS 1.635044 VOL_ICIL.NS 1.629784 VOL_SOBHA.NS 1.560555 VOL_NCC.NS 1.523700 VOL_SREINFRA.NS 1.474480 VOL_NIITTECH.NS 1.465744 VOL_HDIL.NS 1.434779 VOL_CHENNPETRO.NS 1.421684 VOL_TRIDENT.NS 1.414574 VOL_GRANULES.NS 1.395518 VOL_BEML.NS 1.390699 VOL_GMDCLTD.NS 1.359200 VOL_RNAVAL.NS 1.358851 ... ... VOL_NFL.NS 0.860680 VOL_HIMATSEIDE.NS 0.855493 VOL_JKLAKSHMI.NS 0.839273 VOL_FLFL.NS 0.835207 VOL_SHK.NS 0.818122 VOL_PERSISTENT.NS 0.789523 VOL_BALRAMCHIN.NS 0.781389 VOL_EIDPARRY.NS 0.769538 VOL_REPCOHOME.NS 0.763575 VOL_ATUL.NS 0.757913 VOL_LAURUSLABS.NS 0.742563 VOL_SOUTHBANK.NS 0.737751 VOL_VRLLOG.NS 0.715091 VOL_CEATLTD.NS 0.692976 VOL_WABAG.NS 0.664062 VOL_TIMKEN.NS 0.615183 VOL_GODFRYPHLP.NS 0.598700 VOL_DENABANK.NS 0.591947 VOL_UCOBANK.NS 0.578498 VOL_NAVKARCORP.NS 0.544169 VOL_SCHNEIDER.NS 0.538137 VOL_BSE.NS 0.522614 VOL_RAYMOND.NS 0.490265 VOL_FSL.NS 0.474156 VOL_CGPOWER.NS 0.466409 VOL_ITDC.NS 0.448447 VOL_MONSANTO.NS 0.435284 VOL_DCBBANK.NS 0.435099 VOL_JKTYRE.NS 0.387489 VOL_OMAXE.NS 0.294883

Once you have arrived at the Beta Values for Large Cap, Sharpe Ratio/Volatility Values for Mid and Small Cap Stocks, construct a Portfolio with Top 7-8 stocks each in a Large Cap, Mid Cap and Small Cap and arrive at “MYPORTFOLIO” with ~25 stocks.

Python program to consider identified stocks in program #1 and construct “MYPORTFOLIO” and Plot Efficiency frontier with Max of Sharpe Ratio and Min of Volatility Values, thus arriving at 2 Portfolios showing the returns considering backtesting over the last 2 years from 2016-2017.

Selected Stocks in Portfolio:

VOL_UNIONBANK.NS 2.170028 VOL_BANKINDIA.NS 2.113974 VOL_RCOM.NS 1.990837 VOL_CANBK.NS 1.854292 VOL_PCJEWELLER.NS 1.834894 VOL_GMRINFRA.NS 1.766205 VOL_JINDALSTEL.NS 1.524516 VOL_L&TFH.NS 1.444537 """ Volatility Large cap VOL_JPASSOCIAT.NS 4.431737 VOL_GNFC.NS 3.574764 VOL_PNCINFRA.NS 2.278846 VOL_STRTECH.NS 2.229402 VOL_INOXWIND.NS 2.090468 VOL_INFIBEAM.NS 2.008561 VOL_GSFC.NS 1.991663 VOL_RAIN.NS 1.894089 VOL_BBTC.NS 1.829212 VOL_MOIL.NS 1.827504 VOL_FCONSUMER.NS 1.822743 VOL_DBL.NS 1.742365 VOL_ITI.NS 1.710671

Program output showing efficient frontier for 2 portfolios with MYPORTFOLIO, showing values of returns, Volatility and Sharpe Ratio for the Portfolio.

Two Portfolios with Max Sharpe Ratio and Min Volatility

Portfolio # 1

Returns 0.250297 Volatility 0.155174 Sharpe Ratio 1.613012 AXISBANK.NS 0.030742 BANKBARODA.NS 0.029452 BHEL.NS 0.003374 HEROMOTOCO.NS 0.003664 CIPLA.NS 0.078108 DRREDDY.NS 0.054943 SBIN.NS 0.025007 HCLTECH.NS 0.070226 RELIANCE.NS 0.106834 HINDUNILVR.NS 0.101651 UNIONBANK.NS 0.101836 BANKINDIA.NS 0.032457 RCOM.NS 0.011342 GMRINFRA.NS 0.014042 JINDALSTEL.NS 0.062114 PCJEWELLER.NS 0.035489 L&TFH.NS 0.068476 JPASSOCIAT.NS 0.023635 GNFC.NS 0.056779 PNCINFRA.NS 0.070353 STRTECH.NS 0.015912 INOXWIND.NS 0.003564

Portfolio # 2

Returns 0.398010 Volatility 0.197242 Sharpe Ratio 2.017875 AXISBANK.NS 0.087238 BANKBARODA.NS 0.003753 BHEL.NS 0.055004 HEROMOTOCO.NS 0.016172 CIPLA.NS 0.014446 DRREDDY.NS 0.012755 SBIN.NS 0.075367 HCLTECH.NS 0.070347 RELIANCE.NS 0.002490 HINDUNILVR.NS 0.009251 UNIONBANK.NS 0.097322 BANKINDIA.NS 0.010150 RCOM.NS 0.000398 GMRINFRA.NS 0.029947 JINDALSTEL.NS 0.069755 PCJEWELLER.NS 0.080285 L&TFH.NS 0.088866 JPASSOCIAT.NS 0.005632 GNFC.NS 0.093626 PNCINFRA.NS 0.070391 STRTECH.NS 0.105415 INOXWIND.NS 0.001390--------------COMPUTING ALPHA AND BETA FOR PORTFOLIO----------

PORTFOLIO BETA= 1.30107342631PORTFOLIOALPHA= 0.224494080754PORTFOLIOVOLATILITY= 0.228721920896MOMENTUM= 0.28839782936

----------------PORTFOLIO RETURNS----------------------------

Data Analysis based on the output from EFFICIENCY FRONTIER OF MYPORTFOLIO STOCKS

MYPORTFOLIO – with a combination of Multi-Cap stocks provides the Investor with two options:

Relatively Lower Risk with Moderate Return which has a Portfolio Return of 25% with Volatility of 15% and Portfolio Sharpe Ratio of 1.61

Relatively Higher Risk with Higher Returns which has a Portfolio Return of 39% with Volatility of 19% and Portfolio Sharpe Ratio of 2.01

Based on the risk profile of the Investor, he/she may choose to go with either of portfolio 1 or 2 for Investment purposes.

Key Findings

Summarizing the above-mentioned steps, Quantitative Finance techniques help:

Identify Beta values for Large, Mid and Small Cap Stocks

Identify Volatility values for these stocks

Back Testing of the Index with stocks and performance over 8 years period

Help arrives at a set of stocks that could constitute MyPortfolio (max of 25 stocks)

Determine the weights to be provided to each stock in the basket/portfolio

Determine the Efficiency Frontier for 2 portfolios based on backtesting for 2 years

Provide Options to the Investor depending on the Risk Profile, with a guidance around Expected Returns, Volatility and Sharpe Ratio of the underlying two portfolios with stock weights

Quantitative Finance provides a scientific approach to thePortfolio Managementprocess by helping us arrive at a set of optimal stocks and determine the Efficient Frontier for this optimal portfolio.

Learnings from Efficient Frontier

The efficient frontier is the set of optimal portfolios that offers the highest expected return for a defined level of risk or the lowest risk for a given level of expected return.

Since the efficient frontier is curved, rather than linear, a key finding of the concept was the benefit of diversification. Optimal portfolios that comprise the efficient frontier tend to have a higher degree of diversification than the sub-optimal ones, which are typically less diversified.

One assumption in investing is that a higher degree of risk means a higher potential return. Conversely, investors who take on a low degree of risk have a low potential return. According to Markowitz's theory, there is an optimal portfolio that could be designed with a perfect balance between risk and return. The optimal portfolio does not simply include securities with the highest potential returns or low-risk securities. The optimal portfolio aims to balance securities with the greatest potential returns with an acceptable degree of risk or securities with the lowest degree of risk for a given level of potential return. The points on the plot of risk versus expected returns where optimal portfolios lie are known as the efficient frontier.

Assume a risk-seeking investor uses the efficient frontier to select investments. The investor would select securities that lie on the right end of the efficient frontier. The right end of the efficient frontier includes securities that are expected to have a high degree of risk coupled with high potential returns, which is suitable for highly risk-tolerant investors. Conversely, securities that lie on the left end of the efficient frontier would be suitable for risk-averse investors.

Challenges/Limitations

The efficient frontier and modern portfolio theory have many assumptions that may not properly represent reality. For example, one of the assumptions is that asset returns follow a normal distribution. In reality, securities may experience returns that are more than three standard deviations away from the mean more than 0.03% of the observed values. Consequently, asset returns are said to follow a leptokurtic distribution or heavy-tailed distribution.

Additionally, Markowitz's theory assumes investors are rational and avoid risk when possible, there are not large enough investors to influence market prices, and investors have unlimited access to borrowing and lending money at the risk-free interest rate. However, the market includes irrational and risk-seeking investors, large market participants who could influence market prices, and investors do not have unlimited access to borrowing and lending money.

Additional considerations in the process of selecting Investments

The above approach to selecting Investments/stocks and constructing MyPortfolio is purely based on Quantitative stocks. However, it would be advisable to consider fundamental data to arrive at a Quantitative Value Investing Strategy. - For example, select the initial set of stocks that meet the following criteria by using fundamental data, say: P/E < 12, P/B < 2, ROE > 15%, market cap > 500 crores - And post meeting up of the criteria, follow the steps in the Python program to determine the Efficient Frontier of Investment portfolio. This will enhance picking up VALUE stocks.

Macroeconomic factors to help determine the sectoral allocation of the portfolio. We have gone in our example with a portfolio selection based on backtesting of data and this does not consider any specific consideration to the sectoral allocation of the portfolio. - For example, last 3 years India has seen a continuing drop in Crude Oil Prices which has, in turn, helped the Oil Marketing companies to do well. However, a sudden rise in Crude Oil prices at the beginning of 2018 gives us a view that we should be considering more of Oil refining companies in the mix. A similar logic will hold true for beaten down sectors with IT and Pharma over last 2 years but with the improving prospects in 2018, one could choose to increase sectoral allocation to these industry segments.

Additionally, Markowitz's theory assumes investors are rational and avoid risk when possible, there are not large enough investors to influence market prices, and investors have unlimited

Implementation Methodology (if live/practical project)

We have constructed MYPORTFOLIO in this live project, and have gone with the following methodology:

Python program to help us determine the Large Cap Stocks based on Beta Values, Mid and Small Cap stocks based on Volatility values to arrive at the initial set of 25 stocks, and

Efficient Frontier to help us determine two portfolios with expected returns, volatility and Sharpe Ratio.

Both the Python programs have been run, and the program outputs have been obtained from Spyder and values pasted in this project report.

The following video that explains - “Portfolio Assets Allocation: A practical and scalable framework for Machine Learning Development” by Raimondo Marino from Milan, Italy and “Portfolio Optimization for Dividend Stocks” by Kurt Selleslagh from Singapore.

ThisPortfolio Assets Allocation with Machine Learningarticle is the final project submitted by the author Raimondo Marino as a part of his coursework in the Executive Programme in Algorithmic Trading (EPAT) at QuantInsti.

Conclusion

Quantitative Finance Techniques help us in a significant way in the Investment selection process and thus arriving at an Optimum Portfolio of stocks.

The Portfolio Management Theory and the Efficient Frontier though defined in the early 1950s stand relevant even today, and the Quantitative Finance techniques help us in the practical implementation of these theories to arrive at Optimal Portfolio in the Indian stock markets.

You can enroll for theportfolio management courseon Quantra. In this course, you will learn different portfolio management techniques such as Factor Investing, Risk Parity and Kelly Portfolio, and Modern Portfolio Theory.

If you are more interested in learning about Fama-French models, you can also check out theFama-French five-factor model.

Annexure/Codes

The Python programs have been attached along with this project report in the same ZIP file, relevant program outputs have been incorporated in this report.

Bibliography

EPAT    Executive Programme in Algorithmic Trading MPT     Modern Portfolio Theory CAPM  Capital Asset Pricing Model EF        Efficient Frontier NSE     National Stock Exchange of India EMH     Efficient Markets Hypothesis NIFTY  The NIFTY index is NSE's benchmark stock market index for the Indian equity

Our sincere thanks to the faculty and coaches at QuantInsti to have taught us the Quantitative Finance techniques, and the guidance provided by our Mentor Abhishek Kulkarni in the process of executing this project.

Disclaimer: The information in this project is true and complete to the best of our Student’s knowledge. All recommendations are made without guarantee on the part of the student or QuantInsti®. The student and QuantInsti® disclaim any liability in connection with the use of this information. All content provided in this project is for informational purposes only and we do not guarantee that by using the guidance you will derive a certain profit.

Files in the download:

NotebookPortfolio - Python Code

Login to Download

---

*Imported from QuantInsti Blog on 2026-04-27*
