# Why Volatility Adjusted Sizing Matters More Than You Think

**原文链接**: https://algomatictrading.substack.com/p/why-volatility-adjusted-sizing-matters

**发布时间**: 2026-04-05

**抓取时间**: 2026-04-05 16:22:17

---

## 摘要

Why Volatility Adjusted Sizing Matters More Than You Think
The hidden flaw in 99% of backtests and why your static position sizing could be sabotaging your edge
Algomatic Trading
Feb 08, 2026
31
7
7
Share
You’ve built a strategy. The backtest looks solid. Win rate is respectable. Sharpe ratio is decent. You’re ready to go live.
Then reality hits.
The strategy that showed a smooth 40% annual return in backtesting delivers 15% with very deep drawdowns. What happened?
The answer is often hiding in plain sight, buried in a single line of code that most traders never question:
contracts = 1
Static position sizing isn’t just ineffective, it’s dangerous. And if you’re using it in your backtests, you’re not testing what you think you’re testing.
The Problem With “Trading One Contract”
Static posit...

---

## 全文

Why Volatility Adjusted Sizing Matters More Than You Think
The hidden flaw in 99% of backtests and why your static position sizing could be sabotaging your edge
Algomatic Trading
Feb 08, 2026
31
7
7
Share
You’ve built a strategy. The backtest looks solid. Win rate is respectable. Sharpe ratio is decent. You’re ready to go live.
Then reality hits.
The strategy that showed a smooth 40% annual return in backtesting delivers 15% with very deep drawdowns. What happened?
The answer is often hiding in plain sight, buried in a single line of code that most traders never question:
contracts = 1
Static position sizing isn’t just ineffective, it’s dangerous. And if you’re using it in your backtests, you’re not testing what you think you’re testing.
The Problem With “Trading One Contract”
Static position sizing is seductive in its simplicity. Pick a number: 1 contract, 10 shares, $1000 per trade and keep it constant across every trade, every market condition, every volatility regime.
It feels safe. It feels consistent.
But here’s what it actually does:
It creates a moving target for your risk.
When you trade a fixed position size:
During low volatility periods, you’re massively under-risking (leaving money on the table)
During high volatility periods, you’re massively over-risking (exposing yourself to catastrophic losses)
Your actual risk per trade fluctuates wildly, sometimes 0.1% of your account, sometimes 5%
This wouldn’t be terrible if markets stayed in one volatility regime. But they don’t.
Markets breathe. They expand and contract.
They go from calm to chaotic and back again.
What Your Backtest Isn’t Telling You
Here’s the truth:
backtests with static sizing lie to you about consistency.
A backtest that trades 1 contract on every signal appears to have “constant risk exposure.” The equity curve looks smooth. The metrics look stable.
But that smoothness is an artifact of historical averaging not a reflection of the actual risk you’d experience in real-time.
Consider two scenarios with the same strategy, same entry/exit logic, trading the same market:
Scenario A: March 2020 (COVID crash)
ATR (5-day): $45
Your static 1-contract position = $45 risk per point
Actual account risk: 4.5% per trade (on a $10,000 account)
Scenario B: July 2021 (low volatility)
ATR (5-day): $8
Your static 1-contract position = $8 risk per point
Actual account risk: 0.8% per trade
Same strategy. Same position size. 5.6x difference in risk.
During the crash, you’re betting big on every trade. During the calm, you’re barely moving the needle. Neither is optimal. And your backtest averaged them together into one misleading number.
Join 7,000+ traders learning systematic trading and get new strategies & research every month.
Subscribe
The Dynamic Solution: Volatility-Adjusted Position Sizing
This is where most traders stop thinking and assume “dynamic sizing” means something complicated.
It’s not.
Here’s the entire position sizing logic I use:
// POSITION MANAGEMENT
//-------------------------------------------------------------------------
timeframe (daily)
atr = averagetruerange[5]    //Usually I use atr 5 or 14
contractsToTrade = (riskPercent * 0.01) * portfolioSize / (atr)

// === INPUTS ===
once riskPercent = 0.5       // change this to adjust position size
once portfolioSize = 2000    // change this to adjust position size
timeframe (default)
Four lines of code. That’s it.
Let’s break down what’s happening:
The Core Formula
Position Size = (Risk % × Portfolio Size) / ATR
What this does:
Takes your desired risk per trade (0.5% in my case)
Multiplies it by your account size ($2000)
Divides by the current 5-day Average True Range
Why ATR?
ATR (Average True Range) measures recent volatility, how much the market has actually been moving. It’s the perfect proxy for “how much could this trade move against me.”
When ATR is high (volatile markets), you trade smaller positions. When ATR is low (calm markets), you trade larger positions.
The result:
Your actual dollar risk per trade stays consistent, regardless of market conditions.
A Real Example: The Math That Saves Your Account
Let’s revisit those two scenarios with dynamic sizing instead:
Scenario A: March 2020 (COVID crash)
Portfolio: $10,000
Risk per trade: 0.5% = $50
ATR (5-day): $45
Position size: $50 ÷ $45 = 1.11 contracts
Scenario B: July 2021 (low volatility)
Portfolio: $10,000
Risk per trade: 0.5% = $50
ATR (5-day): $8
Position size: $50 ÷ $8 = 6.25 contracts
Same dollar risk. Same percentage risk. Completely different position sizes.
In the crash, you’re automatically pulling back to 1 contract. In the calm, you’re scaling up to 6 contracts. Your risk stays constant at exactly $50 per trade.
It’s basic risk management that a lot of systematic traders ignore.
Why Static Sizing Fails In Backtesting
When you backtest with static position sizing, you’re not just getting inaccurate results, you’re getting three specific types of distortion:
1.
Survivorship Bias On Steroids
Static sizing means your strategy “survives” high-volatility periods in the backtest purely by luck. Your 1-contract position might have gotten obliterated if you’d been properly sized for your risk tolerance.
In live trading, you won’t have the luxury of that luck repeating.
2.
False Confidence In Drawdowns
Your backtest shows a max drawdown of 15%. But that’s the average of wildly different risk exposures. The real max drawdown, if you’d been consistently risking 0.5% per trade, could be 25% or more.
You’re making decisions based on a number that doesn’t reflect reality.
3.
Opportunity Cost Blindness
During low-volatility periods, your static 1-contract position was risking 0.3% when you should have been risking 0.5%. You left 40% of potential profits on the table, profits that would have compounded over time.
Your backtest doesn’t show you the returns you missed.
Comparison between two backtests
Let me show you a comparison to see what the key differencies are in the performance in two backtests. Both of these backtests use the exact same entry/exit parameters and everything except the position size is identical.
Shorter term backtests (which is what most people show you) looks insanely good because the sizing is huge. The future drawdown will always be the biggest and in the case with a static sizing it will be huge or even devastating because you have no idea what to expect.
Static 2-contract position size with 20.000€ capital.
Dynamic 1% risk on 20.000€ capital size.
The Hybrid Approach: Why I Use Both Daily And Default Timeframes
You might have noticed something in my code:
timeframe (daily)
atr = averagetruerange[5]
contractsToTrade = (riskPercent * 0.01) * portfolioSize / (atr)
timeframe (default)
I’m calculating ATR on the daily timeframe, even if I’m trading intraday.
Why?
Because intraday volatility is noise. Daily volatility is signal.
If you’re trading a 15-minute strategy and you calculate ATR on 15-minute bars, you’ll get whipsawed by every micro-move. Your position sizing will fluctuate wildly based on the last few bars.
By anchoring to daily ATR, you get:
Smoother position size adjustments
Reduced sensitivity to intraday noise
Consistent risk exposure that adapts to true market regimes, not micro-fluctuations
This is the “hybrid” part, dynamic sizing based on a longer-term volatility measure. You get the benefits of adaptation without the chaos of constant recalculation.
The Dangers Of Ignoring This (And Why People Still Do)
If dynamic sizing is so obviously better, why doesn’t everyone use it?
Three reasons:
1.
It’s Harder To Backtest
Most backtesting platforms default to “number of shares” or “number of contracts.” Calculating position size based on ATR requires custom code. It’s easier to just type “1” and move on.
2.
It Reveals The Truth
When you switch from static to dynamic sizing, your backtest results change. Sometimes dramatically.
That strategy that looked amazing at 1 contract? When you size it properly for consistent risk, the returns drop by 30% and the drawdowns double.
Most traders would rather live in blissful ignorance than face the reality that their edge isn’t as strong as they thought.
They would simply have a better looking backtest than better looking live results.
3.
It Requires Discipline In Live Trading
Dynamic sizing means your position size changes with every trade. You can’t just “trade 5 contracts today.” You need to calculate, adjust, and stick to the math even when it feels wrong.
When volatility explodes and your system says “trade 1 contract,” every instinct screams to trade more. When volatility collapses and your system says “trade 10 contracts,” fear tells you to pull back.
The discipline required is where most traders fail, not in the strategy, but in the execution.
How To Implement This (Even If You’re Not A Coder)
You don’t need a PhD in mathematics to implement volatility-adjusted sizing. You need three things:
1.
A Way To Calculate ATR
Most trading platforms have this built-in. TradingView, ProRealTime, MetaTrader, they all have ATR indicators.
Use the 5-day or 14-day ATR depending on your trading timeframe, I use this:
Day trading: 5-day ATR
Swing trading: 14-day ATR
Position trading: 20-40-day ATR
2.
A Risk Per Trade Number
Pick a percentage of your account you’re willing to lose on any single trade. Common ranges:
Conservative: 0.25% - 0.5%
Moderate: 0.5% - 1%
Aggressive: 1% - 2%
I use 0.5% because it gives me room to be wrong 200 times before I’m wiped out. That’s enough runway to let my edge play out.
It’s very important to check the minimum size at your broker, with a too low size the backtest can look flat at volatile or recent periods because the desired size is less than the accepted minimum size, take an extra look at this.
3.
The Formula (Again)
Position Size = (Risk % × Portfolio Size) / ATR
Calculate this before every trade. Adjust your position size accordingly.
That’s it. You’re now in the top % of traders who actually manage risk properly.
The Compounding Effect Over Time
Here’s what most traders miss: the benefit of dynamic sizing isn’t just risk management, it’s compound growth optimization.
When you maintain consistent percentage risk across all trades:
Your wins compound more efficiently (because you’re sized appropriately for the opportunity)
Your losses don’t compound catastrophically (because you’re not over-leveraged)
Your equity curve smooths out (because volatility adjustments happen automatically)
The trader using static sizing might survive. The trader using dynamic sizing thrives.
Common Objections (And Why They’re Wrong)
“But my strategy works with static sizing!”
Does it? Or does it work
on average
across multiple volatility regimes, masking periods where you were wildly over- or under-leveraged?
Test it with dynamic sizing. If the returns drop significantly, you didn’t have an robust edge, you had luck during low-volatility periods.
“This is too complicated for beginners.”
It’s literally one formula:
(Risk% × Portfolio) / ATR
If you can calculate a tip at a restaurant, you can calculate your position size:)
“I don’t want to keep adjusting my position size.”
You adjust your stop loss based on the trade, don’t you? You adjust your entry based on price action, don’t you?
Position sizing is the most important variable in your trading equation. If you’re not adjusting it, you’re not serious about consistency.
“What if ATR goes to zero?”
It won’t. ATR measures actual price movement. If a market is truly dead (ATR approaching zero), you shouldn’t be trading it anyway.
The Path Forward
If you take one thing from this article, take this:
Static position sizing is a lie you tell yourself to avoid doing the math.
It makes backtesting easier. It makes trading feel simpler. But it makes your results worse.
Dynamic, volatility-adjusted position sizing is not a “nice to have.” It’s foundational. It’s the difference between a backtest that misleads you and a backtest that prepares you.
Here’s what I want you to do:
Take your current strategy
Backtest it with static sizing
(however you’re doing it now)
Backtest it with dynamic sizing
using the formula I shared
Compare the results
I guarantee you’ll see a difference. The question is whether you’ll accept it or ignore it.
Most traders ignore it. They’d rather maintain the illusion of a great strategy than face the reality of mediocre risk management.
Don’t be most traders.
Final Thoughts
The markets don’t care about your backtest.
They don’t care that your strategy worked with 1 contract per trade. They don’t care that your equity curve looked smooth in 2019.
They care about how you manage risk
right now
, in
this
volatility regime, with
these
market conditions.
Dynamic position sizing is how you translate a theoretical edge into real, sustainable profits. It’s how you survive the crashes and capitalize on the calms.
It’s not sexy. It’s not complicated. But it works.
And in trading, “works” is the only metric that matters.
Do you have any question?
Drop a comment below. I read every single one, and the best discussions happen in the comments section.
If this article changed how you think about position sizing, share it with another trader. They’ll thank you later.
Disclaimer:
I am not a financial advisor and I don’t recommend you to trade my strategies. This article is for informational and educational purposes only. Trading involves risk, and you can lose money. Always do your own research.
31
7
7
Share

---

*由 Substack Strategy Tracker 自动抓取*
