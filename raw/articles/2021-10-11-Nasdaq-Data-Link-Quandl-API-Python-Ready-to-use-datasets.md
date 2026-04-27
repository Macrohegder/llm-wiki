---
title: "Nasdaq Data Link | Quandl API, Python & Ready-to-use datasets"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/nasdaq-data-link/"
date: "2021-10-11"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Nasdaq Data Link | Quandl API, Python & Ready-to-use datasets

**来源**: [QuantInsti](https://blog.quantinsti.com/nasdaq-data-link/)  
**日期**: 2021-10-11  
**作者**: QuantInsti

---

## 原文

Nasdaq Data Link | Gaining insights from ready-to-use datasets using Quandl API in Python

ByAnshul Tayal

If you have worked with data before, you know how painstakingly difficult it can be to fetch and convert raw data into a usable format. As data analysts, we are always looking for ready-to-use datasets that can save us time scraping, cleaning, and standardising the data.

Another challenge is extracting information from data has become a needle in a haystack problem because of the quintillion bytes of data generated every day. The haystack keeps growing, so finding the needles keeps getting fiendishly hard. A fundamental challenge with data-driven decisions is to find those few needles.

Given this backdrop when it comes to traditional datasets, the investing/finance world is also looking at unusual data sources. We call them alternative datasets.Marketparticipants are increasingly using alternative data to gain an edge over their competitors.

This article introduces you toNasdaq Data Link, a platform with an extensive collection of traditional and alternative data sources.

This article has the following sections:

What is Quandl and Nasdaq Data Link?

What are the various types of datasets provided by Nasdaq Data Link?

How to access data from Nasdaq Data Link using Quandl API?What is an API call?How to get a free Quandl API key?How to install the Quandl package in Python?How to access various types of datasets using Quandl API in Python

What is an API call?

How to get a free Quandl API key?

How to install the Quandl package in Python?

How to access various types of datasets using Quandl API in Python

Steps to get access to any dataset through Quandl API in Python

Nasdaq Data Link Free subscription vs Nasdaq Data Link Premium subscription

What is Quandl and Nasdaq Data Link?

Quandl was founded in 2011 by Tameer Kalem, a quant who worked in the hedge fund industry for more than a decade. It was created as a “Wikipedia for numerical data” and aimed to extract value from the colossal amount of data available today. In 2018, Nasdaq acquired Quandl to complement its data and analytics business.

In September 2021, Nasdaq launched its new platform Nasdaq data link built using the Quandl infrastructure.

Nasdaq Data Link allows you to access both proprietary data (Nasdaq,Quandl, etc.) and datasets via third parties (ex. Trading Economics,IQ Banker, etc.)

What are the various types of datasets provided by Nasdaq Data Link?

Nasdaq Data Link provides three types of datasets:

Core financial data

Environmental, Social and Corporate Governance (ESG) data

Alternative data

Core financial data

These are the traditionalfinancial datasetsused by investors to analyse and predict behaviour in stock prices. They range from bond yields to stock and forex derivatives to oil databases. There are 223 datasets here.

These datasets are categorised across:

Asset class

Data type

Region

Publisher

Let’s look a little bit further into these categories. The following table shows the distribution of datasets under “Asset class”:

ASSET CLASSES

Equities

Currencies

Interest Rates & Fixed Income

Options

Indexes

Mutual Funds & ETFs

Real Estate

Venture Capital & Private Equity

Economy & Society

Energy

Agriculture

Metals

Futures

The following table shows the distribution of datasets under “Data type.”

DATA TYPES

Prices & Volumes

Estimates

Fundamentals

Corporate Actions

Sentiment

Derived Metrics

National Statistics

Technical Analysis

Others

The following table shows the distribution of datasets under “Region.”

REGION

United States

Europe

Africa

North America

Latin America

Oceania

Middle East

Global

For more details about each dataset, you can gohere.

ESG Data

This section contains datasets that quantifydatasuch as the impact of companies on the environment, health and society. It provides datasets related to GHG emission, insights on natural disasters, biodiversity reports, gender equality metrics, ESG risk metrics, etc. There are a total of 9 datasets in this section.

Datasets in this section are categorised across:

Area of impactEnvironmentSocialCorporate Governance

Environment

Social

Corporate Governance

Sustainable development goals (SDGs)

For more details about each dataset, you can gohere.

Alternative data

This section contains the alternative datasets created using various raw datasets. To give a few examples:

A company’s spending and payments,

Tracking of corporate air travels that can give insights into M&A deals and expansion plans,

Daily data on crop yield forecasts,

Using AI on satellite images to generate a real-time global index of metal supply and much more.

Datasets in this section are categorised based on the following:

Asset classesCommoditiesCurrenciesEquityFixed IncomeReal Estate

Commodities

Currencies

Equity

Fixed Income

Real Estate

Data originBusiness ExhaustConsumer ActivityPrimary ResearchSatellites & SensorsSentiment & InternetOthers

Business Exhaust

Consumer Activity

Primary Research

Satellites & Sensors

Sentiment & Internet

Others

Industry/SectorAutoB2BConstructionEnergyFinanceLogisticsRetailSecurityTechnology

Construction

Energy

Finance

Logistics

Retail

Security

Technology

Investment styleFundamentalQuantitativeTechnicalOthers

Fundamental

Quantitative

Technical

Others

Here’s a catalogue with details of all the alternative datasets provided:Alternative data catalogue.

However, alternative datasets are only available for institutional clients. If you wish to register as an institutional client to access the data, you can gohere.

How to access data from Nasdaq Data Link using Quandl API?

Even though Quandl is just one of the data providers of Nasdaq data link, you can still fetch all the datasets provided by Nasdaq Data Link using a Quandl API (Application Programming Interface) call. Let’s first understand the term “API call”.

What is an API call?

API defines the rules for communication between two systems. To give an analogy, you cannot just go to a printing facility and print a cheque book of a bank for yourself. There’s a procedure that you have to follow.

You go to the bank website, fill up the form, attach your documents and submit. The system then processes in the background, and when your account is ready, account details and the cheque book is handed over to you.

This is precisely how an API works. The bank is the system that we want to communicate with, and we don’t have access to the system’s internals; we can only talk through the API layer, i.e. the bank website where we fill up the form and submit the documents. This is called anendpoint.

While fetching data, you also need an API key for the system to keep a record of your identity, just as you need your bank account no. for any transaction.

An API call provides the inputs to the system to access the data we need. Each system has a different API, just as each bank’s website has a different web address.

For example:

The endpoint for News API ishttps://newsapi.org/v2/everything

Example  of an API call:https://newsapi.org/v2/everything?q=tesla&from=2021-07-26&sortBy=publishedAt&apiKey=API_KEY

In the above example,

Endpoint  - https://newsapi.org/v2/everything

Inputs       - Tesla, start date, i.e. 2021-07-26,

Sort by     -  “Published” and,

API_KEY - Your API-key generated while creating the account

To search for API endpoints, you can go to Programmable Web, one of the largest API directories available. Also, a detailed description of an API can be foundhere.

Now that you have understood how an API call works, let’s see how we can access data from Quandl API using python.

How to get a free Quandl API key?

The first step to fetch data using Quandl API is to generate a free API key by creating an account onNasdaq Data Link. You can find your API key in the account settings section once the account has been successfully created.

Here’s what the account settings section looks like:

How to install the Quandl package in Python?

Use this code to install the Quandl package in Python:

## Install the quandl library
!pip install quandl

How to access various types of datasets using Quandl API in Python?

To access various types of datasets using Quandl API in Python, use this code:

## Importing library
import quandl

Historical stock price data

# Configuring API key
# We use the get() function to fetch the historical stock price data for Tesla
quandl.ApiConfig.api_key = (YOUR-API-KEY-HERE)
tsla = quandl.get('WIKI/TSLA', start_date = "2010-06-29", end_date = "2018-03-27")

A dataframe is returned as output and stored in the variable “tsla”. You can use any ticker symbol instead of ‘TSLA’ to get data for any other stock.

Here’s what the output looks like:

Let’s plot atime seriesgraph to see how price has changed over time.

## Plotting the close price of Tesla
fig = tsla['Close'].plot(grid=True, figsize=(15,8))
fig.set_xlabel("")
fig.set_ylabel("Price", size=18)

Here’s what the output looks like:

We can collapse the data into weekly, monthly, quarterly, etc., using the collapse parameter.

Tsla_monthly = quandl.get('WIKI/TSLA', start_date = "2010-01-01", end_date = "2021-08-01", collapse = “monthly”)

Data from London Bullion Market Association

London Bullion Market Association is an international trade association for gold and silver markets. This is a free dataset.

Here’s how we can access the dataset:

## Getting the silver data from LBMA
quandl.get('LBMA/SILVER', start_date='2011-09-06', end_date='2021-09-08')

Here’s what the output looks like:

Core US Fundamental Data - Sample of a premium subscription dataset

Here’s how you can get the data for Tesla (for example)

## Getting fundamental data for Tesla
quandl.get_table('SHARADAR/DAILY', ticker='TSLA')

Here’s what the output looks like:

Steps to get access to any dataset through Quandl API in Python

These steps will guide you about getting access to any dataset through Quandl API in Python.

Step 1- Go to the Nasdaq Data Link cataloguehere.

Step 2- Select any dataset you find interesting and read the description.

Step 3- Go to the “Usage” section and select python.

Step 4- You’ll be presented with the command to download the data using Quandl API in Python.

Once this is done, you have the dataset at your disposal.

Nasdaq Data Link Free subscription vs Nasdaq Data Link Premium subscription

Quandl provides a large variety of free datasets. However, it also has datasets that come under a paid subscription.

The following are the details:

Nasdaq Data Link provides over 250+ datasets, out of which 40 have free access.

Most premium datasets provide free samples as well.

Users with a free subscription have a limit of 300 calls per 10 seconds, 2,000 calls per 10 minutes and a limit of 50,000 calls per day.

Users with a premium subscription have a limit of 5,000 calls per 10 minutes and a limit of 720,000 calls per day.

Other free and premium subscription features include full API access, downloads in multiple formats, export and visualisation options, and more.

Suggested reads

How to Get Historical Market Data Through Python API

Stock Market Data And Analysis In Python

Turning data into insights and building strategy using Python

Bibliography

Nasdaq Data Link: Publishers

Data organization: Nasdaq Data Link

Conclusion

This article introduced you to a newly launched platform (Nasdaq Data Link) that provides access to ready-to-use traditional and alternative datasets and demonstrated the process of fetching datasets from various publishers (on Nasdaq Data Link) using Quandl API in python.

We looked at various types of datasets offered by Nasdaq Data Link and their accessibility based on subscription.

Getting access to clean data is crucial for building andbacktesting trading strategies, and Nasdaq Data Link with Quandl API will help you in this journey. If you wish to learn more about building trading strategies, check out theQuantitative Trading Strategies and Modelscourse on Quantra.

Disclaimer: All data and information provided in this article are for informational purposes only. QuantInsti®makes no representations as to accuracy, completeness, currentness, suitability, or validity of any information in this article and will not be liable for any errors, omissions, or delays in this information or any losses, injuries, or damages arising from its display or use. All information is provided on an as-is basis.

---

*Imported from QuantInsti Blog on 2026-04-27*
