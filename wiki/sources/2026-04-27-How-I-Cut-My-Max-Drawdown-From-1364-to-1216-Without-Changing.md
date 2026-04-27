---
title: "How I Cut My Max Drawdown From -13.64% to -12.16% Without Changing the Signal (Full Backtest + Code)"
author: "SetupAlpha"
source: "Substack"
url: "https://setup4alpha.substack.com/p/how-i-turned-57876-into-69534-with-the-same-strategy"
date: "2026-04-27"
topics: ["systematic-trading", "algorithmic-trading"]
---

# How I Cut My Max Drawdown From -13.64% to -12.16% Without Changing the Signal (Full Backtest + Code)

**来源**: [SetupAlpha](https://setup4alpha.substack.com/p/how-i-turned-57876-into-69534-with-the-same-strategy)  
**日期**: 2026-04-27  
**作者**: SetupAlpha

---

## 摘要

How I Cut My Max Drawdown From -13.64% to -12.16% Without Changing the Signal (Full Backtest + Code)
How Adding One Rule Improved Every Single Metric in My Backtest
SetupAlpha
Feb 22, 2026
∙ Paid
10
1
Share
Hello Traders,
Last week’s strategy ran a Sharpe of 1.07, a max drawdown of -13.64%, and a win rate just under 70%. Those numbers held up well over 11 years of data.
But I kept running the test. One question wouldn’t go away: when the system steps aside from equities, the capital sits in cash. Cash earns nothing. Is there a better destination?
I added one extra asset. Same signal, no new parameters.
Max drawdown dropped from
-13.64% to -12.16%.
MAR ratio annual return divided by max drawdown improved
25%
, from 0.96 to 1.20. Annual return went from 13.13% to 14.57%. Net profit on a $20,...

---

## 原文

How I Cut My Max Drawdown From -13.64% to -12.16% Without Changing the Signal (Full Backtest + Code)
How Adding One Rule Improved Every Single Metric in My Backtest
SetupAlpha
Feb 22, 2026
∙ Paid
10
1
Share
Hello Traders,
Last week’s strategy ran a Sharpe of 1.07, a max drawdown of -13.64%, and a win rate just under 70%. Those numbers held up well over 11 years of data.
But I kept running the test. One question wouldn’t go away: when the system steps aside from equities, the capital sits in cash. Cash earns nothing. Is there a better destination?
I added one extra asset. Same signal, no new parameters.
Max drawdown dropped from
-13.64% to -12.16%.
MAR ratio annual return divided by max drawdown improved
25%
, from 0.96 to 1.20. Annual return went from 13.13% to 14.57%. Net profit on a $20,000 account increased by
$11,658
over the same test period.
Final strategy
This article shows the strategy, why it works, and gives you the full updated RealTest code + strategy rules.
If you haven’t read
last week’s article
yet, start there this builds directly on it.
Ray Dalio stood at the
World Economic Forum
in Davos in January 2020 and said, on live television:
“Cash is trash. Get out of cash. There’s still a lot of money in cash.”
Two months later, SPY was down 34%. And something else was up double digits.
People filed Dalio’s quote as a January hot take and moved on. But he wasn’t talking about market timing. He was pointing at a capital problem every systematic trader eventually runs into.
When a system steps aside from equities, the capital has to go somewhere. Most of the time it defaults to cash. And cash earns nothing while the market keeps rotating.
When the market is in a risk-off environment where is the money actually going?
Not “what’s the safe place to hide.” Where is the active rotation happening?
A Paper
A Quantitative Approach to Tactical Asset Allocation Mebane T. Faber May 2006, Working Paper Spring 2007, The Journal of Wealth Management
In 2006, Meb Faber published a white paper called “
A Quantitative Approach to Tactical Asset Allocation.
” It became one of the most downloaded investment research papers ever written.
The central finding was this: a simple, rule-based system that rotates between asset classes based on trend signals can produce equity-like returns with bond-like drawdowns. The key word is rotates.
Faber’s work showed that different asset classes take turns leading during different macro environments. When one is in a downtrend, another is almost always in an uptrend. Capital has somewhere to go, you just have to build the system to follow it.
It shows up in the actual historical data, cycle after cycle.
In the 2020 COVID selloff, while U.S. equities were collapsing, IEF the 7-10 year Treasury ETF posted a full-year return of over 10%. TLT, the longer-duration version, returned 17.9% for the year. When equities panic, capital does not disappear. It rotates into safety.
The 2022 rate cycle broke this pattern. Bonds got hit alongside equities. That’s a real caveat and one worth taking seriously. But across the full window of data we’re working with 2015 to today the rotation holds.
The System Already Knows
Here’s what struck me when I ran this next backtest.
The system we built
last week
already has the signal. It identifies when the macro environment is risk-off. It knows, with reasonable historical accuracy, when conditions are deteriorating for equities.
BLUE: Strategy vs YELLOW: SPY Buy n Hold
That same signal also happens to describe exactly the environment where the flight-to-safety rotation has historically worked.
So the question became: what if we gave the system a destination, instead of a waiting room?
I backtested it. Added one asset.
The MAR ratio return divided by max drawdown, the number that tells you how hard the capital is working relative to the pain it takes went from
0.96 to 1.20.
That is a 25% improvement in capital efficiency. In the backtest data, 2015 to February 2026.
Max drawdown dropped. Annual return went up. Net profit on a $20,000 account increased by over
$11,600
across the test period.
One asset, the same signal but a fundamentally different use of the time the system previously spent doing nothing.
If you’re building RealTest systematic strategies and want more of this kind of approach, the strategies section on
SetupAlpha.com
is worth exploring.
In this article, you will unlock:
The asset:
What activates when the system steps aside from equities and why the logic behind it is grounded in decades of institutional capital flow data
The complete RealTest code:
Full upgrade to last week’s script, copy-paste ready
Trading Strategy rules (Step-By-Step)
This post is for paid subscribers
Subscribe
Already a paid subscriber?
Sign in

---

*由 Substack Strategy Tracker 自动抓取*

---

*Imported from Substack on 2026-04-27*
