# Weekly Research Recap

**原文链接**: https://www.quantseeker.com/p/weekly-research-recap-0be

**发布时间**: Apr 21, 2026

**抓取时间**: 2026-04-25 08:42:59

---

## 摘要

Weekly Research Recap
Latest research on investing and trading
QuantSeeker
Apr 21, 2026
11
2
Share
This week’s Tuesday Roundup brings together the most useful investing ideas I found recently, from fresh academic studies and market research to thoughtful blog posts and smart discussions online. Links are included throughout so you can explore further.
Commodities
Spot-Based Basis and Basis Momentum in Commodity Futures Markets
(Luo and Xue)
A smarter way to trade commodity futures may be to look beyond the futures curve itself. Using 41 Chinese commodities, basis and basis-momentum signals built from actual spot prices and futures prices beat traditional basis/carry measures. The strongest spread implied a return of +1.73% per month with a Sharpe of roughly 1.40.
Key takeaway: Spot-market ...

---

## 全文

Weekly Research Recap
Latest research on investing and trading
QuantSeeker
Apr 21, 2026
11
2
Share
This week’s Tuesday Roundup brings together the most useful investing ideas I found recently, from fresh academic studies and market research to thoughtful blog posts and smart discussions online. Links are included throughout so you can explore further.
Commodities
Spot-Based Basis and Basis Momentum in Commodity Futures Markets
(Luo and Xue)
A smarter way to trade commodity futures may be to look beyond the futures curve itself. Using 41 Chinese commodities, basis and basis-momentum signals built from actual spot prices and futures prices beat traditional basis/carry measures. The strongest spread implied a return of +1.73% per month with a Sharpe of roughly 1.40.
Key takeaway: Spot-market information may contain carry signals that are missed by futures-only models.
Equities
Five-Factor Market-Neutral Strategy Across Korean and U.S. Equity Markets: Structural Alpha Without Regime Filters
(Quinn)
A market-neutral strategy spanning Korean and U.S. equities reports unusually strong performance: A Sharpe ratio of 3.64, a maximum drawdown of just -0.3%, and an 12.8% annual alpha after controlling for six standard factors. It combines five low-correlation signals from distinct return sources.
Key takeaway: Diversifying across multiple niche inefficiencies usually matters more than chasing a few crowded factors.
Commodity Price Risk and the Cross-Section of Equity Returns
(Dong and Palazzi)
U.S. stocks whose returns deviate from levels implied by market + commodity risk exposures tend to reverse next month. Underpriced minus overpriced stocks earned 1.86% monthly, equal-weighted, with a Sharpe of 1.31, the strongest in smaller, less-followed names.
Key takeaway: Commodity-linked mispricing may be a niche source of alpha.
Momentum Returns and the Role of Liquidity Improvements
(Bro)
Momentum may not be a standalone anomaly at all. This paper argues that much of classic stock momentum reflects improving liquidity: Past winners become easier to trade, while losers become harder. A long-short liquidity-improvement factor returned 0.65% per month (roughly 0.69 annualized Sharpe) and rendered momentum alpha insignificant in factor tests.
Key takeaway: Some momentum profits may stem from gradual repricing to changing liquidity conditions.
Factor Investing
Factor Investing in Emerging Markets: From Multi-Factor Industry Portfolios to a Market-Neutral Alpha Strategy
(Zhang, Dong, He, and Zheng)
This paper tests factor investing in emerging markets using strict out-of-sample splits. A beta-hedged EM strategy built from six classic signals (size, value, quality, momentum, low vol, yield) delivered a gross Sharpe of 0.83, 0.67 net after costs, 4.16% annual alpha, and just -5.2% max drawdown (2019 to 2024).
Key takeaway: In emerging markets, diversified simple factors can still deliver strong risk-adjusted returns.
FX
Survival of the Fittest: A Three-Factor Model in the Currency Market
(Liu, Wang, and Zhao)
The crowded “currency factor zoo” may boil down to three core drivers: Dollar (DOL), Carry (CAR), and Output Gap (GAP). Using Bayesian model selection on 1991 to 2024 FX data, this trio ranked highest versus popular alternatives and best explained rival factors. In the authors’ recursive portfolio test, it posted a 1-year out-of-sample annualized Sharpe of 2.99.
Key takeaway: In FX, parsimonious macro factor models may beat complexity.
Machine Learning and Large Language Models
Machine Learning and Technical Analysis in International Market
(Chin and Lin)
Across 25 equity markets, machine learning outperformed OLS when using 107 technical price/volume signals. Global long-short monthly returns reached 1.15% vs 0.58%, with ML also adding value among large firms and in down markets.
Key takeaway: Technical indicators may still contain alpha, and flexible models seem better at extracting it.
Option Return Predictability via Large Language Models
(Liu, Zhou, Cheng, Zou, and Wang)
GPT-5 is tested as an autonomous generator of option-return factors in U.S. and Chinese markets using only option characteristics. In a post-Sept 2024 out-of-sample test, many generated factors beat benchmarks and delivered significant positive alpha. Many reported Sharpe ratios were strong, based on backtests of delta-hedged portfolios.
Key takeaway: LLMs may become valuable tools for idea generation in niche, high-dimensional markets.
Timing Currency Factors with Machine Learning
(Torok)
Machine learning may help time FX factors, but gains are concentrated in specific cases. This paper tests 264 signals across currencies, options, equities, and macro data to time carry and USD factors. Most individual predictors added little, but Developed Market USD timing improved Sharpe by 0.4 to 0.5 in 2012–2024 out-of-sample tests.
Key takeaway: In FX, ML may be most useful for selective risk timing rather than broad forecasting.
Latency Alpha: Real-Time LLM-Based Semantic Extraction of EIA Petroleum Data for Forecasting and Trading Crude Oil Futures
(Pape)
This paper tests an LLM system that reads the weekly EIA petroleum report in real time, converts report surprises into trading signals, and trades WTI futures. In a 2022 to 2023 backtest (88 releases), it reports a Sharpe of 1.82, a Sortino ratio of 2.89, 31.2% cumulative return, and a 68.5% hit rate.
Key takeaway: In event-driven markets, faster semantic interpretation of public data may create temporary alpha opportunities.
Interpretable Systematic Risk around the Clock
(He)
The author uses U.S. equity market data plus an open-source LLM to identify what drives major market jumps. Macroeconomic jump risk earned the strongest premium: 3.65% annually with a Sharpe of 0.78 (vs market 0.53). A real-time strategy rotating into the best-priced jump-risk theme each year reached a Sharpe of 0.95 out of sample.
Key takeaway: Not all volatility is equal; macro shocks appear to earn the richest compensation.
Portfolio Construction
Measuring Strategy-Decay Risk: Minimum Regime Performance and the Durability of Systematic Investing
(Alexander and Fabozzi)
Many quant strategies look strong in backtests but weaken across regimes. A new paper proposes Minimum Regime Performance (MRP): The worst Sharpe observed across historical environments. Among the tested equity factors, only Quality kept a positive MRP, while Size and Investment looked fragile.
Key takeaway: Judge the durability of strategies across regimes, not just average Sharpe.
Dynamic Allocation with Macro Factor-Mimicking Portfolios
(Molinaro and Chaudron)
Inflation may be more tradable than investors think. This paper ranks stocks by inflation beta, builds high- and low-inflation-beta portfolios, then uses macro forecasts to rotate between them. The best strategy delivered 21.4% annual return with a Sharpe of 1.09.
Key takeaway: Forecasting macro regimes may add value when expressed through targeted inflation-sensitive equity exposures.
Blogs
Inflation as a trading signal
(Macrosynergy)
Pairs Trading in the Metals Complex: A Reality Check
(Quantseeker)
From Risk Premia to Constraints: How Markets Really Clear
(CFA Institute)
Annual performance update- year 12
(Rob Carver)
Exploiting Mean-Reversion in Decentralized Prediction Markets: Evidence from Polymarket Binary Contracts
(Quantpedia)
Podcasts
“It’s the Dumbest Market in the World” - Quant Trader Scott Phillips on Edge in Crypto
(Odds on Open)
Markets Look Calm… But Are They? ft. Rob Carver
(Top Traders Unplugged)
$1,900 Small Cap Trader Hit $2.9 Mil in Profits · Eduardo Briceño
(Chat with Traders)
Social Media & Industry Research
Quantitative Trading Is Going To Eat All Markets
(SystematicLongShort)
How should you size your trend trades?
(Concretum Research)
Mastering Claude Code in 30 Minutes
(via Movez)
Can you trust your intraday database?
(Concretum Research)
Last Week’s Most Popular Links
Optimal Buy-and-Hold Asset Allocation: A Multi-Horizon Drawdown-Constrained Approach
(Wang and Wang)
Can AI Do Financial Research? LLM-Guided Hypothesis Discovery in Asset Pricing
(Liu, Liu, Liu, and Mei)
Don’t Mix What Should Be Separated: Why Combining Value and Momentum Signals Destroys Alpha
(Morales)
This Substack is reader-supported. To receive new posts and support my work, consider becoming a free or paid subscriber.
Subscribe
Disclaimer: This newsletter is for informational and educational purposes only and should not be construed as investment advice. The author does not endorse or recommend any specific securities or investments. While information is gathered from sources believed to be reliable, there is no guarantee of its accuracy, completeness, or correctness.
This content does not constitute personalized financial, legal, or investment advice and may not be suitable for your individual circumstances. Investing carries risks, and past performance does not guarantee future results. The author and affiliates may hold positions in securities discussed, and these holdings may change at any time without prior notification.
The author is not affiliated with, sponsored by, or endorsed by any of the companies, organizations, or entities mentioned in this newsletter. Any references to specific companies or entities are for informational purposes only.
The brief summaries and descriptions of research papers and articles provided in this newsletter should not be considered definitive or comprehensive representations of the original works. Readers are encouraged to refer to the original sources for complete and authoritative information.
This newsletter may contain links to external websites and resources. The inclusion of these links does not imply endorsement of the content, products, services, or views expressed on these third-party sites. The author is not responsible for the accuracy, legality, or content of external sites or for that of any subsequent links. Users access these links at their own risk.
The author assumes no liability for losses or damages arising from the use of this content. By accessing, reading, or using this newsletter, you acknowledge and agree to the terms outlined in this disclaimer.
Paid subscriptions may not be available in all jurisdictions and may change without notice.
11
2
Share

---

*由 Substack Strategy Tracker 自动抓取*
