---
title: "Predicting SL/TP Signal Using Machine Learning"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/predicting-sl-tp-signal-machine-learning-project-sunanda/"
date: "2020-01-20"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Predicting SL/TP Signal Using Machine Learning

**来源**: [QuantInsti](https://blog.quantinsti.com/predicting-sl-tp-signal-machine-learning-project-sunanda/)  
**日期**: 2020-01-20  
**作者**: QuantInsti

---

## 原文

Predicting SL/TP Signal Using Machine Learning

The most challenging part of trading is to decide when to exit a position. This EPAT Project could help you predict when to exit a BUY/ SELL position ie. in predicting SL/TP signal without human intervention, by using Machine Learning.

This article is the final project submitted by the authors as a part of their coursework in theExecutive Programme in Algorithmic Trading (EPAT®)at QuantInsti®. Do check ourProjects pageand have a look at what our students are building.

About the Author

Sunanda Ballais a senior data scientist building algorithmic trading models using machine learning. A Quant, Sunanda is into algorithmic trading, strategy building and backtesting. she holds a Bachelor’s degree in Computer Science from NIT, Warangal and a Masters degree in Computer Engineering from VJTI. Having 18+ years of experience in the industry across various roles, Sunanda is presently the AVP at Citibank, Pune.

Project Abstract

I have converted the unstructured financial data into dollar bars. Dollar bars are formed by sampling an observation every time pre-defined market value is exchanged. On these bars, I have applied a moving average crossover strategy to decide BUY/SELL position.

The most challenging part of trading is to decide when to exit a position. For this in technical analysis, we have a lot of technical indicators. Without human intervention using a machine learning technique, I could predict when to exit a BUY/ SELL position.

I have got very good accuracy when I used the meta-labelling technique.

Introduction

Many financial operations require making decisions based on predefined rules, like option pricing, algorithmic execution, or risk monitoring. This is where the bulk of automation has taken place so far, transforming the financial markets into ultra-fast, hyper-connected networks for exchanging information.

In performing these tasks, machines were asked to follow the rules as fast as possible. As emotional beings, subject to fears, hopes, and agendas, humans are not particularly good at making fact-based decisions, particularly when those decisions involve conflicts of interest.

In those situations, investors are better served when a machine makes the calls, based on facts learned from hard data. This not only applies to investment strategy development, but to virtually every area of financial advice: granting a loan, rating a bond, classifying a company, recruiting talent, predicting earnings, forecasting inflation, etc.

Furthermore, machines will comply with the law, always, when programmed to do so. If a dubious decision is made, investors can go back to the logs and understand exactly what happened. It is much easier to improve an algorithmic investment process than one relying entirely on humans. when it comes to identifying subtle patterns in a high-dimensional world, where the rules of the game change every day, all that fine-tuning turns out to be detrimental.

An ML algorithm can spot patterns in a 100-dimensional world easily.

Data Mining

Typically for any ML, “Garbage in, garbage out”. We need to do a lot of data pre-processing for the machine learning to be successful. Structuring the data correctly is very important.

Data collection:I have downloaded, IVE (S&P 500 Value Index) tick data fromhere. The data has Date, Time, Price, Bid, Ask, Volume fields for every tick.

Data preparation:Checked for outliers in price. Detected outliers in the prices using the median of absolute deviation (MAD) approach and deleted those prices.

Dollar Bars:Finance practitioners often refer to the OHLC data rows as “bars”. Instead of standard time bars which are samples of the ticks at regular interval of time, developed information-driven bars. I have applied the technique of “Dollar Bars”. Whenever the total amount of dollars traded exceeds the threshold, generated an OHLC bar. Next, I generated informative labels to indicate when to exit a BUY/SELL position on the dollar bars. The method is explained below.

Volatility calculation:The first step to understand the markets is to understand volatility in returns. When we use 1-day time bars we calculate volatility in daily returns. Here I am looking at dollar bars (irrespective of the time taken), so I calculated volatility in returns of the dollar bars. I have used Parkinson's Historical Volatility (HL_ HV). The Parkinson number, or High Low Range Volatility, developed by the physicist, Michael Parkinson, in 1980 aims to estimate the Volatility of returns for a random walk using the high and low in any number of bars.

Implementing moving average crossover strategy:

Buy/ Sell position (signal):This is generated whenever there the following conditions are satisfied.The logarithmic returns are greater than 3 times the average volatility. This is to ensure that the signal is a very strong signal.There is a crossover between 3 bars moving average crosses 7 bars average upwards / downwards.

The logarithmic returns are greater than 3 times the average volatility. This is to ensure that the signal is a very strong signal.

There is a crossover between 3 bars moving average crosses 7 bars average upwards / downwards.

Generating SL/TP Labels manually:(Stop Loss (SL) and Take Profit (TP))The following method is used in generate SL/ TP.Considered 3 barriers for deciding SL/TP. Two horizontal barriers one on the upside and one on the downside when log-returns breach threshold. One vertical barrier at the completion of two-dollar bars.There are three barriers (lower barrier, upper barrier, vertical/ dollar barrier). Based on what is touched first, the SL/TP is generated.

The following method is used in generate SL/ TP.

Considered 3 barriers for deciding SL/TP. Two horizontal barriers one on the upside and one on the downside when log-returns breach threshold. One vertical barrier at the completion of two-dollar bars.

There are three barriers (lower barrier, upper barrier, vertical/ dollar barrier). Based on what is touched first, the SL/TP is generated.

Now we have built a model using a strategy. Next, we will see whether it is possible to predict a label (SL/TP) using technical indicators and machine learning. This way we can automate the label generation.

Machine Learning:The dollar bars have open, high, low, close, volume for each bar.

Feature generation:I have used a package in Python to generate many technical indicators. From this I have deleted those features whose correlation is >= 50%.

Meta-Labelling:When I have implemented the moving average crossover strategy (discussed above) three types of signals (0, 1, -1) are generated. We can build a model to predict class (1 vs -1). When I tried this, I got 54% accuracy only. But as discussed[1], we can build a model to predict class (0 Vs [ 1, -1]). So, I implemented logisticregressionusing meta-labelling technique. This gave 64.85% accuracy.

Artificial intelligence in stock tradingfurther refines these models, adapting to market changes and enhancing predictions. This enables more data-driven, strategic trading decisions in ever-changing markets.

Key Findings

Dollar bars

Volatility Calculation

Technical Indicators – IID feature generation

Machine Learning technique

Conclusion

This model can detect SL/TP with accuracy 65.86%.We can improve this model by doing some more study.

If you want to learn various aspects of Algorithmic trading then check out theExecutive Programme in Algorithmic Trading (EPAT). The course covers training modules like Statistics & Econometrics, Financial Computing & Technology, and Algorithmic & Quantitative Trading. EPAT equips you with the required skill sets to build a promising career in algorithmic trading.

If you want to learn to use SVM on financial markets data and create your own prediction algorithm then yo can also check out theTrading with Machine Learning: Classification and SVMat Quantra. The course covers classification algorithms, performance measures in machine learning, hyper-parameters and building of supervised classifiers.

Disclaimer: The information in this project is true and complete to the best of our Student’s knowledge. All recommendations are made without guarantee on the part of the student or QuantInsti®. The student and QuantInsti®disclaim any liability in connection with the use of this information. All content provided in this project is for informational purposes only and we do not guarantee that by using the guidance you will derive a certain profit.

Files in the download:

Dollar Bars

Feature generation

Labelling dbars

Model fitting using Data Labelling

Login to Download

---

*Imported from QuantInsti Blog on 2026-04-27*
