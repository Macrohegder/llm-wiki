---
title: I Tested My September Strategy on a New Market. Here's What Happened.
author: The Rogue Quant
url: https://roguequant.substack.com/p/the-month-end-pattern-that-keeps
date: 2026-01-16T21:37:26+00:00
source: substack
paywalled: True
---

# I Tested My September Strategy on a New Market. Here's What Happened.

**URL**: https://roguequant.substack.com/p/the-month-end-pattern-that-keeps
**Date**: 2026-01-16T21:37:26+00:00
**Author**: The Rogue Quant

---

Back in September, I stumbled on a pattern on bonds.

The pattern:

> Buying Treasury bonds when there are exactly X days left in the month exploits institutional rebalancing flows.


Buying Treasury bonds when there are exactly X days left in the month exploits institutional rebalancing flows.

Pension funds, ETFs, insurance companies... they all rebalance at month-end.

The Federal Reserve even published research showing Treasury trading volume is 33% higher on the last trading day of the month (TDLM).

That original strategy on US bonds (daily) you can read it here:


#### The End-of-Month Trading Edge I Discovered During My Morning Walk


So I revisited the strategy and tested the core idea on a different bond market. Different timeframe.

Today’s article is about that.

Here’s what you’ll see:

- The TDLM pattern applied to 5-Year Treasury Notes (FV) on 600-minute bars

The TDLM pattern applied to 5-Year Treasury Notes (FV) on 600-minute bars

- A simple filter that made the strategy even more robust

A simple filter that made the strategy even more robust

- Why this confirms the edge is real (not just a data mining artifact)

Why this confirms the edge is real (not just a data mining artifact)

Let’s get into it.

I backtest strategies so you don't have to guess. Just code, data, and stuff that actually works. Free is good.Paid gets you the full playbook.


### The Baseline:


I decided to test this strategy on FV (5-Year Treasury Notes) using 600-minute bars. between 2007-2026.

All tests in this article include slippage and commissions.

First, I wanted to test the raw pattern.

No filters. No stops. No fancy exits.

Just the core idea…

> “Buy when there are X trading days left in the month. Exit after Y days.”


“Buy when there are X trading days left in the month. Exit after Y days.”

Simple as that…

> $31,520 profit. 2.2 Profit Factor. 227 trades. 62% win rate.


$31,520 profit. 2.2 Profit Factor. 227 trades. 62% win rate.

The edge is there.

No optimization. No curve-fitting. Just the raw month-end effect showing up exactly where it should.

So the obvious question…

> Could I improve this without falling into the curve-fitting trap?


Could I improve this without falling into the curve-fitting trap?

And that’s exactly what I’m going to show you next...


### The Filter: A Simple Pullback Condition


I needed something simple.

Not a complex indicator.

Not multiple conditions stacked together.

Just a clean, logical way to measure if price has retreated over the last few bars.

The idea:

If the market is lower now than it was a few days ago, we have a pullback.

That’s it.

Combined with the last days of the month, the logic becomes:

> Buy at month-end... but only when there’s been a recent pullback.


Buy at month-end... but only when there’s been a recent pullback.

Here’s what happened:

$33,401 profit. 2.66 Profit Factor. 168 trades. 64% win rate.

The filter cut 59 trades.

The bad ones (in theory)

Profit Factor jumped from 2.27 to 2.66.

Win rate improved from 62.11% to 63.69%.

Average trade went up 43% — from $138.86 to $198.82.

Same edge. Less noise.


### Now the fun part…


The complete code.

The exact filter (and why I chose it).

The exit logic that keeps the winners running.

And the statistical tests I ran to make sure this isn’t just a pretty equity curve.

Btw, if you’re not a paid subscriber yet, here’s what you’re missing:

> →The complete code below— the exact filter, entry logic, and exit rules I use→The custom function— ready to drop into your workspace→Plain English version— so you can port it to whatever platform you use→The TRQ App— 250+ strategies extracted from academic papers, updated daily(annual only)→Request Custom Backtests— send me your idea, I’ll test it and publish the results→A Big Fat Discounton my January Challenge — “Zero to First Automated Strategy” in 20 days(details coming soon)→Exclusive GPTs dropping in 2025— first one: a trading idea generator trained on academic papers(annual only)


→The complete code below— the exact filter, entry logic, and exit rules I use→The custom function— ready to drop into your workspace→Plain English version— so you can port it to whatever platform you use→The TRQ App— 250+ strategies extracted from academic papers, updated daily(annual only)→Request Custom Backtests— send me your idea, I’ll test it and publish the results→A Big Fat Discounton my January Challenge — “Zero to First Automated Strategy” in 20 days(details coming soon)→Exclusive GPTs dropping in 2025— first one: a trading idea generator trained on academic papers(annual only)

Ok, enough teasing…

Let’s get into it…


## [Complete Strategy Code]

