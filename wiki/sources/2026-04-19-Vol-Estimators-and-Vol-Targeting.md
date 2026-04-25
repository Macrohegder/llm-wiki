# Vol Estimators and Vol Targeting

**Source**: [[2026-04-19-Vol-Estimators-and-Vol-Targeting]] | [QuantSeeker](https://www.quantseeker.com/p/vol-estimators-and-vol-targeting)
**Date**: 2026-04-19
**Tags**: #article #substack

## One-Sentence Summary

> Vol Estimators and Vol Targeting
The impact of volatility estimators on performance
QuantSeeker
Oct 25, 2024
∙ Paid
9
1
Share
Introduction
Volatility targeting has been shown to increase risk-adjusted...

## Key Insights

1. **原文来源**: [QuantSeeker](https://www.quantseeker.com/p/vol-estimators-and-vol-targeting)

## Full Content

Vol Estimators and Vol Targeting
The impact of volatility estimators on performance
QuantSeeker
Oct 25, 2024
∙ Paid
9
1
Share
Introduction
Volatility targeting has been shown to increase risk-adjusted returns for certain assets and strategies. But does the choice of volatility estimator matter? In this blog post, I explore nine different estimators, ranging from daily to intraday volatility measures, and evaluate their impact on volatility targeting performance.
Background
Research has found that volatility targeting can increase risk-adjusted returns, particularly for certain types of assets. For example, Harvey et al. (2018) show that volatility targeting is especially effective for assets or strategies where the correlation between returns and volatility is negative, such as equities or credit, leading to higher risk-adjusted returns and a lower likelihood of extreme outcomes. However, the impact of volatility targeting on risk-adjusted returns in other asset classes appears to be more muted. Additionally, several studies have demonstrated that volatility targeting can be beneficial for specific strategies, such as long-short equity momentum and FX carry, by mitigating crash risk and increasing Sharpe ratios.
Volatility scaling is typically performed by adjusting portfolio weights at each rebalancing date. This is done by dividing the target volatility by a measure of expected volatility, which is based on either past data or forecasted volatility for the asset or strategy.
\(r_{s, t+1} = \frac{\sigma_{\text{target}}}{\sigma_{\text{expected},t}} r_{r, t+1},\)
where subscripts
s
and
r
denote scaled and raw returns, respectively. The focus of this blog post is on what to use as the denominator in volatility scaling.
Continue reading this post for free, courtesy of QuantSeeker.
Claim my free post
Or purchase a paid subscription.

---

*由 Substack Strategy Tracker 自动抓取*

---

*Imported from Substack on 2026-04-25*
