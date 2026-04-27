---
title: "We Got a 73.8% Win Rate From a Trend Indicator - Something Doesn’t Add Up"
author: "SetupAlpha"
source: "Substack"
url: "https://setup4alpha.substack.com/p/73-percent-win-rate-trend-indicator-macd-sp500"
date: "2026-04-27"
topics: ["systematic-trading", "algorithmic-trading"]
---

# We Got a 73.8% Win Rate From a Trend Indicator - Something Doesn’t Add Up

**来源**: [SetupAlpha](https://setup4alpha.substack.com/p/73-percent-win-rate-trend-indicator-macd-sp500)  
**日期**: 2026-04-27  
**作者**: SetupAlpha

---

## 摘要

We Got a 73.8% Win Rate From a Trend Indicator - Something Doesn’t Add Up
A 2026 academic paper proved MACD is suboptimal for trend following
SetupAlpha
Apr 05, 2026
∙ Paid
10
1
Share
How should I use MACD?
Should I even be using it at all?
Most traders think MACD is a trend-following indicator.
Here’s what you need to understand.
A 2026 academic paper tested MACD against a simple moving average on 70 global markets across 33 years of data.
The paper found that MACD does
not outperform a single moving average for trend following.
I took the paper’s exact MACD formula and ran it on S&P 500 stocks. The result was a 73.8% win rate with an average winning trade lasting just 14 days.
MACD on trend following is fine if you enjoy the indicator, but don’t count on it to trend-follow on US equities...

---

## 原文

We Got a 73.8% Win Rate From a Trend Indicator - Something Doesn’t Add Up
A 2026 academic paper proved MACD is suboptimal for trend following
SetupAlpha
Apr 05, 2026
∙ Paid
10
1
Share
How should I use MACD?
Should I even be using it at all?
Most traders think MACD is a trend-following indicator.
Here’s what you need to understand.
A 2026 academic paper tested MACD against a simple moving average on 70 global markets across 33 years of data.
The paper found that MACD does
not outperform a single moving average for trend following.
I took the paper’s exact MACD formula and ran it on S&P 500 stocks. The result was a 73.8% win rate with an average winning trade lasting just 14 days.
MACD on trend following is fine if you enjoy the indicator, but don’t count on it to trend-follow on US equities.
So how do I even use MACD, or should I be using it at all?
Here’s what it’s actually doing instead.
What Is MACD and Why Does Everyone Use It?
MACD stands for Moving Average Convergence Divergence. It is one of the most popular trading indicators in the world.
The idea is simple. You take a fast moving average of price (usually the last 12 days) and a slow moving average (usually the last 26 days). When the fast one rises above the slow one, price is gaining momentum. That is your buy signal.
Most traders use MACD to identify trends. When a stock is trending upward, MACD signals that momentum is building. When it starts breaking down, MACD signals that the trend is weakening.
It sounds logical. The problem is that the research does not always support it.
The Paper That Made Us Question Everything
Sébastien Valeyre published a paper called
“Breaking the Trend: How to Avoid Cherry-Picked Signals.”
His main argument was this. When you build a complex trading signal by combining multiple indicators, you risk accidentally tuning it to fit the past. The strategy looks amazing on historical data. But it only looks good because you unknowingly shaped it around data that no longer exists. This is called cherry-picking.
His conclusion was that a single, simple moving average is the best trend-following signal you can build. Adding more indicators, including MACD, does not help and can actually hurt.
He tested this on 70 markets globally including commodities, bonds, currencies, and stock indices from 1990 to 2023. The simple moving average got a Sharpe ratio of 1.245. MACD got 1.18.
A quick note on Sharpe ratio:
it measures how much return you earn relative to the risk you take. Higher is better. A Sharpe of 1.0 is considered solid. Above 1.2 is excellent.
Simple won and MACD lost.
So I decided to try the paper’s exact MACD formula ourselves, but on S&P 500 stocks instead of global futures markets.
How I Ran the Test
I coded the paper’s MACD formula in a backtesting tool called RealTest.
A backtest means running a strategy on historical price data to see how it would have performed in the past. It is not a guarantee of future results, but it is the best tool I have for evaluating whether a strategy has a real edge.
I tested it on every S&P 500 stock from January 2000 to April 2026. Importantly, I included stocks that no longer exist, companies that went bankrupt or got acquired. Most backtesting tools skip these, which makes results look better than they really are. I did not do that.
The strategy holds up to 10 stocks at a time, sizes each position equally, and accounts for real trading fees and the small cost of not always getting the exact price you expected.
I also ran the paper’s recommended simple moving average at five different speeds, from fast (reacting quickly to price changes) to slow (smoothing out noise), to compare directly.
Right now,
Financial markets are
not in good shape
due to the war between Iran and the U.S.
This negative trend could continue for a long time because of higher
gas prices
and the expectation that rates will stay higher for longer, even if the war ends soon.
Thankfully, this is the best environment for mean-reversion strategies.
Here are some of our strategies that are currently benefiting from these market conditions.
Mean Reversion Strategy
(Last Weeks Return
+3.21%
)
Weekly Buy The Dip Strategy
(YTD Return
+20%
)
Weekly Buy The Dip Strategy VS Spy Buy & Hold (YTD)
Short Term MR
(Larry Connor Style) Strategy (YTD
+10.54%)
Short Term MR (Larry Connor Style) Strategy YTD
Back to the article…
What the Numbers Said
The simple moving average results were exactly what you would expect from a trend-following strategy.
The fastest version, reacting to 50 days of price history, earned a 4.3% annual return and won on only 39.8% of its trades. That is normal. Trend following loses more often than it wins. But the wins are big enough to make it worthwhile.
As I slowed down the moving average, results improved. The slowest version, using 180 days of price history, earned 9.62% per year with a Sharpe ratio of 0.61. Still a low win rate, around 38%. Still normal for trend following.
Now the MACD.
Annual return of 12.21%. Sharpe ratio of 0.74. Win rate of 73.8%.
The annual return and Sharpe beat the best simple moving average result. But the win rate makes no sense at all.
73.8% of trades were profitable. The average winning trade lasted 14 days.
That is not trend following. That is something else entirely.
Why 73.8% Win Rate Is the Wrong Number for a Trend Strategy
Here is the key difference between trend following and mean reversion, explained simply.
Trend following works by being wrong a lot. You buy a stock hoping it will keep rising. Most of the time it does not. You take a small loss and move on. But occasionally you catch a stock that climbs for months and that one trade covers all the losses. Professional trend-following funds typically win on 35 to 45% of their trades. The wins are just much bigger.
Mean reversion works the opposite way. Stocks that drop sharply tend to bounce back. You buy the dip and sell the recovery. You are right more often. But your gains are small and quick.
A 73.8% win rate with 14-day holds is clearly a mean reversion profile. Not trend following.
There is more. When the MACD strategy wins, it holds for 14 days on average. When it loses, it holds for 41 days. In real trend following, losers get cut quickly and winners run for months. Here it is completely backwards.
The strategy also made 3,139 trades over 26 years. The best simple moving average made just 221. That is 14 times more activity, with a completely different style.
Whatever this formula is doing on S&P 500 stocks, it is not following trends.
Why This Matters If You Trade US Stocks
If you have ever added MACD to a trend-following strategy hoping it would improve results and instead saw no improvement or even worse performance, this is likely why. On individual US stocks, MACD does not behave as a trend tool.
And if you decide to run this strategy yourself, understand that it will behave like a mean reversion strategy. It will not diversify your trend-following systems. It will move in line with your other short-term strategies.
Knowing what your strategy is actually doing is more important than knowing its backtest numbers.
I put a lot of time and effort into making systematic trading research concise and actionable for you. Consider supporting my work by becoming a subscriber.
Subscribe
Why US Stocks Behave Differently
Here is a well-known fact about individual US stocks. When a stock drops sharply over two to four weeks relative to the rest of the market, it has a statistically higher chance of bouncing back over the next couple of weeks. This is called short-term mean reversion.
It is one of the most studied and exploited patterns in US equity markets. Dozens of profitable strategies are built around it. The basic idea is simple: buy the dip in a healthy stock and sell the recovery.
The paper’s MACD formula was never designed to exploit this. But the negative 20-day weight accidentally does exactly that.
The formula prefers stocks that have pulled back recently. That is the contrarian short-term component at work. At the same time, the 120-day component acts as a quality check, making sure the stock is still in a solid medium-term uptrend before the strategy enters.
Put those two things together and you get a strategy that buys short-term weakness in stocks that are still fundamentally healthy. It holds for about two weeks, captures the bounce, and exits.
That is mean reversion with a trend filter on top. Not trend following.
That is where the 73.8% win rate comes from. Mean reversion strategies win frequently by design. The trend filter adds an extra layer by keeping the strategy out of damaged or falling stocks, pushing the win rate even higher.
The Full RealTest Code + Strategy Rules
This is the complete code. Survivorship-bias-free data, real trading fees, 0.1% slippage included, 10 positions at a time, S&P 500 stocks only, tested from 2000 to 2026.
This post is for paid subscribers
Subscribe
Already a paid subscriber?
Sign in

---

*由 Substack Strategy Tracker 自动抓取*

---

*Imported from Substack on 2026-04-27*
