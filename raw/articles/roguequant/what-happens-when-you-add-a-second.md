---
title: How to Build an Uncorrelated 2-Strategy Portfolio With Under $500 in Margin
author: The Rogue Quant
url: https://roguequant.substack.com/p/what-happens-when-you-add-a-second
date: 2025-10-12T04:13:04+00:00
source: substack
paywalled: True
---

# How to Build an Uncorrelated 2-Strategy Portfolio With Under $500 in Margin

**URL**: https://roguequant.substack.com/p/what-happens-when-you-add-a-second
**Date**: 2025-10-12T04:13:04+00:00
**Author**: The Rogue Quant

---

I got a lot of messages after my last article on how to build a systematic trading portfolio with a small account.

If you missed it, you can read it here:


#### How to Build a Real Trading Portfolio on a Small Account


And among all the questions, one kept coming up:

> “Leo, you showed us the Corn strategy. What’s next?”“How do I actually build this micro-portfolio you keep talking about?”


“Leo, you showed us the Corn strategy. What’s next?”“How do I actually build this micro-portfolio you keep talking about?”

Fair question.

Because one strategy isn’t a portfolio…

It’s just a start.

The real diversification begins with a couple of uncorrelated strategies (easy to say, but very few people know how to actually do it).

That’s where things start to behave differently…

Where one market chops while the other trends.

Here’s what actually happens when you combine uncorrelated strategies to your portfolio:

Pretty cool, right?

And the best part?

You can trade uncorrelated strategies like the Corn system from the last article and the Natural Gas setup I’m about to show you with a required margin of only…


#### $492


It’s $108 for micro Corn and $384 for micro Natural Gas.

That means with the same $5,000 account, you can now run:

- Strategy #1: Micro Corn ($108 margin)

Strategy #1: Micro Corn ($108 margin)

- Strategy #2: Micro Natural Gas ($384 margin)

Strategy #2: Micro Natural Gas ($384 margin)

You just diversified acrossagriculture and energywith less capital than a single mini ES contract requires.


## Here’s what we’ll cover today:


- Why Natural Gas completes your micro-portfolio: the energy-commodity correlation gap + margin efficiency

Why Natural Gas completes your micro-portfolio: the energy-commodity correlation gap + margin efficiency

- From one strategy to two: how to manage correlation, risk allocation, and execution when you add a second system

From one strategy to two: how to manage correlation, risk allocation, and execution when you add a second system

- The Value Composite strategy:a 2.1 Profit Factor approach that caught almost 1,000% returns over the backtesting period.

The Value Composite strategy:a 2.1 Profit Factor approach that caught almost 1,000% returns over the backtesting period.

Let’s dig in.

This Substack is powered by backtests, forward tests, LLMs, and people like you. Subscribe if you like data-driven strategy building without the guru nonsense. Free is cool.Paid is cooler.


## Part 1: Why Natural Gas Is Your Second Strategy


Most traders think about adding strategies like collecting Pokémon cards.

“I have Corn. Now I need Crude Oil. Then maybe EUR/USD...”

Wrong approach.

You don’t add strategies randomly.

You add them strategically based on three criteria:


### Criterion #1: Uncorrelated Market Drivers


Corn responds to:

- Weather patterns

Weather patterns

- Planting/harvest cycles (seasonal)

Planting/harvest cycles (seasonal)

- Agricultural demand

Agricultural demand

Natural Gas responds to:

- Heating demand (seasonal)

Heating demand (seasonal)

- Industrial production

Industrial production

- LNG export activity

LNG export activity

- Weather (but different impact than agriculture)

Weather (but different impact than agriculture)

In theory they don’t move together.

But theory doesn’t matter to us.

What we care about is whether the strategies themselves are uncorrelated.

That’s what you want.

And I’m about to show you the correlation between these two strategies, just keep reading…


### Criterion #2: Margin Efficiency


Remember the margin requirements:

- Micro Corn (MZC):$108

Micro Corn (MZC):$108

- Micro Natural Gas (MNG):$384 (for shorting or $363 for long overnight)

Micro Natural Gas (MNG):$384 (for shorting or $363 for long overnight)

With $5,000, you can run both strategies with plenty of buffer room.

Portfolio margin calculation:

- Corn strategy allocation: $1,000

Corn strategy allocation: $1,000

- Natural Gas strategy allocation: $1,200

Natural Gas strategy allocation: $1,200

- Combined strategies: $2,200

Combined strategies: $2,200

- Cash buffer: $2,800 (56%)

Cash buffer: $2,800 (56%)

You’re not even close to maxing out your capital.


### Criterion #3: Strategy Logic Diversity


Here’s where it gets interesting.

The Corn strategy is mean-reversion.

Buy when price gets oversold → exit when it returns to average.

Natural Gas uses a completely different approach:

Value-based directional entries.

When price is undervalued relative to recent range (for longs) or showing specific short setups (for shorts), the system enters with the trend.

One portfolio. Two different edges. Two different market conditions.

But that’s diversification in theory becausewe haven’t actually calculated the correlationyet…

So let’s do that now.

I calculated the correlation between the two strategies using daily P&L alignment.

> The result:+0.009


The result:+0.009

That’s practically zero well below the0.3threshold for good diversification.

In short, both strategies: Corn (agriculture) and Natural Gas (energy) truly move independently.


## Part 2: Managing Your Two-Strategy Portfolio


Okay, so you know you want to add Natural Gas.

But how do you actuallymanagetwo strategies?

Here’s the framework.


### Step 1: Recalculate Risk Allocation


You can’t just split $5,000 in half.

Different strategies have different risk profiles.

Risk allocation based on max drawdown is one option:

Notice the Natural Gas strategy has a deeper drawdown.

That’s why it gets slightly more allocated capital… to absorb the volatility.

But you’re still keeping56% in cash buffer.

Why?

Because when both strategies hit drawdowns simultaneously (and they will), you need cushion.


### Step 2: Track Correlation in Real-Time


Before you go live, backtest the correlation between your two strategies.

I’ve just shown you the correlation between the two strategies, and the process is quite simple…

How to do this:

- Export daily returns for both strategies

Export daily returns for both strategies

- Calculate correlation coefficient

Calculate correlation coefficient

- Target: correlation < 0.3

Target: correlation < 0.3

If correlation > 0.5, you’re not actually diversified.

You can do this in Excel or ask ChatGPT/Claude for a Python script.

Takes 3 minutes.


### Step 3: Deploy Gradually


You don’t need 30 days or 30 trades.

You need enoughreal-world datato see if the system behaves as expected.

If your strategy trades often, great you’ll know fast.

If it only triggers a dozen times a year, you focus onbehavior, not frequency.

Run both systems small.

Monitor volatility, drawdown, correlation, and signal quality.

When live behavior aligns with what the backtest projected, scale gradually.

If it diverges, pause and investigate.

The goal isn’t to match performance.

(Read the above again because it’s important)

It’s to confirm thelogic still holdswhen the market stops behaving nicely.


## Part 3: The Natural Gas Value Composite Strategy


Alright, let’s talk about the strategy itself.

This one’s different.

It’s not another mean-reversion system trying to buy dips.

It’s not your classic breakout chasing momentum either.

It’s something in between…

Avalue-based directional strategythat reacts when price gets too cheap (or too expensive)relative to its own structure.

It uses a function called

> Value Composite.


Value Composite.


### The Core Idea


Think of it this way:

Every market has a “fair zone” a range where price spends most of its time.

When volatility expands and price leaves that zone, one of two things happens: either it snaps back, or it accelerates in the same direction.

This system is built to recognizewhichof those scenarios is unfolding.

It looks at:

- How far price has stretched from its recent value range;

How far price has stretched from its recent value range;

- Whether it’s doing so in the direction of trend or against it;

Whether it’s doing so in the direction of trend or against it;

- And whether the expansion is statistically significant.

And whether the expansion is statistically significant.

When those conditions align, the system takes a position and rides the move.

Nothing fancy to be honest.


### The Results


Here’s the equity curve (2007-2025):

Key metrics:

It has a stronger bias toward the short side than the long side.

But overall, it’s a solid strategy with a decent average trade net profit and win/loss ratio.

Both strategies running = diversified exposure across agriculture and energy with less than $500 in combined margin.

That’s the micro-portfolio edge.


### Annual Performance Breakdown


What stands out:

- Consistent profitability across most years

Consistent profitability across most years

- Only 2 significant losing years (2013 and 2024)

Only 2 significant losing years (2013 and 2024)

- Best year: 2009 with 23.22% return

Best year: 2009 with 23.22% return

- Profit Factor consistently above 2.0 in winning years

Profit Factor consistently above 2.0 in winning years

It’s 18 years of consistent edge across multiple Natural Gas market regimes.

Before we look at the full strategy code, a quick note…

> If you’ve been following me for a while, you’ve probably wondered where all these ideas come from.They come from theRogue Quant App— my private research database with over150 trading strategies, each extracted from academic papers and translated into plain English logic you can actually test.Annual subscribers get full access to it.


If you’ve been following me for a while, you’ve probably wondered where all these ideas come from.

They come from theRogue Quant App— my private research database with over150 trading strategies, each extracted from academic papers and translated into plain English logic you can actually test.

Annual subscribers get full access to it.

Now… let’s talk about the Natural Gas strategy code.


## [Complete Strategy Code]

