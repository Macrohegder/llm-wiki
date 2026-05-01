---
title: I'd Rather Be Profitable Than Right. Inside My $244k Gold Strategy (No Crystal Ball Required)
author: The Rogue Quant
url: https://roguequant.substack.com/p/id-rather-be-profitable-than-right
date: 2026-01-24T20:40:12+00:00
source: substack
paywalled: True
---

# I'd Rather Be Profitable Than Right. Inside My $244k Gold Strategy (No Crystal Ball Required)

**URL**: https://roguequant.substack.com/p/id-rather-be-profitable-than-right
**Date**: 2026-01-24T20:40:12+00:00
**Author**: The Rogue Quant

---

I have a friend who is right about Gold more often than I am.

Way more often.

But I’m profitable. He’s not.

The difference is that he’s trying to predict while I’m building systems.

Having a smart opinion feels good.

Being the guy who “called it” at the bar.

Posting your thesis on X with 47 charts.

But here’s what nobody wants to hear:

> Being right and making money are two different games.


Being right and making money are two different games.

My friend plays the prediction game.

He studies macro. He tracks central banks. He knows which Middle East conflict will move Gold 2%.

I don’t play that game.

I play the “what does the market actually do” game.

So instead of building another opinion...

I backtested a structural breakout system on Gold.

That’s what today’s article is about.

Here’s what you’ll see:

- A simple 2-rule entry that waits for Gold to show its hand (not your opinion)

A simple 2-rule entry that waits for Gold to show its hand (not your opinion)

- The “Surf” trailing stop that follows structure instead of arbitrary levels

The “Surf” trailing stop that follows structure instead of arbitrary levels

- Why I deliberately left 2025 out of the backtest (and what happened when the system ran blind)

Why I deliberately left 2025 out of the backtest (and what happened when the system ran blind)

- The 50% giveback rule that protects profits without killing the trade

The 50% giveback rule that protects profits without killing the trade

- Full code + 19 years of results

Full code + 19 years of results

Let’s go.


### THE SETUP


Before I tell you what the strategy is, I want you to know exactly what I tested.

Because most traders don’t lose money from bad entries.

They lose money from bad testing.

Here’s the test environment:

Market:@GC (Gold Futures)Timeframe:1440 min (Daily)Range:02/01/2007 → 01/23/2026Costs included:Slippage + commissions ($30 + $5 round-trip)Position size:1 contract

I split the 19-year like this:

- In-Sample(training): 02/01/2007 → 12/31/2019

In-Sample(training): 02/01/2007 → 12/31/2019

- Out-of-Sample(validation): 01/01/2020 → 01/31/2024

Out-of-Sample(validation): 01/01/2020 → 01/31/2024

And I added two minimum requirements:

- At least50 trades in IS

At least50 trades in IS

- At least50 trades in OOS

At least50 trades in OOS

I also deliberately left all of 2025 out.

This isn’t the same as out-of-sample.

Even though I used a solid OOS window, I still left out an entire year the strategy hadneverbeen trained on.

Even if you’re “not looking” to your OOS data you can still contaminate it.

For example:

- You develop on IS → test on OOS

You develop on IS → test on OOS

- OOS fails → you go back to IS, adjust

OOS fails → you go back to IS, adjust

- Test on OOS again → works better now

Test on OOS again → works better now

- Repeat a few times...

Repeat a few times...

Result:You just optimized for OOS indirectly.

You SAW the data. You adjusted based on what failed. Even if you didn't "train" on it directly.

That’s why leaving 2025 completely out is different:

2025, I:

- NEVER looked at

NEVER looked at

- NEVER tested

NEVER tested

- NEVER adjustedanything based on it

NEVER adjustedanything based on it

- It’s 100% blind

It’s 100% blind

It's as close as you can get to forward testing (which btw is another crucial step of the process of building robust trading strategies)

Now let me show you the strategy that came out of this process...


### THE LOGIC


This is astructural breakout systemon Gold.

A simple one…

Just two filtered entries and three smart exits.


### The Regime Filter


I use a ridiculously simple long-term filter to define the macro bias.

Bullish regime → only long breakoutsBearish regime → only short breakouts

That’s it.

Just:“Is Gold trending up or down on a macro level?”

This one filter kills most bad trades before they happen (in theory of course)


### The Two Entries


Entry #1: Long BreakoutWhen Gold is in a bullish regime AND breaks above recent structure → Buy

Entry #2: Short BreakoutWhen Gold is in a bearish regime AND breaks below recent structure → Sell Short

That’s it.

The regime filter tells us which direction to play.The structural break tells us when to enter.

No predictions required.


### The Exits (where most traders fail)


Most people obsess over entries.

I obsess over exits.

This system hasthreeways to get out:

1. The “Surf”: A structural trailing stop that follows the market’s rhythm instead of arbitrary levels.

2. The 50% Giveback Rule: Once you’re up big, the system won’t let you give back more than half. It protects profits without killing winners early.

3. Fixed Risk/Reward: Defined stop loss and profit target. Not every trade hits the target... but when they do, the payoff covers a lot of losses.

That’s the framework.

Simple regime filter.Structural breakouts.Smart exits.

Now let me show you what it actually did over almost 19 years...


### THE RESULTS (2007 → 2026)


Over the full test window:

Total Net Profit:$244,880Profit Factor:1.72Trades:312Win Rate:39.74%Avg Trade:$784.87Avg Win / Avg Loss:$4,717 / $1,809 =2.61:1Max Drawdown (intraday):20%Annual Return:7.00%

Solid numbers.

312 trades over 19 years.40% win rate.But winners are 2.6x bigger than losers.

That’s the whole game.

Shorts slightly outperform longs (2.01 vs 1.60 profit factor).

Winning trades hold for 9 bars on average.Losing trades exit after 3.6 bars.

Cut fast. Ride long.


### YEAR-BY-YEAR BREAKDOWN


Here’s how it performed year by year:

Profitable in17 out of 19 years.

Only 2 losing years: 2010 and 2019.

Again… no prediction needed

That’s why…


### PROCESS > OPINION


As a systematic trader, you can have all the opinions you want.

> Butdata > feelings.


Butdata > feelings.

You don’t need to decode the macro puzzle.You don’t need to predict what central banks will do next.

You need totestif there’s an edge in your hypothesis.

The first step is to have access to quality data.

I’ve been usingFMP (Financial Modeling Prep)more and more... and the data quality is excellent.

The link above is an affiliate link (I don’t usually do this, but the service is solid and I personally use it.) I worked out a deal with them so Rogue Quant readers get a discount on subscriptions.

They even provide alternative data like CoT.

Highly recommended.


#### Back to the point:


You need aprocessto avoid the countless backtest traps (lookahead bias, IS/OOS data burn, overfitting, etc.).

You need aprocessto have confidence allocating capital to a strategy.

And even then... it’s not a guarantee it’ll be profitable in live trading.

But you did your part.You backtested correctly.You validated statistically.You put it in forward testing and monitored live execution.

And just as important as all of this:

> Build a portfolio of strategies instead of searching for the one holy grail.


Build a portfolio of strategies instead of searching for the one holy grail.

Anyway...

If you’re a subscriber, you already know what comes next.

If you’re not yet, the best value is becoming anannual subscriberto get access to:

- Historical archive of all published strategies

Historical archive of all published strategies

- My app with 250+ strategies extracted from academic papers (written in plain English)

My app with 250+ strategies extracted from academic papers (written in plain English)

- My Trading Ideas GPT (launching Q1)

My Trading Ideas GPT (launching Q1)

- The Rogue Quant community

The Rogue Quant community

- And more to come…

And more to come…

Now, the most anticipated part…


## [Complete Strategy Code]

