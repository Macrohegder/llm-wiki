---
title: "Portfolio Optimization For Maximum Return-To-Risk Ratio Using Python"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/portfolio-optimization-maximum-return-risk-ratio-python/"
date: "2018-02-08"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Portfolio Optimization For Maximum Return-To-Risk Ratio Using Python

**来源**: [QuantInsti](https://blog.quantinsti.com/portfolio-optimization-maximum-return-risk-ratio-python/)  
**日期**: 2018-02-08  
**作者**: QuantInsti

---

## 原文

Portfolio Optimization Using Monte Carlo Simulation

ByMohak Pachisia&Mandeep Kaur

In theprevious blogof this series, we saw how to compute the mean and the risk (or standard deviation) of a portfolio containing 'n' number of stocks, each stock 'i' having a weight of 'wi'.

In this blog, we will examine the process ofportfolio optimisationthrough the reallocation of asset weights. Portfolio optimisation, in this context, refers to constructing an asset allocation that aligns with one of several possible investment objectives.

Conditions of Portfolio Optimization

Portfolio optimization typically seeks to identify an allocation of capital across assets that satisfies one of the following conditions:

Maximum Sharpe Ratio Portfolio (Tangency Portfolio): A portfolio that maximizes the return-to-risk ratio, formally defined as the Sharpe ratio, which is the excess return over the risk-free rate per unit of risk.

Minimum Variance Portfolio: A portfolio that achieves the lowest possible risk (as measured by portfolio variance or standard deviation) for a given level of expected return.Maximum Return Portfolio at a Given Risk: A portfolio that delivers the highest expected return for a specified level of risk.

Annual Returns and Standard Deviation

This article utilizes annualised returns and annualised standard deviation, based on one year ofstock data(2024). However, in practical applications, annualised returns and annualised standard deviation could also be employed. The conversion from daily to annual figures is performed using the standard formulas, assuming 252 trading days in a calendar year:

Annualised Returns = Mean of daily return* 252

Annualised Standard Deviation = Daily Standard Deviation* sqrt(252)

Let us consider a portfolio consisting of four stocks in banking/financial services sector, namely: Bank of America (BAC), Goldman Sachs (GS), JP Morgan Chase & Co (JPM) and Morgan Stanley (MS).

To start with, we’ll assign random weights to all four stocks, keeping the sum of the weights to be 1. We will compute the return and standard deviation of the portfolio as we did in the previous blog and record it. We will then run Monte Carlo Simulations on our portfolio to get the optimal weights for the stocks. We will usepythonto demonstrate how portfolio optimization can be achieved. Before moving on to the step-by-step process, let us quickly have a look atMonte Carlo Simulation.

Monte Carlo Simulation

This simulation is extensively used in portfolio optimization. In this simulation, we will assign random weights to the stocks. One important point to keep in mind is that the sum of the weights should always sum up to 1. At every particular combination of these weights, we will compute the return and standard deviation of the portfolio and save it. We’ll then change the weights and assign some random values and repeat the above procedure.

The number of iterations depends on the error that the trader is willing to accept. Higher the number of iterations, higher will be the accuracy of the optimization but at the cost of computation and time. For the purpose of this blog, we will restrict ourselves to 10000 such iterations. Out of these 10000 results for returns and corresponding standard deviation, we can then achieve portfolio optimization by identifying a portfolio that satisfies on any of the 3 conditions discussed above.

Portfolio Optimization Process in Python

Let’s start by importing relevantlibrariesand fetching the data for the stocks for  the year 2024.

The data looks as shown:

B_A_C	          G_S	         J_P_M	         M_S
Date

2024-01-02	32.851429	377.245605	166.179565	89.284668
2024-01-03	32.492874	370.920959	165.455276	87.392487
2024-01-04	32.754520	372.047943	166.553253	87.620689
2024-01-05	33.365032	375.438599	167.388885	88.657104
2024-01-08	33.103386	377.789673	167.145996	88.913834

We will then convert these stock prices into returns and will save this under the name ‘stock_ret’.

Output:

We will now calulate the mean return of all stocks and thecovariance matrix.

Output:

B_A_C    0.311970
G_S      0.450367
J_P_M    0.383907
M_S      0.364621
dtype: float64
          B_A_C       G_S     J_P_M       M_S
B_A_C  0.052034  0.043756  0.040258  0.040840
G_S    0.043756  0.066842  0.047369  0.053826
J_P_M  0.040258  0.047369  0.055535  0.040262
M_S    0.040840  0.053826  0.040262  0.068850

Let us define an array to hold the result of each iteration. The array will hold the returns, standard deviation,Sharpe ratioand weights for each step in the iteration. We will define one result array initially containing all zeroes and will save the simulation results in this array. The number of columns in the array is 7 to hold portfolio return, standard deviation, Sharpe Ratio and the weights of all stocks. The number of columns will change with the number of stocks in theportfolioas we have to store the weights for all the stocks. That's why we use the 'len function' while defining the array. The number of rows in the array is equal to the number of iterations.

Let’s now move on to the iterations.

We then save the output in a ‘pandasdata frame’ for easy analysis and plotting of data.

sim_frame = pd.DataFrame(simulation_res.T,columns=['ret','stdev','sharpe',stock[0],stock[1],stock[2],stock[3]])
print (sim_frame.head())
print (sim_frame.tail())

Output:

ret     stdev    sharpe       BAC        GS       JPM        MS
0  0.372583  0.217626  1.712036  0.306097  0.213561  0.299019  0.181323
1  0.363463  0.216364  1.679873  0.394337  0.130685  0.435499  0.039480
2  0.389084  0.222811  1.746252  0.133718  0.290982  0.339756  0.235544
3  0.387731  0.227346  1.705464  0.193391  0.360197  0.124769  0.321643
4  0.403024  0.230934  1.745187  0.147800  0.508287  0.134870  0.209043
           ret     stdev    sharpe       BAC        GS       JPM        MS
9995  0.393074  0.226539  1.735132  0.086871  0.322538  0.278485  0.312106
9996  0.380222  0.220915  1.721121  0.251156  0.283732  0.233118  0.231994
9997  0.378073  0.225809  1.674303  0.274834  0.308734  0.075159  0.341274
9998  0.361877  0.221326  1.635042  0.315757  0.127436  0.153136  0.403672
9999  0.386932  0.231995  1.667842  0.193662  0.371691  0.032976  0.401671

The above output shows the rows and columns of the simulation results. We can now select the portfolio with respect to the conditions we discussed earlier.

Maximum Sharpe Ratio Portfolio (Tangency Portfolio) :By locating the portfolio with the highest Sharpe Ratio

Minimum Variance Portfolio: By locating the portfolio with the lowest standard deviation

Maximum Return Portfolio at a Given Risk: By locating the portfolio with a specific standard deviation. Here take our target portfolio to have a standard deviation closest to 23%. Because our simulated portfolios may not have a portfolio that has an exact s.d of 23%, we take a threshold range of 0.05% and spot the portfolio closest to our target portfolio.

The portfolio for max Sharpe Ratio:
 ret       0.422893
stdev     0.235598
sharpe    1.794974
BAC       0.007436
GS        0.600565
JPM       0.371630
MS        0.020369
Name: 9591, dtype: float64
The portfolio for min risk:
 ret       0.347404
stdev     0.213900
sharpe    1.624142
BAC       0.458589
GS        0.000216
JPM       0.358250
MS        0.182945
Name: 1505, dtype: float64
The portfolio with standard deviation closest to 23%:
 ret       0.419614
stdev     0.234454
sharpe    1.789751
BAC       0.045694
GS        0.601202
JPM       0.303228
MS        0.049876
Name: 7443, dtype: float64

The output can be plotted using the matplotlib library as the relevant points can be highlighted as shown:

In the output, the red star shows the portfolio with the maximum Sharpe ratio, the blue star depicts the point with the minimum standard deviation, and the green star depicts the portfolio with the maximum return at chosen level of risk.

From the above curve, we can get the composition for the required optimal portfolio based on any of the three conditions as discussed above. We can select the portfolio with maximum return for a given risk or a portfolio with minimum risk for a given return or we can simply select the portfolio with maximum Sharpe ratio.

Summary

Just to summarize our complete analysis, we first downloaded the stock price data for one month and computed the mean return of all the stocks and the covariance matrix (which is used in computing the standard deviation of the portfolio). We then ran a Monte Carlo Simulation to compute the risk and return of the portfolio by randomly selecting the weights of the portfolio. We then identify the optimal portfolio based on the Sharpe ratio or other conditions.

Next Step

Our next blogcovers various aspects of the portfolio performance evaluation and portfolio performance measurement. It starts with why evaluation and measurement are necessary. Then explains how to compute and analyse the returns generated by the portfolio after a particular time period.

Update

We have noticed that some users are facing challenges while downloading the market data from Yahoo and Google Finance platforms. In case you are looking for an alternative source for market data, you can use Quandl for the same.

Download Python Code

Portfolio Optimization Using Monte Carlo Simulation - Python Code

Login to Download

Note: The original post has been revamped on 13thMay 2025 for recentness, and accuracy.

Disclaimer: All investments and trading in the stock market involve risk. Any decision to place trades in the financial markets, including trading in stock or options or other financial instruments, is a personal decision that should only be made after thorough research, including a personal risk and financial assessment and the engagement of professional assistance to the extent you believe necessary. The trading strategies or related information mentioned in this article is for informational purposes only.

---

*Imported from QuantInsti Blog on 2026-04-27*
