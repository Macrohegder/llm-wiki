---
title: "AutoRegressive Fractionally Integrated Moving Average (ARFIMA) model"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/arfima-model/"
date: "2023-10-13"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# AutoRegressive Fractionally Integrated Moving Average (ARFIMA) model

**来源**: [QuantInsti](https://blog.quantinsti.com/arfima-model/)  
**日期**: 2023-10-13  
**作者**: QuantInsti

---

## 原文

AutoRegressive Fractionally Integrated Moving Average (ARFIMA) model

ByJosé Carlos Gonzáles Tanaka

Usually, in algorithmic trading, we talk about AutoRegressive Integrated Moving Average (ARIMA) models. They’re very popular in the industry. You might remember that the “d” component in the model can be 0, 1, 2, etc. What if 'd' could take fractional values? We’ll learn about such models i.e. AutoRegressive Fractionally Integrated Moving Average (ARFIMA) here.

Let’s dive in and enjoy!

What is an ARFIMA model?

Purpose of the ARFIMA model

The ARFIMA Model Specification

Estimation of an ARFIMA model in R

Estimating the ARFIMA model in Python

An ARMA-based vs an ARFIMA-based model strategy performance comparison

Suggestion by Lopez de Prado

What is an ARFIMA model?

Do you remember an ARIMA(p,d,q) model? Let’s write its equation:

Usually “d” is 0, when we model asset returns, and d=1 when we model asset prices, “d=2” when second differences of the original series are stationary, etc.

An ARFIMA(p,d,q) is the same as an ARIMA(p,d,q). The only difference is that for the ARFIMA model, “d” can take float values between -1 and 1.

Purpose of the ARFIMA model

While learning about algo trading, you might have learned that in order to apply an ML model, or an econometric model such as the ARMA, GARCH, etc., it’s really important to convert the usually-non-stationary series into a stationary series by finding the integer-type order of integration and differencing “d” times the series.

Understanding thestationary data definitionis crucial for effectively applying models like ARFIMA, ARMA, or GARCH. By ensuring your data is stationary, you lay the foundation for more accurate predictions and stronger models. Explore further to see how this concept can refine your analysis and enhance the reliability of yourtrading strategies.

Well, we say this because ML models, as statistical models, need to be used on data that has a constant mean, variance and covariance (with respect to time).

However, when we convert prices to returns, to make them stationary, we have returns which have the good statistical properties to be used as input for an ML, but they lose what is called “memory”.

This is nothing else than the persistence of autocorrelation that we usually find it in asset prices. Then, a researcher in the 80s came up with an interesting model.

Hosking (1981)presented the ARIMA process to have the “d” value become a non-integer value, i.e., generalized the ARIMA model to make it have the differencing degree to be fractional values. This is what we call the ARFIMA model.

The main model’s purpose is to account for the persistence of memory that we find in economic and financial prices in levels while estimating an ARMA model on them.

This means that we could model an ARMA model which could have incorporated the long-term persistence that we don’t usually have in ARMA models applied to prices in first differences. This feature increased the forecasting power of simple ARIMA models.

According toLópez de Prado (2018), there is scarce literature related to ARFIMA models. Applications in retail trading are minimal, too. Let’s try our hand at it and see what emerges.

The ARFIMA Model Specification

Let’s understand the model better with algebraic formulations as it’s usually done with the ARMA model. We follow López de Prado's (2018)booknotation and formulas.

You have learned in the ARMA article about lag operators. Let’s leverage on that article knowledge and use the lag operator here to explain the ARFIMA model.

Let’s reprise the mechanics of the lag operator. If X(t) is a time series, we have

For d = 2 is:

In order to explain in detail the ARFIMA model lag slopes, we remember here the following math formula, that, for any positive integer “n”.

Besides, for any real number “d”:

Now, an ARFIMA(0,d,0) model can be described as:

With d float values between -1 and 1.

The polynomial characteristic

can be converted to a binomial series expansion as:

Besides, the ARFIMA(0,d,0) model residuals can be described as X:

Where the coefficients (the weights) per each X, using all the above formulas, are described as

At this stage, you might want to quit this article.

I don’t understand these formulas!

Don’t worry! We have the following formula to iterate through each weight:

Where "k" represents the lag of price series. This is a nicer formula to create the weights, right? So whenever you have a specific “d”, you can use the above formula to create your ARFIMA residuals.

However, if you want to estimate an ARFIMA(p,d,q) model, then you would need to estimate the parameters with optimization algorithm.

Should I recreate the estimation from scratch?

No! There are great R libraries called “arfima” and “rugarch”. Let’s continue to the next section to learn more about this.

Estimation of an ARFIMA model in R

We’re going to estimate an ARFIMA(1,d,1) model and also create an ARFIMA-based trading strategy.

Let’s do it!

First, we install and import the necessary libraries:

Step 1: Import libraries

We import the Microsoft stock from 1990 to 2023-09-09 and pass the data into a dataframe.

Step 2: Estimate ARFIMA

We estimate an ARFIMA(1,d,1) with the “arfima” function provided by the “arfima” package.

Let’s show the summary

In the “Mode 1 Coefficients” section, you will see the coefficients. In this case we estimated an ARFIMA(1,d,1) model. The phi estimate represents, as in the ARMA model, the autoregressive component. It’s significant.

The theta estimate represents the moving average component, which is also significant. The “d.f” is the fractional integration parameter, which is 0.49623, which is also significant. The fitted mean is the mean of model-based in-sample prediction values. Sigma^2 is the variance of residuals.

In the Numerical Correlations of Coefficients section, you see the correlation values between each parameter. In the Theoretical Correlations of Coefficients, you see the correlation obtained by theQuinn (2013)algorithm.

The theoretical correlations are the ones we should expect in case  The last result, the Expected Fisher Information Matrix of Coefficients, is thecovariance matrixassociated with maximum-likelihood estimates.

Don’t worry about these concepts. We only need to take care of the coefficients, their values and their statistical significance.

Step 3: Plotting

Let’s compute the residuals and plot them.

The ARFIMA(1,d,1) model might not be the best model for the MSFT prices. The parameters p and q might be other numbers. That’s why we’re going to use the “autoarfima” function provided by the “rugarch” library.

We’re going to estimate a series of ARFIMA models for each day. In order to do that, we’re going to use all the CPU cores available on our computer.

That’s why we’re going to use the parallel package.

Parallel Package

Step 1: Find the number of cores

We’re going to use the total number of cores minus one, so the one not used will be actually used for the whole operation.

Step 2: Create clusters

We’re going to create aclusterof these cores with the following function.

Step 3: Estimate ARFIMA models

Now we estimate several ARFIMA(p,d,q) models varying their parameters for only the first 1000 observations (4 years, aprox.). There are many inputs for the autoarfima function:

We choose to estimate the ARFIMA models with p and q values ranging from 0 to 5.

To select the best model, we use the BIC.

We select the “partial” method, in the sense that, e.g., if estimate an ARFIMA(2,d,0), then we only estimate a single model with 2 lags in the AR component. If we selected the “full” method, then for the ARFIMA(2,d,0), we would estimate 3 models: A model with only the first lag, only the second lag, and the last with the two lags.

If we set the arfima input to FALSE, then we would estimate an ARMA model, so we set it to TRUE.

We include a mean for the series, so we set it to TRUE.

We use the cluster created above to parallelize the estimation and gain speed with it.

We use the normal distribution setting distribution.model to “norm”.

Estimate the models with the general nonlinear programming algorithm setting the solver to “solnp”. You can also choose “hybrid” so the estimation is done with all the possible algorithms.

Set return.all to False because we don’t want to return all the fitted models, only the best one selected with the BIC.

Let’s code to get the ARFIMA residuals’ plot and then show it

Don't worry about the first value, it's actually the first asset price value. You can take the residuals from row 2 onwards in case you want to do something else with them.

Estimating the ARFIMA model in Python

Up to now, there’s no way to create an ARFIMA model in Python. So what do you do?

There are many ways. You can use libraries. Here we’re going to create our own way without using any Python library.

First, you’ll have two files

A Python file with the following code:

Import libraries

Import data from yahoo finance

Save the data into an xlsx file with the name “data_to_estimate_arfima”

Call the R script called “Estimate_ARFIMA.R”.

Import the dataframe that results from the R file as “df”

Plot the residuals from “df”

An R script with the following code:

Import libraries

Set the working directory the same as the script’s folder

Import the data called “data_to_estimate_arfima.xlsx” and save it in data

Estimate the best ARFIMA model with the autoarfima function from the “rugarch” package.

Create another dataframe called “data2” to save the dates and the residuals

Save “data2” into an Excel file named “arfima_residuals_R.xlsx”

The whole procedure will be based on the Python file steps. In Python step 4, we’re going to use the R script. Once the R script finishes running, then we continue with Python step 5 and onwards.

Let’s present the R script file called “Estimate_ARFIMA.R”. It uses a lot of the code learned above.

Let’s now go through each step in the jupyter notebook

Step 1: Import libraries

First, we import the necessary libraries

Step 2: Getting the data

Then we download the data from yahoo finance of Apple for the years 2020 to September 2023 and save it in an Excel file

Then, we call the subprocess library and use the “run” function. It has two inputs. The second one is the R script which should be located in the same folder in which the jupyter notebook is located.

And the first input is the “Rscript” application from the R programming language which allows you to make this whole process happen. I'm using Linux, so you just need to put "Rscript".

In the case of Windows, you'll need to specify the "Rscritpt" address. The address “C:\Program Files\R\R-4.2.2\bin” is from my personal computer. Try searching in your own computer where this Rscript is located.

Voilà! There you go! You have run an R script without open any R IDE. Just using a jupyter notebook!

Now, let’s plot the residuals. First, we import the created dataframe. It will be saved in the same working directory. We dropped the first row because it can be ignored.

Now, let’s plot the residuals

An ARMA-based vs an ARFIMA-based model strategy performance comparison

We’re going to compare an ARMA-based and an ARFIMA-based model trading strategy to see which one performs better!

We’re going to use again the Apple price time series from 1990 to 2023-09-09.

Step 1: Import libraries

We'll import and install the necessary libraries.

Step 2: Downloading data

Download the data and create the adjusted close price returns.

Step 3: Estimating the ARFIMA model

Create a “df_forecasts” dataframe in which we will save the ARFIMA residuals and the trading strategy signals. We choose (arbitrarily) to estimate the ARFIMA model using a span of 1500 observations (6 years).

Step 4: Estimating the ARFIMA model each day

Create a loop to estimate the ARFIMA model each day. We make use of CPU-multithreading as we did before. We go long whenever the forecasted price is higher than the last historical price. We choose the best model based on the BIC.

Before the for loop, we present 2 functions. The first one is to estimate the ARFIMA model. The second one is a wrapper function which will allow us to stop the estimation whenever it takes more than 10 minutes. There could be some cases where the estimation doesn't converge, or takes too long to converge. In these cases, we can stop the estimation with this wrapper function.

Step 5: Creating signals

Estimate the ARMA model and create signals based on the best model chosen by the BIC, too. We also use a 1500-observation span. We keep using the df_forecasts dataframe from before to save the signals.

Step 6: Cumulative returns

Create the ARFIMA-based and ARMA-based cumulative returns.

Let’s code to plot both strategies’ cumulative returns together with the buy-and-hold strategy.

In terms of the equity curve last values, the Buy and Hold strategy performs the best compared to the other two strategies.

Let’s compute the statistics of each strategy:

According to the table, we can see that the buy-and-hold strategy is the best one as per all the statistics. However, the ARFIMA model gets a lower volatility. The ARMA model is also better than the B&H strategy except for the annual and cumulative returns.

Besides, the ARMA model is also superior with respect to the ARFIMA model except with respect to the annual and cumulative returns, where the latter model performs better than the former model.

Some considerations are to be taken into account. We didn’t:

Incorporate slippage and commissions.

Incorporate a risk-management process.

Optimize the span

Use other information criterias such as Akaike, HQ, etc.

Suggestion byLopez de Prado

Having stationarity and memory preservation at the same time

ARFIMA model residuals might not always result in being a stationary time series. If the ARFIMA estimation gives a “d” between the range [-0.5,0.5], then the ARFIMA model will be stationary; otherwise, the model won’t be stationary.

So, even though the ARFIMA model captures the long memory of the price series. Not necessarily the model will provide stationary residuals.

López de Prado suggests that we can assure having a stationary process while preserving the long memory of the price series.

How?Well, instead of estimating the ARFIMA model, we actually calibrate the “d” parameter with an ADF test in order to find the best “d” that makes the ARFIMA residuals stationary and also has the memory persistence of the asset prices. To evaluate the memory preservation, we find the correlation between the asset prices and their price ARFIMA-based residuals.

Step 1: Import libraries

Let’s show the code. First we import the respective libraries

Step 2: Import data

Then, we import the Apple price data from 2001 to September 2023.

Step 3: Functions

We provide the following two functions given by López de Prado’sbookwith slight modifications.

The first functionis to compute the weights described above.

We use as inputs the chosen “d”, a threshold to be used to truncate the number of weights.

As you go well behind the past, the weights will have a small number, in order to avoid such tiny numbers, we truncate the number of weights.

The “lim” is a limit number to be considered also a truncation number to select a specific number of weights.

The second functionis to compute the ARFIMA residuals based on the chosen “d”.

The first input is the price series, then you input the chosen “d”. Next the threshold described above, and the last input are the weights array.

In case you input the weights array, this second function will use it; otherwise, the function will use the first one to compute the weights.

The next functionis also provided by López de Prado’s book.

It’s used to compute a dataframe in which we will use a range of “d” values in order to compute the ADF test statistic, p-value, the number of autoregressive lags in the ADF equation, the number of observations in the ARFIMA residuals, the 95% confidence level and the correlation.

Step 4: Applying the functions

Let’s use all these functions. We apply the last function to the Apple prices. See the results:

As you can see, we get the results of the ARFIMA residuals’ statistics using a range of “d” values: 10 “d” values.

As per López de Prado, the best d will be chosen based on the ARFIMA model whose residuals will be stationary and also preserve memory. How to detect that?

Let’s see. In order to choose the best “d” which makes an ARFIMA model stationary. We need to choose the ARFIMA model ADF p-value which is close and lower than 5%. As you can see in the table, we’re going to choose the “d” values from 0.3 to 1, because these “d” values make the ARFIMA residuals stationary.

But that’s not all, we need to take care also of the long memory preservation. How to check that?

Well, the “corr” value is the correlation between the ARFIMA model residuals and the price series. Whenever there is a high correlation, we are going to be sure the long memory is preserved.

Note: If you compute the correlation of the price return series, you will see that the autocorrelation will be very low, we leave you that as an exercise.

So, are you ready? Did you guess it?

The best “d” according to this range of “d” values is 0.3 because the ARFIMA residuals for this “d” are stationary (p-value is 0.049919) and it preserves the long memory of th price series (correlation is 0.85073).

Now, we know you are a good student and you say:Why would we need to settle for this 0.3 value?We can can an even better value with more decimals!

Yes, that’s right.

That’s why we present you below a function which will estimate the best “d” with better precision. The function uses the following inputs:

DF: The dataframe of the asset prices.

Alpha: The confidence level to be used to compare the ARFIMA models’ results.

Minimum: The minimum value of the range of “d” values.

Maximum: The maximum value of the range of “d” values.

The function procedure goes like this:

Step 1:Copy the dataframe of the asset prices.

Step 2:Use the “d_estimates_db” function from above with the minimum and maximum values.

Step 3:Open a try-except block in which:

Select the “d” value from the “out” dataframe whose confidence level is the closest to and higher than “alpha” confidence level and save it in d1.

Select the “d” value from the “out” dataframe whose confidence level is the closest to and lower than “alpha” confidence level and save it in d2.

Proceed to estimate again the “out” dataframe having as minimum and maximum values for the range of “d” values the d1 and d2 numbers.

Open a try-except block to repeat the process. This new block will have inside another try-except block.

This whole process is to assure that we get a “d” number for which its ARFIMA model will be stationary as per the “alpha” confidence level.

We show the function now:

We could have created a single range of "d" values, instead of creating these nested try-except blocks. But this process assures we don’t estimate too many ARFIMA models whose “d” specific numbers will be useless.

Let’s use this function to compute the best “d” for the Apple prices. Our p-value threshold will be 0.04. This number is chosen arbitrarily. As long you it is below 5% (and close) everything will be ok. The closeness should be evaluated as per the correlation between the asset prices and the ARFIMA-based residuals

The best “d” is 0.3145 for the Apple prices between 2001 and 2022.

Let’s use the fracDiff_FFD function to compute the ARFIMA residuals:

And let’s plot these residuals:

Just to confirm, we apply an ADF test to these residuals

The p-value is 2.6% and less than 5%. Thus, these ARFIMA residuals are stationary.

Let's see the correlation between these residuals and the price series

Correlation is 0.84, thus is high. This means the ARFIMA residuals preserve the long memory persistence of the price series.

How would we use these ARFIMA residuals for our trading strategies?López de Prado suggests using these residuals as our prediction feature in any machine-learning model to create an algorithmic trading strategy on any asset price.

Conclusion

Everything’s been so cool, right? We spent time learning the basic theory of the ARFIMA model, estimated it and also used it as a strategy to forecast price returns. Don’t forget also that you can use the model’s residuals as a prediction feature for a machine learning model.

In case you want to learn more about time series models, you can profit from our courseFinancial Time Series Analysis for Trading. Here you will learn everything about the econometrics of time series. Don’t lose the opportunity to improve your strategy performance!

Files in the download

ARFIMA for article Part 1

ARFIMA for article Part 2

Estimate ARFIMA

Estimate ARFIMA with R in Python

Lopez de Prado ARFIMA

Login to Download

Disclaimer: All investments and trading in the stock market involve risk. Any decision to place trades in the financial markets, including trading in stock or options or other financial instruments is a personal decision that should only be made after thorough research, including a personal risk and financial assessment and the engagement of professional assistance to the extent you believe necessary. The trading strategies or related information mentioned in this article is for informational purposes only.

---

*Imported from QuantInsti Blog on 2026-04-27*
