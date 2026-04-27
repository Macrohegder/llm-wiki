---
title: "Portfolio Management Of Multiple Strategies Using Python"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/portfolio-management-strategy-python/"
date: "2024-05-02"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Portfolio Management Of Multiple Strategies Using Python

**来源**: [QuantInsti](https://blog.quantinsti.com/portfolio-management-strategy-python/)  
**日期**: 2024-05-02  
**作者**: QuantInsti

---

## 原文

Portfolio Management Of Multiple Strategies Using Python

In today's dynamic financial landscape, effectiveportfolio managementis paramount for investors seeking to optimise returns while managing risk. Harnessing the power ofPython, a versatile programming language, a trader can get unparalleled opportunities to construct and manage portfolios comprising multiple investment strategies.

From understanding the fundamentals of portfolio construction to implementing sophisticated risk management techniques, this guide will equip you with the necessary skills to navigate complex financial markets with more confidence! Join us as we delve into the realm of portfolio management strategies with Python and unlock endless possibilities for managing your trading portfolio with Python.

Checkout our Latest Video on a deeper perspective on portfolio rebalancing from a quantitative lens. He explains the rationale behind rebalancing and how to apply it effectively using Python.

Download the files here:

Login to Download

We cover:

Brief of portfolio management

Essential concepts of portfolio management

Efficient Portfolios

Portfolio Elements

Portfolio performance measures

Building a simple portfolio

Instruments or assets of a portfolio

Understanding multiple investment strategies

Python fundamentals for portfolio management

Implementing strategies for portfolio management with Python

Risk management in portfolio construction

Quantitative analysis for portfolio management

Strategies that contradict each other in portfolio management

Future trends in Python for portfolio management

Brief of portfolio management

Portfolio managementinvolves the strategic allocation and management of assets to achieve specific investment objectives while balancing risk and return. Managing a portfolio or handling multiple strategies doesn't deviate much from managing a portfolio of assets. Here, the operational assets are the strategies themselves. These strategies involve long, short, or waiting positions, all aiming to maximise returns while minimising risks.

The fundamental question arises:How should capital be allocated among various strategies and instruments to optimise returns and mitigate risks?

To establish a benchmark for optimisation, we initially distribute equal weights to each element within a simple portfolio. Numerous academic studies explore optimising capital distribution weights, each focusing on different parameters.

Two prominent and contrasting methods include:

Markowitz's efficient frontier, seeks to maximise returns within a defined risk level, thus, emphasising risk containment.

Kelly's method, proposed by John Kelly and Ed Thorpe, aims to maximise the expectation of log utility of wealth, prioritising return maximisation.

You will find a detailed learning of these two methods mentioned above in the course onQuantitative Portfolio Management. It is necessary that the traders get familiar with these and other methods to determine the most suitable approach aligning with their investment style and risk tolerance.

Let us see the essential concepts ofportfolio managementnext to learn the concept in detail later.

Essential concepts of portfolio management

The essential concepts ofportfolio managementare:

Efficient Portfolios

“An efficient portfolio is defined as a portfolio with minimal risk for a given return, or, equivalently, as the portfolio with the highest return for a given level of risk.”

Efficient portfolios are the smartest way to manage your money when you invest. Imagine spreading your money across different types of investments, like shares, bonds, and property. This helps keep your money safe even if the market performs unexpectedly. In an efficient portfolio, as a trader, you will look at things such as predicting the returns from each trade, how risky each trade is, and how they behave compared to each other. It's all about finding the right mix.

Alongside, you've got to keep an eye on the markets and make changes in your trades as and when needed. Markets change, economies shift, so what's good today might not be tomorrow. When we only have one portfolio management strategy managing one instrument, portfolio management is limited to maximising return while minimising risk. This would be the simplest portfolio, but not a simple solution.It is not a simple solution because we have to answer some questions.

Can we achieve the desired return with the instrument we are working with?

Are there other instruments that allow us to achieve a higher return with the same risk or less risk with the same return?

On the other hand, if we want to diversify the portfolio and, therefore, reduce the risk associated with the portfolio management strategy or instrument, we must build a portfolio with different instruments and ideally different strategies that capture different market regimes. Therefore, in addition to the above questions, we need to answer what weight we assign to each portfolio management strategy and what weight we give to each instrument within the portfolio to achieve the required objective (Max return vs Min risk).

We will check the elements of a portfolio next.

Portfolio Elements

Let's define the portfolio's elements below.

Assets:These are the investments held within the portfolio, such as stocks, bonds, cash, real estate, commodities, or alternative investments likehedge fundsor private equity.

Asset Allocation:This refers to the proportion of the portfolio allocated to different asset classes. For example, you might have 60% of your portfolio in stocks and 40% in bonds.

Diversification:Diversification involves spreading investments across different assets, industries, geographic regions, and investment styles to reduce risk. It helps mitigate the impact of poor performance in any single investment.

Risk Management:This involves strategies to mitigate risk, such as setting stop-loss orders, diversifying across asset classes, and using derivatives like options or futures for hedging.

Return Objectives:These are the financial goals of the portfolio, such as achieving a certain level of return to fund retirement or generate income.

Time Horizon:This is the length of time over which the portfolio is expected to be held. Longer time horizons may allow for more aggressive investment strategies, while shorter time horizons may require a more conservative approach.

Liquidity Needs:This refers to how easily assets can be converted into cash without significant loss of value. Portfolios may need to be structured to meet short-term cash flow requirements.

By carefully considering and managing these elements, traders can construct portfolios that align with their financial goals, risk tolerance, and investment preferences.

Let us see the performance measures or the various metrics to find out the performance of an ideal portfolio.

Portfolio performance measures

Algorithmic traders have at their disposal a large number of measures orperformance metricsto analyse the portfolio management strategy and/or the portfolio performance. Mastering these metrics is a key module in any solidalgorithmic trading course, helping traders move from theory to real, data-driven portfolio decisions.Some of the most used portfolio performance metrics are:

Annualised Returns

Annualised Volatility

Sharpe Ratio

Sortino Ratio

Treynor Ratio

Information Ratio

Skewness

Kurtosis

Maximum Drawdown

Number of Trades

Profit ratio

Holding period

In addition to these individual measures, thepyfolio libraryimplements a fantastic catalogue of performance measures and graphics that are certainly worth learning to use. We will see some of their performance reports through this post.

Now, let us move to building a simple portfolio part.

Building a simple portfolio

To build our example portfolio we are going to use two methods. One with two stocks and three strategies for portfolio management and the other with three stocks and again three strategies.

It is needless to say any strategy that is considered to be part of the portfolio should undergobacktestingthat offers us an adequate level of certainty about the strategy returns. Hence, it is important to learn backtesting if not done yet. The Quantra course onbacktesting trading strategies pythonis the most direct way to build this skill, covering everything from data handling to strategy evaluation using Python.

Going forward, let us check the instruments or the assets that are utilised in portfolio management.

Instruments or assets of a portfolio

Assets are the main elements of a portfolio and their characteristics are decisive for obtaining the determined risk/benefit ratio. Some of the most important assets are:

Currency

Volatility

Liquidity

Commission

Slippage

Correlation (in relation to other assets)

Currency:If our portfolio is denominated in dollars and we buy an instrument on the European stock exchange, we are buying in euros. Therefore, the return on our investment not only depends on the return of the instrument (or strategy) but also depends on the fate of the currency. In the short term, it may be insignificant, but in the long term, it may boost return, reduce it or increase losses.

Volatility:The volatility of the instrument allows us to estimate if we will be able to reach the desired return or if we will be able to contain the required risk. If we want to boost the return, we will generally look for more volatile assets and if we want to contain the risk we will look for less volatile assets. It is difficult to raise the return of our strategy to 20% with a treasury bond with an annualised return of 3% (perhaps by increasing the position, leverage or other formulas, but it is difficult). On the other hand, it is difficult to contain the risk of our strategy at 10% if we fill the portfolio of wild penny-stocks with volatilities of more than 300%.

Liquidity:The liquidity of an instrument indicates its capacity to absorb our entry or exit position, logically this is more important for strategies that handle large positions, but the liquidity of a single contract can be critical at certain times (expiration date, moments of panic, etc.).

Cost:The cost of the asset allows us to know the position and the weight that the asset will have within our portfolio. Let's suppose that we have a strategy that exploits a characteristic of the gold price. We can invest in gold in multiple ways, among them we can buy Gold futures contracts, e-mini Gold and Micro Gold, we have available Options, ETF, etc. each with a cost, volatility, commissions, slippage, etc.

Commission and Slippage:Commissions and slippage undermine the return on our portfolio and should be studied in depth. The slippage is closely related to the bid-ask price.

Correlation:Finally, when we are analysing different instruments to include in our portfolio of strategies it is necessary to take into account thecorrelationwith possible assets or stocks. For example, if our portfolio management strategy is exploiting a trend following system with an e-mini gold contract, it would not make much sense from a diversification point of view to include the future of silver which usually has a high correlation with gold. Ideally, we will look for low correlation assets to exploit the same portfolio management strategy.

Next, we will find out the multiple investment strategies deployed in portfolio management.

Understanding multiple investment strategies

There are certain investment strategies that can be implemented using various Python libraries such as NumPy, pandas, scipy, and scikit-learn, along with tools for optimisation and simulation. Additionally, financial data can be fetched using APIs like Yahoo Finance or Alpha Vantage for analysis and implementation of these strategies.

Here are multiple portfolio management strategies that can be implemented in Python:

Equal Weighted Portfolio:Allocate equal weights to all assets in the portfolio.

Market Cap Weighted Portfolio:Allocate weights to assets based on their market capitalisation.

Minimum Variance Portfolio:Construct a portfolio with the lowest possible variance, typically achieved through mean-variance optimisation.

Maximum Sharpe Ratio Portfolio:Construct a portfolio that maximises the Sharpe ratio, which represents the risk-adjusted return.

Risk Parity Portfolio:Allocate weights to assets such that each asset contributes equally to the portfolio's overall risk.

Inverse Volatility Weighted Portfolio:Allocate weights to assets inversely proportional to their volatility.

Bayesian Optimisation:Use Bayesian methods to optimise portfolio allocation based on historical data and prior beliefs.

Monte Carlo Simulation:Simulate various market scenarios and optimise portfolio allocation based on the simulation results.

Factor Investing:Construct portfolios based on specific factors such as value, growth, momentum, or quality, aiming to outperform the market.

Tactical Asset Allocation:Adjust portfolio weights dynamically based on market conditions or economic indicators.

We will see the fundamentals for the portfolio management practice using Python next.

Python fundamentals for portfolio management

Python offers a robust set of tools and libraries that make it a powerful choice for portfolio management. Here are some fundamental Python concepts and tools essential for portfolio management:

Data Handling with Pandas:Pandas is a popular library for data manipulation and analysis. It's commonly used for handling financial data, such as stock prices, dividends, and economic indicators.

Numerical Computing with NumPy:NumPy provides support for large, multi-dimensional arrays and matrices, along with a collection of mathematical functions. It's particularly useful for performing numerical computations and statistical analysis.

Visualisation with Matplotlib and Seaborn:Matplotlib is a versatile library for creating static, interactive, and animated visualisations in Python. Seaborn builds on top of Matplotlib and provides a high-level interface for creating attractive statistical graphics.

Portfolio Optimisation with scipy.optimize:The scipy.optimise module offers optimisation algorithms for solving various mathematical optimisation problems. Portfolio optimisation involves maximising returns while minimising risk, and scipy.optimize can be used to implement optimisation routines for this purpose.

Risk Metrics Calculation:Python libraries like QuantLib and scipy.stats offer functions for calculating risk metrics such as volatility, beta,Sharpe ratio, and Value at Risk (VaR). These metrics are crucial for assessing and managing portfolio risk.

Time Series Analysis with Statsmodels:Statsmodels is a library for estimating and interpreting statistical models. It includes functions for time series analysis, such as autoregressive integrated moving average (ARIMA) modelling and seasonal decomposition.

API Integration for Market Data:Python libraries like requests or dedicated financial APIs (e.g., Alpha Vantage, Yahoo Finance) can be used to fetch real-time or historical market data forportfolio analysisand decision-making.

Backtesting Strategies with Backtrader or PyAlgoTrade:Backtesting involves simulating trading strategies using historical data to evaluate their performance. Libraries like Backtrader and PyAlgoTrade provide tools for backtesting trading strategies in Python.

By mastering these Python fundamentals and leveraging the rich ecosystem of libraries and tools available, one can effectively manage portfolios, analyse investment strategies, and make data-driven investment decisions.

Now, let us get to the implementation part. We will implement different strategies with two sets of portfolios. One portfolio with two assets and another one with three assets.

Implementing strategies for portfolio management with Python

Let us see the examples of the implementation of different strategies inportfolio managementwith -

A. Portfolio of two assets

The strategies used in this are:

Equal Weighted Portfolio

Market Cap Weighted Portfolio

Minimum Variance Portfolio

B. Portfolio of three assets

The strategies used in this are:

Maximum Sharpe Ratio Portfolio

Risk Parity Portfolio

Inverse Volatility Weighted Portfolio

We have discussed these strategies briefly earlier in this blog.

A. Portfolio of two assets

Visualisation of daily returns and cumulative returns

Let us, first of all, see the visualisation of a portfolio with 2 stocks, that is, APPLE (ticker = AAPL) and Coca-cola (ticker = KO). We will see the daily returns as well as the cumulative returns of the portfolio.

Output:

Portfolio Performance Metrics:
Sharpe Ratio: 0.90
Average Daily Return: 0.0007
Average Annualised Return: 0.17
Volatility (Standard Deviation of Daily Returns): 0.0121

In the output above, the following are the observations:

A Sharpe ratio of 0.90 means that, on average, the portfolio generated 0.90 units of excess return per unit of risk. A higher Sharpe ratio indicates better risk-adjusted performance.

Average daily return represents the average return of the portfolio on a daily basis over the given time period. An average daily return of 0.0007 means that, on average, the portfolio's value increased by 0.07%.

Average return of the portfolio on an annualised basis is calculated by multiplying the average daily return by the number of trading days in a year (252 in this case). An average annualised return of 0.17 means that, on average, the portfolio generated a return of 17%.

Volatility (Standard Deviation of Daily Returns) measures the dispersion of returns around the average return. It indicates the degree of variation in the portfolio's returns. A standard deviation of daily returns of 0.0121 means that, on average, the daily returns of the portfolio deviated from the mean return by 1.2%.

Investment strategies using the portfolio of two assets

Let us now visualise the portfolio of two assets, that is, ‘AAPL and KO’ using different strategies namely:

Equal Weighted Portfolio

Market Cap Weighted Portfolio

Minimum Variance Portfolio

Output:

Here's what each graph above signifies:

Equal Weighted Portfolio:This graph shows the performance of a portfolio where each asset is given an equal weight, meaning the same amount of investment is allocated to each asset. The plotted line represents the cumulative returns of the portfolio over the specified time period. It helps visualise how the portfolio composed of equally weighted assets performs compared to other strategies.

Market Cap Weighted Portfolio:This graph shows the performance of a portfolio where the weights of assets are determined based on their market capitalisation. Assets with higher market capitalisation have a larger weight in the portfolio compared to assets with lower market capitalisation. The plotted line represents the cumulative returns of the portfolio over time, reflecting the performance of this market-cap-weighted strategy.

Minimum Variance Portfolio:This graph shows the performance of a portfolio constructed to minimise portfolio variance or volatility. The weights of assets in this portfolio are determined to minimise the overall risk of the portfolio while achieving the desired level of return. The plotted line represents the cumulative returns of the portfolio over time, illustrating the performance of this risk-optimised strategy.

Each plotted graph provides insight into how different portfolio construction strategies perform over time, allowing investors to evaluate their effectiveness in achieving investment objectives and managing risk. If the desired results from the strategy are not achieved, the parameters in the portfolio such as weights assigned, volume etc. can be set accordingly.

Using the same strategies, you can include a portfolio of as many assets as you usually trade with having a low or negative correlation with each other.

Including assets with low correlation can help reduce portfolio risk while potentially enhancing returns. The specific assets included in an efficient portfolio depend on various factors such as investment objectives, risk tolerance, time horizon, and market conditions.

B. Portfolio of three assets

This time, we will take into consideration a portfolio with 3 stocks, that is, APPLE (ticker = AAPL), Coca-cola (ticker = KO) and Old National Corp (ticker = ONB). We will see the daily returns as well as the cumulative returns of the portfolio.

After this, we will see the portfolio performance using each of the three strategies, namely

Maximum Sharpe Ratio Portfolio

Risk Parity Portfolio

Inverse Volatility Weighted Portfolio

In the code below, we have compiled all the steps necessary for the same.

Output:

Each graph in the output above represents a distinct portfolio strategy and its performance:

Maximum Sharpe Ratio Portfolio:The graph in the output displays returns generated by the portfolio constructed using the Maximum Sharpe Ratio (MSR) approach. It shows how returns fluctuate over time, reflecting the strategy's aim to maximise risk-adjusted returns by achieving the highest possible Sharpe ratio.

Risk Parity Portfolio:This graph illustrates returns generated by the portfolio constructed using the Risk Parity approach. It highlights how returns vary over time, indicating the strategy's focus on balancing risk contributions across asset classes for more stable returns.

Inverse Volatility Weighted Portfolio:The graph depicts returns from the portfolio constructed using the Inverse Volatility Weighted approach. It demonstrates how returns evolve over time, showcasing the strategy's emphasis on assigning higher weights to less volatile assets to reduce portfolio volatility.

It is important to note that backtesting results do not guarantee future performance. The presented strategy results are intended solely for educational purposes and should not be interpreted as investment advice. A comprehensive evaluation of the strategy across multiple parameters is necessary to assess its effectiveness.

From the above output, you can see how a portfolio of three stocks with three different strategies perform. On the basis of your analysis, you cancreate a portfolio of various stocksand utilise the three strategies as mentioned above.

Going forward, we will see how to do risk management in portfolio construction.

Risk management in portfolio construction

Risk management in portfolio construction is vital for achieving investment goals while minimising potential losses. Diversification, spreading investments across various asset classes, sectors, and regions, mitigates risk by avoiding overexposure to any single asset or market segment. Asset allocation strategically distributes investments based on risk tolerance, aligning the portfolio with the investor's objectives.

Thorough risk assessment identifies and quantifies different types of risks, such as market risk and credit risk, enabling the implementation of appropriate risk management strategies. Regular monitoring of portfolio risk metrics and performance facilitates timely adjustments and rebalancing to maintain the desired risk profile. Overall, effective risk management practices are essential for navigating market uncertainties and safeguarding investment portfolios.

Now we will be seeing the role and importance of quantitative analysis in portfolio management.

Quantitative analysis for portfolio management

Quantitative analysis in portfolio management harnesses mathematical and statistical methods to inform investment decisions. Key aspects include:

Risk Assessment:Quantitative models gauge market, credit, and liquidity risks, aiding proactive risk mitigation.

Portfolio Optimisation:Techniques like mean-variance optimisation craft portfolios for maximum returns at a chosen risk level.

Performance Measurement:Metrics such as Sharpe ratio and alpha assess portfolio effectiveness and risk-adjusted returns.

Asset Valuation:Models like P/E ratios determine asset values, aiding investment decision-making.

Risk Management Strategies:Quantitative analysis guides hedging, stress testing, and scenario analysis to manage portfolio risks effectively.

Overall,quantitative analysisempowers portfolio managers with data-driven insights to navigate markets efficiently and achieve investment objectives.

Now we will check out which strategies contradict each other in the portfolio management practice.

Strategies that contradict each other in portfolio management

When you're piecing together a portfolio of different strategies using Python, it's crucial to steer clear of combinations that work against each other, defeating the purpose of diversification. Let's look at a couple of scenarios to avoid:

Highly Correlated Strategies:The whole point of diversifying your portfolio is to spread out risk by investing in assets that don't all move in sync. If you have two strategies that focus on similar market movements or rely on closely correlated assets (think gold and silver), you won't get the independent risk reduction you're aiming for. For example, pairing up a strategy that follows trends in gold futures with another one that does the same for silver futures wouldn't be ideal because gold and silver prices tend to move together.

Strategies with Offsetting Signals:It's best if your strategies give you different signals that complement each other. Including strategies that consistently give conflicting trade recommendations will cancel out each other's impact.

Picture one strategy that buys stocks whenever a particular momentum indicator goes up and another strategy that sells those same stocks when the same indicator goes down. You'd end up with a lot of activity but not necessarily a lot of overall gain.

Let us now see the future trends in Python for portfolio management and on the basis of what the research says for the same.

Future trends in Python for portfolio management

Below are the potential future trends in Python for portfolio managers. ⁽¹⁾

Integration with AI and Machine Learning:Python's extensive data science libraries like Scikit-learn and TensorFlow will be crucial in building AI-powered portfolio management tools (You can learn all about in this course onAI for Portfolio Management). These tools can analyse vast amounts of financial data, identify patterns, and suggest optimal investment strategies.

Advanced Analytics for Better Decision Making:Python's data manipulation capabilities (Pandas) and data visualisation tools (Matplotlib) will be essential for portfolio managers to make data-driven decisions. They can use Python to analyse portfolio performance, identify risks, and uncover new investment opportunities.

Algorithmic Trading and Automation:Python's ability to automate tasks will be a boon for algorithmic trading. Python scripts can be used to execute trades based on predefined rules and market signals, reducing human error and reaction times.

Backtesting:Python's simulation capabilities will allow portfolio managers to backtest the trading strategies. Backtesting helps assess the potential performance of a portfolio under different market conditions.

Conclusion

Portfolio management, coupled with Python's analytical methods, offers investors a powerful toolkit for navigating financial markets. By emphasising diversification, risk management, and quantitative analysis, investors can construct robust portfolios aligned with their objectives. As Python continues to evolve, its role in portfolio management is poised to expand, driving innovation and efficiency in investment strategies.

Incorporating diverse data sources, likeYahoo Finance Futures, can elevate portfolio management strategies by improving risk assessment and enhancing asset allocation. Leveraging such data alongside Python-based tools allows traders to optimize their models, driving more accurate predictions and smarter decision-making for improved performance.

With a commitment to harnessing data-driven insights and adapting to emerging trends, investors can confidently navigate the complexities of portfolio management, achieving long-term success in their financial endeavours.

In case you wish to learn about effective portfolio management with Python and quantitative methods in detail, explore our learning track: "Portfolio Management and Position Sizing using Quantitative Methods." Find out the diverse strategies for optimising trade size, capital allocation, and handle the portfolio management challenges head-on. Be sure to check it out to transform your portfolio management approach!

Author:Chainika Thakar(Originally written byMario Pisa)

Note: The original post has been revamped on 2ndMay 2024 for recentness, and accuracy.

Disclaimer: All investments and trading in the stock market involve risk. Any decision to place trades in the financial markets, including trading in stock or options or other financial instruments is a personal decision that should only be made after thorough research, including a personal risk and financial assessment and the engagement of professional assistance to the extent you believe necessary. The trading strategies or related information mentioned in this article is for informational purposes only.

---

*Imported from QuantInsti Blog on 2026-04-27*
