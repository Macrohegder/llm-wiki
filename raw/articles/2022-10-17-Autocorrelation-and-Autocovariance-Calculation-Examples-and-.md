---
title: "Autocorrelation and Autocovariance: Calculation, Examples, and More"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/autocorrelation-autocovariance/"
date: "2022-10-17"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Autocorrelation and Autocovariance: Calculation, Examples, and More

**来源**: [QuantInsti](https://blog.quantinsti.com/autocorrelation-autocovariance/)  
**日期**: 2022-10-17  
**作者**: QuantInsti

---

## 原文

Autocorrelation and Autocovariance: Calculation, Examples, and More

ByJosé Carlos Gonzáles Tanaka

Autocorrelation and autocovariance are one of the most critical metrics in financial time series econometrics. Both functions are based on covariance and correlation metrics. You will learn more about them. This easy-to-learn essential guide will help you understand better about ARMA models.

What is autocovariance?

What is autocorrelation?

What are the autocovariance and autocorrelation at lag zero?

Calculation of autocovariance with an example

Calculation of autocorrelation with an example

Computation of autocovariance and autocorrelation in Python

Plot the autocorrelation function in Python

Computation of autocovariance and autocorrelation in R

Plot the autocorrelation functions in R

What is partial autocorrelation?

Computation of partial autocorrelation in Python and R

You might have encountered yourself trying to learn the AutoregressiveMoving Average(ARMA) model. You then started to see a lot of use of covariances and correlations, but strangely enough, you see those two words with the prefix "auto"and you get frightened!

Don’t worry, this article will help you understand their details. Just keep the focus on the article and everything will be ok!

What is autocovariance?

First, you need to understand whatcovariance and correlationare. Remember that covariance is applied to 2 assets. The autocovariance is the same as the covariance.

The only difference is that the autocovariance is applied to the same asset, i.e., you compute the covariance of the asset price return X with the same asset price return X, but from a previous period.

How’s that possible?Simple, check it out:

Where X and Y can be the returns of asset X and Y, respectively.

Now, the autocovariance function can be defined as:

Where:

\( \gamma_{s} \text{: Autocovariance at lag “}s\text{”}.\)

\( r_{t} \text{: Asset price returns at time “}t\text{”}.\)

\( r_{t-s} \text{: Asset price returns at time “}t-s\text{”}.\)

What is autocorrelation?

In simple terms,autocorrelationis the same as the correlation function! To be specific, autocorrelation, as the autocovariance, is applied to the same asset.

Check the difference between correlation and autocorrelation (also called serial correlation) below:

$$ \text{Corr(X,Y)} =  \frac{\sum_{i=1}^{n}\left(X_{i}-\overline{X}\right)\left(Y_{i}-\overline{Y}\right)}{\sqrt{\left(\sum_{i=1}^{n} \left( X_{i}-\overline{X} \right)^2 \right)\left(\sum_{i=1}^{n} \left( Y_{i}-\overline{Y} \right)^2 \right)} }= \frac{\sum_{i=1}^{n}\left(X_{i}-\overline{X}\right)\left(Y_{i}-\overline{Y}\right)}{\sqrt{\sum_{i=1}^{n} \left( X_{i}-\overline{X} \right)^2}\sqrt{\sum_{i=1}^{n} \left( Y_{i}-\overline{Y} \right)^2}}$$$$\text{Corr(X,Y)} = \frac{Cov(X,Y)}{SD_{X}SD_{Y}}$$

Where:

\( \text{Cov(}X,Y\text{: Covariance between }X \text{ and }Y.\)

\( SD_{X} \text{: Standard Deviation of variable }\text{X}.\)

\( SD_{Y} \text{: Standard Deviation of variable }\text{Y}.\)

Now let’s check the autocorrelation:

Where:

\( \rho_{s} \text{: Autocorrelation at lag “}s\text{”}.\)

\( r_{t} \text{: Asset price returns at time “}t\text{”}.\)

\( r_{t-s} \text{: Asset price returns at time “}t-s\text{”}.\)

\( \text{Var}\left(r_t\right) \text{: Variance of returns}.\)

You might ask us:

Why variance and not the multiplication of thestandard deviationof the returns at the different lags?

Well, you must remember that an ARMA model is applied to stationary time series. This topic belongs totime series analysis. Consequently, it is assumed that the price returns, if stationary, have the same variance for any lag, i.e.:

What are the autocovariance and autocorrelation at lag zero?

Interesting question and simple to answer! Let’s see first for the former:

Can you guess what the last part resembles?It is the variance of the price returns!

Consequently, the autocovariance of the returns at lag 0 is the variance of the returns.

Can you guess now what the autocorrelation of the returns would be at lag 0?Let’s use the formulas to find out:

Since we know, from the above algebraic calculation, that the covariance of the same variable is its variance, we have the following:

Consequently, the autocorrelation function for any asset price return at lag 0 is always 1.

Calculation of the autocovariance with an example

You might have been thinking up to now:Why are the autocovariance and autocorrelation defined with an “s” subscript?Great question!

Let us explain: Actually, the autocovariance formula defined above is a function which allows the calculation of the autocovariance for different lags. The same for the autocorrelation function.

Confused? Don’t worry! We got you covered!

Let’s see an example to make the concept clear to your thoughts! We are going to make an example of how to calculate the autocovariance of the Microsoft price returns at lag 1. We are going to use the autocovariance function shown above.

Imagine we have the following returns for Microsoft prices:

Day 10

Let’s suppose we want to compute the autocovariance at lag 1. You will need the returns up to day 10, and the 1-period lagged returns up to day 9.

Thus, you have the following data structure for returns on days 10 and 9:

Variable

Day 10

\( r_{t} \)

\( r_{t-1} \)

Do you get to see the difference between the 2 variables?The second one is the first lag of Xt.

Now, since the 2 variables have different dimensions (the first one has 10 observations, while the second one has 9), we are going to use data from day 2 onwards.

Consequently, our data is as follows:

Variable

Day 10

\( r_{t} \)

\( r_{t-1} \)

The covariance between these 2 variables will be the autocovariance of the returns at lag 1.

You can do this, right?Check an example we give in our previous article.

Before you get ready to use a pencil and a piece of paper, let us tell you something important.

Remember the autocovariance formula:

If you paid attention to details, you could see that the average return is the same for both returns, in our case, for returns up to day 10 and up to day 9. As we explained before, autocovariance and autocorrelation functions are applied only tostationary time series.

Consequently, not only the variance but also the mean is a unique value for the whole span. That’s why the mean is the same for any lag of the price returns.

The mean of the Microsoft price returns is 1.1%. Let’s follow the procedure to compute the autocovariance:

Variable

\( r_{t} \)

\( r_{t-1} \)

\( \left(r_{t}-\overline{r}\right) \)

\( \left(r_{t-1}-\overline{r}\right) \)

\( \left(r_{t}-\overline{r}\right) \)\( \left(r_{t-1}-\overline{r}\right) \)

-0.100%

3.900%

-0.004%

-3.100%

-0.100%

0.003%

1.900%

-3.100%

-0.059%

-5.100%

1.900%

-0.097%

4.900%

-5.100%

-0.250%

0.900%

4.900%

0.044%

-2.100%

0.900%

-0.019%

-4.100%

-2.100%

0.086%

Day 10

2.900%

-4.100%

-0.119%

The autocovariance is just the sum of the last column values divided by (N-1, equal to 8), which results in -0.046%.

Calculation of the autocorrelation with an example

Let’s follow the same exercise and compute the autocorrelation of the Microsoft price returns up to day 10 at lag 1. The autocorrelation is the autocovariance divided by the variance. We give you the exact hint you need: The variance of Microsoft price returns up to day 10 is 0.121%.

Let’s follow the algebraic formulas and use the numbers to compute the autocorrelation:

Computation of autocovariance and autocorrelation in Python

Before we do this section, let us tell you something. We have computed the autocovariance and autocorrelation of the Microsoft price returns at lag 1. We couldn’t have computed at lag 2, lag 3, etc. We leave you that as an exercise!

InPython, or any other programming language, when you are required to compute these two important metrics, you will need to compute them at many lags, not only 1, as we did previously above.

So, keep in mind that we are going to use Python to compute the autocovariance and autocorrelation functions, i.e., the autocovariance and autocorrelation at different lags.

First, let’s import the necessary libraries to use:

We now download the Microsoft close prices from January 2021 to August 2022:

We compute the price returns:

As we told you above, in any programming language which has available a library to compute the autocovariance and autocorrelation, you will see you’re going to have functions to get their values for many lags with just that unique functions.

So, let’s compute the autocovariance function up to lag 10 for the Microsoft price returns.

Check the values below:

\( \gamma_{0} \)

0.00028672

\( \gamma_{1} \)

-0.00001403

\( \gamma_{2} \)

-0.00000250

\( \gamma_{3} \)

-0.00001941

\( \gamma_{4} \)

0.00002185

\( \gamma_{5} \)

0.00000488

\( \gamma_{6} \)

-0.00001460

\( \gamma_{7} \)

0.00001332

\( \gamma_{8} \)

-0.00002423

\( \gamma_{9} \)

0.00002422

Let’s compute the first 10 autocorrelation values:

See the values:

\( \rho_{0} \)

\( \rho_{1} \)

-0.04893

\( \rho_{2} \)

-0.00871

\( \rho_{3} \)

-0.0677

\( \rho_{4} \)

0.076198

\( \rho_{5} \)

0.017024

\( \rho_{6} \)

-0.05092

\( \rho_{7} \)

0.046457

\( \rho_{8} \)

-0.08451

\( \rho_{9} \)

0.084456

As you learned previously, you see that the autocorrelation at lag 0 is 1.

Plot the autocorrelation function in Python

What is usually done in econometrics is to plot the autocorrelation function. We, of course, are going to do that, see:

You see something strange in the plot, right? What is that blue-coloured highlighted zone? Well, it’s the confidence interval. You can compute that zone with the following formula:

Where T is the total number of observations.

Computation of autocovariance and autocorrelation in R

Let’s go through this excellent programming language. We install the necessary packages and import them:

Next, we use the getSymbols method to download the Tesla stock data with the same span as for Microsoft.

We compute the returns:

And we obtain the autocovariance function up to lag 10:

Let’s now compute the autocorrelation function up to lag 10:

As you can deduct, the default value for “type” is the autocorrelation function.

Plot the Autocorrelation Function in R

Finally, let’s plot the autocorrelation function:

We specify first the graph parameters: The main size increase, the axis values increase and the axis labels increase all of them with respect to the plot default value. Besides, we define the margins of the plot.

Next, we plot the autocorrelation function. Finally, we apply the graph parameters to the autocorrelation function plot.

What Is partial autocorrelation?

Since our mission is to prepare you to model an ARMA process, we need to explain to you this function.

What is it? Let’s explain the function of intuition.

For example, the autocorrelation function at lag 5 might have correlations with its previous lags’ autocorrelations. The partial autocorrelation function gives the autocorrelation at lag 5, but without the relationship of the shorter lags’ autocorrelations.

Putting it in another way, the autocorrelation of Microsoft price returns at lag 5 is about the autocorrelation between returns at time t and at the time (t-5). But this autocorrelation is also influenced by the correlations from lag 1 to lag 4.

The partial autocorrelation is a function that allows having the autocorrelation of returns t and (t-5) removing the indirect relationship that returns from lag 1 to 4 have on it.

Computation of partial autocorrelation in Python and R

Let’s compute them in python and R.

We follow our previous order. We begin with Python. We plot the partial autocorrelation function for Microsoft:

Let’s compute the partial autocorrelation function for the Tesla stock price returns in R:

We use the same code as for the autocorrelation function, but this time we specify “type=partial” to get the desired output.

Conclusion

ARMA models based their construction of inspection of the autocovariance and autocorrelation functions. Here, we have helped you understand the most important things about them and their applications in Python and R.

This will help you whenever you want to trade algorithmically since you have here useful code to use. Whenever you initiate yourself on the ARMA models, you will definitely remember this article and be well prepared to understand those types of models. Bookmark this article in your browser, you will not regret it!

As we told you before, this two formulas belong to the time series analysis topic. We guess you're already excited about the topic, aren't you? Do you want to continue learning about it? Check this course ontime series analysisto start trading algorithmically!

Are you ready to create your ARMA model? We bet you are!Ready? Set?Go algo!

File in the download

Autocorrelation and autocovariance in Python

Login to Download

Disclaimer: All investments and trading in the stock market involve risk. Any decision to place trades in the financial markets, including trading in stock or options or other financial instruments is a personal decision that should only be made after thorough research, including a personal risk and financial assessment and the engagement of professional assistance to the extent you believe necessary. The trading strategies or related information mentioned in this article is for informational purposes only.

---

*Imported from QuantInsti Blog on 2026-04-27*
