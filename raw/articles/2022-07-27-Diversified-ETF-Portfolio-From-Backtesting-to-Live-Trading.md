---
title: "Diversified ETF Portfolio: From Backtesting to Live Trading"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/diversified-etf-portfolio-project-chee-wai-wan/"
date: "2022-07-27"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Diversified ETF Portfolio: From Backtesting to Live Trading

**来源**: [QuantInsti](https://blog.quantinsti.com/diversified-etf-portfolio-project-chee-wai-wan/)  
**日期**: 2022-07-27  
**作者**: QuantInsti

---

## 原文

Diversified ETF Portfolio: From Backtesting to Live Trading

This project explains the creation and backtesting of a trading strategy using a portfolio of nine sectors ETFs as well as translating this strategy to live-trading on Interactive Brokers (IBKR), using REST API. This project is completely coded on Jupyter Notebook.

The project highlights the importance ofbacktesting trading strategiesto validate their performance before applying them in live markets. By leveraging tools like Jupyter Notebook and APIs, learners can seamlessly transition from strategy development to execution, ensuring practical and efficient implementation.

This article is the final project submitted by the author as a part of his coursework in the Executive Programme in Algorithmic Trading (EPAT) at QuantInsti. Do check ourProjects pageand have a look at what our students are building.

About the Author

CW Wanis a life-long learner with keen interests in business, economics, finance, and data science. He believes algorithmic trading is a subject where all his interests converge. He is currently working in an engineering and tech conglomerate in Singapore.

He holds an Executive MBA from the Quantic School of Business and Technology, a Masters of Science in Business Analytics from NUS Masters of Science in Business Analytics (MSBA), as well as a Master of Science in Financial Economics from Queen Mary University of London.

Project Abstract

This EPAT Final Project comprises two parts.

The first part involves creating and back-testing a profitable strategy using a portfolio of nine SPDR Sector ETFs[1]. I created a long-only daily strategy, with entry/exit signals based on short/long EMA crossovers, and dynamic capital allocation (rebalancing every quarter).

A 10-yearback-test using daily data from January 2012 to December 2021 yields an average annual return of over 30%, a Sharpe Ratio of 1.4, and maximum drawdown of -12%.

The second part involves translating the above strategy to live-trading on Interactive Brokers(IBKR). Using IBKR’s Client Web API[2](RESTful API), and coding completely on Jupyter Notebook[3], I successfully created all the necessary functions to algorithmically execute the daily routine of the above strategy.

This part of the project had been the most grueling and took almost 2 months to complete, but also the most satisfying.

Acknowledgements

I would like to thank my project mentors Rekhit Pachanekar and Danish Khajuria for their valuable advice and guidance for the project, and my Course Support Manager - Laxmi Rawat, for her impeccable support during the EPAT course.

Project Motivation

Before I joined the EPAT course, I asked the sales counsellor if it would be possible, for the Final Project, to create a live algo trading model/portfolio that is similar to something like this:

Before I started EPAT, I had almost zero experience live-trading the markets, but I had some basic data science and coding experience with Python. I also had some experience with Quantopian[5]. But it was shut down before I could learn very much about algorithmic trading.

Hence for me, if nothing else, I would like to take away from the EPAT course the ability to build and manage my own investment portfolio that is at least as good as the ones available for retail investors out there.

Introduction

With this objective in mind, my project comprises two parts:

Part 1: Back-testing a Profitable Strategy– Applying the lessons learnt on Python trading - Object- Oriented Programming[6], Event-based Back-testing[7], and ETF trading[8]- I managed to create a simple but profitable strategy using a portfolio of nine SPDR Sector ETFs.

A 10-year back-test using daily data from January 2012 to December 2021 yields an average annual return of over 30%, a Sharpe Ratio of 1.4, and maximum drawdown of -12%. This strategy appeared to have the potential to outperform the results of the retail fund mentioned above.

Part 2 – Live-trading the Profitable Strategy– Applying the lessons learnt on REST API[9]and Algorithmic Trading System Architecture[10], I managed to code all the necessary functions to algorithmically execute the daily routine of the above-mentioned strategy, using IBKR’s Client Web API to connect to the broker. And I did it all completely on Jupyter Notebook.

The rest of this report is structured as follows:

Section 2 provides more details on the back-testing and results.

Section 3 explains how the live-trading algorithm was designed.

Section 4 concludes.

Part 1: Backtesting

Data Mining

The main instruments selected for this strategy are nine SPDR Sector ETFs:

TICKER

DESCRIPTION

Consumer Discretionary

Consumer Staples

Energy

Financials

Health Care

Industrials

Materials

Technology

Utilities

The rationale for choosing these nine ETFs are as follows:

Simplicity– It is easier to track the overall performance of nine sectors than to track 1,500 companies.

Transaction costs– It is less expensive to trade only 9 instruments instead of 1,500 companies.

Diversification– Each ETF is already a diversified portfolio of the best companies in each sector. A portfolio of ETFs allows even further diversification. Dynamic capital allocation, performed quarterly, allows the portfolio to load up on better performing sectors, “ride the winners”.

We used Yahoo Finance[11](Python yfinance library) to download10 years of daily price data, starting from Jan 2012 to end December2021.

We included SPY to use as a benchmark. The price chart for these 9 ETFs and SPY are as follows:

Description of Strategy

Entry/ExitSignals: We employed a long-only Exponential Moving Strategy (EMA) cross-over strategy: If short-EMA crosses over 1.01x long-EMA, we enter long. Otherwise we exit the trade.

Trade Frequency: We used Daily Close prices to compute the signals. Hence the strategy will be executed once a day. During live-trading, the routine will be performed within the last 5 minutes of each trading session of the US market.

Dynamic Capital Allocation: We track each ETF’s performance quarterly and compute each ETF’s new capital allocation be dividing its quarterly return by the sum of quarterly returns of all the ETFs. This ensures that the better forming the ETF, the more capital will be allocated to it for the next quarter.

Data Analysis

Using Object-Oriented Programming, we performed an event-based back-test using Python on Jupyter Notebook. The results are as follows:

Key Findings

The cumulative 10-yearlog returns for the strategy is 1.58 (or simple return of 385%), which slightly beat its SPY benchmark (log return 1.54, simple return 366%).

The maximum drawdown is -0.13, which translates to -12%. This happened during the onset of the COVID19 pandemic in 2020. As can be observed, the drawdown experienced by SPY was much steeper then.

The Sharpe Ratio achieved is 1.39.

The performance statistics for each ETF are as follows.

We observed that while all the ETFs had positive average profit, only Consumer Discretionary and Tech had over 0.5 hit ratio.

It appears that for the rest, the returns from fewer positive trades far exceeded the losses from negative trades.

Limitations

The limitation of the above-mentioned strategy is that it was too simple, although it gave a good performance. More could be done to improve the strategy or to fine-tune the strategy parameters for better performance.

However, there is a Part 2 where I had to translate the strategy to live-trading, which I believe is more important to accomplish. Strategy improvement could be done after the project is submitted.

Live Trading

Implementation Methodology

Part 2 of the project was to convert the strategy into a live algorithmic trading system.

I already had an account with Interactive Brokers(IBKR), so the first step was to determine which of the methods taught in the EPAT course would I use to connect to IBKR.

IBKR TWS API[12]– This is IBKR’s proprietary, open-source API.

IBridgePy[13]– This is a third-party application designed to look and work like Quantopian’s platform.

IBKR’s REST API– This is IBKR’s industry standard RESTfulAPI.

My trials with the three methods taught in the EPAT are summarized in the table below:

Consideration

TWS API

IBridgePy

REST API

Built-in methods for trading

Quantopian style

Need to create own methods/functions

Files to install

TWS or IB Gateway

“TWS API Install 1016.01.msi file”

TWS or IB Gateway

IBridgePy.zip file (unzip only, no need to install)

TWS or IB Gateway (optional)

clientportal.gw zip file (unzip only, no need to install)

Free version requires manual download new IBridgePy.zip file every 1+ weeks.

US$360 annual subscription required for IBridgePy Premium version

Effort (Ranked)

Medium

Need to learn how to use the built-in methods

Low, if everything goes smoothly

Quantopian style

Need to create own methods/functions

Ease of Troubleshooting

Undetermined

Likely difficult to check what’s wrong ‘under the hood’

No way of checking what’s wrong ‘under the hood’

Error msgs make no sense

Jupyter Notebook friendly?

Undetermined

Need to run an IBridgePy .py file which will then run your own code which must be in a separate .py file

Skill Transferable

to other brokers?

Limited to IBKR, TD Ameritrade and Robinhood

Yes, many brokers offer REST API

It came down toIBridgePy (easy?)vs. REST API (flexibility).

After struggling with IBridgePy’s difficulty to troubleshoot (and annoying need to update the zip file too regularly) for a few weeks, I decided to use the REST API method.

Although it was time-consuming to build my own methods/functions to connect with IBKR, the ability to use Jupyter Notebook (useful for beginner coders!), design them to work exactly the way I want, and troubleshoot errors immediately was invaluable. In addition, the skills learnt in using the RESTAPI is transferable to other brokers(such as Alpaca[14]) and other non-trading purposes.

Trading System Design

Following the EPAT lesson on System Architecture[10], I designed my system in accordance with the basic architecture of anAutomated Trading System:

The Trader App I use is the Jupyter Notebook, a friendly but powerful Python GUI suitable for both beginners and advanced users. Its structure allows me breakup the code into separate parts to test and troubleshoot them individually.

Its ability to include mark-down language makes it easier for me to document every step. My Notebook for this project is thus included in the Annexure of this report.

The rest of the blocks are made up of Python functions. There are three types of functions:

TRADING SEQUENCE Functions– these core functions initialize the trading environment, ensure that the trading session is connected and authenticated with the broker, and call the appropriate ALGO TRADING Functions or IB REST API Functions at the scheduled time in the trading day.

ALGO TRADING Functions– these are designed to execute the specific parts of trading operations. When required, these functions will call IB RESTAPI Functions to communicate with the Broker to get information or place orders.

IB REST API Functions– these are created to send GET or POST requests to IBRK server and receive and process RESPONSES.

The following table lists and describes all the three types of functions written to execute the algo trading strategy, starting with the TRADING SEQUENCE Functions.

The first listed,algo_daily_schedule(), is the main schedule control function that will call the other appropriate TRADING SEQUENCE Functions at the time of the trading day as shown.

The other TRADING SEQUENCE Functions will call the appropriate ALGO TRADING Functions or IB REST API Function as required.

ALGO TRADING Functions will call IB REST API Functions in order to communicate with the Broker.

Types of functions written to execute the algo trading strategy

The various types of functions that are written for this project are as mentioned in the below pdf:

The link to download this PDF is provided at the end of this blog.

Challenges

Coding the trading system using the REST API is a grueling affair.

Many hours were in fact spent writing the IB REST API functions that connect with the broker.

I first had to get the GET or POST structure correct.

Then I had to parse the RESPONSES into a format that is compatible with my system.

Much effort was spent to handle error responses or unexpected responses.

After the project, more work could be done to improve on the error handling.

The limitation is that the quarterly-rebalancing and dynamic capital allocation was not included. Reason for its omission is I did not have 3 months to test it.

The other main limitation is that risk management blocks were not built into the system. Both these limitations will be completed after the project.

Bibliography

https://www.sectorspdr.com/sectorspdr/

https://interactivebrokers.github.io/cpwebapi/

https://jupyter.org/

https://www.syfe.com/equity100

https://en.wikipedia.org/wiki/Quantopian

EPAT Course: DMP-02 Introduction to Object Oriented Programming

EPAT Course: DMP-03/04 Python for Finance

EPAT Course: EFS-06 Understanding Exchange Traded Funds

EPAT Course: TBP-02 REST API

EPAT Course: TIO-01System Architecture for Automated Trading Systems

https://pypi.org/project/yfinance/

https://interactivebrokers.github.io/tws-api/

https://ibridgepy.com/

https://alpaca.markets/

Summary

I have completed two parts for this EPAT Final Project.

In the first part I created and back-tested a profitable strategy using a portfolio of nine SPDR Sector ETFs. A 10-yearback-test using daily data from January 2012 to December 2021 yields:

an average annual return of over 30%,

a Sharpe Ratio of 1.4, and

maximum drawdown of -12%.

These results are encouraging that they seem to outperform the retail fund that inspired the project. However, the strategy is simple and more could be done to improve its performance.

In the second part I translated the above strategy to live-trading on Interactive Brokers (IBKR), using the REST API method and coding completely on Jupyter Notebook.

This part of the project had been the most grueling and took almost 2 months to complete, but also the most satisfying. More work will be done to include the quarterly rebalancing part and also add in Risk Management considerations.

Conclusion

Working on this project has been a fruitful experience, in that I drew the lessons learnt from many EPAT courses. I was able to come up with a profitable strategy, use Python to back-test, and create a algorithmic trading system to execute the strategy live on an IBKR paper-trading account.

From a beginner in this field before I started the course to becoming able to accomplish this after the course (with help from the project mentors, of course!), I believe this testament that the EPAT course is truly excellent!

If you want to learn various aspects of Algorithmic trading then check out thisalgo trading coursewhich covers training modules like Statistics & Econometrics, Financial Computing & Technology, and Algorithmic & Quantitative Trading. EPAT equips you with the required skill sets to build a promising career in algorithmic trading. Enroll now!

File in the download

Complete Python Code of the project

PDF doc - Types of functions written to execute the algo trading strategy

Login to Download

Disclaimer: The information in this project is true and complete to the best of our Student’s knowledge. All recommendations are made without guarantee on the part of the student or QuantInsti®. The student and QuantInsti®disclaim any liability in connection with the use of this information. All content provided in this project is for informational purposes only and we do not guarantee that by using the guidance you will derive a certain profit.

---

*Imported from QuantInsti Blog on 2026-04-27*
