---
title: "Order Flow Strategy For Crypto Markets [EPAT PROJECT]"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/order-flow-strategy-crypto-markets/"
date: "2018-12-21"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Order Flow Strategy For Crypto Markets [EPAT PROJECT]

**来源**: [QuantInsti](https://blog.quantinsti.com/order-flow-strategy-crypto-markets/)  
**日期**: 2018-12-21  
**作者**: QuantInsti

---

## 原文

Order Flow Strategy For Crypto Markets [EPAT PROJECT]

This article is the final project submitted by the authors as a part of their coursework inExecutive Programme in Algorithmic Trading(EPAT™) at QuantInsti®. Do check our Projects page and have a look at what our students are building.

About the Author

An EPATian,Arsen Zahrayis based in Ukraine and has Master’s Degrees in Computer Science from State University 'Lviv Polytechnics' and from Silesian University of Technology.

The CEO of ‘iathao’, he holds the EPAT Certificate of Excellence.

Project Abstract

I have collected full orderbook history of ETHBTC (Ethereum traded against Bitcoin) as traded on Poloniex and investigated how this data can be used to build a profitable strategy for ETHBTC pair.

I have investigated 2 possible strategies in several possible variations:

Strategy 1

The idea for the first strategy comes from a fact that if you take a group of people and ask them to estimate the number of balls in a jar, the average estimate is going to be better than each individual estimate.

Computing price estimates based on total bids and total asks positions (aggregated in different ways), and using those to filter out trades derived from moving average crossing strategy offers a moderate improvement in performance (as measured by best performing simulated strategy) compared to not using this data

Strategy 2

The second strategy I investigated would exploit the fact that if there is market order disbalance, and the traders, who entered the position at the time of the disbalance, end up in the red, they are likely going to take the losses and thereby move the market in the opposite direction.

The second strategy offers a consistent measurable advantage for a wide range of parameters tested, indicating that it will continue to work in the future. The main drawback of the strategy is that the average advantage provided is around .01% per trade if executed with market orders, which is lower than the commission that needs to be paid on Poloniex to enter and exit the trade.

Another thing that I discovered while writing this project is that evaluating strategy profitability based on best simulation profitability is cherry picking. Plotting strategy profitability as discovered in all simulations using different parameters offers a better picture of how the strategy would perform if we selected a random set of params in the past, which, in turn, offers a better estimate on how the strategy is going to perform in the future

Recommended Reads

The Ichimoku Cloud And Trading Strategy

Aroon Indicator: How To Use It For Cryptocurrency Trading

Cryptocurrencies Trading Strategy With Data Extraction Technique

Disclaimer: The information in this project is true and complete to the best of our Student’s knowledge. All recommendations are made without guarantee on the part of the student or QuantInsti®. The student and QuantInsti® disclaim any liability in connection with the use of this information. All content provided in this project is for informational purposes only and we do not guarantee that by using the guidance you will derive a certain profit.

List of files in the zip archive:

Project Report

Source Code Files

Excel Files

Login to Download

---

*Imported from QuantInsti Blog on 2026-04-27*
