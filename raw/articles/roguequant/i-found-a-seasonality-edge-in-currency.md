---
title: I Found a Seasonality Edge in Currency Futures Then Made It Better With One Rule
author: The Rogue Quant
url: https://roguequant.substack.com/p/i-found-a-seasonality-edge-in-currency
date: 2026-03-03T02:57:24+00:00
source: substack
paywalled: True
---

# I Found a Seasonality Edge in Currency Futures Then Made It Better With One Rule

**URL**: https://roguequant.substack.com/p/i-found-a-seasonality-edge-in-currency
**Date**: 2026-03-03T02:57:24+00:00
**Author**: The Rogue Quant

---

Last week I showed you how I found an edge in Copper futures.

Same starting point today.

Different market. Different angle.

I was going through some seasonality ideas inside my app.

> For those who don’t know it’s a research library I built with over 270 trading strategies extracted from academic papers, translated into plain English.


For those who don’t know it’s a research library I built with over 270 trading strategies extracted from academic papers, translated into plain English.

It’s only available to annual subscribers.

And it’s exactly where this story starts.

I was reading through calendar-based patterns. Monthly anomalies. Things that repeat not because of news or fundamentals but simply because ofwhenthey happen.

And somewhere in that rabbit hole I decided to test the…

> TDOM. Trading Day of Month.


TDOM. Trading Day of Month.

Simple concept: instead of askingwhat day of the weekis it, you askwhat trading day of the monthis it.

Day 1 is the first trading day. Day 2 is the second. All the way to day 22.

I decided to test it on currency futures.

And that’s where things got interesting.

Here’s what you’ll see today:

- The calendar-based pattern I found in currency futures and how I was confident it wasn't just data mining

The calendar-based pattern I found in currency futures and how I was confident it wasn't just data mining

- How adding a single rule to a mediocre baseline turned it into something I can actually monitor to trade in my portfolio

How adding a single rule to a mediocre baseline turned it into something I can actually monitor to trade in my portfolio

- The unconventional exit mechanism behind this strategy and the variation that pushed the Profit Factor to a level I wasn’t expecting

The unconventional exit mechanism behind this strategy and the variation that pushed the Profit Factor to a level I wasn’t expecting

Let’s dive in.

I backtest strategies so you don't have to guess. Just code, data, and stuff that actually works. Free is good.Paid gets you the full playbook.


## Not Great. Not Garbage.


I started with the simplest version possible.

One entry rule. That’s it.

The result was…

Profit Factor 1.63.Win rate just above 50%.An equity curve that looked like this:

A decent start.

But with some uncomfortable drawdowns.

And here’s what I’ve learned after years of doing this (and I’ve said it before):

> A weak baseline isn’t a dead end. It’s a starting point.


A weak baseline isn’t a dead end. It’s a starting point.

The signal was there.

And I had one more question before touching anything:

Is this real or just data mining?


## One Rule. That’s All It Took.


Before I started optimizing anything, I needed to answer that question.

So I kept it simple and did some parameter stabilization tests.

It passed.

So I added one extra condition.

Nothing exotic. A simple price action rule that made sense for this long entries.

And ran the backtest again.

Profit Factor jumped to 2.91.Win rate went from 50% to 62%.And the equity curve with less drawdowns has that feeling “now we’re talking.”

One extra condition.

That’s it.

Now I had something worth digging into further.

So I kept going.


## I Used It Backwards


There’s a signal I’ve been using for years as an entry filter.

The idea is simple: you run it before taking a trade to check if the market conditions are right.

Is this worth trading right now?

This time I used it as an exit instead.

Same signal. Different question.

Is it time to leave?

I tested it.

I tested the exit with a time-based stop and this “backwards” signal

And the results you saw above are what came out the “backwards” signal.

I’ll show you in a moment what the exactly exit I used…

And all the variations that pushed the Profit Factor to 3 and to 4…

And of course, with the complete strategy code, the full report and the trades list

Before we dive in...


#### If You’re Not an Annual Subscriber, Here’s What You’re Missing:


- Live portfolio access (already running)— You’ll see exactly which strategies I’m running in a real account.

Live portfolio access (already running)— You’ll see exactly which strategies I’m running in a real account.

- Full access to my Strategy App (270+ academic strategies)— A curated research library extracted from academic papers, rewritten in plain English so you can build from logic instead of guessing.

Full access to my Strategy App (270+ academic strategies)— A curated research library extracted from academic papers, rewritten in plain English so you can build from logic instead of guessing.

- The last 12 months of published strategies (+30 systematic trading strategies)— With complete rules and performance report.

The last 12 months of published strategies (+30 systematic trading strategies)— With complete rules and performance report.

- Early access to my AI research assistant (launching soon)— The same structured prompt engine I use to generate and refine trading ideas fast.

Early access to my AI research assistant (launching soon)— The same structured prompt engine I use to generate and refine trading ideas fast.

- The ability to request specific backtests— If there’s an idea you want pressure-tested, you can ask for it directly.

The ability to request specific backtests— If there’s an idea you want pressure-tested, you can ask for it directly.

- Big discounts on every product I launch— Starting with the upcomingZero to First Automated StrategyChallenge in March.

Big discounts on every product I launch— Starting with the upcomingZero to First Automated StrategyChallenge in March.

- Partner perks— Exclusive discounts on platforms, tools, and data feeds I actually use (btw, if you need data feed send me a DM I may have something for you)

Partner perks— Exclusive discounts on platforms, tools, and data feeds I actually use (btw, if you need data feed send me a DM I may have something for you)

- Direct access (via email) to me for 12 months— Research questions, strategy feedback, prompt reviews. Something I don’t offer anywhere else.

Direct access (via email) to me for 12 months— Research questions, strategy feedback, prompt reviews. Something I don’t offer anywhere else.

I want this!

Now you know what you've been leaving on the table.

Let’s move on.


## The Complete Strategy Code

