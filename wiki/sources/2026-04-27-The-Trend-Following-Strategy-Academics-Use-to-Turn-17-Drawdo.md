---
title: "The Trend-Following Strategy Academics Use to Turn -17% Drawdowns Into 7% Annual Returns"
author: "SetupAlpha"
source: "Substack"
url: "https://setup4alpha.substack.com/p/the-trend-following-strategy"
date: "2026-04-27"
topics: ["systematic-trading", "algorithmic-trading"]
---

# The Trend-Following Strategy Academics Use to Turn -17% Drawdowns Into 7% Annual Returns

**来源**: [SetupAlpha](https://setup4alpha.substack.com/p/the-trend-following-strategy)  
**日期**: 2026-04-27  
**作者**: SetupAlpha

---

## 摘要

The Trend-Following Strategy Academics Use to Turn -17% Drawdowns Into 7% Annual Returns
Very Simple Trend-Following Trading Strategy
SetupAlpha
Mar 22, 2026
∙ Paid
19
2
Share
Your stock drops 8%. You sell.
Next month it’s up 12%. Sound familiar?
There’s an academic paper that derives the mathematically optimal trend-following portfolio.
The formula it lands on says something interesting:
The exit doesn’t depend on the individual stock at all.
Every position is controlled by one signal. The trend of the overall market.
I took that formula and turned it into a tradeable strategy.
In this article is will show you:
Entry, exit, ranking, all straight from the paper (+ paper link)
Full trading strategy rules
RealTest script
Here’s the strategy and what it returned.
I break down academic trading...

---

## 原文

The Trend-Following Strategy Academics Use to Turn -17% Drawdowns Into 7% Annual Returns
Very Simple Trend-Following Trading Strategy
SetupAlpha
Mar 22, 2026
∙ Paid
19
2
Share
Your stock drops 8%. You sell.
Next month it’s up 12%. Sound familiar?
There’s an academic paper that derives the mathematically optimal trend-following portfolio.
The formula it lands on says something interesting:
The exit doesn’t depend on the individual stock at all.
Every position is controlled by one signal. The trend of the overall market.
I took that formula and turned it into a tradeable strategy.
In this article is will show you:
Entry, exit, ranking, all straight from the paper (+ paper link)
Full trading strategy rules
RealTest script
Here’s the strategy and what it returned.
I break down academic trading research like this every Sunday. 2,000+ readers get it in their inbox. Subscribe if you want in.
Subscribe
The Core Idea
The market moves together.
When stocks trend up, most of them trend up. When the market rolls over, most stocks follow. Individual stock signals are mostly noise on top of this shared trend.
So instead of watching 500 different exit signals on 500 different stocks, this strategy watches one thing:
is the broad market still trending up?
How do you know? It’s simpler than you think, i’ll soon talk about it.
The entry side is just as clean. When the market trend turns positive, buy the
least volatile
stocks in the S&P 500. Why least volatile? Because in a trend-following context, low-volatility stocks give you the best risk-adjusted exposure. This comes from a concept called risk parity. You want each position contributing roughly equal risk to your portfolio. The simplest way to do that is to favor calm, steady movers over wild ones.
Why This Works
Think about it this way.
You buy a basket of S&P 500 stocks because the market is trending up. One of those stocks drops 8% on an earnings miss. What do you normally do? You sell it.because feels like the right call.
But if the overall market is still healthy and trending higher, that stock will probably recover. The shared market trend pulls everything along. By selling, you locked in a loss that would have turned into a gain.
The academic paper behind this strategy formalizes exactly this intuition. It shows that for a diversified basket of trend-following positions, the
shared market trend is the dominant signal
. Individual stock movements are mostly noise. Reacting to that noise with stop losses, individual exits, trailing stops, actually makes your portfolio worse. Not better.
The paper tested this on 47 futures across stocks, bonds, and currencies from 1985 to 2020 and achieved a Sharpe ratio of over 1.0. That’s strong for any trend-following system.
Know someone who trades individual stock signals and keeps getting stopped out? Send them this.
Share
Results
Backtested on S&P 500 stocks, 2000–2026, $10,000 account:
A Sharpe of 0.75 won’t make headlines on its own. The paper achieved over 1.0. But they could go both long and short across stocks, bonds, and currencies. We’re limited to long-only equities. When the market drops, the paper’s strategy profits from shorts. Ours just goes to cash. That gap is structural, not a flaw in the approach.
Left equity has no slippage and commissions.
Slippage and fees are significantly affecting the strategy.
What Makes This Different
Most trend-following strategies I see work like this calculate a trend for each stock, enter the best ones, exit each one when its own trend fades.
This strategy flips that completely.
There is no per-stock signal.
All 10 positions enter together and exit together, controlled by one market-level switch. The only thing that differs between stocks is their volatility ranking at entry.
Small losse, big winners.
The exit doesn’t depend on the individual stock at all.
Every position is controlled by one signal. The trend of the overall market.
I took that formula and turned it into a tradeable strategy.
Now let’s talk about the paper & strategy itself, next:
The Paper
Strategy Rules
RealTest Script
This post is for paid subscribers
Subscribe
Already a paid subscriber?
Sign in

---

*由 Substack Strategy Tracker 自动抓取*

---

*Imported from Substack on 2026-04-27*
