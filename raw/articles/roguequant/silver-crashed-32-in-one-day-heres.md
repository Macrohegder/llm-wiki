---
title: Silver Crashed 32% in One Day. Here's Why I Slept Fine.
author: The Rogue Quant
url: https://roguequant.substack.com/p/silver-crashed-32-in-one-day-heres
date: 2026-02-01T19:14:31+00:00
source: substack
paywalled: True
---

# Silver Crashed 32% in One Day. Here's Why I Slept Fine.

**URL**: https://roguequant.substack.com/p/silver-crashed-32-in-one-day-heres
**Date**: 2026-02-01T19:14:31+00:00
**Author**: The Rogue Quant

---

October 19, 1987.The Dow drops 22% in a single day.

May 6, 2010.The Flash Crash wipes $1 trillion in 36 minutes.

January 30, 2026.Silver opens at $115. Hits $118. Then craters to $74.

A 32% drop. In. One. Day.

You probably heard about theseBlack Swanspopularized by Nassim Nicholas Taleb — the events you can’t predict, but must survive.

And the thing is if you had one strategy, fully allocated to Silver, yesterday you’d be staring at a hole in your account.

But what if you had 3 strategies? 5? 10?

That’s what today’s article is about.

Here’s what you’ll see today:

- Why chasing the “Holy Grail” strategy is the fastest way to blow up

Why chasing the “Holy Grail” strategy is the fastest way to blow up

- A simple Silver reversal system with a 3.6 Profit Factor (and 18 years of data)

A simple Silver reversal system with a 3.6 Profit Factor (and 18 years of data)

- The math behind portfolio diversification (it’s simpler than you think)

The math behind portfolio diversification (it’s simpler than you think)

- Why I slept fine last night while Silver was crashing

Why I slept fine last night while Silver was crashing

- Full strategy code + backtest results

Full strategy code + backtest results

Let’s go.

I backtest strategies so you don't have to guess. Just code, data, and stuff that actually works. Free is good.Paid gets you the full playbook.


## The “Holy Grail” Is the Fastest Way to Lose Money


Let’s do some math.

Silver Futures last Friday:

- Open: $115.88

Open: $115.88

- High: $118.45

High: $118.45

- Low: $74.00

Low: $74.00

That’s a $41.88 drop from open to low.

One Silver contract is 5,000 ounces. Each $1 move = $5,000.

So if you were long one contract at the open with no stop (or your stop got blown through):

$41.88 × 5,000 = $209,400

One contract. One day.

Now imagine that was your only strategy. Your whole account, riding on Silver.

This is the Holy Grail trap. You find something that works, you fall in love with it, you go all-in.

And then a Black Swan shows up.


## The Boring Fix That Saves Careers


What if you had five strategies instead?

Let’s say your strategies performance looked like this:

Same Black Swan. Different outcome.

The Silver strategy still got hit. But it wasn’t 100% of the account. It was 20%.

And the other strategies?

If you’ve done your homework - built systems with low correlation to each other - they didn’t care about Silver’s meltdown.

They were doing their own thing, in their own markets, with their own logic.

This is the whole point of portfolio diversification. Not to avoid losses. You can’t avoid losses.

But to make sure one bad day doesn’t end your career.


## The Silver Strategy


Now let me show you something…

I’ve been testing a simple Silver strategy…

Two entry conditions.

One exit rule.

If you’ve been following me for a while, you know I like simple.

Start simple, get fancy later.

Most of the time, simple is enough.

You don't need a Masters in financial engineering or data science. I know because I have one - and I barely use it to develop my trading systems.

You don’t need the latest deep learning framework.

You don’t need to spend six months building a transformer model that predicts Silver prices based on satellite images of mining trucks. (Though honestly, that might work.)

Don’t get me wrong. I’m all for learning. The more knowledge you have, the better.

And the more diverse, the better - ideas connect in non-linear ways, and sometimes a concept from one field unlocks something in another (especially when walking or taking a shower :))

Anyway, take a look at how a simple reversal pattern with a clean exit can do the job…


### The Setup


Before I show you the results, I want you to know exactly what I tested.

I like to say most traders don’t lose money from bad entries but from bad testing.

Here’s the backtest environment:

- Market:@SI (Silver Futures)

Market:@SI (Silver Futures)

- Timeframe:1440 min

Timeframe:1440 min

- Range:02/01/2007 → 12/31/2024

Range:02/01/2007 → 12/31/2024

- Costs included:Slippage + commissions ($65 + $5 per round-trip)

Costs included:Slippage + commissions ($65 + $5 per round-trip)

- Position size:1 contract

Position size:1 contract

Here are the results…

Now, you might be looking at the equity curve and noticing it runs until 01/30/2026. But I just said I tested until 12/31/2024...

Here’s what’s going on.

I always leave a chunk of data completely untouched.

The strategy was trained on data from 2007 to 2017. That’s my in-sample period:

Then I validated it on 2018 to 2024. That's my out-of-sample:

Which means all of 2025 (and January 2026) was also out-of-sample. Data the system never saw during development.

I do this for extra insurance. It doesn’t eliminate the possibility that OOS performance was luck - nothing does - but it puts the odds more in my favor.

These are small details I add to my development process. Each one reinforces the thesis that the strategy has a better chance of surviving live trading.

But as I always say: the ultimate boss is live trading. There’s no escaping that.

Back to the data.

18 years. 180 trades. Here’s what it looks like:

The equity curve isn’t a perfect 45-degree line. There’s a flat period in the middle where the system went nowhere.

Most traders would have abandoned it.

But look what happened after.

Out of 18 years, only 4 were negative. And the worst? -4.18% in 2008.

Here’s my point:

These are solid numbers… 3.62 Profit Factor is excellent. 62% win rate with a 2:1 reward-to-risk ratio is also good.

And I still wouldn’t trade it alone.

Because last Friday could have been one of those 68 losing trades. And if this was my only system, I’d be questioning everything right now.


## Building a Real Portfolio


If you've been following me for a while, you know I've been writing about this topic…

For example, a lot of people think they need $50k to build a proper portfolio…

I wrote how to start one with a 2.6 Profit Factor strategy and a lot less capital here:


#### How to Build a Real Trading Portfolio on a Small Account


If you want to go even smaller - two strategies, under $500 in margin, opposite market behaviors - you can also read another piece here:


#### How to Build an Uncorrelated 2-Strategy Portfolio With Under $500 in Margin


And just last week,Algomatic Tradingtook this concept further and added one of my strategies into a portfolio of 5 strategies.

The result? A 74% reduction in drawdown compared to trading each strategy individually.

You can read about this collaboration we did here:


## What’s Inside the Silver Strategy


So far I’ve shown you the results. The equity curve. The year-by-year breakdown.

But I haven’t told you what the strategy actually does.

Here’s the short version:

It’s a reversal pattern. Simple logic.

The exit? Even simpler. One condition. Based on how the market opens relative to recent behavior.

Just keep reading to get access to the full code.

Also… if you’re not a subscriber yet, the best value is becoming anannual subscriberto get access to:

- Historical archive of all 30+ published strategies (including this one)

Historical archive of all 30+ published strategies (including this one)

- My app with 250+ strategies extracted from academic papers (written in plain English)

My app with 250+ strategies extracted from academic papers (written in plain English)

- My Trading Ideas GPT (launching Q1)

My Trading Ideas GPT (launching Q1)

- First-hand access to the experiments I’m running with LLMs focused on trading

First-hand access to the experiments I’m running with LLMs focused on trading

- Direct access to me via email for any questions about systematic trading

Direct access to me via email for any questions about systematic trading

- And more to come…

And more to come…

You can subscribe here:

I backtest strategies so you don't have to guess. Just code, data, and stuff that actually works. Free is good.Paid gets you the full playbook.

Now, the part you’ve been waiting for…


## [Complete Strategy Code]

