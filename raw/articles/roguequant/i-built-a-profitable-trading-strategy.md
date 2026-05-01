---
title: I Built a Profitable Dollar Strategy in January. 10 Months Later, I Still Won't Trade It.
author: The Rogue Quant
url: https://roguequant.substack.com/p/i-built-a-profitable-trading-strategy
date: 2025-10-19T05:01:01+00:00
source: substack
paywalled: True
---

# I Built a Profitable Dollar Strategy in January. 10 Months Later, I Still Won't Trade It.

**URL**: https://roguequant.substack.com/p/i-built-a-profitable-trading-strategy
**Date**: 2025-10-19T05:01:01+00:00
**Author**: The Rogue Quant

---

Quick one today because I’m traveling with the family.

But I want to show you something I’ve been wrestling with since January…

A Dollar Index strategy that looks solid on paper.

If you trade forex you’ll like this one.

Clean backtest. Survived 10 months of paper trading without blowing up.

And I still can’t bring myself to put real money on it.

This is the part of systematic trading nobody talks about…

> The hesitation that hits you right before you go live, even when the numbers look goodon paper.


The hesitation that hits you right before you go live, even when the numbers look goodon paper.


#### Here’s what we’re covering today:


1. Why genetic algorithms create strategies you can’t fully explain(and why that matters when your capital is on the line)

2. What 10 months of paper trading actually reveals(spoiler: it’s not what you think)

3. The trust framework I use to decide: go live or kill it

Let’s dig in.


## Part 1: The Unexplainable Edge Problem


Here’s what happened.

Back in January, I used a genetic algorithm software to build this Futures Dollar strategy.

I love the software. And even though I’ve tested countless platforms over the years, there are only two I actually trust but only one I use regularly.

And not necessarily to generate trading strategies.

I’ll tell you which software in a minute, but first, here’s what you need to know:

> Genetic algorithms test thousands of combinations of conditions, entries, exits, and position sizing, hunting for statistical edges in ways your brain never could.


Genetic algorithms test thousands of combinations of conditions, entries, exits, and position sizing, hunting for statistical edges in ways your brain never could.

The platform spit out a strategy that:

- Shows consistent returns across different market conditions

Shows consistent returns across different market conditions

- Has overall clean entry and exit logic

Has overall clean entry and exit logic

- Uses time-based and profit-based exit conditions

Uses time-based and profit-based exit conditions

Look at the equity curve…

Sounds good, right?

Here’s the problem.

When I look at the specific parameters the algorithm chose, I can’t explainwhycertain numbers work.

For example, the strategy uses different “profitable close” thresholds for long vs short positions.

The logic counts how many bars close in profit, then exits after hitting a specific count.

Why that exact count? Why does it work?

The genetic algorithm tested it. The backtest confirms it. But I can’t build a narrative around why it shouldcontinueworking.

And that’s the uncomfortable truth about algo-generated strategies:

> You don’t always need to understand why something works to profit from it.


You don’t always need to understand why something works to profit from it.

But you absolutely need to trust it enough to stick with it during drawdowns.

That’s where I’m stuck.


## Part 2: When Paper Trading Stretches Too Long


My normal validation process is 3 to 6 months in a paper account.

Watch the strategy execute in real-time.

Look for behavioral quirks.

Make sure it does what the backtest promised.

This Dollar strategy?

Almost 10 months in incubation.

Nearly double my longest typical validation period.

And here’s what’s interesting: it’s performed exactly as expected.

No catastrophic failures. No weird behavior. Takes profits, takes losses, generally does what it’s supposed to do.

So why am I still hesitating?

Because the longer I watch it, the more I notice edge cases I can’t explain.

I keep asking: what is this thing actually capturing?

Is it exploiting a genuine market inefficiency? Or did the genetic algorithm just find a pattern in the historical data that happens to work... for now?

After 10 months, I still don’t have a satisfying answer.

And that’s the real lesson:more time in paper trading doesn’t necessarily give you more confidence.

Sometimes it just gives you more questions.


## Part 3: The Trust Framework (Go Live or Kill It)


So here’s my situation.

I have a strategy that:

- Shows solid performance in backtesting

Shows solid performance in backtesting

- Survived 10 months of paper trading without blowing up

Survived 10 months of paper trading without blowing up

- Contains logic that works but feels partially mysterious

Contains logic that works but feels partially mysterious

- Uses a genetic algorithm platform that’s genuinely impressive (seriously, this thing is powerful)

Uses a genetic algorithm platform that’s genuinely impressive (seriously, this thing is powerful)

The question isn’t whether the strategy works, clearly does.

The question is…

Whether I trust it enough to allocate real capital.

Here’s a simple framework I use to make this call:

A) Mechanical RobustnessDoes the strategy work across different market conditions and timeframes?

- This one: Yes

This one: Yes

B) Logical CoherenceCan I explain why the edge should persist?

- This one: Partially (I understand the general approach, but not every parameter choice)

This one: Partially (I understand the general approach, but not every parameter choice)

C) Emotional ResilienceCan I stick with this strategy through a 20% drawdown?

- This one:Not sure yetbut here’s the thing: the historical drawdown on this strategy so far has been less than 5%

This one:Not sure yetbut here’s the thing: the historical drawdown on this strategy so far has been less than 5%

If I can’t answer “yes” to all three, the strategy stays in incubation no matter how good it looks on paper.


## The Hesitation Every Systematic Trader Faces


Here’s what I’ve learned after years of running systematic strategies:

The hesitation before going live is a feature, not a bug.

It forces you to confront whether you truly trust yourprocessor whether you’re just chasing performance numbers.

Every systematic trader I know faces this. Even with experience. Even with winning strategies.

Because trusting something you can’t fully understand is hard.

That’s why having a process is an edge…

Hving a validation process rigorous enough that you can trust the results, even when you don’t understand every mechanical detail.

For now, this Dollar strategy stays in incubation.

Not because it’s failing. Not because the genetic algorithm platform isn’t good (it’s actually incredible).

But because I’m not ready to trust it with real money.

And in systematic trading, that hesitation might be the smartest trade I make all year.

Here’s the truth about this platform:

It goes way beyond just creating trading strategies. And without a doubt, the money I invested in it has paid itself back 100x over the past 7 years.

This platform is different. It has multiple statistical tests specifically designed to catch overfitting and is designed for non-programmers.

I use it all the time for generating and validating trading ideas.

Okay, enough teasing.

Let me tell you which platform it is and more importantly share the strategy code with you…


## The Platform and The Code

