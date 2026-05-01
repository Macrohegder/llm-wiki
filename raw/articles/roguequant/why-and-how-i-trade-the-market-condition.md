---
title: Why (and How) I Trade the Market Condition Everyone Avoids
author: The Rogue Quant
url: https://roguequant.substack.com/p/why-and-how-i-trade-the-market-condition
date: 2025-11-24T00:01:16+00:00
source: substack
paywalled: True
---

# Why (and How) I Trade the Market Condition Everyone Avoids

**URL**: https://roguequant.substack.com/p/why-and-how-i-trade-the-market-condition
**Date**: 2025-11-24T00:01:16+00:00
**Author**: The Rogue Quant

---

Today’s post is going to be quick because I just got back from a long holiday weekend with the kids and I’m exhausted.

But of course I have something for you.

I was working on a RBOB gasoline futures strategy last week.

Testing a concept that had already worked on other futures markets…

And it’s pretty simple…

Comparing today’s opening price to a historical high/low/close from several days back.

But…

> It’s based on normalized price levels.


It’s based on normalized price levels.

And today’s article is about:

- The normalized price comparison that works on many different markets (hint: it’s not about oversold)

The normalized price comparison that works on many different markets (hint: it’s not about oversold)

- Why there’s a specific ADX number that acts like a market “off switch” and what happens when you trade into it

Why there’s a specific ADX number that acts like a market “off switch” and what happens when you trade into it

- How to combine both into a stupidly simple long-only system that exits on a timer

How to combine both into a stupidly simple long-only system that exits on a timer

Let’s dive in.

This Substack is powered bybacktests, forward tests, LLMs, and people like you. Subscribe if you likedata-driven strategy buildingwithout the guru nonsense. Free is cool.Paid is cooler.


## What is this strategy about?


Most mean reversion strategies look for “oversold” conditions.

RSI below 30.Bollinger Bands stretched.Price way down from its moving average.

You know the drill.

This isn’t that.

This strategy uses a different kind of comparison…

It’s based on normalized price levels.

It’s comparing today’s open price to a historical low from several days back.

Both normalized.

When today’s open drops at or below that historical low, something interesting happens.

But this setup only works when the market is in a very specific state…

The market needs to be dead quiet.

And I don’t mean “kind of slow.”

I mean measurably, statistically flat.

That’s where ADX comes in.

ADX measures trend strength.

High ADX means strong trend.

Low ADX means...well, most people call it “no trend.”

I’ll share in a moment the exact setup I use for ADX.

It’s probably lower than you’d think is even tradeable.

But first, let me show you…


## The numbers that made me pay attention


Before I explain the “why,” let me show you what caught my eye.

I backtested this on RBOB Gasoline futures (@RB) from 2007 to 2025.

Long only.

126 trades.

60% win rate.

Profit factor of 2.34.

Look at this equity curve:

Solid equity curve.

Especially since those numbers already include slippage and commissions.

Share

That’s 18 years of compound growth with three losing years.

The strategy holds each position for a short period.

No trailing stops. No subjective exits. Just a simple time-based rule.

Maximum drawdown over nearly two decades? 21%.

Now let me tell you why it works…


## Why does this actually work?


Think about what happens when ADX drops to extremely low levels.

The market isn’t trending. There’s no momentum. No clear direction.

Most traders hate this kind of environment.

You, me and 99% of traders wantneedmovement. We wantneedvolatility. We wantneed“something to happen.”

But there’s opportunityin choppy markets…

When trend strength collapses, price gets compressed.

It oscillates in a tight range.

Every small dip below a recent level gets rejected.

Every small push above resistance fails.

The market becomes a rubber band.

And rubber bands snap back.

Now here’s where the normalized comparison comes in.

Most mean reversion setups use absolute price levels or percentage-based indicators.

Usually those don’t scale across markets.

What’s “oversold” on gasoline isn’t the same as “oversold” on the S&P 500.

Normalized comparisons solve this.

You’re comparing today’s opening price to a historical low but both values are normalized.

This makes the comparison work across several different markets.

When today’s normalized open drops to or below a normalized low from X days ago, you’re seeing a specific pattern:

Price tried to gap down or open weak... but the market has no directional conviction to follow through.

That’s the setup.

ADX + normalized price weakness = mean reversion edge.

It’s just compression and snap-back.

You’re not trying to ride the move forever.

You’re not predicting where price will reverse.

You’re simply capturing the initial bounce…

The mechanical, statistical tendency for price to revert when it’s been compressed in a low-trend environment.

Hold for a fixed number of bars. Exit. Repeat.


## The specific mechanics


Here’s what I found:

There’s averynarrow band of parameters that makes this work consistently.

The ADX threshold can’t be too high (you’ll catch trending moves and get chopped up).

It can’t be too low (you’ll miss too many setups).

The lookback period for the normalized low? Same deal.

Too short and you’re trading noise.

Too long and you miss the compression dynamic.

The exit timing? If you hold too long, you give back profits. If you exit too early, you miss the bounce.

I’m going to give you those exact numbers now…

This is exactly the kind of edge thatrequiresthe complete picture to implement correctly.

Half the information is worse than no information.

If you try to “guess” the parameters based on what I’ve said so far, you’ll probably get it wrong.

And then you’ll conclude the strategy doesn’t work.

If you’re a paid subscriber, I’m giving you the full playbook:

- The two functions to normalize price

The two functions to normalize price

- The exact ADX threshold

The exact ADX threshold

- The precise lookback period for the normalized low comparison

The precise lookback period for the normalized low comparison

- The time-based exit rule

The time-based exit rule

- The complete EasyLanguage code

The complete EasyLanguage code

- Plain English translation of every line

Plain English translation of every line

Let’s get into it.

(Quick note: I’ll also share with you a long-short variation at the end. It performed well as you can see below, but honestly? I prefer the long-only version.)


## [Complete Strategy Code]

