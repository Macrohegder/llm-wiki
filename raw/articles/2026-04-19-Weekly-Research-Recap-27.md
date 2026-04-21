# Weekly Research Recap

**原文链接**: https://www.quantseeker.com/p/weekly-research-recap-c48

**发布时间**: Sep 02, 2025

**抓取时间**: 2026-04-19 22:25:42

---

## 摘要

Weekly Research Recap
Latest research on investing and trading
QuantSeeker
Sep 02, 2025
8
1
Share
Hi there. It's time for this week’s research recap, highlighting top investing insights from the past week with direct links to the full sources.
Equities
Global News Networks and Return Predictability
(Freire, Moin, Quaini, and Soebhag)
News sentiment, extracted from a massive global article dataset, predicts daily equity index returns across 14 developed markets. Local sentiment strategies nearly double buy-and-hold Sharpe ratios (e.g., U.S. 1.34 vs. 0.62), with net alphas of about 16% after trading costs and one-third smaller drawdowns. Adding cross-border news flows delivers further gains, with sizeable alphas. Hence, both local and global sentiment are shown to provide tradable signals fo...

---

## 全文

Weekly Research Recap
Latest research on investing and trading
QuantSeeker
Sep 02, 2025
8
1
Share
Hi there. It's time for this week’s research recap, highlighting top investing insights from the past week with direct links to the full sources.
Equities
Global News Networks and Return Predictability
(Freire, Moin, Quaini, and Soebhag)
News sentiment, extracted from a massive global article dataset, predicts daily equity index returns across 14 developed markets. Local sentiment strategies nearly double buy-and-hold Sharpe ratios (e.g., U.S. 1.34 vs. 0.62), with net alphas of about 16% after trading costs and one-third smaller drawdowns. Adding cross-border news flows delivers further gains, with sizeable alphas. Hence, both local and global sentiment are shown to provide tradable signals for market timing.
On the Macroeconomic Foundations of the Anomaly Zoo
(O’Doherty, Wang, and Yan)
Many stock market anomalies can be explained by macroeconomic risks. Out of 190 macro variables, 43 carry significant risk premia. Two-factor models based on NIPA (National Income and Product Accounts) aggregates and housing variables cut average anomaly alphas by more than 60%, often outperforming leading benchmark models. For instance, industrial production explains roughly 85% of momentum profits, while housing factors nearly eliminate value/growth anomalies. Thus, many anomalies reflect compensation for macroeconomic risk rather than mispricing.
Cross-Sectional Spillovers of Earnings Surprises and Asset Price Anomalies
(He and Zhang)
Earnings surprises spill over to peers identified via textual similarity in earnings calls, lifting related stocks and producing a drift lasting up to 20 days. A long–short portfolio earns 11% annually with a Sharpe ratio of 1.75 (before costs). At the factor level, aggregated spillovers forecast value and size premia and explain most anomaly alphas post-2009. Overall, the findings show that cross-firm earnings news diffuses gradually, reflecting underreaction in peer stock prices.
Volatility-Weighted Concentration and Effective Fragility in U.S. Equity Markets
(Nagaram and Phadke)
U.S. equity markets are now more concentrated than at any point in the past 60 years, with the top five firms comprising about 25% of the S&P 500, and index concentration implying effective diversification of only about 48 stocks. Recent returns have been overwhelmingly powered by the “Magnificent 7”; stripping them out leaves the index flat. Investors should note that cap-weighted indexing today carries hidden fragility, making diversification beyond mega-cap tech essential.
Machine Learning and Large Language Models
Centaur Trading: Human-machine integration in stock market prediction
(Matuozzo, Yoo, and Provetti)
This paper introduces Centaur Trading, where human experts guide neural networks by selecting historically relevant training periods instead of relying solely on recent data. While the authors emphasize that this choice is best made through domain expertise, they note that future work could employ financial LLMs or automated search tools to identify past regimes most comparable to current conditions. The key insight is that human judgment combined with machine learning outperforms either approach in isolation, especially during paradigm shifts.
Do Sell-side Analyst Reports Have Investment Value?
(Lv)
The paper studies whether the written narratives in analyst reports add predictive value. It processes 1.2 million reports (2000–2023) using language-model embeddings, applies ridge regression to forecast 12-month returns, and builds portfolios that are updated monthly. Stocks with the most favorable narrative signals outperform those with the weakest by roughly 0.9–1.2% per month, with Sharpe ratios > 0.6, even after trading costs. Most gains come from the long side, especially when short-term weakness coincides with optimistic forward-looking commentary.
FX Sentiment Analysis with Large Language Models
(Ballinari and Maly)
This study fine-tunes Meta’s Llama 3.1 on FX news to trade G10 currencies. The model often beats benchmarks, but performance swings sharply by news source: DailyFX with Llama delivers a Sharpe of 0.42, FXStreet with VADER soars to 1.70, while some models generate negative performance. The results show that domain-specific LLM fine-tuning can yield tradable FX signals, but success depends heavily on both data source and model choice.
Large Language Model Disagreement
(Liu, Liu, and Wang)
The authors develop a new measure of large language model disagreement (LLMD), defined as the dispersion in how six LLMs interpret earnings call transcripts. LLMD is economically large, more pronounced in small, volatile, and poorly performing firms, and robustly predicts lower future returns. The evidence suggests that high LLM disagreement reflects information asymmetry and should be viewed by investors as a cautionary signal of weak expected performance.
Pairs Trading
Cointegration-based pairs trading: identifying and exploiting similar exchange-traded funds
(Chen and Alexiou)
This paper tests cointegration-based ETF pairs trading from 2000 to 2024. Across 30 pairs, overall profitability is limited, though select cases like SPY–IVV generate strong results (29% return, Sharpe 1.5). Many pairs underperform, and lowering z-score thresholds improves returns and Sharpe ratios but at the cost of deeper drawdowns and higher tail risk. The evidence shows ETF pairs trading works only in stable relationships, making careful pair selection and adaptive risk management essential.
Portfolio Construction
Naïve and Optimal Portfolios Reconciled: A Golden Criterion and Adaptive Shrinkage Combination Strategy
(Feng, Huang, Wang, and Zhang)
Equal-weighted portfolios often outperform optimized ones out-of-sample. This paper shows why: Under the “Golden Criterion” (a unit eigenvector in the covariance matrix), 1/N is mathematically optimal. Extending this with a blend of equal and optimal weights, the method on S&P 500 data delivers out-of-sample R-squared up to 40.5% and Sharpe ratios above 1.0, showing that simplicity can be optimal.
Blogs
The (hidden) trading value of central bank liquidity information
(Macrosynergy)
Tactical Allocation 2.0: Lower Drawdowns, Higher Sharpe
(QuantSeeker)
Neural Nets and Factor Models
(Eric Falkenstein)
GitHub
ChatGPT Micro-Cap Experiment
Podcasts
Cliff Asness Returns
(Facts vs Feelings)
Chris Carrano – Designing Practical Factor Models
(Flirting with Models)
The Misreading of Trend ft. Nick Baltas
(Top Traders Unplugged)
A Storm May Be Coming To Wall Street (Bob Elliott Breaks It Down For Investors)
(Meb Faber Show)
Social Media
Gold's role as a diversifier
(D.E. Shaw)
High-vol Trend Following
(Dunn Capital)
Last Week’s Most Popular Links
Sizing the Risk: Kelly, VIX, and Hybrid Approaches in Put-Writing on Index Options
(Wysocki)
A New Star Is Born: Does the VIX1D Render Common Volatility Forecasting Models for the US Equity Market Obsolete?
(Albers)
Asymmetry and Crude Oil Returns
(Liu, Zhang, and Bouri)
This Substack is reader-supported. To receive new posts and support my work, consider becoming a free or paid subscriber.
Subscribe
Disclaimer: This newsletter is for informational and educational purposes only and should not be construed as investment advice. The author does not endorse or recommend any specific securities or investments. While information is gathered from sources believed to be reliable, there is no guarantee of its accuracy, completeness, or correctness.
This content does not constitute personalized financial, legal, or investment advice and may not be suitable for your individual circumstances. Investing carries risks, and past performance does not guarantee future results. The author and affiliates may hold positions in securities discussed, and these holdings may change at any time without prior notification.
The author is not affiliated with, sponsored by, or endorsed by any of the companies, organizations, or entities mentioned in this newsletter. Any references to specific companies or entities are for informational purposes only.
The brief summaries and descriptions of research papers and articles provided in this newsletter should not be considered definitive or comprehensive representations of the original works. Readers are encouraged to refer to the original sources for complete and authoritative information.
This newsletter may contain links to external websites and resources. The inclusion of these links does not imply endorsement of the content, products, services, or views expressed on these third-party sites. The author is not responsible for the accuracy, legality, or content of external sites or for that of any subsequent links. Users access these links at their own risk.
The author assumes no liability for losses or damages arising from the use of this content. By accessing, reading, or using this newsletter, you acknowledge and agree to the terms outlined in this disclaimer.
8
1
Share

---

*由 Substack Strategy Tracker 自动抓取*
