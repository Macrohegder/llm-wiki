# Weekly Research Insights

**原文链接**: https://www.quantseeker.com/p/weekly-research-insights-7ae

**发布时间**: Jun 12, 2025

**抓取时间**: 2026-04-19 22:24:13

---

## 摘要

Weekly Research Insights
A New Signal to Avoid Momentum Crashes
QuantSeeker
Jun 12, 2025
∙ Paid
2
Share
Hi there! In this week’s edition of
Research Insights
, I explore recent research on how to reduce equity momentum crashes. While it’s well known that volatility scaling can help smooth returns and limit drawdowns in long-short momentum strategies, a recent paper proposes a different approach, adjusting for a stock’s distance from its 52-week high. The strategy is shown to roughly double the Sharpe ratio of standard momentum. I put the idea to the test with an empirical analysis.
A New Signal to Avoid Momentum Crashes
Momentum is arguably the most traded anomaly in financial markets. It has been shown to work across asset classes, geographies, and time. In equities, however, momentum str...

---

## 全文

Weekly Research Insights
A New Signal to Avoid Momentum Crashes
QuantSeeker
Jun 12, 2025
∙ Paid
2
Share
Hi there! In this week’s edition of
Research Insights
, I explore recent research on how to reduce equity momentum crashes. While it’s well known that volatility scaling can help smooth returns and limit drawdowns in long-short momentum strategies, a recent paper proposes a different approach, adjusting for a stock’s distance from its 52-week high. The strategy is shown to roughly double the Sharpe ratio of standard momentum. I put the idea to the test with an empirical analysis.
A New Signal to Avoid Momentum Crashes
Momentum is arguably the most traded anomaly in financial markets. It has been shown to work across asset classes, geographies, and time. In equities, however, momentum strategies, especially long-short implementations, are prone to sharp drawdowns, often referred to as momentum crashes.
A substantial body of academic research has explored the causes of these crashes and how to mitigate them. While several methods have been proposed, the most popular and seemingly robust is volatility scaling. Although volatility scaling yields only modest improvements for many other strategies and anomalies, it has been shown to significantly enhance the performance and risk profile of momentum.
An interesting feature of momentum crashes is that they tend to occur at very specific times, typically right after bear markets when volatility is elevated and the market stages a sharp rebound.
Daniel and Moskowitz (2016)
make a compelling case that these crashes stem from the time-varying risk exposures embedded in momentum portfolios. They show that momentum portfolios behave like a short call option during rebounds. This dynamic arises because past losers, often distressed or highly levered, become extremely sensitive to market upswings, occasionally generating triple-digit returns in a single month. The short leg of the strategy effectively "crashes up," inflicting severe losses on the overall portfolio.
Specifically:
After bear markets, the short (loser) leg becomes loaded with high-beta stocks.
When the market rebounds, those stocks rebound the most, inflicting large losses.
Momentum performs worst not during the bear market itself, but when it ends.
This pattern is clearly illustrated in Figure 2 of Daniel and Moskowitz, which plots the cumulative returns of the long and short sides of a standard momentum strategy during two major crash periods: the 1930s and 2009. The short leg shows extreme volatility and sharp outperformance in these episodes, which severely drags down total portfolio returns.
Source: Daniel and Moskowitz, 2016, Momentum crashes, Journal of Financial Economics (Open Access:
CC BY 4.0
).
To mitigate this effect, Daniel and Moskowitz develop a dynamic momentum strategy that adjusts leverage based on predicted momentum returns and volatility. This approach more than doubles the Sharpe ratio of a standard momentum strategy, reduces crash risk, and performs well across equities, bonds, currencies, and commodities.
But what if we could reduce crash risk without relying on dynamic leverage? A more recent paper suggests that sharp drawdowns are largely driven by beaten-down stocks trading far below their 52-week highs. When the market rebounds strongly, these names, often found in the short leg of the momentum strategy, tend to outperform stocks closer to their highs, delivering a blow to portfolio returns.
The paper proposes a method that controls for this 52-week high proximity effect. The strategy nearly doubles the Sharpe ratio of standard momentum and significantly reduces drawdowns, with results that hold across both U.S. and international markets.
I take a closer look at this idea below and test it out-of-sample using various specifications on U.S. stocks.
Continue reading this post for free, courtesy of QuantSeeker.
Claim my free post
Or purchase a paid subscription.

---

*由 Substack Strategy Tracker 自动抓取*
