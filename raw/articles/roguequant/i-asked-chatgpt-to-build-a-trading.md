---
title: I Asked ChatGPT to Build a Trading Strategy from Scratch
author: The Rogue Quant
url: https://roguequant.substack.com/p/i-asked-chatgpt-to-build-a-trading
date: 2025-03-29T20:06:16+00:00
source: substack
paywalled: False
---

# I Asked ChatGPT to Build a Trading Strategy from Scratch

**URL**: https://roguequant.substack.com/p/i-asked-chatgpt-to-build-a-trading
**Date**: 2025-03-29T20:06:16+00:00
**Author**: The Rogue Quant

---

“Ask and you shall receive” - Matthew 7:7

A few weeks ago, my oldest son turned 6.

And during the party — even though he was having a great time — he kept coming over to ask me:

This Substack is reader-supported. To receive new posts and support my work, consider becoming a free or paid subscriber.

> “Dad, can I open a present now?”


“Dad, can I open a present now?”

Every time I told him the same thing:

> “Wait until we get home. Go enjoy the party.”


“Wait until we get home. Go enjoy the party.”

But let’s be honest…

You know that feeling.

The excitement. The mystery. The thrill of unwrapping something new.

Sometimes it’s “Wow, I love it.”

Other times... “Oh. This.”

Anyway…

I get the exact same feeling when I mess around with LLMs to generate trading strategies.

Today’s post is a behind-the-scenes walkthrough of a recent experiment I ran using ChatGPT to build a new trading strategy…

Relax… you will like it

Ready?


### Start With a Goal


I always start with a goal in mind.

Here’s what I wanted:

- A strategy to tradefutures

A strategy to tradefutures

- On thedailytimeframe

On thedailytimeframe

- With just1–3 parameters

With just1–3 parameters

- And a goal of at least20% annual return

And a goal of at least20% annual return

So I asked ChatGPTexactly that.

It replied with a few clarifying questions (because I told ChatGPT to do it), and then gave mefive strategy ideas:

- Simple Breakout Trend-Follower

Simple Breakout Trend-Follower

- RSI Mean-Reversion

RSI Mean-Reversion

- Moving Average Crossovers with Volatility Filter

Moving Average Crossovers with Volatility Filter

- Momentum Pullback Strategy

Momentum Pullback Strategy

- Bollinger Bands Breakout

Bollinger Bands Breakout


### Let ChatGPT Do Its Thing


Let’s focus on the first strategy for now.

I asked ChatGPT to write out the full strategy logic.

Then I dropped it into TradeStation.

I started testing it on theS&P500, using:

- $2.50 commission

$2.50 commission

- $12.50 slippage

$12.50 slippage

Here’s the results:

Share

hummm, not bad at all!

Then ChatGPT suggested testing on other markets — and to my surprise, it worked on 4 out of the 5 assets it recommended.

But I went further and ran the strategy across 40 futures instruments.

Guess what?

The best results wereexactlyon the symbols ChatGPT had flagged.

(Yes, seriously.)


### Run the Backtest and Analyze


I shared the @ES results back with ChatGPT…

It analyzed the equity curve and even suggested improvements…

The first suggestion was to optimize the parameters.

So I ran the two optimizations:

- EntryLength 10 to 60 with steps of 5

EntryLength 10 to 60 with steps of 5

- ExitLength 5 to 30 with steps of 5

ExitLength 5 to 30 with steps of 5

→ 66 combinations total.

Here’s what stood out:

As you can see above the original parameters (20 and 10) were #11 on the list.

Optimized versions had higher profit but far fewer trades. You can see clearly the number of trades drops from 76 (our original test) to 39 - abig red flagfor overfitting.

But here’s the interesting:

> All 66 versions were profitable


All 66 versions were profitable

That’s a good signal.

So I pushed forward.

I ran a walk-forward test and… it bombed.

When I complained to ChatGPT about it, it replied with something that actually made sense…

so yeah, we found a great overfitting idea.


### Keep Asking Better Questions


We kept discussing new ideas — like adding a volatility filter would lead to even fewer trades…

and it replied with some reasonable logic…

As you can see this back-and-forth could go on forever.

That’s the beauty of it.

It’s not about finding a perfect strategy out of the box.

It’s about generating new ideas to test…

ideas that spark something new and eventually lead to a profitable strategy

ChatGPT won’t hand you an edge, that would be too easy.

But it might hand you a map.

You just need to ask the right questions.

And bring alittlea lot of patience into the process.

(It helps if you have kids.)


### What WouldYouHave Done?


At what point would you have stopped?

After the first good result?

After testing 40 assets?

After all 66 parameter combos came back profitable?

Btw, have you ever tried building a trading strategy with ChatGPT (or any AI)?

Also, I didn’t include the full ChatGPT convo or the code in this post — otherwise, it’d be a mile long.

But if you want it — the full prompt, my back-and-forth with ChatGPT, the code, and which other instruments performed well — just reply, and I’ll send it over.

Leave a comment

Upgrade to paid

Talk soon,

LeoThe Rogue Quant

This Substack is reader-supported. To receive new posts and support my work, consider becoming a free or paid subscriber.

DISCLAIMER:This script is provided for educational and informational purposes only. It is not financial advice, nor a recommendation to buy or sell any securities or financial instruments. Trading involves substantial risk and is not suitable for every investor. You are solely responsible for your own investment decisions and should seek advice from a licensed financial advisor before acting on any information provided in this code and article. The author(s) and publisher disclaim all liability for any loss or damage arising directly or indirectly from the use of this code, including but not limited to trading losses, data inaccuracies, or system errors. Use this code at your own risk.
