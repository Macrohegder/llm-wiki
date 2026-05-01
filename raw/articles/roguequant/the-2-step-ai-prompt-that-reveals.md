---
title: The 2-Step AI Prompt That Reveals Hidden Edges in Any Trading Dataset
author: The Rogue Quant
url: https://roguequant.substack.com/p/the-2-step-ai-prompt-that-reveals
date: 2025-06-25T02:26:52+00:00
source: substack
paywalled: True
---

# The 2-Step AI Prompt That Reveals Hidden Edges in Any Trading Dataset

**URL**: https://roguequant.substack.com/p/the-2-step-ai-prompt-that-reveals
**Date**: 2025-06-25T02:26:52+00:00
**Author**: The Rogue Quant

---

I spent years working as a data scientist (back when AI still felt like science fiction)

And one of the first things you learn is this:

> ❝Before you model anything, explore the data.❞


❝Before you model anything, explore the data.❞

> explore the data first, they told him…


Exploratory Data Analysis (EDA) is the first step when working with large datasets.

I like IBM’s definition:

“EDA helps determine how best to manipulate data sources to get the answers you need, making it easier for data scientists to discover patterns, spot anomalies, test a hypothesis, or check assumptions.”

Which, in plain English, means:

> →understand the personality of your dataset before you touch any models.


→understand the personality of your dataset before you touch any models.

That’s like training a machine learning model onimages of cats and dogs, and then trying to use it to classifymedical X-rays.

The inputs might look similar (they’re all images) but the structure, patterns, and what matters are completely different.

Same with trading.

Look again at IBM’s definition, it’s easy to miss how powerful it really is:

“discoverpatterns, spotanomalies, test ahypothesis, or checkassumptions.”

This Substack is powered bybacktests, forward tests, LLMs, and people like you. Subscribe if you likedata-driven strategy buildingwithout the guru nonsense. Free is cool.Paid is cooler.


## Why Most Trading Strategies Collapse in Live Markets


Let me give you an example so you can see the importance of EDA.

You're analyzing Gold Futures and discover that the average daily range over the past 6 months is about 20 points.

That tells you something:

- Maybe your profit target should live inside that range

Maybe your profit target should live inside that range

- Maybe you should only enter on high-range breakouts

Maybe you should only enter on high-range breakouts

- Maybe you're trading a quieter market than you thought

Maybe you're trading a quieter market than you thought

The "shape" of the data matters.

Ignore it, and your strategy will probably fail no matter how elegant the code.


## What’s the Problem?


Most traders rush to build strategies without understanding thepersonalityof the asset they’re trading.

They test entry/exit rules.They optimize parameters.They run backtests for weeks......on a dataset they barely know.

That’s like trying to win a chess match without knowing the rules of the pieces.


## Why Understanding Your Data Changes Everything


If you don’t understand the market’s structure:

- You overfit to noise

You overfit to noise

- You chase patterns that don't repeat

You chase patterns that don't repeat

- Your backtests collapse in live trading

Your backtests collapse in live trading

But when youdounderstand the market?

- You can anticipate regime shifts.

You can anticipate regime shifts.

- You build strategies that align with actual behavior.

You build strategies that align with actual behavior.

- You trust your system because it reflects the truth of the data.

You trust your system because it reflects the truth of the data.


## The Solution: A Prompt That Thinks Like a Senior Data Scientist


That's why I built a specific prompt.

A single, reusable prompt that turns any LLM into a senior exploratory data scientist.

It doesn't just spit numbers…

It makes connections. It finds tension. It asks better questions than most humans I know.

It's a 2-step process:

Step 1:It reviews your dataset and proposes 20+ ideas worth exploring. Each idea comes with a reason why it matters for finding an edge.

Step 2:You choose which ones to pursue (or ask for more). Only then does the AI dig in and analyze.


## What the AI Found in 18 Years of Gold Data


I’ll show you an example.

I wanted to test this on Gold Futures.

So I uploaded daily data (in a CSV file with OHLCV format) from 2007 to 2025 and ran the prompt.

First, it gave me 25 smart, data-driven metrics to choose from:

But I didn’t like some of the first 20 so I asked to 20 more not so obvious ideas and got this…

Then I picked a few and ran the second part of the prompt…

The AI did the analysis.

And here’s what came back:

For example, you now know Gold’saverage annual volatilityis12.52%, and on most days, Gold moves15–20 points. But in volatile clusters, that can expand to40–50 points… fast.

If you’re building a short-term strategy (say, a 5-day swing trade), this tells you exactly how tight yourprofit targetshould be…

…and how far yourstopcan go without being nonsense.

Or takeseasonality.

Gold inJanuaryaverages a+16.53% annualized returnwith a68.4% win rate.

That doesn’t mean January is magic.

But it does mean one thing loud and clear:

If you’re going to take risk, December and January are better bets than June and September.

Same goes forFridays.

On average, Friday trades have historically delivered7.76% annualized returnsslightly stronger than any other day of the week.

So if your system triggers on a ThursdayorFriday?

All else equal… choose Friday.


## “But AI Doesn't Understand Markets…”


I hear this objection constantly.

And yeah, it'skindaright.

AI doesn't "understand" markets like a pro trader.

It doesn't feel fear when it sees -5%.

It doesn't have intuition about geopolitics (well, sometimes it does…)

But it does something better:

> it analyzes data without emotional bias.


it analyzes data without emotional bias.

When you see a -6% drop in gold, your reptilian brain screamsSELL!

The AI looks at 18 years of data and responds coldly:

"Historically, drops like this reverse 72% of the time within 5 days."

It's not about AI "understanding" markets.

It’s aboutremoving noise, bias, and emotionand letting the data speak.


## What These Numbers Mean for Your Trading


These aren't trivia facts.

Each insight can directly influence:

- Entry timing:Friday setups vs Tuesday setups

Entry timing:Friday setups vs Tuesday setups

- Stop placement:ATR-based vs percentage-based

Stop placement:ATR-based vs percentage-based

- Target setting:Inside the average range vs breakout expectations

Target setting:Inside the average range vs breakout expectations

- Position sizing:January vs May allocation

Position sizing:January vs May allocation

- Risk management:Volatility regime filtering

Risk management:Volatility regime filtering

The goal is to build strategies aligned with how the asset behaves, not how you wish it behaved.


## How This Changes Strategy Development


Instead of:

- Having an idea

Having an idea

- Testing it on any data

Testing it on any data

- Optimizing until it works

Optimizing until it works

Do this:

- Understand the data first

Understand the data first

- Find natural patterns and edges

Find natural patterns and edges

- Build strategies around proven behaviors

Build strategies around proven behaviors

- Test robustness across different regimes

Test robustness across different regimes


## The Universal Application


And the best part is that you can run this same prompt on any asset:

> Crude, ES, BTC, individual equities, ETFs, forex pairs...



#### Crude, ES, BTC, individual equities, ETFs, forex pairs...


Even using free data from Yahoo Finance (though I always recommend high-quality data when possible).

It's like having a senior data scientist on your team who never gets tired, never has bad days, and works for the cost of an API call.

Now let’s dive into the prompt itself…


## The Complete 2-Step Exploratory Data Analysis Trading Prompt

