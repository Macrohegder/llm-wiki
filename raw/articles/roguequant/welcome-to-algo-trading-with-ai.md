---
title: Welcome to The Rogue Quant. 
author: The Rogue Quant
url: https://roguequant.substack.com/p/welcome-to-algo-trading-with-ai
date: 2025-01-30T00:13:12+00:00
source: substack
paywalled: False
---

# Welcome to The Rogue Quant. 

**URL**: https://roguequant.substack.com/p/welcome-to-algo-trading-with-ai
**Date**: 2025-01-30T00:13:12+00:00
**Author**: The Rogue Quant

---

Welcome to Fight Club. The first rule of Fight Club is: you do not talk about Fight Club ―Chuck Palahniuk

It’s the first edition and I’m already breaking the first rule of one of my favorite movies.

> The first rule of trading is:Nobody shares the good stuff.



### The first rule of trading is:Nobody shares the good stuff.


And let’s be real, it makes sense. Why would anyone willingly share a strategy that’s actually making them money?

Especially with people they don’t even know? (I’m Leo btw, nice to meet you)

If you found a golden goose laying eggs in your backyard, would you hand out the GPS coordinates to everyone?

Of course not.

Nobody wants to create competition for themselves.

In the trading world, good information is power.

Winning strategies are like closely guarded secrets… just think about the employees at the Medallion Fund. They have to sign a non-disclosure agreement. Because when you’re running a fund with returns as ridiculous as theirs, protecting the strategy is just as important as building it. And, let’s face it, in this game, the people who know the secrets win.


### So, Why Am I Doing This?


There are a few reasons, so let me lay it out for you—no fluff, no mystery.

Spoiler alert: You’re not going to succeed with just one strategy. That’s the end of the movie, right there. Period.

It took me years to figure that out. What you need is a portfolio of strategies, and you need to monitor that portfolio closely (don’t worry, we’ll get there but one newsletter at a time).

Now, sharing one strategy with you isn’t going to hurt me. If it did, I wouldn’t be doing this (sorry to disappoint you). In fact, when traders share ideas, two things usually happen:

- Hatersshow up, ranting about why it doesn’t work. (“Blah blah blah, it breaks in this market condition, yada yada yada…”)

Hatersshow up, ranting about why it doesn’t work. (“Blah blah blah, it breaks in this market condition, yada yada yada…”)

- Smart peoplecome in, offering critiques or new perspectives. And guess what? That helps me refine the strategy, test it from new angles, and ultimately level up my own game.

Smart peoplecome in, offering critiques or new perspectives. And guess what? That helps me refine the strategy, test it from new angles, and ultimately level up my own game.

So, to those of you who’ll push me to rethink, refine, and evolve—thank you in advance. I know you’re out there, and you’re going to make me better.


### Why Else?


I’ve spent alotof money (and time) chasing shiny objects—guru courses, meh mentorships, sketchy trading systems (the holy grail, you know?), late-night YouTube marathons, and even self-taught Python sessions because, apparently, suffering builds character. The beginning of my journey (or should I say the first 15 years of wanting to become a professional trader) was brutal, and I’ve been through enough pain to know how does it feel to start from scratch in this market, in this industry of illusions…

“I'll make a million in 6 months with this strategy...” yep been there... didn't happen.

I also know what it's like to put so much energy into a project for years (did someone say 15 years?) and look back and see that you haven't moved anywhere.

Or watch your finances evaporate by operating penny stocks... (but that's a story for another time)

What can I say… I’ve seen a lot over the years. But in the last 10 years (just for context—I’ve been in this market for 25), everything changed when I started building trading systems and trading systematically.

The real turning point came when I realized that, before running any strategy, I needed to test if the idea actually had an edge. Once I understood that, I started seeing real results.

And I haven’t stopped since.

And again… sharing my ideas in public helps me too. Writing them down forces me to refine my thinking, improve my logic, and, as a result, elevate my game. So yes, I’m doing this to help you—but let’s not pretend I’m not getting something out of it.


### One More Reason


People have been telling me for ages,“You should start a newsletter. You’d kill it.”They said people might even pay for it. So I thought,Why not? Let’sbacktest thisforward-test this idea.

And here we are.

Welcome to the exception to the rule. Let’s get started.


### The Momentum Strategy: Testing the Edge on Futures


Today, we’re diving into one of the most classic (and debated) strategies in trading:

> momentum



### momentum


You’ve probably heard about this strategy a million times before...

From academic papers like"Fact, Fiction, and Momentum Investing"by Clifford S. Asness et al. (2014)…

…or books like"Dual Momentum Investing: An Innovative Strategy for Higher Returns with Lower Risk"by Gary Antonacci (this is a great one btw)

…to legendary traders like Richard Dennis, Mark Minervini, Richard Driehaus, Ed Seykota, Michael Covel, and many others talking about different forms of momentum.

So yeah, I know you have heard it before…

But here’s the twist—we’re not just talking theory. We backtested it, and I’m here to show you exactly what worked, what didn’t, and what you can learn from it.


### The Idea


Momentum strategies are built on one simple premise: what’s moving in one direction is likely to keep moving in that direction. It’s the trading equivalent of Newton’s First Law—a market in motion stays in motion (until it doesn’t).

In this edition, I’m going to show you a trading idea I backtested in the interest rates market, specifically on the daily TY (10-Year U.S. Treasury Note Futures).

This is the first result I got:

This strategy is pretty simple when you break it down.

It’s all about figuring out if the price of something—stocks, futures, whatever—is going up or down, and then riding that move for a while.

Here’s how it works:


### Step 1: Check the Trend


We look at the price today and compare it to where it was 50 days ago. That gives us an idea of whether the price is trending up or down.

- If the price today is higher than it was 50 days ago, we think,“Hey, this thing is climbing. Let’s buy and see if we can ride the trend.”

If the price today is higher than it was 50 days ago, we think,“Hey, this thing is climbing. Let’s buy and see if we can ride the trend.”

- If the price today is lower, we think,“Alright, it’s falling. Let’s short it and try to profit on the way down.”

If the price today is lower, we think,“Alright, it’s falling. Let’s short it and try to profit on the way down.”

Formula Logic:

- We’re subtracting the older price to see how much the price has moved.

We’re subtracting the older price to see how much the price has moved.

- Then we divide by the older price to calculatethe percentage changeover the last 50 days.

Then we divide by the older price to calculatethe percentage changeover the last 50 days.

- Example:If the price today is $110 and it was $100 fifty days ago:Momentum = (110 - 100) / 100 = 0.10 (or +10%)Positive momentum: The price has risen by 10%.Negative momentum: The price has dropped.

Example:

- If the price today is $110 and it was $100 fifty days ago:

If the price today is $110 and it was $100 fifty days ago:

- Positive momentum: The price has risen by 10%.

Positive momentum: The price has risen by 10%.

- Negative momentum: The price has dropped.

Negative momentum: The price has dropped.

This part is calledmomentum—we’re just going with the flow of where the price seems to be headed.

Positive Momentum: When the calculation is positive (e.g., +10%), it means the price is trending up. That’s your signal tobuy.

Negative Momentum: When the calculation is negative (e.g., -5%), it means the price is trending down. That’s your signal toshort.

Simple as that.

Here’s the code for easylanguage:


### Step 2: Avoid Chaotic Markets


Before we make a trade, we check how wild the market is.

We use something calledvolatility, which measures how much the price has been bouncing around lately.

If it’s jumping up and down too much, it’s hard to predict what’ll happen next. So we skip trading in those situations.

We measure volatility with a number called ATR (Average True Range).

If this number is low enough, it means the market is calm, and we’re good to go.

If it’s too high, we just wait for better conditions.


### How It All Works Together


- ATR Calculation:We use the last 14 days of price movement to calculate how volatile the market is.ATR gives us a simple number: how much the price is moving, on average, per day.

ATR Calculation:

- We use the last 14 days of price movement to calculate how volatile the market is.

We use the last 14 days of price movement to calculate how volatile the market is.

- ATR gives us a simple number: how much the price is moving, on average, per day.

ATR gives us a simple number: how much the price is moving, on average, per day.

- Threshold Comparison:We compare the ATR to a threshold (ATRThreshold).If ATR is too high, we stay out. If it’s low enough, we trade.

Threshold Comparison:

- We compare the ATR to a threshold (ATRThreshold).

We compare the ATR to a threshold (ATRThreshold).

- If ATR is too high, we stay out. If it’s low enough, we trade.

If ATR is too high, we stay out. If it’s low enough, we trade.

- Why This Matters:Volatility is the enemy of consistency. Big swings make it harder for momentum strategies to work. By filtering out trades during chaotic times, we increase the chances of success.

Why This Matters:

- Volatility is the enemy of consistency. Big swings make it harder for momentum strategies to work. By filtering out trades during chaotic times, we increase the chances of success.

Volatility is the enemy of consistency. Big swings make it harder for momentum strategies to work. By filtering out trades during chaotic times, we increase the chances of success.

Here’s the code:


### Step 3: Decide When to Exit


Once we’re in a trade, we don’t stay forever.

We have two simple rules for getting out:

- If the trend reverses: Let’s say we bought because the price was going up. If the price starts going down instead, we get out to avoid losing too much.

If the trend reverses: Let’s say we bought because the price was going up. If the price starts going down instead, we get out to avoid losing too much.

- If we’ve been in the trade for 10 days: Even if nothing bad happens, we don’t like hanging around for too long. If the trade isn’t doing much after 10 days, we exit and look for a better opportunity.

If we’ve been in the trade for 10 days: Even if nothing bad happens, we don’t like hanging around for too long. If the trade isn’t doing much after 10 days, we exit and look for a better opportunity.


### Why This Works


- Momentum Reversal:This ensures we only stay in trades while the trend is in our favor. If the trend flips, we’re out immediately.

Momentum Reversal:

- This ensures we only stay in trades while the trend is in our favor. If the trend flips, we’re out immediately.

This ensures we only stay in trades while the trend is in our favor. If the trend flips, we’re out immediately.

- Time-Based Exit:Not all trades will work as expected. By setting a time limit, we avoid wasting time and resources on trades that aren’t going anywhere.

Time-Based Exit:

- Not all trades will work as expected. By setting a time limit, we avoid wasting time and resources on trades that aren’t going anywhere.

Not all trades will work as expected. By setting a time limit, we avoid wasting time and resources on trades that aren’t going anywhere.

- Discipline:Exiting quickly when conditions change keeps losses small and capitalizes on trends while they’re still active.

Discipline:

- Exiting quickly when conditions change keeps losses small and capitalizes on trends while they’re still active.

Exiting quickly when conditions change keeps losses small and capitalizes on trends while they’re still active.

Here’s the code:


### Here’s the trading performance


We’re not trying to predict the future or guess where the market will go next. Instead, we’re playing the odds:

- Prices that are moving in one direction tend to keep moving that way for a while. That’s why we use momentum.

Prices that are moving in one direction tend to keep moving that way for a while. That’s why we use momentum.

- Markets that are too volatile are harder to trade, so we avoid them.

Markets that are too volatile are harder to trade, so we avoid them.

- By exiting quickly when things don’t go our way, we keep losses small and stay in the game.

By exiting quickly when things don’t go our way, we keep losses small and stay in the game.


#### Key Metrics Breakdown


- Total Net Profit: $35,936.25This is the final profit after all wins and losses across 368 trades. It’s decent but needs to be contextualized with other metrics like drawdown and trade efficiency.

Total Net Profit: $35,936.25

- This is the final profit after all wins and losses across 368 trades. It’s decent but needs to be contextualized with other metrics like drawdown and trade efficiency.

This is the final profit after all wins and losses across 368 trades. It’s decent but needs to be contextualized with other metrics like drawdown and trade efficiency.

- Profit Factor: 1.24For every $1 lost, the strategy makes $1.24. While positive, this indicates a relatively slim margin, suggesting room for improvement in either risk management or trade filtering.

Profit Factor: 1.24

- For every $1 lost, the strategy makes $1.24. While positive, this indicates a relatively slim margin, suggesting room for improvement in either risk management or trade filtering.

For every $1 lost, the strategy makes $1.24. While positive, this indicates a relatively slim margin, suggesting room for improvement in either risk management or trade filtering.

- Total Number of Trades: 368This shows the strategy is active, which is great for building a diversified portfolio. More trades provide better statistical significance in the performance metrics.

Total Number of Trades: 368

- This shows the strategy is active, which is great for building a diversified portfolio. More trades provide better statistical significance in the performance metrics.

This shows the strategy is active, which is great for building a diversified portfolio. More trades provide better statistical significance in the performance metrics.

- Win Rate: 51.09%Just over half of the trades are winners. Momentum strategies often have win rates in this range, as they rely on capturing outsized winners to offset losses.

Win Rate: 51.09%

- Just over half of the trades are winners. Momentum strategies often have win rates in this range, as they rely on capturing outsized winners to offset losses.

Just over half of the trades are winners. Momentum strategies often have win rates in this range, as they rely on capturing outsized winners to offset losses.

- Avg Trade Net Profit: $97.65On average, each trade nets $97 (not the best I know). But this is solid because I’m considering slipagge and commissions and with 368 trades over 15 years, it indicates the strategy might benefit from either higher frequency or larger position sizing.

Avg Trade Net Profit: $97.65

- On average, each trade nets $97 (not the best I know). But this is solid because I’m considering slipagge and commissions and with 368 trades over 15 years, it indicates the strategy might benefit from either higher frequency or larger position sizing.

On average, each trade nets $97 (not the best I know). But this is solid because I’m considering slipagge and commissions and with 368 trades over 15 years, it indicates the strategy might benefit from either higher frequency or larger position sizing.

- Max Drawdown: $12,880.00This is the largest loss from peak equity. It’s significant but manageable given the total net profit and the strategy's long-term horizon.

Max Drawdown: $12,880.00

- This is the largest loss from peak equity. It’s significant but manageable given the total net profit and the strategy's long-term horizon.

This is the largest loss from peak equity. It’s significant but manageable given the total net profit and the strategy's long-term horizon.

- Return on Initial Capital: 35.94%Over the backtest period, the strategy generated a return of nearly 36%. Annualized, that’s2.19% per year, which is underwhelming for systematic trading.

Return on Initial Capital: 35.94%

- Over the backtest period, the strategy generated a return of nearly 36%. Annualized, that’s2.19% per year, which is underwhelming for systematic trading.

Over the backtest period, the strategy generated a return of nearly 36%. Annualized, that’s2.19% per year, which is underwhelming for systematic trading.

- Largest Winning Trade: $5,053.75Largest Losing Trade: -$3,368.13The largest winner is 1.5x the size of the largest loser, aligning with the momentum strategy’s goal to let winners run.

Largest Winning Trade: $5,053.75Largest Losing Trade: -$3,368.13

- The largest winner is 1.5x the size of the largest loser, aligning with the momentum strategy’s goal to let winners run.

The largest winner is 1.5x the size of the largest loser, aligning with the momentum strategy’s goal to let winners run.

- Average Winning Trade: $994.49Average Losing Trade: -$839.05The ratio of avg win to avg loss is1.19, which is okay but not exceptional. Improving this ratio could significantly boost the strategy's performance.

Average Winning Trade: $994.49Average Losing Trade: -$839.05

- The ratio of avg win to avg loss is1.19, which is okay but not exceptional. Improving this ratio could significantly boost the strategy's performance.

The ratio of avg win to avg loss is1.19, which is okay but not exceptional. Improving this ratio could significantly boost the strategy's performance.

- PNL/Max Drawdown: 2.79This ratio shows the profit earned for every dollar of drawdown risk. A ratio above 2 is generally considered good, so this is a strong point for the strategy.

PNL/Max Drawdown: 2.79

- This ratio shows the profit earned for every dollar of drawdown risk. A ratio above 2 is generally considered good, so this is a strong point for the strategy.

This ratio shows the profit earned for every dollar of drawdown risk. A ratio above 2 is generally considered good, so this is a strong point for the strategy.


### Weaknesses & Improvement Ideas


- Low Annual Return (2.19%):The strategy could benefit from:Increasing trade frequency by shortening the lookback period (e.g., from 50 days to 30 days).Adding filters to reduce losing trades (e.g., tighter volatility thresholds or momentum confirmation signals).

Low Annual Return (2.19%):

- The strategy could benefit from:Increasing trade frequency by shortening the lookback period (e.g., from 50 days to 30 days).Adding filters to reduce losing trades (e.g., tighter volatility thresholds or momentum confirmation signals).

The strategy could benefit from:

- Increasing trade frequency by shortening the lookback period (e.g., from 50 days to 30 days).

Increasing trade frequency by shortening the lookback period (e.g., from 50 days to 30 days).

- Adding filters to reduce losing trades (e.g., tighter volatility thresholds or momentum confirmation signals).

Adding filters to reduce losing trades (e.g., tighter volatility thresholds or momentum confirmation signals).

- Relatively High Drawdown:Reduce the max drawdown by:Incorporating a trailing stop to lock in profits.Testing position sizing based on volatility (e.g., risk 1% of equity per trade).

Relatively High Drawdown:

- Reduce the max drawdown by:Incorporating a trailing stop to lock in profits.Testing position sizing based on volatility (e.g., risk 1% of equity per trade).

Reduce the max drawdown by:

- Incorporating a trailing stop to lock in profits.

Incorporating a trailing stop to lock in profits.

- Testing position sizing based on volatility (e.g., risk 1% of equity per trade).

Testing position sizing based on volatility (e.g., risk 1% of equity per trade).

- Profit Factor (1.24):Improve the profit factor by:Optimizing exits to capture larger wins (e.g., trailing stops or dynamic exit rules).Filtering out low-quality trades using additional indicators (e.g., RSI or MACD confirmation).

Profit Factor (1.24):

- Improve the profit factor by:Optimizing exits to capture larger wins (e.g., trailing stops or dynamic exit rules).Filtering out low-quality trades using additional indicators (e.g., RSI or MACD confirmation).

Improve the profit factor by:

- Optimizing exits to capture larger wins (e.g., trailing stops or dynamic exit rules).

Optimizing exits to capture larger wins (e.g., trailing stops or dynamic exit rules).

- Filtering out low-quality trades using additional indicators (e.g., RSI or MACD confirmation).

Filtering out low-quality trades using additional indicators (e.g., RSI or MACD confirmation).


### What We Learned


- Momentum Works (Sometimes):This strategy thrived in clear, trending markets but was a nightmare during sideways action. The key takeaway? Momentum strategies need filters to avoid getting chewed up in choppy markets.

Momentum Works (Sometimes):This strategy thrived in clear, trending markets but was a nightmare during sideways action. The key takeaway? Momentum strategies need filters to avoid getting chewed up in choppy markets.

- Simplicity Has Its Limits:While the 10/50 moving average crossover is easy to implement, it’s also a blunt instrument. Adding additional filters (like volatility measures) could improve performance.

Simplicity Has Its Limits:While the 10/50 moving average crossover is easy to implement, it’s also a blunt instrument. Adding additional filters (like volatility measures) could improve performance.

- Backtesting Is Everything:Without the backtest, you might assume this strategy is a holy grail. But seeing the data—the good, bad, and ugly—tells the real story.

Backtesting Is Everything:Without the backtest, you might assume this strategy is a holy grail. But seeing the data—the good, bad, and ugly—tells the real story.


### Wait! To get the full code upgrade your subscription here:


Unlock the Code. Literally.


### Got Questions?


Awesome—let’s talk.

I personally read and reply to every single email. Yep, no bots, just me—Leo.

Now my turn… Have you ever tried a momentum strategy? What filters or tweaks have worked (or bombed) for you? Hit reply and share your thoughts—I’d love to hear them. Who knows? Your idea might even make it into a future backtest and feature.

Next week, we’ll dive into a strategy that uses another asset as a filter. Stay tuned for more backtests, lessons, and (hopefully) fewer drawdowns.

And here’s a teaser for next week: we’re exploring a strategy that uses a completely different asset as a filter. Think more edge, fewer drawdowns, and some lessons you don’t want to miss.

Let’s keep pushing—research smarter, backtest harder, and build trading systems that actually work.

Catch you in the next issue,Tchau for now!

– Leo
