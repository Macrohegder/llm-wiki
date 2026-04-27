---
title: "Machine Learning Logistic Regression: Python, Trading and more"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/machine-learning-logistic-regression-python/"
date: "2024-02-15"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Machine Learning Logistic Regression: Python, Trading and more

**来源**: [QuantInsti](https://blog.quantinsti.com/machine-learning-logistic-regression-python/)  
**日期**: 2024-02-15  
**作者**: QuantInsti

---

## 原文

Machine Learning Logistic Regression: Python, Trading and more

Imagine a world where you can predict market movements with uncanny accuracy, where gut feelings give way to data-driven insights, and where every trade is a calculated step towards profit. This, my friend, is the alluring promise of machine learning in trading.

Among the many algorithms vying for dominance in this arena, logistic regression stands out as a versatile and beginner-friendly tool. But how exactly does it work in the world of trading?

Think of Machine learning logistic regression as a binary classifier. It analyses mountains of historical data – prices, volumes, indicators – and learns to distinguish between two distinct outcomes: up or down. Delve into the intricacies of logistic regression in machine learning for trading as we harness its capabilities to forecast stock price movements using Python.

Integratingartificial intelligence in tradingallows us to enhance the logistic regression model further, enabling it to adapt and optimize its predictions based on evolving market conditions, ultimately leading to more informed trading decisions. To learn how to apply such models in live trading environments from scratch, analgo trading coursecovering machine learning and Python together is a great starting point.

This blog covers:

What is logistic regression?

Linear regression and logistic regression

Example of logistic regression in trading

Types of logistic regression

Logistic regression vs linear regression

Key assumptions while using logistic regression

Steps to use logistic regression

How to use logistic regression in Python for trading?

Challenges of logistic regression

Overcoming the challenges of logistic regression

Machine learning tasks generally bifurcate into two realms:

The expected outcome is defined

The expected outcome is not defined

The former characterised by input data paired with labelled outputs, is termed supervised learning. Conversely, when input data lacks labelled responses, that is, in the latter case, it's known as unsupervised learning. Explore the 'unsupervised learning course' from Quantra.

Additionally, there's reinforcement learning, which refines models through iterative feedback to enhance performance. Now, we explore Machine Learning Logistic Regression.

What is logistic regression?

Logistic regression falls under the category of supervised learning; it measures the relationship between the categorical dependent variable and one or more independent variables by estimating probabilities using a logistic/sigmoid function.

It is primarily used for binary classification problems where the outcome can take on only two possible categorical values, often denoted as 0 and 1. Some examples are, "success" or "failure", "spam" or "not spam", etc.

Despite the name ‘logistic regression’, this is not used formachine learning regressionproblems where the task is to predict the real-valued output. It is a classification problem which is used to predict a binary outcome (1/0, -1/1, True/False) given a set of independent variables.

Linear regression and logistic regression

Logistic regression is a bit similar to linearregression, or we can say it is a generalised linear model. In linear regression, we predict a real-valued output 'y' based on a weighted sum of input variables.

$$y=c + x_1*w_1 + x_2*w_2+ x_3*w_3 +........+ x_n*w_n$$

The aim of linear regression is to estimate values for the model coefficients c, w1, w2, w3 ….wn and fit the training data with minimal squared error and predict the output y.

Machine learning Logistic regression does the same thing but with one addition. The logistic regression model computes a weighted sum of the input variables similar to the linear regression, but it runs the result through a special non-linear function, the logistic function or sigmoid function to produce the output y. Here, the output is binary or in the form of 0/1 or -1/1.

$$y = logistic(c + x_1*w_1 + x_2*w_2+ x_3*w_3 +........+ x_n*w_n)$$

$$y = 1/1 + e[-(c + x_1*w_1 + x_2*w_2+ x_3*w_3 +........+ x_n*w_n)]$$

The sigmoid/logistic function is given by the following equation.

y = 1 / 1+ e-x

As you can see in the graph, it is an S-shaped curve that gets closer to 1 as the value of the input variable increases above 0 and gets closer to 0 as the input variable decreases below 0.

In the context of Machine learning logistic regression, the decision boundary is commonly set at 0.5, meaning that if the predicted probability is greater than 0.5, the outcome is classified as 1 (positive), and if it is less than 0.5, the outcome is classified as 0 (negative).

Now, let us consider the task ofpredicting the stock pricemovement. If tomorrow’s closing price is higher than today’s closing price, then we will buy the stock (1), else we will sell it (-1). If the output is 0.7, then we can say that there is a 70% chance that tomorrow’s closing price is higher than today’s closing price and classify it as 1.

Further, you can see this video below for learning about machine learning regression models.

Example of logistic regression in trading

Logistic regression can be used in trading to predict binary outcomes (stock price will “increase” or decrease”) or classify data based on predictor variables (technical indicators). Here's an example of how Machine learning logistic regression might be applied in a trading context:

Example: Predicting Stock Price Movement

Suppose a trader wants to predict whether a stock price will increase (1) or decrease (0) based on certain predictor variables or indicators. The trader collects historical data and selects the following predictor variables:

Moving Average Crossover:A binary variable indicating whether there was a recent crossover of the short-term moving average (e.g., 50-day MA) above the long-term moving average (e.g., 200-day MA) (1 = crossover occurred, 0 = no crossover).

Relative Strength Index (RSI): A continuous variable representing the RSI value, which measures the momentum of the stock (values range from 0 to 100).

Trading Volume: A continuous variable representing the trading volume of the stock, which may indicate the level of interest or activity in the stock.

The trader builds a logistic regression model using historical data, where the outcome variable is the binary indicator of whether the stock price increased (1) or decreased (0) on the next trading day.

After training the logistic regression model, the trader can use it to make predictions on new data. For example, if the model predicts a high probability of a stock price increase (p > 0.7) based on past or current data, the trader may decide to buy the stock.

Types of logistic regression

Logistic regression is a versatile statistical method that can be adapted to various types of classification problems. Depending on the nature of the outcome variable and the specific requirements of the analysis, different types of logistic regression models can be employed.

Here are some common types of logistic regression:

Binary Logistic Regression:This is the most basic form of logistic regression, where the outcome variable is binary and can take on two categorical values, such as "yes" or "no," "success" or "failure". These values are read as "1" or "0" by the machine learning model.

Hence, binary logistic regression is used to model the relationship between the predictor variables (RSI Indicator, MACD etc.) and the probability of the outcome being in a particular category (“increase” or “decrease” in stock price).

Multinomial Logistic Regression:In multinomial logistic regression, the outcome variable is categorical and can have more than two unordered categories. This type of logistic regression is suitable for modelling nominal outcome variables with three or more categories that do not have a natural ordering.

For example, classifying stocks into multiple categories such as "buy," "hold," or "sell" based on a set of predictor variables such as fundamental metrics, technical indicators, and market conditions.

Ordinal Logistic Regression:Ordinal logistic regression is used when the outcome variable is ordinal, meaning that it has a natural ordering but the intervals between the categories are not necessarily equal. Examples of ordinal variables include Likert scale ratings (e.g., "strongly disagree," "disagree," "neutral," "agree," "strongly agree"). Ordinal logistic regression models the cumulative probabilities of the outcome variable categories.

For example, analysing the ordinal outcome of trader sentiment or confidence levels (e.g., "low," "medium," "high") based on predictor variables such as market volatility, economic indicators, and news sentiment.

Multilevel Logistic Regression (or Hierarchical Logistic Regression):Multilevel logistic regression is used when the data has a hierarchical or nested structure, such as individuals nested within groups or clusters. This type of logistic regression accounts for the dependence or correlation among observations within the same cluster and allows for the estimation of both within-group and between-group effects.

For example, Modelling the binary outcome of stock price movements within different industry sectors (e.g., technology, healthcare, finance) while accounting for the hierarchical structure of the data (stocks nested within sectors).

Mixed-effects Logistic Regression:Mixed-effects logistic regression combines fixed effects (predictor variables that are the same for all observations) and random effects (predictor variables that vary across groups or clusters) in the model. This type of logistic regression is useful for analysing data with both individual-level and group-level predictors and accounting for the variability within and between groups.

For example, examining the binary outcome of stock price movements based on both individual-level predictors (such as company-specific factors, technical indicators) and group-level predictors (such as industry sector, market index etc.).

Regularised Logistic Regression:Regularised logistic regression, such as Lasso (L1 regularisation) or Ridge (L2 regularisation) logistic regression, incorporates regularisation techniques to prevent overfitting and improve the generalisability of the model. Regularisation adds a penalty term to the logistic regression model, which shrinks the coefficients of the predictor variables and selects the most important predictors.

For example, building a binary classification model to predict whether a stock is likely to outperform the market based on a large number of predictor variables while preventing overfitting and selecting the most important features.

Each type of logistic regression has its assumptions, advantages, and limitations, and the choice of the appropriate model depends on the nature of the data, the type of outcome variable, and the specific research or analytical objectives.

Difference between logistic regression and linear regression

Now, let us see the difference between logistic regression and linear regression.

Feature/Aspect

Linear Regression

Logistic Regression

Outcome Type

Continuous where the variable can take any value within a given range (e.g., daily stock price)

Binary or Categorical (e.g., Price is “Up” or “Down”)

Prediction

Value prediction. For example, stock price

Probability prediction For example, likelihood of an event

Relationship Assumption

Linear, that is, the dependent variable (such as predictive outcome) can be found out with the help of independent variables (such as past values). For example, on the basis of historical data, a trader can predict future prices of stock.

Log-Linear. For example, consider a situation where a quantity grows exponentially over time. A log-linear model would describe the relationship between the logarithm of the quantity and time as linear, implying that the quantity grows or decays at a constant rate on a logarithmic scale.

Model Output

Change in outcome per unit change in predictor

Change in log odds per unit change in predictor

Applications

Predicting in terms of amounts

Classifying in categories

In essence:

Linear Regression predicts a continuous outcome based on predictors.

Logistic Regression estimates the probability of a categorical outcome based on predictors.

Key assumptions while using logistic regression

Logistic regression, like other statistical methods, relies on several key assumptions to ensure the validity and reliability of the results. Here are some of the key assumptions underlying logistic regression:

Binary Outcome:Logistic regression is specifically designed for binary outcome variables, meaning that the outcome variable should have only two categorical outcomes (e.g., 0/1, Yes/No).

Linearity of Log Odds:The relationship between the predictor variables and the log odds of the outcome should be linear. This assumption means that the log odds of the outcome should change linearly with the predictor variables.

Independence of Observations:Each observation in the dataset should be independent of the other observations. This assumption ensures that the observations are not correlated or dependent on each other, which could bias the estimates and inflate the Type I error rate.

No Multicollinearity:The predictor variables in the model should not be highly correlated with each other, as multicollinearity can make it difficult to estimate the individual effects of the predictor variables on the outcome.

Large Sample Size:Logistic regression models perform better and provide more reliable estimates with a larger sample size (data values). While there is no strict rule for the minimum sample size, having a sufficiently large sample size ensures that the estimates are stable and the model has enough power to detect significant effects.

Correct Specification of Model:The logistic regression model should be correctly specified, meaning that all relevant predictor variables should be included in the model, and the functional form of the model should accurately reflect the underlying relationship between the predictor variables and the outcome.

Absence of Outliers:The presence of outliers in the dataset can influence the estimates and distort the results of the logistic regression model. It is essential to identify and handle outliers during data cleaning to ensure the robustness and validity of the model.

In summary, while logistic regression is a powerful and widely used method for modelling binary outcomes, it is crucial to ensure that the key assumptions of the model are met to obtain valid and reliable results. Violation of these assumptions can lead to biassed estimates, inaccurate predictions, and misleading conclusions, emphasising the importance of careful data preparation, model checking, and interpretation in logistic regression analysis.

Steps to use logistic regression in trading

Below are the steps that are used in logistic regression for trading.

Step 1 - Define the Problem:Identify what you want to predict or classify in trading, such as predicting whether a stock will go up or down based on certain factors.

Step 2 - Collect Data:Gather historical data on stocks, including predictor variables (e.g., trading volume, market index, volatility) and the binary outcome (e.g., stock went up = 1, stock went down = 0).

Step 3 - Preprocess the Data:Clean the data, handle missing values, and transform variables if needed (e.g., normalise trading volume).

Step 4 - Split the Data:Divide the dataset into training and test sets to train the model on one set and evaluate its performance on another.

Step 5 - Select Variables:Choose the predictor variables (independent variables) that you believe will help predict the outcome (dependent variable).

Step 6 - Build the Model:Use software or programming tools to build a logistic regression model with the selected variables and the binary outcome.

Step 7 - Train the Model:Train the logistic regression model on the training dataset, adjusting the model's parameters to minimise errors and fit the data.

Step 8 - Evaluate the Model:Test the trained model on the test dataset to evaluate its performance, using metrics such as accuracy, precision, recall, or the area under the ROC curve.

Step 9 - Interpret the Results:Interpret the coefficients and odds ratios in the logistic regression model to understand the relationships between the predictor variables and the probability of the outcome.

Step 10 - Make Predictions:Use the trained logistic regression model to make predictions on new data or real-time data in trading, such as predicting the likelihood of a stock going up or down based on current market conditions.

Step 11 - Monitor and Update:Continuously monitor the performance of the logistic regression model in real trading scenarios and update the model as needed with new data and insights.

How to use logistic regression in Python for trading?

Now that we know the basics behind logistic regression and the sigmoid function, let us go ahead. Now, we will learn how to implement logistic regression in Python and predict the stock price movement using the above condition.

This is how the Python code is used:

Step 1: Import Libraries

We will start by importing the necessary libraries such asTA-Lib.

Step 2: Import Data

We will import the AAPL data from 01-Jan-2005 to 30-Dec-2023. The data is imported from yahoo finance using ‘pandas_datareader’.

Output:

[*********************100%%**********************]  1 of 1 completed
Open	High	Low	Close	Adj Close	Volume
Date						
2023-12-22	195.179993	195.410004	192.970001	193.600006	193.600006	37122800
2023-12-26	193.610001	193.889999	192.830002	193.050003	193.050003	28919300
2023-12-27	192.490005	193.500000	191.089996	193.149994	193.149994	48087700
2023-12-28	194.139999	194.660004	193.169998	193.580002	193.580002	34049900
2023-12-29	193.899994	194.399994	191.729996	192.529999	192.529999	42628800

Let us print the top five rows of column‘Open’, ‘High’, ‘Low’, ‘Close’.

Step 3: Define Predictor/Independent Variables

We will use 10-days moving average,correlation, relative strength index (RSI), the difference between the open price of yesterday and today, the difference between the close price of yesterday and the open price of today. Also, open, high, low, and close prices will be used asindicators to make the prediction.

You can print and check all the predictor variables used to make astock price prediction.

Step 4: Define Target/Dependent Variable

The dependent variable is the same as discussed in the above example. If tomorrow’s closing price is higher than today’s closing price, then we will buy the stock (1), else we will sell it (-1).

Step 5: Split The Dataset

We will split the dataset into a training dataset and test dataset. We will use 70% of our data to train and the rest 30% to test. To do this, we will create a split variable which will divide the data frame in a 70-30 ratio. ‘Xtrain’ and ‘Ytrain’ are train dataset. ‘Xtest’ and ‘Ytest’ are the test dataset.

Step 6: Instantiate The Logistic Regression in Python

We will instantiate the logistic regression in Python using the ‘LogisticRegression’ function and fit the model on the training dataset using the ‘fit’ function.

Step 7: Examine The Coefficients

Output:

0	1
0	Open	[5.681225012480715e-18]
1	High	[5.686127781664772e-18]
2	Low	[5.6201381013603385e-18]
3	Close	[5.5831060987233e-18]
4	Adj Close	[5.0129246504381945e-18]
5	Volume	[9.71316227735615e-11]
6	S_10	[5.471752301907141e-18]
7	Corr	[3.1490350717776683e-19]
8	RSI	[3.646275382070163e-17]

Step 8: Calculate Class Probabilities

We will calculate the probabilities of the class for the test dataset using the ‘predict_proba’ function.

Output:

Output:
[[0.49653675 0.50346325]
 [0.49587905 0.50412095]
 [0.49479691 0.50520309]
 ...
 [0.49883229 0.50116771]
 [0.49917317 0.50082683]
 [0.49896485 0.50103515]]

Step 9: Predict Class Labels

Next, we will predict the class labels using the predict function for the test dataset.

Now, let us see what the prediction shows here.

Output:

[1 1 1 ... 1 1 1]

If you print the ‘predicted’ variable, you will observe that the classifier is predicting 1, when the probability in the second column of variable ‘probability’ is greater than 0.5. When the probability in the second column is less than 0.5, then the classifier will be predicting -1.

In the output above, the signal shows 1, which is a buy signal. But, for which dates did it predict 1?

Let us find out below.

Output:

Date(s) with Buy Signal(s):
2024-01-01
[1 1 1 ... 1 1 1]

Step 10: Evaluate The Model

Confusion Matrix

The Confusion matrix is used to describe the performance of the classification model on a set of test dataset for which the true values are known. We will calculate the confusion matrix using the ‘confusion_matrix’ function.

Output:

[[  0 665]
[  0 764]]

Classification Report

This is another method to examine the performance of the classification model.

print(metrics.classification_report(y_test, predicted))

Output:

precision    recall  f1-score   support

          -1       0.00      0.00      0.00       665
           1       0.53      1.00      0.70       764

    accuracy                           0.53      1429
   macro avg       0.27      0.50      0.35      1429
weighted avg       0.29      0.53      0.37      1429

The f1-score tells you the accuracy of the classifier in classifying the data points in that particular class compared to all other classes. It is calculated by taking the harmonic mean of precision and recall. The support is the number of samples of the true response that lies in that class.

The accuracy of the model is at 0.53 or 53%.

Step 11: Create Trading Strategy Using The Model

We will predict the signal to buy (1) or sell (-1) and calculate the cumulative Nifty 50 returns for the test dataset. Next, we will calculate the cumulative strategy return based on the signal predicted by the model in the test dataset. We will also plot the cumulative returns.

Output:

Challenges of logistic regression

Now, let us find out below which challenges can be faced while using logistic regression.

Model Complexity:Financial markets are complex and influenced by numerous factors, including economic conditions, geopolitical events, investor sentiment, and market dynamics. Logistic regression may not capture all the nonlinear relationships and interactions among variables, limiting its ability to model and predict market movements accurately.

Overfitting and Underfitting:Overfitting occurs when the logistic regression model is too complex and fits the training data too closely, capturing noise and random fluctuations rather than the underlying patterns. Underfitting, on the other hand, occurs when the model is too simple and fails to capture the relationships and variations in the data, leading to poor performance on both training and test datasets.

Imbalanced Data:In trading, the distribution of the outcome variable (e.g., stock price movements) may be imbalanced, with a disproportionate number of observations in one class (e.g., more instances of stock price increases than decreases). Imbalanced data can lead to biassed models that prioritise the majority class and perform poorly in predicting the minority class.

Dynamic Nature of Markets:Financial markets are dynamic and constantly evolving, with changing trends, volatility, and investor behaviour. Logistic regression models, which are trained on historical data, may not adapt quickly to new market conditions and may require frequent updates and recalibrations to maintain their predictive accuracy.

External Factors and Black Swan Events:Logistic regression models may not account for unexpected or rare events, such as black swan events, geopolitical crises, or sudden market shocks, which can have a significant impact on market movements and cannot be fully captured by historical data alone.

Overcoming the challenges of logistic regression

Here’s how you can overcome the challenges that arise while using logistic regression:

Model Complexity:Evaluate and refine model complexity using regularisation and feature selection.

Overfitting and Underfitting:Mitigate overfitting and underfitting through cross-validation and ensemble methods.

Data Quality and Availability:Invest in high-quality data and thorough preprocessing techniques.

Imbalanced Data:Address class imbalance with oversampling, undersampling, or alternative metrics.

Model Interpretability:Utilise model-agnostic tools for transparent and actionable insights.

Dynamic Nature of Markets:Continuously monitor and update models with evolving market data.

External Factors and Black Swan Events:Implement risk management strategies to mitigate unexpected events.

Also, you can check out this video below by Dr Thomas Starke (CEO, AAAQuants) in order to learn to use logistic regression more effectively in trading.

Conclusion

Logistic regression in trading offers a powerful tool for predicting binary outcomes, such as stock price movements, by leveraging historical data and key predictor variables. While logistic regression shares similarities with linear regression, it utilises a sigmoid function to estimate probabilities and classify outcomes into discrete categories.

However, traders must be mindful of its assumptions, potential challenges, and the dynamic nature of financial markets. By adhering to best practices, continuous monitoring, and incorporating risk management strategies, logistic regression can enhance decision-making processes and contribute to more informed and effective trading strategies.

Ready to revolutionise your algorithmic trading? Immerse yourself in Quantra's comprehensive learning track, "Machine Learning & Deep Learning in Trading - I."

With this learning track, you will find the uses of AI-powered market domination with the help of five expertly-crafted courses covering Introduction to ML for Trading, Data & Feature Engineering, Decision Trees, ML Classification and SVM, and Python Libraries for Algorithmic Trading.

Moreover, you will get an interactive learning environment with video lectures, quizzes, assignments, and hands-on coding exercises. That is not it. With each course, you will learn at your own pace from industry veterans, solidifying core ML concepts for application in financial markets for a successful trading journey!

File in the download

Machine Learning Logistic Regression in trading - Python notebook

Login to Download

Author:Chainika Thakar(Originally written ByVibhu Singh)

Note: The original post has been revamped on 15th February 2024, for the accuracy and recentness.

Disclaimer: All data and information provided in this article are for informational purposes only. QuantInsti®makes no representations as to accuracy, completeness, currentness, suitability, or validity of any information in this article and will not be liable for any errors, omissions, or delays in this information or any losses, injuries, or damages  arising from its display or use. All information is provided on an as-is basis.

---

*Imported from QuantInsti Blog on 2026-04-27*
