# The Supertrend Indicator Backtested

**Source**: [[2026-04-25-The-Supertrend-Indicator-Backtested]] | [Quantified Strategies](https://quantifiedstrategies.substack.com/p/supertrend-indicator)
**Date**: 2026-04-25
**Tags**: #article #substack #backtest #trend-following

## One-Sentence Summary

> The Supertrend Indicator Backtested
Explained With Trading Rules
QuantifiedStrategies.com
Mar 26, 2026
∙ Paid
4
1
Share
In today’s article about algorithmic trading, we take a close look at backtestin...

## Key Insights

1. **原文来源**: [Quantified Strategies](https://quantifiedstrategies.substack.com/p/supertrend-indicator)

## Full Content

The Supertrend Indicator Backtested
Explained With Trading Rules
QuantifiedStrategies.com
Mar 26, 2026
∙ Paid
4
1
Share
In today’s article about algorithmic trading, we take a close look at backtesting the
Supertrend Indicator
to see if this popular tool actually delivers on its promising name.
The Supertrend is a trend-following tool that plots a line above or below the price based on volatility, utilizing the Average True Range (ATR).
How the Supertrend Indicator is Calculated (Formula)
Supertrend Indicator example
The foundation of the indicator is the median price, calculated by adding the high and low of a bar and dividing by two:
MedianPrice = ( H + L ) / 2;
From this median price, two bands are created:
Upper Band:
Median Price + (Multiplier * ATR)
Lower Band:
Median Price - (Multiplier * ATR)
Olivier Seban, the inventor of the Supertrend, suggested using a 10-period lookback with a multiplier of 3.
Although there are two bands, only one line appears on the chart at a time because the indicator alternates between them based on a specific rule: the lower band cannot move downward, and the upper band cannot move upward.
The Trading Strategy
The strategy follows simple, non-optimized rules to avoid curve fitting:
Here is a trade example:
Supertrend indicator trade example
The buy signal was triggered on 05/29/2020 at 3044.31, and the sell signal was triggered on 01/21/2022 at 4397.94, resulting in a gain of 1353.63 points, which equals a profit of 44.46%.
The Backtest Results (1960–Present)
This strategy was tested on the S&P 500 using weekly data going back to 1960. The results reveal a compelling case for trend-following:
Supertrend indicator explained and backtested
Wealth Growth:
A 100,000 investment would have grown to nearly 5.4 million, even without accounting for dividends.
Win Rate:
The strategy boasted a 68% win rate across only 41 trades.
Risk Management:
The maximum drawdown was only 25%, which is significantly lower than a traditional buy-and-hold strategy.
Risk-Adjusted Return:
Because you are only invested 63% of the time, the risk-adjusted return comes in at 9.8%, which actually outperforms buy-and-hold.
Backtesting the Supertrend Indicator
The Supertrend indicator’s primary strength is its ability to protect capital during major market downturns and keep traders positioned within large trends. However, it is far from perfect; its biggest weakness is sideways or “choppy” markets, where it often produces whipsaws: small, repeated losses as the price fluctuates across the line.
While it is a solid, data-driven tool, it should not be used blindly as a standalone strategy without considering market context. Ultimately, the data confirms that there is significant value to be found in backtesting the Supertrend Indicator.
Trading Rules:
This post is for paid subscribers
Subscribe
Already a paid subscriber?
Sign in
Previous
Next

---

*由 Substack Strategy Tracker 自动抓取*

---

*Imported from Substack on 2026-04-25*
