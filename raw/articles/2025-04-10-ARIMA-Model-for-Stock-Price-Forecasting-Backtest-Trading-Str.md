---
title: "ARIMA Model for Stock Price Forecasting | Backtest Trading Strategies with Python"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/forecasting-stock-returns-using-arima-model/"
date: "2025-04-10"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# ARIMA Model for Stock Price Forecasting | Backtest Trading Strategies with Python

**来源**: [QuantInsti](https://blog.quantinsti.com/forecasting-stock-returns-using-arima-model/)  
**日期**: 2025-04-10  
**作者**: QuantInsti

---

## 原文

Forecasting Stock Prices Using ARIMA Model

ByJosé Carlos Gonzáles Tanaka

Prerequisites

This blog is a hands-on tutorial that walks you through the math behind the ARIMA model and how to implement it as a backtesting strategy for stock trading. You'll not only learn how to apply ARIMA models but also how to enhance your results with advanced concepts and references.

To get the most out of this blog, it’s essential to build a strong understanding of time series fundamentals. Start withIntroduction to Time Seriesto learn the core concepts such as trend analysis, seasonality, and autocorrelation. If you’re exploring alternatives to traditional statistical methods, you may findTime Series vs LSTM Modelshelpful—it compares time series models with deep learning-based forecasting.

ARIMA is the same as ARMA models. The difference lies in how you treat the time series to be modeled. Learn the theoretical aspects of these models in thisARMA model guide. These models require stationarity, go throughStationarityto learn how to convert non-stationary time series into usable form. Complement this withThe Hurst Exponentto evaluate long-term memory in data, andMean Reversion in Time Seriesto understand one of the underlying principles many time series models rely on.

Next, level up with more advanced topics. Learn multivariate time series modeling withVector Autoregression (VAR), explore asset relationships withJohansen Cointegration, and dive into time-varying parameters and multivariate forecasting withTime-Varying-Parameter VAR. For implementation,  a working knowledge of essential Python libraries is extremely helpful. If you're new to data analysis in Python or want to sharpen your skills, begin by exploring thePython Trading Libraryblog, which introduces you to tools specifically designed for financial applications. To handle and manipulate structured data efficiently, dive into thePython Pandas Tutorial, which covers the DataFrame structure, slicing, filtering, and time series-specific functions. For numerical computations, especially arrays and vectorized operations commonly used in forecasting models, theNumPy Tutorialoffers a practical guide. Finally, to visualize trends, model forecasts, and backtesting results, refer to theMatplotlib Tutorial, which teaches you how to create plots that communicate your findings clearly and effectively. Together, these resources provide a strong Python foundation for building and deploying ARIMA-based trading models.

Also, don’t forget to brush up onBacktesting basics—an essential skill when applying ARIMA for trading strategy validation.

Stock market forecasting has always been a subject of great interest for investors, analysts, and traders seeking to make informed investment decisions. One of the popular methods employed in time series analysis is the Autoregressive Integrated Moving Average (ARIMA) model. With its ability to capture trends, seasonality, and stationary behaviour, the model has proven to be a powerful tool for forecasting stock returns.

This blog will explore this widely used model forecasting model and how it can be applied to forecast stock returns. It will also take you through a detailed step-by-step procedure for implementing the model as a strategy using Python.

The ARIMA (Autoregressive Integrated Moving Average) model is handy for analysing and predicting sequential data.

It combines three important elements:

AutoRegressive (AR): It means we use the lag of the time series to be modeled as variables.

Differencing (I or Integrated): It is the order of integration of the time series to be modeled, and

Moving average (MA): It means we take the lagged values of the error term of the regression to model the time series.

All the concepts covered in this blog are taken from this Quantra learning track onFinancial time series analysis for trading. You can take aFree Previewof the course by clicking on the green-coloured Free Preview button.

Let us learn more about ARIMA model and forecasting stock prices using this model with this blog that covers:

What is ARIMA model?

Relevance of using the model with time series data in trading

Pros of using the model in trading

Cons of using the model in trading

How to use the model to forecast and trade stocks in Python?

Notes to take your model to the next level

What is ARIMA model?

ARIMA(p,d,q) stands for Autoregressive Integrated Moving Average. It’s an econometric model fitted to a specific univariate time series. This means we apply this model to a single time series model. Whenever we apply an econometric model to more than one time series, we say this model is multivariate. This model can be mathematically written as

WhereYtis the differenced time series value,φ1,φ2, ...,φprepresent the coefficients of the autoregressive component, andθ1,θ2, ...,θqrepresent the coefficients of the lagged error variables. All these coefficients are unknown parameters and are found through the model’s estimation.

Theεterms are assumed to be independent, identically distributed error terms with zero mean.

Here,Ytis expressed in terms of its past values (a total ofpautoregressive components of the model) and the current and past values of error terms (a total ofqmoving average components).

There’s something called the “Box-Jenkins” methodology, where we find the p, d, and q values by checking the plots of the autocorrelation and partial-autocorrelation functions. This process is done manually, and we cannot do it algorithmically. Here, we provide an algorithm-based methodology to find the correct values.

Step 1: Testing and Ensuring Stationarity

The series has to be stationary to fit the model to atime series. A stationary time series is a time series without trend, with a constant mean and variance over time, making it easy to predict values.

Finding the order of integration– We apply the differencing method to convert a non-stationary process to a stationary process until we find the order of integration. Differencing a time series means finding the differences between consecutive values of a time series data. The differenced values are then used to fit the model to uncover new correlations or other interesting statistical properties.

We can apply the unit root test sequentially to find the correct order of integration. This is how the algorithm works:

We apply the ADF test to the price series in levels:

If the p-value is less than 5%, then the prices in levels are stationary. This means the prices in levels are I(0), i.e., the order of integration of the prices in levels is zero.

If the p-value is higher than 5%, then prices are not stationary. So we proceed to first-difference the prices and continue with the following:

We apply the ADF test to the first difference of the price series:

If the p-value is less than 5%, the first difference is stationary. This means the prices in levels are I(1) and the first difference of the prices is I(0). This means we need to difference the prices 1 time to make them stationary.

If the p-value is higher than 5%, then the first difference is not stationary. So we proceed to second-difference the prices and continue with the following:

We apply the ADF test to the second difference of the price series:

If the p-value is less than 5%, the second difference is stationary. This means the prices in levels are I(2), the first difference of the prices is I(1) and the second difference of the prices is (0). This means we need to difference the prices 2 times to make them stationary.

If the p-value is higher than 5%, then the second difference is not stationary. So we proceed to third-difference the prices and continue with the following:

We apply the ADF test to the third difference of the price series and so on until we find stationarity.

Hence, we can make the following conclusion:

The price time series is I(d) if we need to difference the prices “d” times to make them stationary.

Step 2: Identification of p and q

In this step, we identify the appropriate order of Autoregressive (AR) and Moving average (MA) processes by using theAutocorrelation function (ACF) and Partial Autocorrelation function(PACF).

Once we know the order of integration of the price series, called “d”, we create an algorithm to find the best p and q values.

How do we do that?

Well, we estimate multiple ARIMA models with different values of p and q and choose the model with the lowest Akaike Information Criterion (AIC). This will be the best model, and its p and q values will be the best parameters.

Step 3: Estimation and Forecasting

Once we have determined the parameters (p,d,q), we use the best model to forecast the next-period price so we can use it to get a long or short signal.

Relevance of using ARIMA model with time series data in trading

Autoregressive Integrated Moving Average models have several applications in trading and financial markets. Here's how the model is utilised in trading:

Stock price forecasting

Traders and investors often rely on econometric models to forecast stock prices or returns. These predictions aid decision-making processes for buying, selling, or holding stocks.

Volatility modelling and risk management

This type of model is valuable for modelling and predicting market returns. If we estimate a GARCHmodelfor the ARIMA model’s returns, we can forecast volatility, manage risk properly, price options, and optimize trading strategies.

GARCH models can contribute to effective risk management strategies by estimating measures such as portfolio value at risk (VaR) or expected shortfall (ES). These measures assist traders in assessing and mitigating potential losses in different market scenarios.

Market analysis

With this model, you can analyse historical market data, unveiling trends, cycles, and seasonality. These insights inform decision-making regarding optimal entry or exit points in the market.

Pros of using the model in trading

Captures Time-dependent Patterns:The model effectively captures autocorrelation-based patterns of the dependent variable, its lagged values, and the model’s lagged errors.

Proven Methodology:The model is a well-established and widely used modelling technique in time series analysis with a solid foundation in statistics. It has been successfully applied in various domains, including trading.

Interpretability:These type of models provide interpretable results, allowing traders to understand the relationship between past and future price movements and make informed decisions based on the model's coefficients and statistical measures.

Cons of using the model in trading

Limited Complexity:These models assume linear relationships and may struggle to capture complex or non-linear patterns in financial markets. They might not fully capture sudden changes or rare events that can significantly impact prices.

Data Quality and Assumptions:The models require high-quality data and rely on assumptions such as stationarity. Violations of this assumption can affect the model's accuracy and reliability.

Short-term Focus:These models are better suited for short-term forecasting rather than long-term predictions. They may struggle to capture longer-term trends or shifts in market dynamics.

How to use the model to forecast and trade stocks in Python?

Let us see the steps for using the model with time series data in the popularPython programming language.

Step 1: Import the required libraries

Import pandas, numpy, matplotlib, itertools and statsmodels modules.

Step 2: Load and prepare the data

Import the adjusted Apple stock data from 1990 to April 2025.

Subset the data so that we only use the Close data.

Compute the Close-to-Close returns

Step 3: Build 2 functions for the event-driven backtesting loop

Find_integration_order: This function will allow us to get the order of integration for each time we fit the model. The algorithm works the same as explained above.

Select_arima_order: This function will get for us the best model as per the AIC, as explained above. We estimate multiple models, ranging p and q from 0 to 6 (without estimating an ARIMA(0,d,0) because that would be a random process), and we use a for loop to get the AIC of each model. Finally, we choose the (best) model with the lowest AIC.

There’s something else: We have used the price time series with a log transformation. Why? The prices might suffer from high volatility, but log transformations help us have lower volatility and an easier time series for the model to fit.

Step 4: Set some variables for the event-driven backtesting loop.

Set the position column to zero for the computation of the strategy returns.

Set the current_model variable to None to be used for the weekly estimation.

Set the last_fit_date variable to None as a flag used for the weekly estimation.

Set the train_span as the number of days for the model’s estimation. For this occasion, we set it to 3 years (750 observations, approximately)

Set the year_start as the first year to be used to backtest the strategy.

Step 5: Optimise the parameters of the ARIMA (p, d, q) each week and forecast each day

The for loop goes as follows:

Fit the model only on Mondays

Find the order of integration of the price series

Select the best p-and-q pair

Estimate the best model

Forecast the next price

Generate the signal and save it in the data dataframe. We log the current price because the model is trained on log prices.

Step 5: Compute the strategy and buy-and-hold returns

To compute the returns, we subset the data dataframe to use only the results from 2019  onwards.

Step 6: Plot the strategy and buy-and-hold returns

Notes to take your model to the next level

Maybe the returns are not interesting enough right? The industry has heavily used this model for decades.

I know what you’re thinking. You need to improve the results. Well, here we present to you some interesting tweak ideas to perform:

Did you miss something about the model’s theory? Don’t worry, you can explore its intricacieshere.

You should optimize the train_span to achieve possibly better performance.

We have fitted the model weekly. What about fitting the modeldaily? Or monthly?

What if we train the model only when we really need it? Try thisalgorithmto achieve that goal!

In case you want to use, e.g. monthly-frequency data, to trade each period, you’ll be short of historical data. You can usesyntheticdata to trade good enough!

Do you know you can fit an this model using your Nvidia GPU? You’ll benefit a lot from using the cuml library from Nvidia because the estimation is much faster! Learn the basicshere.

Do you want to try more complex models? You know you have everything in this blog! You can check theARFIMAand the ARTFIMA.

What about a risk management process with stop-loss and take-profit targets? Tweak the code to incorporate them. Do you want to apply the Kelly criterion? Or maybe, therisk-constrainedKelly criterion?

What about meta-labelling to size the trade? Try tweaking the code to apply that

You canexplore the full Python code for using the ARIMA model with time series datafor predicting stock prices in Sections 18, Unit 9, Unit 11, and Unit 15 of the course titled Financial Time Series Analysis for trading. These units consist of examples that explain the use of this model with all the parameters and real-time data.

Unit 9 will start by covering the basics of the ARIMA model with Python.

Unit 11 will consist of the entire Python code for the above-mentioned steps.

Unit 15 will help you find the best-fit model.

Conclusion

In trading, ARIMA models analyse historical price patterns, identify trends, and detect potential turning points in stock prices. These models can help traders anticipate market movements, assess risk, and optimise their investment strategies. By leveraging the statistical properties of time series data, this model enables traders to make informed decisions based on a thorough understanding of market dynamics.

If you wish to explore more about using the the discussed model and other type of econometric models for forecasting stock returns, you can explore our course onFinancial time series analysis for trading. This is the perfect course to understand the concepts of Time Series Analysis and implement them in live trading markets. Starting from basic AR and MA models, to advanced models like ARIMA, SARIMA, ARCH and GARCH, this course covers it all.

Further Reading

Once you've learned and tried ARIMA, a great next step is to exploreARFIMA Models, which extend ARIMA by addressing long-memory behavior in financial data.

To develop more well-rounded trading strategies, broaden your knowledge with practical tools and techniques. Learn to spot patterns usingTechnical Analysis, manage risk effectively throughTrading Risk Management, explore asset correlation techniques inPairs Trading, and understand trading mechanics withMarket Microstructure.These concepts, when used alongside ARIMA, can significantly enhance your strategy-building process.

If you’re looking for a comprehensive and structured approach to mastering quantitative trading, theExecutive Programme in Algorithmic Trading (EPAT)is highly recommended.The course covers time series analysis (including stationarity, ACF, PACF), advanced statistical models like ARIMA, ARCH, and GARCH, and Python-based trading strategies.It also includes modules on statistical arbitrage, alternate data, and reinforcement learning, making it ideal for serious learners ready to apply these concepts in real-world trading.

File in the download:

Forecasting Stock Prices Using ARIMA Model - Python notebook

Feel free to make changes to the code as per your comfort.

Login to Download

Note: The original post has been revamped on 10thApr 2025 for recentness, and accuracy.

Disclaimer: All data and information provided in this article are for informational purposes only. QuantInsti®makes no representations as to accuracy, completeness, currentness, suitability, or validity of any information in this article and will not be liable for any errors, omissions, or delays in this information or any losses, injuries, or damages 	arising from its display or use. All information is provided on an as-is basis.

---

*Imported from QuantInsti Blog on 2026-04-27*
