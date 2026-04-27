---
title: "Dynamic Money Management"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/dynamic-money-management/"
date: "2020-01-15"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Dynamic Money Management

**来源**: [QuantInsti](https://blog.quantinsti.com/dynamic-money-management/)  
**日期**: 2020-01-15  
**作者**: QuantInsti

---

## 原文

Dynamic Money Management

ByZach Oakes

Many aspiring traders dream mostly of God-like returns — beginning with a few good trades they get the mental calculator out and start figuring out exactly when they’ll reach Billionaire status, or open the next Renaissance Capital.

Experienced traders will tell you that good and bad trades really don’t change much between amateurs and master traders — the real difference is in discipline, and that’s usually realized in the form of Money Management.

When I think of the holy grail system, I dream mostly in Standard Deviation, Correlations, and Drawdowns. I dream of a system with a standard deviation that requires scientific notation to measure it’s Variance, with an Avg Correlation < -.25, and Drawdowns < 1%.

I only think about return, or really any upside measure of performance once during the development process — and that’s when I first test a system to ensure it meets my minimum performance threshold. As long as it’s sufficient, I don’t think about returning again until the Portfolio level.

For those who are curious, my system threshold is usually:

25% YoY,

<2.5% DD,

Sharpe > 2.5,

Avg Trade > $75, and

a Win Rate > 65%.

We’ll come back to win rate in a second, as I think quantitatively it’s one of the two most important predictors of a system's strength. Systems generally digress into a balancing act of a few pairs of metrics — Win Rate vs Average Trade (A stop & target balancing act), and Max Loss/Fixed Stop vs Drawdown — I find that a low fixed stop generally increases drawdowns (by lowering win rate — see balancing act 1).

For those of you who aren’t following — let’s define win rate, and then I’ll show you where it ties into this build — as there are a few ways it can be measured. I tend to measure it was Winning Trades / Total Trades, but a lot of people measure it as more of a recall statistic and treat it as Winning Trades / Losing Trades, but I find the metric to have too many moving parts — when given a choice, I always choose the simplest form of expressing any problem.

So back toMoney Management — discipline incarnate for the quantitative trader.

If you haven’t noticed, I think of strategies in terms of Risk first — I always consider the downside and the worst case, and I build up from there. My typical money management tends to follow the same logic, as I prefer to use the most conservative money management algorithms I can find. I think there’s something to be said for ‘staying power’ in trading — my priority is making sure I’m still alive when my system gets to the right combination of events to rally.

Some of you will say this is overly negative — and I should focus on not needing to recover — but for those of you who have traded systematically for years know — all systems come with drawdowns — and the better the system the more difficult the drawdown always seems to be mentally.

The MM solution for me historically has been using Fixed Ratio, which uses a Delta value that allows you to protect your profits, and only add a contract when you’ve earned Delta amount ofprofits per contract— so if your delta is 50k, and you’re at 1 contract, you need 50K of profit to increase to 2, and then to get to 3 you need 100k (2x50k).

Here’s the formula, for reference.

N = .5 * SQRT(1 + 8*(ProfitPerContract/Delta)) + 1

OR in Python:

qty = .5 * (np.sqrt(1 + 8*(P/D)) + 1)

While this is a good foundational solution, I have always been interested in finding a way to utilize that key piece of the puzzle — Win Rate — into Money Management.

Maybe there’s a way we can increase position size for each direction, or even specific entry, as the entry or side proves its strength by a high win rate?

That was a bit wordy — simply put, let’s say your short entries are 9/10, and your long entries are 4/10 — maybe we should be putting most of our money behind the short entries until it begins to balance?

(An argument could be made that we should weigh the opposite, as the ratios should eventually approach their respective means — but this is an Efficiency MM system, not a Mean Reverting MM system! Might be fun to try on your own though?)

So what would this require in the strategy code? Obviously we need a way to count trades of each direction, which can simply be incremented with each entry — (and be mindful of scope, be sure to use a Class variable or Global, otherwise it will clear with the scope of the method).

So let’s do Globals as it’s simpler/more readable — I’ll add LONGS and SHORTS variables, initialize them at 0 (although it may be a good idea to set them at say 10, and initialize the WINS to 5 to start them even). These variables will count the directional trades, but if you have 10 different entry signals you can add global counts for each.

For each count (Denominator), we’ll create a LongWins (numerator), to calculate our respective WinPct variable — both should be globals or class vars as well.

For the placement, I put the globals up top by imports, however, how should we increment the Wins? I chose to do this by simply incrementing the ‘xWins’ Globals in my trailStop logic (right before it’s called — exiting a winning trade), but if you have a fixed target that works as well.

You could also go the opposite route and only track the Losses with fixed stop (and then make sure to calculate WinPct = (1-LongLosers).

I also have 2 logic-based exits — they exit after a series of lower lows / higher highs, but it’s not clear whether or not this is profitable. There are a few ways to handle this — you can make a call to determine the cost basis, thus open PnL just before it, or (for simplicity sake) I just incremented them by .5, considering them neutral in general.

Now that you have your counts set, and all the variables needed — it’s time to use them!

I created a method to take these values as inputs, and determine a proper Quantity for your respective entries. I’ve attached the code, but to clarify this is where you’ll be assigning win pct with WinPctLongs = LongWins / Longs.

Another key piece is to set a global for MAXQTY, or the full qty — which I just set to 100 for now. This is what your win pct will be taking a percentage of to determine the fixed quantity and make sure you’re returning an int (or round down a float — round(qty,0)) because there are no half shares.

To use the prior example, (9/10) shorts would now be trading 90 shares (.9 x MAXQTY) short for the next short entry.

While this MM system didn’t perform great on the basic example — mostly because it initially scaled it down to 1/100th of size (I would initialize each WinPct to 50, and double your initial QTY for testing MAXQTY to get comparable results) — I do think Dynamic MM methods like this can be practically used in conjunction with traditional MM Algos like Fixed Ratio; The goal is that the final product is greater than the sum of its parts.

Discipline cannot be taught in 6 lines of code.

But hopefully, with a bit of exploration, you can use this to develop the proper grit required by the market.

Happy Trading!

Disclaimer: The views, opinions, and information provided within this guest post are those of the author alone and do not represent those of QuantInsti®. The accuracy, completeness, and validity of any statements made or the links shared within this article are not guaranteed. We accept no liability for any errors, omissions or representations. Any liability with regards to infringement of intellectual property rights remains with them.

Files in the download:

mod_beg - Python code

Win_Rate_MM Jupyter Notebook

(In example codes, I have also included Fixed Ratio, code, and a method for tracking multiple instruments/strategies within one system with dictionaries)

Login to Download

---

*Imported from QuantInsti Blog on 2026-04-27*
