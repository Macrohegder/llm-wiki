# When XLP Diverges From Recent High And Low: A Mean Reversion Trading Strategy Explored

**Source**: [[2026-04-04-When-XLP-Diverges-From-Recent-High-And-Low:-A-Mean-Reversion-Trading-Strategy-Explored]] | [Unknown](https://quantifiedstrategies.substack.com/p/when-xlp-diverges-from-recent-high)
**Date**: 2026-04-04
**Tags**: #article #substack #strategy #mean-reversion

## One-Sentence Summary

> When XLP Diverges From Recent High And Low: A Mean Reversion Trading Strategy Explored
QuantifiedStrategies.com
Apr 20, 2024
1
Share
A while back we discussed a day trading strategy in SPY. This one w...

## Key Insights

1. **原文来源**: [Unknown](https://quantifiedstrategies.substack.com/p/when-xlp-diverges-from-recent-high)

## Full Content

When XLP Diverges From Recent High And Low: A Mean Reversion Trading Strategy Explored
QuantifiedStrategies.com
Apr 20, 2024
1
Share
A while back we discussed a day trading strategy in SPY. This one works well on XLP as well, with some modifications.
The core concept of this strategy involves calculating the average true range (ATR), the recent low of the asset, and the (C-L)/(H-L) ratio daily. It uses these metrics to determine whether to enter long or short positions based on specific criteria.
We backtest the following trading rules:
Calculate a 25-day average of the (High minus Low — (H-L)). That is the “ATR”.
Calculate the Low of the last 10 days.
Calculate the (C-L)/(H-L) ratio every day (IBS).
Calculate a band 2.5 times above the 10 day low using the average from point number 1 (ATR).
If XLP closes above the band in number 4, and point 3 has a higher value than 0.8, then go short at the close.
Exit on tomorrow’s close.
Equity curve for both Short and Long position is shown below.
1
Share
Previous
Next

---

*由 Substack Strategy Tracker 自动抓取*

---

*Imported from Substack on 2026-04-25*
