---
title: "Heston Model: Options Pricing, Python Implementation and Parameters"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/heston-model/"
date: "2024-05-13"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Heston Model: Options Pricing, Python Implementation and Parameters

**来源**: [QuantInsti](https://blog.quantinsti.com/heston-model/)  
**日期**: 2024-05-13  
**作者**: QuantInsti

---

## 原文

Heston Model: Options Pricing, Python Implementation and Parameters

Originally written byRekhit Pachanekarand Edited byChainika Thakar

The Heston option pricing model, also known as the Heston model, aims to enhance the Black-Scholes model, which made unrealistic assumptions. A key assumption was that volatility stayed the same throughout an option's lifespan.

However, in reality, volatility tends to vary and is seldom constant. Steven Heston developed a mathematical model where volatility is unpredictable and follows a random pattern. Moreover, Heston's model offers a straightforward solution, streamlining the process and gaining wider acceptance in the financial community.

Whether you're a financial analyst, a quantitative researcher, or someone interested in learning about the sophisticated financial models for trading related or work related purposes, this blog will help you grasp the fundamentals of the Heston model. Since the Heston model is an advanced options pricing concept, readers who are new to options are encouraged to first exploreoptions trading basicsbefore proceeding. You'll learn about its theoretical underpinnings and gain practical insights into the Heston model and its applications in option pricing.

Let's proceed to explore the topics covered in this blog.

What is the Heston model?

Heston model parameters

Essentials of Heston model while pricing options

Steps for pricing European options using Heston model

Heston model implementation for pricing options using Python

Heston model vs Black-Scholes model

Assumptions while using the Heston model

Benefits of using the Heston model

Limitations of using the Heston model

Extensions of the Heston model

What is the Heston model?

The Heston model, introduced by Steven Heston in 1993, is a mathematical model used in financial mathematics to price options. It is an extension of theBlack-Scholes modeland is widely used to value options where the underlying asset's volatility is not constant but follows a stochastic process.

Volatility represents the magnitude of upward and downward movements in a security over a given period. Technically, it is measured as the standard deviation of the annualised returns over that period, or simply as the square root of the variance of the returns.

In the Heston model, both the underlying asset's price and its volatility are assumed to follow stochastic differential equations (SDEs). The model assumes that volatility follows a mean-reverting process, which means it tends to revert to a long-term average over time.

This feature of the model allows it to capture the volatility smile observed in the market, where options with different strike prices but the same maturity may have different implied volatilities. The Heston model has become a standard model forpricing optionsin both equity and foreign exchange markets due to its ability to capture the dynamics of asset prices and the volatility surface accurately.

Let's first explore why it's important not to treat volatility as a constant. Imagine you maintain volatility as a constant value. Now, if you were to plot a graph with strike prices on the x-axis and the implied volatility of a group of options on the y-axis, you would observe a curved line. This phenomenon is known as thevolatility smile.

The reason behind thevolatility smileis that implied volatility tends to be higher for deep out-of-the-money options and generally decreases as we move towards in-the-money or at-the-money options. Interestingly, the volatility smile was considered rare before the 1987 crash. However, after the crash, traders realised that out-of-the-money options, although rare, could occur.

Here is an example of how the graph might look:

According to the Black-Scholes model, this line should have been flat. However, to ensure that option prices better reflect real-world conditions, the Heston model introduced a stochastic volatility model.⁽¹⁾

In the Heston model, two functions are considered:

Brownian motion, representing the underlying asset price

The variance (represents volatility)

Going forward, we will understand the general parameters taken into consideration with the Heston model.

Heston model parameters

The Heston model has several parameters that describe the dynamics of the underlying asset's price and volatility.

The main parameters of the Heston model are:

Initial asset price (S0):The current price of the underlying asset.

Mean reversion rate (κ):The speed at which the volatility reverts to its long-term average.

Long-term average volatility (θ):The long-term average volatility level to which the volatility reverts.

Volatility of volatility (ν):The volatility of the volatility process. It determines the amplitude of volatility fluctuations.

Correlation between asset price and volatility (ρ):The correlation between the asset price and its volatility process. This parameter determines how changes in the asset price affect its volatility.

Risk-free interest rate (r):The risk-free interest rate.

Time to maturity (T):The time until the option's expiration.

Strike price (K):The price at which the option holder has the right to buy or sell the underlying asset.

These parameters are used to define the stochastic differential equations governing the dynamics of the asset price and its volatility in the Heston model.

Let us now see the essentials of the Heston model while pricing the options.

Essentials of Heston model while pricing options

The Heston Model is a mathematical model used to price options. The stochastic differential equations (SDEs) are the essential concepts for the Heston Model. Below you can see both the equations.

The first equation representsStock Price Dynamics, and is as follows:

dS(t) = µS(t)dt + √v(t)S(t)dW₁(t)

This equation describes thelogarithmic price movementof the underlying asset. Here's a breakdown of the terms:

dS(t): Infinitesimal change in the price of the underlying asset at time t.

µ: Coefficient, representing the expected return of the asset per unit time.

S(t): Price of the underlying asset at time t.

dt: Infinitesimal time change.

√v(t): Volatility factor, representing the standard deviation of the asset's return per unit time. This term incorporates the concept of stochastic volatility, meaning the volatility can fluctuate over time.

dW₁(t): Infinitesimal Wiener process (Brownian motion), representing a random shock or innovation term.

This equation captures the price movement of the asset, considering both the expected return and random fluctuations influenced by volatility.

It is like a mini-formula that captures how the price of an asset changes over brief moments in time (represented by dt). It considers two main factors:

Expected Return (µS(t)dt):This reflects the average amount the asset price is expected to increase over that tiny time period. It predicts the direction of the price movement, considering factors like overall market trends and the asset's historical performance.

Random Fluctuations (√v(t)S(t)dW₁(t)):This part acknowledges that asset prices don't just smoothly follow the expected return. There are random ups and downs due to various unpredictable events and market noise. This term incorporates the asset's current price (S(t)), its volatility (v(t)), and a random shock element (dW₁(t)) to account for these unpredictable fluctuations.

By putting these two factors together, this equation allows us to model the price movement of the asset over time considering both the expected trend and the random fluctuations along the way.

2. The second equation representsVolatility Dynamicsand is as follows:

dv(t) = κ(θ - v(t))dt + συ(t)dW2(t)

Here's a breakdown of the terms:

dv(t): Infinitesimal change in the volatility of the asset at time t.

κ: Mean reversion rate, representing the speed at which volatility tends to move back towards its long-term average (θ).

θ: Long-term average volatility.

v(t): Volatility of the asset at time t.

dt: Infinitesimal time change.

σ: Volatility of volatility, representing the standard deviation of the volatility process.

dW2(t): Infinitesimal Wiener process (Brownian motion), independent of the first Wiener process (dW₁(t)), representing a random shock affecting the volatility.

This equation models the volatility itself as a separate process with its own mean reversion and random fluctuations.

Volatility, representing price fluctuations, isn't constant and changes over time. Usingmean reversion strategies, this model helps traders understand and predict these shifts in volatility, making it a valuable tool for market analysis.

Here's what each part signifies:

Mean Reversion (κ(θ - v(t))dt):Imagine volatility as a ball tied with a rope to a certain height (θ). This term represents the strength of that rope. The higher the κ (mean reversion rate), the stronger the pull, meaning volatility tends to get dragged back towards its long-term average (θ) if it strays too far.

Random Shocks (σv(t)dW2(t)):Just like asset prices, volatility can also experience unexpected fluctuations. This term, with its Greek letters, considers the volatility's current level (v(t)) and another random shock factor (dW2(t)) to account for these unpredictable changes.

In essence, this equation allows us to model how volatility itself might change over time. It considers the tendency to revert to a long-term average but also acknowledges the possibility of random ups and downs in volatility.

Both these equations are typically used within the Heston Model. By solving these equations numerically, we can simulate the potential price paths of the underlying asset and its volatility, allowing for more accurate option valuation compared to models with constant volatility.

Python implementation to visualise stock price dynamics and volatility dynamics

Let us see the Python code that will generate two plots:

Stock Price Dynamics:How the stock price changes over time.

Volatility Dynamics:How the volatility of the stock changes over time.

Output:

Output:

Ahead, we will see the steps of the Heston model for pricing European options.

Steps for pricing European options using Heston model

Below are the steps of options pricing using the Heston model. We are taking European call and put options in this example.

Step 1: Define model parameters

Step 2: Calculate the characteristic function

Step 3: Calculate the option price

Step 1: Define model parameters

Define the parameters of the Heston model that we discussed above.

Step 2: Calculate the characteristic function

Use the Heston model characteristic function formula to calculate the characteristic function of the Heston model. The characteristic function is a concept that is widely used in option pricing models like the Heston model.

In the context of the Heston model, the characteristic function is a mathematical function that fully describes the joint distribution of the underlying asset price and its stochastic volatility at expiration.

The characteristic function for the Heston model is given by:

Step 3: Calculate the option price

Use Fourier inversion to compute the option price. Fourier inversion is a mathematical technique used to compute option prices in models like the Heston model. In the context of the Heston model, the characteristic function is used to price options via Fourier inversion.

Fourier inversion involves integrating the characteristic function over a range of frequencies (or a range of values for the integration variable u) to obtain the option price.

For a European call option, the option price can be expressed as:

Similarly, for a European put option, the option price can be expressed as:

where:

Now we will see the Python implementation for pricing options using the Heston model.

Heston model implementation for pricing options using Python

Below is the Python implementation for pricing options using the Heston model. Here are the steps involved in the same:⁽¹⁾

Step 1: Import libraries

Step 2: Define model parameters

Step 3: Define functions

Step 4: Calculate the call and put option prices

Step 1: Import libraries

Step 2: Define model parameters

Step 3: Define functions

Step 4: Calculate the call and put option prices

Output:

European Call Option Price: 27.63
European Put Option Price: 15.06

Let us move to learning about the difference between the Heston model and the Black-Scholes model now.

Heston model vs Black-Scholes model

Let us first see how the Heston model differs from the Black-Scholes model since Heston is an improvement of the Black-Scholes model.⁽²⁾

Here is a clear distinction in the table below mentioning characteristics of each model.

Aspect

Black-Scholes Model

Heston Model

Purpose

Assumes constant volatility and log-normal distribution of asset returns.

Explicitly models stochastic volatility, allowing for changes in volatility over time.

Volatility Dynamics

There is a fixed volatility throughout.

It models stochastic volatility as a mean-reverting process.

Parameters

Considers factors such as current price, time, interest rate, and a fixed volatility.

Needs more information such as how volatile markets usually are, how fast they go back to normal, and how related price changes are to volatility changes

Closed-form Solution

Provides closed-form solution.

Doesn't provide a closed-form solution.

Flexibility

Only works for bothbasic optionsand exotic options. Although, it may require extensions or modifications.

Can handle many types of options, even theexotic optionssuch as barrier, binary etc.

Adjusting or calibrating difficulty

Calibrating the Black-Scholes model typically involves straightforward adjustments to its input parameters.

Refining the Heston model to accurately reflect real market dynamics requires a more intricate process, often necessitating iterative adjustments and computational analysis to align the model's parameters with observed market data.

Let us now move forward and find out the various assumptions of the Heston model.

Assumptions while using the Heston model

When using the Heston model, several assumptions are made:

Continuous trading:Trading occurs continuously, and the market is frictionless.

No dividends:The underlying asset does not pay any dividends during the option's life.

No transaction costs:There are no transaction costs associated with trading the option or the underlying asset.

No arbitrage opportunities:There are no risk-free arbitrage opportunities in the market.

Constant risk-free rate:The risk-free interest rate is constant and known.

Constant parameters:The parameters of the model (such as mean reversion rate, long-term average volatility, volatility of volatility, and correlation) are assumed to be constant over time.

However, it's important to note that in reality, some of these assumptions may not hold true, and adjustments may be necessary when applying the model to real-world situations.

Let us find out the benefits of using the Heston model next.

Benefits of using the Heston model

Using the Heston model offers several benefits:

Captures volatility smile:The Heston model can capture the volatility smile observed in the market, where options with different strike prices but the same maturity may have different implied volatilities. This makes it more accurate in pricing options compared to the Black-Scholes model.

Stochastic volatility:Unlike the Black-Scholes model, which assumes constant volatility, the Heston model incorporates stochastic volatility. It allows volatility to fluctuate over time, reflecting the reality of financial markets more accurately.

Mean-reverting volatility:The Heston model assumes that volatility reverts to a long-term average over time, which is consistent with empirical observations of market behaviour.

Flexibility:The Heston model is flexible and can be calibrated to fit different market conditions. This allows for more accurate pricing of a wide range of financial derivatives, including options on equities, indices, currencies, and interest rates.

Realism:By incorporating stochastic volatility, the Heston model better reflects the complex dynamics of financial markets, making it more suitable for pricing options in real-world conditions.

Market standard:The Heston model has become one of the standard models for option pricing and risk management in both equity and foreign exchange markets, widely used by practitioners in the financial industry.

After seeing the benefits that the Heston model’s use offers, we will now move to the limitations of the same.

Limitations of using the Heston model

The following can be considered as the limitations of the Heston model:

One of the main limitations of the Heston model is the presence of the parameters in the model which have to be calibrated carefully to provide a decent estimate of the option prices.

It is found that the Heston model suffers when it comes to predicting the option prices for short-term options as the model fails to capture the highimplied volatility.

The Heston model is comparatively more complex than the Black-Scholes model which deters traders from using this option.

The extensions of the Heston model come next.

Extensions of the Heston model

Several extensions of the Heston model have been proposed to address its limitations and to better capture the complexities of financial markets. Some of the notable extensions include:

Stochastic interest rates:Extending the Heston model to incorporate stochastic interest rates allows for a more accurate representation of the term structure of interest rates and the correlation between interest rates and asset prices.⁽³⁾

Jump diffusion:Adding jumps to the Heston model captures sudden, discontinuous movements in asset prices. This extension is particularly useful for modelling extreme events such as market crashes.

Time-dependent parameters:Allowing the model parameters to vary over time can improve its ability to capture changes in market conditions and the term structure of volatility.⁽⁴⁾

Multiple factors:Extending the Heston model to include multiple sources of volatility allows for a more flexible and realistic representation of market dynamics, particularly in markets with complex dependencies between different asset classes.⁽⁵⁾

Model calibration:Developing more sophisticated calibration techniques to estimate the model parameters from market data can improve the model's ability to fit observed option prices accurately.⁽⁶⁾

These extensions of the Heston model address some of its limitations and make it a more powerful tool for pricing and hedging a wide range of financial derivatives in real-world market conditions.

Conclusion

The Heston model, an extension of the Black-Scholes model, revolutionised options pricing by incorporating stochastic volatility, thus addressing the limitations of its predecessor. By allowing volatility to fluctuate over time, the Heston model accurately captures the volatility smile observed in financial markets. Steven Heston's mathematical model provides a closed-form solution, simplifying the pricing process and gaining widespread acceptance.

With this comprehensive guide we explored the intricacies of the Heston model, from its formula and assumptions to its limitations and practical implementation. Through Python examples, we gained a deeper understanding of the model's application in options pricing.

Despite its benefits, the Heston model requires careful parameter calibration and may struggle with short-term option pricing. However, extensions such as stochastic interest rates and jump diffusion address these limitations, making the Heston model a powerful tool for pricing and hedging financial derivatives in real-world market conditions.

Apart from the Heston Model, other option pricing models are BSM and Derman-Kani Model, and you may explore them to understand them better in our comprehensive learning track that will help you learn aboutquantitative trading in the futures and options markets. Grasp this opportunity to learn volatility forecasting,options backtesting, risk management, option pricing models and greeks as well as various trading strategies in a hands-on manner. Let this be your guide ahead. Enroll now!

File in the download

Heston model – SDE and options pricing - Python notebook

Login to Download

Note: The original post has been revamped on 21stFebruary 2024 for recentness, and accuracy.

Disclaimer: All investments and trading in the stock market involve risk. Any decision to place trades in the financial markets, including trading in stock or options or other financial instruments is a personal decision that should only be made after thorough research, including a personal risk and financial assessment and the engagement of professional assistance to the extent you believe necessary. The trading strategies or related information mentioned in this article is for informational purposes only.

---

*Imported from QuantInsti Blog on 2026-04-27*
