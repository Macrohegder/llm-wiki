---
title: From 1.18 to 2.90 Profit Factor: The Simple Momentum Filter That Fixes Oversold Strategies
author: The Rogue Quant
url: https://roguequant.substack.com/p/from-118-to-290-profit-factor-the
date: 2025-12-01T02:02:12+00:00
source: substack
paywalled: True
---

# From 1.18 to 2.90 Profit Factor: The Simple Momentum Filter That Fixes Oversold Strategies

**URL**: https://roguequant.substack.com/p/from-118-to-290-profit-factor-the
**Date**: 2025-12-01T02:02:12+00:00
**Author**: The Rogue Quant

---

A subscriber messaged me last week.

Wanted a strategy for the US (30-year Treasury futures).

I know that mean-reverting strategies tend to perform well on the US market.

So, like I always do, I started with the simplest version...

Used a classic mean reversion indicator to see if there was any hint (I said hint) of a potential edge...

Ran the backtest.

> 291 trades.Profit factor 1.18.Win rate 68%.


291 trades.Profit factor 1.18.Win rate 68%.

Nah.

So the second step (and most of the time the last step) I test a second rule combined with the initial idea.

In this case I added a momentum filter.

Ran it again.

> 117 trades.Profit factor 2.90.Win rate 77%.


117 trades.Profit factor 2.90.Win rate 77%.

Same 18 years of data.

Same base logic.

One filter changed everything.

In this article we’ll cover:

- Why the US is perfect for mean reversion strategies

Why the US is perfect for mean reversion strategies

- The stochastics setup everyone uses (and why it barely breaks even)

The stochastics setup everyone uses (and why it barely breaks even)

- The momentum filter that transformed a 1.18 profit factor into 2.90

The momentum filter that transformed a 1.18 profit factor into 2.90

Let’s dive in.

This Substack is powered bybacktests, forward tests, LLMs, and people like you. Subscribe if you likedata-driven strategy buildingwithout the guru nonsense. Free is cool.Paid is cooler.

Share


## WHY THE US IS PERFECT FOR MEAN REVERSION


Treasury futures show mean reversion patterns.

Not always. But consistently enough to exploit.

Think about what happens in a mean-reverting market.

Price drops.

Everyone sees it’s oversold.

But oversold can get more oversold.

That’s where most systems die.

They enter too early.

The momentum filter solves this.

You’re not predicting the turn.

You’re confirming it’s already happening.

By the time you enter, the selling pressure is exhausted.

The bounce has started.

You’re not catching the knife.

You’re picking it up off the ground.

And here’s the other thing.

The US market structure helps.

Treasuries don’t gap randomly like stocks.

They don’t have earnings surprises.

No CEO tweets tanking the price overnight.

Just economic data, Fed policy, and bond market flow.

Predictable patterns.

Which means mean reversion works better here than most markets.

Add a momentum confirmation filter?

Now you’ve got something.

The system holds for a few days, exits, repeats.

If momentum confirmed the reversal, the bounce happens fast.

Usually within 3-5 days.

After that, you’re just giving back profits…


## THE STOCHASTICS SETUP (AND WHY IT BARELY WORKS)


Here’s what I tested first.

Basic oversold setup.

Nothing fancy.

Ran it on the US from 2007 to 2025.

291 trades.

68% win rate.

Profit factor 1.18.

Look at those numbers closer though.

Average winner: $854.

Average loser: $1,590.

You’re winning twice as often but losing double when you’re wrong.

That’s the problem right there.

The system finds oversold conditions fine.

But it can’t tell if the selling is actually done.

Sometimes you catch the bounce.

Sometimes you catch a falling knife.

68% sounds good until you realize the 32% is killing you.

I stared at this for a while.

There had to be a way to filter out the bad signals without overfitting…

The ones where price just keeps dropping.

That’s when I thought about momentum direction.

Not momentum strength.

Direction.


## THE FILTER THAT CHANGED EVERYTHING


Added one thing.

A momentum direction filter.

Ran the backtest again.

117 trades.

Profit factor 2.90.

Win rate 77%.

Wait.

Take a look at the equity curve…

Solid.

Same base setup.

The filter cut out more than half the signals.

But kept all the good ones.

18 consecutive winners at one point.

Max consecutive losers? 5.

The equity curve just... climbs.

Overfitting move?

I also ran Monte Carlo and Variance tests and the results were still solid.

Here’s what the filter does.

It waits for momentum to actually turn.

Not just for price to look oversold.

You’re still buying dips.

But only when the dip is already reversing.

Sounds simple.

It is simple.

But the difference in results is massive.

If you’re a paid subscriber, I’m giving you everything:

- The exact momentum filter and threshold

The exact momentum filter and threshold

- The precise parameters

The precise parameters

- Complete Strategy code

Complete Strategy code

- Plain English translation of every line

Plain English translation of every line

Let’s get into it.


## HERE’S THE FILTER (AND THE FULL STRATEGY CODE)


The filter is…
