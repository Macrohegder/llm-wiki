---
title: The Breakout Scoring System That Delivered 19% Per Year
author: The Rogue Quant
url: https://roguequant.substack.com/p/the-breakout-scoring-system-that
date: 2025-07-01T21:27:03+00:00
source: substack
paywalled: True
---

# The Breakout Scoring System That Delivered 19% Per Year

**URL**: https://roguequant.substack.com/p/the-breakout-scoring-system-that
**Date**: 2025-07-01T21:27:03+00:00
**Author**: The Rogue Quant

---


## Nothing is Original


One of the books that most influenced my creative process of creating automated strategies was 'Steal Like an Artist' by Austin Kleon.

If you haven't read it, here's the (almost) one-paragraph summary…

> Kleon argues that nothing is completely original.All creative work builds on what came before, so the key is to "steal" from multiple sources you admire and combine them into something uniquely yours.It's not about copyingone thing, but aboutcollecting influencesand remixing them through your own perspective and style.


Kleon argues that nothing is completely original.

All creative work builds on what came before, so the key is to "steal" from multiple sources you admire and combine them into something uniquely yours.

It's not about copyingone thing, but aboutcollecting influencesand remixing them through your own perspective and style.

That's exactly how I approach building trading systems.

I don't have the pretension of finding a totally original edge that nobody's seen before.

My goal is to identify things that work and make small modifications that make sense and fit my trading style.

Every trading system I've ever built, every strategy that has ever worked, started with me stealing an idea from someone else.

I steal from old trading books.

I steal from conversations with other quants.

And my favorite place to steal from?

Dense, boring academic papers that most people would rather use as coasters.

The secret to trading isn't having a single, brilliant, original idea.

It's about seeing the good ideas hiding in plain sight and combining them into something new.

Something that is uniquely yours.

Today's post is the story of one such theft.

This Substack is powered bybacktests, forward tests, LLMs, and people like you. Subscribe if you likedata-driven strategy buildingwithout the guru nonsense. Free is cool.Paid is cooler.


## Find Something Worth Stealing


Your source material is everywhere.

You just have to be curious enough to look.

My curiosity recently led me to this paper:

> "Are simple technical trading rules profitable in bitcoin markets?"by Niek Deprez and Michael Frömmel


"Are simple technical trading rules profitable in bitcoin markets?"by Niek Deprez and Michael Frömmel

The researchers tested a mind-numbing75,360 different trading rules.

The central question was whether simple technical trading rules canoutperform a buy-and-hold strategyin the Bitcoin market.

The technical indicators primarily covered were:

• Filter rules,• Channel Breakout (CB),• Moving Averages (MA),• Support and Resistance (S&R),• Relative Strength Indicator (RSI)• On-Balance Volume Averages (OBV)

Spoiler alert:

Yes, the study found that simple technical trading rules can outperform buy-and-hold, especially on a risk-adjusted basis.

But what caught my attention was a simple sentence buried in the middle of all that data...

> "...combining multiple technical trading rules has real diversification benefits and helps limit large drawdowns."


"...combining multiple technical trading rules has real diversification benefits and helps limit large drawdowns."

Now, you might say, "Nothing groundbreaking there."

And you'd be right, but...

Here's where the light bulb went off:

What if I took the best-performing indicators from their study, created a ranking system, and applied it not to Bitcoin but to a completely different market?

Suddenly, a new idea worth exploring.

And that's exactly the strategy I'm about to show you...


## Steal Like An Artist


Based on the technical trading rules from the paper, I decided to test some breakout indicators.

My natural tendency was to think about indexes because it’s all about trending…

But instead of creating a system with 5 indicators (which would probably lead to overfitting), I defined a simple rule:

> if the system identified 2 out of 5 conditions for entering a trade, then we'd have a buy signal.


if the system identified 2 out of 5 conditions for entering a trade, then we'd have a buy signal.

Here's how the scoring works:

If the first entry signal appears → add 1 pointIf the second entry signal appears → add 1 more pointAnd so on, up to the 5 chosen signals

But here's the key:you only need 2 out of 5 signals to trigger an entry.

Think of it like a jury that doesn't need unanimous agreement just a majority vote.

Here are the five signals I chose:

1. Short Channel Break + Volume:Classic breakout of the recent high, but only if volume backs it up. Price moves without volume tend to be fake.

2. Medium Channel Break:A breakout of a longer lookback period. This suggests the move might have real legs, not just short-term noise.

3. Bollinger Band Break:When price closes outside the upper band, it's statistically significant. The market is moving with unusual force.

4. Volatility Expansion:I look for periods when the range compresses tight, then suddenly expands. It's like a spring releasing stored energy.

5. ATR Momentum Filter:A simple check that we're buying into strength above the channel middle, not catching a falling knife.

The rule was simple:at least two signals must agree.

(Way cleaner than trying to optimize 5 different indicators simultaneously, which usually ends in tears.)

Here are the results…


## The Backtest Results


I tested this remixed approach on Nasdaq futures, 4-hour bars, over the last 5 years.

Here's what my version produced:


#### Core Numbers:


- Net Profit: $155,525.00 (1.8 profit factor)

Net Profit: $155,525.00 (1.8 profit factor)

- Win Rate: 55%

Win Rate: 55%

- Total Trades: 139 over 5 years

Total Trades: 139 over 5 years


#### Year by Year



#### Other Key Metrics:


- Annual Rate of Return: 19%

Annual Rate of Return: 19%

- Buy & Hold Return: 67%

Buy & Hold Return: 67%

- Return on Account: 581%

Return on Account: 581%

- Max. Drawdown (trade close to trade close): 27%

Max. Drawdown (trade close to trade close): 27%

- Average Trade Net Profit: $1,119

Average Trade Net Profit: $1,119

- Ratio Avg win / Avg Loss: 1.48

Ratio Avg win / Avg Loss: 1.48

As you can see, the numbers are solid. And this was before any optimization.

I even ran a walk-forward analysis and the results held up always a good sign.

I also did a parameter stabilization analysis.

Instead of optimizing dozens of variables I only optimized 3 key parameters.

The performance clusters remained stable across different parameter choices.

Change the lookback from 10 to 12? Still worked.

This suggests we have an edge here, not just optimized noise.

Before I show you the complete code to test this yourself, let me share 3 key lessons...


## Three Key Lessons


Testing this multi-confirmation approach taught me three key lessons:

Lesson 1: Academic Ideas Need Real-World Translation

The paper's insight about combining signals was solid, but their Bitcoin results didn't directly transfer to equity futures.

I had to adapt the concept to fit the NQ's behavior patterns and volatility characteristics.

Lesson 2: Sum Signals, Don't Stack Indicators

Instead of creating some Frankenstein system with overlapping indicators, I used a simple scoring approach. Each signal adds +1 to a counter. Need 2+ points to trade. Done.

This is way cleaner than traditional indicator stacking and avoids the overfitting death trap that kills most multi-indicator systems.

Lesson 3: Steal Frameworks, Not Just Strategies

Don't try to copy strategies literally. Focus on the frameworks and test them in different markets.

The "multiple confirmations" concept is the real gold here. This same scoring approach could work for mean reversion, momentum, volatility breakouts…

Sometimes the methodology is worth more than the actual strategy.

Now let's get to the part I know you're waiting for...


## The Complete Code

