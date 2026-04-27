# 7 Rules to Change Your Systematic Trading in 7 Months

**发布时间**: Sun, 29 Mar 2026 10:35:15 GMT

**原文链接**: https://setup4alpha.substack.com/p/7-rules-systematic-trading

**抓取时间**: 2026-04-27 19:23:03

---

## 摘要

7 Rules to Change Your Systematic Trading in 7 Months Most traders have all seven problems at once. This is the order to fix them. SetupAlpha Mar 29, 2026 ∙ Paid 9 2 Share You adjust the entry. No improvement and then you change the exit. Still the same. You add a regime filter and the backtest gets smoother but live trading doesn’t change. The problem is not what you’re adjusting. It’s that you’re working on layer three when layer one is still broken. Systematic trading strategies fail at specific points, in a predictable order. Not randomly. The same failure modes kept appearing in the same sequence across every strategy that didn’t survive. Seven of them. These rules came from building the SetupAlpha strategy library over several years. The strategies that failed, failed at exactly one ...

---

## 全文

7 Rules to Change Your Systematic Trading in 7 Months
Most traders have all seven problems at once. This is the order to fix them.
SetupAlpha
Mar 29, 2026
∙ Paid
9
2
Share
You adjust the entry. No improvement and then you change the exit. Still the same. You add a regime filter and the backtest gets smoother but live trading doesn’t change.
The problem is not what you’re adjusting. It’s that you’re working on layer three when layer one is still broken.
Systematic trading strategies fail at specific points, in a predictable order. Not randomly. The same failure modes kept appearing in the same sequence across every strategy that didn’t survive. Seven of them.
These rules came from building the SetupAlpha strategy library over several years. The strategies that failed, failed at exactly one of these points, in roughly this order. Work through them sequentially. Each one clears the path for the next.
Rule 1: If You Can’t Explain Why a Strategy Works in One Sentence, Don’t Trade It
This is not a simplicity rule, its more like a fragility detector.
If you can explain your strategy in one sentence, you understand what it’s exploiting. And if you know what it’s exploiting, you know when that edge is gone. You have a way to diagnose underperformance that doesn’t involve re-optimizing everything from scratch.
For example:
One of the ETF rotation strategies I sell at
SetupAlpha
has a one-sentence explanation:
every month, I buy the ETFs with the highest momentum over the past months.
You know why it works:
momentum tends to persist over short windows. You know what regime it needs, trending markets where recent winners keep winning. You know when to be suspicious when the strategy underperforms in a clear trending market, something else is wrong not the logic itself.
You can see the full strategy at
ETF Rotation Monthly Rebalance
.
Now consider a strategy with this entry:
Buy when the 14-period RSI crosses above 52, the 50-day MA is above the 200-day MA, the stock is within 3% of a 20-day high, and volume is above its 20-day average etcetc.
Try writing one sentence explaining what market behavior that exploits. You can’t. Which means if it stops working, you have no idea what broke.
The test:
write one sentence starting with “This strategy works because the market tends to...” If you can’t finish that sentence with something specific, go back and simplify until you can.
Rule 1 is the filter.
The next six rules decide what survives it.
Rule 2: The Simple Version Almost Always Wins
When a strategy starts underperforming, the instinct is to add rules. A regime filter here, an extra condition there, a volatility screen somewhere else. After three rounds of this, the strategy has eight parameters and a suspiciously smooth equity curve.
The simpler version (the one you started with before the additions) usually performs better out-of-sample. Out-of-sample means data the strategy never saw during development the real test, not the rehearsal. Not always better. But often enough that the burden of proof should be on the complexity, not on the simplicity.
How Simplicity Turns $100K Into $1.7M with 2 Simple Trading Strategies
SetupAlpha
·
October 19, 2025
Every trader wants the holy grail.
Read full story
Before adding any rule or parameter, run both versions side by side for at least six months of out-of-sample data. If the complex version doesn’t clearly outperform, cut the addition. The simpler strategy will be easier to trust when it has a bad month, easier to diagnose when something changes, and less likely to be fitting noise instead of real market structure.
Rule 3: Mean Reversion and Trend Following Need Different Regime Filters
This is the mistake I see most often in portfolios of multiple strategies:
the same SPY > SMA(200) filter applied to every strategy, regardless of type.
It works for trend following. For mean reversion, it often makes no sense at all. In many cases, no filter is the better answer.
Here’s why.
Mean reversion strategies profit from overreactions:
stocks that drop sharply and snap back. The largest overreactions happen during selloffs. Selloffs happen below the 200-day moving average. If you filter out everything below SMA(200), you are filtering out the exact conditions where mean reversion has its strongest edge.
Trend following is the opposite. It needs sustained directional movement. The 200-day filter keeps trend strategies out of choppy, directionless markets, exactly the environment where trend strategies lose slowly on false signals.
Rule 4: Paper Trade With Live Data for Three Months Before Real Money
Not backtesting, not a walk-forward.
Live paper trading:
real signals, real fills (simulated), real market hours, for at least three months.
Early in my trading career, I accidentally submitted a batch of orders incorrectly:
wrong sizes on some positions. I was on a demo account, so nothing happened. The cost was zero. I fixed it, understood how it happened, and built a check into my process.
If that had been a live account, the loss would have been significant and immediate. Not because the strategy was wrong. Because order entry is an operational skill that breaks in ways backtests never show double submissions, incorrect position sizing from manual entry, data pipeline errors that generate phantom signals. These are not edge cases. They happen, especially in the first months of running a system.
The goal is not to confirm the strategy works. The backtest did that. The goal is to find the operational failures before they become expensive ones.
Next 3 rules are the most important in my opinion because:
Rule 5:
Don’t waste time on dead signals
Rule 6:
Build strategies that survive reality
Rule 7:
Don’t sabotage your own edge
This post is for paid subscribers
Subscribe
Already a paid subscriber?
Sign in

---

*由 Substack Strategy Tracker 自动抓取*
