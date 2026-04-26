---
title: "Taming OLMAR's 1222% Backtest into a Sustainable 106% CAGR"
author: Stuart Farmer (Paper to Profit)
url: https://papertoprofit.substack.com/p/taming-olmars-1222-backtest-into
date: 2025-05-20
topics:
  - mean-reversion
  - OLMAR
  - portfolio-selection
  - online-algorithm
source: Substack
---

# Taming OLMAR's 1222% Backtest into a Sustainable 106% CAGR

**Mean reversion: the secret sauce to sustainable alpha.**

Author: Stuart Farmer | May 20, 2025

---

## Summary

This article introduces the **Online Moving Average Reversion (OLMAR)** system by Bin Li and Steven Hoi (Nanyang Technological University, Singapore, 2012). OLMAR is an online portfolio selection algorithm that exploits mean reversion — assets trading above their moving average are expected to revert downward, and those below are expected to revert upward.

The author implemented OLMAR on SP600 Small Cap constituents with a 25-day moving average window, achieving an astonishing **1222% CAGR** in raw backtest (though with extreme drawdowns of -75%+ and 68x annual turnover). By applying **0.2x leverage** (allocating only 20% of capital to the strategy, keeping the rest in cash), drawdowns were reduced to -27% while still achieving **106% CAGR** at 10 bps transaction costs.

---

## Core Concepts

### Mean Reversion
- **Mean**: a long-run average level (e.g., 200-day moving average)
- **Reversion**: the force that drives price back toward that mean
- Market participants driving mean reversion: Value Traders, Reactionary Traders, Risk-Considerate Traders (rebalancing), Market Makers

### OLMAR Algorithm (Step by Step)

1. Get current prices for assets in basket
2. Compute updated moving average for each (window size = variable)
3. For assets above MA → expect them to come down (short)
4. For assets below MA → expect them to come up (long)
5. Calculate 'expected returns' = % difference between current price and MA
6. Apply expected returns to current portfolio weights (returns × weights)
7. **Buy low, sell high**: adjust weights to increase exposure to underperforming assets and decrease overperforming ones
8. Repeat next day

---

## Strategy Rules

| Rule | Detail |
|------|--------|
| **Asset Universe** | SP600 Small Cap constituents (author's test); generalizable to any basket |
| **Moving Average Window** | 25 days |
| **Weighting** | Online portfolio selection — weights adjust daily based on expected mean reversion |
| **Rebalancing** | Daily |
| **Max Drawdown (raw)** | ~-75%+ (prolonged periods) |
| **Max Drawdown (0.2x leverage)** | ~-27% |
| **Annual Turnover** | 68x (flip entire portfolio every 3.7 days) |
| **Transaction Costs** | 10 bps assumed for stable version |
| **Performance (0.2x leverage)** | **106% CAGR**, -27% max drawdown |

---

## Backtest Results

### Raw OLMAR (1x leverage)
- CAGR: **1222%**
- Drawdown: -75%+ regularly
- Turnover: 68x/yr
- Even at 50 bps fees: still ~909% CAGR (but -85% drawdown)

### Tamed OLMAR (0.2x leverage, 10 bps fees)
- CAGR: **106%**
- Max Drawdown: **-27%** (below equal-weighted benchmark)
- Transaction costs: 10 bps

---

## Pseudocode

```
class OLMAR:
    parameters:
        window = 25
        leverage = 0.2  # 20% capital allocation
    
    initialize:
        weights = 1/N for each of N assets
    
    on each day:
        # Get current prices
        prices = get_prices(assets, today)
        
        # Compute moving averages
        ma = sma(prices, window)
        
        # Calculate expected returns (reversion prediction)
        expected_returns = []
        for each asset:
            if price > ma:
                expected_return = (ma - price) / price  # negative = expect drop
            else:
                expected_return = (ma - price) / price  # positive = expect rise
        
        # Apply to portfolio weights
        new_weights = weights * (1 + expected_returns)
        new_weights = normalize_to_sum_1(new_weights)  # ensure weights sum to 1
        
        # Apply leverage
        actual_weights = new_weights * leverage
        cash_weight = 1 - leverage  # rest in risk-free asset
        
        # Rebalance
        execute_trades(weights -> actual_weights)
        
        # Update for next iteration
        weights = new_weights
```

---

## Limitations & Risks

1. **Extreme turnover** (68x/yr) — high transaction costs eat significantly into returns
2. **Prolonged drawdowns** even after de-leveraging
3. **Multi-asset requirement** — OLMAR is inherently a portfolio strategy, not single-instrument
4. **Not suitable for vnpy single-asset CTA framework** — requires cross-sectional portfolio selection
5. **Look-ahead bias risk** — ensure MA computation uses only historical data
6. **Survivorship bias** in SP600 backtest without delisted constituents

---

## Verdict

| Dimension | Rating (1-5) |
|-----------|--------------|
| **Data Quality** | ⭐⭐⭐ (SP600 constituents, survivorship bias concern) |
| **Rule Completeness** | ⭐⭐⭐⭐ (clear algorithm steps, but params tied to specific paper) |
| **Actionability** | ⭐⭐⭐ (requires multi-asset infrastructure, high turnover) |
| **Risk Transparency** | ⭐⭐⭐ (drawdowns disclosed, but volatility statistics limited) |
| **Novelty** | ⭐⭐⭐⭐⭐ (OLMAR is a well-respected academic algorithm) |

**Overall: 🟡 Yellow** — Excellent academic strategy with proven edge, but multi-asset requirement and extreme turnover make it challenging for single-instrument CTA implementation in vnpy.

---

## Reproduced: Single-Instrument SPY Version (2026-04-26)

We implemented a single-instrument adaptation of OLMAR for SPY using vnpy BacktestingEngine:

**Strategy Logic (Single-Instrument Adaptation):**
- Compute 25-day SMA
- Entry: close < MA × (1 - threshold) → LONG; close > MA × (1 + threshold) → SHORT
- Exit: price crosses back to MA
- Parameters: SMA period (10-60), deviation threshold (1%-15%)

**Results Summary:**

| Version | Symbol | Period | Sharpe | Trades | MaxDD | CAGR |
|---------|--------|--------|--------|--------|-------|------|
| OLMAR-SPY (default 2%) | SPY | 2014-2026 | **-0.14** | 183 | -16.6% | ~0% |
| OLMAR-SPY (5% threshold) | SPY | 2014-2026 | **0.07** | 41 | -11.8% | ~0% |
| OLMAR-SPY (OAT optimized) | SPY | 2014-2026 | 0.00 | 0 | 0% | — |

**Key Finding:** The OLMAR algorithm's edge fundamentally comes from **cross-sectional portfolio diversification** (simultaneously holding many assets, some reverting up and others down). When reduced to a single instrument, the mean reversion signal on SPY alone is too weak to generate consistent alpha — especially in a long-term trending market like the S&P 500.

**Takeaway:** This confirms the article's caveat — OLMAR is inherently a multi-asset portfolio strategy. Single-instrument simplification loses the core advantage and produces near-zero expected returns on major equity indices.
