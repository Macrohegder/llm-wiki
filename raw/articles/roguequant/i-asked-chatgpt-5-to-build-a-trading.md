---
title: I Asked ChatGPT-5 to Build a Trading Strategy From Scratch. Here's What Happened.
author: The Rogue Quant
url: https://roguequant.substack.com/p/i-asked-chatgpt-5-to-build-a-trading
date: 2025-08-17T22:12:40+00:00
source: substack
paywalled: True
---

# I Asked ChatGPT-5 to Build a Trading Strategy From Scratch. Here's What Happened.

**URL**: https://roguequant.substack.com/p/i-asked-chatgpt-5-to-build-a-trading
**Date**: 2025-08-17T22:12:40+00:00
**Author**: The Rogue Quant

---

“Have you tested GPT-5 yet?Is it any good for creating trading strategies?”

Last week, 4 different people asked me the same question.

And if you've been following me for a while, you know I use LLMs in some pretty weird ways when it comes to trading.

But this latest model from OpenAI has been getting mixed reviews...

I went to bed thinking about it.

Is GPT-5 really that much better than GPT-4o for trading?

Sunday morning. Kids getting ready to go play soccer. Me in my pajamas withcoffeetea…

And I had this random thought:

"Do I have time to ask GPT-5 to spin up a strategy before the kids are ready?”

So I typed a simple prompt into ChatGPT-5…

And to be honest, I wasn’t expecting much…

The output came back in like 5 seconds:

Three rules. Clean. Simple. (Almost) Predictable.

But now I was curious...

Could this basic setup actually work?

Here's what I'll cover in this post:

1. The Prompt Strategy2. The Code GPT-5 Actually Created3. The Shocking (not shocking) Results (and the one tweak that changed everything)

This Substack is powered bybacktests, forward tests, LLMs, and people like you. Subscribe if you likedata-driven strategy buildingwithout the guru nonsense. Free is cool.Paid is cooler.


## The Prompt Strategy (and Why I Kept It Stupid Simple)


Look, I could have cheated.

I could have given it hints about what works in gold.

I could have mentioned volume patterns, volatility clusters, correlation plays...

I could have dropped breadcrumbs about liquidity windows...

But I didn't.

The whole point was to test GPT-5raw.

No human bias.

No "helping" the AI.

Here's exactly what I sent:

> "You are my quant trader coach and mentor.I want you to build a trading strategy (in easylanguage) from scratch to trade Gold Futures. Assume I trade only one contract (don't need to write this in the code).I want to backtest on daily bars. It's a MUST to use only 3 rules.I like simple and clean systems. It must be profitable and with 3+ Profit Factor.Anything else you can choose whatever you want to build a robust trading strategy.Now go ahead and give me the code."


"You are my quant trader coach and mentor.

I want you to build a trading strategy (in easylanguage) from scratch to trade Gold Futures. Assume I trade only one contract (don't need to write this in the code).

I want to backtest on daily bars. It's a MUST to use only 3 rules.

I like simple and clean systems. It must be profitable and with 3+ Profit Factor.

Anything else you can choose whatever you want to build a robust trading strategy.

Now go ahead and give me the code."

Notice what I DID specify:

- Only 3 rules (simple systems are more robust)

Only 3 rules (simple systems are more robust)

- Profit Factor above 3 (quality threshold)

Profit Factor above 3 (quality threshold)

- Gold Futures on daily bars (daily bars are easier to create strategies)

Gold Futures on daily bars (daily bars are easier to create strategies)

- EasyLanguage (so I could actually test it fast)

EasyLanguage (so I could actually test it fast)

What I deliberately DIDN'T mention:

- No regime filters

No regime filters

- No mean reversion hints

No mean reversion hints

- No specific indicators

No specific indicators

- Zero directional bias

Zero directional bias

This was a clean test.

GPT-5 had to "invent" everything from scratch.


## The Code GPT-5 Actually Created


GPT-5 had basically created a pullback system that:

- Only trades with the major trend

Only trades with the major trend

- Buys when price gets "oversold" during an uptrend

Buys when price gets "oversold" during an uptrend

- Exits when momentum shifts back up

Exits when momentum shifts back up

GPT-5 wrote actual, compilable EasyLanguage code.

Not pseudocode. Not "here's the concept."

Real codewith proper syntax, variables, and logic flow that I could literally copy-paste into TradeStation.

(I'll share the complete code in a moment)

The big question remained:

> Would this thing actually make money?


Would this thing actually make money?

Time to find out...


## The Results Were... Disappointing (At First)


I loaded the code into TradeStation.

Set it to run on Gold Futures from 2007 to 2025.

Hit "run backtest."

Initial Results:

- Net Profit: $29,430

Net Profit: $29,430

- Profit Factor: 1.55

Profit Factor: 1.55

- Win Rate: 64.81%

Win Rate: 64.81%

- Total Trades: 54

Total Trades: 54

Profitable? Yes.

Profit Factor above 3 like I asked?Nope.

GPT-5 had failed my main criteria.

But something caught my eye...

The equity curve could be improved. The problem wasn't the entry logic.

The problem was the exit.

Looking at the trade-by-trade breakdown, I saw what was happening:

- Great entry timing ✓

Great entry timing ✓

- Winning trades were being cut too short ✗

Winning trades were being cut too short ✗

- The system was leaving money on the table

The system was leaving money on the table

Then I had a thought…

What if I just... held the winners a bit longer?

One tiny tweak. Changed a single number.

The results after that one change:

- Net Profit:$95,780(tripled!)

Net Profit:$95,780(tripled!)

- Profit Factor:4.21(crushed the target!)

Profit Factor:4.21(crushed the target!)

- Win Rate:78.85%(even better!)

Win Rate:78.85%(even better!)

Wait... WHAT?!

One number change took this from "meh" to "wow"?

Next question…


## "But Wait... That's Obviously Overfitting, Right?"


This was exactly my first thought.

How does one tiny parameter change triple the profits?

Sounds like classic curve-fitting bullsh*t.

But then I dug deeper...

I ran an optimization on just the exit parameter...

And guess what?

The original parameter that GPT-5 had given me was thesecond worstout of 50!

The chart above shows the exit optimization from 1 to 50.

Parameter 5 (GPT-5's original choice) was the second-worst performer, even though it was still positive.

The thing is: the change made logical sense

The original exit was cutting profits too early.

Holding longer lets you capture more of the reversal.

Some extra data about the optimization:

The win rate actually IMPROVED

- Original: 64.81%

Original: 64.81%

- Optimized: 78.85%

Optimized: 78.85%

Only 3 losing years out of 18.

But here's what really convinced me this was legit:

I ran a walk-forward test and the results held up consistently.

Ok, enough.

Let’s get into the exact 3-rule Gold system…The exit tweak that pushed PF from 1.55 → 4.21…And the full code so you can rerun the test yourself.
