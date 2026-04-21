# Portfolio #4: Three Markets, Four Behaviors

**原文链接**: https://algomatictrading.substack.com/p/portfolio-4-three-markets-four-behaviors

**发布时间**: 2026-04-05

**抓取时间**: 2026-04-05 16:21:54

---

## 摘要

Portfolio #4: Three Markets, Four Behaviors
How uncorrelated market structures create a smoother and more resilient compounding curve.
Algomatic Trading
Dec 07, 2025
16
1
5
Share
A mean-reversion system thrives in chop…
until volatility expands and every dip keeps dipping.
A trend strategy prints steady gains…
until the trend goes flat for a year.
Index-focused systems work…
until equities enter a sideways grind.
This is the reality of systematic trading:
Every edge is cyclical and every system eventually breaks.
Professionals don’t bet on which edge will work next.
They build portfolios where
multiple, independent behaviors
are operating at all times.
This portfolio follows that exact principle.
It blends four systems across
NASDAQ100, GOLD, and DAX
, each with its own behavioral niche an...

---

## 全文

Portfolio #4: Three Markets, Four Behaviors
How uncorrelated market structures create a smoother and more resilient compounding curve.
Algomatic Trading
Dec 07, 2025
16
1
5
Share
A mean-reversion system thrives in chop…
until volatility expands and every dip keeps dipping.
A trend strategy prints steady gains…
until the trend goes flat for a year.
Index-focused systems work…
until equities enter a sideways grind.
This is the reality of systematic trading:
Every edge is cyclical and every system eventually breaks.
Professionals don’t bet on which edge will work next.
They build portfolios where
multiple, independent behaviors
are operating at all times.
This portfolio follows that exact principle.
It blends four systems across
NASDAQ100, GOLD, and DAX
, each with its own behavioral niche and volatility profile.
In this post, you’ll see
why this combination works
, how the systems hedge each other, and why the portfolio becomes stronger than the individual parts.
Portfolio Logic
This portfolio is built around one simple objective:
combine behaviors that rarely peak or fail at the same time.
Instead of stacking similar systems on the same index, we deliberately mix:
Weekly sentiment reversals
Deep-dip mean reversion
Trend-following on commodities
Regime-independent pullback trading in European equities
This creates an equity curve with fewer dead periods and smaller correlated drawdowns.
Enjoying this post?
Free readers get ideas but paid members get the
full code
and access to my
complete premium strategy library
.
Subscribe
Included Systems
1.
Strategy #13: Turnaround Tuesday — NASDAQ100
A rule-based reversal system on the 1H timeframe.
Captures sentiment extremes at the beginning of the week.
Best in oversold, emotionally driven markets.
2.
Strategy #6: LC2RSI — NASDAQ100 (Daily)
Short-term mean-reversion using micro-exhaustion signals.
Enters deep dips in strong uptrends, exits on quick rebounds.
Strongest in range-bound, noisy markets.
3.
Strategy #8: Donchian Trend — GOLD (Daily)
A simple trend system based on Donchian channel.
Excellent during trending commodity cycles, inflationary periods, and macro-driven flows.
Weakness in equities often coincides with strength here.
4.
Strategy #12: DAX Mean Reversion — DAX (Daily)
A simple, robust mean-reversion strategy with volatility-aware sizing and structural confirmation.
Balances the NASDAQ systems by trading a completely different market personality, the german stock index DAX40.
Each system has its own “job,” and the portfolio works because they
rarely struggle at the same time.
Why It Works
Market Structure Diversification
NASDAQ - GOLD - DAX.
Their underlying drivers: macro, flows, volatility regimes are fundamentally different.
Behavioral Diversification
Reversals, micro-dips, structural trends, and multi-day pullbacks all express
different behaviours
.
Asynchronous Triggering
Signals don’t cluster.
One system might fire once a week, another twice a month.
Less overlap means cleaner risk distribution.
Volatility-Scaled Position Sizing
All systems use ATR-based sizing, ensuring:
Controlled risk per trade
No oversized bets
Smooth capital allocation over time
Portfolio Performance (2006–2025)
Portfolio Metrics:
(starting capital 20,000€)
CAGR:
10.0%
MAR Ratio:
1.63
Win Rate:
66.9%
Gain/Loss Ratio:
1.77
Profit:
113,509€
Trades:
1,065
Max Drawdown:
–4,486€ (-6,1%)
Max DD Duration:
398 days
Average DD Duration:
83 days
Interpretation
Each individual system produces a modest
3–6% CAGR
, but their equity curves are noisy and regime-dependent.
When combined, they generate a
stable 9–10% CAGR
with a
balanced drawdown profile
and improved recovery times.
This is the core principle of systematic portfolio engineering:
Edges that seem ordinary on their own can become extraordinary when they do not correlate.
None of these results come from optimization, only from thoughtful diversification.
Portfolio Behavior in Practice
The portfolio’s equity curve is smoother, more stable, and far less dependent on single-market conditions.
When NASDAQ mean-reversion has stagnant periods, GOLD trends pick up.
When GOLD chops, DAX mean reversion shows strength.
When nothing trends, Turnaround Tuesday keeps generating low-frequency, high-quality signals.
When volatility spikes, ATR-based sizing naturally contracts exposure.
The result is
controlled drawdowns and fewer long stagnant periods
, which makes the portfolio psychologically executable in real life.
Key Takeaways
Diversification is about behavior, not quantity.
Timeframes are less important than structural uncorrelation.
ATR-based sizing creates natural regime adaptation.
Multiple small edges > One large but fragile edge.
The best portfolios feel stable, not exciting.
What’s Next
Premium members will receive:
The new DAX Daily Mean-Reversion Strategy (
coming next week)
Full code, explanation and breakdown.
You’ll also get access to:
All previous premium strategies
The complete portfolio library
The position sizing framework
Upcoming systems
👉
Upgrade to Premium
to unlock every system and build your own professional-grade strategy portfolio.
Included Strategies
Strategy #8: The Easiest Trend System You’ll Ever Trade (Donchian Channel Breakout)
Algomatic Trading
·
September 5, 2025
Read full story
LC2RSI — NASDAQ100 (accessible on my website only)
Deep-dip mean reversion in strong uptrends.
Turnaround Tuesday — NASDAQ100
Weekly reversal exploiting sentiment patterns.
DAX Mean Reversion — DAX
A clean, volatility-scaled pullback strategy.
Premium includes full code for each system except the LC2RSI which can be accessed on my website.
Thank you for your support!
Disclaimer:
I am not a financial advisor and I don’t recommend you to trade my strategies. This article is for informational and educational purposes only. Trading involves risk, and you can lose money. Always do your own research.
16
1
5
Share

---

*由 Substack Strategy Tracker 自动抓取*
