---
title: "A time-varying-parameter vector autoregression model with stochastic volatility"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/tvp-var-stochastic-volatility/"
date: "2024-11-07"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# A time-varying-parameter vector autoregression model with stochastic volatility

**来源**: [QuantInsti](https://blog.quantinsti.com/tvp-var-stochastic-volatility/)  
**日期**: 2024-11-07  
**作者**: QuantInsti

---

## 原文

A time-varying-parameter vector autoregression model with stochastic volatility

ByJosé Carlos Gonzáles Tanaka

The basic Vector Autoregression (VAR) model is heavily used in macro-econometrics for explanatory purposes and forecasting purposes in trading. In recent years, a VAR model with time-varying parameters has been used to understand the interrelationships between macroeconomic variables. Since Primiceri (2005), econometricians have been applying these models using macroeconomic variables such as:

Japan time series (Nakahima, 2011)

US Bond yields (Fischer et al., 2022)

Monthly Stock Indices from industrialized countries (Gupta et al., 2020)

Peruvian exchange rate (Rodriguez et al., 2024)

Indian exchange rate (Kumar, M., 2010)

This article extends the model usage to something our audience greatly cares about: trading! You’ll learn the basics of the estimation procedure and how to create a trading strategy based on the model. You can find the TVP-VAR-SV model code onGitHubas well.

Are you excited? I was when I started writing this article. Let me share what I’ve learned with you!

This blog covers:

What is the difference between a basic VAR and a TVP-VAR-SV model?

The TVP-VAR-SV model variables

The priors

The mixture of indicators

The TVP-VAR-SV model estimation algorithm

A TVP-VAR-SV estimation in R

A trading strategy using the TVP-VAR-SV model in R

Notes about the TVP-VAR-SV strategy

What is the difference between a basic VAR and a TVP-VAR-SV model?

All the explanations of the basic VAR can be found in our previous article onVAR models. Here, we’ll provide the system of equations and compare them with our new model.

Let’s remember the basic model. For example, a basic bivariate VAR(1) can be described as a system of equations:

A time-varying parameter VAR would be something like the following:

Do you get to see the difference between the two models? Not yet?

Let’s use matrices to see it clearly.

Where:

Now you see it?

The only difference is that the model's parameters vary as time passes. Hence, it’s referred to as a  “time-varying-parameter” model.

Even though the difference appears simple,  the estimation procedure is much more complex than the basic VAR estimation.

You now say: I know we can have time-varying parameters, but where is the stochastic volatility in the previous equations?

Wait for it, my friend! We’ll see it later!

Don’t worry, we’ll keep it simple!

The TVP-VAR-SV model variables

The system of equations of the model

Using a new notation provided by Primiceri (2005):

Where:

Y: The vector of time series

B: The parameters of the lagged time series of this reduced model

A: The contemporary parameters of the time series vector

Sigma: The time-varyingstandard deviation(volatility) of each equation in the VAR.

Epsilon: A vector of shocks of each equation in the VAR.

What is the reduced model and what are contemporary parameters?

Well, in macroeconometrics, the reduced model can be understood as a simple VAR as modeled in our previous article onVAR models. In this model, today’s time series values of the VAR vector are impacted only by their lag versions.

However, economists also talk about the impact that the same today’s time series values have on each other today’s time series values. This can be modeled as:

This can shown as a matrix below:

Which can also be presented as a system of equations:

The above model is understood in econometrics as a structural model to comprehend the time series interrelationships, contemporary or not, between the time series analyzed.

So, assuming we have daily data, the first question, which belongs to y1, has a12*y2 as today’s y2 impact on today’s y1. The same is true for the second question, which belongs to y2, where we see a21*y1, which is today’s time series y1 impact on y2. In a VAR, we have lag periods impacting today’s variables, in a structural VAR we have today’s variables impacting today’s other variables.

Due to these contemporary relationships, there is a problem called endogeneity, where the error terms epsilons are correlated with Y_t-1. To estimate a structural VAR, we need to clearly identify the matrix A variables. As Eric (2021) explained, there are 3 ways in the economic literature. But it’s not only that, as per this model, A is also time-varying. We’ll see later how this variables are estimated.

When you pre-multiply the system of equations by A^-1, you get something like:

Which can be further simplified as:

Time-varying volatilities?

Yes! In a basic VAR, the error terms are homoskedastic, meaning, they present constant variance. In this case, we have variances that change over time; they’re time-variant.

The time-varying parameter stochastic behaviors

The basic VAR had its parameters constant. In this TVP-VAR-SV, we have almost all of our parameters time-variant. Due to this, we need to assign them stochastic processes. As in Primiceri (2005), we define them as:

We can then specify the matrix of variances of all the model’s shocks as:

Where I_n is the identity matrix and n is the number of time series in the VAR (in our case it’s 2). Q, S, and W are square positive-definitecovariance matriceswith a number of rows (or columns) equal to the number of parameters in B, A, and Sigma, respectively.

Something else to note: sigma is stochastic-based, which can be interpreted as stochastic volatility as, e.g., theHeston modelis.

The priors

For a Bayesian inference, you always need priors. In the Primiceri (2005) algorithm, the priors are computed using your data sample's first “T1” observations.

Using our previously defined variables, you can specify the priors (following Primiceri, 2005, and Del Negro and Primiceri, 2015):

N(): Normal distribution

B_ols: This is the point estimate of the B parameters obtained by estimating a basic time-invariant VAR using the first T1 observations of the data sample.

V(B_ols): This is the point estimate of the B parameters’ variances obtained by estimating a basic time-invariant structural VAR using the first T1 observations of the data sample. In B_0, the variance is multiplied by 4. This value can be named k_B.

A_ols: This is the point estimate of the A parameters obtained by estimating a basic time-invariant structural VAR using the first T1 observations of the data sample.

V(A_ols): This is the point estimate of the A parameters’ variances obtained by estimating a basic time-invariant structural VAR using the first T1 observations of the data sample. In A_0, this variance is multiplied by 4. This value can be named k_A.

log(sigma_0): This is the point estimate of the standard errors obtained by estimating a basic time-invariant structural VAR using the first T1 observations of the data sample.}

I_n: This is the identity matrix with “nxn” dimensions, where “n” is the number of time series used to estimate the VAR on them. Contrary to to A_0 and B_0, this variance is just multiplied by 1, where this value can be named k_sig.

IW: The inverse Wishart distribution

Q_0 follows an IW distribution with a scale matrix of k_Q^2 times 40 times V(B_ols) and 40 degrees of freedom

W_0 follows an IW distribution with a scale matrix of k_W^2 times 2 times V(B_ols) and 2 degrees of freedom

Q_0 follows an IW distribution with a scale matrix of k_S^2 times 2 times V(B_ols) and 2 degrees of freedom

k_Q^2, k_W^2 and k_S^2 are 1, 0.01 and 0.1, respectively.

Once you estimate the priors with the first T1 observations, then you get the posterior distribution using the rest of the data sample.

The mixture of indicators

Before we dive into the algorithm, let’s learn something else. Do you remember the reduced-form model:

To clear the error term, we get

Primiceri (2005), appendix A.2 explains that the above model has a Gaussian non-linear state space representation. The difficulty with drawing Sigma_t is that they enter the model multiplicatively.

This presents the issue of not making it easy for the Kalman filter estimation done inside the whole estimation algorithm (The Kalman filter is linear-based). To overcome this issue, Primiceri (2005) applies squaring and takes the logarithms of every element of the previous equation. As a consequence of this transformation, the resulting state-space form becomes non-Gaussian, because the log(epsilon_t^2) has alog chi-squared distribution. To finally get a normal distribution for the error terms, Kim et al. (1998) use a mixture of normals to approximate each element of log(epsilon_t^2). Thus, the estimation algorithm uses the mixture indicators for each error term and each date.

The TVP-VAR-SV model estimation algorithm

First of all, you need to know the TVP-VAR model estimation explained here follows the Primiceri (2005) methodology and Del Negro and Primiceri (2015).

This methodology uses the modified Bayesian-based Gibbs sampling algorithm provided by Cogley and Sargent (2005) to estimate the parameters.

Now you say: What? Is that Chinese?

We’ve got it! Don’t worry! Let’s explain the algorithm in simple words in detail. To let you know, regarding the Bayesian estimation approach, please refer to this article onBayesian Statistics In Financeand this other one onFoundations of Bayesian Inferenceto fully learn more about it.

Let’s explain the algorithm. Following Del Negro and Primiceri (2015), the algorithm consists of the following loop:

Draw means

Use the Kalman filter to update the state equation and compute the likelihood.

Sample the variable from its posterior distribution using a Metropolis-Hastings step.

MCMC is Markov Chain Monte Carlo. Please refer to our article onIntroduction To Monte Carlo Analysisto learn more about this type of Monte Carlo and the Metropolis-Hastings algorithm.

Theta is [B, A, V] where these 3 variables were defined previously.

p(e|d) is the corresponding probability distribution of “e” given “d”.

You iterate until you make the distribution converge. Even though we say the algorithm is based on MCMC and Metropolis-Hastings, Primiceri (2005) applies his own specifications for his TVP-VAR-SV model.

A TVP-VAR-SV estimation in R

Let’s see how we can estimate the model in this programming language. Let’s install the corresponding libraries.

Then let’s import them

Let’s import the data and compute the log returns.

Let’s estimate the model with all the available data and forecast the next-day return. To get this forecast, we get draws from the converged posterior distribution and we use the mean of all the draws to output a forecast point estimate. You can also use the median or any other measure of central tendency (Giannone, Lenza, and Primiceri, 2015).

Output:

[0.015880450, 0.013688861, 0.014319192, 0.002445156, 0.005108312, 0.020364678, 0.015684312]

These returns’ signs will depend on each day’s estimation.

There are 4 inputs to discuss:

tau: is the length of the training sample used for determining prior parameters via least squares (LS). In this case, we set it to one year: 250 observations. So, if we have “n” observations, we use the first 250 observations to get the priors and the last “n-250” for model estimation.

nf: Number of future time periods for which forecasts are computed. In this case, we’re interested in the next-day return.

nrep: It’s the number of MCMC draws excluding the burn-in observations. We set it to 300. You can read more about it in our blog onIntroduction To Monte Carlo Analysis.

nburn: The number of MCMC draws used to initialize the sampler used for convergence to get the posterior distribution. We set it to 20. So, since we have 300 draws, we compute the posterior distributions with the last 280 draws (300-20).

The function actually has more inputs, let’s see them together with their default values:

k_B = 4, k_A = 4, k_sig = 1, k_Q = 0.01, k_S = 0.1, k_W = 0.01,

pQ = NULL, pW = NULL, pS = NULL

You can relate k_B, k_A and k_sig with the previous section priors. Regarding the other inputs, see below:

A trading strategy using the TVP-VAR-SV model in R

Now we get to the place you wanted! We will use the same imported libraries and the same dataframe called var_data, which contains the stocks’ price log returns.

Some things to say:

We initialize the forecasts from 2019 onwards.

We estimate using 1500 observations as span.

We also estimate a basic VAR to compare performance with our TVP-VAR-SV strategy.

The strategy for both models will be long only.

Since the TVP-VAR-SV model estimation takes a lot of time each trading period, we have made the code script so that if you need to stop the code from running, you can do it and run it later by running the whole code again.

Let’s first define the function that will allow us to import the dataframe of the forecast results dataframe of the basic VAR and the TVP-VAR-SV model in case you have done so previously.

Then, we

Set the initial date to start the forecasting process.

Import the saved df_forecasts dataframe, otherwise, we create a new one without the previous function.

Set the span as 1500.

Next, we create the basic-VAR-based strategy signals. The code follows our previous article onVector AutoRegression model.

Next, we create the TVP-VAR-SV model signals through a similar loop. This time we set tau to 40. The input can be chosen arbitrarily as long as you respect the proportions between nrep and nburn.

The estimation of the model each day will take some minutes, thus, the whole loop will take a long time. Be careful. In case you need to turn off your computer before the loop runs, you can just turn on once again your computer and run the script once again. The code is written in such a way that whenever you want to continue running the for loop, you can just run the whole code.

Next, we compute the strategy returns. We have four strategies

A Buy-and-Hold strategy

A basic-VAR-based strategy

A TVP-VAR-SV-based strategy

A strategy based on the TVP-VAR-SV model makes its long signals if and only if the Buy-and-Hold cumulative returns are higher than their 15-window simple moving average.

See, Focusing only on equity returns, the basic VAR performs the worst.

The TVP-VAR-SV and the SMA-based TVP-VAR-SV strategy perform closely to the Buy-and-hold strategy. However, the latter performs the best in almost all the years. Let’s see their trading summary statistics.

The equity-curve informal conclusion can be further confirmed by the summary statistics.

The basic VAR performs the worst with respect to not only returns but also equity volatility. This is reflected in poor results for the Sharpe, Calmar, and Sortino ratios. The maximum drawdown is also huge.

The TVP-VAR-SV performs slightly better with respect to the Buy-and-Hold strategy.

The SMA-based TVP-VAR-SV is the best performer. It has an increased 80% equity curve return with respect to the Buy-and-Hold strategy and the other statistics are clearly better. The Sortino ratio is quite good, too.

Notes about the TVP-VAR-SV strategy

There are some things we need to take into account while developing a strategy based on this model:

We chose tau equal to 40 arbitrarily, which is probably not enough. Choosing another number would likely produce different results. The seed is also arbitrarily chosen. Do a hyperparameter tuning to get the best results while doing a walk-forward optimization.

We have chosen nrep equal to 300. This is quite small compared to macroeconometric standards, where nrep gets to be 50,000 in some cases. The reason econometricians use such a large number is that macroeconomic data samples are usually very small compared to financial data samples. Due to the low quantity of data samples, macroeconomic data tends to be fitted with this model very quickly even though they use nrep high. Due to our span being equal to 1500, if we used nrep equal to 50,000, the estimation for each day will surely take hours or even days. That’s why we use only 300 as nrep. Please feel free to change nrep at your convenience. Just make sure that, if you trade hourly, the model estimation should take less time than an hour for live trading, if you trade daily, the model estimation should take less than a day, and so on.

We haven’t incorporated stop-loss and take-profit targets. Please do so to improve your results.

Conclusion

We have delved into the basic definition of a TVP-VAR-SV model. We then explained a little bit the model estimation, and finally we opted for a trading strategy backtesting loop script to test the model performance.

Do you want to learn the basics of the financial time series analysis? Do not hesitate to learn from our courseFinancial Time Series Analysis for Trading.

Do you want more models to be tested?

Do not hesitate to follow our blog, we’re always creating more strategies for you!

References

Cogley, T. and Sargent, T. J. (2005), “Drifts and Volatilities: Monetary Policies and Outcomes in the Post WWII U.S.,” Review of Economic Dynamics, 8(2), 262-302.

Del Negro, M. and Primiceri, G., (2015), Time Varying Structural Vector Autoregressions and Monetary Policy: A Corrigendum, The Review of Economic Studies, 82, issue 4, p. 1342-1345.

Eric (2021) “Understanding and Solving the Structural Vector Autoregressive Identification Problem” in https://www.aptech.com/blog/understanding-and-solving-the-structural-vector-autoregressive-identification-problem/, consulted on August 1st, 2024.

Fischer MM, Hauzenberger N, Huber F, Pfarrhofer M (2023) General Bayesian time-varying parameter VARs for predicting government bond yields. J Appl Econom 38(1):69–87

Giannone, Domenico, Lenza, Michele and Primiceri, Giorgio, (2015), Prior Selection for Vector Autoregressions, The Review of Economics and Statistics, 97, issue 2, p. 436-451.

Gupta, R., Huber, F., and Piribauer, P. (2020) Predicting international equity returns: Evidence from time-varying parameter vector autoregressive models, International Review of Financial Analysis, Volume 68, 101456, ISSN 1057-5219.

Kim, S., Shephard, N., and Chib, S., (1998), Stochastic Volatility: Likelihood Inference and Comparison with ARCH Models, The Review of Economic Studies, 65, issue 3, p. 361-393.

Kumar, M., (2010) A time-varying parameter vector autoregression model for forecasting emerging market exchange rates, International Journal of Economic Sciences and Applied Research, ISSN 1791-3373, Kavala Institute of Technology, Kavala, Vol. 3, Iss. 2, pp. 21-39

Nakajima, Jouchi, (2011), Time-Varying Parameter VAR Model with Stochastic Volatility: An Overview of Methodology and Empirical Applications, Monetary and Economic Studies, 29, issue, p. 107-142.

Primiceri, Giorgio, (2005), Time Varying Structural Vector Autoregressions and Monetary Policy, The Review of Economic Studies, 72, issue 3, p. 821-852.

Rodriguez, G., Castillo, P., Calero, R., Salcedo, R., Arellano, M. A., (2024), Evolution of the exchange rate pass-through into prices in Peru: An empirical application using TVP-VAR-SV models, Journal of International Money and Finance, Volume 142, 2024, 103023, ISSN 0261-5606.

File in the download:

Trading strategy using the TVP-VAR-SV model in R - Python notebook

Login to Download

Disclaimer: All data and information provided in this article are for informational purposes only. QuantInsti®makes no representations as to accuracy, completeness, currentness, suitability, or validity of any information in this article and will not be liable for any errors, omissions, or delays in this information or any losses, injuries, or damages arising from its display or use. All information is provided on an as-is basis.

---

*Imported from QuantInsti Blog on 2026-04-27*
