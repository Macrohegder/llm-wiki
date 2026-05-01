---
title: Can LLMs Really Build Robust Trading Strategies? I Put Gemini and Claude to the Test.
author: The Rogue Quant
url: https://roguequant.substack.com/p/can-llms-really-build-robust-trading
date: 2025-07-23T18:58:07+00:00
source: substack
paywalled: True
---

# Can LLMs Really Build Robust Trading Strategies? I Put Gemini and Claude to the Test.

**URL**: https://roguequant.substack.com/p/can-llms-really-build-robust-trading
**Date**: 2025-07-23T18:58:07+00:00
**Author**: The Rogue Quant

---

These questions hit my inbox constantly:

ChatGPT or Claude?

Gemini or DeepSeek?

Can any of these LLMs actually create robust strategies?

Which one delivers the best results?

So I decided to test an idea you can replicate yourself.

In fact, I encourage you to try it the results might surprise you.


## The Idea


Every week, I publish a trading idea I've backtested with historical data and share the code so you can modify, improve, and discuss it in our community chat.

This week's concept was beautifully simple:

> Buy when: volatility spike + price at bottomSell when: price recovers


Buy when: volatility spike + price at bottomSell when: price recovers

I took this basic idea to Gemini 2.5 Pro to see what it could create.

The prompt I used (which you'll find at the end of this article) was based on a model I've shared in this previous article below:


#### I Built a Prompt That Extracts Trading Strategies from Academic Papers — and Found the Best AI Tool for the Job



### What Gemini Delivered (And Why It Failed)


The initial results looked promising on the surface:

- Win ratio: 73%

Win ratio: 73%

- But only 49 trades over 18 years

But only 49 trades over 18 years

- Average win/loss ratio: a measly 0.43

Average win/loss ratio: a measly 0.43

And the equity curve…

The equity curve told the real story:not tradable.

Here's what most traders get wrong:

They expect a single conversation with an LLM to produce a working strategy.

That's like expecting to find gold on your first swing of the pickaxe.

This Substack is powered by backtests, forward tests, LLMs, and people like you. Subscribe if you like data-driven strategy building without the guru nonsense. Free is cool.Paid is cooler.


### The Hidden Gem Approach


What you need instead is a conversation. A debate.

You need to:

- Challenge the LLM's assumptions

Challenge the LLM's assumptions

- Point out obvious flaws

Point out obvious flaws

- Ask for alternatives

Ask for alternatives

- Keep pushing back

Keep pushing back

That back-and-forth dialogue is where the hidden gems emerge.

So I shared the disappointing equity curve with Gemini, highlighted the problems, and specifically questioned the tiny number of trades across 18 years.

Gemini's response was brilliant in its simplicity: change just one parameter in one variable.

Instead of using factor 2 as the trigger, use factor 1.

That single adjustment transformed everything.

The new results were wild:

- Dramatically improved equity curve

Dramatically improved equity curve

- No optimization whatsoever

No optimization whatsoever

- Clear potential for further development

Clear potential for further development

And here’s the equity curve…

I want to emphasize:

This wasn't curve-fitting or over-optimization.

One parameter change in one variable revealed something worth pursuing.

And how do you improve a trading strategy without overfitting?

That’s exactly what I’m going to show you next…


## The Improvement


Here's where I see LLM enthusiasts go completely wrong.

They ask the same AI to "improve the strategy," and it returns the original idea buried under 7 new filters and 5 optimization suggestions.

You know what happens next…

A hopelessly overfitted system.

So instead of continuing with Gemini, I used a technique I've shared in the article below:


#### Research Is Just the Start: How I Turn Ideas Into Strategies


I asked Claude Opus 4 to review Gemini's strategy and propose improvements.

Long story short…

Claude's refinements (before any optimizations) delivered:

As you can see:

- Profit Factor jumped from 1.85 to 2.31

Profit Factor jumped from 1.85 to 2.31

- Win rate remained stable

Win rate remained stable

- Average trade net profit increased from $1,001 to $1,381

Average trade net profit increased from $1,001 to $1,381

- Average win/loss ratio improved from 0.71 to 0.91I told you it might cause surprise…

Average win/loss ratio improved from 0.71 to 0.91

So yes, you can create strategies using LLMs. But not the lazy way.

Not with prompts like "create me a robust strategy that makes money."

Instead, treat it like collaborating with another trader:

- Question assumptions

Question assumptions

- Point out errors

Point out errors

- Ask for feedback

Ask for feedback

- Work as a team

Work as a team


## What’s Next?


You might be thinking,

"this sounds too good to be true. How do you know this strategy will actually work in live trading?"

You're absolutely right to be skeptical.

I haven't run comprehensive robustness tests yet…

Only a basic parameter stabilization analysis during optimization.

This involves checking whether changing a moving average from 50 to 49 drastically alters results or keeps them relatively stable.

The strategy passed this preliminary test, but there's substantial work ahead:walk-forward analysis, Monte Carlo simulations, variance testing, and more.

This isn't a finished product, it's a promising foundation that demonstrates the potential of collaborative AI development.


## What This Means for Your Trading


The real lesson isn't about which LLM is "best."

It's about approach.

Most traders treat AI like a magic wand: ask once, get disappointed, give up.

The successful approach treats AI like a knowledgeable colleague who needs guidance, pushes back on bad ideas, and improves through iteration.

This dynamic of conversing between different AIs has been the most effective method I've found for developing solid trading ideas with real trading potential.


## The Code Behind the Results


Since you're probably curious about the actual implementations…

I'll share both versions:

The original Gemini code and Claude's improved version, plus the exact prompt I used for Claude's review.
