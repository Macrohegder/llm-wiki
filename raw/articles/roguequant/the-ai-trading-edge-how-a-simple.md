---
title: The AI Trading Edge: How a Simple ChatGPT Idea Became a Walk-Forward Tested Strategy
author: The Rogue Quant
url: https://roguequant.substack.com/p/the-ai-trading-edge-how-a-simple
date: 2025-05-25T23:22:57+00:00
source: substack
paywalled: True
---

# The AI Trading Edge: How a Simple ChatGPT Idea Became a Walk-Forward Tested Strategy

**URL**: https://roguequant.substack.com/p/the-ai-trading-edge-how-a-simple
**Date**: 2025-05-25T23:22:57+00:00
**Author**: The Rogue Quant

---

Before we dive in, I want to share a milestone:

Appreciate you for being on this journey with me.

Now, let’s move on…

In my last post I showed you how I use a simple ChatGPT prompt to generate endless trading ideas.

Today’s post is about one of those ideas and…

How it turned into a Crude Oil strategy with a3.07 profit factor.

Before you start thinking “wow, that was easy”…

Pump the brakes.

Finding truly solid edges isn’t something you stumble on every day.

You need a rock-solid process.

I built mine nearly a decade ago, and I’ve been refining it ever since, while also guiding a small group of serious traders along the way.

And now, using AI in my workflow has taken that process to another level.


#### In today’s post you’ll learn:


- How I turned a ChatGPT prompt suggestion into a PF 3.07 edge, including the human tweaks and tests that made it trade-worthy (potentially).

How I turned a ChatGPT prompt suggestion into a PF 3.07 edge, including the human tweaks and tests that made it trade-worthy (potentially).

- The core logic behind the setup, why combining structural price patterns with volatility-adjusted filters can lead to reliable mean-reversion signals.

The core logic behind the setup, why combining structural price patterns with volatility-adjusted filters can lead to reliable mean-reversion signals.

- What the walk-forward revealed, how the strategy performed out-of-sample using a simple time-based exit.

What the walk-forward revealed, how the strategy performed out-of-sample using a simple time-based exit.

Ready?

Let’s go!

This Substack is powered by backtests, forward tests, LLMs, and people like you. Subscribe if you like data-driven strategy building without the guru nonsense. Free is cool. Paid is cooler.


### How I turned a generic idea into a tradeable edge


Let me give you a bit of context before we jump in.

I recently decided to build a systematic portfolio in public.

This came directly from reader feedback (many of you asked to see the strategies I share here actually running live, in real markets.)

So that’s what I’m building.

Sometime in the second half of this year, I plan to publish a portfolio of3 to 5 strategiesdeveloped inside this newsletter (after rigorous validation), and show you exactly how to put everything into action.

But before any trade goes live, I always start the same way:

> I define a clear goal.



#### I define a clear goal.


For this one, I wanted to trade a futures contract that offeredmicro-sized exposure.

And to break away from equity indices (like SP500, Nasdaq, Dow Jones etc) a bit, I chose to focus onan energy market.

In that space, there are three instruments that offer mini contracts on Tradestation:

Then, I went back to the same prompt I shared last week, the one I use to generate ideas fast.

The one where I ask the model to act like a quant researcher with a PhD in creative arts…

> 👉If you missed that, you can check it out here.


👉If you missed that, you can check it out here.


### What I got back was a basic mean-reversion setup:


- Use recent highs and lows

Use recent highs and lows

- Look for signs of short-term weakness

Look for signs of short-term weakness

- Exit after a few bars

Exit after a few bars

Nothing special on its own.

But I’ve learned not to ignore simple ideas, especially when they come wrapped in structure.

So I used it as a starting point.

That’s it.

No curve-fitting.

No dozens of filters.

Just one good idea, dialed in with a repeatable process.

What happened next involved ChatGPT, a false breakout filter, some volatility-normalized logic and a final PF of 3.07.

Next, let’s break down the logic behind the actual setup, and why it works.


### Breaking down the logic


I’ll share the full rules in a moment…

But first, let me walk you through the core ingredients that make this setup tick.

At a high level, the strategy combines three powerful ideas:


#### 1. A failed breakout pattern


It looks for moments when price stretches beyond recent highs but can’t hold.

Think of those “look above and fail” moves—classic signs of exhaustion, especially in fast-moving markets like crude.


#### 2. A statistical oversold filter


Instead of saying“price looks cheap”, it asks:

“Is price objectively low when compared to recent volatility?”

That’s where volatility normalization comes in, allowing the system to adapt to the environment rather than using fixed levels.


#### 3. A clean, consistent exit


No chasing targets. No over-optimization.

Every trade exits at the same time:the very next day’s open(at market).

Individually, each element is simple.

But when combined, they create something far more powerful, a setup that catches exhaustion, confirms statistical extremes, and exits before noise takes over.

In the next section, I’ll show you exactly how this logic held up in out-of-sample testing using a walk-forward approach.


### Walk-Forward Results


(aka: can it hold up under pressure?)

Backtests are nice.

But I’ve been doing this long enough to know that a beautiful in-sample curve means nothing if the strategy breaks the moment it sees fresh data.

So I ran a walk-forward.

For this one, I used a rolling window of504–126:

- 504 bars in-sample(that’s roughly 2 years of data)

504 bars in-sample(that’s roughly 2 years of data)

- Followed by126 bars out-of-sample(around 6 months)

Followed by126 bars out-of-sample(around 6 months)

- Repeat the process, shifting forward each time

Repeat the process, shifting forward each time

- No re-optimizing, no peeking ahead

No re-optimizing, no peeking ahead

In each window, the strategy is “trained” on the in-sample data, then immediately tested on fresh, unseen data.

What I was looking for:

- Stable performance outside the training window

Stable performance outside the training window

- No major drop in win rate or average trade

No major drop in win rate or average trade

- Equity curves thatlook like they belong to the same familyacross time

Equity curves thatlook like they belong to the same familyacross time

And the results?

They passed the test.

Even when the market regime shifted…

even when volatility spiked…

The logic held up.

That’s when I knew this setup wasn’t just curve-fit luck.

It had real potential.

Now for the best part…

Keep reading to access the full code, and see exactly what I’m planning to do next with this strategy…
