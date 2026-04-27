---
title: "Using Sentiment Analysis To Trade Equities [EPAT PROJECT]"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/sentiment-analysis-trade-equities/"
date: "2019-01-17"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Using Sentiment Analysis To Trade Equities [EPAT PROJECT]

**来源**: [QuantInsti](https://blog.quantinsti.com/sentiment-analysis-trade-equities/)  
**日期**: 2019-01-17  
**作者**: QuantInsti

---

## 原文

Using Sentiment Analysis To Trade Equities [EPAT PROJECT]

This article is the final project submitted by the author as a part of their coursework inExecutive Programme in Algorithmic Trading (EPAT™)at QuantInsti®. Do check our Projects page and have a look at what our students are building.

About the Author

An EPATian,Siddhant R Vaidyais based in Pune, India and has a bachelor's degree in Engineering from Pune University.

A trader working at Capstone Securities Analysis Pvt. Ltd, he holds the EPAT Certificate of Excellence.

Platform: Python

Project Abstract

The market is driven by people, and people are driven by emotions. We come across numerous events where sentiments have been more influential in driving a stock up or down than any other factors pertaining to the fundamental or technical aspects of the stock. A few examples of such events: the launch of a new iPhone, cryptocurrency mania, Tesla launching new cars, senior executives resigning or getting fired, etc.

I believe at any point in time if we are able to gauge the sentiment of an asset in the market, we will be able to successfully trade that asset profitably. The best way to assess the market sentiment is analyzing the main source of information that people use;news.

Data required:

The historical news data was availed from newsapi.org for the last 6 months. The asset chosen for my project is Nvidia Corporation (NVDA) and I downloaded the historical data for the same 6 months period from Yahoo Finance.

Procedure:

The project is divided into 3 main parts. News extraction, Sentiment score generation, and Strategy Execution.

1. News extraction

To get all relevant news articles related to Nvidia, we use the multiple filters in our query URL. The output we get are URLs for the news articles. We save these URLs in an excel file.

2. Sentiment score generation

Once we have the URLs for the required news articles, we use Requests and Newspaper package of python to extract the text from each article. Once we get the text, we need to process the data before we can consume it. We remove all symbols and special characters along with the stop words. Once this is done, we analyze each article to get a sentiment score for that article.

a. Textblob package that provides us with a polarity and a subjectivity score b.Vader sentimentanalyzer from Sentiment Intensity Analyzer package that provides us with a score between -1 to +1

For the final strategy, we will be using only the Vader sentiment score as it more straightforward and the results are better.

3. Strategy Execution

We have multiple scores for a couple of days as we might have multiple news articles on that day. But we are interested in only the most impactful news articles. Hence using a groupby, we find the max and min sentiment scores for each day. Then we create an indicator called 'extreme score' by adding the two. The logic behind this is that, say, for a particular day we get 2 conflicting news articles, one with very positive sentiment and one with a high negative sentiment, we should stay away from such events and not trade. Our indicator takes care of that.

We then set the thresholds for our long and short positions and then compare the results of our strategy with the Buy and Hold strategy.

Results:

Test period (Mar 2018 - August 2018)

Buy and Hold returns (absolute):17.76%

Strategy returns (absolute):24.72%

Buy and Hold Sharpe ratio:0.906

Strategy Sharpe ratio:1.34(Assuming risk-free rate of 4%)

Graph of returns

Limitations of project

Vader sentiment analyser is preferred for social media analysis. In our case, it tells us well if a news article is speaking positively of Nvidia or negatively, but it cannot comprehend the business aspect. News providers are quite polite in their articles, even when things are disastrous in reality. Hence gauging the true sentiment in such cases becomes difficult. The solution is to create a lexicon that incorporates the business aspect as well.

Further scope of the project

The indicator can be further improvised and the thresholds can be optimized

Employing machine learning for generating more effective sentiment scores

For any other strategies, sentiment analysis can be used for risk management

Using sentiment analysis for identifying black swan events

Next Step

If you want to learn various aspects ofAlgorithmic tradingthen check out ourExecutive Programme in Algorithmic Trading (EPAT™). The course covers training modules like Statistics & Econometrics, Financial Computing & Technology, and Algorithmic & Quantitative Trading. EPAT™ is designed to equip you with the right skill sets to be a successful trader.Enroll now!

You can enroll for thesentiment analysis courseon Quantra which will help you devise new trading strategies using Twitter, news sentiment data. In this course, you will learn to predict the market trend by quantifying market sentiments.

Recommended reads:

Crowdsourced Sentiment Analysis Trading Strategy

Application of Sentiment Analysis in Trading: Where it works?

Disclaimer: The information in this project is true and complete to the best of our Student’s knowledge. All recommendations are made without guarantee on the part of the student or QuantInsti®. The student and QuantInsti® disclaim any liability in connection with the use of this information. All content provided in this project is for informational purposes only and we do not guarantee that by using the guidance you will derive a certain profit.

List of files in zip archive:

Excel File containing the range of dates

Python code to extract News URLs

Sentiment score generation strategy

Login to Download

---

*Imported from QuantInsti Blog on 2026-04-27*
