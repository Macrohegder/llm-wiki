---
title: How I Found an Edge in Futures Markets Using AI and a No-Code Tool
author: The Rogue Quant
url: https://roguequant.substack.com/p/how-i-found-an-edge-in-futures-markets
date: 2026-02-23T05:46:29+00:00
source: substack
paywalled: True
---

# How I Found an Edge in Futures Markets Using AI and a No-Code Tool

**URL**: https://roguequant.substack.com/p/how-i-found-an-edge-in-futures-markets
**Date**: 2026-02-23T05:46:29+00:00
**Author**: The Rogue Quant

---

One of the most common questions I get is this:

> “Where do you actually find ideas worth testing?”


“Where do you actually find ideas worth testing?”

The honest answer is: it’s a pipeline.

Ideas don’t appear fully formed.They evolve.

Most of the time, I start with something structural…

Something already studied, documented, or observed repeatedly in market behavior.

For example, theweekend effect.

If you search "weekend effect" on papers.ssrn.com, you'll find dozens of academic papers like these:

This is a topic discussed in multiple academic papers across equities and commodities.

Btw, if you're an annual subscriber, you already have access to my app:

> More than 270 trading strategies extracted from academic research, translated into plain English so you don't have to read a 40-page paper to understand the core idea.


More than 270 trading strategies extracted from academic research, translated into plain English so you don't have to read a 40-page paper to understand the core idea.

The weekend effect is in there.

I backtest strategies so you don't have to guess. Just code, data, and stuff that actually works. Free is good.Paid gets you the full playbook.

But here’s the part most traders miss:

A published anomaly is not a finished strategy.

It’s a starting point.

So last week, I took that starting point and pushed it further.

Here’s what you’ll see today:

- How I usedAIto generate a list of seasonality trading ideas for a specific futures market

How I usedAIto generate a list of seasonality trading ideas for a specific futures market

- How I ran those ideas through a no-code statistical validation workflow — the kind of tool that saves you hours of coding and keeps you from falling in love with overfitted strategies

How I ran those ideas through a no-code statistical validation workflow — the kind of tool that saves you hours of coding and keeps you from falling in love with overfitted strategies

- The one small prompt tweak that turned a decent strategy into something I actually want to trade (full code included)

The one small prompt tweak that turned a decent strategy into something I actually want to trade (full code included)

Let’s dive in.


## The Way I Ask AI For Trading Ideas


I use LLMs a lot, but not to generate “full strategies.”

I use them as anidea engine.

Think of it like having a researcher sitting next to you…but with a completely different brain.

Which means it will hand you hypotheses you’d probably never think to test.

So I started with something thatalreadyhas research behind it (the weekend effect) and asked Claude to expand that starting point into other seasonality angles specifically for Copper.

You’ll get my full prompt at the end of the article.

But the short version is: I asked fora list of testable seasonality hypotheses.

Ideas I could validate quickly with clean rules.

And I forced Claude to think like a researcher by giving it a few constraints:

- No external data(no inventory, macro events, COT, news)

No external data(no inventory, macro events, COT, news)

- No indicators required

No indicators required

- Clear entry + clear exit

Clear entry + clear exit

- A reason why it might exist(so we’re not just pattern-hunting)

A reason why it might exist(so we’re not just pattern-hunting)

- A quick way to falsify it(so I can kill it fast if it’s junk)

A quick way to falsify it(so I can kill it fast if it’s junk)

Then I asked for 10 ideas.

Not “the best one.”Just a list.

Because the magic is generatingenoughideas… and letting backtesting do the selection for you.

Claude came back with a menu ranging from boring to weird:

-Weekday effects.-Short streak behavior.-Simple calendar patterns.-A couple of “this sounds too dumb to work” hypotheses.

Then I sorted the list using one criterion:

Which idea is cheapest to test first?

And the simplest one — the one that required almost no logic at all — is where this whole thing started getting interesting.

In the next section, I’ll show you the baseline idea I tested first… and why it was the right baseline to start with (even though most traders would ignore it).


## The Simple Version Most People Would’ve Left Alone


The simplest idea on the list was…

> The Monday weakness hypothesis.


The Monday weakness hypothesis.

The logic: bad news accumulates over the weekend. Sellers dominate Monday morning. Copper drifts lower early in the week.

So I tested the most basic version possible…

> Sell Monday open. Cover Tuesday open.


Sell Monday open. Cover Tuesday open.

No filters. No conditions. Just the raw anomaly.

Here’s what that looks like on Continuous Copper Futures (HG) going back to 2007:

Not great but not garbage.

Positive expectancy. 49% win rate. But the drawdowns were ugly.

But a weak baseline isn’t a dead end. It’s a starting point with room to improveif you know how to do it.

I’ll say that again because is the most important lessos here:

> “It’s a starting point with room to improveif you know how to do it.”


“It’s a starting point with room to improveif you know how to do it.”

And this is where the workflow matters.


## Is This Edge Real Or Am I Just Torturing Data?


Before I start tweaking anything, I need to know one thing:

Is there any real signal here or am I just torturing data until it confesses?

This is where most retail traders go wrong.

They see a promising equity curve and immediately start adding filters. An indicator here. A regime condition there. Before long they have a Frankenstein strategy that looks incredible on paper and falls apart live.

I don’t do that.

Instead, I run the raw idea through a structured validation workflow first. One that stress-tests the hypothesis statistically before I touch a single parameter.

The tool I use for this doesn’t require any coding. You build the logic visually, run it across a sample of the dataset, and immediately get a picture of whether you’re looking at an edge or a mirage.

The tool is called Build Alpha. If you're interested, reach out. I have something in the works for Rogue Quant subscribers specifically.

But here’s what I check at this stage:

Equity curve. P&L/DD ratio. Number of trades. Average trade. Profit Factor. Win/Loss ratio. E-Ratio.

Also: Monte Carlo bands, variance testing, and drawdown distribution but not deeper as I’d if the strategy was more polished.

The baseline passed some of these checks. Failed others.

Which meant one thing: the idea had potential. But it needed a better entry condition.

So I went back to Claude…


## Stop Asking AI to “Make It Better”


I went back to Claude with a specific ask.

Not “make this strategy better.”

That’s how you get bananas with AI.

Instead I asked something much more precise:

> “The Monday weakness effect in Copper has positive expectancy but poor risk-adjusted metrics. Suggest 3 simple entry filters based only on price action, no indicators that might improve the quality of the setups. For each one, give me the behavioral logic.”


“The Monday weakness effect in Copper has positive expectancy but poor risk-adjusted metrics. Suggest 3 simple entry filters based only on price action, no indicators that might improve the quality of the setups. For each one, give me the behavioral logic.”

But I also share a file with Claude that I think improved a lot the output and I’ll share this little detail with you in a moment.

But the thing is: Claude came back with a few ideas.

It was a single price-action condition. No indicator. No external data. Just one thing that had to be true about the market before I’d take the trade.

I added it to the baseline. Ran the backtest.

And this is what happened to the equity curve.

Same market. Same day-of-week logic. One extra condition.

That’s it.

Here’s what changed:

Profit Factor went from 1.29 to2.43.

Win rate went from 49% to65.79%.

Max drawdown dropped to just$9,577on a strategy that’s been running since 2007.

And in 19 years of trading? Only2 losing years.2009 and 2012.

Now we are talking…


#### But what was that one condition?


That’s exactly what I’m going to show you now along with the complete strategy code, the full Build Alpha validation, and a mistake I did in the process.

Before we dive…


#### If You’re Not an Annual Subscriber, Here’s What You’re Missing:


- Live portfolio access (starting March 1)— You’ll see exactly which strategies I’m running in a real account.

Live portfolio access (starting March 1)— You’ll see exactly which strategies I’m running in a real account.

- Full access to my Strategy App (270+ academic strategies)— A curated research library extracted from academic papers, rewritten in plain English so you can build from logic instead of guessing.

Full access to my Strategy App (270+ academic strategies)— A curated research library extracted from academic papers, rewritten in plain English so you can build from logic instead of guessing.

- The last 12 months of published strategies (+30 systematic trading strategies)— With complete rules and performance report.

The last 12 months of published strategies (+30 systematic trading strategies)— With complete rules and performance report.

- Early access to my AI research assistant (launching soon)— The same structured prompt engine I use to generate and refine trading ideas fast.

Early access to my AI research assistant (launching soon)— The same structured prompt engine I use to generate and refine trading ideas fast.

- The ability to request specific backtests— If there’s an idea you want pressure-tested, you can ask for it directly.

The ability to request specific backtests— If there’s an idea you want pressure-tested, you can ask for it directly.

- Big discounts on every product I launch— Starting with the upcomingZero to First Automated StrategyChallenge in March.

Big discounts on every product I launch— Starting with the upcomingZero to First Automated StrategyChallenge in March.

- Partner perks— Exclusive discounts on platforms, tools, and data feeds I actually use.

Partner perks— Exclusive discounts on platforms, tools, and data feeds I actually use.

- Direct access (via email) to me for 12 months— Research questions, strategy feedback, prompt reviews. Something I don’t offer anywhere else.I want this!

Direct access (via email) to me for 12 months— Research questions, strategy feedback, prompt reviews. Something I don’t offer anywhere else.

I want this!

Now you know what you've been leaving on the table.

Let's move on.


## The Complete Strategy (And The Mistake I Almost Missed)

