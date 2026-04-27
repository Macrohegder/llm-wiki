---
title: "We Tried Mean Reversion on Gold — And Didn’t Expect This (+32.7% this year)"
author: "SetupAlpha"
source: "Substack"
url: "https://setup4alpha.substack.com/p/we-tried-mean-reversion-on-gold-and"
date: "2026-04-27"
topics: ["systematic-trading", "algorithmic-trading"]
---

# We Tried Mean Reversion on Gold — And Didn’t Expect This (+32.7% this year)

**来源**: [SetupAlpha](https://setup4alpha.substack.com/p/we-tried-mean-reversion-on-gold-and)  
**日期**: 2026-04-27  
**作者**: SetupAlpha

---

## 摘要

We Tried Mean Reversion on Gold — And Didn’t Expect This (+32.7% this year)
Free Gold ETF Algorithmic Trading Strategy + RealTest backtest.
SetupAlpha
Aug 13, 2025
9
5
Share
One of our long-time clients runs only
our mean reversion strategies.
They’re doing well. In fact, very well.
Recently, he emailed us:
“If your mean reversion systems are this consistent on equities, why not build some for other markets? You should try something on gold.”
It’s a fair question. GLD (the gold ETF) is a big, liquid market. And in theory, mean reversion should work anywhere there’s human emotion, overreaction, and a tendency for prices to snap back.
So… we gave it a shot.
Free RealTest code
Today we’re sharing that GLD strategy with you
for free
.
But before you get excited, we don’t actually think it’s ro...

---

## 原文

We Tried Mean Reversion on Gold — And Didn’t Expect This (+32.7% this year)
Free Gold ETF Algorithmic Trading Strategy + RealTest backtest.
SetupAlpha
Aug 13, 2025
9
5
Share
One of our long-time clients runs only
our mean reversion strategies.
They’re doing well. In fact, very well.
Recently, he emailed us:
“If your mean reversion systems are this consistent on equities, why not build some for other markets? You should try something on gold.”
It’s a fair question. GLD (the gold ETF) is a big, liquid market. And in theory, mean reversion should work anywhere there’s human emotion, overreaction, and a tendency for prices to snap back.
So… we gave it a shot.
Free RealTest code
Today we’re sharing that GLD strategy with you
for free
.
But before you get excited, we don’t actually think it’s robust enough to trade live.
Why share it then?
Because it’s a great case study in
how to test an idea, spot its weaknesses, and decide whether it belongs in your portfolio
.
Why We Tried This
The logic was simple:
Mean reversion in equities works because stocks tend to overreact to short-term moves but have a long-term upward drift.
Gold also has emotional spikes and sell-offs, so maybe the same pattern exists there.
If it worked, we could have a nice diversifier:
Uncorrelated with equities.
Different macro drivers.
Potential to smooth portfolio drawdowns.
Step 1 - Importing the Data
We start with clean historical data from
Norgate
, focusing on the most widely traded gold ETF:
$GLD
.
Why Norgate? Because
data quality is everything
. Without survivorship-bias-free, accurate price history, backtest results are meaningless.
Step 2 - Entry Rules
When we looked at gold’s price behavior compared to equities, we noticed its swings tend to last longer. So we went with:
RSI(3) < 30
… Short-term oversold
EntryLimit
: Only enter if
RSI(2) < 20
… Adds an extra layer of “really stretched” before buying
In practice:
We’re only buying when gold has pulled back hard in the very short term.
Step 3 - Exit Rule
Because gold has a long-term upward drift (even if weaker than equities), we exit when it’s
short-term overbought
:
RSI(3) > 80
This is a classic “fade the extreme” approach.
+ Commission (don’t forget)
Step 4 - First Test Results
When we ran the basic version, the results were… interesting.
Compared to simple buy-and-hold in GLD or SPY:
green line = strategy
The strategy made money, but only during certain periods.
Outperformance happened mainly when gold was already in an
uptrend
.
In sideways or down markets, performance lagged badly.
Step 5 - Trend Filters
Let’s add a trend filter and see how this GLD mean reversion behaves when we only buy if it’s above the
200-day SMA
.
Then we’ll try the same with the
252-day SMA
(one trading year)
And the
500-day SMA
.
Even with those filters, this strategy still isn’t beating SPY buy-and-hold or even GLD buy-and-hold.
And that’s critical, because if a strategy can’t outperform a simple benchmark, there’s no point running it every day. You’d be better off just buying SPY and letting the money sit there.
This is why we focus on RealTest strategies that actually beat their benchmarks, both in backtests and in real markets.
Every strategy we trade and publish has
1–3 years of out-of-sample performance (depends on the strategy)
, so you can see exactly how it’s done live before deciding to run it yourself.  Take 10 sec & go check it out now →
https://setupalpha.com/collections/realtest-strategies-and-backtests
But….
Gold is uncorrelated with SPY so it can add some value.
No leverage. Max exposure is 100%.
What We Learned
Even though we won’t run this live, it taught us a few things:
Not every edge transfers between markets.
Mean reversion in equities doesn’t guarantee mean reversion in gold.
Trend context matters.
GLD MR only really worked during gold bull phases.
It can still be a diversifier.
In the last two years, this simple version made strong gains which could help smooth a multi-strategy portfolio.
Download this RealTest GLD strategy for
FREE HERE
Subscribe and you don’t miss the next alpha!
Subscribe
9
5
Share

---

*由 Substack Strategy Tracker 自动抓取*

---

*Imported from Substack on 2026-04-27*
