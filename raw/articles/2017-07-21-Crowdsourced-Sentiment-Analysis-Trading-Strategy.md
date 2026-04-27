---
title: "Crowdsourced Sentiment Analysis Trading Strategy"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/crowdsourced-sentiment-analysis-strategy/"
date: "2017-07-21"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Crowdsourced Sentiment Analysis Trading Strategy

**来源**: [QuantInsti](https://blog.quantinsti.com/crowdsourced-sentiment-analysis-strategy/)  
**日期**: 2017-07-21  
**作者**: QuantInsti

---

## 原文

Crowdsourced Sentiment Analysis Trading Strategy

ByMilind Paradkar

Sentiment analysis trading strategies are not new in the markets. There are a number of resources which are used to develop such strategies, capture the market sentiment and trade based on the signals generated from these strategies.

We also have some financial news portals which use the sentiment data and put up sentiment indicator bars or conduct polls to gauge the sentiment of the visitors on theirs sites. The news site can measure sentiment on various topics and subjects.

I came across one such financial markets portal that provides sentiment indicator bar for all the stocks and I thought of creating a strategy using the sentiment bar. Generally, strategies based onsentiment analysis tradinginvolve collating large data and coming up with a sentiment score which can give profitable trading signals. In this case, I am directly using the sentiment bar as an input to my strategy. So, here goes my simple strategy.

My first step was to pull the Buy/Sell/Hold values for each of the stocks in my list. I wrote a simple program in Python to help me achieve this. Knowledge of HTML and CSS was also required to find the exact location of the sentiment bar and scrape the respective buy/sell/hold values from the HTML page. I used the relevant Python libraries which helped me do all the heavy lifting.

The next step involved storing these values in the form of a Python data frame or in a spreadsheet for further analysis and validation of the values.

What can I do with these values? How do I know whether the sentiment values displayed on the website are a fair representation of the overall market sentiment for the stocks? One experiment that I did was to capture the sentiment score just before the market open and then validate it against the change in stock prices by the end of the market session. The table below gives the single-day results on a sample of stocks. As can be observed the results are not that encouraging.  However, single-day results do not tell us anything about the potential of the strategy and hence, we need to test it over a period of time.

This was one way in which the sentiment score was used. What are the other ways of using the sentiment scores? I have listed some possible ways below to play with the sentiment scores and use the strategy:

Filter the scores and take a position in the stocks for which the scores are at the higher end.

Compare the sentiment scores obtained with sentiment scores displayed on some other site.

Combine this strategy with some other strategy to generate robust trading signals.

I will continue working on this strategy, observe the results over a period of time and try different ways to develop a robust strategy if I can. I will share the results of this crowdsourced sentiment strategy in my future blog. So watch out for my next blog onsentiment analysis trading. Meanwhile, you can read other sentiment trading strategies available on our blog here.

Sentiment Analysis on News Articles using Python

Sentiment Analysis in Trading Using R [WORKING MODEL]You can enroll for thesentiment analysis courseon Quantra which will help you devise new trading strategies using Twitter, news sentiment data. In this course, you will learn to predict the market trend by quantifying market sentiments.Next Step

If you want to learn various aspects ofAlgorithmic tradingthen check out ourExecutive Programme in Algorithmic Trading (EPAT™). The course covers training modules like Statistics & Econometrics, Financial Computing & Technology, and Algorithmic & Quantitative Trading. EPAT™ is designed to equip you with the right skill sets to be a successful trader.Enroll now!

---

*Imported from QuantInsti Blog on 2026-04-27*
