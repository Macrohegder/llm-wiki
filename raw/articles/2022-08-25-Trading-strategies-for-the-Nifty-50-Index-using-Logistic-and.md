---
title: "Trading strategies for the Nifty 50 Index using Logistic and Linear Regression"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/trading-strategies-nifty-50-index-logistic-linear-regression-project-vatsin-thaker/"
date: "2022-08-25"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Trading strategies for the Nifty 50 Index using Logistic and Linear Regression

**来源**: [QuantInsti](https://blog.quantinsti.com/trading-strategies-nifty-50-index-logistic-linear-regression-project-vatsin-thaker/)  
**日期**: 2022-08-25  
**作者**: QuantInsti

---

## 原文

Trading strategies for the Nifty 50 Index using Logistic and Linear Regression

The project involves using Logistic and Linear regression models in order to predict the closing price of next trading session for the Nifty 50 index using a set of input variables derived from the OHLC data of the Index.

Using a set of input variables such as (C-L) > (H-C), (H>Ht-1) & (L>Lt-1) we fit the model on the preceding calendar year and use the present year to run the model and back test the trading strategy.

Based on the performance of the strategies created by the Logistic model and the Linear regression model, we evaluate the performance by comparing the two amongst themselves and against the benchmark.

This article is the final project submitted by the author as a part of his coursework in the Executive Programme in Algorithmic Trading (EPAT) at QuantInsti. Do check ourProjects pageand have a look at what our students are building.

About the Author

Vatsin Thakerdescribes himself as an individual looking forward to integrate financial knowledge and technology. Vatsin is currently working at Vista Intelligence as a Research Executive where he amalgamates technology & artificial intelligence to the world of finance & business.

He holds an MS in Finance, a Bachelors in Financial Markets and has done certifications in Derivatives, Research, as well as Security to name a few. Vatsin is also an EPAT alumnus.

Project Abstract

Complex machine learning and deep learning techniques, artificial neural networks and computationally intensive mathematical models are being widely used in the domain of finance. Particularly in the forecasting of securities and indices of the stock markets around the globe.

The ultimate objective of this project focuses on using simplified machine learning models to create trading strategies using justified logic. This is done in order to evaluate the predictive power of these models against its benchmark.

This helps assess whether these models can be used to generate alpha as an alternative to highly complex models and techniques.

Introduction

With the advent of technology, multiple machine learning techniques have evolved which are used in the predictions of security prices.

Linear regression is one of the simplest forms of machine learning techniques which is used in estimating the value of the dependent variable based on the set of independent variables.

Logistic regression is another type of machine learning technique which estimates the probability of an event taking place (or not) based on a set of binary independent variables.

This project is a study involving the techniques of linear and logistic regression to create trading strategies in order to determine the predictive powers of the two models and comparisons with the benchmark Nifty 50 Index.

Data Mining

For the purpose of this study, we collect daily closing price data for the index from the NSE website for a period of 4 calendar years (2018-2021). We split the data into training and testing periods.

Data for 2018 is used for training the models and 2019 is the testing period after which the strategy is evaluated based on various metrics and so on. This process is repeated for all the years wherein the current year’s data is used to train the model and the following year’s data is used to test the model.

The data for the 4 years would capture multiple phases of the market which are the pre-COVID phase, COVID fall phase and the post-COVID recovery phase. The performance of the strategies in various phases could give an insight into the capability and reliability of these models over a longer time frame and different market phases.

Data Analysis

Logistic Regression Model

Logistic Regression Model is also known as a predictive model which gives output in the form of Binary results.

A Linear regression gives output in the form a value based on the betas of the independent variables and values of the independent variable

A Logistic regression model gives the output which can be interpreted as the probability of an event occurring.

Such a model is used when the data is dichotomous or binary (1 or 0). For this model, the independent variables are transformed into binary based from the raw data provided for the Nifty 50 Index.

The probability we wish to calculate is whether the succeeding day’s closing price of the Nifty 50 Index is higher than the current day’s closing price or not.

If the probability of this event occurring is greater than a provided threshold (50%),

we take a position at the current day’s closing price and

square off at the next day’s closing price

this is provided that the succeeding day’s trading session does not have an opening price less than our entry price.

In such a case, we square of at the opening price itself and limit the loss based on the hypothesis that the market has a weak opening which could lead to further weakening.

In order to calculate this probability, we use our training datasets to create the logistic model by creating 3 independent variables encoded as 1 and 0. We fit the model based on the data provided and compute the betas by maximizing the natural log of the likelihood.

The independent variables used for the logistic model were:

1. (C-L) > (H-C):Difference between the current day close and current day low is greater than the difference between the current day high and current day close. This variable denotes whether the closing price of the current day was nearer to the high price or the low price.

If it is closer to the high price, then the difference between the high price and close price will be lesser than the difference between the close price and the low price which is a sign of bullishness.

If this condition is fulfilled, the variable is assigned a value of 1 for that day and 0 otherwise.

2. (H>Ht-1):Current day high is higher than the previous day high. This is a sign of bullishness as previous day high was broken signaling buying momentum which can drive the prices further up.

If the condition is fulfilled, the variable is assigned 1 and 0 otherwise.

3. (L>Lt-1):Current day low is higher than the previous day low. This is a sign of bullishness as previous day low was not broken signaling strong support which can drive the prices further up.

If the condition is fulfilled, the variable is assigned 1 and 0 otherwise.

The dependent variable is the closing price of the succeeding day compared to the current day’s closing price.

(Ct+1>C):If the succeeding day’s closing price is higher than the current day’s closing price, the variable is assigned 1 and 0 otherwise.

Based on the above variables encoded as 1 and 0 based on the historical price data of the Nifty 50 Index, we fit a logistic model on the data for the time period 1-1-2018 to 31-12-2018 for computing the betas of the independent variables.

Given as the odds ratio, we denote Z in the form of a linear equation given by:

Zi= C + β1Xi1 + β2Xi2 + ………. + βkXik

Z is also termed as the odds ratio given by:

Zi= log[pi/(1-pi)]

For our study we denote Z as:

Zi= C + β1[(C-L) > (H-C)] + β2[H>Ht-1] + β3[L>Lt-1]

For values of the above independent variables denoted either as 1 and 0, the betas are multiplied by the same and based on the equation, the value of Z is computed.

In logistic regression, the model is dependent on the odds ratio which is transformed into probability using the sigmoid function given by:

pi= 1/(1+e-z)

In our study, the odds ratio is the ratio of probability of success divided by the probability of failure. Here, the probability of success is the succeeding day closing price higher than the current day closing price.

The odds ratio is then transformed into probability of success by using the sigmoid function which is also called as the logistic transformation. Once the betas are computed by maximizing the sum of the natural log of likelihood, the Z value is transformed using the sigmoid function and the predictions are made.

In order to evaluate the accuracy of the model, we create a matrix called as the Confusion matrix which computes the accuracy of the model predictions when compared with the actual event.

Linear Regression Model

Linear regression, as the name suggests, is a linear model which establishes a linear relationship between the dependent and the independent variables which is said to be the linear combination of the two.

Most commonly used notations in linear regression is theindependent variable(or variables) denoted by Y which are used as inputs to determine the value of thedependent variableX by using a linear equation represented by the intercept and the slope of the equation which is also called as the beta of the independent variable.

In Linear regression the dependent variable is a single characteristic represented by Y which is predicted using the independent variables. Based on the number of variables used to predict the value of the dependent variable, a regression model can be classified as:

Simple linear regression model- in case of a single independent variable, or

Multiple linear regression model- in case of more than one independent variable.

The most commonly used technique to create a linear regression model from the given dataset,Ordinary Least Squares (OLS)orLeast Squares Regressionis used.

For the purpose of this study, we created a trading strategy using the logistic regression model and compared the performance of the same with the benchmark Nifty 50 Index.

We used the three independent variables given by (C-L) > (H-C), H>Ht-1and L>Lt-1to predict whether the succeeding day’s closing price would be higher than the closing price of the current day.

We build a similar kind of trading strategy using Multiple linear regression using the same independent variables but create an entry logic which is closely related to the one used in the logistic model.

A Multiple linear regression model is represented as the following

Yi= C + β1Xi1 + β2Xi2 + ………. + βkXik

Given above, we predict the value of Y (dependent variable) using the independent variables represented by X.

The coefficients of the independent variables (also called as theslopeorbeta) are determined using an iterative method given by theOLS methodwhich calculates the sum of the squares of each data point from a given line and minimizes this sum using the iteration process.

At the end of the iteration process, we get a linear line which has the minimum sum of squares which is the regression equation for the model. For our study, the regression equation to be formed is given by

Yi= C + β1(H-C) + β2(C-L) + β3[H>Ht-1] + β4[L>Lt-1]

Key Findings

The above table is a summary of the various metrics of the strategies built using the logistic regression model and the linear regression model.

The models are compared with the benchmark Nifty 50 Index in terms of the returns generated for the given year and we see outperformance by both the models in 5 out of the 6 scenarios.

If we are to compare the two models among themselves, the logistic regression model performed better than the linear regression model in terms of the returns for all the phases.

There was not much to differentiate between the models in terms of the hit ratio which measured the accuracy of the trades undertaken.

Limitations

Although the strategies outperformed its benchmark, there are a few limitations in the study

Ignorance of transaction costs and slippages

Considering the Nifty 50 Index as the underlying and not its futures contract

Assuming that executions happen at the exact opening and closing prices

Unable to implement position sizing

Conclusion

The models shows the ability to significantly outperform the Nifty50 benchmark. It highlights the fact that simple strategies created using such variables can be proven profitable.

One must take care of the justified logic in the formation of thetrading strategywhich includes entry, exit and stop-loss logic, preceded by the creation and computation of the respective models.

The complete Python code and related information is provided in the Python code below. You can download and refer to it.

If you want to learn various aspects of Algorithmic trading then check out thisalgo trading coursewhich covers training modules like Statistics & Econometrics, Financial Computing & Technology, and Algorithmic & Quantitative Trading. EPAT equips you with the required skill sets to build a promising career in algorithmic trading. Enroll now!

File in the download

Complete Python Code of the project

Data files from 2018 to 2021 in excel format

Login to Download

Disclaimer: The information in this project is true and complete to the best of our Student’s knowledge. All recommendations are made without guarantee on the part of the student or QuantInsti®. The student and QuantInsti®disclaim any liability in connection with the use of this information. All content provided in this project is for informational purposes only and we do not guarantee that by using the guidance you will derive a certain profit.

---

*Imported from QuantInsti Blog on 2026-04-27*
