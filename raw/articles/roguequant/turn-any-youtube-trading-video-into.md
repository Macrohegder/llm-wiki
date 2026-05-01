---
title: Turn Any YouTube Trading Video Into a Backtestable System (With 2 AI Prompts)
author: The Rogue Quant
url: https://roguequant.substack.com/p/turn-any-youtube-trading-video-into
date: 2025-06-13T19:34:47+00:00
source: substack
paywalled: True
---

# Turn Any YouTube Trading Video Into a Backtestable System (With 2 AI Prompts)

**URL**: https://roguequant.substack.com/p/turn-any-youtube-trading-video-into
**Date**: 2025-06-13T19:34:47+00:00
**Author**: The Rogue Quant

---

YouTube is flooded with trading ideas.

But like any flood…

99% of what’s floating isn’t gold…

It’s garbage.

Yet sometimes, buried inside these rambling videos, there are surprisingly solid ideas.

The problem?Time.

If you're like me (kids, family and a life to live :)), you don’t have hours to watch 40-minute videos hoping to catch the 3 minutes where the speaker finally drops actual trading logic.

Most videos go like this:

> "I made 1,130% last month using this setup..."[20 minutes of lifestyle montage]"...you just wait for the signal and enter. Simple."


"I made 1,130% last month using this setup..."[20 minutes of lifestyle montage]"...you just wait for the signal and enter. Simple."

No parameters. No definitions. No risk management.

Despite the great hooks like this…

or this

or this

It’s trading content for views not for traders.

But let’s be clear:

Not everything is useless.

Some creators do share real frameworks and solid ideas.

Not to copy and paste and think you have a ready-to-trade strategy…

But to mine for components you can adapt, combine, and build into your own research.


## The Real Problem: Information Density


In most videos, you’re dealing with:

- 45 minutes of stories

45 minutes of stories

- Vague "rules of thumb"

Vague "rules of thumb"

- Random market philosophy

Random market philosophy

- About 2 minutes of actual rules

About 2 minutes of actual rules

You end up:

- Pausing, rewinding, rewatching

Pausing, rewinding, rewatching

- Taking messy notes that won't make sense tomorrow

Taking messy notes that won't make sense tomorrow

- Still not having a fully testable strategy

Still not having a fully testable strategy

This doesn’t scale.

You can’t build a serious research process like this.

If you want to build a serious idea bank, you need to process dozens of strategies — fast.

At 2 hours per video?You’re spending your whole life watching gurus talk.

Now imagine:

• Processing ANY YouTube trading video in seconds• Getting fully structured, backtest-ready trading rules• Immediately knowing if the video contains a real strategy or pure clickbait

That's exactly what I built.

And today, I’ll show you exactly how it works.


## The 2-Prompt Extraction Engine


The system works in two surgical stages:


### Prompt 1: Extract Trading Logic


You feed the YouTube transcript into Prompt 1.

The AI then:

- Filters out stories, fluff, and filler

Filters out stories, fluff, and filler

- Ignores motivational speeches

Ignores motivational speeches

- Extracts only actionable trading logic

Extracts only actionable trading logic

- Breaks out entry, exit, stop loss, risk rules, and market context

Breaks out entry, exit, stop loss, risk rules, and market context

The Extraction Process:

You start with this…

"Intro0:00 hey traders in this video you'll learn0:02 the simplest day trading strategy for0:04 beginners you literally don't need any0:06 experience to be profitable and it's the0:09 strategy I wish I would have known when0:10 I first started out because it uses0:13 Concepts that professional Traders use0:15 but simplified so much that anyone can}0:17 do it and just because the strategy is0:19 simple doesn't mean it's not profitable0:21 as I've also did a back test of it and0:23 it came out with a staggering 65% win0:26 rate which is pretty good for just a0:28 simple strategy so let's get started the The Strategy0:31 strategy is so simple we only look at…”

And on and on for 20 minutes.

And end up with this…

You now have fully testable rules without burning dozens of hours on YouTube.

But then you probably want to test it, right?

So next, you take that extraction and feed it into Prompt 2.

The AI converts it into clean, platform-independent pseudocode:

- No programming language required

No programming language required

- Fully structured IF/THEN logic

Fully structured IF/THEN logic

- Platform-agnostic (Python, PineScript, EasyLanguage, etc.)

Platform-agnostic (Python, PineScript, EasyLanguage, etc.)

So here’s it comes the second prompt…


### Prompt 2: Convert to Pseudocode


With the extracted logic, you run Prompt 2.

It structures the rules into implementation-ready pseudocode:

This is now ready to be coded in EasyLanguage, PineScript, Python, or handed to any developer.


## Why Two Prompts Work (And Why One Doesn’t)


Most people try:

> "Hey ChatGPT, extract the strategy from this transcript and give me code."


"Hey ChatGPT, extract the strategy from this transcript and give me code."

That fails because you’re asking AI to dotwo very different jobs at once:

- Linguistic extraction

Linguistic extraction

- Logical structuring

Logical structuring

When you separate the two tasks,each prompt can specialize → and produce MUCH better output.

I tested both approaches on 50+ real videos.

The two-stage approach consistently produces cleaner, more accurate results than trying to do everything in one shot.


## The Hidden Problems You Need to Know


Even with good prompts, here’s where most people fail (and where I failed early on):


### 1. Corrupted Transcripts


YouTube auto-transcripts destroy trading terminology:

- "RSI" → "our aside"

"RSI" → "our aside"

- "Bollinger Bands" → "bowling your bands"

"Bollinger Bands" → "bowling your bands"

- "MACD" → "mack dee"

"MACD" → "mack dee"

- "Fibonacci" → "fiber notchy"

"Fibonacci" → "fiber notchy"

- "Stop loss" → "stop lost"

"Stop loss" → "stop lost"

The AI will extract complete nonsense unless you handle this.

My Solution:

- I added trading terminology correction directly into Prompt 1.

I added trading terminology correction directly into Prompt 1.

- The AI learns how to interpret noisy transcripts logically.

The AI learns how to interpret noisy transcripts logically.

- If it finds unclear chart references, it flags timestamps for screenshots.

If it finds unclear chart references, it flags timestamps for screenshots.


### 2. AI Hallucinations


AI loves to invent non-existent rules:

- Hyper-precise numbers: "RSI exactly 23.7"

Hyper-precise numbers: "RSI exactly 23.7"

- Multi-step processes pulled from thin air

Multi-step processes pulled from thin air

- Risk rules that were never discussed

Risk rules that were never discussed

- Extra indicators magically appearing

Extra indicators magically appearing

My Solution:

Built strict anti-hallucination protocols directly into the prompt:

> "Extract ONLY what is explicitly stated.If information is missing, write: ‘REQUIRES_SPECIFICATION’."


"Extract ONLY what is explicitly stated.If information is missing, write: ‘REQUIRES_SPECIFICATION’."


### 3. Incomplete Strategies


Roughly 70% of YouTube "strategies" aren’t actually strategies.

They’re entertainment disguised as education.

Red flags:

- No entry definitions

No entry definitions

- No exit rules

No exit rules

- No risk parameters

No risk parameters

- “Works in all markets & timeframes” nonsense

“Works in all markets & timeframes” nonsense

My solution:

The prompt immediately shows you whether there's even a strategy worth testing or if you should skip the video entirely.

It's saved me countless hours on videos that sound promising but contain zero actionable content.


## The Compound Effect


This isn’t just about saving time.

It compounds your edge:

- You learn faster

You learn faster

- You test 5x more ideas per week

You test 5x more ideas per week

- You refine your system-building skills

You refine your system-building skills

- You build your personal research database

You build your personal research database

And in systematic trading,volume matters.

The more ideas you process →The more valid setups you discover →The faster you build true edge.


## The Prompts That Run My Extraction Engine


You've now seen the full system at work.

But building these prompts took months of iteration:

- 50+ real YouTube videos processed

50+ real YouTube videos processed

- Dozens of failed tests

Dozens of failed tests

- Multiple rounds of refining edge cases

Multiple rounds of refining edge cases

These aren’t "off-the-shelf" prompts.

They’re designed specifically forYouTube transcript messiness.

I’m sharing both full prompts below:

• The Trading Logic Extraction Prompt• The Pseudocode Conversion Prompt

Enjoy…
