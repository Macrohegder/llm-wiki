---
title: How to Improve Your Strategy by 29% with a Single Line of Code
author: The Rogue Quant
url: https://roguequant.substack.com/p/how-to-improve-your-strategy-by-29
date: 2025-03-09T21:23:30+00:00
source: substack
paywalled: False
---

# How to Improve Your Strategy by 29% with a Single Line of Code

**URL**: https://roguequant.substack.com/p/how-to-improve-your-strategy-by-29
**Date**: 2025-03-09T21:23:30+00:00
**Author**: The Rogue Quant

---

I have two little boys, ages 4 and 5.

They love dressing up, but they don’t always pick the right costume for the weather.

Last week, my oldest had a costume day at school.

It was 35°C (95°F)—blazing hot—and he insisted on going as a ninja.

I suggested he wear something cooler, like a soccer player, but—like most kids—he didn’t listen.

By the time he got home, he was miserable, complaining about the heat all day.

At least he didn't consider the astronaut costume!

But I bring this up because traders make the same mistake.

We apply strategies designed for trending markets in choppy conditions… or try mean-reversion setups when volatility is exploding.

And that’s whereregime filterscome in.


### What is a Regime Filter?


A regime filter is a systematic approach to identifying and adapting to different market states or "regimes".

It’s like a weather forecast for the markets.

It helps traders recognize the current market environment and adjust their strategy accordingly.

Just like weather has different states—sunny, cloudy, stormy—financial markets have distinct states.

Some traders divide markets into just two types: trending and mean-reverting.

But in this article, we’ll consider three:

- Trending RegimeClear directional movementAssets consistently moving up or downMomentum strategies work wellExample: Bull or bear markets

Trending Regime

- Clear directional movement

Clear directional movement

- Assets consistently moving up or down

Assets consistently moving up or down

- Momentum strategies work well

Momentum strategies work well

- Example: Bull or bear markets

Example: Bull or bear markets

- Sideways (Choppy) RegimePrices oscillating within a rangeNo clear directional trendMean-reversion strategies perform betterAssets trading between support and resistance levels

Sideways (Choppy) Regime

- Prices oscillating within a range

Prices oscillating within a range

- No clear directional trend

No clear directional trend

- Mean-reversion strategies perform better

Mean-reversion strategies perform better

- Assets trading between support and resistance levels

Assets trading between support and resistance levels

- Volatility Spike RegimeSudden, sharp price movementsHigh uncertaintyIncreased market unpredictabilityOften occurs during economic announcements, geopolitical events

Volatility Spike Regime

- Sudden, sharp price movements

Sudden, sharp price movements

- High uncertainty

High uncertainty

- Increased market unpredictability

Increased market unpredictability

- Often occurs during economic announcements, geopolitical events

Often occurs during economic announcements, geopolitical events


### Why Regime Filters Matter


Why should you even care about regime filters?

Because market conditions change.

A trend-following strategy won’t perform the same way in a mean-reverting environment.

Take a simple momentum strategy, likeRate of Change (ROC).

It measures how fast a price moves compared to a past period.

If you’re in a trending market, it looks like this:

But in a mean-reverting market, price bounces between key levels, making momentum indicators unreliable.

The price is moving within a range, which means you sell when it rises and approaches resistance levels and buy when it drops near support levels.

The problem is that a trend-following strategy won’t work as expected in a market like this.

If your strategy is built to follow trends, the best move in a sideways market is…

Don’t trade at all.

A good regime filter helps you:

• Identify the current market state• Adjust strategy parameters dynamically• Manage risk more effectively• Avoid applying the wrong strategy at the wrong time

Based on these principles, I testedregime filters across 46 futuresusing a simple trend-following strategy.

Here’s all the assets that I backtested:


### The Experiment



#### Test Parameters


📊Assets:46 futures (indexes, currencies, energy, metals, softs, meats, grains, interest rate and even crypto)📆Timeframe:Daily⏳Period:January 2007 – February 2025📈Strategies:Trend-following, mean reversion, breakouts

Originally, I planned to present four strategies and four different regime filters, but the article became too long. So, I decided to split it intofour parts.

This isPart 1, where I testedone simple regime filter:

> Filter Condition: Only take trades in a bull market.


Filter Condition: Only take trades in a bull market.

How do we define a bull market?Simple:

Now let’s see if filtering trades actually improved performance.


### The Results: Does Filtering Improve Performance?


Let’s get straight to the numbers.

Without a regime filter, the total portfolio profit came in at$707,490.

With the regime filter (only taking trades in a bull market), total profit jumped to$918,511—a29% increase.


### Breaking It Down



#### 1. Higher Returns, More Selective Trading


The regime filter producedfewer trades, but the ones it took weremore profitable.

The profit factor increased slightly, indicating an improvement in trade quality. At the same time, the number of trades dropped significantly, which also means lower commission costs.


#### 2. Win Rate & Average Trade Size: More Efficient Trades


One of the key concerns when adding a filter is whether it actually improves trade quality. Here’s what the data shows:

Not only did thewin rate improve, butaverage winning trades became larger—a huge win.

However,average losing trades also got bigger, which means further refinements could help.


#### 3. Risk & Drawdown: Still Room for Improvement


Surprisingly,maximum drawdowns didn’t improve.

While theprofit-to-drawdown ratio improved, thelargest losing trade remained unchanged.


#### 4. Which Assets Benefited the Most?


Here’s a look atwhich markets improved the mostwith the filter:

Meanwhile, somemarkets performed worsewith filtering:

Clearly,some assets respond much better to regime filtering than others.

That leads us to an important question…


### Does Regime Filtering Always Work?


Of course not. And btw, there is no “always” in financial markets.

A regime filter helps you avoid taking trades in unfavorable market conditions—butit doesn’t guarantee that filtered trades will always be more profitable.

Take trend-following strategies, for example. They thrive in markets that experience strong, sustained trends.

But what happens if the filter mistakenly keeps you out of the early stages of a trend?

You could miss some of the best opportunities simply because the market hadn't "officially" signaled an uptrend yet.

Here’s the real issue:market behavior is fluid, not binary.

A trend doesn’t start and stop based on a strict set of rules, and volatility doesn’t rise and fall in a perfectly predictable way.

If you apply a rigid filter that’s too slow to react, you might avoid bad trades, but you might also sit on the sidelines while profitable opportunities pass by.

That’s why blindly applying a regime filter isn’t the best approach.

Instead, consider:

- How different market environments impact your strategy.A filter that works well for one asset or timeframe might hurt performance in another (this is the fractal nature of markets).

How different market environments impact your strategy.A filter that works well for one asset or timeframe might hurt performance in another (this is the fractal nature of markets).

- How quickly your filter adapts.A slow-moving filter (like a 200-day moving average) may keep you out of great trades, while a faster one (like ATR-based volatility regimes) might react too frequently.

How quickly your filter adapts.A slow-moving filter (like a 200-day moving average) may keep you out of great trades, while a faster one (like ATR-based volatility regimes) might react too frequently.

- Whether a filter aligns with your strategy.If a strategy naturally benefits from high volatility, filtering out volatile periods could actually hurt performance.

Whether a filter aligns with your strategy.If a strategy naturally benefits from high volatility, filtering out volatile periods could actually hurt performance.

- Intermarket Dynamics.The behavior of one market can influence another. For instance, the regime of the US Dollar can significantly impact commodity markets (I’ll write about intermarket strategies next week).

Intermarket Dynamics.The behavior of one market can influence another. For instance, the regime of the US Dollar can significantly impact commodity markets (I’ll write about intermarket strategies next week).

- Structural Breaks.Major economic events, policy changes, or technological disruptions can fundamentally alter how a market behaves, rendering historical patterns obsolete—meaning your regime filter could become useless overnight.

Structural Breaks.Major economic events, policy changes, or technological disruptions can fundamentally alter how a market behaves, rendering historical patterns obsolete—meaning your regime filter could become useless overnight.

- Develop a multi-factor regime identification.Instead of relying on a single indicator, develop systems that dynamically weight multiple factors based on their recent predictive power. I frequently applied this concept as a data scientist—fine-tuning predictive models to adapt to shifting real-world conditions, though in a completely different industry.

Develop a multi-factor regime identification.Instead of relying on a single indicator, develop systems that dynamically weight multiple factors based on their recent predictive power. I frequently applied this concept as a data scientist—fine-tuning predictive models to adapt to shifting real-world conditions, though in a completely different industry.

So, while regime filtering can be a powerful tool, it’s not a one-size-fits-all solution. It’s just one piece of a much larger puzzle when it comes to refining trading strategies.


### Final Thoughts: What This Means for Your Trading


This experiment showedone simple wayto improve a strategy—by filtering trades based on market conditions.

But it’s just the beginning.

There aremanyways to implementbetter regime filters, such as:

- Momentum-based filters(MACD, RSI, ADX)

Momentum-based filters(MACD, RSI, ADX)

- Volatility-based filters(ATR, Bollinger Bands, VIX)

Volatility-based filters(ATR, Bollinger Bands, VIX)

- Machine learning models(for the quant nerds out there)

Machine learning models(for the quant nerds out there)

- Market breadth indicators(Advance-Decline Line, new highs vs. new lows)

Market breadth indicators(Advance-Decline Line, new highs vs. new lows)

And of course,combining multiple filterscould lead toeven better resultsoverfitting so take that into account (I’m repeating myself I know but this is super important).

InPart 2, I’ll explore another type of regime filter—one based onvolatility conditions instead of moving averages.

If you are a paid subscriber you also get:

✅The exact codeI used for the backtest so you can test it yourself✅Ask me anythingabout regime filters to fine-tune your strategy✅The top 5 assetsthat saw the biggest performance boost (and what they have in common)✅Request custom backtests—send me your strategy, and I’ll test it for you

You can upgrade here:

What You're Missing Inside

See you next time,

tchau,

- Leo
