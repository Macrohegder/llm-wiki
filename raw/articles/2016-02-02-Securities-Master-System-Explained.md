---
title: "Securities Master System Explained"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/securities-master-system/"
date: "2016-02-02"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Securities Master System Explained

**来源**: [QuantInsti](https://blog.quantinsti.com/securities-master-system/)  
**日期**: 2016-02-02  
**作者**: QuantInsti

---

## 原文

Securities Master System Explained

By Gasa Mzolo, a Java Developer

As a developer in the world of vast technologies available to us at the click of a button, many of us more often than not, care about the fun part of building a program from scratch and seeing it work, eventually. Hoping that requirements don't change from a higher power that basically fills our hearts with enough stress to, if ever converted to poison, would kill a whole colony of rats. They do however, fill our hearts with glee come payday right?! These higher powers only care about the final product working and not about the art of how it was built. In the same breath, there are those jobs which many programmers don't consider as art, and that is my focus today.

Database design and administration is one of those jobs we would almost always run from. In the world of computational investing, just as in the world of programming, we often focus on the alpha model in order to generate the best back-tested Sharpe ratio prior to putting the system into production. Data, as we all know, or information rather, plays a critical role in the actual program or alpha model's success. Without data or information, it's just a prototype of what could be in future.

A securities master database is just as good as an engine of analgorithmic trading strategyand execution engine. This service helps us obtain, stores, cleans and exports it. Furthermore, according to Michael Halls-Moore, a securities master is an organisation-wide database that stores fundamental, pricing and transactional data for a variety of financial instruments across asset classes. It provides access to this information in a consistent manner to be used by other departments such as risk management, clearing/settlement and proprietary trading.

Some of the instruments that an HFT firm normally considers are the following:

Equities

Equity Options

Indices

Foreign Exchange

Interest Rates

Futures

Commodities

Bonds - Government and Corporate

Derivatives - Caps, Floors, Swaps

Furthermore, Halls-Moore states that securities master databases often have teams of developers and data specialists ensuring high availability within a financial institution.

Reasons why securities masters are used (an expansion)

Risk Management

Accurately assess risk

Optimize credit policy

Reduce operational risk

Trade Execution

Reduce trade failures

Reduce execution costs

Reduce capital expenditures

Regulatory Compliance

Similar to Risk Management

Client Experience

Improve client satisfaction

Improve employee productivity

Automate client on-boarding

Data sets used

EOD data for equities is easy to obtain. There are a number of services providing access for free via web-available APIs:

Yahoo Finance

Google Finance

QuantQuote (S&P500 EOD data only)

EODData (requires registration)

Quandl Python API

It is straightforward to manually download historical data for individual securities but it becomes time-consuming if many stocks need to be downloaded daily. Thus an important component of our securities master will be automatically updating the data set.

Methods of storing data

There are various ways to store data and they are to be highlighted below. Just note that each of these has its own advantages and disadvantages.

Flat-File Storage

Flat-files often make use of the Comma-Separated Variable (CSV) format, which store a two-dimensional matrix of data as a series of rows, with column data separated via a delimiter (often a comma, but can be whitespace, such as a space or tab). For Google pricing data, each row represents a trading day via the OHLC archetype (i.e. the prices at the open, high, low and close of the trading period).

Advantages:

Simplicity

Ability to be heavily compressed for download

Disadvantages:

Poor performance

Lack of query capability

Document Stores

One that a Java developer may least likely use, are document stores. One would find that a wide catalogue of document stores exists, and they differ substantially from RDBMS systems (discussed below), in that there is no concept of table schemas. Instead, there are collections and documents, which are the closest resemblances to tables and records, respectively.

Advantages:

Suited to fundamental or meta data

Disadvantages:

Not well designed for time-series such as high-resolution pricing data

Relational Database Management Systems

These systems are the most liked by developers and of course can be used in conjunction with flat-files. This system, as the name suggests, relates data to one another. It has the capacity to represent financial instruments almost in an object form through the relationships which each table of data has with the next. Some technologies, for those who prefer object orientated languages, such as Hibernate, allow one to map their data through document stores, to a certain table, after having extracted the data from whichever data-source one may have chosen. This already uses a combination of all three methods of storing data.

Advantages

Simplicity of installation

Platform independence

Ease of querying and integration

Performance optimization

Disadvantages

Complexity of customization

Difficulties of achieving higher performance due to heavy stored procedures etc.

Historical Data structure

For simplicity’s sake, it is safer to store/represent data in its object form. This allows for easy database mapping as we have seen the benefits of using relational databases. This allows us to separate different parts of data and put them back together again using certain keys and criterion.

The objects as highlighted by Halls-Moore are as follows:

Exchanges- The ultimate original source of the data

Vendor- A particular data point obtained from

Instrument/Ticker- The ticker/symbol for the equity or index, along with corporate information of the underlying firm or fund.

Price- The actual price for a particular security on a particular day.

Corporate Actions- The list of all stock splits or dividend adjustments (this may lead to one or more tables), necessary for adjusting the pricing data.

National Holidays- To avoid miss-classifying trading holidays as missing data errors, it can be useful to store national holidays and cross-reference.

It is also advised that one combines multiple sources of vendors for accuracy as they use different methods for resolving tickers. This brings us to our next topic, data integrity, evaluation, standardization and accuracy.

Data integrity, standardization and accuracy

Historical pricing data is prone to various errors. Many of these errors rely on manual judgement in order to make a decision on how to proceed. Of course it is possible to automate the notification of such errors with a moderate use of data analytics tools but the solution is much harder to automate. Halls-Moore states that one should, for instance, choose the threshold for being told about spikes in terms of, how many standard deviations to use and over what look-back period. He further notes that, a too high standard deviation will miss some spikes, but too low and many unusual news announcements will lead to false positives. As we understand, these can have a major impact on the results of your Sharpe ratio. These issues should therefore be handled with extreme care.

The following are the common types of errors which one could expect from data vendors as highlighted by Halls-Moore:

Corporate Actions - Incorrect handling of stock splits and dividend adjustments. One must be absolutely sure that the formulae have been implemented correctly.

Spikes - Pricing points that greatly exceed certain historical volatility levels. One must be careful here as these spikes do occur - see the May Flash Crash for a scary example. Spikes can also be caused by not taking into account stock splits when they do occur. Spike filter-scripts are used to notify traders of such situations.

OHLC Aggregation - Free OHLC data, such as from Yahoo/Google is particular prone to 'bad tick aggregation' situations where smaller exchanges process small trades well above the 'main' exchange prices for the day, thus leading to over-inflated maxima/minima once aggregated. This is less an 'error' as such, but more of an issue to be wary of.

Missing Data - Missing data can be caused by lack of trades in a particular time period (common in second/minute resolution data of illiquid small-caps), by trading holidays or simply an error in the exchange system. Missing data can be padded (i.e. filled with the previous value), interpolated (linearly or otherwise) or ignored, depending upon the trading system.

Big Data and GIGO (Garbage In – Garbage Out)

This term was the brainchild of an IBM technician and instructor George Fuechsel and according to a Princeton University article, the term is used to “primarily to call attention to the fact that, computers will unquestioningly process the most nonsensical of input data (garbage in) and produce nonsensical output (garbage out)”. Halls-Moore states that it is crucial that accurate, timely data is used to feed the alpha model otherwise the results will be at best poor or at worst completely incorrect. Consequentially, this leads to large losses if the system is put into production.

Big data takes a vector-like form and is comprised of volume, velocity and variety. Big data differs from regular data in the sense that the data sets are enormous. It therefore cannot be analysed by conventional hardware and software because that only handles megabytes and kilobytes of data whilst big data tools can be used to handle terabyte and petabyte sized data. The speed at which big data is created in terms of automated trading can be really high if your algorithm also considers news publications, Twitter and Facebook feeds. This is also akin to the variety of the data which one gets into their system as the news feeds are unstructured and need to be sorted first before considering any analysis.

Some vendors of machine readable news feeds such as Deutsche Börse with AlphaFlash® attempt to deliver on are:

Flexibility: Information must allow for quick incorporation of the new event. The event could be a specific new economic report, even if this event might only be of market moving significance on one occasion.

Depth and Breadth: Digging deeper into mainstream market events. This is systematically extending the depth and breadth of its offering in everyday circumstances.

Unscheduled events: These could be announcements that are scheduled for a particular day, but no specific time, such as a quarterly earnings update or an unexpected event that a company is obliged to announce by law as it may have material effect on the markets. The data is processed by AlphaFlash® and automatically extracted then sent to clients as a AlphaFlash® message.

Automation processes and improving efficiency

Eradicating any inefficiencies and automating the whole lifecycle of data in your system is one of the core practices of having an automated system. From the acquisition, to the cleaning, to the validation, storage and evaluation and use of data, all parts need to be as efficient as possible because as aforementioned, without data, especially clean data, your software is as good as a prototype.

There are various aspects that one could optimize in terms of how one extracts data, say, from where it is stored. There are many considerations for optimizing queries (in the context of a RDBMS) and I will highlight transaction management. A transaction can be defined as an invisible unit of work comprised of several operations, all or none of which should be performed in order to preserve data integrity. Just as much as a trade execution is a transaction, the operations involved therein are considered a transaction.

The properties of a transaction are as follows:

Atomicity: This implies indivisibility; any indivisible operation (one which will either complete fully or not at all) is said to be atomic.

Consistency: A transaction must transition persistent data from one consistent state to If a failure occurs during processing, the data must be restored to the state it was in prior to the transaction.

Isolation: Transactions should not affect each other. A transaction in progress not yetcommittedorrolled back, must be isolated from other transactions. Although several transactions may run concurrently, it should appear to each that all the others completed before or after it; all such concurrent transactions must effectively end in sequential order.

Durability: Once a transaction has successfully committed, state changes committed by that transaction must be durable and persistent, despite any failures that occur afterwards.

A transaction can thus end in two ways; a commit, meaning the execution in each step of the transaction was successful, or a rollback, which guarantees that none of the steps are executed due to an error in the previous steps.

There are many other aspects of transaction management which will be covered in articles to follow as it falls out of the scope of this particular one.

Finally, automating the download of the data could be done with something as easy as a bat file in Windows, placed in the Task Scheduler, that could start up your software at a certain point and download the data at the end of a trading day for a low frequency trading system, or start-up your software when the markets open. One can then activate email notifications or SMS notifications depending on where your software is located. This will obviously involve all processes inherent in your software.

Architecture of a securities master system

What I personally like about the securities master system and what I believe is crucial to one’s trading software to actually work efficiently, is that it takes on the Model-View-Controller pattern which many programmers are familiar with. The basis of this pattern is that the program is separated into three different sections for reasons such as maintenance and obviously data integrity, to an extent. By having a tiered system, coupling it with the MVC pattern, one significantly reduces the impact that a bad data read could have on the whole algorithm as components are kept in isolation from one another, preventing any clutter.

In terms of the high level architecture of a securities master system, the components which one would expect would be the master data hub, which houses hierarchies and market indices for instance, and it would be surrounded by data sources, a downstream application and some internal systems. The data sources would be those mentioned in the previous heading, these sit on the data integration layer. The downstream application would be the alpha model which sits on the presentation layer.

Some highlights on the features which the architecture, according to Cognizant 20-20 Insights, a leader in IT, consulting and business process outsourcing services that is also part of the S&P500, states that:

Data validation rules must exist in the system to ascertain the accuracy and quality of data sources, particularly from external vendors.

Security provisions must be that create audit trails and guard against unauthorized changes in the data

Conclusion

The reason for a securities master system are mainly for risk management, trade execution, regulatory compliance and client experience, as deducted in this article. There are various data sets which are used which are available from various data vendors such as Google/Yahoo and the evaluation of that data needs to be up to scratch as the data one receives from data vendors is prone to various errors not accounted for in the data that one collects for analysis. Not forgetting the big data that one receives from Twitter, Facebook, RSS feeds and machine readable news feeds such as that from Deutsche Börse.

The manner in which one stores data also leads us to how to represent the data collected from various vendors as the advantages of a relational database management system allows us to store data in almost object form. Of course the RDBMS can also be coupled with other methods of storing the data in order to reach higher levels of efficiency. Following up on efficiency, we discovered that transaction management can help us greatly improve our speed as one can use the four properties, namely atomicity, consistency, isolation and durability to measure the integrity of the data that one reads from their RDBMS. Finally, the architecture of a securities master system plays a crucial role in terms of the different layers involved within the whole system. The model-view-controller pattern that it follows eliminates a whole range of inefficiencies which could hinder a trading system from performing at optimal levels.

Next Step

If you are a retail trader or a tech professional looking to start your own automated trading desk, startlearning algo tradingtoday! Begin with basic concepts likeautomated trading architecture,market microstructure,strategy backtesting systemandorder management system.

Update

We have noticed that some users are facing challenges while downloading the market data from Yahoo and Google Finance platforms. In case you are looking for an alternative source for market data, you can use Quandl for the same.

---

*Imported from QuantInsti Blog on 2026-04-27*
