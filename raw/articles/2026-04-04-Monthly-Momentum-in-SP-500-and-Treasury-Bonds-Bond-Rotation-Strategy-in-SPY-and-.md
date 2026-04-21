# Monthly Momentum in S&P 500 and Treasury Bonds (Bond Rotation Strategy in SPY and TLT)

**原文链接**: https://quantifiedstrategies.substack.com/p/monthly-momentum-in-s-and-p-500-and

**发布时间**: Sep 09, 2024

**抓取时间**: 2026-04-04 21:58:42

---

## 摘要

Monthly Momentum in S&P 500 and Treasury Bonds (Bond Rotation Strategy in SPY and TLT)
QuantifiedStrategies.com
Sep 09, 2024
1
Share
The SPY and TLT rotation trading strategy might work well because TLT often works as a safe haven when the stock market is weak. Below you find the logic and code for this simple SPY and TLT momentum/rotation strategy. The drawdown is low but the total return is better than “buy and hold”.
Here we look at a similar ETF sector momentum/rotation strategy but we exclude EEM: A SPY and TLT strategy (S&P 500 and 20 years Treasury bond).
We backtest the following trading rules:
* It’s based on monthly quotes in the ETFs SPY and TLT.
* Every month rank both based on last month’s performance/momentum.
* Go long the one with the best performance the prior month.
* Hol...

---

## 全文

Monthly Momentum in S&P 500 and Treasury Bonds (Bond Rotation Strategy in SPY and TLT)
QuantifiedStrategies.com
Sep 09, 2024
1
Share
The SPY and TLT rotation trading strategy might work well because TLT often works as a safe haven when the stock market is weak. Below you find the logic and code for this simple SPY and TLT momentum/rotation strategy. The drawdown is low but the total return is better than “buy and hold”.
Here we look at a similar ETF sector momentum/rotation strategy but we exclude EEM: A SPY and TLT strategy (S&P 500 and 20 years Treasury bond).
We backtest the following trading rules:
* It’s based on monthly quotes in the ETFs SPY and TLT.
* Every month rank both based on last month’s performance/momentum.
* Go long the one with the best performance the prior month.
* Hold for one month and repeat (or continue being long the same instrument).
The rules are simple. Obviously, this strategy is best performed in a tax-deferred account, but without slippage and taxes, the equity curves look like this from 2003 until today (shown in the below image)
1
Share
Previous
Next

---

*由 Substack Strategy Tracker 自动抓取*
