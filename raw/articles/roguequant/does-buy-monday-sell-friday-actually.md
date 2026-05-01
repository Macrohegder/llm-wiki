---
title: Does "Buy Monday, Sell Friday" Actually Work? I Backtested it
author: The Rogue Quant
url: https://roguequant.substack.com/p/does-buy-monday-sell-friday-actually
date: 2025-07-16T02:55:43+00:00
source: substack
paywalled: True
---

# Does "Buy Monday, Sell Friday" Actually Work? I Backtested it

**URL**: https://roguequant.substack.com/p/does-buy-monday-sell-friday-actually
**Date**: 2025-07-16T02:55:43+00:00
**Author**: The Rogue Quant

---

I'm traveling with the kids, and even though the focus is on playing with them all the time, I still have some free time when they're asleep…

and I use that time to run some backtests, of course :)

The article is the result of a backtest I did on a well-researched anomaly…

> The weekday effect


The weekday effect


## What is the Weekday Effect?


The weekday effect is a market anomaly suggesting that certain days of the week tend to produce higher or lower returns than others.

The paper I was reading basically tells to…

"Buy on Monday, sell on Friday."

The theory goes that markets often decline on Mondays (weekend news, position adjustments) and recover during the week, with Friday often showing strength as institutional money flows in before the weekend.

It sounds almost too naive to work in today's markets, right?

This Substack is powered bybacktests, forward tests, LLMs, and people like you. Subscribe if you likedata-driven strategy buildingwithout the guru nonsense. Free is cool.Paid is cooler.


## Testing the Basic Idea on NASDAQ


I decided to test this with the simplest possible approach on NASDAQ futures.

Here's literally all the code I started with:

Six lines. That's it.

Buy every Monday, sell every Friday, regardless of market conditions.


## The Results Were... Interesting


The basic strategy actually showed positive returns over the backtest period, but with some serious problems…

- Long flat period:from Nov 2021 to Dec 2023

Long flat period:from Nov 2021 to Dec 2023

- No risk managementwhatsoever

No risk managementwhatsoever

- Horrible Sharpe ratiodue to volatility

Horrible Sharpe ratiodue to volatility

- Ignored market contextcompletely

Ignored market contextcompletely

It was profitable in raw terms, but it seems we could improve it…


## How to improve a trading strategy?


This got me thinking…

What if the weekday effect has some validity, but needs proper risk management and market context?

So I enhanced the basic strategy with:

- Trend filter: Only buy Mondays when above the 60-day (~3 months) moving average

Trend filter: Only buy Mondays when above the 60-day (~3 months) moving average

- Volatility filter: Skip trades when daily range is too extreme (below 0.5% or above 3.0%)

Volatility filter: Skip trades when daily range is too extreme (below 0.5% or above 3.0%)

- Stop losses: 3% maximum loss per trade

Stop losses: 3% maximum loss per trade

- Smart exits: Trailing stops and profit targets

Smart exits: Trailing stops and profit targets

I didn’t optmize any parameter…


## The Results


The difference was dramatic:

- Drawdowns cut by 30%

Drawdowns cut by 30%

- Profit Factor improved from 1.34 to 1.84

Profit Factor improved from 1.34 to 1.84

- Win Rate improved from 57% to 66%

Win Rate improved from 57% to 66%

- Avg Trade Net Profit from $632 to $873

Avg Trade Net Profit from $632 to $873

- Much smoother equity curve

Much smoother equity curve

- Actually tradeable with real money

Actually tradeable with real money

The enhanced version proved that the weekday effect might have some statistical edge, but only when combined with proper risk management and market awareness.


## But Here's the Thing...


You might be thinking…

"Doesn't all this extra filters defeat the purpose of a simple weekday strategy?"

Fair point.

But here's what I learned:

Market anomalies like the weekday effect aren't magic.

They're statistical tendencies that work better in certain market conditions.

The "enhancement" isn't about complexity for its own sake – it's about being smart enough to step aside when conditions aren't favorable.

The original six-line strategy was throwing money at the market every Monday regardless of whether we were in 2008, 2020, or a bull market.

The enhanced version asks:"Is this a good Monday to buy?"

And it basically implements a moving average filter with a stop loss/profit targets…

So no complexity here.


## The Real Lesson


Simple strategies can work, but they need guardrails.

The weekday effect appears to have some statistical validity, but only when you're intelligent about when and how you apply it.

Raw market anomalies are starting points, not finished products.


## The Complete Enhanced Code


Now, the code you were expecting…

It’s show time…
