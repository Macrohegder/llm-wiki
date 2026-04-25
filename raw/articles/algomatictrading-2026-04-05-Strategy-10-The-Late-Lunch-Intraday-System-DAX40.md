# Strategy #10: The Late Lunch Intraday System (DAX40)

**原文链接**: https://algomatictrading.substack.com/p/strategy-10-the-late-lunch-intraday

**发布时间**: 2026-04-05

**抓取时间**: 2026-04-05 16:21:34

---

## 摘要

Strategy #10: The Late Lunch Intraday System (DAX40)
Calm mid-day trends. Fixed risk. Simple timing.
Algomatic Trading
Oct 19, 2025
∙ Paid
14
4
Share
Most traders think all the action happens at the open.
But some of the most stable intraday trends unfold quietly, when the morning noise fades and liquidity returns.
This is what I call the
Late Lunch System
, a clean, intraday approach that rides mid-day directional moves with fixed ATR-based risk sizing.
No prediction. No chasing breakouts. Just structured exposure inside a narrow time window.
The Problem…
Most intraday traders burn out fast.
They scalp noise, over-leverage small moves, and end up feeding spreads instead of compounding returns.
Common pitfalls:
Overtrading:
Sitting through the open and reacting to every tick.
Unscaled risk...

---

## 全文

Strategy #10: The Late Lunch Intraday System (DAX40)
Calm mid-day trends. Fixed risk. Simple timing.
Algomatic Trading
Oct 19, 2025
∙ Paid
14
4
Share
Most traders think all the action happens at the open.
But some of the most stable intraday trends unfold quietly, when the morning noise fades and liquidity returns.
This is what I call the
Late Lunch System
, a clean, intraday approach that rides mid-day directional moves with fixed ATR-based risk sizing.
No prediction. No chasing breakouts. Just structured exposure inside a narrow time window.
The Problem…
Most intraday traders burn out fast.
They scalp noise, over-leverage small moves, and end up feeding spreads instead of compounding returns.
Common pitfalls:
Overtrading:
Sitting through the open and reacting to every tick.
Unscaled risk:
Taking identical position sizes in 10-point and 50-point volatility regimes.
Emotional exits:
Closing trades early or late because there’s no predefined structure.
This system solves all three, with very few lines of code.
In just a few hours,
Strategy #9: The 5-Day Mean-Reversion System
will move into the
Premium Vault
.
If you’ve been thinking about testing it, this is your final chance, it’s still available for
Monthly
and
Annual paid members
until the switch.
After that, only
Premium / Founder
members will have full access to it inside the complete
Algomatic Strategy Library
.
Upgrade now to secure
Strategy #9
, this new
Late Lunch System
, and early access to future releases before they become Premium-only.
Enjoying this post?
Free readers get ideas but paid members get the
full code
and access to my
complete premium strategy library
.
Subscribe
Strategy Overview
The “Late Lunch System” focuses on one small intraday trend window, trading
only when
the market structure supports continuation.
It combines three key components:
A clear timing filter:
This avoids the morning volatility cluster and positions for the smoother mid-day trend.
A directional bias:
This single rule keeps us aligned with the prevailing micro-trend.
A fixed ATR-based position size:
Every trade risks the same percentage of portfolio equity relative to current volatility, maintaining consistent exposure across sessions.
No overnight exposure, no surprises.
Simple. Clean. Repeatable.
Backtest Setup
Market:
DAX (CFDs & Futures)
Timeframe:
30-min bars
Sample period:
2006–2025
Costs:
2-point spread included
Results & Metrics
Win rate:
55%
Profit factor:
1.19
Max drawdown:
-10.4%
CAGR:
4.7%
Average trade duration:
~11 hours (same-day)
MAR ratio:
0.45
These numbers may look modest, but that’s the point.
It’s a
steady intraday edge
designed to complement mean-reversion and swing systems, not replace them.
Why It Works
Intraday structure:
The intraday window often captures secondary directional pushes as liquidity shifts from Europe toward the U.S. session.
Volatility scaling:
Using ATR from daily bars ensures the same dollar risk per trade, regardless of market regime.
No overnight risk:
Trades are closed before the session ends, removing gap exposure entirely.
Discipline by design:
By limiting trading hours and enforcing a fixed exit, emotional interference is minimized.
It’s not about calling the next breakout, it’s about
being present
for a statistically favorable slice of the day.
Code & Logic
Here’s the complete code used for this system:
This post is for subscribers in the Premium Member  plan
Upgrade to Premium Member
Already in the Premium Member  plan?
Sign in

---

*由 Substack Strategy Tracker 自动抓取*
