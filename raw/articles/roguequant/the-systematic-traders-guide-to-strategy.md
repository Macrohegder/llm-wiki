---
title: The Systematic Trader's Guide to Strategy Optimization: From $165k to $218k With One Filter
author: The Rogue Quant
url: https://roguequant.substack.com/p/the-systematic-traders-guide-to-strategy
date: 2025-08-25T02:58:06+00:00
source: substack
paywalled: True
---

# The Systematic Trader's Guide to Strategy Optimization: From $165k to $218k With One Filter

**URL**: https://roguequant.substack.com/p/the-systematic-traders-guide-to-strategy
**Date**: 2025-08-25T02:58:06+00:00
**Author**: The Rogue Quant

---

In 1954, Ray Kroc walked into a small burger joint in San Bernardino, California, owned by the McDonald brothers.

He didn't see what everyone else saw - just another hamburger stand.

He saw a system that could bescaled and standardized.

The brothers had already figured out the hard part:

Fast food that people actually wanted to buy.

But Kroc saw dozens of tiny improvements that could transform their decent local business into a money-printing empire.

He didn't try to reinvent the hamburger.

He didn't create a revolutionary new restaurant concept from scratch.

He took something that already worked and made it work exponentially better.

That obsession with systematic improvement over ground-up innovation is exactly what separates profitable systematic traders from the broke dreamers still searching for the "holy grail" strategy.

Most traders spend years trying to discover the next breakthrough system.

Smart traders take existing strategies and systematically make them better.

The difference? Smart traders actually make money.


## What we're going to cover today


In today's article, I'm going to show you a systematic technique capable of transforming any mediocre trading strategy into a consistent profit generator.

Here's exactly what we'll cover:

- A real case studyshowing how I took a basic 3-day reversal strategy from $165k to $218k profit using exactly ONE filter

A real case studyshowing how I took a basic 3-day reversal strategy from $165k to $218k profit using exactly ONE filter

- The 100-filter systematic testing frameworkthat I use to upgrade strategies without curve-fitting

The 100-filter systematic testing frameworkthat I use to upgrade strategies without curve-fitting

- Why 95% of traders fail at strategy optimization(and the overfitting trap that destroys even good strategies)

Why 95% of traders fail at strategy optimization(and the overfitting trap that destroys even good strategies)

By the end of this article, you'll understand why hunting for "holy grail" strategies is a waste of time, and how to systematically improve any decent strategy you already have.

Think Ray Kroc, not Thomas Edison.

We're not trying to invent the light bulb.

We're taking McDonald's and turning it into a billion-dollar empire through systematic improvement.

This Substack is powered bybacktests, forward tests, LLMs, and people like you. Subscribe if you likedata-driven strategy buildingwithout the guru nonsense. Free is cool.Paid is cooler.

Let's start with…


## How I upgraded a solid ES reversal strategy with systematic filter testing


I had this mean reversion strategy that worked decently well on ES daily bars.

I don't remember exactly where I got the idea - possibly from Art Collins' excellent book "Beating the Financial Futures Markets", but the logic was dead simple:

The 3-Day Consecutive Reversal Strategy:

- Buy when price drops for X consecutive days

Buy when price drops for X consecutive days

- Sell short when price rises X consecutive days

Sell short when price rises X consecutive days

- Exit all positions after X number of days

Exit all positions after X number of days

Classic mean reversion play.

Clean, logical, profitable.

Here’s the base perfomance:

While the short side was slightly negative, the long side was solidly profitable and the overall equity curve wasn't bad.

The backtest ran from 2007 to 2025 including realistic slippage and commissions.

Solid returns, but I knew there was room for improvement.

The strategy was taking too many low-probability trades during choppy market conditions.

So I decided to run it through my filter optimization toolkit.

Instead of guessing which additional condition might help, I systematically tested it against my library of hundreds of proven filters.

Each filter tested individually to see which one would statistically improve the base performance.

After testing, one filter stood out with significant improvement:

- Total Net Profit:+$40k more profit)

Total Net Profit:+$40k more profit)

- Profit Factor: 1.64 (+12% improvement)

Profit Factor: 1.64 (+12% improvement)

- Win Rate: 51% (maintained consistency)

Win Rate: 51% (maintained consistency)

- Total Trades: 265 (slightly fewer, better quality trades)

Total Trades: 265 (slightly fewer, better quality trades)

$40,000+ in additional profit from adding exactly one filter condition.

And the equity curve?

Way Better…

Same core strategy logic.

Same market.

The only difference was that one additional filter that screened out the noise trades.

This Substack is powered bybacktests, forward tests, LLMs, and people like you. Subscribe if you likedata-driven strategy buildingwithout the guru nonsense. Free is cool.Paid is cooler.=


## The 3-step filter optimization framework that beats guesswork


Now let me show you exactly how this filter testing process works.

Most traders approach strategy improvement like they're throwing darts blindfolded.

They'll add an RSI here, a moving average there, maybe a volume condition "because it feels right."

That's not optimization. That's expensive trial and error.

My approach is systematic:


### Step 1: Take a decent base strategy


Start with something that has sound economic logic and modest profitability.

Like my 3-day reversal system - not spectacular, but profitable and logical.

Key point:You're not looking for perfection. You're looking for a solid foundation that can be systematically improved.


### Step 2: Run it through the filter gauntlet


This is where the magic happens.

I test the base strategy against my library of 100+ individual filters:

- Trend filters(moving averages, breakouts, ADX conditions)

Trend filters(moving averages, breakouts, ADX conditions)

- Momentum filters(RSI levels, MACD signals, rate of change)

Momentum filters(RSI levels, MACD signals, rate of change)

- Volatility filters(ATR conditions, Bollinger squeezes)

Volatility filters(ATR conditions, Bollinger squeezes)

- Volume filters(relative volume, OBV confirmations)

Volume filters(relative volume, OBV confirmations)

- Time Based filters(day of the week, time of the day)

Time Based filters(day of the week, time of the day)

- Price action filters(gap patterns, support/resistance levels)

Price action filters(gap patterns, support/resistance levels)

Each filter gets tested individually.

No stacking, no complex combinations.

Just clean, isolated testing to see which single addition improves performance.


### Step 3: Pick the winner and implement


After testing, I sort results by key metrics: net profit, profit factor, maximum drawdown.

The filter that shows statistically significant improvement across multiple metrics gets permanently added to the strategy.

In this case, one filter emerged as the clear winner- improving profit by $40k while maintaining consistency.


## But wait - isn't testing 100+ filters just sophisticated curve-fitting?


This is the objection I get every single time I share this process.

"Dude, testing hundreds of filters on the same data is textbook overfitting. You're just curve-fitting with extra steps."

Let me be honest: this criticism is valid - IF you do it wrong.

And most traders do it completely wrong.


### The Real Problem: Parameter Hunting vs. Hypothesis Testing


Here's the difference between what kills most traders and what actually works:

What Kills Traders (Parameter Optimization):

- Test RSI levels: 30, 31, 32, 33... up to 70

Test RSI levels: 30, 31, 32, 33... up to 70

- Find that RSI 37.5 works "best" historically

Find that RSI 37.5 works "best" historically

- Optimize moving average periods: 9, 10, 11, 12... up to 50

Optimize moving average periods: 9, 10, 11, 12... up to 50

- Discover that 23-period MA is "optimal"

Discover that 23-period MA is "optimal"

Result: You've memorized random noise in historical data.

What Actually Works (Economic Hypothesis Testing):

- Test if momentum works better during low volatility (Hypothesis 1)

Test if momentum works better during low volatility (Hypothesis 1)

- Test if mean reversion improves after volume spikes (Hypothesis 2)

Test if mean reversion improves after volume spikes (Hypothesis 2)

- Test if trends perform better when clearly established (Hypothesis 3)

Test if trends perform better when clearly established (Hypothesis 3)

Result: You're validating market inefficiencies that exist for economic reasons.

Think of it this way:

Parameter optimizationis like asking:

> "What exact temperature should we cook fries? 347.2°F or 347.3°F?"


"What exact temperature should we cook fries? 347.2°F or 347.3°F?"

You can test a million micro-variations and find the "optimal" temperature that happened to work in your historical sample.

Hypothesis testingis asking:

> "Do customers prefer fresher fries?"


"Do customers prefer fresher fries?"

This is testing a fundamental business principle that should work across locations and time periods.


### Why My 100 Filters Aren't Curve-Fitting


1. Each Filter Tests a Different Economic Principle

- Volatility filter: "Strategies work differently in calm vs chaotic markets"

Volatility filter: "Strategies work differently in calm vs chaotic markets"

- Volume filter: "Price moves with unusual volume are more meaningful"

Volume filter: "Price moves with unusual volume are more meaningful"

- Momentum filter: "Established trends continue longer than random walks"

Momentum filter: "Established trends continue longer than random walks"

These aren't variations of the same thing - they're testing separate market behaviors.

2. ON/OFF Switches, Not Parameter Tweaking

I don't optimize "what RSI level works best."

I test "does overbought/oversold context matter at all?"

Binary questions have binary answers.

No infinite parameter space to get lost in.

3. The Economic Logic Test

Every filter must answer: "Why should this work?" before I test "Does this work?"

No economic story = no testing. Period.


### My Reality Check Framework


Step 1: Economic Logic FirstIf I can't explain to a smart 12-year-old why a filter should work, it doesn't get tested.

Step 2: Separate Validation DataI never select filters based on the same data I test them on. That's like grading your own exam. Also, walk-forward is mandatory with other statistical test like Monte Carlo, Variance testing etc.

Step 3: Forward TestingEvery filter that survives gets tested live with small position sizes. Market reality kills overfitted ideas fast.

Step 4: Continuous MonitoringFilters that stop working (compared to the historical backtesting) get removed. No emotional attachment to "what used to work."


### But…


Do some of my 100+ filters probably contain some curve-fitting? Sure.

That's why 85% of them get rejected during validation.

The 15% that survive aren't perfect - they're just robust enough to work when markets change.

And here's the key: I'm not trying to predict the exact future.

I'm identifying structural market inefficiencies that persist because of:

- Transaction costs

Transaction costs

- Human behavioral biases

Human behavioral biases

- Institutional constraints

Institutional constraints

- Information flow delays

Information flow delays

These change slowly enough for systematic strategies to profit from them.


### The Bottom Line


Testing 100 parameters to find the "perfect" RSI level? That's curve-fitting.

Testing 100 economic hypotheses about market behavior? That's research.

The difference isn't in the quantity - it's in the methodology.

Most traders can't tell the difference.Also, most burn their data in backtesting phase, I don’t. But this is a topic for another article.


## Further Reading…


If you want to dive deeper into the systematic approach to strategy optimization and overfitting detection…

The paper"The Probability of Backtest Overfitting"by Marcos López de Prado and Bailey which provides the mathematical foundation for measuring overfitting probability.

Also, de Prado’s book"Advances in Financial Machine Learning"is essential reading.

Besides that, an easier reading is David Aronson's"Evidence-Based Technical Analysis". A lot of statistical validation (with examples) in trading system development.

The classic"The Evaluation and Optimization of Trading Strategies"by Robert Pardo provides practical frameworks for walk-forward analysis and out-of-sample testing that every systematic trader should understand.

For the behavioral psychology behind pattern-seeking bias,Kahneman and Tversky'spapers on cognitive biases explain why we're evolutionarily programmed to overfit data.

These aren't light reading, but they represent the difference between systematic trading based on academic rigor versus the trial-and-error approach that dominates retail trading forums.

The mathematics don't lie. The methodologies work. The question is whether you'll use them.


#### Anyway, enough theory…



#### Let’s get into the exact code and filter I used to improve the strategy.

