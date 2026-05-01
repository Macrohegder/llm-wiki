---
title: I made my first $100,000 using THIS ONE price action strategy
author: The Rogue Quant
url: https://roguequant.substack.com/p/i-made-my-first-100000-using-this
date: 2025-05-12T03:59:37+00:00
source: substack
paywalled: True
---

# I made my first $100,000 using THIS ONE price action strategy

**URL**: https://roguequant.substack.com/p/i-made-my-first-100000-using-this
**Date**: 2025-05-12T03:59:37+00:00
**Author**: The Rogue Quant

---

Sorry for the clickbait title.

It’s not mine.

I saw it on social media…

You know how it goes…

You’re just browsing, and suddenly there it is:

“How I made $100K trading one candlestick pattern”

And your brain goes:

“Wait… what does this guy know that I don’t?””I know all candlestick patterns.”“Is there a secret I don’t know?”“Ugh. Fine. I’ll click…”

And yeah, I clicked.

The “guru” was talking about a candlestick pattern…

> The Hammer


The Hammer

…but with made-up names he came up with himself.

He also claimed to have “a context” for trading it.

So I did what any systematic trader would do (or at least should do)…

> I tested the hypothesis


I tested the hypothesis

In this post, I’ll show you:

- The original strategy and how it actually performed

The original strategy and how it actually performed

- What happened when I stripped it down to its core pattern

What happened when I stripped it down to its core pattern

- How I turned a losing setup into a testing lab for new ideas

How I turned a losing setup into a testing lab for new ideas

Ready? Let’s go.


### So... what is a Hammer candle?


According to Investopedia:

In plain English:

- Small body near the top of the range

Small body near the top of the range

- Long lower wick

Long lower wick

- Shows up after a downtrend

Shows up after a downtrend

Simple, right?

But wait…

How do we define a “downtrend”?

This is important.

If you’re a data-driven trader, you need to define everything clearly.

Otherwise, you’ll just start seeing “patterns” that aren't really there.

For this experiment, I defined a downtrend as:

> Three consecutive bars with lower lows.


Three consecutive bars with lower lows.

That’s it. Simple, mechanical, and testable.


### Defining the Hammer pattern


I coded the hammer.

In the chart below, you can see the pattern highlighted in magenta (I also added an arrow for clarity).

Here’s how I defined the hammer, I mean, how I coded it…


### First test: Hammer with no context


Now that we have a working hammer definition, I tested the simplest setup:

> Buy the day after a Hammer appears.Exit 5 days later.


Buy the day after a Hammer appears.Exit 5 days later.

That’s it.

This is the beauty of systematic trading.

You can test ideas in seconds (as long as you have good data).

So I ran the backtest on daily bars of theES (S&P 500 futures)since 2007.


### The results?


Not bad at all, I’d say.

Especially for a preliminary test with a raw candlestick pattern.

Let’s get back to what brought us here.

The strategy that supposedly made $100k by trading hammers.

Drumroll…


### The $100k strategy experiment


Just to recap…

We will backtest a candlestick pattern (the hammer) with filters.

According to the guru, the real power comes fromcontext, specifically:

> Only trade Hammers that appearnear the previous day’s low(for longs) or the previous day’s high (for shorts)


Only trade Hammers that appearnear the previous day’s low(for longs) or the previous day’s high (for shorts)

So the important thing here is to identify yesterday’s highs and lows.

I ran an indicator that shows these points:

• Red line: yesterday’s high

• Blue line: yesterday’s low

So a valid trade would be like the one below:

Only the candle marked by the first arrow (painted in magenta) is valid because it's close to the blue line, which represents the previous day's low.

Although the other candles are hammers, they are not close (enough) to the blue line.

By the way, for this backtest, I’m trading only longs.

Now for the part you’ve been waiting for…

Does this strategy have a positive expectancy?

In other words…


### Does it make money?


See for yourself…

Sorry to disappoint you.

The simple strategy of buying a hammer and selling it five days later outperformed the one that supposedly made $100,000.

Of course, there might be nuances, trader intuition, and countless other variables the guru considered but didn’t mention.

But the fact is:

> this idea of trading hammers near the previous day’s low zone wasn’t profitable.


this idea of trading hammers near the previous day’s low zone wasn’t profitable.

At least the way it was implemented in our code.


### What now?


So I took the hammer idea for a walk across a bunch of markets.

Some said “meh.”

Some let’s just say…

they hada lotto say.

Of course, I wouldn’t leave you empty-handed.

Take a look at the equity curves below…

And this

And this…


## Can you guess which instruments produced those curves?


Keep reading to discover which futures contracts they belong to…

And get access to the full code.
