---
title: "Decision Tree Classifier For Trading Part-1"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/decision-tree-classifier-trading-part-1/"
date: "2017-10-31"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Decision Tree Classifier For Trading Part-1

**来源**: [QuantInsti](https://blog.quantinsti.com/decision-tree-classifier-trading-part-1/)  
**日期**: 2017-10-31  
**作者**: QuantInsti

---

## 原文

Decision Tree Classifier For Trading Part-1

ByVarun Divakar

The strategy in this blog will cover no normal technical indicators, but some of my own creation. Also, we will see the difference between strategy performance on test and train data along with respect to the changes in the size of the train data and the prediction length.

Unlike in my previous blogs, in here I will use a dynamic time frame to fetch data for the past few days. But before we begin, let us import the necessary libraries.

I have defined the starting date for the data to be pulled as the date 365 days/ 1 year in the past. You can use a static date format, but this will help you fetch the latest data whenever you run this code.

Next, I created a few indicators and changed the names of some columns to easily refer them to the code later.

I will briefly explain the indicators that I used. I have created a column called ‘dif’. This measures the change in the close price with respect to the change in yesterday’s range. We are trying to check if there is any correlation between today’s close with respect to the price volatility yesterday. After this, I have created a column called ‘sec_dif’, this is the second order difference of change in close prices. Here we measure the change in dif with respect to the change in yesterday’s range.

We also use another indicator called the diff_v which is used to measure the change in the range today compared to that of a day before.

After this, I calculated the market returns. Please note that these returns are forward-looking. As the prediction is generated at the end of the day or just before the close of the day, we can simply multiply the predicted trend with this returns and measure the strategy performance easily.

After creating the indicators, we calculate the returns and signal columns needed to measure the strategy performance and for training the algorithm respectively. We will use the prior day's returns as a part of the indicators, to see if there is any correlation between the trend for tomorrow and today’s market performance.

We scale the data after selecting our indicators, using the MinMaxScaler. This scaler function reduces the feature values to a range of 0 to 1.

Next, we decide the test data size, in this case, I chose 20 days which represents the last one month data.

After this, I have used adecision treeclassifier with increasing complexity, by adding more depth and features, to see how well the algorithm predicts with the help of thisdecision treeclassifier.

I will plot the performance of the strategy with increasing complexity (1-9, 9 being most complex) and also measure the accuracy of these algorithms.

There is no clear indication of any trend or how the algorithms have performed, in general, this result is very mixed. Now, let us print the train data performance and visualize the performance.

Here, the observations are very clear. You can clearly see that the more complex algorithms are doing a very good job at predicting the trend and the less complex ones are more like a coin toss. Given this train data, we could expect the most complex algorithm to perform better on the test data. But unfortunately, this is not the case. As you can see, the last 20 days performance in the above graph shows clearly that all the algorithms are almost equally bad. The reason for this is that we are not using the data available up until that point of the day to make the prediction. In other words, we are not making the prediction for last data by using an algorithm trained on entire data prior to that day, but we are assuming that the data of the past (365 days - 20 days) will have a similar trend as the next 20 days, which is mostly not the case. Let us verify this by decreasing the number of days to be predicted to just 5, then we can see a marked difference in the test data performance of the algorithms.

Here, you can see that the algorithms that are overfitting or underfitting the train data have done poorly and the algorithms that have the best learning have a consistent performance. Please note that you see only 4 out of 9 algorithms as most of them are overlapping. If you want to verify the accuracy of the strategy, you can print the code containing the accuracy again with new test data. Here, ideally, when one uses a time series data we need to use an LSTM type of approach to make predictions. That is use past ‘x’ days of data to train the algorithm and then predict for the next day. This would improve your accuracy considerably. We will look into this in my next blog.

Next Step

If you want to learn various aspects ofAlgorithmic tradingthen check out theExecutive Programme in Algorithmic Trading (EPAT™). The course covers training modules like Statistics & Econometrics, Financial Computing & Technology, and Algorithmic & Quantitative Trading. EPAT™ equips you with the required skill sets to be a successful trader.Enroll now!

Disclaimer:All investments and trading in the stock market involve risk. Any decisions to place trades in the financial markets, including trading in stock or options or other financial instruments is a personal decision that should only be made after thorough research, including a personal risk and financial assessment and the engagement of professional assistance to the extent you believe necessary. The trading strategies or related information mentioned in this article is for informational purposes only.

Download Python Code

Decision Tree Classifier Python Code

Login to Download

---

*Imported from QuantInsti Blog on 2026-04-27*
