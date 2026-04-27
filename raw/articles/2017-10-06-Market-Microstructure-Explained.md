---
title: "Market Microstructure Explained"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/market-microstructure/"
date: "2017-10-06"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Market Microstructure Explained

**来源**: [QuantInsti](https://blog.quantinsti.com/market-microstructure/)  
**日期**: 2017-10-06  
**作者**: QuantInsti

---

## 原文

What Is Market Microstructure?

ByAnupriya Gupta&Viraj Bhagat

Markets microstructure deals with issues of market structure and design, price formation, price discovery, transaction and timing cost, information & disclosure, and investor behavior.  TheNational Bureau of Economic Research (NBER)defines market microstructure as a field of study that is devoted to theoretical, empirical, and experimental research on the economics of security markets. It is the functional setup of amarketfunctioning under a given set of rules & deals.

In this article, we will explore the key topics that fall under the ambit of Market Microstructure.

Traders in Financial Markets

Traders in financial markets can be broadly classified as Brokers and Proprietary traders. Brokers arrange trades for their clients and are known by different names such as agency traders, commission traders, or commission merchants. Proprietary traders on the other hand trade on their own accounts.  These traders take long or short positions in the markets. A long position involves traders owning the trading instrument, while a short position means traders sell the instrument which they do not own. These long and short positions taken by traders can be for different time durations which can vary from milliseconds to days and months.

The Trading Process

Types of Markets

These traders can choose the markets in which they want to place their trades. Exchanges which facilitate trading can be either quote-driven, order-driven or may follow a hybrid market model.

Following are the major market types and characteristics of each type:

Hybrid Market

Allows direct negotiation between counterparties with huge trading volumes

This market is in principle an order-driven market

Order-driven Market

Uses trading rules to arrange their trades

All traders essentially participate equally

Traders placing orders on an order book that are matched following a consistent set of rules. - Priority is an Important Rule

Price is given the first priority & Time is given the second priority in the Order Book

Quote-driven Market

Transaction occurs between:Traders & DealersMarket Maker

Traders & Dealers

Market Maker

Market Makers quote Firm Prices since they play a role in providing liquidity

Buy/Sell a given quantity at quoted Prices

Orders

Market microstructure is mainly about the different order types. These are categorized based on conditions like Price, Time, Quantity, and other conditions. Every exchange will specify the type of orders that are allowed for the market participants. Some of the important orders are specified below:

Price condition - Market Order

A buy or sell order is executed at the best price, established on the market, is obtainable at the time of entering the order and is prevailing in the market at the time of submission of the order

For a market order seller (buyer), the best price is the highest (lowest) bid (ask) posted by the potential buyer (seller).

Price condition - Limit Order

A limit buy (sell) order specifies the maximum (minimum) price at which the trader will buy (sell).

Price limits for buyers (sellers) are normally placed at prices below (above) the current price at which shares can be bought (sold).

Price condition - Stop Order

Stop orders are similar to market orders & are used to buy or sell an asset at the best available price with the intention to limit losses & can be triggered by short-term fluctuations.

Orders are only processed if the market reaches a specific price.

Time condition - Good till Cancelled (GTC) Order

A GTC order is a buy or sell stock at a set price that is active until the investor decides to cancel it or the trade is executed.

If an order does not have a good-till-canceled instruction then the order will expire at the end of the trading day the order was placed.

Time condition - Immediate-or-cancel (IOC) Order

Immediately executed or canceled by the exchange.

Unlike FOK orders, IOC orders allow for partial fills.

Time condition - Day Order

A day order is a limit or stop order that is canceled at the end of the trading day, and will not be active the next morning.

Quantity condition - Disclosed Quantity (DQ)

An order with a DQ condition allows the Trading Member to disclose only a part of the order quantity to the market.

Conditional Orders

An order which is executed only when a specific condition is satisfied.

Priority Rules

When orders are placed by the market participants there are some priority rules based on which these orders are executed by exchanges. Trading Priority Rules can be classified as follows:

Price Priority

Buyers posting higher bids have priority over buyers posting lower bids.

Sellers posting lower asks have priority over sellers posting higher asks.

Based on the principle of price priority, market orders take precedence over all limit orders.

Price priority is a self-enforcing rule because honest traders naturally search for the best prices.

Time Priority

Order that is placed first is executed first.

The principal of time priority means the order put the earliest takes precedence among orders at the same price.

It gives precedence to the traders whose bid or offer first improve the current best bid or offer.

Size Priority

Order with the largest size is executed first.

Requirements for trade size represent another key aspect of designing a set of trading rules.

These aspects may strongly discriminate between wholesale markets, where an order size above a pre-specified threshold is treated, and retail markets, where any order size can be executed.

Types of Trading

Traders employdifferent trading strategiesand trading styles based on their beliefs and knowledge of the markets. Some of these have been covered below.

Momentum Trading:Momentum tradingis a technique in which traders buy and sell according to the strength of recent price trends. Here the traders look to find stocks that are high percentage andvolumemovers of the day, moving significantly in one direction and try to acquire the desired profit by taking positions in such stocks.

Trading based on Mean Reversion:The opposite of Momentum trading is trading based on the concept ofmean reversion strategy. This stems from the concept that stocks which deviate from their historic mean price will tend to revert back over a period of time to their mean value. Traders can take long or short positions to profit from the mean reverting behavior of stocks.

Swing Trading:Swing trading is a type of trading style wherein short-term strategies that are played in the most liquid stocks or indices to take advantage of price swings, either reversing back to the median or fading a rally and last from one day to a few weeks.You can strengthen your skills and strategies by enrolling in a comprehensiveswing trading course.

Day Trading:It is the act of buying and selling a financial instrument within the same trading day, or even multiple times over the course of a day, taking advantage of small price moves, such that all positions are closed before the market closes for the trading day.

Technical Trading:Trading obsessed with charts and graphs, monitoring lines on stock or index graphs for signs of convergence or divergence that might indicate buy or sell signals.

Fundamental Trading:Trading based on fundamental analysis, which examines things like corporate events such as actual or anticipated earnings reports, stock splits, reorganizations or acquisitions.

Scalping:The trading wherein the trader "scalps" a small profit from each trade by exploiting the bid-ask spread by darting in and out of a stock or other asset class multiple times a day to reap a small profit on each trade to add up to the big dough at the end of the day.

Conclusion

Market microstructure has captured interests globally in a dramatic manner in the recent years owing to the rapid transformation of the financial market environment driven by technology, regulation, and globalization. It has grown rapidly as an important subfield of finance, and financial researchers continue to explore this vast insightful field. We will bring more blogs on this topic in our upcoming posts.

Next Step

Learn the various aspects of the portfolio performance evaluation and portfolio performance measurement.In this postwe explain how to compute and analyze the returns generated by the portfolio after a particular time period.

Market microstructure is essential in trading firms because it enhances order execution, cost efficiency, and strategy development. If you’re looking to master how modern markets truly operate, Module 3:Market Microstructure Course— part of the Executive Programme in Algorithmic Trading (EPAT) — is a must. You’ll also learn how to develop and apply execution strategies that minimize market impact, explore core trading strategies like trend following, delta neutral, market making, and statistical arbitrage, and analyze transaction costs to optimize performance. With hands-on exposure to Python and Excel-based tools, the learning is as practical as it is deep.

To explore the full curriculum and gain skills across machine learning, financial computing, quant trading strategies, and more, check out the completeExecutive Programme in Algorithmic Trading (EPAT). Whether you're just starting out or looking to level up, EPAT gives you the structure, depth, and practical expertise to succeed in today’s markets.

---

*Imported from QuantInsti Blog on 2026-04-27*
