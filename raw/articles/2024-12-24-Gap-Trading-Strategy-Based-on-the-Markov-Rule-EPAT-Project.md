---
title: "Gap Trading Strategy: Based on the Markov Rule | EPAT Project"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/epat-project-gap-trading-strategy-based-on-the-markov-rule/"
date: "2024-12-24"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Gap Trading Strategy: Based on the Markov Rule | EPAT Project

**来源**: [QuantInsti](https://blog.quantinsti.com/epat-project-gap-trading-strategy-based-on-the-markov-rule/)  
**日期**: 2024-12-24  
**作者**: QuantInsti

---

## 原文

Gap Trading Strategy: Based on the Markov Rule | EPAT Project

By:Hetansh GosarThe trading strategy focuses on gap trading in Indian equities, specifically targeting stocks with lower volatility and avoiding high-volatility market conditions. This long-only approach involves entering positions at the day’s close and exiting at the next day's open. As Indian markets mature and more stocks become eligible for trading, the strategy’s performance improves over time, yielding better results and a higher Sharpe ratio. Gap trading offers greater predictability and significantly reduces volatility, making it a reliable and effective approach for consistent returns.

This article is the final project submitted by the author as a part of his coursework in the Executive Programme in Algorithmic Trading (EPAT) at QuantInsti. Do check ourProjects pageand have a look at what our students are building.Other EPAT Project publications on Gap Trading Strategy and Markov Rule are listed below:

Market Regime Detection with Hidden Markov Model[EPAT PROJECT]  (Year: 2020)

About the Author

My name is Hetansh Gosar, a 23-year-old from Ahmedabad. I hold a Bachelor's degree in BusinessAdministration and have successfully completed all three levels of the Chartered Market Technician (CMT) program. I will be eligible for the CMT charter upon completing three years of industry experience. For the past two years, I have been working as a Technical Researcher, gaining valuable expertise in market analysis and trading strategies.

EPAT batch: #61Certification status: Certification of ExcellenceMentor:Rekhit PachanekarConnect with me: www.linkedin.com/in/hetansh-gosar

Strategy Idea

The idea is to enter the market when the conditions are satisfied:

If today’s candlestick body is greater than yesterday’s candlestick body (this is to indicate an increase in momentum).

If today’s close is greater than the open (this is to indicate a positive momentum).

Today’s percentage change should be less than 2%(in order to avoid trades during extreme volatility such as the Great Recession or COVID-19).If these three conditions are satisfied then we enter on today’s closing and exit on the next day’s opening. The graph shows the parameters of when to take a trade.

Motivation

The motivation for the strategy comes from the idea that a strong momentum that persisted during the day would continue even when the markets were closed and not being traded. Hence there would be a gap in the opening of the next day. We would like to capture that gap by entering right before the close and exiting on the open. We use long trades only as in case of up moves, there is predictive power of the previous day, while not the same with down moves.

As there is no certainty of continuation in trend in case of down moves, there might be a change of sentiment and we won't be able to capture the gap. We use the true range of candles as the true range can show us what the intrinsic strength of the day was.

When there is an increase in the size, we can determine that the momentum has increased for the day which would mean a strong enough momentum. When there is too much volatility in markets, such as during the crash of COVID-19 or the great recession, the predictive power of the previous day is lost and there is a lot of unnecessary movement in the market.

To avoid that, we do not take trades that are greater than 2% in closing as that would be a lot of volatility, and also with such great returns on the day of entry, there are chances of a bit of retracement on the next day. By using just gaps to trade, we do not get a lot of returns and a lot of returns, but we get more stable returns. We can use leverage to magnify the returns, and we aimed to have a better-adjusted hit ratio, so we could have a smoother equity graph.

Project Abstract

The strategy is designed in a way that targets the trade gap. It generates an entry on closing and the exit is at the next open. This strategy best works for low-volatility stocks (equities with less ATR/price ratio) in Indian markets.

The findings suggest that there was a decent profit with less volatility, theoretically, in backtesting.

Dataset

We use nifty daily data as our trading dataset.

Data Mining

The data we are using is of the stock itself and nifty data along with it. The strategy requires stock data for entering at close price, exiting at open price, and high, low and close data for ATR. While nifty data is required for its ATR since we have used a filter in which if the market is extremely volatile, we stay cash and do not trade.

The data is downloaded from yfinance, which is a part of the code of the testing strategy itself. So, when the function of the backtesting strategy is run, both the data (nifty and stock) will be downloaded and then the backtesting will take place.

After the backtesting is done, there is a different set of code which is of pyfolio, run to have results.

The coding is done in Python completely.

The 10 stocks used to create a portfolio are:

Bharti-airtel

Coal India

Colpal

Reliance

Solaris Inds

Zydus Lifescience

The testing was done over a period of 10 years, from 2014-1-1 to 2024-1-1. It doesn’t make sense to test before a certain number of years, since the markets were very volatile back then, but had eventually become less volatile. As our markets are maturing, there are more and more stocks becoming less volatile and they would then be tradable.

Data Analysis

What we found out is that usually stocks gave a decent return, usually greater than 15% CAGR, with around a max drawdown of 10 to 15 per cent.

If we create a portfolio of the ten stocks mentioned above, the CAGR comes out to be around 24.9%, cumulative returns 771.6%, annual volatility around 4.1%, and max drawdown around 2.4%.

Key Findings

The strategy works well when the markets are in a low volatility phase. The stocks should be in general low volatile and not necessarily up trending. This strategy works best in a portfolio, as there is not much systematic risk and more unsystematic risk, so when trading a whole portfolio, the risk-adjusted returns are pretty strong. The theoretical sharp ratio is coming out to be more than 5, which is because of extremely low volatility, but it needs to be tested in live markets as there are a few limitations of the strategy as well.

Challenges/Limitations

One of the greatest challenges is to get the open price, as the strategy is tested on past data, we have a clear opening price, but we need to capture the opening price in order to get the exact same results.

The transaction costs are not included in the backtest results, which could be pretty high as we enter and exit trades on an everyday basis.

Conclusion

The strategy theoretically works well. It has good enough returns for the amount of risk we take. The limitations might be crucial and should be considered as they may skew the results drastically. But if there is not much change in returns, and because of the low volatility, we might still be able to get a decently or well-performing strategy after application. A benefit of this strategy is that it is applied to equity, so we do not face challenges of derivatives, and as time goes by, and markets mature, the pool of stocks for us to choose from increases, so we can deploy more capital in it with less impact cost.

This strategy might be good for someone looking for a moderate return with less risk. For someone willing to risk more and bear the expense of interest, getting leverage is an option. The strategy has stable returns especially in portfolio format so taking leverage should not be that difficult. With the CAGR of the portfolio being around 25%, it did beat the index well, also with much lesser volatility. It does not affect much if the markets are not bullish, it might create some volatility in our portfolio returns but might not face huge drawdowns.

Annexure

The following is the code used to generate the strategy function used to create a “pandas” dataframe with strategy returns in it:

def strategy(stock,start_date,end_date):

# Downloading data

df1 = yf.download(stock, start = start_date, end = end_date, auto_adjust = True)

data = yf.download('^NSEI', start = start_date, end = end_date)

# Creating ATR and volatility filter on nifty

data['atr'] = ta.ATR(data['High'], data['Low'], data['Close'], 5)

data['atr_perc'] = data['atr']/data['Close']

# Merging data of nifty and stock

df = df1.merge(data[['atr_perc']], left_index=True, right_index=True, how='left')

# Creating returns

df['returns'] = np.log(df['Close']/df['Close'].shift())

# Creating true range

df['true_range'] = np.maximum.reduce([df['High']-df['Low'],

df['High']-df['Close'].shift(),

df['Close'].shift()-df['Low']])

# Creating conditions of entry

df['condition'] = np.where( (df['true_range'] > df['true_range'].shift()) &

(df['returns'] < 0.02) &

(df['returns'] > -0.02), 1, 0)

# Creating signal with the help of condition

df['signal'] = np.nan

df['signal'] = np.where((df['condition'] == 1) & (df['returns'] > 0), 1,

np.where((df['condition'] == 1) & (df['returns'] < 0), 0, np.nan))

df['signal'] = df['signal'].ffill()

# A filter for avoiding volatile periods

df['signal'] = np.where(df['atr_perc'].shift() > 0.03, 0, df['signal'])

# Calculating the returns on trading the gap

df['o_c_returns'] = np.log(df['Open']/df['Close'].shift())

# getting returns

df['strategy_returns'] = df['signal'].shift() * df['o_c_returns']

df['cum_strategy_returns'] = df['strategy_returns'].cumsum()

df['b&h_returns'] = df['returns'].cumsum()

return df

File in the download

The Python codes for implementing the strategy are provided in the downloadable button including data download,  code used to generate the strategy function used to create a “pandas” data frame with strategy returns in it.

Login to Download

Next Steps for you

Want to know how EPAT equips you with skills to build your trading strategy in Python? Check out theEPAT course curriculumto find out more.

Gap Trading Strategy is one of the simplest trading strategies for day traders. Check out the course onDay Trading Strategies for Beginnersif you are interested in day trading.

If you are interested in learning more about Gap Trading and Markov Rule, read the blogs here:

Markov Model - An Introduction

Intro To Hidden Markov Chains

Introduction To Monte Carlo Analysis

Explore EPAT trading projects on various topics:

Crypto Perpetual Contract Pair Trading

Time-Series and LSTM Models: A Comparative Study for Stock Price Prediction

Optimizing Exit Conditions Using a Variable Take Profit and Stop Loss

Dispersion trading strategy in the Indian markets

Disclaimer:The information in this project is true and complete to the best of our Student’s knowledge. All recommendations are made without guarantee on the part of the student or QuantInsti®. The student and QuantInsti® disclaim any liability in connection with the use of this information. All content provided in this project is for informational purposes only and we do not guarantee that by using the guidance you will derive a certain profit.

---

*Imported from QuantInsti Blog on 2026-04-27*
