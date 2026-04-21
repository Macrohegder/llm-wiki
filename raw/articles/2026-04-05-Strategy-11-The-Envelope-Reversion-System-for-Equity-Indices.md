# Strategy #11: The Envelope Reversion System for Equity Indices

**原文链接**: https://algomatictrading.substack.com/p/strategy-11-the-envelope-reversion

**发布时间**: 2026-04-05

**抓取时间**: 2026-04-05 16:21:45

---

## 摘要

Strategy #11: The Envelope Reversion System for Equity Indices
Buy controlled dips. Sell into relief. Clean structure. Clear logic.
Algomatic Trading
Nov 16, 2025
∙ Paid
19
5
10
Share
Most of the time, markets don’t crash or skyrocket.
They oscillate.
They drift around a fair value and constantly pull back toward it.
This strategy is built to trade that move.
We don’t guess tops or bottoms.
We simply
step in
when price stretches too far away from its norm… and step out when it snaps back.
Simple to understand. Easy to automate. Surprisingly robust across decades.
The Problem…
Many traders try to catch every move the market makes. The result?
Chasing noise → Overtrading
Fixed sizing → Wrong exposure in wrong conditions
No clear exit → Profits evaporate
This strategy fixes that by defining:
...

---

## 全文

Strategy #11: The Envelope Reversion System for Equity Indices
Buy controlled dips. Sell into relief. Clean structure. Clear logic.
Algomatic Trading
Nov 16, 2025
∙ Paid
19
5
10
Share
Most of the time, markets don’t crash or skyrocket.
They oscillate.
They drift around a fair value and constantly pull back toward it.
This strategy is built to trade that move.
We don’t guess tops or bottoms.
We simply
step in
when price stretches too far away from its norm… and step out when it snaps back.
Simple to understand. Easy to automate. Surprisingly robust across decades.
The Problem…
Many traders try to catch every move the market makes. The result?
Chasing noise → Overtrading
Fixed sizing → Wrong exposure in wrong conditions
No clear exit → Profits evaporate
This strategy fixes that by defining:
Exactly when to enter
Exactly when to exit
How to avoid most bad conditions
No guesswork. No gut feelings.
Just clear signals.
Enjoying this post?
Free readers get ideas but paid members get the
full code
and access to my
complete premium strategy library
.
Subscribe
Strategy Overview
This system uses a
moving average
, and creates a small
envelope
around it, basically a soft upper and lower band.
When price
pulls back below the lower band
, while still
trending above the 200-day trend
, we buy.
When price
rebounds back above the upper band
, we exit.
If you want to run this yourself, you’ll find the full logic and code later in the post.
The Idea
We only buy pullbacks in an uptrend.
We only sell once price snaps back.
This avoids:
Buying into downtrends
Holding through prolonged selloffs
Overstaying rebounds
Three Key Principles
Trend Filter
: We only trade when price is above the 200-day moving average.
This keeps us aligned with the broader uptrend and filters out most bear markets.
Entry Trigger
: Enter when price dips below the lower envelope.
This signals short-term
fear
or
overreaction
within an otherwise healthy trend.
Exit Trigger
: Exit when price rallies back above the upper envelope.
This captures the mean-reversion rebound before momentum fades.
This captures short-term
fear flushes
inside
long-term uptrends
.
Backtest Setup
Markets:
SP500 (Futures)
Timeframe:
Daily (CET)
Sample Period:
2000–2025, including:
Dot-Com Collapse
GFC 2008
COVID Crash + Recovery
2022 Bear Cycle
Position Size:
Dynamic position size based on ATR
Starting Capital:
10000€
Costs:
Fixed 2 point spread included
Stop Loss:
Optional, system can be run without stoploss due to exit criteria and position sizing mechanic.
I would even say that most mean-reversion strategies should be run without stoploss.
Results & Metrics
This is the result after
142 trades
and
25 years
:
Win rate:
69%
Profit factor:
2.32
Max drawdown:
-13%
CAGR:
5.19%
Average hold:
10 Days 19 Hours
MAR Ratio:
0.4
Track This Strategy’s Real Performance
Want to see how this strategy (and all my others) are actually performing?
I’ve built a public tracker that shows the real returns of every strategy I’ve published.
👉
View the strategy tracker here
What you’ll see:
Year-to-date returns for all 10+ strategies
Total returns since published
Maximum drawdown per strategy
Win rates & MAR ratios
Live vs. paper trading status
Real numbers with correct spreads and commissions
No cherry-picking. No hiding the strategies that didn’t work. Updated monthly.
Why It Works
1. Mean Reversion of Flows
Markets tend to
overextend
on both sides.
Short-term panic selling is often followed by a relief.
2. Trend Alignment
We
only
trade in confirmed long-term uptrends.
This filters out most structural drawdowns.
3. Clear Exit Logic
We don’t hold for months and ride the whole trend.
We capture the
snapback
, the high-probability part and leave after around 10 days.
This is where discipline beats prediction.
Takeaways
Simplicity scales.
A clear, repeatable rule-set is easier to trust and stick to across market regimes.
Trade with the trend.
By only buying dips in established uptrends, we avoid most structural drawdowns and long grindy selloffs.
The exit is the edge.
Capturing the snapback is where the payoff happens.
We don’t overstay the rebound.
Let the setup come to you.
We don’t chase.
We wait for price to stretch away from its short-term mean,
then
act.
Small edges compound.
The goal isn’t to snipe the bottom, it’s to repeat a high-probability, high-clarity trade many times across years.
Now, you can try to reverse-engineer this system on your own… or you can fast-track the process, support my work, and access the full code + detailed walkthrough by becoming a paid member.
All strategies are built in ProRealTime, but logic and parameters can easily be ported to TradingView, Python, or other platforms.
The Full Code
This post is for paid subscribers
Subscribe
Already a paid subscriber?
Sign in

---

*由 Substack Strategy Tracker 自动抓取*
