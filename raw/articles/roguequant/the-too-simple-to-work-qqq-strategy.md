---
title: The "Too Simple to Work" QQQ Strategy That Works
author: The Rogue Quant
url: https://roguequant.substack.com/p/the-too-simple-to-work-qqq-strategy
date: 2026-02-16T04:13:01+00:00
source: substack
paywalled: True
---

# The "Too Simple to Work" QQQ Strategy That Works

**URL**: https://roguequant.substack.com/p/the-too-simple-to-work-qqq-strategy
**Date**: 2026-02-16T04:13:01+00:00
**Author**: The Rogue Quant

---

Two years ago, I took the kids on a week-long vacation 2,305 km from home.

We brought four suitcases. Two large, two small.

And if you’ve ever traveled with kids, you already know what happened next…

Dragging bags through airports, lobbies, transfers. Every leg of the trip felt like a logistics operation.

At the hotel, we met a couple who also had two kids.

Same ages as ours.

Their oldest even had the same name as our oldest.

And (I swear I’m not making this up) both were born on the exact same day, month, and year.

So naturally, we became fast friends.

One night, over drinks, the conversation turned to how we each pack for trips. And that’s when they dropped the bomb.

They only travel with carry-on bags.

Two carry-on bags. For a family of four. For a full week.

Meanwhile, we had four suitcases and I still felt like we’d forgotten something.

Two bags. That’s it.

That stuck with me. Not because of packing advice (which was great tbh) but because simplicity is a principle that applies to almost everything…

Cooking. Parenting. Investing.

And especially systematic trading.

Where every rule you add is another chance to overfit.

Today I want to show you what happened when I tested one of the simplest possible strategies on QQQ. Specifically:

- What the strategy does (and why it’s almost embarrassingly simple)

What the strategy does (and why it’s almost embarrassingly simple)

- How it performed across 18 years (including 2008)

How it performed across 18 years (including 2008)

- Why less really might be more when it comes to building edges

Why less really might be more when it comes to building edges

Ready? Let’s dive in.

I backtest strategies so you don't have to guess. Just code, data, and stuff that actually works. Free is good.Paid gets you the full playbook.


## What the Strategy Does (And Why It’s Almost Embarrassingly Simple)


When I’m testing a new idea, I always start with the simplest possible version.

No filters. No extra conditions. Just the core logic, naked, by itself.

Because if the base idea doesn’t show at least some edge on its own, no amount of indicators is going to save it.

And the idea I wanted to test here is probably the oldest one in technical analysis:

> Buying when price is above its long-term moving average.


Buying when price is above its long-term moving average.

That’s literally it.

A simple entry condition based on trend.

One exit condition.

QQQ daily bars going back to 2010.

I know what you’re thinking…

“Leo, this is too basic.”

And honestly? I thought the same thing. But I’ve learned to trust the process: test first, judge later.

So let me show you what came out…


## The Results


Here’s the performance report from 2010 to February 2026:

178 trades. 69% win rate. Profit factor of 2.64.

Let that sink in for a second.

A strategy with a simple condition and one exit condition just delivered a 2.6 profit factor over 15+ years on QQQ.

The average winner ($770) is bigger than the average loser ($652). Not by a huge margin but it doesn’t need to be when you’re winning 69% of the time.

Now let’s look at the year-by-year breakdown, because this is where it gets interesting:

Out of 15+ full years of trading, only two had a meaningful loss: 2011 (-0.59%) and 2022 (-4.22%).

That’s it. Two bad years (2026 just started so…)

And even the “bad” years were… not that bad.

2022 was a brutal year for tech. QQQ dropped over 30%. This strategy lost 4.22%.

But here’s what I want you to focus on:consistency.

This isn’t a strategy that makes all its money in one lucky year. It grinds. Slowly. Year after year.

Which brings us to the obvious question you’re probably asking right now…


## But What About 2008?


If you’ve been reading this newsletter for a while, you know I don’t hide from hard questions.

And the first one that should come to mind is:

“Leo, you started the test in 2010. That’s convenient. You skipped the worst financial crisis in modern history.”

Fair.

So I went back and ran the test from 2007. Including 2008. Including the full meltdown.

Here’s what happened:

In 2008 — the year QQQ dropped over 40% — this strategy lost 4.36%.

4.36%.

A long-only strategy on a Nasdaq ETF. During the Great Financial Crisis. Lost less than five percent.

The overall numbers barely changed. 191 trades. 68.59% win rate. Profit factor of 2.53 (down from 2.64, which makes sense — you’re adding a crisis to the dataset).

The strategy didn’t predict the crash. Nobody does. But the filter did something more valuable: it got out of the way.

When price dropped below its long-term trend, the strategy simply stopped buying.

No predictions. Just… stepped aside.

And that might be the most underrated edge in systematic trading.


## Why Less Might Actually Be More


A simple trading filter usually just answers one question: is the overall trend up or down?

When the trend is up, you’re in. When it’s not, you’re out.

And because there’s almost nothing to optimize, there’s almost nothing to overfit.

The more rules you add to a strategy, the more you’re fitting it to what already happened.

You’re not finding an edge… you’re finding a coincidence.

A beautiful, perfectly backtested coincidence that will break the moment real money hits the market.

With a strategy this simple, there’s nowhere to hide. Either the core idea works or it doesn’t.

And after 191 trades across 18 years — including a financial crisis — it works.

But here’s the thing…

You’ve seen the results. You know the logic. You even know the core idea: buy when price is above its long-term moving average.

You could probably code something up tonight and get... decent results.

Maybe.

But decent results andtheseresults are not the same thing.

Because I haven’t told you:

- It’s notonetrend filter. It’s two. Working together. And the gap between them is where the real edge hides. (Use just one and the Profit Factor drops by almost a full point.)

It’s notonetrend filter. It’s two. Working together. And the gap between them is where the real edge hides. (Use just one and the Profit Factor drops by almost a full point.)

- The exit hasnothingto do with trend. Nothing. It’s not the opposite of the entry. It’s not a crossover. It’s something a lot of traders never think to try and it’s probably the single biggest reason this strategy survives 2008 with a 4% loss.

The exit hasnothingto do with trend. Nothing. It’s not the opposite of the entry. It’s not a crossover. It’s something a lot of traders never think to try and it’s probably the single biggest reason this strategy survives 2008 with a 4% loss.

- This is NOT a moving average crossover strategy. Most traders would default to that. This does something simpler.

This is NOT a moving average crossover strategy. Most traders would default to that. This does something simpler.

That’s what’s below the paywall.

Full rules. Full code. Full reasoning.

The kind of detail that turns “interesting idea” into something you can actually trade.

Speaking of ideas…

The Copper strategy from last week?

That idea started in an academic paper about volatility compression in commodity markets and is part of my database…

It's one of 250+ trading strategies extracted from academic research and translated into plain English.

Mean reversion, momentum, breakout, seasonality, sentiment… across futures, equities, ETFs, commodities, forex.

New papers added every week.

Annual subscribers get full access. It’s not available any other way.

If you’ve ever stared at a screen wondering what to test next this solves that problem permanently.
