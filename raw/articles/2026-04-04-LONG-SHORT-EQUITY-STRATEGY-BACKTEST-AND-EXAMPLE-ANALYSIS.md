# LONG SHORT EQUITY STRATEGY (BACKTEST AND EXAMPLE ANALYSIS)

**原文链接**: https://quantifiedstrategies.substack.com/p/long-short-equity-strategy-backtest-534

**发布时间**: Oct 19, 2025

**抓取时间**: 2026-04-04 22:05:17

---

## 摘要

LONG SHORT EQUITY STRATEGY (BACKTEST AND EXAMPLE ANALYSIS)
QuantifiedStrategies.com
Oct 19, 2025
4
2
Share
Long short equity strategy is a method of investing whereby a trader takes long positions in stocks that are expected to appreciate and, at the same time, takes short positions in stocks that are expected to decline. It is a form of hedging strategy that aims to minimize risk by having both long and short positions while maximizing profits by gaining from the rising values in stocks with long positions and declining values of stocks with short positions.
We backtest the following trading rules:
➨ We create a pair ratio that is simply the price of KO divided by PEP.
➨ We create a 5-day RSI of the pair.
➨ If the RSI value in no. 2 goes below 20, we invest 50% of the equity in KO and sho...

---

## 全文

LONG SHORT EQUITY STRATEGY (BACKTEST AND EXAMPLE ANALYSIS)
QuantifiedStrategies.com
Oct 19, 2025
4
2
Share
Long short equity strategy is a method of investing whereby a trader takes long positions in stocks that are expected to appreciate and, at the same time, takes short positions in stocks that are expected to decline. It is a form of hedging strategy that aims to minimize risk by having both long and short positions while maximizing profits by gaining from the rising values in stocks with long positions and declining values of stocks with short positions.
We backtest the following trading rules:
➨ We create a pair ratio that is simply the price of KO divided by PEP.
➨ We create a 5-day RSI of the pair.
➨ If the RSI value in no. 2 goes below 20, we invest 50% of the equity in KO and short 50% in PEP.
➨ When the RSI value returns to 60, we cover both our positions done in no 3.
➨ If the RSI value in no. 2 goes above 80, we spend 50% of the equity short-selling KO and spend the remaining 50% on a long position in PEP.
➨ We cover our position from no 5 if the RSI value goes below 40.
The strategy’s historical performance can be found in the equity chart shown below.
4
2
Share
Previous
Next

---

*由 Substack Strategy Tracker 自动抓取*
