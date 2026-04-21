# The SIMPLEST Intraday Momentum Strategy in 2026

**Source**: https://tradinginvestingstrategies.substack.com/p/the-simplest-intraday-momentum-strategy
**Date**: 2026-03-28
**Author**: Trading & Investing Strategies
**Status**: Paid article (framework visible, rules + PineScript behind paywall)

---

## Introduction

Author describes missing a clean crude oil trade on March 2nd (Trump announcement about US-Iran war) because he had "no actual plan for how to get in." This led to building a systematic intraday momentum strategy for news-driven moves.

Core insight: "knowing something is coming and having a system for trading it are two completely different things."

---

## Strategy Framework

**Type**: Intraday momentum (news-driven, macro catalysts)
**Frequency**: 3-4 times per week (not every day)
**Asset class**: Individual stocks, commodities (oil example)

### Tool 1: VWAP (Volume Weighted Average Price)

Not used as support/resistance, but as a **control filter**:
- Price > VWAP = buyers in control (institutional size)
- Price < VWAP = sellers in control
- Long setups ONLY when price is above VWAP
- Short setups ONLY when price is below VWAP
- Distance from VWAP shows pressure strength

Key insight: If price holds above VWAP through first 30 minutes of a news-driven move, institutional buyers are defending their position. If price can't reclaim VWAP after gap-up, the move lacks real backing.

### Tool 2: Stochastic RSI

Measures where current RSI sits relative to its own range over a lookback period.
- < 20: oversold, sharp short-term pullback
- > 80: overbought
- Used to time entries WITHIN the move (not for reversal)

---

## Two Methods to Find Setups

### Method 1: News-Driven Symbols
Watch symbols moving on real catalysts:
- Earnings
- Oil inventory reports
- Fed announcements
- Political announcements (e.g., Trump weekend tweets)

Process: Open chart → check VWAP position → check Stoch RSI extreme after pullback → wait for signal.

### Method 2: TradingView Screener
Run every morning to catch symbols with:
- Significant intraday moves
- Elevated volume

Exact screener filters are paywalled.

---

## Paywalled Content

The following are behind the paywall:
- Complete entry and exit rules
- Exact Stoch RSI settings and crossover trigger
- Complete custom TradingView (PineScript) indicator with buy/sell signals
- Alert conditions
- Step-by-step TradingView screener setup with exact filter values

---

## Author's Related Work

- "The Simple VWAP Strategy That Turns Pullbacks Into Consistent Gains" — mean reversion approach on SPY using VWAP differently
