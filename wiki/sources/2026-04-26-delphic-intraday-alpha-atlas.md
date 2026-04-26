---
title: "The Intraday Alpha Atlas: What Works on 30-Minute Bars"
author: "Delphic Alpha"
url: "https://open.substack.com/pub/delphicalpha/p/the-intraday-alpha-atlas-what-works"
date: "2026-04-26"
topics: ["intraday", "alpha", "30-minute", "momentum", "mean-reversion", "delphic-alpha"]
source: "substack"
---

# The Intraday Alpha Atlas: What Works on 30-Minute Bars

> 来源: [Delphic Alpha](https://delphicalpha.substack.com) | 原文链接: [点击阅读](https://open.substack.com/pub/delphicalpha/p/the-intraday-alpha-atlas-what-works)

In thedaily Alpha Atlas, commodity trend was the top alpha at Sharpe 2.20. Zoom to 30-minute bars and it flips to−2.33— but that negative Sharpe is just as valuable. Flip the signal and you have a fade-the-breakout strategy at |Sharpe| 2.85 in bonds, 2.52 in FX, 2.33 in commodities. The alpha map doesn't just shift with frequency. It inverts — and the inversions are tradable.

This post applies the identical 12 parameter-free alphas to30-minute barsacross the same 5 asset classes. The lookback windows — 5, 20, and 120 bars — now correspond to ~2.5 hours, ~10 hours, and ~60 hours respectively. Everything else is unchanged: no optimisation, no fitting, no lookahead.

But this time, I'm adding a dimension the daily Atlas didn't have:tradability. For every signal, I compute return per trade (RPT) per unit bet — what you'd actually earn per directional trade assuming a fixed ±1 position. Intraday alpha research without a turnover lens is incomplete.

A methodological note: all signals usedelay_1(close)— the previous bar's close — instead of the current close. This avoids a subtle shared-variable bias whereclose_tappears in both the signal and the return denominator(close_{t+1} − close_t) / close_t. Without this correction, Sharpe ratios can be inflated by 50–80%. The numbers in this post are bias-corrected.

For every strategy, I now compute:trades per year(sign-changes in the signal),average holding periodin bars, andedge per trade(total PnL divided by number of directional flips). These numbers separate the alphas that areinteresting on paperfrom those that areimplementable in practice.


## Signal Definitions


12 alphasfrom4 families, each computed at three lookback horizonsN ∈ {5, 20, 120}bars:

Each family is oriented so thatpositive Sharpe = winning directionon intraday bars. Families where the original trend/momentum direction loses intraday are flipped to their profitable mean-reversion counterpart:

- Fade Breakout.GoshortwhenP_t > max(P_{t-N:t-1}),longwhenP_t < min(P_{t-N:t-1}). Fades Donchian channel breakouts — the opposite of trend-following. At N=5 this fades breakouts of the last 2.5 hours.

Fade Breakout.GoshortwhenP_t > max(P_{t-N:t-1}),longwhenP_t < min(P_{t-N:t-1}). Fades Donchian channel breakouts — the opposite of trend-following. At N=5 this fades breakouts of the last 2.5 hours.

- Fade MA.Goshortwhen price is above the N-bar SMA,longwhen below. Fades MA crossovers. At N=120, this fades a 2.5-day moving average.

Fade MA.Goshortwhen price is above the N-bar SMA,longwhen below. Fades MA crossovers. At N=120, this fades a 2.5-day moving average.

- CS Reversion.Buy relativelosers, sell relativewinners— the negative of cross-sectional momentum. Rank assets byP_t / SMA_N, go short the strongest and long the weakest.

CS Reversion.Buy relativelosers, sell relativewinners— the negative of cross-sectional momentum. Rank assets byP_t / SMA_N, go short the strongest and long the weakest.

- Mean Reversion (MR).s_t = −z_twherez_t = (P_t − μ_N) / σ_N. Buy oversold, sell overbought. The classic time-series mean-reversion alpha.

Mean Reversion (MR).s_t = −z_twherez_t = (P_t − μ_N) / σ_N. Buy oversold, sell overbought. The classic time-series mean-reversion alpha.

Applied identically to29 instrumentsacross 5 asset classes:

- Equity index futures:ES, NQ, YM, NKD, FTSE, DAX

Equity index futures:ES, NQ, YM, NKD, FTSE, DAX

- Bond futures:TN, UB, ZN, ZF, ZT

Bond futures:TN, UB, ZN, ZF, ZT

- Commodity futures:GC, SI, CL, HG, ZW, ZC

Commodity futures:GC, SI, CL, HG, ZW, ZC

- G7 FX:EUR, GBP, JPY, AUD, CAD, CHF vs USD

G7 FX:EUR, GBP, JPY, AUD, CAD, CHF vs USD

- Crypto:BTC, ETH, SOL, XRP, DOGE, ADA

Crypto:BTC, ETH, SOL, XRP, DOGE, ADA

Period: March 2022 – February 2026 (~4 years). Sharpe ratios annualised from monthly returns. Each instrument contributes ~50,000 bars — roughly 40× the sample size of a daily backtest over the same period.


## The Alpha × Asset Class Heatmap


Each cell shows the annualised Sharpe (left) and return per trade per unit bet (right) for one alpha–asset class pair:

Left: annualised Sharpe. Right: RPT — return per trade assuming a ±1 unit position. All signals use delay_1(close). No costs, no fitting, no lookahead.

Four patterns jump out:

- Fade-the-breakout dominates.Fade 5-bar breakout is the top alpha in bonds (2.85), FX (2.51), commodities (2.33), and crypto (1.79). This is the single strongest finding: intraday breakouts don't follow through — they revert.

Fade-the-breakout dominates.Fade 5-bar breakout is the top alpha in bonds (2.85), FX (2.51), commodities (2.33), and crypto (1.79). This is the single strongest finding: intraday breakouts don't follow through — they revert.

- All four families are now mean-reverting.Fade breakout, Fade MA, CS reversion, and time-series MR all express the same underlying effect: intraday price overshoots revert. Bonds and FX are 12/12 positive. Commodities 10/12. The heatmap is predominantly green.

All four families are now mean-reverting.Fade breakout, Fade MA, CS reversion, and time-series MR all express the same underlying effect: intraday price overshoots revert. Bonds and FX are 12/12 positive. Commodities 10/12. The heatmap is predominantly green.

- Fade breakout beats continuous MR.Fade 5-bar breakout at Sharpe 2.3–2.9 roughly doubles MR 5-bar zscore at 1.0. The ternary signal (fire only at range extremes) is structurally cleaner than the continuous z-score approach.

Fade breakout beats continuous MR.Fade 5-bar breakout at Sharpe 2.3–2.9 roughly doubles MR 5-bar zscore at 1.0. The ternary signal (fire only at range extremes) is structurally cleaner than the continuous z-score approach.

- Equities remain a coin flip.Best equity alpha: CS-Rev 5-bar at 0.47. Only 3/12 strategies are positive. Equity index futures are too efficiently arbitraged for simple signals to gain traction at any frequency.

Equities remain a coin flip.Best equity alpha: CS-Rev 5-bar at 0.47. Only 3/12 strategies are positive. Equity index futures are too efficiently arbitraged for simple signals to gain traction at any frequency.


## Best Strategy per Asset Class


When we treat negative Sharpes as equally tradable (by flipping the signal), the picture is clear:flipped 5-bar breakout is the strongest signal in 4 of 5 classesat |Sharpe| 1.8–2.9. MR 5-bar zscore is the strongestunflippedsignal in bonds (1.04), FX (1.03), and commodities (0.96).

Both are expressing the same insight: at intraday frequencies, the dominant regularity across liquid markets istransient mean reversion. The flipped breakout implements this by fading range extremes; the MR z-score implements it continuously. The breakout version is stronger because it fires selectively at extreme points rather than continuously.


## The Overfitting Tax


I split the data at March 2024 — 2 years in-sample, 2 years out-of-sample — and regressed OOS Sharpe on IS Sharpe for every alpha–asset combination. All signals are already oriented in the profitable direction.

The core advantage of intraday data: ~40× more observations per unit time means your Sharpe estimates are structurally more precise than daily backtests. What you see in-sample is closer to what you get out-of-sample.


## The Tradability Lens: Turnover, Holding Period, and Edge per Trade


Gross Sharpe is necessary but not sufficient. Every strategy here was evaluated for three additional metrics computed directly from the signals:

- Trades per year— the number of directional sign-changes in the signal (a position flip from long to short, or vice versa).

Trades per year— the number of directional sign-changes in the signal (a position flip from long to short, or vice versa).

- Average holding period— mean number of 30-minute bars between sign-changes. A holding period of 1.3 bars means the signal flips direction roughly every 40 minutes.

Average holding period— mean number of 30-minute bars between sign-changes. A holding period of 1.3 bars means the signal flips direction roughly every 40 minutes.

- Edge per trade— total PnL divided by the number of sign-changes. This is what survives (or doesn't) after you pay the spread.

Edge per trade— total PnL divided by the number of sign-changes. This is what survives (or doesn't) after you pay the spread.

Here are the top 10 positive-Sharpe strategies with their tradability profiles:

All signals oriented so positive Sharpe = winning direction. Fade = short on breakout/MA crossover (mean reversion at extremes). CS-Rev = buy cross-sectional losers, sell winners. RPT = return per trade per unit bet. Mar 2022 – Feb 2026.

A signal with Sharpe −2.85 is exactly as tradable as one with +2.85 — you just take the opposite position. The table above ranks by |Sharpe| and marks flipped signals with *. Key patterns:

- Fade-the-breakout dominates.Flipping the 5-bar breakout signal (go short when price breaks above the range, long when it breaks below) produces |Sharpe| 2.3–2.9 in bonds, FX, and commodities. This is the strongest intraday signal in the Atlas — a mean-reversion strategy implemented at range extremes.

Fade-the-breakout dominates.Flipping the 5-bar breakout signal (go short when price breaks above the range, long when it breaks below) produces |Sharpe| 2.3–2.9 in bonds, FX, and commodities. This is the strongest intraday signal in the Atlas — a mean-reversion strategy implemented at range extremes.

- All top signals are mean-reverting.Whether implemented as flipped breakouts (ternary, firing at extremes) or MR z-scores (continuous), the winning edge is the same: intraday price overshoots revert. The breakout version is stronger because it only fires at extreme points and has cleaner signal construction.

All top signals are mean-reverting.Whether implemented as flipped breakouts (ternary, firing at extremes) or MR z-scores (continuous), the winning edge is the same: intraday price overshoots revert. The breakout version is stronger because it only fires at extreme points and has cleaner signal construction.

- RPT ranges from 0.29 to 6.64.Higher RPT means more room to absorb execution costs. Crypto trend 120-bar has the best RPT (6.64) thanks to higher volatility, but wider spreads and slippage partially offset this.

RPT ranges from 0.29 to 6.64.Higher RPT means more room to absorb execution costs. Crypto trend 120-bar has the best RPT (6.64) thanks to higher volatility, but wider spreads and slippage partially offset this.

- 5-bar signals trade 9,000–16,000 times/yearwith 1-bar holding periods. The 120-bar signals trade 2,000–4,000 times/year with 4–5 bar holds — better tradability profiles for markets with wider spreads.

5-bar signals trade 9,000–16,000 times/yearwith 1-bar holding periods. The 120-bar signals trade 2,000–4,000 times/year with 4–5 bar holds — better tradability profiles for markets with wider spreads.


## Regime Dependence


Year-by-year Sharpes for the best strategy per asset class show regime dependence similar to daily. Note that intraday alphas can pick up regime transitions faster — a macro shock that takes days to propagate through close-to-close returns appears within hours on 30-minute bars.

Rolling Sharpe panels are notably smoother than their daily counterparts — an artefact of ~40× more observations per window. This makes conditional performance evaluation more reliable: you can distinguish a genuine regime shift from sampling noise with much less lag.


## Diversification at Higher Frequency


Intraday cross-asset correlations arestructurally lowerthan daily. At the 30-minute scale, asset-specific microstructure effects — session times, venue fragmentation, market-maker inventory cycles — dominate over shared macro factors. The implication: multi-asset deployment offers even greater diversification benefit intraday than daily.


## Equity Curves by Asset Class


Cumulative risk-adjusted PnL by alpha family (4 panels) and lookback horizon (3 lines each), on 30-minute bars:


### Equity Index Futures



### Bond Futures



### Commodity Futures



### G7 FX



### Crypto


Note the MR-5 curves in bonds, FX, and commodities: steep, consistent, and almost monotonically increasing. Contrast with the CS panels: uniformly negative across all asset classes.


## Takeaways


- The alpha map inverts — and the inversions are tradable.Daily commodity trend (+2.20) becomes −2.33 on 30M. Flip that signal and you have a fade-the-breakout strategy at |Sharpe| 2.33. Negative Sharpes are just as valuable as positive ones.

The alpha map inverts — and the inversions are tradable.Daily commodity trend (+2.20) becomes −2.33 on 30M. Flip that signal and you have a fade-the-breakout strategy at |Sharpe| 2.33. Negative Sharpes are just as valuable as positive ones.

- Fade-the-breakout is the strongest intraday alpha.Flipped 5-bar breakout achieves |Sharpe| 2.3–2.9 in bonds, FX, and commodities. It's a mean-reversion strategy that fires selectively at range extremes — stronger and cleaner than continuous z-score approaches.

Fade-the-breakout is the strongest intraday alpha.Flipped 5-bar breakout achieves |Sharpe| 2.3–2.9 in bonds, FX, and commodities. It's a mean-reversion strategy that fires selectively at range extremes — stronger and cleaner than continuous z-score approaches.

- RPT separates tradable from theoretical.Flipped breakout in bonds has RPT 0.85 across ~9,000 trades/year. Crypto trend 120-bar has RPT 6.64 across ~3,800 trades. Higher RPT means more room for execution costs.

RPT separates tradable from theoretical.Flipped breakout in bonds has RPT 0.85 across ~9,000 trades/year. Crypto trend 120-bar has RPT 6.64 across ~3,800 trades. Higher RPT means more room for execution costs.

- Everything is mean reversion at 30 minutes.Whether via flipped breakouts, z-score fading, or flipped MA crossovers, every winning strategy exploits the same microstructure effect: intraday overshoots revert within 1–2 bars.

Everything is mean reversion at 30 minutes.Whether via flipped breakouts, z-score fading, or flipped MA crossovers, every winning strategy exploits the same microstructure effect: intraday overshoots revert within 1–2 bars.

- The strongest portfolio runs both timescales.Daily trend + intraday fade-the-breakout: structurally uncorrelated, mechanistically distinct, and mutually beneficial for execution.

The strongest portfolio runs both timescales.Daily trend + intraday fade-the-breakout: structurally uncorrelated, mechanistically distinct, and mutually beneficial for execution.

The bottom line: zoom from daily to 30-minute and the alpha map inverts. The strongest intraday signal is fade-the-breakout — flipping the very trend signals that work on daily bars. The best systematic portfolio runs both timescales, capturing daily trends and intraday reversions as complementary, uncorrelated legs.
