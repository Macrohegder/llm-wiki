# Turnaround Tuesday Strategy Backtest

**原文链接**: https://quantifiedstrategies.substack.com/p/turnaround-tuesday-strategy-backtest

**发布时间**: Mar 18, 2026

**抓取时间**: 2026-04-04 22:08:51

---

## 摘要

Turnaround Tuesday Strategy Backtest
So Simple, And Still Working Very Well
QuantifiedStrategies.com
Mar 18, 2026
3
1
Share
Today, we make a Turnaround Tuesday strategy backtest.
The Turnaround Tuesday strategy is one of the simplest and most well-known short-term trading edges in the stock market. It is based on a recurring pattern: markets that fall on Monday often rebound on Tuesday or the days after.
This phenomenon, known as the “Turnaround Tuesday effect,” has been observed for decades and is supported by historical data. The core idea is straightforward: buy weakness on Monday and sell the following day (or during the next few days.
In this article, we’ll break down the logic behind the strategy, present backtest results, and explore how small tweaks can significantly improve perfor...

---

## 全文

Turnaround Tuesday Strategy Backtest
So Simple, And Still Working Very Well
QuantifiedStrategies.com
Mar 18, 2026
3
1
Share
Today, we make a Turnaround Tuesday strategy backtest.
The Turnaround Tuesday strategy is one of the simplest and most well-known short-term trading edges in the stock market. It is based on a recurring pattern: markets that fall on Monday often rebound on Tuesday or the days after.
This phenomenon, known as the “Turnaround Tuesday effect,” has been observed for decades and is supported by historical data. The core idea is straightforward: buy weakness on Monday and sell the following day (or during the next few days.
In this article, we’ll break down the logic behind the strategy, present backtest results, and explore how small tweaks can significantly improve performance.
We first covered this strategy on our website as long back as 2012, albeit we have been trading it many years before that.
What is the Turnaround Tuesday effect?
The Turnaround Tuesday effect refers to the tendency of stock markets to reverse direction between Monday’s close and Tuesday’s close.
In simple terms:
If the market drops on Monday → Tuesday tends to be positive (or strong performance the rest of the week)
If the market rises strongly on Monday → returns tend to weaken afterward
This makes it a classic mean-reversion strategy, where traders buy short-term weakness expecting a bounce.
A famous example occurred after the Black Monday, when markets surged sharply on Tuesday and Wednesday following a historic collapse.
Turnaround Tuesday strategy backtest example
Basic Turnaround Tuesday strategy rules
A simple version of the strategy looks like this:
Today is Monday
Monday closes at least 1% lower than Friday
Buy at Monday’s close
Sell at Tuesday’s close
This approach captures the short-term rebound that often follows a weak start to the week.
Backtest results (SPY - S&P 500)
Backtesting this simple rule on the S&P 500 ETF (SPY) shows:
Number of trades: 212
Average gain per trade: 0.3%
Win rate: 56%
CAGR: 1.8%
Market exposure: just 2.5% ()
Despite modest returns, the strategy stands out because of its very low time in the market, making it capital-efficient.
Improving the strategy with filters
The raw Turnaround Tuesday strategy works—but it becomes significantly stronger when you add filters.
Strategy variation with IBS filter
Rules:
Monday closes lower than open
IBS (Internal Bar Strength) < 0.2
Buy at Monday close
Sell Tuesday close
Results:
Average gain per trade: 0.33%
Win rate: 57%
CAGR: 2.7%
Adding a simple filter improves both consistency and returns.
Holding longer increases returns
Another variation extends the holding period:
Today is Monday.
The close must be lower than the close on Friday.
The IBS must be below 0.5.
If 1-3 are true, then enter at the close.
Sell 4 trading days later (at the close).
Results:
Turnaround Tuesday strategy backtest results
Average gain per trade: 0.45%
Win rate: 60%
CAGR: 6.5% ()
This suggests the edge is not limited to Tuesday - it often continues for several days.
Better-performing variation
A more advanced version includes both filters and flexible exits:
Today is Monday.
The close must be lower than the close on Friday.
The IBS must be below 0.5.
If 1-3 are true, then enter at the close.
We sell when the close is higher than yesterday’s high (meaning the high from the previous trading day, so it’s important to monitor price action and patterns observed yesterday) OR 4 trading days later at the close.
Results:
Turnaround Tuesday strategy backtest
Average gain per trade: 0.46%
Win rate: 69%
CAGR: 7% ()
This version balances mean reversion with momentum, improving win rate and risk-adjusted returns.
What does NOT work?
Interestingly, flipping the strategy fails:
Buying strength on Monday leads to poor performance
This reinforces a key principle:
The edge comes from buying weakness - not strength.
Why the strategy works
Several factors may explain the Turnaround Tuesday effect:
Institutional repositioning after weekend news
Retail panic selling on Mondays
Mean-reversion tendencies in equity markets
Short-term liquidity imbalances
Whatever the reason, the data suggests the pattern has persisted for decades.
Key takeaways
Turnaround Tuesday is a robust mean-reversion strategy
It works best after weak Mondays
Adding filters like IBS improves results
Extending the holding period can increase returns
The strategy has low market exposure, making it capital efficient
Final thoughts
The Turnaround Tuesday strategy is a rare example of a simple, persistent market anomaly that still appears to work. While the raw edge is modest, combining it with filters and better exits can turn it into a solid trading strategy.
As always, results depend on execution, costs, and market conditions, but the evidence suggests that buying Monday weakness remains a viable approach. The Turnaround Tuesday strategy backtest is a simple, yet efficient strategy.
3
1
Share
Previous
Next

---

*由 Substack Strategy Tracker 自动抓取*
