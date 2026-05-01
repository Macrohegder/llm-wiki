---
title: This Nasdaq Strategy Has A 75% Win Rate (Until We Found the December Bug)
author: The Rogue Quant
url: https://roguequant.substack.com/p/this-nasdaq-strategy-has-a-75-win
date: 2026-04-30T20:40:59+00:00
source: substack
paywalled: True
---

# This Nasdaq Strategy Has A 75% Win Rate (Until We Found the December Bug)

**URL**: https://roguequant.substack.com/p/this-nasdaq-strategy-has-a-75-win
**Date**: 2026-04-30T20:40:59+00:00
**Author**: The Rogue Quant

---

In 700 BC the Roman calendar had a bug: roughly sixty winter days had no names at all.

King Numa inherited a ten-month system from Romulus and eventually patched it adding two new months.

But the unnamed slot kept causing problems for centuries. Rome was never quite sure what to do withDecember.


### Two and a half thousand years later, NQ has the same problem.


The PivotShift rule is a long-only setup on NASDAQ daily bars.

The entry trigger is structural: a confirmed pivot high that fails to clear a recent prior pivot low (the market’s most recent upside attempt printingbelowa reference point from a few bars back). That’s the compression.

The exit is also structural: a clean break out of a recent range, a signal that the compression has resolved.

Across nineteen years the rule won75.0% of 152 trades, generated $361,405 net on a fixed 1-contract / $100k baseline (commissions and slippage included), and turned three losing years (and two flat ones) into fifteen winning ones.

Then 2022 happened. One trade (entered on December 31, 2021) held 154 calendar days into the bear market and exited at–$70,660.

That single trade accounted for almost the entire 32.1% drawdown of the strategy.

I backtest strategies so you don't have to guess. Just code, data, and stuff that actually works. Free is good.Paid gets you the full playbook.


### Here’s the shape of it. Daily bars. Long only.


The full code with the exact pivot lookback, the lag, the breakout window, the parameter calibration and everything in between I’ll share in a moment.

What matters for this post iswhenthe trades fire…


### And here’s where it breaks.


Of the 152 trades,14 were December entries. The cohort:

- 8 winners, 6 losers:57.1% win rateversus the strategy’s 75.0% baseline.

8 winners, 6 losers:57.1% win rateversus the strategy’s 75.0% baseline.

- Profit factor on the cohort:0.32versus the overall 2.43.

Profit factor on the cohort:0.32versus the overall 2.43.

- Net P&L:–$61,425.

Net P&L:–$61,425.

The other 138 trades made $422,830.

December alone bled $61k while the rest of the calendar paid for it.

Even if you remove the catastrophic 2021-2022 trade entirely, the remaining 13 December trades still earn only a1.47 profit factor, well below every other month.

I don’t see it as an outlier but more as a regime: late-December entries land into thin holiday liquidity, year-end tax repositioning, and the start of multi-month bear corrections in three of fourteen cases.

Which led me to…


### The one-line fix.


So I tested a simple idea. What if I exclude every December from the sample?

Block new entries during the month, leave exits as they are — a trade opened in November can still close in January or beyond.


### Here’s what changes across nineteen years.


Fewer trades, more profit, smaller drawdown, higher win rate, higher profit factor.

The structural losing years (2008, 2011) stay losses, those are real regime breaks, not calendar artifacts.

But 2022 alone improves by $23,845, because the worst entry of the strategy is no longer in the sample at all.


### Three robustness checks (so this isn’t one lucky sequence)


A single backtest is one path through history.

Before trusting it, several standard tests answer different versions of the question:

> “what if the trades had landed differently?”


“what if the trades had landed differently?”


#### 1. Order Permutation Test: does theordermatter?


Take the 142 trades and shuffle the order 1,000 times, replaying each path under fixed-1-contract sizing.

Same trades, same final equity ($478,540), what changes is thepath.

The maximum drawdown across orderings clusters in a tight band:median 23.7%, 95th percentile 51.8%, worst single ordering 98.1%.

The real chronological sequence drew24.7%, almost exactly on the median.

The strategy did not get lucky with the order. (It also did not get unlucky.) Zero of the 1,000 random orderings took the account to ruin.


#### 2. Monte Carlo Bootstrap: what if thesearen’tthe trades?


Resample 142 tradeswith replacement(so the same trade can appear multiple times, or not at all), 1,000 times.

Replay each path.

This is the“could this strategy keep working?”test.

99.9% of resampled runs finish profitable.

Final-equity 5th/50th/95th percentile:$293k / $477k / $683k.

The real result of $479k sits squarely on the median.

Probability of equity hitting zero at any point:0.30%.

This isn’t a thin-tail strategy whose headline is being carried by one or two outlier trades.


#### 3. Risk of Ruin × Return/DD — the size-or-don’t decision (1-year horizon).


A different question this time.

The first two tests asked whether the 19-year track record was real or lucky.

This one asks something more practical:

> if I started this strategy today with $X in the account, what’s the probability of going broke in the first year?


if I started this strategy today with $X in the account, what’s the probability of going broke in the first year?

Here’s how each simulation works. Pick 7 trades at random from the 142 historical tradeswith replacement, so the same trade can show up more than once or not at all.

Seven trades is roughly what the strategy averages in a year.

Play them out one at a time, starting from a chosen capital level. If the account ever drops below $20,000 (the margin required to keep one NQ contract open), the simulation counts as “ruin” and stops.

Otherwise it runs to the end of the seven trades. Repeat 2,500 times per row of the table.

The highlighted row is the first starting capital where the chance of getting wiped out in the first year drops below 2%:$70k.

Below it, that chance climbs past 5%.

At the$100k baseline, the chance of ruin is0%across all 2,500 simulations.

The Return/DD column lands at2.82×at $100k meaning: in a typical year the strategy earns about three times what it loses at its worst drawdown.

One caveat. The simulation treats each trade as independent of the next, meaning a losing trade doesn’t make the following trade more likely to lose.

In reality, losers tend to cluster (bear markets) and so do winners (bull markets).

There are other tests like the block bootstrap that does exactly that (I’ll come back to it later.)

But wait….


### Yes, I know what you’re thinking.


There is one major objection.

“The filter is curve-fit. You found the worst month after the fact and excluded it.”

That’s exactly the right concern.

The full December cohort is 14 trades with a 57% win rate and a 0.32 profit factor.

Remove the worst trade entirely and December’s profit factor stays at 1.47against the rest of the year’s 2.43.

So yes, the rule was discovered retroactively but the strategy remains solid without it.

And let’s not forget…


### What the Romans eventually did.


Numa’s reform didn’t delete December. It just stopped pretending the unnamed winter slot would behave like the rest of the year. Caesar finished the job five centuries later with the Julian calendar.

The PivotShift's fix is faster and smaller: skip the one month where the edge underperforms, and let the other eleven do their job.


### Next…


Before I share the full code with the December filter…

You should already know that every “winning” backtest looks great until OOS happens. Or costs eat the edge. Or it works for 18 months and quietly dies.

What if you could go from idea to incubation-ready strategy without leaving one tab?

That’s what annual subscribers are about to get inside theTRQ Portal: the research operating system I built for myself:

> →Research: paper replications, CoT positioning, seasonal patterns. Where ideas come from.→Trading Ideas: every strategy I’ve ever published, with full code..→Validation: the28-test Batterythat puts any trade list through the same statistical gauntlet institutional desks use. Bailey-López de Prado, BCa bootstraps, double-bootstrap drawdowns etc answered in 30 seconds.→Portfolio: combine validated strategies, see correlation, drawdown…


→Research: paper replications, CoT positioning, seasonal patterns. Where ideas come from.→Trading Ideas: every strategy I’ve ever published, with full code..→Validation: the28-test Batterythat puts any trade list through the same statistical gauntlet institutional desks use. Bailey-López de Prado, BCa bootstraps, double-bootstrap drawdowns etc answered in 30 seconds.→Portfolio: combine validated strategies, see correlation, drawdown…

Take a look inside…

Wow, where do I sign?

Great.

Now the code…


## The Complete Strategy Code

