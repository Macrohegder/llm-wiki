---
title: "How to Build a Short Selling Strategy That Profits in Bear Markets (and Even in Bull Markets)"
author: "SetupAlpha"
source: "Substack"
url: "https://setup4alpha.substack.com/p/how-to-build-a-short-selling-strategy"
date: "2026-04-27"
topics: ["systematic-trading", "algorithmic-trading"]
---

# How to Build a Short Selling Strategy That Profits in Bear Markets (and Even in Bull Markets)

**来源**: [SetupAlpha](https://setup4alpha.substack.com/p/how-to-build-a-short-selling-strategy)  
**日期**: 2026-04-27  
**作者**: SetupAlpha

---

## 摘要

How to Build a Short Selling Strategy That Profits in Bear Markets (and Even in Bull Markets)
Parabolic Short US Stocks Strategy
SetupAlpha
Mar 27, 2025
13
2
5
Share
Hey, I am the portfolio manager in SetupAlpha.
For the past three years, we've fully automated our trading strategies, managing a portfolio of over 20 diverse strategies. Before that, we operated semi-automated systems. And today I wanted to talk about the short selling startegies.
Most traders panic during bear markets. Stocks are falling, portfolios are bleeding, and fear spreads like wildfire.
That’s natural
. But what if you could do the opposite? What if you could profit when the market is crashing?
Today, I’ll walk you through building a
short-selling strategy
that not only works in bear markets but can also generate pro...

---

## 原文

How to Build a Short Selling Strategy That Profits in Bear Markets (and Even in Bull Markets)
Parabolic Short US Stocks Strategy
SetupAlpha
Mar 27, 2025
13
2
5
Share
Hey, I am the portfolio manager in SetupAlpha.
For the past three years, we've fully automated our trading strategies, managing a portfolio of over 20 diverse strategies. Before that, we operated semi-automated systems. And today I wanted to talk about the short selling startegies.
Most traders panic during bear markets. Stocks are falling, portfolios are bleeding, and fear spreads like wildfire.
That’s natural
. But what if you could do the opposite? What if you could profit when the market is crashing?
Today, I’ll walk you through building a
short-selling strategy
that not only works in bear markets but can also generate profits when stocks are bullish. We’ll go step by step coding it, backtesting it, and analyzing the results.
Whether you trade manually or use
RealTest, Python, or Amibroker
, this strategy is one you can apply when the next downturn hits.
Let’s dive in.
What Is Short Selling?
Short selling flips traditional investing on its head. Instead of
buying low and selling high
, you sell first and buy back later at a lower price (if all goes well). The process looks like this:
Borrow shares
from a broker.
Sell them
at the current market price.
Buy them back
later at a lower price.
Return the borrowed shares
and pocket the difference as profit.
Sounds good? Here are the risks:
Stock borrow fees:
Some stocks are expensive to short due to demand.
Short squeezes:
If a heavily shorted stock spikes,
your losses can be unlimited
.
Liquidity issues:
Not all stocks are easy to borrow or exit quickly.
So, how do we minimize risks and build a
profitable short-selling strategy
?
Filtering Stocks for Short Selling
The first step is picking the right stocks. We use a
universe of Russell 1000 stocks
(both current and past (delisted stocks)) to avoid
survivorship bias
. But not every stock is a good shorting candidate.
Here are the key
filters
:
Stock must be shortable
– Large-cap stocks tend to have more available shares to borrow.
Minimum price of $10
– Avoid illiquid penny stocks that can be hard to get exit.
20-day average volume over 200,000
– Ensures sufficient liquidity.
Trade size = max 1% of the stock’s daily volume
– Prevents slippage and if you trade more than this, you
risk moving the price
.
Exclude biotech stocks
– A single FDA approval can send a biotech stock up
200%+ overnight
, no thanks!
These filters ensure we’re trading
liquid stocks that are easy to short
while avoiding extreme volatility.
Intelligent traders don’t miss the next edge, they
click subscribe!
Subscribe
Entry Rules: When Do We Short?
Shorting works best when stocks move
too far, too fast
, parabolic runs often lead to sharp reversals.
Here are some effective short entry signals:
Price closes above the upper Bollinger Band
Stock exceeds a recent high by X%
ADX or momentum indicators confirm extreme movement
Big gap up
For this strategy, we’re using
Qullamaggie’s Parabolic Short Selling rule
, a proven edge. (I won’t disclose the exact rule here, but you can
download the full RealTest code here
or a text file with the rules if you use Python etc.)
Exit Rules: When Do We Cover?
Short trades should be
short-lived
, holding them too long increases risk due to:
Daily borrow fees eating into profits.
Short squeezes that can wipe out gains.
Stocks generally trending upward over time.
Exit rule for this strategy:
Cover when the close is below the previous close.
Hold max 5 days.
This keeps
win probability high
while avoiding unnecessary exposure.
Backtest Results: Does This Short-Selling Strategy Work?
Backtest includes borrow fees, broker commission and limit extra.
We backtested this strategy using
RealTest
, and the results were impressive.
🔹 It
profited even in bullish markets
by capitalizing on short-term overextensions.
🔹
Performance remained stable
across different market conditions.
🔹
Drawdowns were manageable
, making it a viable addition to a trading portfolio.
Want to see the full code?
Access rules and download the full strategy (realtest)
Click here to access all of the rules and download the full realtest strategy
What’s Next?
This was just
one piece of the puzzle
. Next time, we’ll dive into:
How to combine multiple strategies into one portfolio
for smoother returns.
Risk management techniques
to avoid major drawdowns.
Final Thoughts
A
strong short-selling strategy
gives you an edge when markets fall and can even provide profits in bull markets. By following
structured entry and exit rules, filtering for the right stocks, and managing risk
, you can make shorting a valuable part of your trading arsenal.
Trade Smarter, Save Thousands of Hours
⌛
We handle the
research, coding, and testing
, so you can focus on
growing your portfolio
. ⬇️
All Realtest Strategies
Top industry traders are already subscribing, you should too!
Subscribe
We’re not financial advisors and this is not financial advice.
13
2
5
Share

---

*由 Substack Strategy Tracker 自动抓取*

---

*Imported from Substack on 2026-04-27*
