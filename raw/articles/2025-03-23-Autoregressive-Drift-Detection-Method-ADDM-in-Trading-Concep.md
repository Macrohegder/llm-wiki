---
title: "Autoregressive Drift Detection Method (ADDM) in Trading: Concept Drift, Market Regimes, and Strategy"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/autoregressive-drift-detection-method/"
date: "2025-03-23"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Autoregressive Drift Detection Method (ADDM) in Trading: Concept Drift, Market Regimes, and Strategy

**来源**: [QuantInsti](https://blog.quantinsti.com/autoregressive-drift-detection-method/)  
**日期**: 2025-03-23  
**作者**: QuantInsti

---

## 原文

A novel drift detection algorithm for machine learning in trading

ByJosé Carlos Gonzáles Tanaka

Imagine yourself, a great retail trader with an algorithm that flawlessly predicts stock movements for months—until a surprise Fed rate hike sends markets into chaos. Overnight, the model’s accuracy plummets. Why? Concept drift: your model no longer finds patterns in historical data and now underperforms its predictions. For machine-learning-based traders, this is a latent enemy.

But, what if you could detect these shifts in real time and adapt instantly?

Enter ADDM (Autoregressive Drift Detection Method), a game-changing algorithm that turns regime changes into opportunity.

In this guide, we’ll unpack how ADDM works, why it outperforms well-known models, and how traders can harness it to stay ahead of unpredictable markets.

Prerequisites

Since this blog focuses on a machine learning concept applied to model drift detection, it is crucial to start with foundational concepts in machine learning, regression analysis, and time series econometrics. Begin withMachine Learning Basics: Components, Application, Resources, and Moreto understand the fundamental aspects of machine learning. Then, move on toMachine Learning for Algorithmic Trading in Python: A Complete Guideto see how ML models are applied in financial markets.

Understanding regression is essential for modeling relationships in financial data. ExploreExploring Linear Regression Analysis in Finance and Tradingto grasp how regression-based predictive models work, followed byLinear Regression: Assumptions and Limitations, which discusses common pitfalls related to bias and variance in model performance.

Since this blog deals with model drift detection using the SETAR econometric model, it is helpful to study theAutoregressive Moving Average (ARMA/ARIMA) modelto understand how time series models handle dependencies over time. In our blog, we use an R script called from Python, to learn in detail about how to do that, please check this blog AutoRegressive Fractionally Integrated Moving Average (ARFIMA) model.Additionally, decision trees and ensemble learning techniques such as random forests are commonly used in machine learning applications for financial forecasting. The blogsRandom Forest Algorithm in PythonandPredicting Stock Trends with Technical Analysis and Random Forestswill provide insights into how these models can be leveraged in financial trading.

This blog covers:

What is Concept Drift? The Hidden Challenge in Trading

How the ADDM algorithm works

ADDM in Action: A Step-by-Step Workflow

A backtesting trading ML strategy with the ADDM algorithm

What is Concept Drift? The Hidden Challenge in Trading

According to the literature, concept drift refers to situations where the underlying distribution of a predictive target (variable y) evolves over time. This occurs because the processes generating the input features (X) also transform, causing the original patterns captured by machine learning models to lose relevance as data distributions shift gradually. Seasonal trends, emerging trends, or unforeseen events can trigger such shifts.

The research paper categorizes concept drift into three primary types:

Virtual drift: A change occurs in the input feature distribution (X), but the predictive relationship between X and target y remains consistent. This form typically doesn't degrade model performance.

Actual drift: The input data distribution (X) remains stable, but the underlying pattern between X and the prediction feature y changes.

Mixed drift: A combination where both input distributions (X) and the X-to-y relationship undergo shifts simultaneously.

Regardless of type, concept drift poses challenges by degrading model accuracy as historical training data becomes less representative of current realities. When data patterns change, models built on past information struggle to make reliable predictions on new data. This underscores the necessity for continuous drift detection and model adaptation strategies, such as those implemented in frameworks like the ADDM algorithm. ADDM solves this by acting as a "guardian" that monitors and adapts to change.

How the ADDM algorithm works

The algorithm is based on the paper written byZoubeirou and Riveill (2023).

You have two models in this algorithm:

A Predictive Model: Your existing trading algorithm (e.g., LSTM for crypto, random forest for equities, support vector machine for forex, etc.).

A SETAR Model: A regime-switching time-series tool that acts as ADDM’s "alarm system."

What’s the secret weapon?: The SETAR (Self-Exciting Threshold Autoregressive Model).

SETAR analyzes your model’s prediction errors to identify regime changes—moments when ML model underperforms compared to past performance. Here’s how it works:

Regimes: SETAR divides the model’s errors into two distinct states separated by an error “threshold.” The SETAR model is an Autoregressive model with, for example, one AR lag for each regime, so it’s like having two AR models, each with its distinct coefficient values.

Thresholds: When errors cross the predefined threshold (e.g., sudden spikes), SETAR triggers a regime switch, signaling concept drift. However, you shouldn’t take the last error of the model’s error time series to analyze this drift detection. You must use a specific past value (a lag) of the model’s error time series to detect the model drift.

Example: A Bitcoin trading bot performs well in a bull market (Regime 1: errors = 2–5%). After a crypto regulation scare, errors jump to 15% (Regime 2). SETAR detects this threshold breach, alerting the trader, and thus, you need to train a new model.

ADDM in Action: A Step-by-Step Workflow

Let’s break down ADDM’s algorithm, optimized for trading. We’re going to use a span example so it can be better understood:

Input: It starts with your initial training data (Dtr: historical data up to 2017), some data to check the model's initial performance (Dval: historical data from the last 4 months of 2018), and the stream of new market data coming in (Ds: historical data from 2019 up to 2025).

Train your ML model: First, you train your initial trading model (M0) using the historical training data (Dtr) and validate it with Dval to ensure it works reasonably well initially.

Compute validation error: You then calculate how well this initial model performs on the validation data (epsilon_val). This gives you a baseline of the model's error rate in a stable period.

Fix a time window w: The algorithm sets a window of recent data (w) to detect changes. Think of it as focusing on the most recent market activity. Repeat the following tasks each day. This means the steps will continue as long as new market data is available. Once the time window is set, loop the following:

Receive incoming data instances: The algorithm gets a new batch of recent market data (X(t−w)) within the defined window.

Predict values: Your current trading model (M0) makes predictions (ŷt−w) on this new market data.

Compute the model’s error time series: Calculate the difference between these predictions and the actual market outcomes (yt−w). This gives you the error rate of your model on the recent data (epsilon_(t−w)).

Learn the Setar model with epsilon_(t−w) ∪ (epsilon_val): This method takes the history of these recent errors (epsilon_(t−w)) along with the initial validation errors (epsilon_val) and uses them to train the SETAR model. As we discussed, the SETAR model is like a detective for changes in the pattern of these errors.

The SETAR model looks for significant changes in the error rate pattern. It triggers the following steps if it detects a change (a concept drift).Compute drift severity: If a drift is detected, the algorithm calculates how severe the change is (wt) by comparing the error rates in the old and new periods. It uses the third quantile (Q3) of the error rates to do this, which allows it to get a reasonable estimate of the typical error without being too affected by extreme mistakes.Get the most recent labeled data D_recent: The algorithm gathers the most recent market data for which you have the actual outcomes (labels). It will use this new data to adapt the model.Train a new model M_new: It trains a new trading ML model (M_new) using only this most recent data (D_recent). This new model learns the patterns in the changed market conditions.M_updated =M0 * (1− wt) + wt*M_new: The adaptation happens here. The algorithm updates your main trading model (M_updated) by combining the old model (M0) and the new model (M_new). The severity of the drift (wt) determines how much weight is given to the new model. If the drift is severe, the new model gets more importance; if it is less severe, the old model still has a significant influence.

Compute drift severity: If a drift is detected, the algorithm calculates how severe the change is (wt) by comparing the error rates in the old and new periods. It uses the third quantile (Q3) of the error rates to do this, which allows it to get a reasonable estimate of the typical error without being too affected by extreme mistakes.Get the most recent labeled data D_recent: The algorithm gathers the most recent market data for which you have the actual outcomes (labels). It will use this new data to adapt the model.Train a new model M_new: It trains a new trading ML model (M_new) using only this most recent data (D_recent). This new model learns the patterns in the changed market conditions.M_updated =M0 * (1− wt) + wt*M_new: The adaptation happens here. The algorithm updates your main trading model (M_updated) by combining the old model (M0) and the new model (M_new). The severity of the drift (wt) determines how much weight is given to the new model. If the drift is severe, the new model gets more importance; if it is less severe, the old model still has a significant influence.

Compute drift severity: If a drift is detected, the algorithm calculates how severe the change is (wt) by comparing the error rates in the old and new periods. It uses the third quantile (Q3) of the error rates to do this, which allows it to get a reasonable estimate of the typical error without being too affected by extreme mistakes.

Get the most recent labeled data D_recent: The algorithm gathers the most recent market data for which you have the actual outcomes (labels). It will use this new data to adapt the model.

Train a new model M_new: It trains a new trading ML model (M_new) using only this most recent data (D_recent). This new model learns the patterns in the changed market conditions.

M_updated =M0 * (1− wt) + wt*M_new: The adaptation happens here. The algorithm updates your main trading model (M_updated) by combining the old model (M0) and the new model (M_new). The severity of the drift (wt) determines how much weight is given to the new model. If the drift is severe, the new model gets more importance; if it is less severe, the old model still has a significant influence.

5.repeat: The entire step-4 process repeats as long as there is a stream of new market data (Ds). This ensures that your trading model continuously monitors for changes and adapts as needed.

Essentially, the ADDM algorithm watches how well your trading ML model is performing. If it notices a significant change in its performance (indicating a shift in the model’s data distribution), it learns from the recent market behavior and updates your model to keep it aligned with the new conditions.

Why would you love ADDM: 5 ways of using the algorithm

Precision Timing: ADDM detects drifts early, giving traders hours (or days) to adjust strategies before losses compound.

Fewer False Alarms: According to the paper, the SETAR’s threshold-based logic ignores minor noise, avoiding unnecessary retraining.

Seamless Adaptation: By blending old and new models, ADDM preserves proven strategies while integrating new insights.

Universal Compatibility: Works with any model type: neural networks, regression, or even rule-based systems.

Automated Resilience: Integrate ADDM into trading bots for 24/7 drift detection and adaptation.

A backtesting trading ML strategy with the ADDM algorithm

We’re going to compare 2 strategies:

A daily-trained ML-based strategy without a drift detection algorithm.

An ML-based strategy with the ADDM algorithm to detect model drift.

A buy-&-hold strategy will be output as a third reference.

In this algorithm, we need to run a SETAR model. We don’t have any Python library that has this model. But we have it in R, but we also want to use Python, but we don’t want to run the whole backtesting script in R, but…

Don’t worry my friend!

We got you covered!

In my  ARFIMAarticle, I describe how to call an R script from Python. We will follow the same approach and run the SETAR model in an R script. This R script will

Import the model’s error time series dataframe

Estimate a SETAR model based on the above data.

Save the regime found with the above model in the same dataframe.

Save the dataframe in the same data address.

Set 5 as the number of lags each AR model will have for each regime.

Set 2 as the threshold delay (model’s error time series lag) to be compared to model’s error threshold to detect a regime change. The threshold separates each AR model in the SETAR model. In the model’s error time series, each error observation will be above or below that threshold. If the error observation is below the threshold, then we say that on that day the model’s error is, say, in regime 1, if it’s above, we say the model’s error is in regime 2. In this case, we use the second lag of the model’s error time series to compare it to the threshold to detect a regime shift. That’s how the SETAR model works.

Set nthresh to 1. This means there is only one threshold, which means we have only 2 regimes. If we set it to 2, it would mean we have 3 regimes, and so on. For the ADDM algorith, 2 regimes are enough.

The code is the following:

Let’s see below how this code will be plugged into the Python code. The Python code will be the only script to be run by you. So you don’t need to worry about running the R script. The Python code will do it for you.

Let’s do it!

First we important the libraries

Now, we define a class for the ADDM algorithm:

The class can be summarized as follows:

1. __init__(...):

Sets up the drift detector with its core tools:

Stores the machine learning model (e.g., Random Forest)

Defines settings like:error window size: The window size to be used to update each day the new data stream. Each day we use the last window-size observations as a new data stream. We discard the rest.retraining size: the window size to be used as the number of data observations to retrain the new model. We use the most recent data as per this retraining size.validation size: the number of observations to be used to train the SETAR model. This validation size and the error window size make the total number of observations for the SETAR model training.

error window size: The window size to be used to update each day the new data stream. Each day we use the last window-size observations as a new data stream. We discard the rest.retraining size: the window size to be used as the number of data observations to retrain the new model. We use the most recent data as per this retraining size.validation size: the number of observations to be used to train the SETAR model. This validation size and the error window size make the total number of observations for the SETAR model training.

error window size: The window size to be used to update each day the new data stream. Each day we use the last window-size observations as a new data stream. We discard the rest.

retraining size: the window size to be used as the number of data observations to retrain the new model. We use the most recent data as per this retraining size.

validation size: the number of observations to be used to train the SETAR model. This validation size and the error window size make the total number of observations for the SETAR model training.

Prepares empty containers for tracking errors and recent data

2. initialize(X_train, y_train):

Trains the initial model on historical data (e.g., 2015–2018 stock data)

Calculates the model’s starting error rate (smoothed over time)

Saves recent training data in a "memory bank" for future retraining

3. process_stream(X_stream, y_stream):

Predicts: Uses the current model to guess the next day’s price direction

Tracks Errors: Checks if the prediction was wrong and updates a smoothed error rate

Saves Data: Keeps a rolling window of the latest 500 data points

Detects Changes:

Writes errors to an Excel file and runs the above R script to output the regime found from the SETAR model

If a regime change is found (e.g., market behavior suddenly changes), triggers a model update

Saves Results: Stores predictions and drift flags in a spreadsheet

4.  _calculate_severity():

Compares recent errors to past errors

Measures how "bad" the drift is by comparing error spreads (75th percentile of old vs. new errors)

5. _update_model():

Retrains the model using the most recent 500 data points

Replaces the old model with the newly trained version

6. _smooth_errors(errors):

Turns binary daily errors (0s and 1s) into a smoother average (like a 10-day moving average).

Makes it easier to spot trends instead of binary outcomes.

Then,  we do data preparation & target creation

Download historical Microsoft stock data (OHLC prices) from 2015-2025

Create features using percentage price changes

Define target variable (y) as binary indicator: 1 if next day's close price increases, 0 otherwise

Next, we initialize the model training

Split data into training period (2015-2018) and streaming period (2019+)

Initialize Random Forest classifier with fixed hyperparameters:Set 5 as the number of AR lags for the SETAR model.Set d as 2 which is the error lag to be compared to the error threshold defined by the model. If the

Set 5 as the number of AR lags for the SETAR model.

Set d as 2 which is the error lag to be compared to the error threshold defined by the model. If the

Train initial model on pre-2019 data

We’re close! Now, we do the backtesting for the ML-and-ADDM-based trading strategy as described in the section where we described the workflow:

We’re getting closer… do not hurry to see below, wait!

We do the benchmark strategy comparison. Here, we backtest an ML-based trading strategy and train the model daily. Its performance will serve us to analyze the advantages and disadvantages of the ADDM-based strategy:

Implement daily retraining baseline:For each trading day, train a new RF model on the previous 1000 daysMake a prediction for the next day

For each trading day, train a new RF model on the previous 1000 days

Make a prediction for the next day

Wait for it, be patient! Let’s do now performance measurement

Calculate daily returns for each strategy:

ADDM uses predictions from drift-adaptive model

Daily strategy uses latest RF model predictions

Buy-and-hold tracks raw price changes

2. Compute cumulative returns for comparison:

Compound returns over time for each approach

Enables visual/metric-based performance evaluation

Finally! Let’s plot all we need to see graphically!

First, let’s plot the regime changes detected through the entire data stream span:

We can see many regime changes, but there are periods when we don’t need to retrain the ML model.

Let’s plot now the 3 cumulative returns.

We get to see something quite interesting: The ADDM performs poorer compared to the daily-trained strategy up to 2020, but it performs the best onwards.

Let’s have a closer look focusing on both cumulative returns:

Indeed, we are experiencing the above situation. Let’s see how the 3 cumulative returns behaved with a pyfolio function:

Let’s put the results in a single table:

To sum up, the buy-and-hold strategy performs the best regarding the annual return. However, the ADDM-based strategy is close to the buy-and-hold annual and cumulative returns. It has the lowest volatility and the best Sharpe ratio. The max drawdown of the buy-and-hold is the highest, and the ADDM-based strategy has the lowest. The daily-trained algorithm has the worst drawdown. Finally, the ADDM-based strategy has the highest Sortino ratio, i.e., it has the highest downside protection.

The conclusion is clear: You don’t need to fit the model daily, you can actually retrain it as per when the ADDM algorithm tells you to do it.

Notes to tweak the ADDM algorithm:

You can change the number of lags and the threshold delay in the R script. I set them to 5 and 2 because I followed the paper’s recommendation.

You can change the ADDMClassifier object hyperparameters to improve its strategy performance.

You can incorporate risk management to improve the performance of the ADDM-based strategy.

The features of the random forest algorithm are too simple. You need to improve them to improve the model’s performance. We leave you that as an exercise.

Conclusion

Concept drift is an ever-present threat in algorithmic trading, where shifting market dynamics can render once-reliable models obsolete. The ADDM algorithm emerges as a powerful solution, combining SETAR-based regime detection with dynamic model adaptation to sort these changes effectively out.

While no algorithm guarantees perpetual success, ADDM transforms concept drift from a hidden threat into a measurable risk factor. Maintaining model relevance through market regime changes enables you to pursue alpha generation with controlled risk exposure. Please remember, it’s not only about returns, it’s also about preserving capital!

You want to learn the basics? Please check our Quantra Learning Track onAlgorithmic Trading for Beginners.

You want to learn advanced stuff? Please check our Quantra Learning Track onAdvanced Algorithmic Trading Strategies.

Don’t hesitate to contact us if you have any questions.

See you next time!

Reference

Mansour Zoubeirou A Mayaki, Michel Riveill. Autoregressive based Drift Detection Method. IEEE, WCCI (2022) - IEEE world congress on computational intelligenceWORLD CONGRESS ON COMPUTATIONAL INTELLIGENCE, Jul 2022, Padoue, Italy. pp.1-8, ff10.1109/IJCNN55064.2022.9892066ff. ffhal-03740180f

Next steps

The model drift detection algorithm proposed in this blog can be used for any trading strategy with a machine-learning algorithm as a signal-generation model where you feel you don’t need to train it so frequently. Do not forget to use this detection algorithm whenever possible if you consider it appropriate.

Once you have built a strong foundation, dive deeper into machine learning applications in trading. TheMachine Learning & Deep Learning in Tradinglearning track covers essential topics, including data preprocessing, predictive modeling, and AI model optimization, helping you implement classification and regression techniques in financial markets.

For a structured, step-by-step implementation of regression models in trading, considerTrading with Machine Learning: Regression, which guides you through data acquisition, model training, testing, and stock price prediction.

For those looking for an advanced, structured approach to quantitative trading and machine learning, theExecutive Programme in Algorithmic Trading (EPAT)is an excellent choice. This program covers classical ML algorithms (such as SVM, k-means clustering, decision trees, and random forests), deep learning fundamentals (including neural networks and gradient descent), and Python-based strategy development. You will also explore statistical arbitrage using PCA, alternative data sources, and reinforcement learning applied to trading.

Once you have mastered these concepts, you can apply your knowledge in real-world trading using 2 options:

Blueshift. Blueshift is an all-in-one automated trading platform that offers institutional-grade infrastructure for investment research, backtesting, and algorithmic trading. It is a fast, flexible, and reliable platform, agnostic to asset class and trading style, helping you turn your ideas into investment-worthy opportunities.

In case you want to trade forex algorithmically, you can also have thisoption. It’s a ready-made setup to trade forex algorithmically using the Interactive Brokers Python API. It is easy-to-tweak and easy-to-use trading setup where you can modify the existing strategy to implement yours easily.

By following this structured learning path, you will gain expertise in econometric modelling, machine learning-based trading, and model drift detection, allowing you to effectively apply the SETAR-based model drift detection algorithm in financial markets.

File in the download:

ADDM algorithm - Python notebook

The Python code script implementing the ADDM algorithm in a backtesting loop is provided as ADDM_algorithm.ipynb

SETAR - R

The R code script used by the ADDM algorithm to detect the regime changes is provided as SETAR.R

Feel free to make changes to the code as per your comfort.

Login to Download

All investments and trading in the stock market involve risk. Any decision to place trades in the financial markets, including trading in stock or options or other financial instruments is a personal decision that should only be made after thorough research, including a personal risk and financial assessment and the engagement of professional assistance to the extent you believe necessary. The trading strategies or related information mentioned in this article is for informational purposes only.

---

*Imported from QuantInsti Blog on 2026-04-27*
