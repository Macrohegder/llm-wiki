---
title: "Laying the Groundwork for Ito's Lemma and Financial Stochastic Models"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/itos-lemma-trading-concepts-guide/"
date: "2024-12-06"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Laying the Groundwork for Ito's Lemma and Financial Stochastic Models

**来源**: [QuantInsti](https://blog.quantinsti.com/itos-lemma-trading-concepts-guide/)  
**日期**: 2024-12-06  
**作者**: QuantInsti

---

## 原文

Laying the Groundwork for Ito's Lemma and Financial Stochastic Models

ByMahavir A. BhattacharyaThis is a two-part blog where we’ll explore how Ito’s Lemma extends traditional calculus to model the randomness in financial markets. Using real-world examples and Python code, we’ll break down concepts like drift, volatility, and geometric Brownian motion, showing how they help us understand and model financial data, and we’ll also have a sneak peek into how to use the same for trading in the markets.

In the first part, we’ll see how classical calculus cannot be used for modeling stock prices, and in the second part, we’ll have an intuition of Ito’s lemma and see how it can be used in the financial markets.

If you are already conversant with the chain rule in calculus, the concepts of deterministic and stochastic processes, drift and volatility components in asset prices, and Wiener processes, you can skip this blog and directly read this one:Ito's Lemma Applied to Stock Trading

It has an involved discussion on Ito’s lemma, and how it is harnessed for trading in the financial markets.

This blog covers:

Pre-requisites

Etymology of Sorts

The Chain Rule

Deterministic and Stochastic Processes

Drift and Volatility Components on Python

Weiner Weiner Stochastic Dinner

Pre-requisites

You will be able to follow the article smoothly if you have elementary-level proficiency in:

Calculus

Python coding

Etymology of Sorts

You would have learned theorems in high school math. Simply put, a lemma is like a milestone in attempting to prove a theorem. So what is Ito’s lemma? Kiyoshi Ito came up with his own ways of calculus (as if the existing ones weren’t hard to learn already 😝). Why did he do that? Were there any problems with the existing methods? Let’s understand this with an example.

The Chain Rule

Suppose we have the following function:

$$ y = \sin(3x) $$

This function can also be written as:

$$y = \sin(z), \quad \text{where} \quad z = 3x$$

Here, y is a function of z, which itself is a function of x. Such functions are known as composite functions.

This means that whatever value x takes, z would take thrice its value, and whatever value z takes, y would take its corresponding sine value.

Suppose x doubles, what would happen to z? It would also double. And when x halves, z would also halve. Thus, z would always bear the same ratio with x, i.e., 3. The ratio between the change in z, and the change in x would also be 3. We refer to this as the derivative of z with respect to x, also denoted by: dz/dx.

From elementary calculus, you would know that dz/dx = 3.

Similarly, dy/dz = cos(x), that is, the tangent to the slope of the sinusoidal curve sin(x) at every point on the curve would be cos(x).

What about dy/dx?

We can solve this using the chain rule, shown below:

$$ \frac{dy}{dx} = \frac{dy}{dz} \cdot \frac{dz}{dx} $$					–-------------- 1

Substituting the above values for dy/dz and dz/dx,

$$ \frac{dy}{dx} = \cos(x) \cdot 3 = 3 \cos(x) $$

Straightforward, isn’t it?

Sure, but only when we deal with ‘functions’. The problem is, when it comes to finance, we deal with processes. What kind of processes? Well, we can have deterministic processes and stochastic processes.

Deterministic and Stochastic Processes

A deterministic process is one whose realized path, and value after certain intervals of time is known beforehand with certainty.  Examples would be the returns on a fixed deposit or the payouts of an annuity.

What about a stochastic process then? Can you think of something whose value can never be predicted with certainty, even for the next second? The path traversed by a stock! Can you imagine a world where the stock prices follow a deterministic path? No, right? But hey, we’ll discuss this too in a while now!

Coming back, in financial literature, stock prices are assumed to follow a Geometric Brownian motion. What’s that? Keep reading!

Suppose you ignite an incense stick. What variables contribute to the path that a single particle of fumes from the stick would follow? The wind speed in the surroundings, the direction of the wind, the density of the surrounding air, the absolute and relative proportion of other particles already present in the air, the size of the particles of the incense stick, the gap between each particle, the molecular orientation of the particles, their inflammability, and so on.

Even if you can create an elegant model that factors in the effect of all these variables, would you be able to predict with certainty the exact path that a single fume particle would traverse? No! Same is the case with asset prices. Suppose you know the fundamentals of the underlying, values of all technical indicators, the drift (we’ll come to this in a while), the volatility, the risk-free rate, macro-economic metrics, market sentiments, and everything else. Can you predict the exact path the price will take tomorrow?

If yes, well, you don’t need to read any further. Keep your secrets and make a ton of money 😁. Realistically, we cannot predict it with certainty. Stock returns follow a path similar to the incense stick fumes. We call it  “Brownian motion” or “Wiener process”.

How do we characterise them?

Firstly, the value of the random variable at time t = 0, is 0.

Secondly, the value of the random variable at one time instant would be independent of its value in any previous time instant.

Thirdly, the random variable would have a normal distribution.

Finally, the random variable would follow a continuous path, not a discrete one.

Now, stock prices don’t have values = 0, at time t =0 (when they get listed). Stock prices are also known to have autocorrelations; i.e., the price at any given instant depends on one or more of the prices in previous instances. Stock prices also don’t follow a normal distribution. Still, how can it be that they follow a Brownian motion?

There’s a minor tweak that we need to do here. We shall use the daily returns of the adjusted close prices as a proxy for the increments in the stock prices. And since the price returns follow a Brownian motion, the prices themselves follow what is known as a geometric Brownian motion (GBM).

Let’s explore the GBM further using math notation. Suppose we have a stochastic process S. We say that it follows a GBM if it can be written in the following form:

$$ dS_t = \mu S_t \, dt + \sigma S_t \, dW_t $$							--------------- 2

Let’s treat S as the stock price here.

dStsimply refers to the change in the stock price over timet. Suppose the current price is $200, and it becomes $203 the next day. In this case,dSt= $3, andt= 1 day.

The Greek alphabet μ (written as mu, and pronounced as ‘mew’) represents the drift. Let’s take the Microsoft stock to understand this.

Drift and Volatility Components on Python

Note:The graphs and values obtained are as of October 18, 2024.

This last plot (Figure 4) is the crux of everything we did on Python. What’s the blue line denoting? It’s the path taken by Microsoft stock's adjusted close prices over the past ten years. And what’s the orange line for? Well, it’s just a simple straight line that connects the first day's adjusted closing price and the most recent adjusted closing price.

I’m trying to show here that irrespective of which of the two paths the stock would have taken, it would have reached the same destination today. We can see from the blue line that the stock price has increased over the past ten years. That explains the positive slope of the orange line. This is known as the “drift”. We have essentially broken down the path of the adjusted close price into two components: the drift, and the volatility. When we add these two, we get the adjusted close prices. The following plot (Figure 5) illustrates this by plotting all three together:

Stock Price = Drift Component + Volatility Component

If you need more intuition on the drift and volatility component, imagine driving from cities A to B. As much as you would like to take the imaginary path that connects both cities straight, you can’t since there will be buildings, trees, mountains, etc. You would need to take detours and turns to reach your destination.

Remember I asked you to imagine a world where the stock prices follow a deterministic path? That’s what the drift component is, after all! Can you imagine trading in a world where stock prices follow only the drift component and don’t have any volatility component?

We have taken a long detour from our main discussion (yup, we have drifted away from our drift)! Coming back to the GBM, we understood what μ is. σ is another Greek alphabet (called and pronounced as ‘sigma’) and denotes the volatility.

In equation 2, the first term is the deterministic component, and the second term is the stochastic or random or indeterministic, or noise component. Also, μ is the percentage drift, and σ is the percentage volatility.

The equation essentially tells that the change in the stock price at time t is an additive combination of the change in the stock price due to the drift component and the volatility component.

The drift component here is the product of the drift μ, the stock price at time t, and the unit change in time dt. Let’s consider dt to be one day, as mentioned earlier, for the sake of simplicity. If the stock price S is treated as a continuous random variable, ideally, we should measure dt in milli, micro, nano, or even picoseconds.

Weiner Weiner Stochastic Dinner

The volatility component is more nuanced.  We know what σ and St denote in the equation. What we don’t know yet is: $$ W_t $$

Or do we?

Remember Brownian motion (the fumes of the incense stick)? That’s what \( W_t \) denotes here. The letter W is used since this motion is called a Wiener process. I’ll (hopefully) discuss Wiener processes in depth in a subsequent blog. But for now, just know that the increments follow a normal distribution with mean = 0 and variance = t for a Wiener process.

This means if the value of \( W_t \) changes from \( W_1 \) to \( W_2 \), \( W_2\) to \( W_3 \), and so on, the changes \( W_2 \) – \( W_1 \), \( W_3 \) – \( W_2 \), and so on follow a normal distribution. The mean or expected value of this distribution is 0. This means that if we have many samples of such changes, the average of these changes would be 0 (or very close to it). What about the variance? The variance is equal to the time duration; hence, the standard deviation would be the root of this time duration.

When we say \( W_t \) follows a normal distribution with mean = 0 and variance = t, multiplying this with \( \sigma \), we can conclude that the volatility component follows a normal distribution with mean = 0, and variance = \( \sigma_t \).

Wanna see what a Weiner process looks like!

Here you go…

We simulated 15 paths that the Wiener process could have taken, over 10 days. At what frequency are the values getting updated? Every second. The shaded region is the expected standard deviation of the returns. This is how the fumes from an incense stick would look if you tilt it sideways!

Conclusion

With this, we come to the end of part I. We learned about the chain rule in classical calculus, Brownian motion, geometric Brownian motion, and how stock prices follow a geometric Brownian motion. We also developed a visual intuition for Wiener processes (Brownian motion).

In part II, we’ll cover Ito calculus, and show how to use it for developing a trading strategy. Here’s the link to the second part:Ito's Lemma Applied to Stock Trading.

You can avail of the below-mentioned freeQuantitative Finance Courseofferings on Quantra to gain insights into Python for trading, data procurement, and stock market basics:

Python for Trading

Get Market Data

Stock Market Beginner Course

If you need a small primer on the math required for trading in the financial markets, you can go through this blog article: https://blog.quantinsti.com/algorithmic-trading-maths/

If you want to get started with algorithmic trading and need knowledge on how to do so, you can learn from here:

Algorithmic Trading for Beginners

And, if you want to learn in detail the basic and advanced statistics used in algo trading, data modeling, strategy building, backtesting using Python, how to set up yourproprietary trading deskand much more, you can check out the EPAT:

Algorithmic Trading Course

References:

Main Reference:

https://research.tilburguniversity.edu/files/51558907/INTRODUCTION_TO_FINANCIAL_DERIVATIVES.pdf

Auxiliary References:

Wikipedia pages of Ito’s lemma, Brownian motion, geometric Brownian motion, quadratic variation, and, AM-GM inequality

2. EPAT lectures on statistics and options trading

All investments and trading in the stock market involve risk. Any decision to place trades in the financial markets, including trading in stock or options or other financial instruments is a personal decision that should only be made after thorough research, including a personal risk and financial assessment and the engagement of professional assistance to the extent you believe necessary. The trading strategies or related information mentioned in this article is for informational purposes only.

---

*Imported from QuantInsti Blog on 2026-04-27*
