---
title: "Black Scholes Model: Formula, Limitations, Python Implementation"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/black-scholes-model/"
date: "2020-04-07"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Black Scholes Model: Formula, Limitations, Python Implementation

**来源**: [QuantInsti](https://blog.quantinsti.com/black-scholes-model/)  
**日期**: 2020-04-07  
**作者**: QuantInsti

---

## 原文

Black Scholes Model: Formula, Limitations, Python Implementation

ByRekhit Pachanekar

The Black Scholes Model! There are a few models in this world which make the world stand up and take notice, and this is one of them. If I have to explain it in simple terms, the Black Scholes model helps us in finding the price of an option, a European option to be precise. If you want to understand or refresh your knowledge on Options, check out the basics of Options article. But why is it so important to know the price of an option?

Let’s take an example here. As of March 21, Tesla’s share price was $427.53. Now if we check the options data on Yahoo Finance, you will find a lot of options being traded at various strike prices. Let’s zoom in on three of them for now. Note that these options are going to expire on March 27, 2020.

Now, there are three different strike prices, $300, $305, $310, with options bought at $149, $128, $123.

You must have backtested a certain strategy to predict the stock price of Tesla on March, so which price you should buy an option to maximise your gains.

This is exactly where the Black-Scholes model helps you. Fischer Black and Myron Scholes had built the foundation for this model which was later worked on by Robert Merton to give us the equation which is popular all over the world now.

Let us go through the points covered in this article first:

Assumptions of the Black Scholes Model

Black Scholes formula

Black Scholes in Python

Limitations

Variants to overcome BSM

Assumptions of the Black Scholes Model

While the Black Scholes model can be reduced to just one equation, there were a lot of sacrifices made to make it simple. Some have been made to reduce the complexity, for example, assuming that the stock does not pay dividends. This helps to reduce the calculations in finding the optimal price of the option.

But bear in mind that this doesn’t mean that it is a limitation and will exclude all stocks which paid out dividends for the time period we are calculating the option prices. One can always factor in the dividends after we have computed the option prices using the Black Scholes Model.

Thus, let’s go through the assumptions now.

The constant risk-free rate of return

One of the factors affecting the option prices is the risk-free rate return. The assumption is that the risk-free return will remain constant from the point we purchase the Option to its expiry date. It is also assumed that you can borrow or lend with this rate easily. The reason this is important is that if you found that all things remaining same, if the options return is equal to the risk-free rate, then people would go for the risk-free asset and not the Option.

Log return of risky asset’s price is a random walk

Here, we assume that the markets are efficient and the markets have a drift which is increasing and follow the geometric Brownian motion. This shows that while we cannot exactly predict the price of the underlying asset, we can calculate its expected return.

Dividends are not taken into account

We assume that the stock doesn’t pay any dividends and hence its value is dependent on its price only.

No arbitrage opportunities

If we see that there is an arbitrage opportunity when it comes to the option and the underlying asset, we would immediately use that to our advantage and won’t have to worry about the option price. Hence, we assume that there are no arbitrage opportunities.

No limit on buying and selling of the underlying risky asset

We assume that we can buy or sell any amount of the underlying asset to maximise our gains. In this manner, we don’t have to worry about an upper limit on the number of transactions we are allowed.

No transactions costs

Quite simply, this model doesn’t take into account the brokerage, commissions, borrow charges or any other transaction costs we might incur while trading Options. Thus, we have to be careful of accounting for them when we are evaluating different options.

Great! Now that we have gone through the assumptions of the model, let’s get to the heart of the matter, i.e. the Black-Scholes equation.

Black Scholes formula

Before we state the formula, let’s try to gain an understanding of the factors which could affect the Options price. Now, thanks to the assumptions of the Black Scholes model, we don’t have to worry about the intricate details like stock dividends and fluctuating interest rates etc. while deriving the options price. But what can possibly impact the options price?

The first is obviously the underlying asset’s price. Moving further, we would also like to know what happens if the price increases or increases until we reach the expiration date of the Option.

This is where the expected rate of return comes into the picture.

Along with this, we also have to consider the time value of money. In simple terms, $100 right now is more valuable to $100 in one year, because you can put this $100 in a bank and get some interest after a year.

Let’s expand on this. Suppose you can get a 4% rate of interest in a bank. Thus, after one year, it will be ($100) + (4/100)*(100) = $104. You can put that in the form of a formula as (Your amount)*(1 + i%). Now, if you think that you are going to get $104 in one year, then you just have to divide it by (1+i%) to get its present value. We call this the discounting factor. The ‘i’, in this case, is the interest you could get.

For the sake of this article, we will not go into the nitty-gritty of it but when it comes to the Black Scholes Model, the discounting factor is (e-rT).

All right! So far we have realised that the option price can be affected by the underlying asset price. The time to expiry as well as the Exercise price, i.e. the Strike price.

We also have to take into account the volatility of the underlying asset. Why is that important?

Let’s say that there are two stocks, A and B. If you are buying a European call Option, you would be concerned about how far the price can go at the time of expiry, either high or lower than the strike price. This can be deduced by finding the volatility i.e. the standard deviation of log normal returns.

Let us list them down now.

S = Stock price

N() = Cumulative Standard normal distribution

K = Strike price of the option

t = time till the option expires

r = risk-free rate of interest

e= exponential term ie 2.7183

C= option price

For the sake of simplicity, we are considering the underlying asset to be a stock and the stock option is a European Call option. The reason we are using a European Call Option is that this option can only be exercised at the time of expiry and not before.

Now we can move to the actual formula which looks like this.

Now what is d1and d2?Let me lay down the values before I try to explain it. Thus,$$d_1 = \frac{ln \frac{S}{K}+(r + \frac{s^2}{2})t}{s {\sqrt t}}$$and$$d_1 = \frac{ln \frac{S}{K}+(r - \frac{s^2}{2})t}{s {\sqrt t}}$$Where, s = standard deviation of log returns andln = natural logarithmWhile the actual derivation of these terms is somewhat lengthy and entails a deep dive into statistics, we can see that we are using the same terms and more importantly we are taking the natural log of the ratio of the stock price and the exercise price.Coming back to the main formula, we can actually divide it into two parts:The first part, S*N(d1) is what you get ie the underlying stock if we decide to exercise our right to buy the stock.The second part, K*e(-rt)*N(d2) is what you have to pay to receive that option. Thus the exercise price, i.e. K is multiplied by the discounting factor e(-rt) as this is the amount which we could have invested in a riskless asset instead of buying the option.The cumulative standard normal distribution function i.e. N() gives us the probability values for the expected values. Think of it as a probability value between 0 and 1. Thus you would now understand why we subtract the second part of the equation from the first to get the Option price.That’s all there is to the option pricing model. You can simply put the values in the equation and find the Option price. And depending on differentoptions trading strategies, you can create a risk-neutral portfolio for yourself.All right, hold on. Sure, we can get all the values of the variables, but what about volatility. How do you gauge the volatility of the underlying asset?Well, the first thought that came to your mind is correct, we look up the historical prices, calculate their log normal returns and easily find the volatility. Then we assume that historical volatility will be more or less similar to the future volatility and thus calculate the options price on it.But, there is another way to go about it, which seems like a shortcut. You see, if you check the options data for any stock, you will find a dozen of them at various strike prices, option prices etc. Now, we can use the option price which the market believes is the right price and use it as our “C” in the Black-Scholes equation to find the volatility. This is called the Implied volatility. You can check out thisarticlewhich goes in-depth about the concept.Awesome! We have understood how the Black Scholes Equation works for a European Call Option. Now let’s see if we can implement this in Python.Black Scholes in PythonIf you want to find the current options data using python, you can use yahoo finance module to extract the relevantoptions datafor a company.import yfinance as yf # Import yahoo finance module
tesla = yf.Ticker("TSLA") # Passing Tesla Inc. ticker

opt = tesla.option_chain('2022-06-17') #retreiving option chains data for 17 June 2022To see the option calls, you will input the following code:opt.callsSimilarly for put options, you use the following code:opt.putsNow, we could probably code a few lines to implement the formula in Python, but the great thing about Python is its extensive use of libraries. Thus, we have the python library,mibianwhich makes it extremely easy to deduce the option prices.The python code is simply:BS([underlyingPrice, strikePrice, interestRate, daysToExpiration], volatility=x, callPrice=y, putPrice=z)The syntax for BS function with the input as volatility along with the list storing an underlying price, strike price, interest rate and days to expiration:c = mibian.BS([427.53, 300, 0.25, 4], volatility=60)Here, we have taken our example of Tesla and input the Underlying price as $427.53, the exercise or Strike price as $300, Risk-free interest rate as 0.25% and days until expiration as 4.We have put the volatility figure as 60%.Now, if we need to find the Option call price of Tesla, we will just write the following:c.callPriceThe output is:127.53821909748126What do you think? Is the Black Scholes model right? Why don’t you try finding the options call price for another stock and leave the details in the comments.All right! We have looked at the formula as well as its implementation in Python. Now we move on to the next topic, i.e. the limitations of the model.LimitationsBefore we list down the limitations of the Black Scholes Model, we have to understand that the creators of this model had to sacrifice a few things before they could build a working model. Having said that, let us list down the limitations:Volatility and the risk-free rate of returns are assumed to be constant even though it is dynamic in reality.The stock price is assumed to be a random walk and thus large price moves due to certain factors like earnings reports, mergers and acquisitions are not incorporated in the model.In case of stocks which pay dividends during the period we have calculated the options price, the model doesn’t take the dividend into account, thus not correctly pricing the option.While the pricing of in the money and out of the money options are accurate, it tends to deviate sharply when it comes to pricing deep out of the money options.While other factors are directly observed and calculated, volatility has to be estimated and thus, could lead to different option prices.Ok, we went through the limitations of the model, but are there ways to overcome these? OR maybe a more efficient model. Let’s see that in the next section.Variants to overcome BSMOne of the better alternatives to the Black Scholes model is the Heston model of option pricing. This model assumes that volatility is not constant but arbitrary. It also allows for volatility to be mean reverting, which is closer to the real scenario than the Black Scholes model.While Heston's model deserves an article to itself, I will list the equation below.$$dS = μS dt +{\sqrt v_t} S * dW_t^S$$Here,Vtis the instantaneous variance.And,$$dv_t  = k(θ-v_t ) dt +ξ{\sqrt v_t}  * dW_t^v$$Here,ξ is the volatility of volatilityk is the rate at which vt returns to 0θ is the long run price varianceW is the Weiner processes which is supposed to be continuous random walksThis does look daunting but it is more efficient than the Black Scholes pricing model.All right. We looked into one of the alternatives of the Black Scholes Model.ConclusionThe Black Scholes model was a turning point for the options world who finally had a mathematical foundation to build their options portfolios. The Black Scholes model also gave rise to a number of option hedging strategies which are still being implemented today.In this article, we covered the significance as well as the formula of the black Scholes model. We have also gone ahead and looked at the python code for the Black Scholes model and how to use it to calculate the European option call price. You can try out your own option trading strategies by starting theoptions trading learning trackon Quantra to start trading.File in the download:Black Scholes Model Formula, Limitations, Python Implementation - Python Notebook

Let me lay down the values before I try to explain it. Thus,

Where, s = standard deviation of log returns and

ln = natural logarithm

While the actual derivation of these terms is somewhat lengthy and entails a deep dive into statistics, we can see that we are using the same terms and more importantly we are taking the natural log of the ratio of the stock price and the exercise price.

Coming back to the main formula, we can actually divide it into two parts:

The first part, S*N(d1) is what you get ie the underlying stock if we decide to exercise our right to buy the stock.

The second part, K*e(-rt)*N(d2) is what you have to pay to receive that option. Thus the exercise price, i.e. K is multiplied by the discounting factor e(-rt) as this is the amount which we could have invested in a riskless asset instead of buying the option.

The cumulative standard normal distribution function i.e. N() gives us the probability values for the expected values. Think of it as a probability value between 0 and 1. Thus you would now understand why we subtract the second part of the equation from the first to get the Option price.

That’s all there is to the option pricing model. You can simply put the values in the equation and find the Option price. And depending on differentoptions trading strategies, you can create a risk-neutral portfolio for yourself.

All right, hold on. Sure, we can get all the values of the variables, but what about volatility. How do you gauge the volatility of the underlying asset?

Well, the first thought that came to your mind is correct, we look up the historical prices, calculate their log normal returns and easily find the volatility. Then we assume that historical volatility will be more or less similar to the future volatility and thus calculate the options price on it.

But, there is another way to go about it, which seems like a shortcut. You see, if you check the options data for any stock, you will find a dozen of them at various strike prices, option prices etc. Now, we can use the option price which the market believes is the right price and use it as our “C” in the Black-Scholes equation to find the volatility. This is called the Implied volatility. You can check out thisarticlewhich goes in-depth about the concept.

Awesome! We have understood how the Black Scholes Equation works for a European Call Option. Now let’s see if we can implement this in Python.

Black Scholes in Python

If you want to find the current options data using python, you can use yahoo finance module to extract the relevantoptions datafor a company.

import yfinance as yf # Import yahoo finance module
tesla = yf.Ticker("TSLA") # Passing Tesla Inc. ticker

opt = tesla.option_chain('2022-06-17') #retreiving option chains data for 17 June 2022

To see the option calls, you will input the following code:

opt.calls

Similarly for put options, you use the following code:

opt.puts

Now, we could probably code a few lines to implement the formula in Python, but the great thing about Python is its extensive use of libraries. Thus, we have the python library,mibianwhich makes it extremely easy to deduce the option prices.

The python code is simply:

BS([underlyingPrice, strikePrice, interestRate, daysToExpiration], volatility=x, callPrice=y, putPrice=z)

The syntax for BS function with the input as volatility along with the list storing an underlying price, strike price, interest rate and days to expiration:

c = mibian.BS([427.53, 300, 0.25, 4], volatility=60)

Here, we have taken our example of Tesla and input the Underlying price as $427.53, the exercise or Strike price as $300, Risk-free interest rate as 0.25% and days until expiration as 4.

We have put the volatility figure as 60%.

Now, if we need to find the Option call price of Tesla, we will just write the following:

c.callPrice

The output is:

127.53821909748126

What do you think? Is the Black Scholes model right? Why don’t you try finding the options call price for another stock and leave the details in the comments.

All right! We have looked at the formula as well as its implementation in Python. Now we move on to the next topic, i.e. the limitations of the model.

Limitations

Before we list down the limitations of the Black Scholes Model, we have to understand that the creators of this model had to sacrifice a few things before they could build a working model. Having said that, let us list down the limitations:

Volatility and the risk-free rate of returns are assumed to be constant even though it is dynamic in reality.

The stock price is assumed to be a random walk and thus large price moves due to certain factors like earnings reports, mergers and acquisitions are not incorporated in the model.

In case of stocks which pay dividends during the period we have calculated the options price, the model doesn’t take the dividend into account, thus not correctly pricing the option.

While the pricing of in the money and out of the money options are accurate, it tends to deviate sharply when it comes to pricing deep out of the money options.

While other factors are directly observed and calculated, volatility has to be estimated and thus, could lead to different option prices.

Ok, we went through the limitations of the model, but are there ways to overcome these? OR maybe a more efficient model. Let’s see that in the next section.

Variants to overcome BSM

One of the better alternatives to the Black Scholes model is the Heston model of option pricing. This model assumes that volatility is not constant but arbitrary. It also allows for volatility to be mean reverting, which is closer to the real scenario than the Black Scholes model.

While Heston's model deserves an article to itself, I will list the equation below.

Vtis the instantaneous variance.

ξ is the volatility of volatility

k is the rate at which vt returns to 0

θ is the long run price variance

W is the Weiner processes which is supposed to be continuous random walks

This does look daunting but it is more efficient than the Black Scholes pricing model.

All right. We looked into one of the alternatives of the Black Scholes Model.

Conclusion

The Black Scholes model was a turning point for the options world who finally had a mathematical foundation to build their options portfolios. The Black Scholes model also gave rise to a number of option hedging strategies which are still being implemented today.

In this article, we covered the significance as well as the formula of the black Scholes model. We have also gone ahead and looked at the python code for the Black Scholes model and how to use it to calculate the European option call price. You can try out your own option trading strategies by starting theoptions trading learning trackon Quantra to start trading.

File in the download:

Black Scholes Model Formula, Limitations, Python Implementation - Python Notebook

---

*Imported from QuantInsti Blog on 2026-04-27*
