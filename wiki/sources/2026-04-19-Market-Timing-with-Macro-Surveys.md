# Market Timing with Macro Surveys

**Source**: [[2026-04-19-Market-Timing-with-Macro-Surveys]] | [QuantSeeker](https://www.quantseeker.com/p/market-timing-with-macro-surveys)
**Date**: 2026-04-19
**Tags**: #article #substack

## One-Sentence Summary

> Market Timing with Macro Surveys
Reducing Equity Exposure Around Recessions
QuantSeeker
May 26, 2025
9
1
Share
Introduction
Hi there. In recent months, there has been increased chatter about the possi...

## Key Insights

1. **原文来源**: [QuantSeeker](https://www.quantseeker.com/p/market-timing-with-macro-surveys)

## Full Content

Market Timing with Macro Surveys
Reducing Equity Exposure Around Recessions
QuantSeeker
May 26, 2025
9
1
Share
Introduction
Hi there. In recent months, there has been increased chatter about the possibility of a recession triggered by President Trump’s tariff war. The recent pause in tariffs appears to have eased some of those concerns. For example, JP Morgan now
sees
the likelihood of a U.S. recession to be below 50%, and the
recession odds
on Polymarket currently hover around 40%.
For investors, recessions are notoriously difficult to time, and they are typically announced only after the fact, making official recession declarations of limited use for market timing. Prior research has explored early-warning signals such as the yield curve or credit growth, but these indicators can be noisy or lagging. Rather than relying on individual macro signals, a growing literature on economic nowcasting has shown promise in aggregating real-time macro data to track economic conditions and anticipate downturns.
Nowcasting, however, comes with its own challenges, such as infrequent data updates, revisions, and noise. For example,
Beber et al. (2015)
present a straightforward method for obtaining real-time estimates of inflation, growth, and sentiment from a broad set of macroeconomic releases. More recently,
Jain (2022)
discusses the application of machine learning and alternative data to macro nowcasting. See also the recent contribution by
Kislitskiy et al. (2025)
on nowcasting U.S. GDP.
An interesting paper by
Gomez-Cram (2022)
finds that stock markets are slow to incorporate the onset of recessions, as investors tend to underreact to deteriorating macroeconomic conditions. This delay leads to several months of negative equity returns after a recession begins. The paper proposes a dynamic market timing strategy that reduces equity exposure when expected returns decline, typically during early recession phases, and reallocates to cash. This approach improves Sharpe ratios by approximately 30% compared to a standard buy-and-hold strategy.
Recession Beliefs
In a recent paper,
Sun (2025)
uses recession beliefs from the Survey of Professional Forecasters (SPF) to time equity and bond allocations. Using quarterly data from 1982 to 2024, the paper finds that SPF recession probabilities help predict NBER recessions one or more quarters in advance and can be used to shift out of a traditional 60/40 portfolio into bonds or cash.
For example, switching from a 60/40 portfolio to bonds based on SPF signals improves the Sharpe ratio from 0.74 to 0.95, a 28% improvement, and significantly reduces maximum drawdowns. The SPF-based signals are also compared with other common indicators such as consumer sentiment surveys and alternative SPF forecasts. Across all comparisons, recession beliefs emerge as the most consistent and effective signals for both recession forecasting and portfolio allocation.
Testing a Market Timing Strategy
Average Recession Beliefs
I test a variant of these findings by implementing a simple market timing strategy that switches between SPY and TLT, using ETF data obtained from EODHD. Since SPY data begins in 1993 and TLT only starts in 2002, I assume the strategy switches to the risk-free rate (cash) before 2002. I source the SPF recession beliefs (Mean Responses) from the
Survey of Professional Forecasters
, provided by the Federal Reserve Bank of Philadelphia. These beliefs reflect the “
Probability that real GNP/GDP will decline (quarter over quarter) in the quarter in which the survey was conducted (RECESS1) and the following four quarters (RECESS2 to RECESS5).
”
The survey is conducted quarterly, with the response deadline and release date typically falling in the second month of each quarter. For example, the recession probabilities reported since early 2024 are as follows:
The latest data was released on May 16 and shows a sharp increase in recession probabilities, with the estimated probability for the next quarter (Q3 2025) rising to 36.09%. Following the approach in Sun (2025), I define the recession signal as the change in recession probabilities for the upcoming quarter:
Recession Signal: (RECESS2 - Lagged RECESS3)
> 0
In the example above, the last signal would be 36.09 - 19.83, which exceeds zero. The market timing rule switches out of stocks whenever the signal exceeds zero.
Dispersion of Recession Beliefs
In addition to the level of recession beliefs, I also test a timing signal based on the dispersion of those beliefs. While this dimension is not explored in Sun (2025), prior research has shown that increased uncertainty or disagreement among investors often signals weaker near-term market performance. To compute dispersion, I use the Individual Responses dataset from the same
source
. This dataset provides recession probability forecasts for each participant (ID) across various horizons. An excerpt is shown below.
I define the dispersion of beliefs as the cross-sectional standard deviation of

---

*Imported from Substack on 2026-04-25*
