---
title: "The Risk-Constrained Kelly Criterion: From the foundations to trading"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/risk-constrained-kelly-criterion/"
date: "2024-11-25"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# The Risk-Constrained Kelly Criterion: From the foundations to trading

**来源**: [QuantInsti](https://blog.quantinsti.com/risk-constrained-kelly-criterion/)  
**日期**: 2024-11-25  
**作者**: QuantInsti

---

## 原文

The Risk-Constrained Kelly Criterion: From the foundations to trading

ByJosé Carlos Gonzáles Tanaka

The Kelly Criterion is good enough for long-term trading where the investor is risk-neutral and can handle big drawdowns. However, we cannot accept long-duration and big drawdowns in real trading. To overcome the big drawdowns caused by the Kelly Criterion, Busseti et al. (2016) offered a risk-constrained Kelly Criterion that incorporates maximizing the long-term log-growth rate together with the drawdown as a constraint. This constraint allows us to have a smoother equity curve. You will learn everything about the new type of Kelly Criterion here and apply a trading strategy to it. You can find the risk-constraint Kelly criterion code onGitHubas well.

This blog covers:

The Kelly criterion

The risk-constrained Kelly criterion

A trading strategy based on the risk-constrained Kelly Criterion

The Kelly criterion

The Kelly Criterion is a well-known formula for allocating resources into a portfolio.

You can learn more about it by using many resources on the Internet. For example, you can find a quickdefinition of Kelly Criterion,a blog with an example of position sizing, and even awebinar on Risk Management.

We won’t go deep on the explanation since the above links already do that. Here, we provide the formula and some basic explanation for using it.

where,

K% = The Kelly percentage

W = Winning probability

R = Win/loss ratio

Let’s understand how to apply.

Suppose we have your strategy returns for the past 100 days. We get the hit ratio of those strategy returns and set it as “W”. Then we get the absolute value of the mean positive return divided by the mean negative return. The resulting K% will be the fraction of your capital for your next trade.

The Kelly Criterion ensures the maximum long-term return for your trading strategy. This is from a theoretical perspective. In practice, if you applied the criterion in your trading strategy, you would face many long-lasting big drawdowns.

To solve this problem, Busseti et al. (2016) provided the “risk-constrained Kelly Criterion”, which allows us to have a smoother equity curve with less frequent and small drawdowns.

The risk-constrained Kelly criterion

The Kelly criterion relates to an optimization problem. For the risk-constraint version, we add, as the name says, a constraint. The basic principle of the constraint can be formulated as:

The drawdown risk is defined as Prob(Minimum Wealth < alpha), where alpha ∈ (0, 1) is a given target (undesired) minimum wealth. This risk depends on the bet vector b in a very complicated way. The constraint limits the probability of a drop in wealth to value alpha to be no more than beta.

The authors highlight the important issue that the optimization problem with this constraint is highly complex thing to solve. Consequently, to make it easier to solve it, Busseti et al. (2016) provided a simpler optimization problem in case we have only 2 outcomes (win and loss), which is the following:

Where:

Pi: Winning probability

P: The payoff of the win case.

b1: The kelly fraction to be found. b1= K%. The control variable of the maximization problem

Lambda: The risk aversion of the trader: log(beta)/log(alpha)

Please take into account that the win/loss ratio defined in the basic criterion named as R is:

R = P - 1, where P is the payoff of the win case described for the risk-constrained Kelly criterion.

You might ask now: I don’t know how to solve that optimization problem! Oh no!

I can surely help with that! The authors have proposed a solution. See below!

The solution algorithm for the risk-constrained Kelly criterion goes like this:

If B1 = (pi*P-1)/(P-1) satisfies the risk constraint, then that is the solution. Otherwise, we find b1 by finding the b1 value for which

As explained by the authors, the solution can be found with a bisection algorithm.

A trading strategy based on the risk-constrained Kelly Criterion

Let’s inspect a trading strategy based on the risk-constrained Kelly criterion!

Let’s import the libraries.

Let’s define our customized bisection method for later use:

Let’s define our 2 functions to be used to compute the risk-constraint Kelly criterion bet size:

Let’s import the MSFT stock data from 1990 to October 2024 and compute the buy-and-hold returns.

Let’s get all the available technical indicators in the “ta” library:

Let’s create the prediction feature and some relevant columns.

Let’s define the seed and some other relevant variables.

We will use a for loop  to iterate through each date.

The algorithm goes like this, for each day:

Sub-sample the data where we’ll use one year of data and the last 60 days as the test span for the sub-sample data

Split the data into X and y and their respective train and test sections

Fit a Support Vector machine model

Predict the signal

Obtain the strategy returns

Get the positive mean return as pos_avg

Get the negative mean return as neg_avg

Get the number of positive returns as pos_ret_num

Get the number of negative returns as neg_ret_num

Set some conditions to get the position size for the day

Get the basic-Kelly and risk-constraint Kelly fraction

Split the data once again as train and test data to

Estimate once again the model, and

Predict the next-day signal

Let’s compute the strategy returns. We compute 2 strategies, the basic Kelly strategy and the risk-constrained Kelly strategy. Apart from that,  I’ve incorporated an “improved” version of the strategy which consists of having the same signal of the previous 2 strategies, but with the condition that the buy-and-hold cumulative returns is higher than their 30-day moving average.

Let’s see now the graphs. We see the basic Kelly position sizes.

Output:

It has high volatility. It ranges from 0 to 0.6.

Let’s see the risk-contraint Kelly fractions.

Output:

It now ranges from 0 to 0.25. It has a lower range of volatility.

Let’s see the strategy returns from the both.

Output:

The basic Kelly strategy has a higher drawdown, as informally checked. The main drawback of the risk-constraint Kelly strategy is the lower equity curve.

Let’s see the improved strategy returns.

Output:

It’s interesting to see that the basic Kelly strategy gets to reduce its drawdown, the same for the risk-constrained strategy. The risk-constrained strategy keeps having a low equity curve.

Some comments:

Once you have a good Sharpe ratio, you can increase the leverage. So, don’t get disappointed by the low equity curve of the risk-constraint Kelly strategy. I leave as an exercise to check that.

You can increase the equity returns with stop-loss and take-profit targets.

You can combine the risk-constraint Kelly criterion with meta-labelling.

The risk-constraint Kelly criterion limitation is the low equity curve. You can imagine solutions to improve the results!

You can use the pyfolio-reloaded library to implement the trading summary statistics and analytics to check formally the lower drawdown and volatility of the risk-constraint Kelly strategy.

Conclusion

As you can see, you can implement the risk-constraint Kelly Criterion to get a smoother equity curve. The main issue might be that it gets you a lower cumulative return, but it can help find days you don’t need to trade, saving you drawdowns!

If you want to learn more about position sizing, don’t forget to take our course onposition sizing!

References

Busseti, E., Ryu, E. K., Boyd, S. (2016), “Risk-Constrained Kelly Gambling”, Working paper.https://web.stanford.edu/~boyd/papers/pdf/kelly.pdf

File in the download

The Kelly Criterion - Python notebook

Login to Download

Disclaimer: All data and information provided in this article are for informational purposes only. QuantInsti®makes no representations as to accuracy, completeness, currentness, suitability, or validity of any information in this article and will not be liable for any errors, omissions, or delays in this information or any losses, injuries, or damages arising from its display or use. All information is provided on an as-is basis..

---

*Imported from QuantInsti Blog on 2026-04-27*
