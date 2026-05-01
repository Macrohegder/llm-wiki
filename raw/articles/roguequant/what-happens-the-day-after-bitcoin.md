---
title: What Happens the Day After Bitcoin Falls (or Rallies) Three Days Straight?
author: The Rogue Quant
url: https://roguequant.substack.com/p/what-happens-the-day-after-bitcoin
date: 2025-04-25T19:05:07+00:00
source: substack
paywalled: False
---

# What Happens the Day After Bitcoin Falls (or Rallies) Three Days Straight?

**URL**: https://roguequant.substack.com/p/what-happens-the-day-after-bitcoin
**Date**: 2025-04-25T19:05:07+00:00
**Author**: The Rogue Quant

---

A few weeks ago…

Friend:“I’m going to wait for Bitcoin to drop three days in a row, then buy.”

Me:“Why?”

Friend:“Because it always goes up on the fourth day.”

Me:“Have you tested that?”

Friend:“I’ve seen it happen plenty of times.”

Me: …

Warning:This newsletter contains equal parts trading algorithms and dad jokes. Subscribe at your own risk.

ok.

So I ran the numbers

Because that’s what data-driven traders do.

We can test almost any idea, whether it’s somethingcrazyunconventional

> “Does Bitcoin rally during a full moon?” (I did test that…)


“Does Bitcoin rally during a full moon?” (I did test that…)

or more reasonable ones…

> “What happens to Bitcoin when the S&P 500 drops more than 3 % in a week?”


“What happens to Bitcoin when the S&P 500 drops more than 3 % in a week?”

Creativity + available data is the whole game (tbh, available data is the 80/20)

Here’s the test.


## Experiment Setup


1. Download daily BTC-USD prices back to 2014

2. Identify two streaks:

> 3-UP– three consecutive green candles3-DOWN– three consecutive red candles


3-UP– three consecutive green candles

3-DOWN– three consecutive red candles

3. Measure thenext-day returnafter each streak

First, we import libraries and download the data

Then we compute the daily returns…

Calculate up and down days…

Next, calculate 3-day streaks…

Then, the next-day return

And finally, the stats…

Now the results…

- 3-DOWN occurrences:354— avg next-day+0.17 %— 55.7 % green

3-DOWN occurrences:354— avg next-day+0.17 %— 55.7 % green

- 3-UP occurrences:515— avg next-day+0.53 %— 55.3 % green

3-UP occurrences:515— avg next-day+0.53 %— 55.3 % green

Oh, and we could plot some graphs too…


## What the Numbers Say



### Meaning…


- Momentum beats dip-buying- the pay-off after 3-UP is roughly 3× the pay-off after 3-DOWN.

Momentum beats dip-buying- the pay-off after 3-UP is roughly 3× the pay-off after 3-DOWN.

- Fear of heights is costly- “overbought” keeps running more often than it collapses.

Fear of heights is costly- “overbought” keeps running more often than it collapses.

- Frequency matters- 3-UP fires 45 % more often, compounding gains.

Frequency matters- 3-UP fires 45 % more often, compounding gains.

- Edge is slim- fees and slippage will eat a chunk of +0.17 %. A single stat is not a system.

Edge is slim- fees and slippage will eat a chunk of +0.17 %. A single stat is not a system.

To be honest, we can’t call it an edge.


### Why this isnota tradable edge, yet


This is just basic stats.

I didn’t test the statistical significance or

…Autocorrelation risk (Daily returns aren’t independent. Standard t-tests assume independence and might overstate the edge) or

…Survivorship & data-source quirks(I relied on Yahoo Finance’s BTC series. Different exchanges or a data glitch could move the average) or

…Transaction costs and slippage (A one-day hold after a tiny edge gets shredded by fees)

among many others.

But I’ll repeat myself again:

> This isbasic statistics, nothing more.


This isbasic statistics, nothing more.

But every systematic strategy starts here:one hypothesis, one quick test, next hypothesis…

The real work is ahead: statistical tests, regime filters, cost modeling, WFA… and then wiring it into a full trading system (which btw is not the end point)


## Where Data-Driven Traders Go Next


If you want to explore more simple ideas (simple in the sense of implementing) go ahead and try:

- Test 2-, 4-, 5-day streaks. Does the edge persist?

Test 2-, 4-, 5-day streaks. Does the edge persist?

- Split bull vs. bear regimes (above/below the 200-DMA).

Split bull vs. bear regimes (above/below the 200-DMA).

- Hold 3–5 days instead of one. Does momentum snowball?

Hold 3–5 days instead of one. Does momentum snowball?

- Combine with a volatility filter or position sizing.

Combine with a volatility filter or position sizing.


## Want the Deep Dive?


Now what?

If this kind of no-BS, data-first exploration is what you’ve been hunting for, hit “Subscribe.”

And if you’re already on the free list, consider upgrading to paid because…

Tomorrow’s issue delivers a complete, statistically vetted trading system: walk-forward results, code, execution rules, the works.

No paywall teasers, no half measures.

Fair enough, I want that

Talk soon,

-LeoThe Rogue Quant

Like my GIFs? Wait till you see my trading systems. Free gets you laughs, paid gets you backtests.

DISCLAIMER:This information is provided for educational and informational purposes only. It is not financial advice, nor a recommendation to buy or sell any securities or financial instruments. Trading involves substantial risk and is not suitable for every investor. You are solely responsible for your own investment decisions and should seek advice from a licensed financial advisor before acting on any information provided in this code and article. The author(s) and publisher disclaim all liability for any loss or damage arising directly or indirectly from the use of this code, including but not limited to trading losses, data inaccuracies, or system errors. Use this code at your own risk.
