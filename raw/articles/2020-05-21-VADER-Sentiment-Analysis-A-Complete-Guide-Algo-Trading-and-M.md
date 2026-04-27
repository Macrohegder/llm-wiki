---
title: "VADER Sentiment Analysis: A Complete Guide, Algo Trading and More"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/vader-sentiment/"
date: "2020-05-21"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# VADER Sentiment Analysis: A Complete Guide, Algo Trading and More

**来源**: [QuantInsti](https://blog.quantinsti.com/vader-sentiment/)  
**日期**: 2020-05-21  
**作者**: QuantInsti

---

## 原文

VADER Sentiment Analysis: A Complete Guide, Algo Trading and More

ByNaman Swarnkar

In finance and trading, a large amount of data is generated every day. This data comes in the form of News, Scheduled Economic releases, employment figures, etc. It is clear that the news has a great impact on the prices of stocks.

Every trader takes great efforts in keeping track of the latest news and updates trade calls accordingly. Automating this task provides better trading opportunities.

In this blog, we are going to study what VADER Sentiment Analysis is and how to use it in our Algorithmic Trading Models using Python.

Topics covered:

What is VADER?

What is the accuracy of VADER?

What is Valence Score?

How does VADER calculate the Valence score of an input text?

How does VADER calculate the Valence score of an input sentence?

Compound VADER scores for analyzing sentiment

Python implementation of VADER

Demo using sentences explaining 5 Heuristics

How to use VADER in Trading?

Generating trade calls using VADER and Simple Moving Averages

What is VADER?

VADER is a less resource-consuming sentiment analysis model that uses a set of rules to specify a mathematical model without explicitly coding it. VADER consumes fewer resources as compared toMachine Learningmodels as there is no need for vast amounts of training data.

VADER’s resource-efficient approach helps us to decode and quantify the emotions contained in streaming media such as text, audio or video. VADER doesn’t suffer severely from a speed-performance tradeoff.

VADERstands forValenceAwareDictionary for sEntimentReasoning.

Don't worry if these words don't make any sense to you right now. By the end of this blog, you’ll have a strong grasp of what these words mean.

Moving on to the next section which discusses the classification accuracy of the VADER model and how VADER achieves it.

What is the accuracy of VADER?

Study shows that VADER performs as good as individual human raters at matching ground truth.

Further inspecting theF1 scores(classification accuracy), we see that VADER (0.96) outperforms individual human raters (0.84) at correctly labelling thesentimentof tweets into positive, neutral, or negative classes.

The reason behind this is thatVADERis sensitive to bothPolarity(whether the sentiment is positive or negative) andIntensity(how positive or negative is sentiment) of emotions.

VADER incorporates this by providing aValence Scoreto the word into consideration. This brings us to the next section.

What is Valence Score?

It is a score assigned to the word under consideration by means of observation and experiences rather than pure logic.

Consider the words 'terrible' , 'hopeless', 'miserable'. Any self-aware Human would easily gauge the sentiment of these words as Negative.

While on the other side, words like 'marvellous', 'worthy', 'adequate' are signifying positive sentiment.

According to the academic paper on VADER, the Valence score is measured on a scale from -4 to +4, where -4 stands for the most ‘Negative’ sentiment and +4 for the most ‘Positive’ sentiment. Intuitively one can guess that midpoint 0 represents ‘Neutral’ Sentiment, and this is how it is defined actually too.

How does VADER calculate the Valence score of an input text?

VADER relies on a dictionary that maps words and other numerous lexical features common to sentiment expression in microblogs.

These features include:

A full list of Western-style emoticons ( for example - :D and :P )

Sentiment-related acronyms ( for example - LOL and ROFL )

Commonly used slang with sentiment value ( for example - Nah and meh )

Manually creating a thorough sentiment dictionary is a labour-intensive and sometimes error-prone process. Thus it is no wonder that manyNatural Language Processing(NLP) researchers rely so heavily on existing dictionaries as primary resources.

Without going into deep technical details, here's a two-step process breakdown for creating such a dictionary.

Researchers working on VADER confirmed the general applicability of these lexical features responsible for sentiments using a'Wisdom of theCrowd'(WotC) approach.

WotCrelies on the idea that the collective knowledge of a group of people as expressed through their aggregated opinions can be trusted as an alternative to expert knowledge. This helped them acquire a valid point estimate for the sentiment valence score of each context-free text.

Amazon Mechanical Turk (MTurk)is one such famous crowdsourcing marketplace where distributed expert raters perform tasks like rating speeches remotely.

Valence score of some context-free text are:

Positive Valence: "okay" is 0.9 "good" is 1.9, and "great" is 3.1

Negative Valence: "horrible" is –2.5, emoticon ' :( ' is –2.2, and "sucks" and it's slang derivative "sux" are both –1.5

How does VADER calculate the Valence score of an input sentence?

VADER makes use of certain rules to incorporate the impact of each sub-text on the perceived intensity of sentiment in sentence-level text. These rules are calledHeuristics. There are 5 of them.

NOTE for Advance readers: These heuristics go beyond what would normally be captured in a typical bag-of-words model. They incorporate word-order sensitive relationships between terms.

Five Heuristics of VADER:

Punctuation, namely the exclamation point (!), increases the magnitude of the intensity without modifying the semantic orientation. For example: “The weather is hot!!!” is more intense than “The weather is hot.”

Capitalization, specifically using ALL-CAPS to emphasize a sentiment-relevant word in the presence of other non-capitalized words, increases the magnitude of the sentiment intensity without affecting the semantic orientation. For example: “The weather is HOT.” conveys more intensity than “The weather is hot.”

Degree modifiers(also called intensifiers, booster words, or degree adverbs) impact sentiment intensity by either increasing or decreasing the intensity. For example: “The weather is extremely hot.” is more intense than “The weather is hot.”, whereas “The weather is slightly hot.” reduces the intensity.

Polarity shift due to Conjunctions, The contrastive conjunction “but” signals a shift in sentiment polarity, with the sentiment of the text following the conjunction being dominant. For example: “The weather is hot, but it is bearable.” has mixed sentiment, with the latter half dictating the overall rating.

Catching Polarity Negation, By examining the contiguous sequence of 3 items preceding a sentiment-laden lexical feature, we catch nearly 90% of cases where negation flips the polarity of the text. For example a negated sentence would be “The weather isn't really that hot.”.

Compound VADER scores for analyzing sentiment

The compound score is computed by summing the valence scores of each word in the lexicon, adjusted according to the rules, and then normalized to be between -1 (most extreme negative) and +1 (most extreme positive). This is the most useful metric if you want a single unidimensional measure of sentiment for a given sentence.

As explained in the paper, researchers used below normalization.

where x = sum of valence scores of constituent words, and  α  = Normalization constant (default value is 15)

Python implementation of VADER

VADER has beenported to other programming languagestoo. Standard Python distribution doesn't come bundled with the VADER module. We'll be using the popularPythonpackage installer,pipto do so.

A package contains all the files you need for a module. Modules are Python code libraries you can include in your project. We use the following code in Anaconda terminal to install VADER.

VADER has been included in the NLTK package itself. Module NLTK is used fornatural language processing. NLTK is an acronym forNatural Language Toolkitand is one of the leading platforms for working with human language data. Alternatively one may use.

Demo using sentences explaining 5 Heuristics

Once done with the environment set-up, it's time to get your hands dirty. I'll be using some sentences similar to those used to explain the 5 heuristics and you can yourself see the algorithm throwing different scores.

How to use VADER in Trading?

Historically, traders around the globe have been relying on the news related to relevant instruments and markets in general while making trade calls.

Manual trading was subjected to risk that arises from the personal biases and emotional response that the trader might have due to any news floating around. With the advent ofAlgorithmic Trading, such risks were minimized. As the competition intensified, traders started coming up with new techniques to have an edge over other traders.

Incorporating sentiment analysis into algorithmic trading models is one of those emerging trends. Smart traders started using the sentiment scores generated by analyzing various headlines and articles available on the internet torefinetheir trading signals generated from other technical indicators.

The best part is everything from scraping news to getting sentiment scores can be automated today very easily with a few lines of code. It's up to the trader's creativity, how to make most out of the techniques available.

We'll build a simple model using Simple Moving Averages as our primary technical indicator and then use VADER sentiment scores to refine our trade calls.

Readers who don't know what Simple Moving Average, can check out this blog onMoving Average Trading. Others can jump to the next section.

Generating Trade calls using VADER and Simple Moving Averages

AMD has been releasing some really good products ever since Dr. Lisa Su (alumnus of MIT) took over the CEO position. Due to her strong leadership skills, the company has bounced back from being heavily debt-ridden to being one of the most traded stocks for the past few years in the US S&P 500 index.

I thought it would be interesting to see how the stock moves with its news sentiment in these harsh times when the future seems uncertain.

Using Pandas Datareader to scrape stock data

Using Simple Moving Crossover Strategy to generate trade calls

Introducing Newsapi.org API

News API is a simple HTTP REST API that returns JSON files with breaking news headlines and search for articles from over 30,000 news sources and blogs.

One can search for articles with any combination of the following criteria:

Keyword or phrase, Eg: find all articles containing the word 'AMD'.

Date published, Eg: find all articles published yesterday.

Source name, Eg: find all articles by 'TechCrunch'.

Source domain name, Eg: find all articles published on gizmodo.com.

Language, Eg: find all articles written in English.

One needs an API key to use the API - this is a unique key that identifies your requests.

The best part: They're free for development, open-source, and non-commercial use. You can get onehere.

Generate your free API-key. Save it for future uses. Check thedocumentationto fully explore this wonderful API.

Using developer mode of Newsapi.org to extract news headlines

Getting compound VADER scores for extracted news headlines

Retaining extreme (max and min) compound scores for same Day news headlines

Summing and calculating final VADER scores

Using final compound VADER scores with threshold to generate trade calls

Considering the volatile behavior of markets these days, we'll use 0.20 as threshold value for making trade calls in our model.

Merging Trade Signals with SMA at higher priority and VADER for refining

You did a great job of making it to the end of the blog, so give yourself a pat on the back.

Conclusion

Although we used SMA as our primarytechnical indicator, one won't face any hassle while using VADER with others too.

Clearly, incorporating VADER sentiment analysis gave us an edge over raw SMA model and this speaks about the power of sentiment analysis in Algorithmic Trading.

Note that, in case of conflict we prioritized SMA and took VADER signals only for refining purposes.

Before deploying any algorithmic model, it's very important tobacktest, add safeguards,paper tradeand keep on optimizing.

Now that you know how VADER works, go on and experiment with it. Have Fun!

You have seen how sentiments have driven the markets in recent times. You can use natural language processing to devise new trading strategies using Twitter, news sentiment data in the course onTrading using Twitter Sentiment Analysis.

If you wish to develop your career in modern methods in finance, be sure to check out this course onSentiment Analysis for finance. It covers various aspects of trading, investment decisions & application using News Analytics, Sentiment Analysis and Alternative Data.

Source and References

[1]Using Sentiment Analysis To Trade Equities, EPAT Project, Siddhant R Vaidya, 2019

https://github.com/cjhutto/vaderSentiment

https://psycnet.apa.org/record/2004-20179-000

https://www.mturk.com/

https://pypi.org/project/pip/

https://www.nltk.org/

https://numpy.org/

https://pandas.pydata.org/

https://matplotlib.org/

https://newsapi.org/register

https://newsapi.org/docs/client-libraries/python

https://github.com/mattlisiv/newsapi-python

Moving Average Trading Strategies

Algorithmic Trading using Sentiment Analysis on News Articles

---

*Imported from QuantInsti Blog on 2026-04-27*
