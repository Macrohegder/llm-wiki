# When Does a Trading Strategy Actually Break?

**原文链接**: https://algomatictrading.substack.com/p/when-does-a-trading-strategy-actually

**发布时间**: 2026-04-05

**抓取时间**: 2026-04-05 16:22:32

---

## 摘要

When Does a Trading Strategy Actually Break?
Variance or Breakdown? How to Know If a Strategy Is Actually Failing
Algomatic Trading
Mar 06, 2026
9
2
Share
Most traders don’t abandon bad strategies.
They abandon good ones during normal drawdowns.
The real challenge in systematic trading isn’t finding an edge.
It’s knowing whether that edge is temporarily cold or structurally broken.
Every strategy will underperform.
The question is not
if
.
The question is whether the underperformance is statistically normal… or evidence of degradation.
Understanding the difference is what separates serious systematic traders from reactive ones.
The Two Failure Modes
When it comes to degradation, traders typically fall into one of two traps:
1. Overreacting to Variance
They shut down a system after a handfu...

---

## 全文

When Does a Trading Strategy Actually Break?
Variance or Breakdown? How to Know If a Strategy Is Actually Failing
Algomatic Trading
Mar 06, 2026
9
2
Share
Most traders don’t abandon bad strategies.
They abandon good ones during normal drawdowns.
The real challenge in systematic trading isn’t finding an edge.
It’s knowing whether that edge is temporarily cold or structurally broken.
Every strategy will underperform.
The question is not
if
.
The question is whether the underperformance is statistically normal… or evidence of degradation.
Understanding the difference is what separates serious systematic traders from reactive ones.
The Two Failure Modes
When it comes to degradation, traders typically fall into one of two traps:
1. Overreacting to Variance
They shut down a system after a handful of losing trades or a few months of flat performance.
2. Ignoring Structural Decay
They keep trading a strategy long after the underlying edge has eroded.
Both are dangerous.
The goal is not to eliminate drawdowns.
The goal is to distinguish between
expected variance
and
structural breakdown
.
That requires a framework.
Layer 1 – Statistical Monitoring
I don’t monitor strategies based on whether they made money recently.
I monitor whether they are behaving within their historical statistical distribution.
There’s a big difference.
When a strategy underperforms, I ask four questions:
Is the rolling win rate outside the historical distribution?
Is the rolling expectancy below long-term expectancy by a meaningful margin?
Is the current drawdown deeper than the historical maximum?
Is the drawdown duration longer than the historical average?
I don’t ask:
“Did the strategy lose money this month?”
I ask:
“Is this performance outside expected variance?”
Most of the time, the answer is no.
Most of the time, the strategy is doing exactly what it’s supposed to do and the trader is the problem.
Your strategies will perform differently than they have, so you will for example have a new max drawdown but this doesn’t mean it is broken.
Variance is not degradation.
Layer 2 – Regime Alignment
This is where most retail traders fall short.
If a trend-following strategy underperforms during a choppy, directionless regime, that’s completely normal. That’s the regime doing what it does.
If that same trend-following strategy underperforms during a strong, persistent trend regime?
That’s worth investigating.
Edges are conditional.
A trend-following strategy does not perform equally in all environments.
If a breakout system underperforms in a sideways market, that is expected behavior.
I won’t go into exactly how I define a regime.
But I will say this: if you’re not thinking about regime alignment, you’re evaluating your strategy blind.
Layer 3 – Portfolio-Level Perspective
A single strategy degrading doesn’t automatically invalidate a portfolio.
This is a concept most retail traders never internalize because they’re focused entirely at the strategy level.
At the portfolio level, I monitor:
Correlation stability between systems
Contribution to total equity curve
Diversification behavior during stress periods
A strategy can go through a rough period and still provide diversification benefits.
Sometimes a lower-return system plays critical defensive work inside the portfolio.
The False Signals
This is the list I keep in my head to avoid making emotional decisions.
Mistakes that
feel
rational but aren’t:
Quitting a system after it hits a new equity high and then pulls back slightly
Killing a strategy after 5–10 consecutive losers
Comparing short-term monthly returns to long-term annual expectations
Adjusting parameters
during
a drawdown to make the equity curve look better
That last one is the most dangerous.
Tweaking a system mid-drawdown doesn’t fix the strategy. It just destroys the backtest validity and makes you feel productive.
Killing a strategy during expected variance is often more damaging than holding a slightly degrading edge too long.
When I Actually Intervene
Intervention is rare.
I consider it only if one or more of the following occur:
Rolling performance metrics fall meaningfully outside historical statistical bounds.
The core structural logic behind the edge is no longer valid.
Correlation assumptions within the portfolio materially shift.
Market structure changes in a way that directly impacts execution or edge mechanics.
Even then, the first step is evaluation and not parameter tweaking.
I never adjust parameters mid-drawdown.
Parameter changes during pain are usually emotional, not rational.
Next time you think about shutting down a strategy, ask yourself:
Am I reacting to outcomes… or distributions?
Am I evaluating a strategy in isolation… or in portfolio context?
Am I distinguishing variance from structural decay?
Edges don’t disappear overnight.
But conviction often does.
The real edge may not be the strategy itself.
It may be your ability to let it work.
This is exactly what my premium membership is built around.
Every month I publish a new algorithmic strategy. The thesis, performance and robustness testing are public. But paid subscribers get the real value: the full code, every single parameter described in text, and it is only by seeing how a strategy really works that one can really gain confidence in it.
Not just strategies. The conviction to trade them.
👉
Get the Full Code & Parameters
Thank you for your support!
Disclaimer:
I am not a financial advisor and I don’t recommend you to trade my strategies. This article is for informational and educational purposes only. Trading involves risk, and you can lose money. Always do your own research.
9
2
Share

---

*由 Substack Strategy Tracker 自动抓取*
