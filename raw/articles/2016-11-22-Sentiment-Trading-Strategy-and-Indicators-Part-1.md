---
title: "Sentiment Trading Strategy and Indicators – Part 1"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/sentiment-trading-indicators-1/"
date: "2016-11-22"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Sentiment Trading Strategy and Indicators – Part 1

**来源**: [QuantInsti](https://blog.quantinsti.com/sentiment-trading-indicators-1/)  
**日期**: 2016-11-22  
**作者**: QuantInsti

---

## 原文

Sentiment Trading Strategy and Indicators – Part 1

Sentiment Trading Indicators and Strategies - Part 1

“Market decides the price”

Asentiment trading strategyis driven by market sentiment. Before we explore on this topic, let us start with the valuation of a security.

True to the saying, it does not matter whether your valuation of a security is true to its fundamentals and that your valuation model is correct to all its sensitive inputs, what matters is whether the market is a consensus of your valuation and this is what will decide the price of the security. Hence what matters is the price that is decided by the market. These prices are decided by the intrinsic pricing along with the sentiment in the market as a price of a security is a function of its intrinsic value and the behavioral factor of the investor.

It’s a common norm that the price of the security will deviate from its intrinsic value and analysts evaluate the security as being under-priced, at par or overpriced but then simply look back at the saying quoted in the beginning of the article. Having said that, we arrive at our topic of discussion:Market Sentiment.

Market sentiment

A market sentiment is a general attitude and feeling of the investors with regards to the present price and the forecasted price of a security, index or other market instruments. This attitude can be a positive, neutral or a negative one. The basis of this attitude formed is in relation to factors like the macroeconomic reports, world events, fundamental analysis, technical analysis, historical price patterns, sector-wise reports and non-economic factors (news, weather etc.).

Bullish Sentiment

The sentiment is said to be bullish when there is a positive attitude. In a bull market, the prices are expected to move in an upward direction. There is greed in the market when it is being pulled by the bull.

Bearish Sentiment

The sentiment is said to be bearish when there is a negative attitude. In a bear market, the prices are expected to move in a downward direction. There is fear in the market when is being dragged/suppressed by the bear.

Sentiment Trading Strategy

ASentiment trading strategyinvolves taking up positions in the market driven by suchbulls or bears. The sentiment trading strategy can be momentum based i.e. going with the consensus opinion or market sentiment and if it’s a bull we invest high and sell higher or vice versa.

The sentiment trading strategy can even be contrarian ormean reversion tradingi.e. opposite to the market sentiment. A contrarian profits from the theory that when there is certain crowd behavior regarding a security, it gives rise to certain exploitable mispricing (overpricing an already prevailing rise in security) and that a great bull is followed by fall in the prices of the security due to corrections or vice versa. We have talked aboutmomentum-based trading strategiesin our article aboutAlgorithmic Trading Strategy & Paradigms.

“A great bull is followed by fall in the prices of the security due to corrections or vice versa”

Sentiment indicators

ASentiment trading strategyuses different indicators. These sentiment indicators attempt to estimate or gauge the investor activity for any signs of bullishness or bearishness before bull or bear takes hold of the market. These sentimenttrading indicatorsgive you the optimistic or pessimistic indication of a particular security before it is reflected in its prices. These indicators help us to front-run in the market before the sentiment is reflected in the market prices.

Sentiment trading indicators can be qualitative likeopinion polls. There are many companies that provide these services of surveying market professionals and investors to conduct periodic polls and publish them. Some of the opinion polls are Investors Intelligence Advisors Sentiment reports, Market Vane Bullish Consensus, Consensus Bullish Sentiment Index. All these poll investment professionals and reports come from American Association of Individual Investors (AAII) that poll individual investors. These polls are regular and data is compiled over to represent in graphs and visualization to understand a particular sentiment. Most widely used polls are US based polls.

Sentiment trading indicators can even be quantitative which are calculated from market data like security price, traded volume, open interest etc. A few of these indicators are as follows:

Put/Call Ratio

Arms Index or Short-term trading Index (TRIN)

Margin Debt

Mutual funds cash position

Short interest ratio

In this article, we will be giving you an overview of Put Call Ratio and TRIN.

Put/Call Ratio

Put/Call ratio is a very significant sentiment trading indicator. Investors use this while doing sentiment trading and one of the more popular markets among them is the options market since options providesleveragefor trading opportunities, flexibility and the asymmetric payoffs which are considered aslotteryby some (buy/long players usually) and premiums/steady income instruments by some (write/short players usually). However, when someone buys a call option or a put option there is an expectation from the buyer’s side that the market will move in an upward direction or downward direction respectively. Owing to the active trades (volume).

Put/call ratio is one of the most dependable market sentiment indicators.

The put/call ratio = put volume/call volume

Put volumeis the number of the put options bought in the market. Whenever an investor buys a put, the investors expect a fall in the security’s price. WhileCall volumeis the number of call options bought in the market. Whenever an investor buys a call, the investors expect a rise in the security’s price.

Hence a ratio greater than 1 indicates that the put options are being bought more than the call options, which in turn implies that the sentiment is bearish and the investors are expecting the market to go down in near future. A ratio less than 1 indicates that since call options are bought more in the market, the overall sentiment is bullish and the market will go upwards in near future. The trader carries out his trades according to the sentiment trading indicator.

This ratio is generally viewed as a contrarian indicator and the strategy is as follows:

When this ratio is considerably greater than 1, there is an extreme bearish sentiment and a possible oversold market and a correction is likely. Hence BUY. These corrections will take market upwards and a long position at such a bottom will yield a good payoff to our contrarian strategy.

When this ratio is considerably less than 1, there is an extremely bullish sentiment and a possible overbought market and a correction is likely. Hence SELL.

While there are no standard numbers that at which point in the ratio one should buy or sell, a trader should look at the general trend where the ratio moves in the higher or lower value. Once there are spikes or trenches and the ratio deviates from these trading ranges, these are the times one should act and take a position.

All the data providers provide the option volume data of the leading exchanges in the world and this indicator can be easily created on a spreadsheet.

While dealing with the contrarian strategies it is important to check even the fundamentals of the underlying. If there are extremely weak fundamentals and the price drop is justified by it, then a contrarian strategy may not work.

Arms Index or short-term trading index (TRIN)

This index was developed by Richard Arms in 1967, also known as TRading INdex (TRIN), is a common ‘flow of funds’ indicator. By the flow of funds, we mean that this indicator signals the amount of money invested in securities of an index/exchange and help us in interpreting a sentiment. To understand TRIN we first need to understand some common terms:

Advancing Stocks: The number of stocks in an index or exchange that have closed in green or after upside movement from previous day close.

Declining Stocks: The number of stocks in an index or exchange that have closed in red or after downside movement from the previous days close.

Advancing volume: Total volume of these advancing stocks.

Declining volume: Total volume of these declining stocks.

TRIN = [(No. of advancing stocks/ No. of declining stocks) / (Advancing volume/Declining volume)]

When an ARMS index is above 1, it indicates a bearish sentiment. This happens because when the number of stocks closing in red is more than those in green it produces an AD stocks ratio of less than 1 andrationallythis indicates a far greater volume traded in red stocks than green stocks. As a result, the AD volume ratio will even be lesser that the AD stock ratio and the entire ratio becomes greater than 1.

Similarly, when an ARMS index is below 1, it indicates a bullish sentiment. A ratio close to 1 indicates a balanced market. So when there are spikes (upward movements) in TRIN, they coincide with large daily losses in markets and trenches (downward movements) in TRIN coincide with large daily gains in the market.

While scaling this indicator on a chart, we will observe a range in which this indicator For trading purposes the time when we will takecontrarianpositions are :

When this ratio is considerably greater than 1 (somewhere near 3), there is an extreme bearish sentiment and a possible oversold market and a correction is likely. Hence BUY. These corrections will take market upwards and a long position at such a bottom will yield a good payoff to our contrarian strategy.

When this ratio is considerably less than 1(somewhere near 0.5), there is an extremely bullish sentiment and a possible overbought market and a correction is likely. Hence SELL.

While these are not standard numbers, one can always find a trading range and deviations from this moving average on either side can help us to take contrarian positions while trading.

Each sentiment trading indicator and strategy associated with it has its own shortcomings; so as to understand the real sentiment in the market what we can do is take a look at more than 1 sentiment indicators to gauge the market sentiment. If there are conclusive evidence that it is a bull or bear and more importantly (since we are dealing with contrarian strategies), it’s an overbought bull or an oversold bear, we can take appropriate positions in the market and maximize our returns.

Conclusion

In the above write-up, we have discussed only 2 such sentiment trading indicators that are used for analysis in the market. However, there are many such indicators gauging sentiment from breadth, volatility, volume, the flow of funds, shorts or margins taken up in the market and every indicator can be interpreted in one’s own style of investing. We have focused on a contrarian style of investing where we are capitalizing on the general optimism or pessimism prevailing in the market, observing a particular trend, taking up a position at the point where trend reverses and exiting the trade once the reversal reaps profits.

Always remember, when you use a sentiment trading strategy do not use these indicators in isolation. Use indications from more than 1 sentiment indicators and try to understand the fundamentals and rationality behind such patterns, but be brave enough to take up the contrarian position and capitalize on the fear or greed of other investors.If you wish to develop your career in modern methods in finance, be sure to check out this course onSentiment Analysis for finance. It covers various aspects of trading, investment decisions & application using News Analytics, Sentiment Analysis and Alternative Data.

If you wish to develop your career in modern methods in finance, be sure to check out this course onSentiment Analysis for finance. It covers various aspects of trading, investment decisions & application using News Analytics, Sentiment Analysis and Alternative Data.

---

*Imported from QuantInsti Blog on 2026-04-27*
