---
title: The One Candlestick Pattern That Only Works on Fridays
author: The Rogue Quant
url: https://roguequant.substack.com/p/what-happens-when-you-add-seasonality
date: 2025-11-10T02:27:03+00:00
source: substack
paywalled: True
---

# The One Candlestick Pattern That Only Works on Fridays

**URL**: https://roguequant.substack.com/p/what-happens-when-you-add-seasonality
**Date**: 2025-11-10T02:27:03+00:00
**Author**: The Rogue Quant

---

I don’t work Fridays.

My work is flexible. I could work any day I want.

Usually I set some days for research, others for writing, but pretty much every day I do some sort of backtesting.

Except Fridays.

Fridays are for the kids. Before they head to school, we hang out. Make breakfast. Do nothing productive.

Which makes this discovery particularly ironic.

The edge I just found in Gold futures? It only works on the day I chose not to work.

The market doesn’t care about my schedule.

But it does care about the calendar.


#### In today’s article you’ll see:


1.The day-of-week analysis that revealed one trading day that made all the money (while the other four days dragged down the results)

2.The classical chart pattern everyone recognizes but nobody tests on this specific day (291 trades over 18 years with 56.7% win rate and 10% drawdown)

3.The full strategy code including the stupidly simple time-based exit that outperformed every stop-loss variation I tested

Let’s start with how I found it.

This Substack is powered bybacktests, forward tests, LLMs, and people like you. Subscribe if you likedata-driven strategy buildingwithout the guru nonsense. Free is cool.Paid is cooler.


## PART 1: THE DAY-OF-WEEK DISCOVERY


I was testing candlestick patterns on Gold futures - 240 minutes bars, to be specific.

I usually test a candlestick pattern within a specific context.

I’ve done this before in past articles…

You can find here:


#### I Backtested Another Famous Candlestick Pattern on 18 Years of Data... And Found Out You're Using It Wrong


Here…


#### I Backtested a Famous Candlestick Pattern on 43 Futures Markets...


And here…


#### Holy Grail or Holy Fail? Backtesting Candlestick Patterns


Some worked occasionally.

Some didn’t work at all.

Nothing that made me want to write home about it.

I’ve been doing this long enough to know that “average” results usually hide something.

But you need to be careful not to torture the data until it shows you what you want to see.

That’s why I follow my strategy development process religiously.

I know it’s robust enough to eliminate most overfitting traps.

Anyway, you know how sometimes a strategy works great in certain conditions and terribly in others?

The average masks the real story.

And one tactic you can start using is simply defining some standard contexts.

Have some ready-to-use templates to test new ideas.

Let me explain…

Instead of just testing a candlestick pattern in isolation, try testing it:

- In a specific volatility context

In a specific volatility context

- During uptrends (or downtrends)

During uptrends (or downtrends)

- When volume hits certain levels

When volume hits certain levels

You get the idea.

I have my context templates ready to go.

Makes my life much easier when testing new (or old) ideas.

Back to the story…

I started splitting the data.

First by year.Then by month.Looking for any pattern in when this thing actually worked versus when it didn’t.

Nothing jumped out.

Then I tried something simpler:day of week.

Using my seasonality context template, I split the exact same strategy into five separate backtests.

Monday trades only. Tuesday trades only. And so on.

Here’s what came back:

Monday:Negative returnsTuesday:Negative returnsWednesday:Negative returnsThursday:Negative returnsFriday:Positive returns 15 of 18 years

Oh, commissions and slippage included…

You don’t usually see splits this clean.

Ran it on different date ranges making sure not to use all my historical data at once.

Same result every time.

The pattern I was testing? It only works on one specific day of the week.

The other four days actively lose money.

291 trades over 18+ years.

All concentrated on this one day.

Now here’s what made this interesting to me.

This isn’t some weird proprietary thing.

It’s not a custom indicator I invented.

It’s a pattern you’d recognize immediately if you’ve ever read a trading book.

Simple as that.

Let’s move on.

I want to show you what I think is actually happening on this day that makes the pattern work.


## PART 2: WHY FRIDAYS ARE DIFFERENT


So why does this pattern only work on Fridays?

I have a theory. And the data backs it up.

Friday is the only day traders don’t want to hold overnight risk into the weekend.

Think about what happens on a Thursday evening.

Thursday evening you close a position. Market reopens Friday morning. Something goes wrong? You have all day to react.

Friday evening? You close (or don’t) and the market’s shut for 60+ hours.

Geopolitical events.Central bank surprises.Random headlines that move Gold.

Institutions hate weekend exposure.

Especially in Gold futures where geopolitical risk is everything.

So they adjust. They hedge before the weekend.

This creates a different volatility signature on Fridays.

Not more volatility. Different.

The classical pattern I’m testing? It captures this Friday repositioning behavior perfectly.

And the numbers prove it.


## THE NUMBERS


Here’s the full breakdown of what this strategy did over 18 years.


#### Overall Performance (2007-2025)


- Total Net Profit: $66,505

Total Net Profit: $66,505

- Total Trades: 291

Total Trades: 291

- Win Rate: 56.70% (165 winners, 126 losers)

Win Rate: 56.70% (165 winners, 126 losers)

- Profit Factor: 2.18

Profit Factor: 2.18


#### Risk Metrics


- Average Win: $745.79

Average Win: $745.79

- Average Loss: $448.81

Average Loss: $448.81

- Win/Loss Ratio: 1.66

Win/Loss Ratio: 1.66

- Max Drawdown (trade close to trade close): $7,005 (7.00%)

Max Drawdown (trade close to trade close): $7,005 (7.00%)

- Max Drawdown (intra-day peak to valley): $10,440 (10.44%)

Max Drawdown (intra-day peak to valley): $10,440 (10.44%)


#### Trade Behavior


- Max Consecutive Wins: 9

Max Consecutive Wins: 9

- Max Consecutive Losses: 5

Max Consecutive Losses: 5

- Average Bars in Total Trades: 3.00

Average Bars in Total Trades: 3.00

The average trade lasts 3 bars maximum.

That tells you something important.

This is not a swing trade strategy. This is not “buy and hold for weeks.”

This captures the initial Friday move and gets out.

Fast in. Fast out.


#### Year by Year Breakdown


The strategy made money in 16 out of 19 years.

Not every year wins.Some years barely move.Some years lose.

But the edge has been consistent enough over 18 (almost 19) years through multiple market regimes that it compounds.


## WHY THIS WORKS (The Logic Behind the Numbers)


Three things.


#### 1. The pattern only works on Fridays


I tested the same pattern on Monday, Tuesday, Wednesday, Thursday.

All negative.

Friday? 2.18 Profit Factor.

Why?

Institutions don’t hold Gold risk into weekends. They adjust positions. Hedge exposure.

That creates directional flow.

The pattern catches that flow.


#### 2. I’m using the WRONG pattern


Here’s the twist.

The pattern I’m trading is a bearish signal.

Classic textbook says “this pattern = sell.”

I’m buying it.

I tested the bullish version (the “correct” one). Didn’t work.

Only the bearish pattern + long entry + Friday = edge.

Why does a bearish pattern work for longs?

Because Friday repositioning creates false bearish signals.

Looks like weakness.

It’s actually institutional hedging.


#### 3. Fixed time exit beats everything


I tested:

- ATR stops

ATR stops

- Percentage stops

Percentage stops

- Trailing stops

Trailing stops

- Profit targets

Profit targets

Fixed time exit (X bars, then out) beat all of them.

Why? Friday moves are fast. Catch the initial pop. Get out before the chop.

That’s the logic.

Now you want the specifics, I know…

> What pattern exactly?How many bars to exit?The complete strategy code?


What pattern exactly?How many bars to exit?The complete strategy code?

Quick note before we dive into the code.

If you’re an annual subscriber, you already have access to my complete strategy database nearly 200 backtested strategies from academic papers, all organized and written in plain English.

That’s where ideas like this one come from.

Alright, here’s the code.


## PART 3: [Complete Strategy Code]

