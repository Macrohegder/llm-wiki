---
title: "Can Equity Curve Trading Turn a Losing Streak Into Your Best Entry Signal?"
author: "SetupAlpha"
source: "Substack"
url: "https://setup4alpha.substack.com/p/equity-curve-trading-mean-reversion-realtest"
date: "2026-04-27"
topics: ["systematic-trading", "algorithmic-trading"]
---

# Can Equity Curve Trading Turn a Losing Streak Into Your Best Entry Signal?

**来源**: [SetupAlpha](https://setup4alpha.substack.com/p/equity-curve-trading-mean-reversion-realtest)  
**日期**: 2026-04-27  
**作者**: SetupAlpha

---

## 摘要

Can Equity Curve Trading Turn a Losing Streak Into Your Best Entry Signal?
Does Equity Curve Trading Work or Is It Just Overfitting With Extra Steps?
SetupAlpha
Apr 26, 2026
∙ Paid
16
4
Share
Hey Systematic Trader,
Does equity curve trading actually make your strategy better?
Is it just overfitting with extra steps, or something real that professional funds use every day?
And if it does work, why does every article tell you to stop trading when your equity drops, when the data says the opposite?
I had all these questions.
So I ran 25 years of backtest data on a mean reversion strategy, tested seven different parameter values, and compared the results side by side. This article is what I found.
MaxDD dropped from
21.26% to 16.47%
.
Win rate climbed from
69% to 72%
.
Profit Factor jumped fro...

---

## 原文

Can Equity Curve Trading Turn a Losing Streak Into Your Best Entry Signal?
Does Equity Curve Trading Work or Is It Just Overfitting With Extra Steps?
SetupAlpha
Apr 26, 2026
∙ Paid
16
4
Share
Hey Systematic Trader,
Does equity curve trading actually make your strategy better?
Is it just overfitting with extra steps, or something real that professional funds use every day?
And if it does work, why does every article tell you to stop trading when your equity drops, when the data says the opposite?
I had all these questions.
So I ran 25 years of backtest data on a mean reversion strategy, tested seven different parameter values, and compared the results side by side. This article is what I found.
MaxDD dropped from
21.26% to 16.47%
.
Win rate climbed from
69% to 72%
.
Profit Factor jumped from
1.76 to 2.06
.
Here is exactly why that works, and how to build it in RealTest.
What Is Equity Curve Trading?
Equity curve trading means using your strategy’s own recent performance as a filter for future trades.
The idea:
Watch your equity curve against a moving average. When the curve is trending up, the strategy is running hot, keep trading. When it is trending down, the strategy is cold, step aside.
The instinct is correct. The direction, for mean reversion, is completely wrong.
Why Mean Reversion Flips the Logic
Mean reversion is the rubber band trade. Pull a price too far from its average, it snaps back. You trade that snap.
The rubber band applies to the strategy’s own returns, not just to the prices it trades.
When a mean reversion system goes through a bad run, the edge is not broken. It is compressed. Think of a basketball player on a shooting slump. A cold week does not mean he forgot how to play. It means he is due.
The law of averages says his next game looks better, not worse.
Mean reversion strategies work the same way. Losses cluster, then reverse. The bad run itself is the signal.
This is called negative return autocorrelation.
Long phrase, simple idea:
the bad periods and good periods of a mean reversion strategy alternate. They do not trend in one direction.
So the filter runs backwards from what feels intuitive:
Trade when equity is above its moving average:
you enter after the warm streak is already winding down
Trade when equity is below its moving average:
you enter right as conditions are statistically turning
The Tracking Benchmark
Before the results, there is one piece of plumbing to understand.
The filter needs a
tracking benchmark.
Think of it as a shadow. Your strategy casts a shadow that keeps moving even when the strategy itself stands still.
Why do you need it? If the main strategy stops taking trades, its equity curve goes flat. A flat line has no meaningful moving average. You would be reading a signal from a frozen instrument. The shadow keeps moving, keeps recording what would have happened, and keeps the filter alive.
In RealTest, the setup is two strategy blocks:
Benchmark: ben
    EntrySetup:  Buy
    Using:       Common

Strategy: MeanReversion
    EntrySetup:  Buy and Extern(@ben, S.Equity < avg(S.Equity, 20))
    Using:       Common
@ben
is the “shadow”.
On every potential entry bar, the strategy checks one thing:
is the shadow’s equity currently below its 20-day average?
Yes:
take the trade. The strategy has been running cold. Statistically favorable territory.
No:
skip the trade. The warm streak is active. Let it exhaust itself first.
The Results (EQC Filter vs Nan)
Same strategy + period (Jan 2000 to Jan 2026). Same $100K starting capital.
Two metrics worth a quick definition.
MAR
is annual return divided by your worst drawdown.
Profit Factor
is total winning dollars divided by total losing dollars. A Profit Factor of 2.06 means for every $1 you lose, you win $2.06. Anything above 1.5 is solid.
The filter cut maximum drawdown by 22%. MAR improved from 0.44 to 0.49. Sharpe from 0.77 to 0.80. Win rate jumped 3 percentage points. Profit Factor went from 1.76 to 2.06.
F
ewer trades (1,168 vs 1,974) and lower absolute net profit ($640K vs $912K). The strategy sits out a portion of the time.
If you care about smooth equity and risk-adjusted returns, the filter wins. If you care only about maximum raw compounding, the unfiltered version wins on net profit. Both are valid answers depending on what you are building.
Equity Curve: Side by Side
Here is what the tracking benchmark (green, always running) looks like overlaid with the filtered strategy (dark red):
They track closely for most of the period. The gaps are the moments the filter was active and the main strategy sat out.
The shadow running alone:
The filtered strategy alone:
Look at 2001 to 2002, and again at 2008 to 2009. The filtered curve holds a staircase shape during those periods. The strategy pauses, the worst drawdown days pass, then it resumes. The rough patches are shorter and shallower.
That visual tells you most of what you need to know. But there is still one question it cannot answer.
Is len=20 a Lucky Number?
If only len=20 works and everything else fails, this is overfitting. Not an edge.
So I ran the optimizer across seven values: 5, 10, 20, 50, 100, 150, 200.
Every single length produces a positive result. The equity curves cluster together. No lucky spike, no fragile optimum hiding in a narrow band.
Shorter lengths trade more and return more in absolute terms:
longer lengths trade less and reduce drawdown further.
Both ends of the range behave sensibly.
The only value that starts to struggle is 200, and even there the strategy is profitable. The issue at len=200 is simply that 602 trades over 25 years is too few events for compounding to work.
The number 20 is not special. The mechanic underneath it is.
The Full Strategy Rules + RealTest Code
Below I am sharing the complete strategy rules and ready-to-use RealTest code with paid subscribers.
What you will get:
Complete RealTest code (copy-paste ready):
full working script including the tracking benchmark
Exact entry and exit rules:
every condition explained in plain English, step-by-step
All parameters explained:
what each does and why it is there
Which len to choose and why:
the MAR vs ROR trade-off broken down clearly
[MOST IMPORTANT] Why this filter backfires on trend following:
and the costly mistake to avoid
Paid subscribers also get access to the full vault:
54+ articles including
20+ with RealTest source code
Organized by category:
Mean Reversion
Trend Following
Breakout
Portfolio Construction
Risk Management.
One subscription, everything published. →
All articles and strategies here
This post is for paid subscribers
Subscribe
Already a paid subscriber?
Sign in

---

*由 Substack Strategy Tracker 自动抓取*

---

*Imported from Substack on 2026-04-27*
