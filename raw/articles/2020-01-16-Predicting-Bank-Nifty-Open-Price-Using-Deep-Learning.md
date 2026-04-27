---
title: "Predicting Bank Nifty Open Price Using Deep Learning"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/predict-bank-nifty-open-price-deep-learning-epat-project-balamurugan/"
date: "2020-01-16"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Predicting Bank Nifty Open Price Using Deep Learning

**来源**: [QuantInsti](https://blog.quantinsti.com/predict-bank-nifty-open-price-deep-learning-epat-project-balamurugan/)  
**日期**: 2020-01-16  
**作者**: QuantInsti

---

## 原文

Predicting Bank Nifty Open Price Using Deep Learning

With the advent of several machine / deep learning models, there have been several theories emerging in applying these techniques for stock market prediction because of the difficulty and complexity it involves. In this project, we’re trying to solve the problem using a classifier to predict whether the Bank Nifty index listed in NSE will go up or down, on the next day open using two Deep Learning models.

This article is the final project submitted by the authors as a part of their coursework in theExecutive Programme in Algorithmic Trading (EPAT®)at QuantInsti®. Do check ourProjects pageand have a look at what our students are building.

About the Author

Balamurugan Ganesanis a product professional with an MBA in Finance from SP Jain, B. Tech from NIT Calicut and completed CFA Level 3. He has around 11 years of experience as a Business Analyst / Product Manager with a proven track record in building products in the Fintech industry. Currently, he works as a Lead Analyst with Bank of America.

Under EPAT, he gained a solid understanding of various real-world implementation techniques in quantitative finance and high-frequency trading under the guidance of industry experts, practitioners and stalwarts in the domain of Algorithmic Trading.

He has extensively used the latest technologies in building products such as implementing deep learning models in tensorflow / keras, machine learning in Scikit Learn, statistical analysis tools using Python.

He is very passionate about the Algorithmic Trading domain where he can put all his skill sets to good use.

Project Abstract

This project looks at developing a deep learning model to predict the direction of the next day open price of BANK NIFTY index. I have considered two deep learning models for this project.

A deep learning model to predict the direction of the next day open price of BANK NIFTY based on 1 minute OHLC intraday data of the current day.

A deep learning model to predict the direction of the next day open price of the top 5 Bank Nifty constituents (by weight). The stocks considered are,

HDFC Bank

ICICI Bank

Axis Bank

Kotak Bank

State Bank of India

Based on the predictions of both the deep learning models, we can decide the strength of the model prediction for BANK NIFTY the next day.

If the BANK NIFTY model predicts an open price that is higher than the current close and the model for the individual stocks also predicts a higher open price, then we’ll consider it to be a strong buy signal and vice versa. We’ll only consider cases where both models predict the same direction for the following day.

We are trying to predict the open price in this project as best returns are made from the open price drift from the previous day’s close. Most of the times after a gap up / down opening the price starts to consolidate around the open price for the rest of the day.

Similar to returns, the risk of overnight positions are also higher compared to intraday positions. I also experimented with movements of all four prices (OHLC) based on the previous day close and got the best predictions for the ‘Open’ price.

The AUC score of the stock model was a commendable 83% and the index model was above 60%.From this project, we can understand that deep learning models can be used for predicting market movements and trends.

The project just showcases a framework to develop a deep learning model with good predictive capabilities given the data availability and technological constraints. With more training data and computational power, we can develop a robust model with very good predictive power.

Project Motivation

With the advent of several machine / deep learning models, there have been several theories emerging in applying these techniques forstock market predictionbecause of the difficulty and complexity it involves.

In this project, I’m trying to solve the problem using a classifier to predict whether the BANK NIFTY index will go up or down, on the next day open.

For this, I will be using a few technical indicators as features apart from the open, high, low, close and volume historical data to predict the individual stock prices of the index.

For the BANK NIFTY model, I’ll be using 1-minute intraday data of the previous day.

The deep learning models will use the historical data to detect non-linear patterns in the historical data and predict the next day open price for the index as well as the individual stocks of the index based on its learning from the training set.

Technical Setup

The project uses Python version 3.5.6

Other major libraries and database versions:

Tensorflow - 1.11.0

Keras - 2.2.4

Sklearn - 0.20.0

Talib- 0.4.17

Imblearn - 0.5.0

MySQL 8

Dataset used

For thestocks model, 20 years of daily OHLCV data of the stocks were used from 2000 January till 2019 September. Data till 2018 December was used for training/cross-validation and 2019 data was used as a test set.

Similarly for theindex model, 21 months of 1-minute intraday data for the first and last hour (9:16 to 10:15 AM and 2:30 to 3:30 PM) of BANK NIFTY from 2018 January till 2019 September was used. Data till 2019 April was used for training/cross-validation and the last 5 months of data were used as a test set.

Model implementation for Stocks

The widely used predictors for stock price forecasting have been technical indicators which are calculated using the daily price and volume data. Hence, I started developing the model using several of these indicators as features to check the predictive capability.

Next, I defined the target variable (y) that we’ll predict using this model. Since the problem has been framed as aclassificationproblem, I will define the target variable as a binary classifier. If the Open price on (t+1)thday is greater than Open price on tthday, then the target variable for tthday will be defined as ‘1’ else ‘0’.

After defining the target variable, I wanted to find the effectiveness of different features. To check the feature importance of each of these indicators, I first used an XGBClassifier for training the dataset and then utilize the Feature importance functionality of XGBClassifier to shortlist the important features.

Below is the code snippet used for extracting the important features using an XGBClassifier for HDFCBANK

I created my own MySQL database to store the daily and intraday data needed for this project. createFeatures is a custom function to create independent features.

After executing the above code snippet, we get an output as shown below.

By analyzing the confusion matrix, classification report, AUC score and Feature importance we can arrive at the optimum number of features with the good predictive capability and use them in our deep learning model. I had to spend a lot of time using trial and error to decide on the features to be used.

Finally, the following features were part of the Artificial Neural Network model

Different combinations of differences between OHLC data of the previous day

The following technical indicators

Momentum Indicators

1. ADX - The ADX indicates the market direction and whether a trend or momentum exists in the same direction. The values range from 0 to 100 and a higher number signifies a strong trend.

2. RSI - The Relative Strength calculates a ratio of the recent upward price movements to the absolute price movement. The RSI ranges from 0 to 100. The RSI is interpreted as an overbought/oversold indicator when the value is over 70/below 30.

3. CCI - The Commodity Channel Index measures the variation of a security's price from its statistical mean. The indicator is used to figure out overbought/oversold regions.

4. ROC - The ROC measures the percentage change in price between the current price and the price a certain number of periods ago. It is generally used to spot overbought/oversold conditions.

Volatility Indicators

1. ATR - Average true range indicates how much a stock moves on average, during a given time frame. The indicator can help in identifying levels to initiate a trade and also determine the stop loss levels for day traders.

2. Bollinger Bands - Bollinger Bands shows the levels of different highs and lows that a security price has reached in a particular duration and also its relative strength. The band widens (high volatility) and narrows (low volatility) depending on volatility.

Volume Indicators

1. ADOSC - The Chaikin A/D Oscillator is a volume indicator that associates changes in price and volume. The indicator is based on the premise that the more volume that accompanies a price move, the more significant the price move.

2. Force Index - The Force Index uses price and volume to assess the power behind a move or identify possible turning points.

Moving Averages

1. Simple Moving Average

2. Exponential Moving Average

Based on the above features the below Artificial Neural Network model is designed using Keras. Learn more about the applications and role ofneural network in tradingto enhance your skills.

Again, the hyperparameters like a number of hidden layers, hidden nodes, kernel initializers, optimizers and so on were finalized based on lots of trial and error.

The code snippet is given below, which runs for all the five stock symbols.

All the input features were scaled using StandardScaler to ensure they are all on the same scale. To avoid overfitting, the parameter validation split was used to utilize 30% of the training set for cross-validation while fitting the model.

A few callback functions of Keras was also used to save the best model and stop the training process if it doesn’t improve beyond a predefined threshold.

The below code snippet runs the model for all the five stocks.

Key Findings

The performance of the model was evaluated based on the confusion matrix, classification report and AUC score on the test dataset.

The results are given for all the five stocks below.

The model has achieved a pretty high AUC score of 83% and above for all the five stocks.

Model Implementation for Index

For BANK NIFTY, the first and last hour intraday OHLC data of the previous day was used from 09:16 to 10:15 AM and 2:30 to 3:30 PM to predict the next day open price of the index. No other additional features were used.

The next day open price was predicted using the model with different intraday time frames and found this combination to have good predictive power. I couldn’t go beyond 120 minutes for the features as the complexity and computational power requirement kept increasing as the timeframe increased.

The data was resampled using the below code snippet.

There was some data imbalance in the training data. The number of times the next day open price drifted higher was way higher than the number of times the next day the open price went lower as shown below.

This data imbalance might hamper the learning of the model. Hence, a method calledSMOTEwas used from the library imblearn to oversample the data and make the target classes equal in number.

All the input features were scaled using StandardScaler to ensure they are all on the same scale. Similar to the stock model, this model was finalized after several trial and error for the hyperparameters.

For this model,sgdoptimizer andhe_uniforminitializer seemed to work better. The model was trained using 16 months of intraday data (2018 January to 2019 April) and used 30% of the data for cross-validation to avoid overfitting. The code snippet for the model is shown below.

Similar callback functions of Keras like the previous model to save the best model and early stopping was used for the index model as well.

Key Findings

The performance of the model was evaluated based on the confusion matrix, classification report and AUC score similar to the above model on the test dataset from May 2019 to September 2019.

The AUC score comes around 60% for this model, which is quite decent for a self-trained model.

Combining both the models

We can now combine the predictive powers of both models to take our trading decisions. Since the stock model tries to predict the open price of the top five constituents of Bank nifty, the probability of prediction will be high if both the stock and index model predicts the same direction. This step has not been implemented in the current project.

Conclusion

From this project, we can understand that deep learning models can be used for predicting market movements and trends.

The project just showcases a framework to develop a basic model with good predictive capabilities given the data availability and technological constraints. With more training data and computational power, we can develop a robust model with very good predictive power.

The current model can be enhanced by using intraday 1-minute data for the individual stocks and BANK NIFTY from 9:15 AM to 3:15 PM (360 minutes) and take positions in the last 15 minutes of the current day based on the model prediction for the next day open in the index/stocks.

We can also try predicting the next day close price or range (high - low) and take trading decisions accordingly. For that, we’ll need more data and computational power.

If you want to learn various aspects of Algorithmic trading then check out theExecutive Programme in Algorithmic Trading (EPAT®).The course covers training modules like Statistics & Econometrics, Financial Computing & Technology, and Algorithmic & Quantitative Trading. EPAT equips you with the required skill sets to build a promising career in algorithmic trading.Enquire now!

Disclaimer: The information in this project is true and complete to the best of our Student’s knowledge. All recommendations are made without guarantee on the part of the student or QuantInsti®. The student and QuantInsti®disclaim any liability in connection with the use of this information. All content provided in this project is for informational purposes only and we do not guarantee that by using the guidance you will derive a certain profit.

Files in the download:

Data Processing

Stocks

Login to Download

---

*Imported from QuantInsti Blog on 2026-04-27*
