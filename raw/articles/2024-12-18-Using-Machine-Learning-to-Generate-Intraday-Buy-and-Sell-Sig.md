---
title: "Using Machine Learning to Generate Intraday Buy and Sell Signals for Cryptocurrency | EPAT Project"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/epat-project-machine-learning-intraday-buy-sell-signals-cryptocurrency/"
date: "2024-12-18"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Using Machine Learning to Generate Intraday Buy and Sell Signals for Cryptocurrency | EPAT Project

**来源**: [QuantInsti](https://blog.quantinsti.com/epat-project-machine-learning-intraday-buy-sell-signals-cryptocurrency/)  
**日期**: 2024-12-18  
**作者**: QuantInsti

---

## 原文

Using Machine Learning to Generate Intraday Buy and Sell Signals for Cryptocurrency | EPAT Project

By:Sharath Chandra Nirmala

In this project, I explored the effectiveness of Random Forests in developing intraday trading strategies for the Bitcoin-US Dollar (BTC-USD) pair using technical indicators. Unlike traditional methods, I utilized Random Forests to generate trading rules, aiming to enhance performance and efficiency. I developed the strategy using two years of 1-minute OHLC data from Alpaca, with various technical indicators as features. The strategy I developed achieved a Sharpe Ratio of 4.47 and a total return of 367.05%, outperforming a simple buy-and-hold approach. I faced challenges with inconsistent volume data, hence I excluded volume from the analysis.

NOTE: This project demonstrates the theoretical approach to applying Random Forests in trading. It shouldn't be applied by itself in the markets as it trades quite frequently and is impractical in its current state. It should only be used as a conceptual base for building more advanced strategies, which I am currently working on.

This article is the final project submitted by the author as a part of his coursework in the Executive Programme in Algorithmic Trading (EPAT) at QuantInsti. Do check ourProjects pageand have a look at what our students are building.Other EPAT Project publications onMachine Learning for trading, Intraday Trading and Cryptocurrencies are listed below:

Order Flow Strategy For Crypto Markets [EPAT PROJECT](2018)

Development Of Cloud-Based Automated Trading System With Machine Learning [EPAT PROJECT](2016)

Machine Learning Based Optimal Portfolio Allocation [EPAT Project](2021)

Machine Learning and Systematic Forex Trading [EPAT Project](2021)

Portfolio Assets Allocation with ML and Optimization for Dividend Stocks [EPAT Project](2022)

Order Flow Strategy For Crypto Markets[EPAT PROJECT] (2018)

About the Author

My name is Sharath Chandra Nirmala, and I'm from Hyderabad, India. I completed my Bachelor of Engineering in Computer Science and Engineering from the National Institute of Engineering, Mysuru in 2024.  Currently, I'm working at Fidelity Investments, India as an Executive Graduate Trainee—Full Stack Engineer in the Asset Management Technology business unit.  I'm passionate about coding, machine learning, and finance, which naturally led me to algorithmic trading. Feel free to connect with me on LinkedIn:https://www.linkedin.com/in/snirmala20/or check out my projects on GitHub:https://github.com/sharathnirmala16/.

EPAT batch: #61Certification status: Certification of ExcellenceMentor:Akshay Choudhary

Project Idea

The idea is to use "machine learning in trading" and its techniques like Decision Trees or other algorithms, if better one is found during research for Buying, Holding, and Selling cryptocurrencies.

The decision tree model is trained on historical data using a set of technical indicators and statistical relationships between these indicators and prices as inputs. The model then learns to make trading decisions (buy or sell signals) based on these inputs or a subset of these inputs.

The initial Idea is to use Decision Trees and compare it with other models mentioned in the coursework, with a final possibility of combining them to yield better results. Ultimately the goal is to have a high win rate and Sharpe ratio as compared to what I have achieved in the paper with stocks that I have mentioned below for cryptocurrencies, as it is easier to go long and short on crypto, and there is higher volatility in this market.

I have already worked on a Decision Tree based long only strategy for trading stocks in the NIFTY50 index after reading about a similar strategy from the textbook given in the course.

While it had a good Sharpe ratio, it’s win rate in the testing data was around ~48.15% and it was a long only strategy. I want to build a bidirectional strategy [long and short] to improve win rate while maintaining or increasing the Sharpe ratio, here is the link to the paper that I wrote about the strategy for stocks:https://arxiv.org/pdf/2405.13959.

Project Abstract

This article aims to explore the effectiveness of Random Forests in developing intraday trading strategies using established technical indicators for the Bitcoin-US Dollar (BTC-USD) pair.

Unlike traditional methods that depend on a static rule set derived from combinations of technical indicators formulated by human traders, the proposed approach utilizes Random Forests to generate trading rules, potentially enhancing trading performance and efficiency.

By rigorously backtesting the strategy, a trader can ascertain the viability of employing the rules generated by the Random Forests algorithm for any market. Random Forest-based strategies have been observed to outperform the simple buy-and-hold strategy in various instances.

The findings underscore the proficiency of Random Forests as a powerful tool for augmenting intraday trading performance. A rules-based strategy becomes more important in highly volatile Cryptocurrency markets.

Dataset

The Dataset will be intraday data 1 minute OHLCV data of BTCUSD [Bitcoin USD] or BTCUSDT [Bitcoin Tether] for at least the last two years.

Project Motivation

Intraday trading involves executing buy and sell orders within the same day to capitalise on minor price fluctuations in the market, accumulating small profits over the trading period.Technical analysis for tradingis a well-established method in intraday trading that employs historical market data to generate indicators, recognise patterns, and make trading decisions based on the identified patterns.

However, conventional technical analysis methods rely on a fixed set of rules based on combinations of technical indicators, which can be time-consuming to develop and may not perform consistently across all assets. Moreover, these methods may not account for individual asset characteristics, leading to suboptimal trading decisions.

Previously, I have worked on a decision tree-based strategy for the equities market [1]. This strategy utilized a set of technical indicators across various stocks and was a long-only strategy. Inspired by this experience, I decided to develop a strategy for the cryptocurrency market, specifically focusing on the Bitcoin-US Dollar (BTC-USD) pair.

Due to the highly volatile nature of cryptocurrencies and the larger datasets involved, a decision tree-based strategy did not perform well in backtesting. To address this challenge, I upgraded the model to Random Forests, an ensemble learning method that combines multiple decision trees to improve predictive accuracy and robustness.

The cryptocurrency market presents an appealing opportunity for several reasons. Firstly, it allows for both long and short positions, providing more flexibility in trading strategies. Secondly, the market operates 24/7, offering a higher frequency of trading opportunities compared to traditional equity markets. These factors motivated me to explore algorithmic trading strategies in the cryptocurrency market using Random Forests.

Data Mining

To develop thealgorithmic trading strategyfor the BTC-USD market, historical data is essential. In this project, the data was obtained from Alpaca, a platform that provides free access to cryptocurrency data through its API. The API offers 1-minute level OHLC (Open, High, Low, Close) data. A dataset spanning two years was collected, comprising approximately 900,000 rows of 1-minute OHLC data for the BTC-USD pair. This extensive data set allows for a comprehensive analysis of the market, enabling the development of a robust trading strategy.

Data Analysis

With the collected OHLC data, various technical indicators were computed to capture the underlying market trends and patterns. These indicators serve as features for the Random Forests model, enabling it to generate. The input features and indicators used for the model are listed below:

Returns [percent change]

15 period percent change

Relative Strength Index [RSI]

Average Directional Index [ADX]

Simple Moving Average [SMA]

Ratio between SMA and Close Price

Correlation between SMA and Close Price

Volatility — Standard deviation of returns

Standard deviation of 15 period returns

The output which the model predicts on is the future percent change which is just the next return value [greater than 0 -> 1, 0 = 0, lower than 0 -> -1].

Key Findings

When it comes to random forests, there are many hyperparameters, the most important are:

n_estimators — The number of estimators/decision trees in the model.

max_tree_depth — The maximum depth of the tree. If None, then nodes are expanded until all leaves are pure or until all leaves contain less than min_samples_split samples.

criterion — can be either “gini”, “entropy”, “log_loss”

The gini criterion was used for the model and the maximum tree depth was set to None, so the model can expand the trees as necessary. As for the number of estimators, I have tested various values and have settled on 11. An odd number of estimators have worked better than the even number of estimators in my analysis.

I have included charts showing various key performance indicators in relation to the number of estimators below. In the code repository, a report can be found that lists various metrics of the strategy in comparison to the buying-and-holding the asset itself [Filename: Random-Forest-BTCUSD.html]. A summary of important metrics of the strategy:

Sharpe Ratio: 4.47

Total Return: 367.05%

Max Drawdown: -22.93%

Win Rate: 53.53%

Profit Factor: 1.06

Limitations

Although the API also provides volume data, it was observed that the volume was zero for most of the rows. This inconsistency in volume data could be attributed to data quality issues (I was using the free API after all). As a result, volume and volume-based indicators were excluded from the strategy development process to ensure the reliability and robustness of the trading signals. Addition of volume based indicators might have been useful as it proved useful for my previous equity based strategy.

Implementation Methodology

For this project, the Random Forest Classifier model was created using the Scikit Learn library. The vectorized backtesting for the strategy was performed using the VectorBt library. The code is explained and can be found in the linked repo [Filename: backtest_script.py]. Some of the generated trees of the model are given below:

Conclusion

The results demonstrated that the Random Forest-based strategy outperformed the simple buy-and-hold strategy, showcasing the potential of Random Forests as a valuable tool for enhancing intraday trading performance in the cryptocurrency market.

Future work includes further hyperparameter tuning of the Random Forests model, incorporating additional features, and exploring other ensemble learning methods to improve the strategy's performance. Additionally, extending the strategy to other cryptocurrency pairs and assessing its performance in different market conditions could provide valuable insights for traders seeking to refine their trading strategies.

In conclusion, the proposed algorithmic trading strategy using Random Forests offers a promising approach for traders looking to capitalize on the unique opportunities presented by the cryptocurrency market.

Annexure/Codes

[1] GitHub Repository: https://github.com/sharathnirmala16/btc-ml-epat-project

Bibliography

[1] Daniya, T., et al. “Classification and regression trees with Gini Index.” Advances in Mathematics: Scientific Journal, vol. 9, no. 10, 23 Sept. 2020, pp. 8237–8247, https://doi.org/10.37418/amsj.9.10.53

[2] Shah, Ishan, and Rekhit Pachanekar. “Chapter 12 - Decision Trees.”Machine Learning in Trading, QuantInsti Quantitative Learning Pvt. Ltd., Mumbai, Maharastra, 2023, pp. 143–155.

[3] Filho, Mario. “Do Decision Trees Need Feature Scaling or Normalization?” Forecastegy, 24 Mar. 2023, forecastegy.com/posts/do-decision-trees-need-feature-scaling-ornormalization/#:~:text=In%20general%2C%20no.,as%20we%27ll% 20see%20later

[4] Shafi, Adam. “Random Forest Classification with Scikit-Learn.” DataCamp, DataCamp, 24 Feb. 2023, www.datacamp.com/tutorial/random-forests-classifier-python.

[5] “Randomforestclassifier.” Scikit, scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html. Accessed 23 July 2024.

[6] My preprint paper which is yet to be published: https://arxiv.org/pdf/2405.13959

File in the download

The Python codes for implementing the strategy are provided, including data download, backtesting scripts, data downloads and implementation technology.

Login to Download

Next steps

Want to know how EPAT equips you with skills to build your trading strategy in Python? Check out theEPAT course curriculumto find out more.

If you are interested in learning more aboutmachine learning, read the blogs here:

Machine Learning Basics: Components, Application, Resources and More

Reinforcement Learning in Finance: Resources and Expert Advice from Paul Bilokon

Artificial Intelligence & Machine Learning in Trading

Machine Learning Logistic Regression: Python, Trading and more

Machine Learning Classification: Concepts, Models, Algorithms and more

Top 10 Machine Learning Algorithms For Beginners

Machine Learning for Algorithmic Trading in Python: A Complete Guide

An Introduction to Unsupervised Learning for Trading

Free Resources to Learn Machine Learning for Trading

You can also access theMachine Learning in Trading Bookfor Free.Read the blogs on cryptocurrency here to get enhanced knowledge in the crypto trading domain with this blog section mentioned below:

Forex & Crypto Trading

Below, there are individual blogs on cryptocurrency trading that you can read:

Crypto Basics: Trading, Blockchain, Future and More

Alt Coins: A Comprehensive Guide

Bitcoin Basics: What it is, Crypto Trading, Bitcoin Algo Trading

Crypto Arbitrage: Overview, Trading Strategies, Opportunities, and More

Cryptocurrency Wallets - A Beginner’s Guide

Bitcoin Blockchain: Components, Mining, Inflation and Algo Trading

Learn more about machine learning and cryptocurrency with the courses in the“Learning Tracks”below so that you can create the right strategy for a specific market regime.

Learning Track: Machine Learning & Deep Learning in Trading Beginners

Learning Track: Artificial Intelligence in Trading Advanced

Learning Track: Algorithmic Trading in Cryptocurrency and Forex

To further advance your skills, consider enrolling in acrypto trading coursethat helps you apply these concepts with practical strategies.

Disclaimer:The information in this project is true and complete to the best of our Student’s knowledge. All recommendations are made without guarantee on the part of the student or QuantInsti®. The student and QuantInsti® disclaim any liability in connection with the use of this information. All content provided in this project is for informational purposes only and we do not guarantee that by using the guidance you will derive a certain profit.

---

*Imported from QuantInsti Blog on 2026-04-27*
