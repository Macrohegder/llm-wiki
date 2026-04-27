---
title: "Short Term Trading Strategies That Work"
author: "SetupAlpha"
source: "Substack"
url: "https://setup4alpha.substack.com/p/short-term-trading-strategies-that-work-realtest"
date: "2026-04-27"
topics: ["systematic-trading", "algorithmic-trading"]
---

# Short Term Trading Strategies That Work

**来源**: [SetupAlpha](https://setup4alpha.substack.com/p/short-term-trading-strategies-that-work-realtest)  
**日期**: 2026-04-27  
**作者**: SetupAlpha

---

## 摘要

Short Term Trading Strategies That Work
Larry Connors & Cesar Alvarez Book Summary & RealTest Applications.
SetupAlpha
May 21, 2025
11
2
Share
A complete RealTest strategy built exclusively on the highest-probability quantified rules from the widely respected book Short-Term Trading Strategies That Work by Larry Connors and Cesar Alvarez.
Most systematic traders are building strategies on broken foundations.
They focus on breakouts. They cut winners short. They follow popular rules that sound good but fail when tested.
This isn’t just my opinion. It’s backed by hard research, presented in one of the most influential short-term trading books:
Short Term Trading Strategies That Work
, by Larry Connors and Cesar Alvarez.
Today, I’ll show you what this book says, and how I turned its core prin...

---

## 原文

Short Term Trading Strategies That Work
Larry Connors & Cesar Alvarez Book Summary & RealTest Applications.
SetupAlpha
May 21, 2025
11
2
Share
A complete RealTest strategy built exclusively on the highest-probability quantified rules from the widely respected book Short-Term Trading Strategies That Work by Larry Connors and Cesar Alvarez.
Most systematic traders are building strategies on broken foundations.
They focus on breakouts. They cut winners short. They follow popular rules that sound good but fail when tested.
This isn’t just my opinion. It’s backed by hard research, presented in one of the most influential short-term trading books:
Short Term Trading Strategies That Work
, by Larry Connors and Cesar Alvarez.
Today, I’ll show you what this book says, and how I turned its core principles into a working RealTest strategy.
Connors and Alvarez ran extensive tests on market behavior. What they found goes against much of what traders consider “common sense.”
They show that:
Buying after a rally underperforms
Stop-losses often reduce returns
Breakouts offer less edge than pullbacks
Most traders still chase strength, use tight stops, and rely on lagging indicators.
Even worse, many try to backtest these ideas with flawed data or platforms that don’t model real execution.
I’m not just summarizing the book. I’m also showing you how to apply it.
Here are three key principles from Connors and Alvarez that RealTest users should understand deeply:
First, Buy Pullbacks, Not Breakouts.
The authors tested this across thousands of symbols, using more than 20 years of quantified research on short-term price behavior. Pullbacks, especially when the market is in a long-term uptrend, consistently outperform breakout entries.
A few months ago, we did a similar study. You can find this
HERE
.
Second, Use Market Regime Filters.
Strategies in the book typically only trade long when the price is above the 200-day simple moving average. That one rule improves edge, lowers drawdown, and filters out low-probability setups during bear phases.
In this strategy, we're using a condition where price must be above the 200-day SMA. This system is built using only rules from the book. You can download the strategy using the link in the description.
Now watch what happens when we remove the 200-day rule,  the system begins taking trades in very bearish stocks we don’t want.
Third, Gap Down plus Close Down.
The book highlights that when markets gap down
and
close lower, the following session often shows a strong tendency to reverse upward.
In RealTest, we can code this as:
GapDownCloseDown: Open < Close[1] and Close < Open
Let’s include this in our strategy.
It helps smooth the equity curve, but it also reduces the number of trades.
That’s a tradeoff: fewer signals, but higher quality setups.
Stop Loss
The book also talks about stop-losses, and their surprising effect.
Connors and Alvarez found that
stop-losses often reduce the performance
of short-term trading strategies.
They write:
“The overwhelming evidence from these tests shows that stop-losses, in general, hurt system performance.”
They clarify:
“We’re not saying that stop-losses don’t work. We’re saying that stop-losses, when added to short-term trading strategies, generally reduce their performance.”
Why? Because
mean reversion strategies require some price movement against the trade
. If a position is exited too early by a stop, it doesn’t allow the market time to revert.
They add:
“In fact, some of the best strategies we’ve published did not have a stop-loss. Instead, they used a time exit or a price-based profit target.”
They recommend:
Avoid using arbitrary stop-loss percentages
Consider
not using stops at all
in mean reversion strategies
Use structured exits, such as:
Holding for a fixed number of days (
Barsheld == 5
)
Exiting after a price bounce (
Close > Avg(Close,10)
)
Using trailing profit-based exits (RSI limit price (
rrsi(2,90)
))
Finally, the book also introduces a
lesser-known volatility rule
that helps identify high-probability mean reversion setups.
We do not reveal the exact rule, but this rule is included in this RealTest strategy.
This equity curve includes IBKR trading cost + limit extra buffer.
Save your time, skip the coding.
Download a strategy that’s statistically proven.
Download this RealTest system
HERE
.
You’ll see every rule used in this system, based directly on the book.
And if you enjoy this kind of breakdown, subscribe and drop a comment with the next book you want decoded for systematic traders.
Subscribe for more!
Subscribe
Disclaimer:
This book is not affiliated with or endorsed by Larry Connors or Cesar Alvarez. It does not reproduce the full content of the book.
https://setupalpha.com/
Got 30 seconds?
Answer 3 quick questions to shape what we build next at SetupAlpha.
Start survey →
11
2
Share

---

*由 Substack Strategy Tracker 自动抓取*

---

*Imported from Substack on 2026-04-27*
