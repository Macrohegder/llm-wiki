---
title: Can You Actually Trade Classic Technical Indicators on Bitcoin?
author: The Rogue Quant
url: https://roguequant.substack.com/p/can-you-actually-trade-classic-technical
date: 2025-06-02T03:41:33+00:00
source: substack
paywalled: True
---

# Can You Actually Trade Classic Technical Indicators on Bitcoin?

**URL**: https://roguequant.substack.com/p/can-you-actually-trade-classic-technical
**Date**: 2025-06-02T03:41:33+00:00
**Author**: The Rogue Quant

---

“How do you come up with ideas to test?”

That’s one of the questions I get the most from subscribers.

So today, I’m going to walk you through a simplified version of my process, one you can start using right after reading this post.


### Where do the ideas come from?


I’ve said this before, but it’s worth repeating…

I read a lot of academic papers.

And the reason is simple:

> They’re an endless source of trading ideas.



#### They’re an endless source of trading ideas.


Not necessarily to copy the exact rules…

but to explore variations, remix concepts, and pressure-test assumptions.

Right now, I have a database of 400+ papers that I review regularly when I want to get “inspired”.

btw,annual subscribers get full access to that database, which I turned into a searchable app.

Inside, you’ll findstrategy cardslike this:

Click“View Details”and you’ll see the full breakdown:

Besides the plain-English summary, key takeaways, entry/exit logic, you have even pseudo-code in Python…

I add new papers every single week.

And today’s post is based on one of them.

This Substack is powered by backtests, forward tests, LLMs, and people like you. Subscribe if you like data-driven strategy building without the guru nonsense. Free is cool. Paid is cooler.


### Here’s what you’ll get in this post:


- Can old-school technical indicators actually work on Bitcoin Futures?

Can old-school technical indicators actually work on Bitcoin Futures?

- How I turn academic papers into testable strategies.

How I turn academic papers into testable strategies.

- Whatactuallyworked and how you can build on it.

Whatactuallyworked and how you can build on it.

Ready?

Let’s go…


### So… what does theresearchsay?


The paper that I found was this one…

We're talking stuff your trading uncle probably used in 1997

- Moving Averages

Moving Averages

- Momentum

Momentum

- RSI

RSI

- OBV

OBV

- Price Channels

Price Channels

No AI. No machine learning.

Just good ol’ buttons and bands.

The paper runs dozens of tests across three major Bitcoin exchanges and checks whetherbasicTA rules (like a 20-day MA crossover) could consistently beat a buy-and-hold.

And…

Some of them worked.

Even after accounting for transaction costs.

But…

(And this is a big but...)

Most of the setups werevery sensitiveto parameter choices.

Meaning:

> If you didn’t nail the exact lookback or threshold…Performance often fell off a cliff.


If you didn’t nail the exact lookback or threshold…Performance often fell off a cliff.

That’s not great for robustness.

But itisgreat for inspiration.

Because if even a plain-vanilla strategy shows a pulse, what happens when you actually know how to test, adapt, and refine it?

Well… that’s where I come in.

Let’s move on to how I turned three of these dusty old indicators into something that might actually deserve a spot in a live portfolio…


## From paper to ideas


Academic results are cool.

But I don’t trade PDFs.

Also, people often say that once a strategy becomes public, its edge starts to fade.

I usually take the main idea and remix it.

Many times, the final result ends up being completely different from the original concept.

And that’s the whole point of collecting ideas.

It’s like building an infinite puzzle and the more pieces you gather, the clearer the big picture becomes.

I’ll show you in 5 steps how to go from no idea to something worth digging deeper into.


#### Step 1 - Where to find ideas


If you don’t have access to my app yet (and I think you should), a good place to start gathering ideas is the website:

https://www.ssrn.com/

There, just click on search and enter a keyword or phrase.

In this example, I typed “bitcoin trading strategies”

And 10,000 papers popped up.

Of course, not all of them fit what I’m looking for, but that’s where refining your search comes in separating the wheat from the chaff.

Which, by the way, is exactly what I do every week when I search for and add relevant strategy papers to my app."

Once I find the paper, I move on to the next step…


#### Step 2 - Understand and Extract the logic


The second step is understanding the core idea behind that logic and why it should work...

Nowadays, this is incredibly easy to do with the help of an LLM.

In this specific case, I simply asked...

But there’s a catch…

It worked so well because I created a custom GPT specifically designed to extract key ideas from papers...

After extracting the paper's core concept in plain English and understanding its theoretical basis, I then begin developing the code implementation...


#### In short, this was the idea…


This is a long-only trend-following strategy that uses two simple moving averages.

It buys when the short-term average rises above the long-term average, signaling upward momentum.

To avoid reacting to short-term noise, the signal must stay valid for a few bars before entering a trade.

There’s also an optional filter that requires the short-term average to be a certain percentage higher than the long-term one.

Once in a trade, the strategy holds the position for a minimum number of bars, no matter what happens.

After that holding period, it exits when the trend weakens that is, when the short-term average drops back below the long-term average.

The idea is to stay invested during strong uptrends and avoid false signals during choppy markets.


#### Step 3: Translate into code


This is where ideas meet execution.

The paper gave me the blueprint…

basic logic, entry/exit rules, and parameter ranges.

But theory doesn’t trade.

I needed to see how these things behavein the real world.

Now you can code it yourself or just ask AI to help you with the logic.

I've been getting great results using AI to write code for me.

Take a look at our first results…

The paper indicated these strategies were highly sensitive to parameter changes.

This means that even a small parameter change - like adjusting the fast MA from 5 to 6 - could dramatically impact results.

So I decided to test this claim...

I ran an optimization focusing solely on the fast and slow moving averages...

The table above shows thatevery single combination was profitable.

And that’s a great sign — because unlike what the paper suggested, this strategy showsstrong parameter stability(at least for the MA…)


#### Step 4: First Results


While the initial results looked promising, a few things caught my attention.

For example…

Only 35 trades over the last 8 years.

That’s about4 trades per year.

Which isway too lowespecially for something as volatile as Bitcoin.

I tried loosening a few parameters to boost trade frequency…

But performance dropped offhardas you can see…

The numbers weren’t terrible…

But they weren’t exactly exciting either.

AProfit Factor of 1.16? That’s underwhelming.

Average trade net profit: $918.31not too bad but that’sbeforeaccounting for slippage and commissions.

I’d want to see at least $1,500 to feel confident.

And once you look at the equity curve…

Yeah… not something I’d feel comfortable trading live.

At all…

So what now?

Do we scrap the whole thing and jump to the next shiny idea?

Nope.

I still believe there’s something worth exploring here.

Which brings us to the next step…


#### Step 5: Small Tweaks, Big Difference


At this point, most people would just toss the system and move on to the next shiny thing.

I don’t do that.

Instead, I treat the first version like a prototype, something I can shape and refine.

So I started tweaking.

Not in the “let’s brute-force optimize everything” kind of way…

But more like:

> What if, instead, we mixed in ideas from other papers?


What if, instead, we mixed in ideas from other papers?

So I tested something simple:

I shortened themoving averagesto have more trades.

But not an overfitted number like 4 and 53.

I played with random rounded numbers…

→ Fast MA:5→ Slow MA:50

That made the system more responsive without going full noise-trader mode.

Then I added:

- A10% profit target

A10% profit target

- A1% stop loss

A1% stop loss

- A10-bar max holding period

A10-bar max holding period

- And an early exit ifvolume momentum fades for 2 days in a row

And an early exit ifvolume momentum fades for 2 days in a row

That’s the real power of building a strategy library you don’t need to reinvent the wheel every time. You just need to know where to borrow the best parts.

And just like that, a basic setup starts showing signs of a real edge.

Let me show you what changed…

And the equity curve…

Perfect?

Far from it.

But now it feels much closer to something I’d actually consider going deeper on refining, validating, maybe even forward-testing.

And this was just the first strategy from the paper.

The paper also explored other classics like:

• Channel Breakouts (CB)• Relative Strength Index (RSI)• On-Balance Volume Averages (OBV)• Support and Resistance (S&R) trading rules

This means, from one paper I can extract dozen of ideas.

Of course probably most of them will be trash but…

When you have asolid process for testing trading ideas, you can run through dozens of them in a short period of time.

And that alone brings you a lot closer to finding something actually worth adding to your portfolio.

And that’s what I did.

I went ahead and tested two more ideas from the paper.

One of them was OBV.

Here’s the resulting equity curve:

and it’s key metrics…

And then I tested a version of the RSI strategy

Which produced this equity curve right here…

Before I show you the full code for all three strategies, let’s rewind for a second.

We’ve covered a lot so far.

You saw where I source my ideas…

How I pulled a raw concept from an academic paper and shaped it into something actually testable…

And then pushed it further.

I refined the logic, added my own layers, and avoided the overfitting trap.

Once I had a version that showed potential, I applied the same framework to two other indicators mentioned in the paper:

OBV and RSI.

Same approach. Different filters. Same goal:

Find something real, something that could make it into a live portfolio.

Now I’m going to show you the full code for all three strategies.

The tweaks. The inputs. The structure that brought each idea to life.

Keep reading…
