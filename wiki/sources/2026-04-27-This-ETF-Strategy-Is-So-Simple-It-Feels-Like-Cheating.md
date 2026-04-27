---
title: "This ETF Strategy Is So Simple It Feels Like Cheating"
author: "SetupAlpha"
source: "Substack"
url: "https://setup4alpha.substack.com/p/this-etf-strategy-is-so-simple-it"
date: "2026-04-27"
topics: ["systematic-trading", "algorithmic-trading"]
---

# This ETF Strategy Is So Simple It Feels Like Cheating

**来源**: [SetupAlpha](https://setup4alpha.substack.com/p/this-etf-strategy-is-so-simple-it)  
**日期**: 2026-04-27  
**作者**: SetupAlpha

---

## 摘要

This ETF Strategy Is So Simple It Feels Like Cheating
SPY & QQQ system that reduces drawdown and smooths returns. (Realtest & Tradingview.)
SetupAlpha
Apr 14, 2025
32
2
7
Share
We’re Really Happy to Share This With You
We’ve been testing and using this strategy ourselves, and it’s one of those rare setups that
just makes sense
.
In this post, I’ll walk through a straightforward trading system built using just two ETFs:
SPY
and
QQQ
.
What You’ll Get (and How You Can Use It)
This strategy is built to be portable and easy to implement, no matter what tools you’re using.
Here’s exactly what you’ll get:
✅
RealTest strategy file
– fully written, just open it and run the backtest
✅
TradingView version
– includes both the indicator and the strategy script with alerts, so you can use it live or vis...

---

## 原文

This ETF Strategy Is So Simple It Feels Like Cheating
SPY & QQQ system that reduces drawdown and smooths returns. (Realtest & Tradingview.)
SetupAlpha
Apr 14, 2025
32
2
7
Share
We’re Really Happy to Share This With You
We’ve been testing and using this strategy ourselves, and it’s one of those rare setups that
just makes sense
.
In this post, I’ll walk through a straightforward trading system built using just two ETFs:
SPY
and
QQQ
.
What You’ll Get (and How You Can Use It)
This strategy is built to be portable and easy to implement, no matter what tools you’re using.
Here’s exactly what you’ll get:
✅
RealTest strategy file
– fully written, just open it and run the backtest
✅
TradingView version
– includes both the indicator and the strategy script with alerts, so you can use it live or visually backtest it
✅
Python breakdown
– the entire strategy logic explained step-by-step, so you can rebuild it yourself in any custom setup
You don’t need to guess or reverse-engineer anything.
Download link is here.
The Core Idea
We’re combining two very different approaches:
SPY
: buy-and-hold
QQQ
: mean reversion
These two strategies don’t overlap in behavior, which is exactly why they work well together.
When you put them side-by-side in one portfolio, they balance each other out in a way that improves the overall equity curve smoother, less volatile, and easier to stick with during difficult periods.
Subscribe if you enjoy academic research based strategies.
Subscribe
Why SPY + QQQ?
SPY
represents broad market exposure. It tends to trend gradually upward over time.
QQQ
, being more tech-heavy, often shows stronger mean reversion behavior sharp dips followed by quick recoveries.
When you apply a basic mean reversion strategy to QQQ (something like buying after short-term oversold conditions), and hold SPY in the background, the result is a system where one side can often offset the other during tough periods.
For example:
If QQQ is in a quiet phase (no signals), SPY continues to grow.
If SPY experiences a pullback, QQQ may trigger a buy and recover quickly.
This creates a natural hedge effect.
Details on the Strategies
SPY Logic:
Simply hold the position continuously.
Optionally, rebalance monthly to maintain a clean portfolio structure.
QQQ Logic:
Wait for a short-term oversold condition (e.g., price below a moving average or a specific % drop).
Enter long trades when that condition triggers.
Exit after a small bounce or when the mean reversion signal resolves.
Note: In our backtest, the QQQ logic uses basic mean reversion rules that are intentionally kept simple for clarity and adaptability.
Backtest Setup
We used
RealTest
for the core testing.
Slippage
was included to better reflect real-world trading.
No commissions on ETFs in IBKR.
All trades were executed using daily close prices, no intraday data used.
BLUE = Our Strategy
YELLOW = SPY Buy & Hold
But now I rebalance SPY monthly.
This is beautiful.
Why It Matters
This system isn’t trying to predict the market or beat every benchmark.
Its strength comes from:
Using clean, easy-to-follow logic.
Combining two uncorrelated approaches. (0.18)
Reducing drawdowns through diversification in strategy behavior not just in assets.
That last point is important. Diversifying by logic often helps more than diversifying by symbols. Many strategies fall apart in live trading because they rely on one type of market behavior. This one handles different phases reasonably well without needing to constantly switch tactics.
We explored the importance of diversification in depth in one of our latest research articles.
How to Combine and Allocate Capital Across Strategies
SetupAlpha
·
April 2, 2025
Read full story
Want to Try It?
You can download everything here: ⬇️
Full RealTest code .rts
The TradingView indicator and strategy
Full Python rules for manual rebuild
📥
Download the files here
(+ more detailed stats)
🐰The Easter Sale is live,
30% OFF
everything. Use code
EASTER30
on checkout. Ends Sunday.
If you have questions about the logic, implementation, or backtest design, just reply or comment. Happy to go deeper into any part of it.
More: https://setupalpha.com/
Subscribe
32
2
7
Share

---

*由 Substack Strategy Tracker 自动抓取*

---

*Imported from Substack on 2026-04-27*
