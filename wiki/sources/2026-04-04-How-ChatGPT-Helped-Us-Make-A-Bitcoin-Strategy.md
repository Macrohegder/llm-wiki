# How ChatGPT Helped Us Make A Bitcoin Strategy

**Source**: [[2026-04-04-How-ChatGPT-Helped-Us-Make-A-Bitcoin-Strategy]] | [Unknown](https://quantifiedstrategies.substack.com/p/how-chatgpt-helped-us-make-a-bitcoin)
**Date**: 2026-04-04
**Tags**: #article #substack #strategy

## One-Sentence Summary

> How ChatGPT Helped Us Make A Bitcoin Strategy
QuantifiedStrategies.com
Aug 29, 2025
8
2
Share
This article outlines the design of a
Bitcoin trend-following strategy using ChatGPT
, with a focus on Bit...

## Key Insights

1. **原文来源**: [Unknown](https://quantifiedstrategies.substack.com/p/how-chatgpt-helped-us-make-a-bitcoin)

## Full Content

How ChatGPT Helped Us Make A Bitcoin Strategy
QuantifiedStrategies.com
Aug 29, 2025
8
2
Share
This article outlines the design of a
Bitcoin trend-following strategy using ChatGPT
, with a focus on Bitcoin's characteristic volatility and aggressive trending behavior.
Trend-following is a proven strategy that reacts to market movements, buying strength, and exiting when the trend weakens.
The process began with a simple prompt in ChatGPT asking for trend-following ideas for Bitcoin, which generated five suggestions, including the Donchian Channel breakout. This classic strategy, popularized by the
Turtle Traders
, involves:
•
Buying when the price breaks above the highest high of the last N days
.
•
Exiting when the price drops below the lowest low of the last M days
. It's favored for its simplicity, systematic nature, and effectiveness on strongly trending assets like Bitcoin.
We made two key adjustments to the standard Donchian Channel breakout:
•
A Shorter Lookback Period
: We used a 15-day high for entry and a 15-day low for exit, rather than the typical 20-day period. This adjustment makes the strategy more responsive, allowing earlier entry into trends, which proved beneficial for crypto.
•
An ADX Filter
: Unconventionally, we chose to only allow trades when the ADX(14) was below 25. Most traders use ADX to confirm strength when it's high, but a low ADX typically signals a quiet or consolidating market. Bitcoin is known for explosive breakouts from these low-volatility conditions. This filter helps avoid noisy periods, positions trades before volatility expands, and reduces false signals.
The
final strategy rules
are:
•
Long Entry
: Bitcoin closes above the 15-day high, AND ADX(14) is below 25. Entry occurs at the close or next open.
•
Exit
: Price closes below the 15-day low. Exit occurs at the close or next open.
•
No Short Trades
: This decision is based on Bitcoin's historical upward bias, where trend-following tends to perform best on the long side.
This strategy works well for Bitcoin because the asset often consolidates for extended periods before breaking out forcefully. The ADX filter specifically waits for calm price action, allowing the system to jump in as momentum builds, aligning with Bitcoin's typical "low-volatility coil → violent move → trend" pattern.
Backtest results on daily BTC/USD data from 2015 showed a
strong Compound Annual Growth Rate (CAGR) of 90%
, outperforming a buy-and-hold strategy (66%). It featured a smoother equity curve, a 63% win rate over 35 trades, and significantly better risk-adjusted returns compared to the basic Donchian breakout. While past performance is not indicative of future results, the underlying logic is sound.
We encourage experimenting with simple ideas and
"breaking the rules"
(like using ADX counter-intuitively) to find unique trading advantages.
8
2
Share
Previous
Next

---

*由 Substack Strategy Tracker 自动抓取*

---

*Imported from Substack on 2026-04-25*
