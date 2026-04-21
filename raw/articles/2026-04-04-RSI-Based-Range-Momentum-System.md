# RSI-Based Range Momentum System

**发布时间**: Thu, 02 Apr 2026 10:40:24 GMT

**原文链接**: https://quantifiedstrategies.substack.com/p/rsi-based-range-momentum-system

**抓取时间**: 2026-04-04 20:42:48

---

## 摘要

RSI-Based Range Momentum System QuantifiedStrategies.com Apr 02, 2026 5 1 Share Most traders view the Relative Strength Index (RSI) solely as a tool for identifying “overbought” or “oversold” conditions, ie, selling when it’s above 70 and buying when it’s below 30. However, the sources suggest that the “true nature” of the RSI is actually as a momentum indicator. When the RSI remains above 50, it signifies that average gains are outpacing average losses, indicating a general price rise. The Core Logic: The “Bull Range” In a healthy uptrend, the RSI doesn’t just bounce around; it stays within a specific “range.” The Bull Zone: During an uptrend, the RSI typically ranges from 40 to 80. The Pullback Support: During a normal pullback in a bull market, the RSI tends to find support and reverse ...

---

## 全文

RSI-Based Range Momentum System
QuantifiedStrategies.com
Apr 02, 2026
5
1
Share
Most traders view the Relative Strength Index (RSI) solely as a tool for identifying “overbought” or “oversold” conditions, ie, selling when it’s above 70 and buying when it’s below 30.
However, the sources suggest that the “true nature” of the RSI is actually as a momentum indicator. When the RSI remains above 50, it signifies that average gains are outpacing average losses, indicating a general price rise.
The Core Logic: The “Bull Range”
In a healthy uptrend, the RSI doesn’t just bounce around; it stays within a specific “range.”
The Bull Zone:
During an uptrend, the RSI typically ranges from 40 to 80.
The Pullback Support:
During a normal pullback in a bull market, the RSI tends to find support and reverse in the 40–50 zone. If it drops to 30, it usually signals something more serious than a simple pullback.
The Strategy Rules
This strategy is inspired by a paper called
Finding consistent trends with strong momentum
by Arthur Hill.
The strategy consists of two indicators:
RSI bull range: RSI fluctuates between 40 and 100 over N days.
RSI bull momentum: highest high value of RSI is greater than 70 over N days.
For this backtest, we will use the 100 days lookback period and the 14-day RSI. This means that, for example, for the RSI bull range to flash a signal, the RSI must have fluctuated between 40 and 100 over the last 100 days.
The Entry Signal:
Buy (specifically tested on the SPY ETF) when both of these conditions are true over the last 100 days:
RSI Bull Range:
The RSI has fluctuated strictly between 40 and 100.
RSI Bull Momentum:
The highest RSI value reached during that period is greater than 70.
The Exit Signal:
Sell only when both conditions turn false.
If one indicator turns false but the other remains true, you stay in the position.
The Results: Quality Over Quantity
Backtesting this strategy on the S&P 500 (SPY) since 1993 yields some decent statistics (backtested in Python):
RSI-Based Range Momentum System
CAGR:
5.93% (buy and hold 9.58%)
Win Ratio:
A high 83% (10 out of 12 trades were profitable).
Risk-Adjusted Return:
16.61% (significantly higher than the CAGR because the strategy is only in the market 35.7% of the time).
Maximum Drawdown:
A modest 12.9%, which helps protect the portfolio from large market crashes.
Conclusion: The Takeaway for Readers
The RSI Range-Momentum strategy is a “low-activity” approach. It doesn’t generate many signals, only 12 since 1993, but the signals it does trigger are highly profitable and help identify major bull markets while keeping you on the sidelines during major downturns. It proves that the RSI can be a powerful momentum tool when you look at the range it inhabits rather than just the peaks and valleys.
5
1
Share
Previous
Next

---

*由 Substack Strategy Tracker 自动抓取*
