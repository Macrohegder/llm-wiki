---
title: "Gaussian Distribution: Formula, Variance, and Applications in Finance"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/gaussian-distribution/"
date: "2022-04-11"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Gaussian Distribution: Formula, Variance, and Applications in Finance

**来源**: [QuantInsti](https://blog.quantinsti.com/gaussian-distribution/)  
**日期**: 2022-04-11  
**作者**: QuantInsti

---

## 原文

Gaussian Distribution: What it is, How to Calculate, and More

ByMario Pisa

In this blog, we learn everything there is to Gaussian distribution. We will reveal some details about one of the most common distributions in datasets, dive into the formula to calculate gaussian distribution, compare it with normal distribution, and so much more.

We'll cover:

What is Gaussian distribution?

Why is it called a Gaussian distribution?

Difference between Gaussian distribution and Normal distribution

How is Gaussian distribution calculated?

Calculating Gaussian distribution using Python

Gaussian distribution in finance

Modern economics and Gaussian distributionWhat is the Efficient Market Hypothesis?What is the Black-Scholes-Merton model?What is the Efficient Frontier Portfolios theory?

What is the Efficient Market Hypothesis?

What is the Black-Scholes-Merton model?

What is the Efficient Frontier Portfolios theory?

Example of Gaussian distribution

What is Gaussian distribution?

When we are working with data in statistics, one of the most fundamental analyses is to check the data distribution.

Depending on the nature of the data, we can find different distributions. Such as the binomial distribution, the Poisson distribution, the Cauchy-Lorentz distribution, etc.

The Gaussian distribution is used in a generalized way to describe the behavior of prices, in this post we will try to understand a little better this distribution and the implications it has on the financial world and risk control.

Why is it called a Gaussian distribution?

The nameGaussian distributioncomes from the mathematician Carl Friedrich Gauss who realized the shape of the curve while studying the randomness of errors.

Or in honor of its discoverer sometimes it is named as Laplace-Gauss distribution since Gauss based his research on Laplace's studies.

Difference between Gaussian distribution and Normal distribution

TheGaussian distributionis so common that it is often called a normal distribution.

In the Gaussian distribution, most of the data are concentrated around a measure with a certain dispersion or variance. To be specific, a Gaussian distribution is symmetric and has a constant mean and variance.

This, therefore allows us to make predictions about an unknown value when we already have a set of known values that follow a Gaussian distribution. If the mean is zero and the variance is one, we call it astandard normal distribution.

Gaussian distribution, normal distribution,  bell curve, Gauss' bell... All these terms refer to the same thing. A normal or Gaussian distribution is found repeatedly in nature, such as the people/animals’ height or weight, the speed in a race, IQ, etc.

Gaussian distribution is one of the most frequently observed data distributions in nature hence, it is thus called normal or standard distribution. Or because of the shape of the graph, it is also often referred to as a Gauss' bell.

How is Gaussian distribution calculated?

The mathematic form of a Gaussian function is as follow:

\(\operatorname{f}(x)=a * \exp(- \frac {(x-b)^{2}} {2c^{2}})\)

for arbitrary real constants \(a\), \(b\) and *non-zero* \(c\).Gaussian functions are widely used in statistics to describe the normal distributions and hence are often used to represent the probability density function of a normally distributed random variable with expected value \(\mu = b\) and variance \(\sigma^2 = c^2\).In this case, the Gaussian is of the form:\(\operatorname{g}(x) = \frac{1} {\sigma \sqrt{2 \Pi}}  \exp(-\frac {1} {2} \frac {(x-\mu)^{2}} {\sigma^{2}} )\)Calculating Gaussian distribution using PythonLet's see how to compute a Gaussian distribution in Python:Gaussian distribution in financeQuantitative analysis of financial markets started with Louis Bachelier in 1900 who developed a new theory of probability based on Pascal and Fermat's 17th century studies of probability.His doctoral thesisThèorie de la Spèculation, which was not without controversy at the time, dealt with speculation as a business.The so-calledrandom walkmodel he developed asserts that prices would rise or fall with the same frequency, in the same way as a coin toss. That is, the outcomes are independent events.In this way he described thestandard deviationmathematically and created a simple mathematical template with which to measure dispersion. It seemed a simple and elegant way to find order within the chaos and randomness.With this model the variation of prices can be assessed.68% of the changes correspond to small variations around the mean (i.e. within one standard deviation),95% within two standard deviations and98% within three standard deviations.Large changes are extremely rare. They are the outliers, unlikely events that should occur once every hundred years.Modern economics and Gaussian distributionAs explained in the above section, the thesis was forgotten until 1964 when it was translated into English and modern economics started to be built on it.What is the Efficient Market Hypothesis?One of the theories that was built on Bachelier's thesis was Fama'sEfficient Market Hypothesis, according to which all relevant information is already reflected in the price.What is the Black-Scholes-Merton model?Another major model built on Bachelier's theory was theBlack-Scholes-Mertonmodel for valuing the fair price of financial options, where, as we know, standard deviation or volatility, is one of the important parameters to be considered.What is the Efficient Frontier Portfolios theory?Nevertheless, these models consider that the world has an order, that it can be described mathematically and therefore control the risk of financial operations and even build portfolios by adjusting the level of risk to be assumed in a portfolio, as proposed by Markowitz in theEfficient Frontier Portfoliostheory.All of the above names have received Nobel prizes for their work, and modern economics has been largely based on these and many other works. All of which found the Gaussian distribution to fit the behavior of markets quite well... at least most of the time.That is to say, all these studies believed that Bachelier was right.Surely the world would be an easier place if financial asset prices followed a Gaussian distribution, we would only need to pull out a calculator to analyse the risk of a trade or create a portfolio with a predefined risk. After all, a deterministic approach, when possible, always gives accurate results.Example of Gaussian distributionHowever, as we can see from the following two graphs, the S&P 500 return has many more outliers than should be expected.If we create a random series with the same mean and standard deviation as the S&P 500 return we see that the random standard distribution is contained and the actual distribution of returns becomes a little wilder.The financial world is full of brilliant minds and logically they realised that something was wrong with the models when we found so many booms & crashes in the markets and they started to patch up the theories with other models like GARCH, FIGARCH, etc.Honestly when I read Mandelbrot I couldn't stop thinking about thegeocentric Ptolemaic systemthat, when someone found evidence that didn't fit the model, Ptolemy created new theories about theheliocentric modelthat challenges it.Well, if you've made it this far, dear reader, I'm sure Mandelbrot's bookThe (mis) Behavior of Marketswon't let you down.It seems clear that the old financial models are coming to an end and other theories and models are emerging that can help us understand, and perhaps control, risk.Mandelbrot doesn't seem very optimistic about the future of machine learning for this endeavor, at least at the time of the book's publication. I particularly believe that it is a field that must be explored and understood as well.However, he proposes a disruptive mathematics - not new - that is still being developed and that could help us better understand the risk of financial operations.ReferencesThe (mis) Behavior of Markets. A fractal view of Risk, Ruin and Reward by Benoît Mandelbrot and Richard L. Hudson.Standard deviation and its use cases in Tradingby By Ashutosh Dave and Udisha AlokConclusionWe have seen that the Gaussian distribution is known by many names and that it is of vital importance in modern economics.We have also mentioned some holes in the theory of Bachelier's random walk and therefore in all the models that have been based on these studies. Finally, we shed a point of light to continue studying.If you too desire to equip yourself with lifelong skills which will always help you in upgrading your trading strategies. With topics such as Statistics & Econometrics, Financial Computing & Technology, Machine Learning, thisalgo trading courseensures that you are proficient in every skill required to excel in the field of trading. Check it out now!Disclaimer: All investments and trading in the stock market involve risk. Any decision to place trades in the financial markets, including trading in stock or options or other financial instruments is a personal decision that should only be made after thorough research, including a personal risk and financial assessment and the engagement of professional assistance to the extent you believe necessary. The trading strategies or related information mentioned in this article is for informational purposes only.

Gaussian functions are widely used in statistics to describe the normal distributions and hence are often used to represent the probability density function of a normally distributed random variable with expected value \(\mu = b\) and variance \(\sigma^2 = c^2\).

In this case, the Gaussian is of the form:

\(\operatorname{g}(x) = \frac{1} {\sigma \sqrt{2 \Pi}}  \exp(-\frac {1} {2} \frac {(x-\mu)^{2}} {\sigma^{2}} )\)

Calculating Gaussian distribution using Python

Let's see how to compute a Gaussian distribution in Python:

Gaussian distribution in finance

Quantitative analysis of financial markets started with Louis Bachelier in 1900 who developed a new theory of probability based on Pascal and Fermat's 17th century studies of probability.

His doctoral thesisThèorie de la Spèculation, which was not without controversy at the time, dealt with speculation as a business.

The so-calledrandom walkmodel he developed asserts that prices would rise or fall with the same frequency, in the same way as a coin toss. That is, the outcomes are independent events.

In this way he described thestandard deviationmathematically and created a simple mathematical template with which to measure dispersion. It seemed a simple and elegant way to find order within the chaos and randomness.

With this model the variation of prices can be assessed.

68% of the changes correspond to small variations around the mean (i.e. within one standard deviation),

95% within two standard deviations and

98% within three standard deviations.

Large changes are extremely rare. They are the outliers, unlikely events that should occur once every hundred years.

Modern economics and Gaussian distribution

As explained in the above section, the thesis was forgotten until 1964 when it was translated into English and modern economics started to be built on it.

What is the Efficient Market Hypothesis?

One of the theories that was built on Bachelier's thesis was Fama'sEfficient Market Hypothesis, according to which all relevant information is already reflected in the price.

What is the Black-Scholes-Merton model?

Another major model built on Bachelier's theory was theBlack-Scholes-Mertonmodel for valuing the fair price of financial options, where, as we know, standard deviation or volatility, is one of the important parameters to be considered.

What is the Efficient Frontier Portfolios theory?

Nevertheless, these models consider that the world has an order, that it can be described mathematically and therefore control the risk of financial operations and even build portfolios by adjusting the level of risk to be assumed in a portfolio, as proposed by Markowitz in theEfficient Frontier Portfoliostheory.

All of the above names have received Nobel prizes for their work, and modern economics has been largely based on these and many other works. All of which found the Gaussian distribution to fit the behavior of markets quite well... at least most of the time.

That is to say, all these studies believed that Bachelier was right.

Surely the world would be an easier place if financial asset prices followed a Gaussian distribution, we would only need to pull out a calculator to analyse the risk of a trade or create a portfolio with a predefined risk. After all, a deterministic approach, when possible, always gives accurate results.

Example of Gaussian distribution

However, as we can see from the following two graphs, the S&P 500 return has many more outliers than should be expected.

If we create a random series with the same mean and standard deviation as the S&P 500 return we see that the random standard distribution is contained and the actual distribution of returns becomes a little wilder.

The financial world is full of brilliant minds and logically they realised that something was wrong with the models when we found so many booms & crashes in the markets and they started to patch up the theories with other models like GARCH, FIGARCH, etc.

Honestly when I read Mandelbrot I couldn't stop thinking about thegeocentric Ptolemaic systemthat, when someone found evidence that didn't fit the model, Ptolemy created new theories about theheliocentric modelthat challenges it.

Well, if you've made it this far, dear reader, I'm sure Mandelbrot's bookThe (mis) Behavior of Marketswon't let you down.

It seems clear that the old financial models are coming to an end and other theories and models are emerging that can help us understand, and perhaps control, risk.

Mandelbrot doesn't seem very optimistic about the future of machine learning for this endeavor, at least at the time of the book's publication. I particularly believe that it is a field that must be explored and understood as well.

However, he proposes a disruptive mathematics - not new - that is still being developed and that could help us better understand the risk of financial operations.

References

The (mis) Behavior of Markets. A fractal view of Risk, Ruin and Reward by Benoît Mandelbrot and Richard L. Hudson.

Standard deviation and its use cases in Tradingby By Ashutosh Dave and Udisha Alok

Conclusion

We have seen that the Gaussian distribution is known by many names and that it is of vital importance in modern economics.

We have also mentioned some holes in the theory of Bachelier's random walk and therefore in all the models that have been based on these studies. Finally, we shed a point of light to continue studying.

If you too desire to equip yourself with lifelong skills which will always help you in upgrading your trading strategies. With topics such as Statistics & Econometrics, Financial Computing & Technology, Machine Learning, thisalgo trading courseensures that you are proficient in every skill required to excel in the field of trading. Check it out now!

Disclaimer: All investments and trading in the stock market involve risk. Any decision to place trades in the financial markets, including trading in stock or options or other financial instruments is a personal decision that should only be made after thorough research, including a personal risk and financial assessment and the engagement of professional assistance to the extent you believe necessary. The trading strategies or related information mentioned in this article is for informational purposes only.

---

*Imported from QuantInsti Blog on 2026-04-27*
