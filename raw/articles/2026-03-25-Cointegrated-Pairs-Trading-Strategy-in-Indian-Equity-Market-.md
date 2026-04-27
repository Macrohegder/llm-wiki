---
title: "Cointegrated Pairs Trading Strategy in Indian Equity Market (2015–2025) | EPAT Project"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/cointegrated-pairs-trading-indian-equity-market-epat-project/"
date: "2026-03-25"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Cointegrated Pairs Trading Strategy in Indian Equity Market (2015–2025) | EPAT Project

**来源**: [QuantInsti](https://blog.quantinsti.com/cointegrated-pairs-trading-indian-equity-market-epat-project/)  
**日期**: 2026-03-25  
**作者**: QuantInsti

---

## 原文

Statistical Arbitrage Using Cointegrated Stock Pairs in Indian Equity Market (2015-2025) | EPAT Project

About the author

Shant Tondonbrings a diverse background blending financial markets analysis, consulting, and entrepreneurship. He holds a Bachelor's in Commerce with a focus on Financial Markets from Narsee Monjee College of Commerce and Economics, and completed his High School Diploma in Business/Commerce at Mayo College, Ajmer.

Professionally, Shant gained early analytical experience as an intern at Teach For India and KPMG in Mumbai, followed by a role as an Analyst at PwC.

Project Abstract

This project builds and evaluates a market-neutral pairs trading strategy focusing on 25 NSE large-cap stocks spanning the Banking, IT, Pharma, Cement, and Auto sectors. The pairs are selected using a residual stationarity test, specifically the ADF(0) with MacKinnon p-value, on a training sample. To ensure statistical robustness and control for false discoveries, the Benjamini–Hochberg False Discovery Rate (FDR) at 5% is applied.

The strategy trades mean-reversion via z-scores of the spread using a walk-forward train/test split. It represents a clean, defendable academic implementation with no look-ahead bias, explicit transaction costs (5 bps per leg per side), equal capital per active pair (₹5,00,000), and comprehensive portfolio-level risk metrics.

Introduction & Project Motivation

Pairs trading is a classic statistical arbitrage strategy that seeks to exploit temporary price divergences between two related assets while maintaining a market-neutral stance. This project applies this concept to the Indian equity market between January 1, 2015, and June 30, 2025.

The primary motivation was to build a rigorous prototype that addresses common algorithmic trading pitfalls, such as look-ahead bias, incomplete Profit and Loss (PnL) calculations, and inadequate multiple testing controls.

Strategy & Implementation Methodology (Technical Breakdown)

The strategy relies on a rolling walk-forward methodology utilizing a 252 trading-day training window and a 21-day test step.

1. Pair Selection & Cointegration:During the training phase, the hedge ratio (β) is estimated using Ordinary Least Squares (OLS).
    Residual stationarity is then tested using the ADF(0) t-stat to generate a MacKinnon p-value.
    The Benjamini–Hochberg FDR is applied at 5% to limit false positives.
    Three highly cointegrated pairs emerged from the framework:HDFCBANK.NSvsKOTAKBANK.NS,HEROMOTOCO.NSvsULTRACEMCO.NS, andHCLTECH.NSvsICICIBANK.NS.

2. Signal Generation Logic:To prevent look-ahead bias, the rolling variables for standard deviation and mean are strictly shifted by 1 day.

Spread Calculation:St= At- β × Bt

Z-Score Calculation:zt= (St- μt-1) / σt-1

Execution Rules:Enter when|zt| > 1.5and exit whenztcrosses 0.

Python Implementation Code

Below is a conceptual Python snippet demonstrating the core mathematical logic utilized in Shant's strategy:

import pandas as pd
import statsmodels.api as sm

def calculate_signals(train_data, test_data, stock_a, stock_b):
    # 1. Estimate Hedge Ratio (Beta) using OLS on Training Window
    model = sm.OLS(train_data[stock_a], train_data[stock_b]).fit()
    beta = model.params

    # 2. Calculate Out-of-Sample Spread
    # Spread formula: S_t = A_t - beta * B_t
    spread = test_data[stock_a] - (beta * test_data[stock_b])

    # 3. Calculate Z-Score strictly avoiding look-ahead bias
    # z_t = (S_t - mu_{t-1}) / sigma_{t-1}
    rolling_mean = spread.rolling(window=30).mean().shift(1)
    rolling_std = spread.rolling(window=30).std().shift(1)
    z_score = (spread - rolling_mean) / rolling_std

    # 4. Generate Trading Signals based on Z-Score Thresholds
    # Enter when absolute z-score > 1.5, Exit when it crosses 0
    long_entry = z_score < -1.5
    short_entry = z_score > 1.5
    exit_signal = (z_score.shift(1) * z_score <= 0)

    return z_score, long_entry, short_entry, exit_signal

3. Portfolio & Risk Management:

Sizing:Equal-weight capital allocation, assigning ₹5,00,000 per active pair.

Costs:Transaction costs are explicitly modeled at 5 bps per leg per side for entry and exit.

PnL Calculation:PnL is mapped from both legs. Any open position is force-closed on the final backtest day to ensure complete reporting.

Key Findings & Portfolio Performance

The out-of-sample backtest generated the following portfolio-level performance metrics over the test period:

Challenges & Limitations

Sizing Constraints:The allocation is educational (equal capital per pair); it does not dynamically model capacity limits or real margin constraints.

Transaction Costs:Modeled cleanly at 5 bps per leg per side, but real-world execution slippage and bid-ask spreads can differ.

ADF(0) Approximation:The model uses a lag-0 ADF for computational speed. A full ADF test with optimized lags is recommended for future iterations.

Multiple Testing:While the FDR method reduces false discoveries, it does not completely eliminate them.

Survivorship Bias:The 25-stock universe is fixed and does not dynamically account for historical index reconstitution.

Next steps

Improving Strategy Performance

While the current strategy provides a clean academic baseline, several targeted enhancements can meaningfully improve its risk-adjusted returns and real-world applicability:

1. Optimise the ADF Lag Selection

Replace the current ADF(0) shortcut with an information-criterion-based lag selector (AIC or BIC). This reduces the risk of spurious cointegration signals and improves pair selection quality, leading to more stable and reliable trade entries.

2. Expand the Universe and Diversify Pairs

The current three-pair portfolio is highly concentrated. Extending the stock universe beyond 25 large-caps to include mid-cap NSE stocks across additional sectors (Energy, FMCG, Metals) would yield a broader set of cointegrated candidates, improve diversification, and reduce the impact of any single pair breaking down.

3. Introduce Dynamic Position Sizing

The strategy currently uses a fixed ₹5,00,000 per pair. Replacing this with volatility-scaled sizing (e.g., inverse-volatility or Kelly-criterion weighting) would allocate more capital to pairs showing stronger mean-reversion signals and tighter spreads, improving overall Sharpe ratio and reducing drawdowns.

4. Refine Entry/Exit Thresholds Adaptively

The fixed z-score thresholds of ±1.5 for entry and 0 for exit are static across all market regimes. An adaptive threshold model; where entry and exit levels are calibrated to each pair’s rolling volatility or regime classification (trending vs. mean-reverting), can filter out low-quality signals and improve the win ratio beyond the current 63.47%.

5. Incorporate Stop-Loss Rules to Control Drawdown

The current maximum drawdown of -34.31% is high relative to the annualised return of 0.30%. Adding a pair-level stop-loss (e.g., exit when the z-score breaches ±3.0 or when unrealised loss exceeds a fixed percentage of allocated capital) would cap downside on regime-breaking events and substantially improve the Sharpe ratio.

6. Address Survivorship Bias with a Rolling Universe

The fixed 25-stock universe inflates historical performance by only including companies that survived the full 2015–2025 period. Using a point-in-time NSE Nifty 50 or Nifty 100 constituent list that reflects actual index composition at each training window would eliminate this bias and produce more realistic forward-looking performance estimates.Steps for continuous learning:To build on the concepts covered in this blog, such as statistical arbitrage, cointegration testing, and mean-reversion strategy development, you can explore advanced resources and structured learning paths that focus on algorithmic trading.

Start with foundational application guides likePython for Trading BasicsandMean Reversion Trading Strategyby Dr Ernest P Chan, which walk through how statistical models are built and evaluated in live financial contexts.

For those looking to go beyond supervised models,Learning Tarck on Advanced Algorithmic Tradingis ideal for complex quantitative techniques, while Factor Based Investing offers insight into strategies that adapt over time and across market regimes.

To further strengthen your modelling and evaluation skills, refer toPortfolio & Risk ManagementandBacktesting Trading Strategies. These resources offer focused guidance on the types of statistical models Shant Tondon used in his EPAT project.

If you’re ready for hands-on learning with industry guidance, explore theQuantitative TradingandArtificial Intelligence in Tradinglearning tracks. These curated paths offer end-to-end training from data handling and feature engineering to model deployment.

Finally, if you’re inspired by Shant Tondon’s structured approach and want to replicate a similar end-to-end project, consider theExecutive Programme in Algorithmic Trading (EPAT). It provides a comprehensive curriculum covering Python, statistics, machine learning, backtesting, and real-world trading applications, all essential components behind this EPAT final project.

Disclaimer: The information in this project is true and complete to the best of our Student’s knowledge. All recommendations are made without guarantee on the part of the student or QuantInsti®. The student and QuantInsti®disclaim any liability in connection with the use of this information. All content provided in this project is for informational purposes only and we do not guarantee that by using the guidance you will derive a certain profit.

---

*Imported from QuantInsti Blog on 2026-04-27*
