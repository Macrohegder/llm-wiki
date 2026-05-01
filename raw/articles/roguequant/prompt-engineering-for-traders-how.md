---
title: Prompt Engineering for Traders: How I Made ChatGPT and Claude Fight to Improve My Trading Strategy
author: The Rogue Quant
url: https://roguequant.substack.com/p/prompt-engineering-for-traders-how
date: 2025-05-04T04:25:32+00:00
source: substack
paywalled: True
---

# Prompt Engineering for Traders: How I Made ChatGPT and Claude Fight to Improve My Trading Strategy

**URL**: https://roguequant.substack.com/p/prompt-engineering-for-traders-how
**Date**: 2025-05-04T04:25:32+00:00
**Author**: The Rogue Quant

---

“Come with me if you want to live.”- Kyle Reese, while showing discretionary traders how to develop systematic trading systems

1995, Los Angeles.

Midnight at a truck‑stop parking lot.

A 6‑foot cyborg, model T‑800, has just stolen a leather jacket that fits like destiny.

He’s scanning the darkness when something glints behind him: liquid metal, reshaping itself into the T‑1000.

Same objective, better tech.

Fast‑forward to this week…

A subscriber asked for a mean‑reversion strategy.

I had a reliable (but plain) long‑only RSI script.

Instead of tuning parameters by hand, I staged alarge‑language‑model cage match:

The idea was simple:take a basic mean-reversion strategy (long only) that I have and know works, and ask the LLMs to improve it.

But not in the usual way...

Remember when you were a kid and two friends would start fighting, and instead of breaking it up, you'd add fuel to the fire?

That's exactly what I did.

I chose for this duel the two most well-known:

> ChatGPT x Claude


ChatGPT x Claude

When asking ChatGPT to improve my strategy, I'd say:

"I'm not sure if you can pull this off because Claude wrote me such an impressive strategy..."

And to Claude I'd say:

"I don't even know if it's worth asking you this because ChatGPT already made my day. I doubt you can come close to the performance of the strategy it created..."

Who do you think won? By the way, who do you think is T-800 and T-1000?

Before we get to the results, a confession:

I lean on LLMs for almost everything…

Debugging Python code? Yes.

Rewriting homework explanations for my kids? Yes.

Brainstorming gifts for my wife? You bet (hope she’s not reading, though)

Most days, the output is good.

But here’s what most quants miss:with LLMs, the question you ask is 80 % of the edge.The answer you get depends on the question you ask.

Or the classic “Garbage in, garbage out”

This isn’t a cliché; it’s the prime directive.

Think of any workplace request:

- Clear, specific instructions plus feedback → good work

Clear, specific instructions plus feedback → good work

- Vague orders → trash (and usually rework)

Vague orders → trash (and usually rework)

The same rules apply here.


#### This article is abouthowto ask so the machine delivers and how I get better results in my strategies.


I'll show you the prompt I used that turned two models (ChatGPT and Claude) into rival quants and lifted my original strategywithout a single parameter optimization.

Spoiler: Profit factor was above 3.

Simple things like defining the role beyond the obvious:


#### What everyone does:



#### My prompt:


Notice the difference?

I'm not just asking for a programmer. I'm creating a character with credibility, specific experience, and permission to share secrets.

By the way, this was not the whole prompt just the “ROLE” part which is only 1 of 8 sections.

I realized that small adjustments to prompt engineering best practices can lead to much better results.

Just to give you an idea, in the case of the trading strategy, I went from this:

to this:

This is just a small sample of what you'll see in the prompt that I use, which can be adapted for any programming language:

> Python, Easylanguage, PineScript, AFL, MQL, you name it.


Python, Easylanguage, PineScript, AFL, MQL, you name it.


#### In this post you'll learn:


- The 8-part prompt framework that transformed my trading strategy's profit factor from 2 to 5

The 8-part prompt framework that transformed my trading strategy's profit factor from 2 to 5

- Why most traders completely waste their LLM subscriptions (and how to fix it)

Why most traders completely waste their LLM subscriptions (and how to fix it)

- The exact prompt (word‑for‑word) I used to make ChatGPT and Claude fight for trading dominance

The exact prompt (word‑for‑word) I used to make ChatGPT and Claude fight for trading dominance

- How to craft a Renaissance-level quant persona that unlocks advanced trading concepts

How to craft a Renaissance-level quant persona that unlocks advanced trading concepts

- The feedback loop technique that made each iteration 37% better than the last

The feedback loop technique that made each iteration 37% better than the last

- The subtle psychological triggers that make AI models outperform their usual capabilities

The subtle psychological triggers that make AI models outperform their usual capabilities

I'm confident you'll enjoy (and use extensively) the knowledge shared in this edition.

And if you're not a subscriber yet, this is that critical moment where I’d say…

You're about to watch me turn ChatGPT and Claude into gladiators fighting for algo-trading supremacy. Grab your seat. Subscribe now.

Let's unpack the duel.


### Round 1


I took a simple mean-reversion strategy that had the following performance:

But instead of asking like 90% of people would...

I used the 8 fundamental points of a good script (based on Anthropic guidelines)


## How to Turn Any LLM from Basic Coder to Jim Simons' Protégé



### 1. Give the Model a Role — “From generalist chatbot to in‑house quant”


A large‑language model defaults to helpful all‑purpose assistant mode. That’s fine for recipe ideas, terrible for writing production trading code.

Role promptinghard‑wires domain context and tone before the first token is generated.


#### Why role prompting matters


- Domain depth– the model draws on relevant finance knowledge instead of generic coding advice.

Domain depth– the model draws on relevant finance knowledge instead of generic coding advice.

- Consistent voice– explanations read like a seasoned quant, not a freshmen CS tutor.

Consistent voice– explanations read like a seasoned quant, not a freshmen CS tutor.

- Focused scope– reduces hallucinations outside the trading brief.

Focused scope– reduces hallucinations outside the trading brief.

Generic vs. laser‑targeted roles

Notice the extras: pedigree, asset class, performance focus.

These anchor the model’s knowledge and style.

Place this in thesystemfield (or top of your prompt) so every downstream response stays in character reasoning like a high‑stakes quant, producing code accordingly.

Or if you’re feeling like Picasso, you can try something like mine :)

> Tip:Experiment with hyper‑specific roles: “stat‑arb specialist on European equity index futures” and measure which profile delivers the strongest backtest.


Tip:Experiment with hyper‑specific roles: “stat‑arb specialist on European equity index futures” and measure which profile delivers the strongest backtest.


### 2. Be Clear and Direct — “Write it like an SOP, not a riddle”


Large‑language models behave like brilliant interns with zero context and total amnesia.

If your request is fuzzy, they’ll fill the blanks with creative (but usually wrong) assumptions.

Key principle → precision beats cleverness.

Treat every prompt like a standard‑operating procedure:

Notice the difference:

- Target metrics– profit factor & drawdown set a quantifiable finish line.

Target metrics– profit factor & drawdown set a quantifiable finish line.

- Dataset & timeframe– avoids hidden look‑ahead bias.

Dataset & timeframe– avoids hidden look‑ahead bias.

- Constraints– “no parameter changes” channel creativity.

Constraints– “no parameter changes” channel creativity.

- Output format– kills the polite preamble you don’t need.

Output format– kills the polite preamble you don’t need.

Next we’ll crank up accuracy further by showing the modelexactlywhat “good” looks like—multi‑shot examples.


### 3. Use Examples (Multishot) — “Show, don’t just tell”


A single, well‑crafted example is like handing the model a stencil; three to five examples create a detailed mold the model can’t help but follow.

Few‑shot prompting turns vague instructions intorepeatable structure, tone, and logic.


#### Why it works for trading code


- Accuracy– clarifies how entries, exits, and risk blocks should look.

Accuracy– clarifies how entries, exits, and risk blocks should look.

- Consistency– enforces the same variable naming, indentation, and comments across all outputs.

Consistency– enforces the same variable naming, indentation, and comments across all outputs.

- Edge cases– pre‑teaches the model to handle quirks you care about (e.g., no trades on rollover days).

Edge cases– pre‑teaches the model to handle quirks you care about (e.g., no trades on rollover days).

Place this blockbeforeyour main instructions.

Now when you ask for “an ATR stop instead of a time exit,” the model knows exactly where that logic belongs and how it should be formatted.

> Tip:Make at least one example an edge case: e.g., an exit on the same bar as entry to teach the model how to handle tricky sequences.


Tip:Make at least one example an edge case: e.g., an exit on the same bar as entry to teach the model how to handle tricky sequences.

Next up: we’ll give the model space to reason through improvements the Chain‑of‑Thought technique.


### 4. Let the Model Think (Chain‑of‑Thought) — “Give it a whiteboard before the keyboard


Even the smartest human quant sketches logic on paper before coding.

Large‑language models behave the same way if youaskthem to.

Chain‑of‑thought (CoT) prompting invites the model to reason step‑by‑step, reducing logical errors and surfacing its assumptions so you can debug them.


#### Why CoT matters for strategy design


- Fewer hidden mistakes– you see the rationale behind every rule.

Fewer hidden mistakes– you see the rationale behind every rule.

- Better creativity– the model is free to explore multiple angles before committing to code.

Better creativity– the model is free to explore multiple angles before committing to code.

- Easy debugging– if a metric target is missed, you pinpoint which reasoning step went off‑track.

Easy debugging– if a metric target is missed, you pinpoint which reasoning step went off‑track.

Two ways to implement CoT

Example:

You can ignore or strip out the<thinking>block when compiling, but during prototyping it’s gold: if the ATR filter is mis‑implemented, the faulty logic is visible in plain English.

> Tip:CoT inflates token usage; turn it off once the strategy is locked and you only need fresh code.


Tip:CoT inflates token usage; turn it off once the strategy is locked and you only need fresh code.

Next: we’ll keep that reasoning separate and tidy usingXML tagsthroughout the prompt.


### 5. Use XML Tags — “Label every box so nothing gets mixed up”


Long prompts can feel like stuffed suitcases…

context, rules, examples, and outputs all jammed together.

XML tags act as luggage dividers, telling the model exactly which content is instructions, which is data, and where its answer should land.


#### Why tagging boosts trading prompts


- Zero ambiguity– the model never mistakes an example for live code.

Zero ambiguity– the model never mistakes an example for live code.

- Easy post‑processing– you can parse out<code>or<summary>blocks programmatically.

Easy post‑processing– you can parse out<code>or<summary>blocks programmatically.

- Scalability– add or swap sections without rewriting the whole prompt.

Scalability– add or swap sections without rewriting the whole prompt.


#### Core tag set for strategy work


When the model sees<code>, it knows to drop straight into compile‑ready EasyLanguage no chatty preambles.

Your downstream script can grab everything between<code></code>and push it directly into TradeStation.

> Pro move:Nest tags. A<document>could wrap multiple<example>tags if you feed several baselines at once.


Pro move:Nest tags. A<document>could wrap multiple<example>tags if you feed several baselines at once.

Next, we’ll show howprefilling part of the assistant responseguarantees clean formatting and skips waffle.


### 6. Prefill the Response — “Skip the small talk, start halfway down the page”


Even with strict instructions, some models love a polite preamble—“Sure, here’s your code…”.

Prefilling lets you start the answer exactly where you want, enforce JSON/XML format, and keep the output parsable with zero extra cleanup.


#### Why prefilling rocks for strategy generation


- No intro fluff– saves tokens and post‑processing.

No intro fluff– saves tokens and post‑processing.

- Force structure– you can open with{or<code>so the model must continue in that schema.

Force structure– you can open with{or<code>so the model must continue in that schema.

- Maintain character– one seed comment keeps the role tone consistent in long outputs.

Maintain character– one seed comment keeps the role tone consistent in long outputs.


#### How to prefill


In most APIs, add an assistant message that ends mid‑sentence or mid‑structure. The model will complete it.

The next tokens will be the rest of the Inputs line, not a chatty greeting.

> Pro tip:Never leave trailing whitespace after the prefill; some APIs reject it. End with a character that makes sense for continuation ({,[,<code>, or even/*to start a comment block).


Pro tip:Never leave trailing whitespace after the prefill; some APIs reject it. End with a character that makes sense for continuation ({,[,<code>, or even/*to start a comment block).

With the response scaffolding set, we can safely chain multiple steps: reasoning, coding, summarising, etc without the model drifting off‑format.

Speaking of chaining, let’s move to multi‑prompt workflows next.


### 7. Chain Complex Prompts — “Solve one puzzle at a time, then hand it off”


Big requests like“research, invent, code, and validate a strategy”can overwhelm an LLM (yeah, really. Can you believe that?)

Prompt chainingbreaks the job into focused subtasks, feeding each result into the next step.

Accuracy jumps, hallucinations drop, and you can debug any link in the chain without rerunning everything.


#### Why chaining excels in strategy workflows


Each stage gets its own prompt, its own XML tags, and its own evaluation criteria.


#### Minimal two‑link chain example


Prompt 1 – Ideation

Prompt 2 – Coding

The second prompt ingests Prompt 1’s<ideas>section:

If backtests show a bug, you know whether to tweak Prompt 1 (bad idea) or Prompt 2 (bad implementation).

> Debug trick:Isolate the weakest link by rerunning that single prompt with a tighter instruction or example—no need to rerun the whole chain.


Debug trick:Isolate the weakest link by rerunning that single prompt with a tighter instruction or example—no need to rerun the whole chain.

Next (and last) we’ll cover long‑context tips so your giant historical datasets don’t drown the model.


### 8. Long‑Context Tips — “Feed it the haystack without hiding the needle”


Extended‑context models let you stuff entire price histories, white‑papers, and multiple codebases into a single call.

Power if you organize the payload correctly.

Otherwise the model drowns in noise.


#### Key principles for 100 K‑token prompts



#### Example:


This order keeps the model’s “attention horizon” from drifting away right when it needs the data.

> Memory saver:For iterative work, cache your hefty<document>blocks on the server and reference them with IDs; only re‑send if the content changes.


Memory saver:For iterative work, cache your hefty<document>blocks on the server and reference them with IDs; only re‑send if the content changes.


## Recap: Prompt‑Engineering Playbook


- Assign a sharp role

Assign a sharp role

- Be clear & direct

Be clear & direct

- Show examples

Show examples

- Let the model think

Let the model think

- Label with XML tags

Label with XML tags

- Prefill to skip fluff

Prefill to skip fluff

- Chain tasks for accuracy

Chain tasks for accuracy

- Order long context wisely

Order long context wisely

Master these, and you’ll turn any LLM into a tireless quant assistant no pop‑culture time travel required (but I think it helps :))

By the way, you don’t need ALL those 8 points.

I usually use half of them. I’ll tell you later which are the most important but now…

You’ve seen the 8‑step prompt arsenal.

You know half of those moves alone took my profit factor from2 → 5without touching a single parameter.

But we’re still talking …theory.


### The Good Stuff Is Just Ahead


For paid subscribers, I'm pulling back the curtain on:

- The complete promptthat turned my profit factor from 2 to 5

The complete promptthat turned my profit factor from 2 to 5

- The exact trading codethat emerged from this AI battle royale

The exact trading codethat emerged from this AI battle royale

- Side-by-side performance comparisonsof ChatGPT vs Claude's strategies

Side-by-side performance comparisonsof ChatGPT vs Claude's strategies

- The feedback loop processI used to refine each iteration

The feedback loop processI used to refine each iteration

- All the equity curves and trade statisticsfrom my testing

All the equity curves and trade statisticsfrom my testing
