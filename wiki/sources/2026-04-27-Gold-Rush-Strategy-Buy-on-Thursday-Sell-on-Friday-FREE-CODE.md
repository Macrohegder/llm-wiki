---
title: "Gold Rush Strategy (Buy on Thursday & Sell on Friday) [FREE CODE]"
author: "SetupAlpha"
source: "Substack"
url: "https://setup4alpha.substack.com/p/gold-rush-strategy-buy-on-thursday-realtest-backtest"
date: "2026-04-27"
topics: ["systematic-trading", "algorithmic-trading"]
---

# Gold Rush Strategy (Buy on Thursday & Sell on Friday) [FREE CODE]

**来源**: [SetupAlpha](https://setup4alpha.substack.com/p/gold-rush-strategy-buy-on-thursday-realtest-backtest)  
**日期**: 2026-04-27  
**作者**: SetupAlpha

---

## 摘要

Gold Rush Strategy (Buy on Thursday & Sell on Friday) [FREE CODE]
Buy gold every Thursday evening and keep the position for 24 hours. (Step-by-step)
SetupAlpha
Aug 06, 2025
9
3
Share
“Buy gold on Thursday, sell on Friday.”
Sounds like one of those trading myths from a shady forum thread, right?
Turns out, this 24-hour XAUUSD trade (a relic from the MetaTrader 4 days) might still have real edge. No indicators and filters. Just a recurring time-based setup.
If you’re curious how this works and how to code it in RealTest I’ll walk you through it step by step.
Before we start, who we are?
AlphaSetup offers RealTest trading & investing strategies crafted from academic research papers. Ready-to-use, market-tested, and built for real results. Go check it out now  -
https://setupalpha.com/
Step 1:...

---

## 原文

Gold Rush Strategy (Buy on Thursday & Sell on Friday) [FREE CODE]
Buy gold every Thursday evening and keep the position for 24 hours. (Step-by-step)
SetupAlpha
Aug 06, 2025
9
3
Share
“Buy gold on Thursday, sell on Friday.”
Sounds like one of those trading myths from a shady forum thread, right?
Turns out, this 24-hour XAUUSD trade (a relic from the MetaTrader 4 days) might still have real edge. No indicators and filters. Just a recurring time-based setup.
If you’re curious how this works and how to code it in RealTest I’ll walk you through it step by step.
Before we start, who we are?
AlphaSetup offers RealTest trading & investing strategies crafted from academic research papers. Ready-to-use, market-tested, and built for real results. Go check it out now  -
https://setupalpha.com/
Step 1: What Is the “Gold Rush” Strategy?
At its core, it's absurdly simple:
Buy
gold (XAUUSD) on
Thursday’s close
Sell
on
Friday’s close
No indicators. No price filters. Just time.
I started systematic trading around 2009, and if you were around then, you know MetaTrader 4 and MQL4 were everywhere.
And yes, it actually comes from the MT4 era, when people coded this into EAs using MQL4. It was floating around forums in the late 2009s when I got into system trading.
So now, I wanted to test it in RealTest to see if this time-based edge still holds up with 2025 data.
Step 2: Set Up the Backtest Environment
We’re using
Norgate data
.
Here’s how to start:
This gives us clean gold data, and we also import
SPY
as a benchmark to compare our strategy performance.
Then, configure the backtest:
We’re testing from 2000 onward because gold was basically untradable (but investable) before that. Liquidity was terrible. You’ll see this clearly when you chart it.
Step 3: Define Your Entry Logic
This is the beauty of the whole thing the logic is so simple.
In RealTest:
DayOfWeek = 4
means
Thursday
We filter for
XAUUSD
only
No price condition, no filters that’s it
Step 4: Define the Strategy
Now for the actual trade logic:
Let’s break that down:
EntrySetup
: Uses our
Buy
signal (from Data section)
Side
: We’re only going long
Quantity
: 100
QtyType
: Uses
percent
of account (100%)
EntryLimit: Close, t
his avoids slippage by entering on a
limit order at close
ExitTime: NextClose
: Exits on
Friday close
Commission
: I haven’t researched forex broker commission fees.
But let’s use Interactive Brokers’ stock fees for now. Just to have something in place.
You could experiment with size, position limits, and filters later.
Step 5: Add a Benchmark
Always compare against something:
This lets you see whether your 1-trade-a-week system actually does anything versus just buying SPY and walking away.
Step 6: Run the Test and Evaluate Results
Once you hit
Test
, here’s what you might notice:
The
Sharpe ratio is solid
Drawdowns are shallow
very manageable
Equity curve
has periods of stagnation, but also solid recoveries
There is a weak spot
pre-2000
which makes sense. Back then, gold was thinly traded and FX spreads were awful. After 2000, things normalize.
Step 9: Test It With Your Own Data
Want to try it? You can free download the RealTest code here or write it from scratch using the snippets above.
It’s great as a learning exercise if you're new to RealTest, or a low-effort alpha idea if you’re already running more complex portfolios.
You can even tweak it:
Add volatility filters
Restrict it to high-liquidity weeks
Overlay economic calendar events
Integrate it into your own strategy or portfolio to diversify.
Speaking of diversification, we just launched a new, highly requested portfolio combination tool. It shows all our strategies, performance, Sharpe ratios, and more.
But I’ll talk more about this portfolio maker in a future but
you can use this now!
What This Strategy Tells Us
The biggest lesson here isn’t about gold.
It’s about
simplicity
.
In a world full of over-optimized, curve-fitted garbage, this strategy shows that
a dumb idea that survives 20+ years of market data might be smarter than you think.
Final Thoughts
Will this make you rich? I don’t know.
But:
It’s
easy to automate
It’s
cheap to run
It’s
uncorrelated
Add it to your RealTest playbook. Try running it live or paper trading it alongside your main systems.
You might be surprised.
👇 Ready to Try It?
✅ Free Download the RealTest code
HERE
👇 Subscribe for Alpha! 👇
Subscribe
9
3
Share

---

*由 Substack Strategy Tracker 自动抓取*

---

*Imported from Substack on 2026-04-27*
