---
title: "ARIMA vs LSTM: A Comparative Study of Stock Price Prediction Models | EPAT Project"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/time-series-lstm-stock-price-prediction-project-ashish-jain/"
date: "2024-01-19"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# ARIMA vs LSTM: A Comparative Study of Stock Price Prediction Models | EPAT Project

**来源**: [QuantInsti](https://blog.quantinsti.com/time-series-lstm-stock-price-prediction-project-ashish-jain/)  
**日期**: 2024-01-19  
**作者**: QuantInsti

---

## 原文

ARIMA Vs LSTM: A Comparative Study of Stock Price Prediction Models | EPAT Project

This project is about comparative study of time-series analysis techniques and ML techniques from the perspective of Stock/Index price prediction. Initial analysis was conducted using time-series modelling techniques eg. ARMA, ARIMA, etc. followed by the analysis of different ML models to predict the next day stock/index price.

After extensive theoretical study of different ANN models and based on input from a mentor, the LSTM model was finalized. Different optimization parameters and techniques on various evaluation criteria e.g. accuracy and precision were analyzed.

Both the prediction techniques i.e. ARIMA and LSTM gave almost similar results in terms of evaluation of predicted price, but it was found that ARIMA predictions are more accurate i.e., less RMSE for predicted price.

This article is the final project submitted by the author as a part of his coursework in the Executive Programme in Algorithmic Trading (EPAT) at QuantInsti. Do check ourProjects pageand have a look at what our students are building.

About the author

With over 18 years of experience in the IT industry,Ashish Jainis a seasoned professional specializing in Treasury and Investment Banking. He is currently serving as Director - Client Delivery, FinTech at Nasdaq.Before joining Nasdaq, he held leadership roles at Adenza as Senior Technical Manager and Calypso Technology as Principal Technical Consultant. He also gained valuable experience as an Application Developer at J.P. Morgan and an ASE at Tata Consultancy Services.Academically, Ashish holds a Master’s Degree in Computer Science from Thapar Institute of Engineering and Technology and a bachelor's degree from GCET, V.V. Nagar. His expertise in IT solutions and project management, combined with deep financial industry knowledge, has enabled him to drive impactful digital transformations in the FinTech space.

Project Abstract

This project is about comparative study of time-series analysis techniques and ML techniques from perspective of Stock/Index price prediction. After evaluation of performance of predicted price, low frequency trading strategy can be built using best model or combination of multiple models.

Introduction

I am new to trading world but have good experience with programming. My motivation was to build decent trading strategy for low-frequency trading using deep learning technologies or time-series modeling. Initial idea was to use time-series model output as input to machine learning models.

But, based on discussion with my mentor, I understood that it’s better to develop comparative study of both models as both are altogether different techniques. Once stock price prediction is available with reasonable accuracy, strategy can be built in a variety of ways.

Data Mining

I had a significant challenge in sourcing high-quality data. As a retail trader, I had a limited budget and I settled on yahoo finance which was giving me adjusted closing prices. Also, as per discussion with mentor, Yahoo Finance is very good option for this kind of comparative study and for scope of low frequency trading.

But forHigh Frequency Trading(HFT), paid data can be used to ensure quality and consistency of data.

I did consider downloading directly from the National Stock Exchange (NSE). The initial results were promising but the python wrapper to do this efficiently failed to work consistently hence I have elected to use yahoo finance.

I have used 5 years ofhistorical datafor my project. I could go back further but given the changes in India, I did not see the value in training a model on old data.

Data Analysis

Initially I started my analysis using time-series modelling techniques. As time-series modelling requires series to be stationary and I used Nifty Index price for my analysis which is not stationary. So, I considered using return series as it was stationary according toAugmented Dickey Fuller Test(ADF) and ACF/PACF analysis.

Understanding thestationary data definitionis crucial for accurate time-series modeling. When your data is stationary, it ensures more reliable results and better forecasting. Dive deeper to explore how this concept can enhance your analysis and improve the precision of your models.

But the prediction of return price and using it to build strategy brings its own complexity. So, I dropped the idea of using return series.

Then I found that differencing by order of 1 made Nifty price series stationary, so I considered usingARIMAmodel for Price forecasting. To get best model, need to find best values for AR and MA parameters.

There are two different approaches to get same:

Based on significant lags from ACF and PACF chart

Using AIC Score criteria for different combinations of parameters.

As you keep on increasing lag numbers, model becomes computationally intensive and takes too much of time to produce results e.g., it takes around 20 mins for 10 years of data. So, I kept parameters levels in range of 1-8.

First, I found initial trail params from ACF/PACF and then I used AIC score criteria to get top three set of params. Then I performed trial/error for those three params and found best param set i.e., 6,1,2.

I evaluated the model based on two criteria:

Root Mean Squared Error/Mean Absolute Percentage Error

Price Direction prediction

Below are the results of best performing time-series model:

The Mean Absolute Error is 109.84

The Mean Squared Error is 20378.46

The Root Mean Squared Error is 142.75

The Mean Absolute Percentage Error is 0.63

Direction Prediction (1 indicates correct direction and 0 indicate wrong direction prediction):

0 -- 1041

1 -- 190

Then I started analysis of ML model to predict next day stock/index price. My mentor provided much useful information/guidance over here and suggested to explore different ANN models, ML techniques before finalizing any ANN model. After extensive theoretical study of different ANN models and based on inputs from mentor, I decided to go ahead withLSTMmodel.

Initially I built single variate LSTM model which was taking only past price as input. Then based on inputs from mentor, I added some common technical indicators as input features to my LSTM model, eg.

MACDetc.

I used MinMax scaler for normalization of various input parameters/features. I used LSTM model with 5 layers. I tried different activation functions e.g., ‘tanh’, ‘relu’ based on theoretical study as well as trial/error. I got the best performance for tanh as input/middle-layer activation functions and ‘linear’ as output activation function. As per suggestion from mentor, I also tried different epochs and batch sizes.

I got best performance for epochs of size 100 with early stopping and batch size of 10. I used 5 years of historic data and train/test split was 80:20.

The best model performance was as below:

The Mean Absolute Error is 151.99

The Mean Squared Error is 34575.89

The Root Mean Squared Error is 185.95

The Mean Absolute Percentage Error is 0.82

Direction Prediction (1 indicates correct direction and 0 indicate wrong direction prediction):

0 -- 132

1 -- 102

Key Findings

The key findings from this project are as below:

Both prediction techniques i.e., ARIMA and LSTM gave almost similar results in terms of evaluation of predicted price, but ARIMA predictions are more accurate i.e., less RMSE.

There is major difference in directional prediction accuracy. LSTM is way better than ARIMA but still it’s less than 50%, so not useful practically.

Higher number of Lags can be used to further increase performance of ARIMA model provided we have sufficient computing resources available.

There are n number of parameters i.e., activation function, number of neurons, number of layers, optimization functions, number of epochs, batch sizes etc. for LSTM model. So best approach is to limit range of various parameters based theoretical study or research available.

But there is no definite logic so trial/error for different parameters is mandatory/recommended to arrive at best model.

It is important to shift predicted price before comparing it with next day close price otherwise model performance will be better due to look ahead bias factor.

Once model is finalized, it should be saved on local file system e.g., using pickle. It can be reused for back testing for different sets of data to avoid long computation time every time.

My analysis was limited to Nifty price series data, but model can be used for other stocks/indexes and fine-tuned for better performance.

Challenges

As time-series models are computationally intensive, it’s practically impossible to test higher lag values on local machine having limited resources.

Python IDEs eg., Spyder gives better performance compared to Jupyter Notebook.

The sourcing of high-quality data is hard and potentially expensive.

Building a Trading Strategy using predicted price is not fully explored. I did vectorized backtesting of LSTM model for NIFTY 10 years data and it produced 13% CAGR for long only trading strategy.

As strategy assumes buying at today’s Close price, which is practically not possible, so program should take available close price before 5mins. of market closing for live trading.

Event based back testing can be used to further refine model, entry and exit criteria of trading strategy e.g., stop loss, trailing stop loss, profit booking etc...

I used simple strategy by generating buy signal if predicted price is higher by 1% of today’s close price. Different varieties of strategies eg., using both Buy/Sell Signals, taking current day Open price as Input to predict today’s Close price, predicting direction only etc. can be evaluated for better returns.

Implementation Methodology

The project has been tested with the nifty50 index data from yahoo finance. It was not possible to test the project with broker supplied data due to limited budget.

All programs are developed in Python using Jupyter notebook and Spyder IDE

Conclusion

It is possible for a retail trader to build an effective strategy that uses machine learning or time-series modelling. Careful feature selection and feature engineering are needed to begin to use the strategy in a production environment. Extensive Trial-error is recommended to test performance for different combinations of model parameters.

Annexure/Codes

By clicking the download button below  you will get:

ARIMA Models

timeseries_nifty_arima.py – Forecasts Nifty prices using ARIMA.

timeseries_nifty_return.py – Predicts Nifty returns with ARIMA.

aic_score.ipynb – Finds the best ARIMA model using AIC score.

LSTM Models

nifty_lstm.py – Uses Close price for Nifty prediction.

nifty_lstm_model_reuse.py – Uses technical indicators + LSTM for price prediction & backtesting (10 years).

Data & Utilities

nifty_18_09.csv – Nifty price data (last 5 years).

tsa_functions_quantra.py – Utility functions for strategy analysis & model evaluation.

These files help in Nifty forecasting, return prediction, and strategy backtesting using ARIMA & LSTM models.

Login to Download

Bibliography

Web links reference used for Time Series Modelling:

https://towardsdatascience.com/time-series-from-scratch-autocorrelation-and-partial-autocorrelation-explained-1dd641e3076f/

https://spureconomics.com/interpreting-acf-and-pacf-plots/

https://www.researchgate.net/publication/261179224_Stock_price_prediction_using_the_ARIMA_model

https://blog.quantinsti.com/forecasting-stock-returns-using-arima-model/

Web links reference used for Machine Learning:

https://blog.quantinsti.com/trading-using-machine-learning-python/

https://blog.quantinsti.com/lstm-networks-predict-price-project-krishna-tunga/

https://machinelearningmastery.com/optimization-for-machine-learning-crash-course/

https://machinelearningmastery.com/how-to-configure-the-number-of-layers-and-nodes-in-a-neural-network/

https://machinelearningmastery.com/how-to-stop-training-deep-neural-networks-at-the-right-time-using-early-stopping/

https://www.finowings.com/technical-analysis/technical-analysis-terms/top-5-technical-indicators-for-novice-traders/

https://www.kaggle.com/code/shivajbd/input-and-output-shape-in-lstm-keras

https://machinelearningmastery.com/choose-an-activation-function-for-deep-learning/

https://blog.quantinsti.com/deep-learning-artificial-neural-network-tensorflow-python/

https://blog.quantinsti.com/machine-learning-model-long-only-strategy-retail-trader-project-pranav-lal/

https://blog.quantinsti.com/trading-strategies-nifty-50-index-logistic-linear-regression-project-vatsin-thaker/

https://towardsdatascience.com/illustrated-guide-to-lstms-and-gru-s-a-step-by-step-explanation-44e9eb85bf21

Udemy Courses:

Deep Learning: Recurrent Neural Networks in Python

time-series-analysis-an

Next Steps for you

Let’s Deep Dive into the essentials ofStationarity, theHurst Exponent, andMean Reversionto understand how and why time‐series data exhibit long‐term memory.

Once you’re comfortable with these, progress to advanced or multivariate methods, includingVector Autoregression (VAR),Johansen Cointegration, andTime-Varying-Parameter VAR.

Strengthen your grasp by looking intoAutocorrelation & Autocovarianceto see how data points relate over time, then deepen your knowledge with fundamental models such asAutoregression (AR),ARMA,ARIMAandARFIMA

If your goal is to discover alpha, you may want to experiment with a variety of techniques, such astechnical analysis, trading risk management, pairs trading basics,andMarket microstructure. By combining these approaches, you can develop and refine trading strategies that better adapt to market dynamics.

Want to know how EPAT equips you with skills to build your trading strategy in Python? Check out theEPAT course curriculumto find out more.

Explore EPAT trading projects on various topics:

LSTM Networks: Can They Predict Equity Index Prices?

Crypto Perpetual Contract Pair Trading

Optimizing Exit Conditions Using a Variable Take Profit and Stop Loss

Dispersion trading strategy in the Indian markets

About EPAT

QuantInsti’s Executive Programme in Algorithmic Trading (EPAT) offers an opportunity to join the exciting field of quantitative finance, with a specialisation in algorithmic trading. It is a fully online course with 120+ hours of live lectures, and a faculty pool of 20+ practitioners and experts from all over the world, with a focus on Python and practical implementation of theory/techniques covered in the course. With dedicated mentorship, the programme enables participants of various backgrounds to join this exciting field.  The curriculum covered in EPAT is comprehensive and cutting-edge, with lifetime access to improvements and additions.Connect with an EPAT career counsellorto discuss the right way ahead for you.

Disclaimer: The information in this project is true and complete to the best of our Student’s knowledge. All recommendations are made without guarantee on the part of the student or QuantInsti®. The student and QuantInsti®disclaim any liability in connection with the use of this information. All content provided in this project is for informational purposes only and we do not guarantee that by using the guidance you will derive a certain profit.

---

*Imported from QuantInsti Blog on 2026-04-27*
