---
title: The 75% Win Rate Strategy I Found While Looking for Something Else
author: The Rogue Quant
url: https://roguequant.substack.com/p/the-75-win-rate-strategy-i-found
date: 2025-08-29T05:50:41+00:00
source: substack
paywalled: True
---

# The 75% Win Rate Strategy I Found While Looking for Something Else

**URL**: https://roguequant.substack.com/p/the-75-win-rate-strategy-i-found
**Date**: 2025-08-29T05:50:41+00:00
**Author**: The Rogue Quant

---

Yesterday I was improving my filter function to work within my trading strategies.

The concept is straightforward:

- develop a strategy in a predetermined period without using the entire historical database.

develop a strategy in a predetermined period without using the entire historical database.

- Then apply optimization across hundreds of filters - trend, volatility, time-based, mean reversion - either on entries, exits, or stops.

Then apply optimization across hundreds of filters - trend, volatility, time-based, mean reversion - either on entries, exits, or stops.

- Test whether the filter improves the original strategy's results.

Test whether the filter improves the original strategy's results.

If it improves, run walkforward analysis leaving out 6-12 months for simulated incubation.

If it passes, deploy to live account and monitor for at least 3 months or 30 trades, whichever comes first.

I learned this filter technique from Andrea Unger years ago.

While I don't follow his strategy development process, the filter concept works.

Before you mention“this is overfitting”,read my previous article on systematic validation methods here:


#### The Systematic Trader's Guide to Strategy Optimization: From $165k to $218k With One Filter


Anyway, back to the story…

I was expanding my filter library, specifically looking to add more trending filter concepts.

Then I recalled the “Hurst Exponent”.


## The Academic Indicator Nobody Uses


The Hurst Exponent measures persistence or anti-persistence in time series data.

In short…

Values above 0.5 indicate trending behavior - yesterday's direction tends to continue today.

Values below 0.5 suggest mean-reverting behavior - what went up yesterday likely comes down today.

Exactly 0.5 represents random walk - no predictable pattern.

Think of it as mathematical measurement of market personality - trending versus choppy.

I studied this during economics school but only tested applications during my algorithmic trading masters program years ago.

And even during my Master’s, I tested the Hurst concept in the development of a few strategies, but it never felt like a “wow, this is amazing…” moment.

This Substack is powered bybacktests, forward tests, LLMs, and people like you. Subscribe if you likedata-driven strategy buildingwithout the guru nonsense. Free is cool.Paid is cooler.


## The Problem


I didn't want to code the Hurst calculation from scratch.

I needed something built into TradeStation.

Searched everywhere. Nothing.

TradeStation's function library contained dozens of indicators but no Hurst implementation.

"Weird," I thought. "I've seen this somewhere recently."

Then it hit me. Build Alpha.

Build Alpha is an algo trading platform that creates trading strategies using billions of signal combinations.

But I use it differently than 99% of users - not for actual strategy deployment, but for trading ideas and statistical validation.

Their statistical testing tools are exceptional.

Since Build Alpha exports strategies to both EasyLanguage and Python, my plan was simple: generate strategies using Hurst filters, export the code, reverse-engineer their implementation, then integrate it into my filter library.

That was the plan…


## The Surprise


I configured Build Alpha for ES futures data and initiated the genetic algorithm.

Three minutes later (or less), the platform started showing me the first strategies it had found using the Hurst signal.

And the first generated strategy displayed this equity curve:

Remember I wasn’t looking for a strategy but the formula behind the Hurst…

But that smooth upward trajectory caught my attention immediately.

I exported the strategy to TradeStation to examine the Hurst implementation.

The function wasn't appearing in my searches because I was looking for "HurstCoeff" or "HurstExp." The actual name was simply "Hurst."

Anyway, I integrated the Hurst function into my filter library (as you can see below) but remained curious about that equity curve statistics.

So I took the strategy from Build Alpha and dropped it into TradeStation…

Then I got this…

And this…

3.36 Profit Factor. 75% win rate. 136 trades over 17 years.

Win/loss ratio: 1.09.

I immediately searched for errors.

Reviewed the code for biases. Nothing suspicious.

Added slippage and commissions. Results barely changed as you can see below…

Powered by code, stats, and a bit of rebellion. Free starts the journey. Paid takes you to the destination


## The Skeptic's Protocol


Excitement wasn't my first reaction. Suspicion was.

Exceptional-looking strategies demand systematic interrogation:

Data mining concern:Probable. Build Alpha tests thousands of combinations.

Sample size adequacy:136 trades over 17 years isn't massive, but it's ok.

Results credibility:3.36 Profit Factor is high but not absurd for long-only index strategies.

Regime diversity:Test period includes 2008 crisis, 2020 pandemic, multiple Fed cycles, varying volatility environments.

Economic logic:Does the underlying concept make behavioral sense?

This last question proved most interesting.

This wasn’t some Frankenstein mix of random indicators.

> It boiled down to just three rules (I’ll reveal them shortly).


It boiled down to just three rules (I’ll reveal them shortly).

Rules so simple they almost feel trivial…


## Build Alpha's Statistical Arsenal


Build Alpha has something most platforms lack: serious validation tools.

Most backtesting software gives you basic performance metrics and calls it done.

Build Alpha goes deeper.

It shows that impressive backtests are worthless if they can't survive statistical scrutiny.

Their testing suite includes Metrics breakdown (e-ratio, PnL, Sharpe…), Monte Carlo analysis, variance testing, noise test, signal breakdown and more.

I ran the Hurst strategy through dozens of tests.

I’ll show here two…


### Test 1: The Variance Test


Simple concept: take the exact same 136 trades but randomize their timing across the 17-year period.

Same entries, same exits, same outcomes - just scrambled randomly through time.

If the strategy were just lucky, the original timing should perform no better than random timing.

Results: The real strategy outperformed 80% of the scrambled versions.

This suggests the strategy captures something about market timing, not just directional bias.


### Test 2: The Stress Test


Monte Carlo analysis runs thousands of simulations with different market scenarios, trade sequences, and outcome variations.

The original strategy consistently landed in the top 20% of results across most scenarios.

Maximum drawdown under worst-case conditions: around $40k on a strategy that grew nearly $900k. Manageable risk for the returns generated.


### The Honesty Check


These tests don't guarantee future performance.

They can't predict regime changes, structural market shifts, or periods when underlying behavioral patterns break down.

What they suggest is that during the test period, the strategy captured genuine edge rather than mining random patterns.

After the statistical validation, one number matters:25.9% ruin probability.

That means a 74% chance of long-term success. Not bulletproof, but significantly better than random.


## The Economic Logic Test


Statistics tell half the story.

The real test is whether underlying logic makes economic sense.

The strategy exploits a persistent behavioral pattern: in trending markets, short-term oversold conditions tend to reverse quickly.

A classic indicator identifies genuine short-term oversold conditions - moments when selling pressure temporarily exhausts itself.

The Hurst filter above 0.5 ensures trades only occur during trending modes - when dips are more likely to be bought rather than signaling deeper weakness.

Time-based exits prevent overstaying when conditions change.

Simple. Logical. Statistically validated (at least with historical data)


## The Timeline Test


Statistical validation demanded regime analysis.

How did the strategy behave across different market environments?

2007-2009 (Financial Crisis):23 trades, remained profitable. Hurst filtering avoided worst choppy periods.

2010-2015 (Low Volatility Grind):Strongest performance. 41 trades, 85% win rate. Perfect environment for buying dips in trending markets.

2016-2019 (Trump Rally):Continued effectiveness. 31 trades, 74% win rate.

2020-2024 (COVID/Fed Chaos):Most concerning period. Different volatility regime, altered market structure. 41 trades, 71% win rate. Still profitable.

The strategy wasn't riding one bull market.

It adapted across multiple regimes because core logic - buying oversold conditions in trending markets - remained valid.


## The Bottom Line


I went searching for a simple formula and accidentally discovered a strategy that passes almost every validation test I know(I didn’t run any WFA, nor incubation or forward testing I must say)

Is it bulletproof? No.

Will it work forever? Probably not.

But it passed a lot of statistical tests, it’s logical, and robust across different market regimes over 17 years.

More importantly, it's simple enough to understand and implement.

Oh, I almost forgot to mention something important…

> The strategy delivered solid results across nearly all the indexes I tested, such as YM (E-mini Dow Futures).


The strategy delivered solid results across nearly all the indexes I tested, such as YM (E-mini Dow Futures).

E-mini MidCap400 - EMD

E-mini Nasdaq - NQ

Below,I’ll walk you through exactly how the strategy works, both in EasyLanguage code and in plain English, so you can easily adapt it to your programming language of choice.

Enjoy!
