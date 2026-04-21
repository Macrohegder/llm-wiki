# Strategy #16: Simple Divergence Strategy on Crude Oil

**发布时间**: Sun, 15 Mar 2026 08:01:56 GMT

**原文链接**: https://algomatictrading.substack.com/p/strategy-16-simple-divergence-strategy

**抓取时间**: 2026-04-06 09:00:27

---

## 摘要

Strategy #16: Simple Divergence Strategy on Crude Oil A simple RSI divergence system that turns crude oil’s extremes into rules-based opportunity. Algomatic Trading Mar 15, 2026 ∙ Paid 16 2 Share Crude oil has a way of making smart traders look foolish. It turns conviction into regret faster than almost any major market. One week it feels unstoppable. The next, it gaps against the crowd and leaves both bulls and bears wondering what just happened. That is exactly why I like it. Not because oil is easy. Because it is emotional. And emotional markets tend to create some of the best systematic opportunities. The Hypothesis Crude Oil is a momentum-driven market. It trends hard, reverses hard, and rarely moves gently. But underneath the price action, momentum tells a different story before pric...

---

## 全文

Strategy #16: Simple Divergence Strategy on Crude Oil
A simple RSI divergence system that turns crude oil’s extremes into rules-based opportunity.
Algomatic Trading
Mar 15, 2026
∙ Paid
16
2
Share
Crude oil has a way of making smart traders look foolish.
It turns conviction into regret faster than almost any major market. One week it feels unstoppable. The next, it gaps against the crowd and leaves both bulls and bears wondering what just happened.
That is exactly why I like it.
Not because oil is easy.
Because it is emotional.
And emotional markets tend to create some of the best systematic opportunities.
The Hypothesis
Crude Oil is a momentum-driven market. It trends hard, reverses hard, and rarely moves gently. But underneath the price action, momentum tells a different story before price does.
When WTI makes a higher high but RSI fails to confirm it, the buying pressure is quietly fading. The move is happening on less energy than it appears. That imbalance tends to resolve, not always immediately, but systematically over time.
The same principle works in reverse. A lower low in price paired with a higher low in RSI suggests sellers are running out of fuel. A bounce doesn’t require good news. It just requires exhaustion.
We’re identifying when the current move is losing conviction and positioning accordingly.
Strategy Overview
This is a dual-direction mean reversion strategy that trades WTI crude oil on the daily timeframe, both long and short. I actually made this strategy back in 2024 but haven’t touched it for more than 2 years, with the recent volatility in Oil I had to bring it back and take a look at how it performed since I made it. This strategy uses RSI divergence for both entry and exit signals, which is the unique twist here: the same framework that gets you in is also what gets you out.
This strategy also use a basic moving average trend filter: we only take longs when the trend is rising and shorts when it is falling. I hate extra parameters but that one extra layer makes a meaningful difference in signal quality.
Join 7,200+ traders learning systematic trading. Paid members get the full code and detailed walkthrough for this strategy below.
Subscribe
Why This Works
The entry works because we’re not just reacting to RSI levels, we’re reacting to disagreement between price and momentum. That disagreement is directional information that raw price action misses entirely.
The exit logic is what sets this version apart. Rather than using a fixed profit target or a time stop alone, the strategy waits for divergence to appear in the opposite direction. You entered on bullish divergence; you exit when bearish divergence shows up or after X amount of days, this time exit isn’t necessarily needed if you trade Futures but if you trade CFDs the overnight fee will usually eat a lot of profit if the trade is too slow.
Position sizing is dynamic, scaled using ATR relative to portfolio size. That means volatility is always accounted for, so a spike in crude oil volatility does not blow the position sizing out of proportion.
Backtest Setup (Jan 2000 - Mar 2026)
To evaluate the idea, the system is tested on:
Instrument:
US Crude Oil Futures
Direction:
Long and short
Timeframe:
Daily bars
Capital base:
€20.000 with volatility-adjusted sizing
Spread:
2.8p
This is not a high-frequency strategy and it is not trying to scalp noise. It is designed for traders who prefer
clean daily setups
, fewer decisions, and a system they can realistically follow manually, semi- or fully automated.
Results & Metrics
A note on the out-of-sample period: the strategy uses an OOS start date of January 2021, meaning everything from that point forward is genuine out-of-sample data.
CAGR:
5.7%
Maximum drawdown:
-9.19%
MAR Ratio:
0.56
Win rate:
69.59%
Profit factor:
1.97
Average gain per trade:
319€
WHAT’S BEHIND THE PAYWALL
The exact divergence parameters: the lookback, the RSI bounds, everything are behind the paywall. Paid members also get a line-by-line walkthrough of the code, so you can understand exactly what the strategy is doing and adapt it to your platform of choice.
Fifteen other fully coded, tested systems are already in the library. This one is a great piece alongside the existing mean reversion strategies.
Full Code & Detailed Walk-Through
This post is for paid subscribers
Subscribe
Already a paid subscriber?
Sign in

---

*由 Substack Strategy Tracker 自动抓取*
