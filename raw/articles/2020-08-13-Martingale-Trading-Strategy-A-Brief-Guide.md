---
title: "Martingale Trading Strategy: A Brief Guide"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/martingale/"
date: "2020-08-13"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Martingale Trading Strategy: A Brief Guide

**来源**: [QuantInsti](https://blog.quantinsti.com/martingale/)  
**日期**: 2020-08-13  
**作者**: QuantInsti

---

## 原文

Martingale Trading Strategy: A Brief Guide

ByChamundeswari Koppisetti

We frequently hear about martingale strategies in casino games where one doubles their bet size after every loss. Can these martingale strategies be applied to trading and increase a trader’s gain?

In this blog, we will be focusing onMartingaleand its application in trading strategies by going through the following topics.

What is martingale?

How does martingale work?

Conditional expectation in martingale

Martingale trading strategy

What is an anti-martingale?

Martingale vs anti-martingale trading strategy in python

What is martingale?

A random variable is an unknown value or a function which takes a particular value for each possible trial. It can be either discrete or continuous. We consider discrete random variable below to explain martingale.

Martingale is a sequence of random variables M1, M2, M3… Mn, where

E [Mn+1|Mn] = Mn, n -> 0, 1, …, n+1                        🡪 (1)

And E [|Mn+1|] < ∞,

Which is read as expectation of Mn+1 given the value of Mn is equal to Mn, i.e. expectation remains constant

For a random variable which takes different values x1, x2, x3 with respective probabilities of p1, p2 and p3, the expectation is calculated as:

E[M] = x1 * p1 + x2 * p2 + x3 * p3,
 In simpler terms, expectation is same as the arithmetic mean.

Note: Martingale is always defined with respect to some information sets, and some probability measure. If the information sets or the probability associated to the process are changed, the process might not be a martingale anymore.

How does martingale work?

Consider a simple game, where you toss a fair coin and win a dollar if the outcome is head and lose the dollar if it’s a tail.

In this game, the probability for either head or tail is always half. So, the average value of win is equal to ½(1) + ½(-1) =0, which implies that you cannot systematically earn any additional money by playing a number of rounds of the game (although random gains or losses is still possible).

Hence, the above satisfies martingale property which says that in any particular round your total earnings are expected to stay the same regardless of the outcomes of the previous rounds.

Conditional expectation in martingale

The expression on left hand side of equation (1) in martingale definition is called ‘conditional expectation’. Conditional expectation (also called the conditional mean) is simply the average, calculated after a set of prior conditions has happened.

Conditional expectation of a random variable X with respect variable Z is defined as a (new) random variable Y = E(X|Z)

Martingale trading strategy

Martingale trading strategy is to double your exposure or investment size on losing trades. As your expected long-term return is still the same, (lose when the price goes down and gain when the price goes up), this strategy can be implemented by buying in dips when the price goes down and lowering your average entry price. Hence, even after a series of losing trades, if a winning trade happens, it regains all the losses including initial trade amount as it results in a profit of 2^p=∑ 2^p-1+1 .

Pros and Cons of Martingale:One of the advantages is, as the trader doubles investment size after every losing trade, the strategy helps to recoup the losses and generate profits improving the net earnings. Whereas the main disadvantage is that if you are increasing the investment size without stop loss limits.

Note:You can lose your entire capital if the company goes bankrupt or result in an uncoverable drawdown requiring additional capital if the odds do not improve in the long run and you continually lose.

What is an anti-martingale?

In an anti-martingale strategy, one doubles the investment size when the prices move in a profitable direction and halve the investment size when there is a loss. This is done with the hope that stocks will continue to rise in a trend, which works inmomentumdriven markets.

Pros and Cons of Anti - Martingale:Major advantage of Anti-Martingale system is the minimal risk during unfavourable conditions, as the trade volume is not increased during losses. Despite advantages, anti-martingale also doesn't result in profits if there are extended losing trades. Hence, entry signals should be computed accurately in order that losses don't cover the profits gained.

In the next section, we will build the Martingale and Anti-martingale strategy in python. If you don’t know where to start with respect to python, you can try our Pythoncourseor the pythonhandbook.

Martingale vs anti-martingale trading strategy in python

We have used the Apple (AAPL) Adjusted Close price data for over 6 months. This data was pulled from the Yahoo finance website and stored in a csv file. To know how to download financial data, you can go through thisblog.

Read the stock data

2019 Half yearly (Jul to Dec) Adjusted Close price data for AAPL has been downloaded

Simple Martingale strategy

Martingale trading strategy is to double your trade size on losing trades.

We start with one stock of AAPL and double the trade volume or quantity on losing trades. Strategy is built considering winning trade as a 2% increase and losing trade as a 2% decrease from the previous close price.

Note: We can notice from the above graph that the trade volume or quantity increases exponentially, and cumulative returns increased. But in this case, we might run out of capital to double theposition, which leads to bankruptcy.

Simple Anti-martingale strategy

Anti-martingale strategy is to double the trade size on winning trades and halve the size on losing trades.

Similar to the above martingale strategy, we start with one stock of AAPL and double the trade volume or quantity on winning trades and half the trade volume or quantity on losing trades. The strategy is built considering winning trade as 2% increase and losing trade as a 2% decrease from the previous close price.

Standard martingale lead to highly variable outcomes in the long run, as it can encounter exponentially increasing losses. Whereas anti martingale return distribution is significantly flatter, with lower variance as it decreases exposure on losses, and increases it on profits. With this in mind, we see that majority of successful traders tend to follow anti martingale strategies as they are considered to be less risky increasing investment size during a winning streak than during a losing streak compared to martingale strategy.

You can check out the learning track foradvanced Algorithmic Trading Strategiesdesigned for traders who want to improve their existing strategies.

Conclusion

In this blog, we first understood the intuitive meaning of martingale by visiting the concept of conditional expectation. Next, we have learnt the types of martingale strategies. In martingale trading strategy, trade size or quantity is doubled on losing trades with the expectation of upcoming profitable trades to cover the losses and generate profits. In an anti-martingale trading strategy, trade size or quantity is halved on losing trades (protecting the downside), and doubled on profitable trades. We have also understood the market conditions which may be suitable for either of the strategy. Finally, we have implemented both, the martingale and anti-martingaletrading strategies. You can learn different types of quantitative strategies and models by enrolling for our learning track onalgorithmic trading for everyone.

Download Data File

Apple six-month earnings

Martingale code

Disclaimer: All data and information provided in this article are for informational purposes only. QuantInsti® makes no representations as to accuracy, completeness, currentness, suitability, or validity of any information in this article and will not be liable for any errors, omissions, or delays in this information or any losses, injuries, or damages arising from its display or use. All information is provided on an as-is basis.

---

*Imported from QuantInsti Blog on 2026-04-27*
