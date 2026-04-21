# Weekly Research Recap

**原文链接**: https://www.quantseeker.com/p/weekly-research-recap-54e

**发布时间**: Mar 25, 2025

**抓取时间**: 2026-04-19 22:22:35

---

## 摘要

Weekly Research Recap
Latest research on investing and trading
QuantSeeker
Mar 25, 2025
12
2
1
Share
It’s time again to catch up on some of last week’s most interesting investing research. Below, you’ll find a carefully curated selection of research papers, with each title linking directly to the original source for those interested in further reading.
Thank you for your continued interest. If you find this useful, please consider clicking the like button, and subscribing if you haven’t already.
Cross-Asset Momentum
Capturing Time-Varying Return Predictability: The Multi-Asset Time Series Momentum Strategy
(Harris, Taylor, and Wang)
While standard time-series momentum strategies rely only on each asset's own return history, research shows that incorporating cross-asset predictability can b...

---

## 全文

Weekly Research Recap
Latest research on investing and trading
QuantSeeker
Mar 25, 2025
12
2
1
Share
It’s time again to catch up on some of last week’s most interesting investing research. Below, you’ll find a carefully curated selection of research papers, with each title linking directly to the original source for those interested in further reading.
Thank you for your continued interest. If you find this useful, please consider clicking the like button, and subscribing if you haven’t already.
Cross-Asset Momentum
Capturing Time-Varying Return Predictability: The Multi-Asset Time Series Momentum Strategy
(Harris, Taylor, and Wang)
While standard time-series momentum strategies rely only on each asset's own return history, research shows that incorporating cross-asset predictability can be beneficial. This paper explores that idea by building a dynamic strategy that trades equities, bonds, and currencies across 20 developed markets. It forms signals using rolling multivariate regressions, taking positions only when relationships are both statistically significant and directionally aligned. Compared to the traditional momentum approach, this cross-asset, time-varying approach delivers significantly higher risk-adjusted returns.
Crypto
The Strategic Bitcoin Reserve: A Hedge Against Inflation or Digital Mirage?
(Krause)
Governments typically hold stable reserve assets like gold, major currencies, and sovereign bonds to guard against inflation and support financial stability. In an unconventional move, the U.S. recently added seized Bitcoin to a new Strategic Bitcoin Reserve to hedge against dollar devaluation, diversify holdings, and signal digital finance leadership. While Bitcoin may offer long-term upside, the paper warns that its extreme volatility and ethical concerns make it a fragile foundation for national reserves and cautions against equating government adoption with reliability.
Tether Premiums and Exchange Rates: Evidence from South Korea
(Park)
When investors in South Korea face restrictions on accessing U.S. dollars, they often turn to Tether, a USD-backed stablecoin that frequently trades at a premium in Korean markets. This premium turns out to be a strong signal: when it rises, the Korean won tends to weaken the next day. In short, the findings suggest that crypto arbitrage creates real FX pressure, and in markets like Korea with partial capital controls, these flows are impactful enough to move exchange rates.
Equities
Political Uncertainty-Managed Portfolios
(Lehnert)
While the standard VIX index has had varied success as a return predictor, this paper explores an alternative: the news-implied VIX (NVIX) developed by Manela and Moreira (2017), which captures political and disaster-related uncertainty in
Wall Street Journal
headlines. The author finds that NVIX predicts higher future returns when uncertainty is elevated and proposes a dynamic strategy that increases market exposure during such periods. The strategy delivers significantly higher risk-adjusted returns than a passive buy-and-hold approach.
Commodity Risk and Forecastability of International Stock Returns: The Role of Oil Returns Skewness
(Salisu and Gupta)
While previous research has found some evidence that oil returns can predict stock returns, this paper shows that the expected skewness of oil returns is a much stronger predictor. Estimated via a quantile regression, expected skewness turns out to be a highly significant out-of-sample predictor of stock returns across both developed and emerging countries, with consistent results over horizons from one to six months.
Mispricing and Correction in Short-Term Returns
(Han, Kang, and Lee)
The standard one-month reversal strategy of buying/shorting past losers/winners has weakened in recent decades. Instead, this paper proposes combining past-month returns with a stock’s expected return, estimated using firm characteristics and machine learning. By focusing on stocks that truly deviate from their expected performance, the strategy is thought to avoid false signals and capture real mispricing, delivering six times the return of the traditional approach.
Nocturnal Trading
(Eaton, Shkilko, and Werner)
Most U.S. stock trading happens during the day, but recently, platforms have started allowing trades overnight, between 8 p.m. and 4 a.m. ET, which is especially useful for investors in Asia. Trades at night tend to be slightly more expensive and can move prices significantly, particularly for ETFs. Overnight trading is growing fast and can meaningfully impact prices, making it a viable window for reacting to news or gaining early exposure.
Fixed Income
The Growing Index Effect in the Corporate Bond Market
(Shin, Zhou, and Zhu)
Index tracking now dominates intraday trading behavior for many corporate bonds, especially those held by passive funds. As passive investing has grown, trades have increasingly concentrated around index-closing times to minimize tracking errors. For example, by 2023, more than 8% of daily bond trading volume occurred within just one minute after the index close, illustrating the influence of index tracking on market activity. While this shift has generally improved liquidity, those benefits can vanish during periods of market stress.
Machine Learning and Large Language Models
Chronologically Consistent Large Language Models
(He, Lv, Manela, and Wu)
Previous findings showing that language models can predict stock returns from news may be inflated due to lookahead bias. To address this, the authors train a series of language models in a strict walk-forward fashion: each model only sees data up to its year and is used to predict returns in the following year. By forming daily long-short portfolios based on news sentiment, they find these models match or even outperform much larger models trained on the full dataset. This suggests that significant predictive performance from LLMs and news sentiment can be achieved without worrying about lookahead bias.
AlphaSharpe: LLM-Driven Discovery of Robust Risk-Adjusted Metrics
(Yuksel)
Rather than relying solely on the Sharpe ratio, which has its shortcomings, this paper uses large language models to develop new performance metrics that adjust for downside risk, skewness, and changing market regimes. Portfolios formed by ranking stocks on these metrics consistently outperform traditional approaches like risk parity and equal weighting.
Enhanced financial sentiment analysis and trading strategy development using large language models
(Kirtac and Germano)
Large language models like OPT, BERT, and FinBERT, trained on U.S. financial news, substantially outperform traditional dictionary-based approaches at capturing sentiment and forecasting short-term stock returns. A daily long-short trading strategy based on the OPT model’s sentiment signals achieves a Sharpe ratio more than twice as high as that of the dictionary-based strategy.
Options
Trading Theta: A Strategy Exploiting Time Decay
(Lu)
This paper discusses in detail the intricacies of profiting from time decay by shorting out-of-the-money SPX and SPY puts, including the hedging techniques used to isolate time decay, contract selection methods, and cost calculations. Simulations show that, while raw returns from Theta exposure can be compelling, transaction costs often erode a significant portion of the profits. The most successful variations of the strategy apply strict trade filters and avoid holding positions over weekends or holidays when risk is elevated and returns are more volatile.
Subjective Expectations for Variance and Skewness: Evidence from Analyst Forecasts
(Chen, Li, and Yang)
Analyst reports are known to contain valuable information for investors. This study uses Morgan Stanley reports, where analysts provide bull, base, and bear price targets, to infer their expectations of a stock’s future volatility and return skewness. These expectations are extracted using a simple model based on the price range and target. By sorting stocks based on analyst-implied variance and skewness, the authors form straddle portfolios that deliver strong risk-adjusted returns when rebalanced monthly.
Trading
The theory of quantitative trading
(Berdondini)
Most people searching for patterns in market data often overlook a simple fact: many patterns arise by chance. This compilation of research papers explores why financial markets represent the most challenging environment for prediction, dominated by randomness, few stable patterns, and constant change. By blending insights from statistics, trading, and psychology, it shows how traditional tools often give a false sense of certainty.
Blogs
Duration carry
(Macrosynergy)
Timing Volatility with the VIX Term Structure
(QuantSeeker)
Trading the Spread: Bitcoin ETFs vs. Cryptocurrencies Infrastructure ETFs
(Quantpedia)
GitHub
FinanceOPS
- “Research in investment finance with Python Notebooks”
Interpretable Machine Learning
-
“A Guide for Making Black Box Models Explainable”
Quantstats
- “Portfolio analytics for quants, written in Python”
Medium
The Gordon-Fisher Expansion: A Powerful Tool for Quantitative Finance
(Filip)
18 Libraries for Time Series Feature Extraction
(Cerqueira)
A Unified Machine Learning Framework for Time Series Forecasting
(Li)
Podcasts
Ep 1331: Moritz Seibert Interview
(Michael Covel)
Intra-Day, High-Octane, Robust Futures Trading - Bob Pardo
(The Algorithmic Advantage)
Linda Raschke shares trading tips from 45 years of trading and being a hedge fund trader
(Edgewonk)
Adapt or Perish: The Truth About Edge Erosion
(Investors Underground)
Last Week’s Most Popular Links
Tactical Asset Allocation with Macroeconomic Regime Detection
(Cunha Oliveira, Sandfelder, Fujita, Dong, and Cucuringu)
Volume Shocks and Overnight Returns
(Cartea, Cucuringu, Jin, and Wilson)
Macro trading signal optimization: basic statistical learning methods
(Macrosynergy)
This Substack is reader-supported. To receive new posts and support my work, consider becoming a free or paid subscriber.
Subscribe
Disclaimer: This newsletter is for informational and educational purposes only and should not be construed as investment advice. The author does not endorse or recommend any specific securities or investments. While information is gathered from sources believed to be reliable, there is no guarantee of its accuracy, completeness, or correctness.
This content does not constitute personalized financial, legal, or investment advice and may not be suitable for your individual circumstances. Investing carries risks, and past performance does not guarantee future results. The author and affiliates may hold positions in securities discussed, and these holdings may change at any time without prior notification.
The author is not affiliated with, sponsored by, or endorsed by any of the companies, organizations, or entities mentioned in this newsletter. Any references to specific companies or entities are for informational purposes only.
The brief summaries and descriptions of research papers and articles provided in this newsletter should not be considered definitive or comprehensive representations of the original works. Readers are encouraged to refer to the original sources for complete and authoritative information.
This newsletter may contain links to external websites and resources. The inclusion of these links does not imply endorsement of the content, products, services, or views expressed on these third-party sites. The author is not responsible for the accuracy, legality, or content of external sites or for that of any subsequent links. Users access these links at their own risk.
The author assumes no liability for losses or damages arising from the use of this content. By accessing, reading, or using this newsletter, you acknowledge and agree to the terms outlined in this disclaimer.
12
2
1
Share

---

*由 Substack Strategy Tracker 自动抓取*
