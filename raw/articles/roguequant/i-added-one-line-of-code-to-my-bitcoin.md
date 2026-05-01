---
title: I Added One Line of Code to My Bitcoin Strategy and the Profit Factor Jumped From 1.96 to 3.53
author: The Rogue Quant
url: https://roguequant.substack.com/p/i-added-one-line-of-code-to-my-bitcoin
date: 2025-11-02T21:44:45+00:00
source: substack
paywalled: True
---

# I Added One Line of Code to My Bitcoin Strategy and the Profit Factor Jumped From 1.96 to 3.53

**URL**: https://roguequant.substack.com/p/i-added-one-line-of-code-to-my-bitcoin
**Date**: 2025-11-02T21:44:45+00:00
**Author**: The Rogue Quant

---

Lately I’ve been backtesting more crypto strategies…

And there are countless reasons why, but the main one is simple:

> You find more edge with straightforward ideas in crypto than almost anywhere else.


You find more edge with straightforward ideas in crypto than almost anywhere else.

The market is still inefficient.

Especially when you compare it to something where every edge has been arbitraged away by high frequency algos.

Bitcoin? Still has room to breathe.

And one of my favorite types of strategies to test is momentum.

Simply because it works.

The logic is sound.The math checks out.Price that’s moving tends to keep moving.

But this time I tested something different.

Instead of buying when the trend is screaming strong...

I bought when the trend looked meh…

Not weak. Not dead. Just... underwhelming.

And it performed better than the traditional approach.

112 trades. 60% win rate. Profit factor over 3.5. Win/Loss average ratio 2.3

In today’s article you’ll see:

- The classic momentum indicator everyone knows (and the unconventional zone that caught 68 winning trades)

The classic momentum indicator everyone knows (and the unconventional zone that caught 68 winning trades)

- The one-line filter that improved profit factor by 80% (it blocks trades when trends look “too perfect”)

The one-line filter that improved profit factor by 80% (it blocks trades when trends look “too perfect”)

- The full code behind the paywall — including the counterintuitive exit I’ve never seen used in 200+ strategies tested

The full code behind the paywall — including the counterintuitive exit I’ve never seen used in 200+ strategies tested

Let’s dive in.

This Substack is powered bybacktests, forward tests, LLMs, and people like you. Subscribe if you likedata-driven strategy buildingwithout the guru nonsense. Free is cool.Paid is cooler.


## Why RSI Is Perfect for Momentum (And Why Most Traders Use It Wrong)


If you’ve been trading for more than 5 minutes, you know what RSI is.

The Relative Strength Index measures how fast price is moving and how strong that movement is.

It oscillates between 0 and 100.

And it’s probably the most popular momentum indicator out there.

For good reason.

RSI is excellent at identifying when price has momentum behind it. When something is actually moving, not just twitching around.

Most momentum strategies wait for RSI to hit extreme readings.

They wait for it to scream “STRONG TREND HERE!”

They wait until the move is so obvious that your grandmother could spot it on a chart.

Then they enter.

But when momentum is THAT obvious... when everyone can see it... you’re not early.

You’re the exit liquidity for people who entered 3 days ago.


## The Unconventional Zone That Actually Works


So I tested something different.

What if instead of waiting for extreme RSI readings...

You bought when RSI showed momentum was building but not yet screaming?

Not weak momentum (RSI below 50 doesn’t work great for long entries).

Not extreme momentum (RSI above 80 means you’re late).

But that middle zone where momentum exists... it’s just not advertising itself yet.

Think of it like catching a wave as a surfer.

The worst surfers wait until the wave is at its peak. By then, it’s too late to position.

The best surfers see the wave forming early. They paddle into position while everyone else is still deciding.

That’s what this strategy does.

It finds momentum that’s there... but not obvious yet.

And here’s the thing that makes it work even better:

It has a filter that blocks trades when the trend looks “too perfect.”

When Bitcoin is making clean higher highs and higher lows the strategy doesn’t enter.

It waits for the messy setups.

The ones that don’t look quite right.

I know it sounds backwards.

But the backtest doesn’t lie…


## The One-Line Filter That Changed Everything


Here’s where this strategy gets really interesting.

Remember how I said it looks for momentum that’s building but not obvious yet?

That’s only half the equation.

The other half is AVOIDING momentum that looks too good.

Let me explain.

Sometimes Bitcoin will be in a perfect uptrend.

Clean higher highs. Clean higher lows. Picture-perfect textbook pattern.

And the RSI might be in that ideal zone.

Everything looks great.

Most traders would enter immediately.

This strategy doesn’t.

It has a simple filter, literally one line of code, that checks if the trend looks “too perfect.”

If Bitcoin is making that clean stair-step pattern everyone loves?

The strategy blocks the trade.

Let’s see the results of adding this filter in the strategy…


#### Before adding the filter…



#### After the filter…


The profit factor jumped from 1.96 to 3.53.

That’s an 80% improvement.

And the win rate went from 53.7% to 60.7%.

So what does this filter actually do?

It blocks trades when Bitcoin is in a “clean” uptrend.

And the numbers prove it: this single filter improved the strategy in so many different ways.

I’ll show you the exact filter and logic in a moment.

But first, let’s dive in into the strategy numbers…


## The Numbers


Here’s the full breakdown of what this strategy did over 7 years.

Overall Performance (2018-2025)

- Total Profit: $339,965

Total Profit: $339,965

- Total Trades: 112

Total Trades: 112

- Win Rate: 60.71% (68 winners, 44 losers)

Win Rate: 60.71% (68 winners, 44 losers)

- Profit Factor: 3.53

Profit Factor: 3.53

Risk Metrics

- Average Win: $6,975

Average Win: $6,975

- Average Loss: $3,053

Average Loss: $3,053

- Win/Loss Ratio: 2.28

Win/Loss Ratio: 2.28

- Max Drawdown (trade close to trade close: $27,845 (27.85%)

Max Drawdown (trade close to trade close: $27,845 (27.85%)

Trade Behavior

- Max Consecutive Wins: 11

Max Consecutive Wins: 11

- Max Consecutive Losses: 5

Max Consecutive Losses: 5

- Average Bars in Winning Trades: 3.37

Average Bars in Winning Trades: 3.37

- Average Bars in Losing Trades: 3.70

Average Bars in Losing Trades: 3.70

The average winning trade lasted 3.37 days.

That tells you something important…

This is a short-term momentum edge.

It captures 3-4 day moves and gets out.

Not a “buy and hold for months” strategy.


## Year by Year Breakdown


The strategy made money in 7 out of 8 years.

2018 was the only red year. Lost 1%.

2025 is crushing it so far: +42% with an 80% win rate.


## What Makes This Work (The Logic Behind the Numbers)


The performance is one thing.

But let me tell you WHY this works.

Because understanding the logic is more important than memorizing the numbers.


#### Reason #1: It catches momentum early


The unconventional RSI zone (which I’ll reveal in a moment) catches moves before they become obvious.

When you’re early, you get better risk/reward. Your stop is tighter. Your profit target is further.


#### Reason #2: It avoids “perfect” trends


That one-line filter that blocks picture-perfect uptrends?

It’s brilliant.

Because when a trend looks perfect on a chart, it means everyone sees it. And when everyone sees it, you’re (probably) late.

The filter forces the strategy to enter on pullbacks and messy setups. Where you’re actually early.


#### Reason #3: The exits are smarter than the entry


Most traders obsess over entries.

This strategy proves that exits matter more.

One exit is time-based (because short-term edges don’t last long).

The other exit is counterintuitive.

It gets you out when something specific happens that signals momentum is stalling.

And it’s what transforms this from a mediocre strategy into a profitable one.

By now you’re probably thinking:

> “Okay, I get it. Unconventional RSI zone. One-line filter. Counterintuitive exit. Cool story. But WHERE’S THE ACTUAL CODE?”


“Okay, I get it. Unconventional RSI zone. One-line filter. Counterintuitive exit. Cool story. But WHERE’S THE ACTUAL CODE?”

Fair question.

What exact RSI numbers am I using?

What’s the logic behind that filter that blocks “perfect” trends?

And what’s that exit that improved the strategy?

So enough teasing.

Here you go…


## [Complete Strategy Code]

