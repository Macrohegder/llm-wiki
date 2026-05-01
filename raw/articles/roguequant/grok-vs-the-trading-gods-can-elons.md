---
title: Grok vs The Trading Gods: Can Elon's AI Actually Improve a Working Strategy?
author: The Rogue Quant
url: https://roguequant.substack.com/p/grok-vs-the-trading-gods-can-elons
date: 2025-09-13T05:29:39+00:00
source: substack
paywalled: True
---

# Grok vs The Trading Gods: Can Elon's AI Actually Improve a Working Strategy?

**URL**: https://roguequant.substack.com/p/grok-vs-the-trading-gods-can-elons
**Date**: 2025-09-13T05:29:39+00:00
**Author**: The Rogue Quant

---

A subscriber recently asked me a simple question:

> “Which LLM do you use for trading strategies?”


“Which LLM do you use for trading strategies?”

He mentioned he’d been experimenting with Grok and getting “surprisingly good” answers.

Now, I subscribe to all the usual suspects…

ChatGPT, Claude, Gemini and yes, I also keep Grok in the mix.

But I usually don’t use any of them to build strategies from scratch (not convinced if there is alpha…)

Where these models shine is in the gray areas:

> Brainstorming ideas, cleaning up messy logic, or spotting variations you hadn’t considered.


Brainstorming ideas, cleaning up messy logic, or spotting variations you hadn’t considered.

So I decided to run a test.

Not to create alpha from scratch, but to see ifGrokcouldimprovean existing strategy.

In this edition, we’ll look at:• Theoriginal strategy• Grok’s “improved” version• The exact prompt I used and whether it was worth it

Let’s dive in.


## The Original Strategy


Before handing anything to Grok, I started with a simple baseline strategy.

I borrowed the core idea (and changed it a little) fromGeorge Pruitt’sexcellent bookEasing Into EasyLanguage.

In fact,Easing Into EasyLanguageis a five–book series, and I strongly recommend it. Below is the first of the series…

In short, the strategy is built on two ingredients:

- Keltner Channels— a volatility-based envelope around price.

Keltner Channels— a volatility-based envelope around price.

- ADX filter— only taking trades when the market isn’t showing strong trend.

ADX filter— only taking trades when the market isn’t showing strong trend.

In plain English:

- Buy when price dips below the lower Keltner band and volatility is quiet

Buy when price dips below the lower Keltner band and volatility is quiet

- Exit when price reverts back to the moving average.

Exit when price reverts back to the moving average.

That’s it. Nothing fancy.

And yet, over the full test period, this little system produced:

- Net Profit:≈ $115,000

Net Profit:≈ $115,000

- Profit Factor:2.0

Profit Factor:2.0

- Total Trades:82

Total Trades:82

- Avg Net Profit:$1,405

Avg Net Profit:$1,405

- Win/Loss Ratio:$2.68

Win/Loss Ratio:$2.68

Not bad for a handful of lines of code.

Take a look at the equity curve:

But here’s where things get interesting…


#### What happens when you ask Grok toimproveit?


This Substack is powered bybacktests, forward tests, LLMs, and people like you. Subscribe if you likedata-driven strategy buildingwithout the guru nonsense. Free is cool.Paid is cooler.


## The Grok Experiment


I didn’t ask Grok to create a brand-new trading system.

That’s not the point.

I wanted to see if it couldimprovethe baseline strategy I just showed you.

So I ran a prompt (I’ll show you later) and I gave it one job:

Keep the core idea and look forsmall, testable upgradesaround entries, exits, filters and risk.

What it changed…

- Entry:from buying dips tobuying strength

Entry:from buying dips tobuying strength

- Risk:addATR-based stopandATR-based target

Risk:addATR-based stopandATR-based target

- Exit:add amidline bailwhen momentum fades.yes, small changes…

Exit:add amidline bailwhen momentum fades.

Why this makes sense…

Let the marketproveitself (breakout), size risk tocurrent volatility, and step off when the push stalls.

The real question:

> Did it actually perform better?


Did it actually perform better?

Take a look at the results.


## The Results


Now let’s put both systems side by side.

That’s not a rounding error,net profit jumped by roughly 64%after Grok rewired the entries/exits and added volatility-aware risk.

And Grok produced MORE trades!

Both systems ran on thesame market and period; the only missing piece was…

> Grok


Grok

Which leads to the real question:what exactly did Grok change, and why did it matter?

That’s where things start to get really interesting…


### But Wait—Isn’t This Just Overfitting?


If you’re skeptical right now, you should be.

A single backtest that magically turns $115k into $188k looks suspicious.

Is Grok just throwing complexity at the wall and overfitting the past?

That’s the right question to ask.

Because in trading, every “improvement” carries a hidden cost…

Whether it’s reduced robustness, more exposure, or drawdowns that look tame on paper but feel brutal in real life.

And that’s exactly why I ran this experiment: not to crown Grok as the new quant genius, but to see if an LLM could deliverpracticalimprovements without crossing into curve-fit fantasy land.

So let’s pull back the curtain onwhat Grok actually changedand whether those tweaks pass the smell test… or not!

But first, let me show youpart 1of the prompt I used:

So this wasPart 1of the prompt I used.

It did the job, Grok analyzed the idea and suggested changes but the answers came backtoo verboseandneedlessly complex.

Lots of moving parts.

I don’t like moving parts, so I ran a second pass with a simplicity override: keep the spirit, cut the noise, cap the knobs…

With that constraint set,things improved…

The code got leaner, the logic was easier to reason about, and the performance improved but…

There’s always abut.

And I’ll reveal the ‘but’, then walk you through bothcomplete code versions, side by side.

By the way, if you’re not a paid member yet, this is a good moment to join the crew

Paid membersget:

- A new backtested strategy every week(with code you can run).

A new backtested strategy every week(with code you can run).

- Access to my strategy database (now an app) with100+ academic-paper ideas, already translated intoplain English logic… so you can test an idea without wading through math-heavy PDFs (for annual subscribers only).

Access to my strategy database (now an app) with100+ academic-paper ideas, already translated intoplain English logic… so you can test an idea without wading through math-heavy PDFs (for annual subscribers only).

Click the button below to become a paid subscriber.


## The BigBut…

