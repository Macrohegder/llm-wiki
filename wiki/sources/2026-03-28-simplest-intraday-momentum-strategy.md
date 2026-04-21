# The SIMPLEST Intraday Momentum Strategy in 2026

**Source**: [[2026-03-28-simplest-intraday-momentum-strategy]] | [Trading & Investing Strategies](https://tradinginvestingstrategies.substack.com/p/the-simplest-intraday-momentum-strategy)
**Date**: 2026-03-28
**Tags**: #strategy #intraday #momentum #vwap #stochastic-rsi #news-driven

## One-Sentence Summary

An intraday momentum system for news-driven moves: use **VWAP as a control filter** (only trade in the direction of institutional flow) and **Stochastic RSI to time entries** during pullbacks within the move.

## Key Insights

1. **VWAP is not support/resistance — it's a control gauge**
   - Most retail traders misuse VWAP as a bounce/break line
   - The correct use: VWAP tells you WHO is in control (buyers vs sellers) based on volume-weighted average execution
   - Above VWAP = institutions are net buyers; Below = net sellers
   - This is why the author calls it "the filter" — it removes low-quality entries by forcing alignment with institutional flow

2. **The FOMO problem is real and systematic**
   - The author missed a clean oil trade not because he didn't know about the catalyst, but because he had "no actual plan for how to get in"
   - This is the gap between "information edge" and "execution edge"
   - The strategy was built specifically to bridge this gap

3. **Intraday momentum is different from swing mean-reversion**
   - Swing strategies (like your [[2026-03-19-5-swing-trading-strategies-for-beginners]]) buy weakness over days
   - This strategy buys strength within a single day — but only on a pullback (Stoch RSI < 20) within an ongoing move
   - It's "momentum with timing," not "chasing the move"

## What We Know vs. What's Paywalled

| Component | Visible | Paywalled |
|-----------|---------|-----------|
| Core concept (VWAP + StochRSI) | ✅ | ❌ |
| Directional filter logic | ✅ | ❌ |
| Setup identification methods | ✅ (2 methods) | ❌ (screener details) |
| **Exact entry rules** | ❌ | ✅ |
| **Exact exit rules** | ❌ | ✅ |
| **StochRSI settings** | ❌ | ✅ |
| **PineScript code** | ❌ | ✅ |
| **Screener filter values** | ❌ | ✅ |

## Actionable Takeaways

1. **🎯 Implement VWAP control filter on existing strategies**
   - If you trade breakouts: only take long breakouts above VWAP
   - If you trade mean-reversion: only take long mean-reversion when price is above VWAP (trend-aligned)
   - This single filter could improve win rates across multiple strategies

2. **🎯 Use StochRSI for entry timing, not reversal prediction**
   - Wait for StochRSI < 20 during a pullback WITHIN an uptrend (price > VWAP)
   - Don't use it to catch falling knives — use it to enter established moves more efficiently

3. **⚠️ Cannot replicate without paywall**
   - The visible framework is solid, but exact parameters (StochRSI period, crossover logic, exit rules) are missing
   - Would need to subscribe or reverse-engineer through backtesting

## Comparison with Existing Strategies

| Dimension | Swing Strategies (QS) | Intraday Momentum (TIS) |
|-----------|----------------------|------------------------|
| Timeframe | Days (swing) | Minutes/Hours (intraday) |
| Direction | Mean-reversion (buy weakness) | Momentum (buy strength on pullback) |
| Core filter | Price vs historical range | VWAP + StochRSI |
| Frequency | 18-21% time in market | 3-4 times per week |
| Asset focus | SPY (broad market) | Individual stocks, commodities |
| Catalyst | None (systematic) | News-driven, macro events |

**Synergy**: These two approaches are highly complementary. The swing strategies catch systematic mean-reversion in SPY; the intraday momentum catches event-driven moves in individual names.

## Related Concepts
- [[VWAP]] — Volume Weighted Average Price, institutional execution benchmark
- [[Stochastic-RSI]] — Oscillator for timing entries within trends
- [[Intraday Momentum]] — trading strength within a single session
- [[News-Driven Trading]] — reacting to catalysts with rules, not emotion
- [[Execution Edge]] — the gap between knowing and acting

## Related Strategies
- [[2026-03-19-5-swing-trading-strategies-for-beginners]] — swing mean-reversion on SPY (complementary)
- [[2026-04-18-consecutive-down-days-strategy]] — another mean-reversion approach

## Credibility Rating

| Metric | Score | Notes |
|--------|-------|-------|
| Conceptual Quality | ⭐⭐⭐⭐☖ | VWAP-as-control-filter is a solid, well-known institutional concept |
| Actionability | ⭐⭐☖☖☖ | Exact rules are paywalled — cannot implement without subscribing |
| Novelty | ⭐⭐⭐☖☖ | VWAP + StochRSI is standard; the packaging for news-driven moves is useful |
| Risk Clarity | ⭐⭐☖☖☖ | No backtest numbers, no drawdown data, no position sizing visible |

**Overall**: 🟡 **Yellow** — Strong conceptual framework with good institutional logic, but exact implementation details are paywalled and no performance data is disclosed. Best treated as a "directional inspiration" rather than a replicable strategy.
