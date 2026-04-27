---
title: "Ito's Lemma Applied to Stock Trading"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/itos-lemma-applied-stock-trading/"
date: "2024-12-06"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Ito's Lemma Applied to Stock Trading

**来源**: [QuantInsti](https://blog.quantinsti.com/itos-lemma-applied-stock-trading/)  
**日期**: 2024-12-06  
**作者**: QuantInsti

---

## 原文

Ito's Lemma Applied to Stock Trading

ByMahavir A. BhattacharyaThis is the second part of the two-part blog where we explore how Ito’s Lemma extends traditional calculus to model the randomness in financial markets. Using real-world examples and Python code, we’ll break down concepts like drift, volatility, and geometric Brownian motion, showing how they help us understand and model financial data, and we’ll also have a sneak peek into how to use the same for trading in the markets.

In the first part, we saw how classical calculus cannot be used for modeling stock prices, and in this part, we’ll have an intuition of Ito’s lemma and see how it can be used in the financial markets. Here’s the link to part I, in case you haven’t gone through it yet:Laying the Groundwork for Ito's Lemma and Financial Stochastic Models

This blog covers:

Pre-requisites

Quick Recap

Ito Calculus

Ito's Lemma Applied to Stock Prices

Use Case - I of Ito's Lemma

Important Considerations

Use Case - II of Ito's Lemma

Till Next Time

Pre-requisites

You will be able to follow the article smoothly if you have elementary-level proficiency in:

Calculus

Python coding

Quick Recap

In part I of this two-blog series, we learned the following topics:

The chain rule

Deterministic and stochastic processes

Drift and volatility components of stock prices

Weiner processes

In this part, we shall learn about Ito calculus and how it can be applied to the markets for trading.

Ito Calculus

Remember  from part I? \( W_t \) is why Ito came up with the calculus he did. In classical calculus, we work with functions. However, in finance, we frequently work with stochastic processes, where \( W_t \) represents stochasticity.

Rewriting the equations from part I:

The equation for chain rule:

$$\frac{dy}{dx} = \frac{dy}{dz} \cdot \frac{dz}{dx}$$–-------------- 1

The equation for geometric Brownian motion (GBM):

$$dS_t = \mu S_t , dt + \sigma S_t , dW_t$$--------------- 2

Equation 2 is a differential equation. The presence of \( W_t \) makes the GBM a stochastic differential equation (SDE).  What’s so special about SDEs?

Remember the chain rule discussed in part I? That’s only for deterministic variables. For SDEs, our chain rule is Ito’s lemma!

Let’s get down to business now.

Ito's Lemma Applied to Stock Prices

The following equation is an expression of Ito’s lemma:

$$df(S_t) = f'(S_t) dS_t + \frac{1}{2} f''(S_t) d[S, S]_t$$--------------- 3

f(x) is a function which can be differentiated twice, and

S is a continuous process, having bounded variation

What do we mean by bounded variation?

It simply means that the difference between St+1 and St, for any value of t, would never exceed a certain value. What this ‘certain value’ is, is not of much significance. What is significant is that the difference between two consecutive values of the process is finite.

Next question: What’s \( [S, S]_t \)?

It’s a notation.

Of what?

A notation to denote a quadratic variation process.

What’s that?

In this blog, we won’t get into the intuition of the quadratic variation. It would suffice to know that the quadratic variation of \( S_t \), i.e., \( [S, S]_t \) is as follows:

$$ \begin{matrix} \lim_{\Delta t \to 0} & \sum_{0}^{t} \left(S_{t_{i+1}} - S_{t_i}\right)^2 \end{matrix} $$

If St follows a Brownian motion, the derivative of its quadratic variation is:

$$d[S, S]_t = \sigma^2 S_t^2 dt$$--------------- 4

Substituting equation 4 in equation 3, we get:

\[ df(S_t) = f'(S_t) dS_t + \frac{1}{2} f''(S_t) \sigma^2 S_t^2 dt \]

--------------- 5

How is this derived?

We can treat equation 5 as a Taylor series expansion till the second order. If you aren’t familiar with it, don’t worry; you can continue reading.

Still, what’s the intuition? Here, f is a function of the process S, which itself is a function of time t. The change in f depends on:

The first-order partial derivative of f with respect to S,

The second-order partial derivative of f with respect to t,

The square of the volatility σ, and,

The square of S.

The last three are multiplied and then added to the first one.

We saw earlier that stock returns follow a Brownian motion, so stock prices follow a GBM. Hence,  suppose we have a process \( R_t \) , which is equal to log(\( S_t \)).

If we take \( R_t \) = log(\( S_t \)) in the GBM SDE (equation 2), and if we use the expression for Ito’s lemma (equation 3), we’ll have:

$$f(S_t) = R_t = \log(S_t)$$--------------- 6

$$dR_t = \frac{dS_t}{S_t} - \frac{d[S_t, S_t]}{2S_t^2}$$--------------- 7

Since $$dS_t = \mu S_t , dt + \sigma S_t , dW_t$$ and

$$d[R, R]_t = \sigma^2 S^2 \, dt$$ (equation 4),

we can rewrite equation 7 as:

$$dR_t = \left(\mu - \frac{\sigma^2}{2}\right)dt + \sigma dW_t$$--------------- 8

Since the second term on the RHS doesn’t depend on the LHS, we can use direct integration to solve equation 8:

$$R_t = R_0 + \left(\mu - \frac{\sigma^2}{2}\right)t + \sigma W_t$$--------------- 9

\[ R_t = \log(S_t) \quad \text{and} \quad S_t = \exp(R_t), \]

Thus, equation 9 changes to:

$$S_t = S_0 \cdot e^{\left(\mu - \frac{\sigma^2}{2}\right)t + \sigma W_t}$$--------------- 10

Let’s understand what the equation means here. The stock price at time t = 0, when multiplied by this term:

$$e^{\left(\mu - \frac{\sigma^2}{2}\right)t + \sigma W_t}$$--------------- 11

would give the stock price at time t.

In equation 2, the drift component had just \( \mu \), but in equation 10, we subtract \( \frac{\sigma^2}{2} \) from \( \mu \). Why so? Remember how we obtain \( \mu \)? By taking the mean of daily log returns, right?

Umm, no! As mentioned in part I, μ is the average percentage drift (or returns), and NOT the logarithmic drift.

As we saw from the drift component and volatility component graphs, the close price isn’t just the drift component, but also the volatility component added to it. Hence, we need to correct the drift to consider the volatility component as well. It is towards this correction that we subtract \( \frac{\sigma^2}{2} \) from μ. The intuition here is that the arithmetic mean of a set of non-negative real numbers is greater than or equal to the geometric mean of the same set of numbers. The value of μ before the correction is the arithmetic mean, and after the correction, it is close to the geometric mean. When taken on an annual basis, the geometric mean is the CAGR.

How do we interpret equation 10? The current stock price is simply a function of the past stock price, the corrected drift, and the volatility.

How do we use this in the markets? Let’s see…

Use Case - I of Ito's Lemma

Note:The codes in this part are continued from part I, and the graphs and values obtained are as of October 18, 2024.

Output:

The mean of the daily percent returns = 0.00109
The standard deviation of the daily percent returns = 0.01707
The variance of the daily percent returns = 0.00029

Output:

Daily compounded returns = 0.00094878

Output:

Corrected daily percent returns = 0.000949

The arithmetic mean of the returns was initially0.00109, and the geometric mean (daily compounded returns) computes to0.00094878. After incorporating the drift correction, the arithmetic mean stood at0.000949. Quite close to the geometric mean!

How do we use this for trading?

Suppose we wanna predict the range within which the price of Microsoft is likely to lie after, say, 42 trading days (2 calendar months) from now.

Let’s seek refuge in Python again:

Output:

Corrected drift for 42 days = 0.03985788
Variance for 42 days = 0.01223456
Standard deviation for 42 days = 0.11060996

Output:

Price below which the stock isn't likely to trade with a 95% probability after 42 days = 347.6
Price above which the stock isn't likely to trade with a 95% probability after 42 days = 541.04

We know with 95% confidence between which ranges the stock is likely to lie after 42 trading days from now! How do we trade this? Ways are many, but I’ll share one specific method.

Output:

Put with strike 345:

Contract Symbol:   MSFT241220P00345000  
Last Trade Date:   2024-10-17 19:44:37+00:00  
Strike:            345.0  
Last Price:1.53Bid:               0.0  
Ask:               0.0  
Change:            0.0  
Percent Change:    0.0  
Volume:            1.0  
Open Interest:     0  
Implied Volatility: 0.125009  
In The Money:      False  
Contract Size:     REGULAR  
Currency:          USD

Call with strike 545:

Contract Symbol:   MSFT241220C00545000  
Last Trade Date:   2024-10-16 13:45:27+00:00  
Strike:            545.0  
Last Price:0.25Bid:               0.0  
Ask:               0.0  
Change:            0.0  
Percent Change:    0.0  
Volume:            169  
Open Interest:     0  
Implied Volatility: 0.125009  
In The Money:      False  
Contract Size:     REGULAR  
Currency:          USD

We have chosen out-of-the-money strikes near the 95% confidence price range we obtained earlier.

This way, we can pocket around $1.53 + $0.25 (emboldened in the above output) = $1.78 per pair of stock options sold, if held till expiry. If we sell one lot each of these call and put option contracts, we can pocket $178, since the lot size is 100. And what’s the assurance of us making this profit? 95%, right? Simplistically, yes, but let’s move closer to reality now.

Important Considerations

Assumption of Normality:We used mean +/- 2 standard deviations and kept talking about 95% confidence. This works in a world where the stock returns are normally distributed. But in the real world, they are not! And more often than not, this deviation from a normal distribution works against us since people react faster to news of impending doom over news of euphoria.

Transaction Costs:We didn’t consider the transaction costs, taxes, and implementation shortfalls.

Backtesting:We haven’t backtested (and forward tested) whether the prices have historically lied (and would lie in the future) within the predicted price ranges.

Opportunity Costs:We also didn’t consider the margin requirements and the opportunity costs, were we to deploy some margin amount in this strategy.

Volatility:Finally, we are trading volatility here, not the price. We’ll end up pocketing the whole premium only if both the options expire worthless, i.e., out-of-the-money. But for that to happen, the volatility must be low until the expiry. We must account for the implied volatilities obtained in the previous code output. Oh, and by the way, how is this implied volatility calculated?

To better understand how volatility affects options pricing, consider exploring our course onoption volatility, where you'll learn key concepts like implied volatility and its impact on your trades.

Use Case - II of Ito's Lemma

We calculate the implied volatility from the classic Black-ScholesMerton model for option pricing. And how did Fischer Black, Myron Scholes, and Robert Merton develop this model? They stood on the shoulders of Kiyoshi Ito! 🙂

Till Next Time

And this is where I bid au revoir! Do backtest the code and check whether it can predict the range of future prices with reasonable accuracy. You can also use mean +/- 1 standard deviation in place of 2 standard deviation. The benefit? The range would be tighter, and you could pocket more premium. The flip side? The chances of being profitable get reduced to around 68%! You can also think of other ways how to capitalise on this prediction. Do let us know in the comments what you tried.

References:

Main Reference:

https://research.tilburguniversity.edu/files/51558907/INTRODUCTION_TO_FINANCIAL_DERIVATIVES.pdf

Auxiliary References:

Wikipedia pages of Ito’s lemma, Brownian motion, geometric Brownian motion, quadratic variation, and, AM-GM inequality

EPAT lectures on statistics and options trading

File in the download

Ito's_Lemma - Python notebook

Login to Download

All investments and trading in the stock market involve risk. Any decision to place trades in the financial markets, including trading in stock or options or other financial instruments is a personal decision that should only be made after thorough research, including a personal risk and financial assessment and the engagement of professional assistance to the extent you believe necessary. The trading strategies or related information mentioned in this article is for informational purposes only.

---

*Imported from QuantInsti Blog on 2026-04-27*
