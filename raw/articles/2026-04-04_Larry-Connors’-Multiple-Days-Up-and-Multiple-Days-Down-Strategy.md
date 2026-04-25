# Larry Connors’ Multiple Days Up and Multiple Days Down Strategy

**原文链接**: https://quantifiedstrategies.substack.com/p/larry-connors-multiple-days-up-and-6c4

**发布时间**: Mar 07, 2026

**抓取时间**: 2026-04-04 22:08:09

---

## 摘要

Larry Connors’ Multiple Days Up and Multiple Days Down Strategy
A Mean Reversion Strategy for Stocks
QuantifiedStrategies.com
Mar 07, 2026
5
1
Share
Today, we present Larry Connors’ Multiple Days Up and Multiple Days Down strategy, naturally with backtested results.
Larry Connors is a well-known trading researcher and author who introduced this strategy in Chapter 6 of his 2009 book High Probability Trading.
The strategy is based on the concept of mean reversion and is designed specifically for ETFs.
Connors argues that ETFs, because they represent diversified baskets of securities, are far less likely to collapse to zero than individual stocks. This diversification makes them particularly suitable for short-term mean reversion strategies.
The trading rules
The strategy attempts to buy ETF...

---

## 全文

Larry Connors’ Multiple Days Up and Multiple Days Down Strategy
A Mean Reversion Strategy for Stocks
QuantifiedStrategies.com
Mar 07, 2026
5
1
Share
Today, we present Larry Connors’ Multiple Days Up and Multiple Days Down strategy, naturally with backtested results.
Larry Connors is a well-known trading researcher and author who introduced this strategy in Chapter 6 of his 2009 book High Probability Trading.
The strategy is based on the concept of mean reversion and is designed specifically for ETFs.
Connors argues that ETFs, because they represent diversified baskets of securities, are far less likely to collapse to zero than individual stocks. This diversification makes them particularly suitable for short-term mean reversion strategies.
The trading rules
The strategy attempts to buy ETFs after a short period of strong selling pressure, while the longer-term trend remains positive. The rules are straightforward:
Trend filter:
The closing price must be above the 200-day moving average.
Short-term weakness:
The closing price must be below the 5-day moving average.
Consecutive declines:
The ETF must have declined in at least four of the last five trading days.
Entry:
If all conditions are satisfied, enter the position at the close.
Exit:
Sell the position at the close when the ETF closes above its 5-day moving average.
Risk management:
The strategy does not use a stop-loss.
Backtest results for SPDR S&P 500 ETF Trust (SPY)
When tested on SPY alone, the strategy produced the following results:
Larry Connors’ Multiple Days Up and Multiple Days Down Strategy
Number of trades: 264
Profit factor: 2.2
Maximum drawdown: 12%
Compound annual growth rate (CAGR): 3.4%
Market exposure: 9%
The relatively modest CAGR is mainly explained by the very low market exposure. The strategy is invested only about 9% of the time because trades occur only during short-term pullbacks within an existing uptrend.
Connors originally tested the strategy on a basket of ETFs rather than a single instrument. We have conducted similar tests on our website, where we have backtested at least six different strategies developed by Connors.
Although the strategy trades infrequently, the results show a solid profit factor, reflecting the strong tendency of ETFs to revert after short bursts of weakness during longer-term uptrends.
5
1
Share
Previous
Next

---

*由 Substack Strategy Tracker 自动抓取*
