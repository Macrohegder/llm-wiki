---
title: I Backtested Another Famous Candlestick Pattern on 18 Years of Data... And Found Out You're Using It Wrong
author: The Rogue Quant
url: https://roguequant.substack.com/p/i-backtested-another-famous-candlestick
date: 2025-10-26T04:06:48+00:00
source: substack
paywalled: True
---

# I Backtested Another Famous Candlestick Pattern on 18 Years of Data... And Found Out You're Using It Wrong

**URL**: https://roguequant.substack.com/p/i-backtested-another-famous-candlestick
**Date**: 2025-10-26T04:06:48+00:00
**Author**: The Rogue Quant

---

If you’re anything like me, you’ve been waiting for this...

One of the best series just released a new episode.

No, not The Office.

Definitely not Game of Thrones.

I’m talking about…


#### Holy Grail or Holy Fail? Backtesting Candlestick PatternsSeries…


Never heard about it?

You can check the previous episodes here:


#### I Backtested a Famous Candlestick Pattern on 43 Futures Markets...


And here:


#### Holy Grail or Holy Fail? Backtesting Candlestick Patterns


And by popular demand (okay, like three people asked), I’m back with another backtest...

This time it’s one of the most famous candlestick patterns out there.

Maybe THE most famous.


#### The Hammer.


In today’s article, you’ll discover:

- Why 18 years of data shows the Hammer works... but not the way you think

Why 18 years of data shows the Hammer works... but not the way you think

- The one thing every trading book recommends that actually KILLS your win rate

The one thing every trading book recommends that actually KILLS your win rate

- How a single filter increased profits by 32% (with barely fewer trades)

How a single filter increased profits by 32% (with barely fewer trades)

So grab your coffee (or whiskey, no judgment here) and let’s dive in.

This Substack is powered bybacktests, forward tests, LLMs, and people like you. Subscribe if you likedata-driven strategy buildingwithout the guru nonsense. Free is cool.Paid is cooler.


## What the Hell is a Hammer Anyway?


Let me steal the definition from Investopedia:

> “The hammer is a bullish reversal candlestick pattern characterized by a small body near the top, a long lower wick, and little to no upper shadow. It signals a shift from selling to buying pressure.”


“The hammer is a bullish reversal candlestick pattern characterized by a small body near the top, a long lower wick, and little to no upper shadow. It signals a shift from selling to buying pressure.”

If you’re a visual guy like me…

The story behind the pattern goes like this:

Imagine you’re watching the market in real-time.

Sellers show up early and push price DOWN hard (that’s the long lower shadow).

They’re aggressive. They’re confident. They smell blood.

But then...

Buyers step in and say “Nah, not today” and reject those lows completely.

Price closes near the high of the day, leaving sellers trapped and confused.

The candle literally looks like the market tried to hammer through the floor... and failed.

It’s a rejected selloff.

A failed breakdown.

What you always hear is…

“When you see a hammer after a downtrend, especially in oversold conditions... that’s your signal. The reversal is coming.”

Sounds logical, right?

Price got pushed down, buyers defended, reversal incoming.

Buy the hammer. Ride the bounce. Profit.

Simple.

Clean.

Obvious.

But here’s the thing about “obvious” in trading...

What if everyone has it backwards?


## The Test


I did what most traders never do:

Actually tested it.

Here’s the setup:

- Market:S&P 500 E-mini futures (@ES)

Market:S&P 500 E-mini futures (@ES)

- Period:January 2007 to October 2025 (18 years)

Period:January 2007 to October 2025 (18 years)

- Data:Daily timeframe

Data:Daily timeframe

Now, if you remember what Investopedia says…

The Hammer is supposed to be areversal pattern that appears after a downtrend.

So naturally, I started by following the textbook:


#### Version 1: The “By-The-Book” Hammer


- Detect hammer pattern

Detect hammer pattern

- But ONLY when price is in a downtrend

But ONLY when price is in a downtrend

- Buy next bar at market

Buy next bar at market

- Hold for 5 bars

Hold for 5 bars

- Exit

Exit

I defined ‘downtrend’ as the close of yesterday is below the 20-day moving average.

Simple.

Seems logical, right? Wait for the downtrend, spot the hammer, catch the reversal.

The results?

- Total Net Profit:$16,325

Total Net Profit:$16,325

- Profit Factor:1.30

Profit Factor:1.30

- Win Rate:61%

Win Rate:61%

- Number of Trades:44

Number of Trades:44

Hmm... profitable, but come on…

Only 44 trades in 18 years? That’s like 2-3 trades per year.

Not something that I like to see in a backtest.

And the average win/loss ratio? 0.82!

Can’t trade that.

So I thought...

“What if the downtrend filter is actually HURTING the strategy?”

So I tried another version…


#### Version 2: All Hammers (No Downtrend Filter)


I removed the downtrend requirement and tested EVERY hammer that appeared.

Bull market, bear market, sideways… didn’t matter.

If the pattern formed, I took the trade.

The results?

- Total Net Profit:$60,325 (+270%!)

Total Net Profit:$60,325 (+270%!)

- Profit Factor:1.62(+24%!)

Profit Factor:1.62(+24%!)

- Win Rate:63%

Win Rate:63%

- Number of Trades:120

Number of Trades:120

Wait... WHAT?

Removing the “textbook rule” made the strategy almost4X more profitable?

This is already interesting...

But we’re not done yet.

Because even at $60k with a 1.62 Profit Factor, there’s still a problem:

It’s a meh strategy…

And the average loss is BIGGER than your average win.

You’re winning 63% of the time, but you’re giving back more on the losses.

It’s profitable... but like I said…

Meh…

So I thought: what if I added a filter for what NOT to do…


## The “What NOT to Do” Filter


Here’s where things get weird.

Most traders think about filters as: “What conditions do I NEED for a trade?”

But what if the real question is:“What trades should I AVOID?”

So I did something simple:

I created a filter that identifies these “obvious” setups...

And then does the OPPOSITE.

Instead of taking them, I avoid them.

One condition.One line of code.Goes against everything you’ve been taught.

The results?

Well... let me just show you the numbers…


#### Version 3: The “What NOT to Do” Filter


- Total Net Profit:$87,787 (+46% from baseline!)

Total Net Profit:$87,787 (+46% from baseline!)

- Profit Factor:2.26 (+40%!)

Profit Factor:2.26 (+40%!)

- Win Rate:67%

Win Rate:67%

- Number of Trades:113 (only 7 fewer trades)

Number of Trades:113 (only 7 fewer trades)

Look at that equity curve.

Tradable.

And here’s the twist:

The filter removed only 6% of the trades... but improved the Profit Factor by 40%.

Just 7 trades.

But those 7 trades? They were dragging down the entire strategy.

Want to know what the filter is?

The ONE CONDITION that turns a 1.62 Profit Factor into 2.26?

The exact rule that adds $27k to your bottom line?

Here you go…


## [Complete Strategy Code]

