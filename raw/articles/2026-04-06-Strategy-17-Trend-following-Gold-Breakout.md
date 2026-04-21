# Strategy #17: Trend-following Gold Breakout

**发布时间**: Sun, 05 Apr 2026 07:30:59 GMT

**原文链接**: https://algomatictrading.substack.com/p/strategy-17-trend-following-gold

**抓取时间**: 2026-04-06 09:00:18

---

## 摘要

Strategy #17: Trend-following Gold Breakout Trend-following gold with one rule: don't fight the direction. Algomatic Trading Apr 05, 2026 ∙ Paid 6 2 Share Ever wonder why most traders miss the big gold moves? They’re either too early, too cautious or watching the wrong signal altogether. What if there was a way to only enter when gold is already proving itself, when momentum is real, not just noise? This post breaks down TF Gold Breakout , a trend-following system built specifically for the gold market. It’s been running out-of-sample since late 2024 and the logic behind it is extremely simple. Earlier this year I made an announcement that I would release 3 strategies that I have traded live for years, this is the 3rd of those strategies. The other two strategies can be found here: Strateg...

---

## 全文

Strategy #17: Trend-following Gold Breakout
Trend-following gold with one rule: don't fight the direction.
Algomatic Trading
Apr 05, 2026
∙ Paid
6
2
Share
Ever wonder why most traders miss the big gold moves?
They’re either too early, too cautious or watching the wrong signal altogether.
What if there was a way to only enter when gold is already proving itself, when momentum is real, not just noise?
This post breaks down
TF Gold Breakout
, a trend-following system built specifically for the gold market. It’s been running out-of-sample since late 2024 and the logic behind it is extremely simple.
Earlier this year I made an announcement that I would release 3 strategies that I have traded live for years, this is the 3rd of those strategies.
The other two strategies can be found here:
Strategy #14: The 3 Down Daily Pullback Strategy
Algomatic Trading
·
Feb 1
Read full story
Strategy #6: My take on Larry Connors 2RSI System (Updated with code)
Algomatic Trading
·
July 13, 2025
Read full story
The Hypothesis
Gold is a momentum market. When it trends, it tends to trend hard driven by macro uncertainty, inflation fears, and institutional flows that don’t reverse overnight.
The idea here is straightforward: wait for the market to confirm it’s in an uptrend across multiple timeframes, then enter only when price is breaking to new highs. You’re not predicting anything. You’re simply following.
This type of breakout entry filters out a lot of the choppy, sideways noise that kills trend-following systems in other markets. Gold has a behavioural tendency to establish ranges and then break violently and this strategy is designed to catch exactly that.
Strategy Overview
TF Gold Breakout is a
long-only, daily trend-following breakout strategy
. It uses a layered moving average filter to confirm the trend is intact, then enters on a price breakout only when the market is effectively proving it wants to go higher.
Position sizing is dynamic, scaled to volatility, which means the system naturally takes smaller bets when gold is wild and larger ones when conditions are calm.
Join 7,300+ traders learning systematic trading. Premium members get the full code and detailed walkthrough for this strategy below.
Subscribe
Why It Works
The layered moving average structure acts as a trend quality filter. You’re not just asking “is price above a moving average?” you’re asking whether the trend has depth and consistency across multiple smoothing layers. That’s a meaningful difference.
The breakout entry adds a timing edge: you’re not buying into a trend early (and suffering through consolidations). You’re waiting for the market to
confirm
continuation.
The exit matters a lot, it steps aside when price starts showing weakness by falling to recent lows. Simply following the market’s own signals.
And the ATR-based position sizing? That’s what keeps this strategy alive during volatile regimes. It’s one of the most underrated risk tools in systematic trading.
A Common Mistake With This Type of Strategy
The biggest trap traders fall into with trend-following breakout systems is
over-optimising the lookback periods
.
It’s tempting. You see the equity curve improve if you tweak the breakout window by one bar or nudge the moving average period slightly. But every tweak you make to fit the past is one step further from a system that works in the future.
With TF Gold Breakout, the parameters were kept deliberately simple. Not because they’re the “best” numbers but because simple, robust parameters survive regime changes. Overfitted systems die the moment the market stops cooperating.
When in doubt: fewer parameters, rounder numbers, more robustness.
Backtest Setup
Market:
Gold (Spot / Futures)
Instrument:
Gold Futures
Platform:
ProRealTime
Timeframe:
Daily
Timezone:
CET
Backtest Period:
Jan 2000 - April 2026
Spreads:
0.3p Spread (Standard IG Market spread)
Backtest Results
Total Gain:
57 220$
Average Gain per Trade:
330$
Total Trades:
173
Winrate:
44.50%
Max Drawdown:
15.69%
Risk/Reward Ratio:
2.37
Time in Market:
19%
Average Trade Duration:
7 Days 12 Hours
CAGR:
5.13%
MAR Ratio: 0.32
One honest observation: this is a
long-only system
. That means it sits out almost entirely during gold bear phases. The time-in-market figure reflects that, this strategy is selective, not active. That’s a feature, not a bug.
What Surprised Me
The thing that genuinely caught my attention was how well the
dynamic position sizing held up during volatile periods
when gold was making historic moves.
Most fixed-size systems either got crushed by volatility or missed the big runs because they sized too small. The ATR-based sizing here naturally increased exposure during calm trending phases and pulled back when things got noisy. It’s a simple mechanic, but watching it work in live conditions is a different thing from just seeing it on a backtest chart.
Sometimes the oldest tools really are the best ones. At least the most robust ones.
How To Get This Strategy
Premium members get the
full ProRealTime code
below including the complete entry logic, exit conditions and the dynamic ATR-based position sizing formula.
If you’re serious about building a portfolio of systematic strategies, the full database (17 strategies and growing) is available to premium members. More strategies are coming soon.
ProRealTime Code + Parameter Description
[Full strategy code, available to premium subscribers]
Includes: trend filter logic, breakout entry, low-based exit, ATR stop loss and dynamic position sizing.
This post is for subscribers in the Premium Member  plan
Upgrade to Premium Member
Already in the Premium Member  plan?
Sign in

---

*由 Substack Strategy Tracker 自动抓取*
