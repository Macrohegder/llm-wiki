---
title: "Quantitative Trading Strategy Using Quantstrat Package in R: A Step by Step Guide"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/quantitative-trading-strategy-using-r/"
date: "2016-01-20"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Quantitative Trading Strategy Using Quantstrat Package in R: A Step by Step Guide

**来源**: [QuantInsti](https://blog.quantinsti.com/quantitative-trading-strategy-using-r/)  
**日期**: 2016-01-20  
**作者**: QuantInsti

---

## 原文

Quantitative Trading Strategy Using Quantstrat Package In R: A Step By Step Guide

In this post, we will be building atrading strategy using R. Before dwelling into the trading jargons using R let us spend some time understanding what R is. R is an open source. There are more than 4000 add-on packages, 18000 plus members of LinkedIn’s group and close to 80 R Meetup groups currently in existence. It is a perfect tool for statistical analysis especially for data analysis. The concise setup of Comprehensive R Archive Network knows as CRAN provides you the list of packages along with the base installation required. There are lot of packages available depending upon the analysis needs to be done. To implement the trading strategy, we will use the package called quantstrat.

Four Step Process of Any Basic Trading Strategy

Hypothesis formation

Testing

Refining

Production

Our hypothesis is formulated as “market is mean reverting”.Mean reversion tradingis a theory that suggests that the prices eventually move back to their average value. The second step involves testing the hypothesis for which we formulate a strategy on our hypothesis and compute indicators, signals and performance metrics. The testing phase can be broken down into three steps, getting the data, writing the strategy and analyzing the output. In this example we consider NIFTY-Bees. It is anexchange-traded fundmanaged by Goldman Sachs. NSE has huge volume for the instrument hence we consider this. The image below shows the Open-High-Low-Close price of the same.

We set a threshold level to compare the fluctuations in the price. If the price increases/decreases, we update the threshold column. The closing price is compared with the upper band and with the lower band. When the upper band is crossed, it is a signal for sell. Similarly, when the lower band is crossed, it is a buy signal.

The coding section can be summarized as follows,

Adding indicators

Adding signals

Adding rules

A helicopter view towards the output of the strategy is given in the diagram below.

Thus our hypothesis that market is mean reverting is supported. Since this is back-testing we have room for refining the trading parameters that would improve our average returns and the profits realized. This can be done by setting different threshold levels, more strict entry rules, stop loss etc. One could choose more data for back-testing, use Bayesian approach for a threshold set up, take volatility into account.

Once you are confident about thetrading strategybacked by the back-testing results you could step into live trading. The production environment is a big topic in itself and it’s out of scope in the article’s context. To explain in brief this would involve writing the strategy on atrading platform.

As mentioned earlier, we would be building the model using quantstrat package. Quantstrat provides a generic infrastructure to model and backtest signal-based quantitative strategies. It is a high-level abstraction layer (built on xts, FinancialInstrument, blotter, etc.) that allows you to build and test strategies in very few lines of code.

The key features of quantstrat are,

Supports strategies which include indicators, signals, and rules

Allows strategies to be applied to multi-asset portfolios

Supports market, limit, stoplimit, and stoptrailing order types

Supports order sizing and parameter optimization

In this post we build a strategy that includes indicators, signals, and rules.

For a generic signal based model following are the objects one should consider,

Instruments- Contain market data

Indicators- Quantitative values derived from market data

Signals- Result of interaction between market data and indicators

Rules- Generate orders using market data, indicators and signals.

Without much ado let’s discuss the coding part. We prefer R studio for coding and insist you use the same. You need to have certain packages installed beforeprogramming the strategy.

The following set of commands installs the necessary packages.

install.packages("quantstrat", repos="http://R-Forge.R-project.org")
install.packages("blotter", repos="http://R-Forge.R-project.org")
install.packages("FinancialInstrument", repos="http://R-Forge.R-project.org")

Once you have installed the packages you import them for further usage.

require(quantstrat)

Read the data from csv file and convert it into xts object.

ym_xts

We initialize the portfolio with the stock, currency, initial equity and the strategy type.

stock.str='NSEI' # stock we trying it on
currency('INR')
stock(stock.str,currency='INR',multiplier=1)
initEq=1000
initDate = index(NSEI[1])#should always be before/start of data
#Declare mandatory names to be used
portfolio.st='MeanRev'
account.st='MeanRev'
initPortf(portfolio.st,symbols=stock.str, initDate=initDate)
initAcct(account.st,portfolios='MeanRev', initDate=initDate)
initOrders(portfolio=portfolio.st,initDate=initDate)

Add position limit if you wish to trade more than once on the same side.

addPosLimit(portfolio.st, stock.str, initDate, 1, 1 )

Create the strategy object.

stratMR

We build a function that computes the thresholds are which we want to trade. If price moves by thresh1 we update threshold to new price. New bands for trading are Threshold+/-Thresh2. Output is an xts object though we use reclass function to ensure.

THTFunc<-function(CompTh=NSEI,Thresh=6, Thresh2=3){
numRow(tht+Thresh)){ tht<-xa[i]}
   if(xa[i]<(tht-Thresh)){ tht<-xa[i]}
   xb[i]

Add the indicator, signal and the trading rule.

stratMR

Run the strategy and have a look at the order book.

out<-try(applyStrategy(strategy=stratMR , portfolios='MeanRev') )
# look at the order book
getOrderBook('MeanRev')
end_t<-Sys.time()

Update the portfolio and view the trade statistics

updatePortf('MeanRev', stock.str)
chart.Posn(Portfolio='MeanRev',Symbol=stock.str)
tradeStats('MeanRev', stock.str)
View(t(tradeStats('MeanRev')))
.Th2 = c(.3,.4)
.Th1 = c(.5,.6)
require(foreach)
require(doParallel)
registerDoParallel(cores=2)
stratMR<-add.distribution(stratMR,paramset.label='THTFunc',component.type= 'indicator',component.label = 'THTT',
                         variable = list(Thresh = .Th1),label = 'THTT1')
stratMR<-add.distribution(stratMR,paramset.label='THTFunc',component.type= 'indicator',component.label = 'THTT',
                         variable = list(Thresh2 = .Th2),label = 'THTT2')
results<-apply.paramset(stratMR, paramset.label='THTFunc', portfolio.st=portfolio.st, account.st=account.st, nsamples=4, verbose=TRUE)
stats

Here is the complete code

require(quantstrat)
ym_xts (tht+Thresh)){ tht<-xa[i]}
   if(xa[i]<(tht-Thresh)){ tht<-xa[i]}
   xb[i]

Next Step

Once you are familiar with these basics you could take a look at how to start usingquantimod package in R. Or in case you're good at C++, take a look at an examplestrategy coded in C++.

If you’re a retail trader or a tech professional looking to start your own automated trading desk, startlearning algo tradingtoday!  Begin with basic concepts likeautomated trading architecture,market microstructure,strategy backtesting systemandorder management system.

Completing analgo trading coursecan provide structured guidance and help you move from a trading idea to a tested and executable strategy more efficiently.

Disclaimer: All investments and trading in the stock market involve risk. Any decisions to place trades in the financial markets, including trading in stock or options or other financial instruments is a personal decision that should only be made after thorough research, including a personal risk and financial assessment and the engagement of professional assistance to the extent you believe necessary. The trading strategies or related information mentioned in this article is for informational purposes only.

---

*Imported from QuantInsti Blog on 2026-04-27*
