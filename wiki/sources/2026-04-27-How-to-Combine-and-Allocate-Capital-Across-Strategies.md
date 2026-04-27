---
title: "How to Combine and Allocate Capital Across Strategies"
author: "SetupAlpha"
source: "Substack"
url: "https://setup4alpha.substack.com/p/how-to-combine-and-allocate-capital"
date: "2026-04-27"
topics: ["systematic-trading", "algorithmic-trading"]
---

# How to Combine and Allocate Capital Across Strategies

**来源**: [SetupAlpha](https://setup4alpha.substack.com/p/how-to-combine-and-allocate-capital)  
**日期**: 2026-04-27  
**作者**: SetupAlpha

---

## 摘要

How to Combine and Allocate Capital Across Strategies
Realtest codes
SetupAlpha
Apr 02, 2025
13
3
Share
Friends, today, we’re diving into something that might sound super technical but stick with me. I promise I’ll make it painless, maybe even fun. We’re talking about
combining multiple trading strategies and allocating capital smartly
.
Smart traders know that
no single strategy makes money every day.
The real edge comes from
combining uncorrelated strategies
and managing capital effectively.
Top traders, like
Rob Carver
, run
80 to 100 strategy variations
. Why? Because diversification within trading strategies reduces risk and
creates more consistent returns
.
In this guide, we'll cover
five proven allocation methods
, starting with the basics and moving toward more sophisticated approa...

---

## 原文

How to Combine and Allocate Capital Across Strategies
Realtest codes
SetupAlpha
Apr 02, 2025
13
3
Share
Friends, today, we’re diving into something that might sound super technical but stick with me. I promise I’ll make it painless, maybe even fun. We’re talking about
combining multiple trading strategies and allocating capital smartly
.
Smart traders know that
no single strategy makes money every day.
The real edge comes from
combining uncorrelated strategies
and managing capital effectively.
Top traders, like
Rob Carver
, run
80 to 100 strategy variations
. Why? Because diversification within trading strategies reduces risk and
creates more consistent returns
.
In this guide, we'll cover
five proven allocation methods
, starting with the basics and moving toward more sophisticated approaches. I’ll also break down the
real challenges
of each method and how to work around them.
By the end, you'll have
practical, ready-to-use methods
for optimizing how capital flows between your trading strategies.
Every example we discuss comes with a RealTest example code
, so you can see exactly how it's done in action.
Why Are We Talking About Strategy Allocation?
In my last video, I showed you how to build a
short-side mean reversion strategy
and that wasn’t random. The key to maximizing returns isn’t just running
more
strategies. It’s about running
uncorrelated
strategies.
If your strategies are too similar, combining them can actually
hurt
your performance instead of improving it. Here’s an example:
If two strategies have
10% correlation
, then even if you have
1,000 strategies
, they only behave like
100 independent ones
.
The lower the correlation, the
more powerful
your portfolio of strategies becomes.
Today, we’re combining a
short-side mean reversion strategy
with a
long-side mean reversion strategy
to test different ways of allocating capital between them.
Step 1: Combining Multiple Strategies (The Right Way)
First things first, we need to
merge multiple strategies
into a single trading system.
RealTest gives us a few ways to do this, but today we’ll use the approach where we
combine multiple strategies into a new file
.
Here’s how it works:
Step 1:
Copy your
short-selling strategy
into a new file.
Step 2:
Copy your
long mean reversion strategy
into the same file.
Step 3:
Make sure both strategies don’t use the same function names
, if they do, they’ll overwrite each other and cause errors.
Now we have
two strategies running together in one system
.
Allocation: Who Gets What?
Now that our strategies are happily cohabiting in one file, we need to figure out how to distribute our precious capital between them. Let’s dive into a few different methods.
Method #1: Equal Weighting
This one’s
as simple as it gets
: split the money evenly across all strategies.
2 strategies? Each gets
50%
of the capital.
4 strategies? Each gets
25%
of the capital.
10 strategies? Each gets… well, you get the idea.
// Realtest code
Quantity: 	50 / positions
QtyType: 	Percent
It’s
easy, avoids overfitting
, and works best when all strategies have similar risk/reward profiles. But it
doesn’t
take into account market conditions or performance differences.
Take a moment and click subscribe!
Subscribe
Method #2: Volatility-Based Allocation
Markets can be calm and boring or wild and chaotic, so why treat all strategies the same?
When the
VIX (volatility index) is high (above 20)
→
allocate more to short-selling strategies
(because they usually thrive in panicky markets).
When the
VIX is low
→
favor long strategies
(since calmer markets are better for trend follow plays).
// Realtest code
Quantity: 	if(extern($$vix,c>20),50,100) / positions
QtyType: 	Percent
It’s a simple way to adjust based on market conditions and protect capital when things get crazy.
Method #3: Trend-Based Allocation (Riding the S&P 500 Wave)
Here, we use an
S&P 500 trend filter
to decide where the money goes:
If the
S&P is in a downtrend
→ More money to
short
strategies.
If the
S&P is in an uptrend
→ More money to
long
strategies.
// Realtest code
Quantity: 	if(extern($SPY,c>Avg(c,200)),100,50) / positions
QtyType: 	Percent
We’ll define a downtrend as the
S&P trading below its 200-day moving average
. The downside? It might miss early recoveries (because trend signals lag), but it helps avoid huge drawdowns.
Are you using Realtest?
We handle the
research, coding, and testing
, so you can focus on
growing your portfolio
. ⬇️
Our Realtest Strategies
Method #4: Performance-Based Allocation
What if we just
give more money to the strategies that are actually working
?
Enter the
Sharpe ratio
- a measure of risk-adjusted performance.
If a strategy has a
Sharpe ratio of 2.0 over the last 20 days
→ It gets more capital.
If it’s performing worse → We reduce its allocation.
// Realtest code
TestData:
	lookback180:	20 // change lenght
	ccc:	        Extern(@MY_STRATEGY_NAME,S.Equity)
	dailyReturn:	(ccc - ccc[1]) / ccc[1]
	mean180:	avg(dailyReturn, lookback180)
	stdDev180:	stddev(dailyReturn, lookback180) * sqr(lookback180) 
	riskFreeRate:	Extern(@MY_STRATEGY_NAME,S.RiskFreeRate)
	sharpe180:	(mean180 * 365 - riskFreeRate) / stdDev180

Strategy: MY_STRATEGY_NAME
       Quantity: 	if(extern($SPY,c>Avg(c,200)),100,50) / positions
       QtyType: 	Percent
This method
rewards winners
but be careful, it can lead to
overfitting
if you keep adjusting too frequently.
Method #5: Moving Average on Your Equity Curve
Compare your
strategy’s equity curve
to a
20-day moving average
.
If the equity is
above
the moving average → The strategy is
doing well
, so we give it
more money
.
If it’s
below
→ We
scale back
the allocation.
// Realtest code
Quantity: 	if(extern(@MY_STRATEGY_NAME, S.Equity>Avg(S.Equity,200)),80,50) / positions
QtyType: 	Percent
A simple way to let momentum dictate how much weight each strategy gets.
Final Boss Move: Combining All These Methods
If you want to be extra fancy, you can
mix and match
these allocation strategies.
Example:
Check if the S&P is above its 50-day moving average
(if yes, full weight; if no, reduce weight).
Check if VIX is below 20
(low volatility = full weight; high volatility = cut it to 0.5).
Check if the equity curve is above its 20-day moving average
(if yes, full weight; if no, reduce it).
TestData:
    Trend1:      if(extern($SPY,c>Avg(c,50)),1,0)
    Volatility:  if(extern($$vix,c<20),1,0.5)
    Performance: if(Extern(@MY_STRATEGY_NAME, S.Equity < avg(S.Equity,20)),1,0.7)

Strategy: MY_STRATEGY_NAME
    Quantity:    ((Trend1 + Volatility + Performance) / 3 * 100) / positions
    QtyType:     Percent
Final allocation?
An average of these three factors, scaled to a percentage.
It’s
dynamic
, adjusts with market conditions, and reduces reliance on any single method. But yeah, it’s more complex to manage.
Try It Out & Let Me Know What You Think!
There you have it. Multiple ways to allocate capital
without overcomplicating things
. Try these methods yourself, mix and match, and see what works for you!
If all this sounds like
way too much work
and you’d rather skip the research, debugging, and coding, we’ve got you covered. We have
ready-made strategies
, including the ones in this article’s tutorial video, available for download. Saves you time, stress, and a few headaches.
Let me know if you have any questions. I’m always happy to help!
About Us
We build high-performance trading strategies based on academic research, rigorously tested in real market conditions, not just theory.
✅
Ready-to-use, fully automated
✅
Survivorship & lookahead bias-free
✅
Built on real data with trading costs included
❌
No “holy grail” strategies
For
three years
, we’ve run a
fully automated portfolio of 20+ strategies
. Now, we’re sharing the few ideas that actually work.
Check those published realtest strategies here.
Subscribe Now!
Subscribe
13
3
Share

---

*由 Substack Strategy Tracker 自动抓取*

---

*Imported from Substack on 2026-04-27*
