---
title: Holy Grail or Holy Fail? Backtesting Candlestick Patterns
author: The Rogue Quant
url: https://roguequant.substack.com/p/holy-grail-or-holy-fail-backtesting
date: 2025-02-09T14:21:02+00:00
source: substack
paywalled: False
---

# Holy Grail or Holy Fail? Backtesting Candlestick Patterns

**URL**: https://roguequant.substack.com/p/holy-grail-or-holy-fail-backtesting
**Date**: 2025-02-09T14:21:02+00:00
**Author**: The Rogue Quant

---

"Show me the money!" –Jerry Maguire

A few days ago, a longtime friend told me he made a winning trade that netted him a few thousand bucks—more specifically, he raked in the cash on one trade.

And before you think I got jealous…

But I got really curious (and alotlittle bit of FOMO hit me), so I asked:

"What's the strategy?"

And he replied,

"Man, I just traded the engulfing pattern."

That simple answer sparked a ton of ideas in my head.

One idea was to start a series in this newsletter dedicated solely to backtesting those famous candlestick patterns we’ve all heard about for ages.

Kind of MythBusters show…

Anyway…

Today’s edition is exactly that—kicking things off by showing you the results of a bullish engulfing strategy in the futures markets.

To get to the bottom of it, I spent more than 30 hours researching and backtesting this strategy.

In short, I backtested this pattern on over 40 futures assets—from coffee to the S&P500, including metals, interest rates, currencies, and of course Bitcoin.

Data doesn't lie (unless you torture it… hello optimization guys I’m talking to you), and I'm here to show you what really worked and what didn’t.

So, grab a drink, sit back, and let's dive into this ‘experiment’ together.


### The Bullish Engulfing Pattern


Let’s break down what a bullish engulfing pattern is. Here’s Investopedia’s definition:

> "A bullish engulfing pattern is a white candlestick that closes higher than the previous day's opening after opening lower than the previous day's close. It can be identified when a small black candlestick, showing a bearish trend, is followed the next day by a large white candlestick, showing a bullish trend, the body of which completely overlaps or engulfs the body of the previous day’s candlestick."


"A bullish engulfing pattern is a white candlestick that closes higher than the previous day's opening after opening lower than the previous day's close. It can be identified when a small black candlestick, showing a bearish trend, is followed the next day by a large white candlestick, showing a bullish trend, the body of which completely overlaps or engulfs the body of the previous day’s candlestick."

So, what does that mean in plain English?

Imagine you're looking at a chart. You see a small red candle that tells you sellers were in charge. Then, the very next day, a huge green candle comes along and completely swallows that previous candle. It’s like a classic David-versus-Goliath moment—suddenly, the bulls take control.

The logic behind this pattern is pretty simple:

> it signals a shift in momentum.


it signals a shift in momentum.

That small red candle shows selling pressure, but when a large green candle appears and completely engulfs it, it means buyers have stepped in with force.

Essentially, this pattern hints that buying strength is building up, which could signal a reversal from the downtrend.

Take a look at the image below (also from Investopedia):


### The Methodology


To really get to the bottom of whether the bullish engulfing pattern has any real edge, I used the following parameters:

- Markets Traded:41 futures instruments (currencies, grains, softs, energies, interest rates, indexes, metals)

Markets Traded:41 futures instruments (currencies, grains, softs, energies, interest rates, indexes, metals)

- Backtest Period:January 1, 2007 – December 31, 2024

Backtest Period:January 1, 2007 – December 31, 2024

- Data Frequency:Daily

Data Frequency:Daily

- Trading Costs:$2.50 commission; $15 slippage (both per contract)

Trading Costs:$2.50 commission; $15 slippage (both per contract)

- Backtesting Platform:TradeStation

Backtesting Platform:TradeStation

I followed my usual process…

> Idea → Research → Backtest → Analyze → Refine


Idea → Research → Backtest → Analyze → Refine

I tried a few optimizations to see if I could uncover any hidden edge…

Spoiler alert: I didn’t find one.


### The Strategy


This strategy is all about spotting a bullish reversal during a downtrend.

Here’s how I defined the variables:

- Downtrend Check:The previous day’s candle must be bearish—meaning it closed lower than it opened (a “black” candle). Plus, its low must be the lowest seen in the past 20 days. This confirms that the market was in a downtrend.

Downtrend Check:The previous day’s candle must be bearish—meaning it closed lower than it opened (a “black” candle). Plus, its low must be the lowest seen in the past 20 days. This confirms that the market was in a downtrend.

- Engulfing Confirmation:On the current day, the candle must flip the script by being bullish (closing higher than it opened—a “green” candle). The body of this candle has to completely engulf the body of the previous bearish candle. In simple terms, the current candle’s high is higher and its low is lower than the previous day’s candle.

Engulfing Confirmation:On the current day, the candle must flip the script by being bullish (closing higher than it opened—a “green” candle). The body of this candle has to completely engulf the body of the previous bearish candle. In simple terms, the current candle’s high is higher and its low is lower than the previous day’s candle.

- Trade Entry:When these conditions are met, a buy order is triggered on the next bar. The idea is that this pattern signals a shift—buyers are taking over, potentially reversing the downtrend.

Trade Entry:When these conditions are met, a buy order is triggered on the next bar. The idea is that this pattern signals a shift—buyers are taking over, potentially reversing the downtrend.

- Exit Rules:Once in the trade, there are two ways to exit:• Hold for a set period (in this case, 5 days).• Or, if the current bar's low falls below the recorded stop level—the low of the candle preceding the engulfing candle—exit the trade immediately.

Exit Rules:Once in the trade, there are two ways to exit:• Hold for a set period (in this case, 5 days).• Or, if the current bar's low falls below the recorded stop level—the low of the candle preceding the engulfing candle—exit the trade immediately.

Like I mentioned before, I dug into the most popular rules I could find online to define this strategy.

For example, how do you define a downtrend? Or even the engulfing pattern?

I chose to define the downtrend as “the lowest low of the last 20 days.”

Maybe that’s not how you do it.

Maybe you use a simple 200-day moving average to signal a downtrend (by the way, I tested that too—and it didn’t work)…

Or perhaps you have an entirely different approach.

The point is, there’s always someone who’ll say,“That’s not how you define XYZ.”

If you’ve got any suggestions to improve this backtest—whatever variable you handle differently—send them my way, and I’ll test them out.

Anyway, shall we move on to the results?


### The Results


I grouped the instruments into these categories:

- Currencies

Currencies

- Grains

Grains

- Softs

Softs

- Energies

Energies

- Interest Rates

Interest Rates

- Indexes

Indexes

- Metals

Metals

For each group, I compiled key metrics:

•Net Profit•Number of Trades•Average Trade•Profit Factor•Maximum Drawdown

Let’s start with…


### Currencies:


Before you say anything let me point some hummm points to consider…

We had few trades in the period… and with the exception of the Mexican peso which has a ‘good’ equity curve… the others don’t follow

The Mexican Peso equity curve (which is pretty decent)…

The green dots shows when the equity makes a new high…

The Canadian Dollar…

The British Pound equity curve…

The Swiss Franc…

Anyway, let’s move on…


### Grains


And this is the best equity curve for this group, the Live Cattle…

Next…


### Softs


Cotton is the worst while Cocoa seems to produce solid results.

But when we check the equity curve…

So we move to the next group…


### Energy


We only have Natural Gas to save the day.

And this is the equity curve…

Not all that bad…

but we still need to see more trades with that setup…

Let’s move, next we have…


### Interest Rates


And this is the 2-Year T-Note equity curve…

There is some room for improvement but what I don’t like is that the others even the 5-Year are pretty bad.

When backtesting groups like these I want to see some consistency among assets…

Otherwise, this can be a fluke…

Let’s check the next…


### Metals


Gold and Platinum are up but here are their equity curves…

Nope, we can’t trade something like that.

And the last one…


### Indexes


As you can see, nearly every case came out with an ugly equity curve—100% of them looked like losers at first glance.

That surprised me, because indices (and perhaps forex) are exactly where we hear gurus rave about having discovered the holy grail of candlestick patterns and yada yada yada.

Let’s recap…

I backtested 41 futures:

- Positive Instruments:18

Positive Instruments:18

- Negative Instruments:23

Negative Instruments:23

Among all the positive instruments, only two winners had a decent equity curve:

- Natural Gas (NG):Net Profit of $25,600.00, strong profit factor (3.22), and a relatively manageable drawdown.

Natural Gas (NG):Net Profit of $25,600.00, strong profit factor (3.22), and a relatively manageable drawdown.

- Mexican Peso (MP1):Net Profit of $7,350.00, boasting an outstanding profit factor of 6.40 and minimal drawdown.

Mexican Peso (MP1):Net Profit of $7,350.00, boasting an outstanding profit factor of 6.40 and minimal drawdown.

And that's the bare minimum I need to continue deepening my research with further statistical analyses—like Monte Carlo simulations, noise tests, variance analysis, optimizations, walk-forward analysis, and so on.

Of course, in this case I already burned the data—because I tested all the way until 12/31/2024—leaving no data for an out-of-sample analysis. But that's a story for another day.

I know it's a lot of information to process—but that's life, right?

And btw, if you're a paid subscriber, you get exclusive access to a detailed report where I show you how to improve the performance of this strategy with just a single tweak in the formula.

No optimizations—just one simple change in the code.

For instance, remember the E-Mini MidCap400 equity curve?

After a small tweak, I got this:

Not perfect (btw that word does not exist in trading) but this is something I can work on a deeper level.

Anyway…

Paid subscribers also get:• The strategy's performance on 60-minute and 240-minute timeframes.• Results using another popular downtrend definition favored by many traders.• How varying the holding period impacts the overall performance.• A Monte Carlo simulation that tests the strategy's robustness.• How to improve the results working only on the exits•A breakdown of the strategy’s performance in different market regimes—bullish, bearish, and sideways• The results of the bearish engulfing pattern in all 41 instruments

I'm want the report

Thanks for reading this deep dive.

Grab another drink (if you’re still awake) and consider subscribing for even more exclusive, in-depth analysis.

tchau,

-Leo
