# Weekly Research Recap

**原文链接**: https://www.quantseeker.com/p/weekly-research-recap-12f

**发布时间**: Mar 10, 2026

**抓取时间**: 2026-04-19 22:28:54

---

## 摘要

Weekly Research Recap
Latest research on investing and trading
QuantSeeker
Mar 10, 2026
11
4
Share
Welcome to this week’s Tuesday roundup, where I highlight the most actionable investing ideas from the past week. The selection spans academic papers, industry research, blog posts, and insightful social-media discussions, with links provided throughout.
Equities
Monetary Policy Surprises and the Cross Sectional Stock Return Predictability in -Volume Sorted Portfolios
(Wang)
Previous research shows that stocks experiencing abnormal trading volume tend to outperform. This paper finds that Fed forward-guidance surprises (changes in expected future policy rates) predict the high-volume return premium. Hawkish guidance significantly reduces future high-minus-low volume spreads.
Key takeaway: Expe...

---

## 全文

Weekly Research Recap
Latest research on investing and trading
QuantSeeker
Mar 10, 2026
11
4
Share
Welcome to this week’s Tuesday roundup, where I highlight the most actionable investing ideas from the past week. The selection spans academic papers, industry research, blog posts, and insightful social-media discussions, with links provided throughout.
Equities
Monetary Policy Surprises and the Cross Sectional Stock Return Predictability in -Volume Sorted Portfolios
(Wang)
Previous research shows that stocks experiencing abnormal trading volume tend to outperform. This paper finds that Fed forward-guidance surprises (changes in expected future policy rates) predict the high-volume return premium. Hawkish guidance significantly reduces future high-minus-low volume spreads.
Key takeaway: Expectations about future interest-rate paths affect cross-sectional stock returns, volume-based long–short signals work best when markets anticipate looser policy.
The Granular Origin of Tail Dispersion Risk
(Andersen, Ding, and Todorov)
Using high-frequency data on S&P 500 stocks, the paper shows that the source of tail risk matters for the price of risk. Stocks exposed to systematic tail shocks earn
lower
returns, while exposure to firm-specific tail shocks is associated with
higher
returns. Combining both signals yields a zero-cost portfolio with improved Sharpe ratios.
Key takeaway: The source of tail risk matters; both systematic and idiosyncratic tail shocks command risk premia, but with opposite signs.
Quantitative Strategies For Momentum And Trend Reversal: Integrating Macroeconomic Factors, Advanced Signal Processing, And Regime Awareness
(Charlotte Sim)
The paper reviews momentum and reversal strategies and illustrates them with simple backtests. Using U.S. data from 2014 to 2024, price momentum earns about 9.2% annually with a Sharpe of 0.74, while a macro-based signal delivers 7.8% with a Sharpe of 0.56. Combining the two reduces volatility and yields a Sharpe of 0.70.
Key takeaway: Macro signals can potentially diversify traditional price momentum strategies.
Systematic Reversal and Industry Momentum
(Gao, Li, Yuan, and Zhou)
Previous research shows that industry portfolios exhibit short-term momentum. Using U.S. equity data, this paper shows that momentum profits are partly suppressed by exposure to a short-term reversal factor. Industry momentum has a Sharpe of about 0.56, but dynamically hedging reversal exposure raises the Sharpe to 1.11 and increases alpha.
Key takeaway: Removing reversal exposure strengthens industry momentum strategies.
Machine Learning and Large Language Models
Generative AI for Finance: A New Framework
(Chai, Jiang, Meng, You, and Zhou)
The paper applies a transformer model (RPBERT) that treats stocks as sequences ordered by characteristics, allowing it to learn cross-firm relationships. In U.S. equities, it achieves 17.9% out-of-sample R² and a long–short portfolio earns 2.5% per month with Sharpe ratios of 2.9–3.5 (before costs), outperforming standard ML and factor models.
Key takeaway: Modeling cross-firm interactions with transformers can improve return prediction and risk-adjusted performance.
Algorithms for Asset Allocators: Review
(Taysom, Firoozye, and Treleaven)
The paper surveys how machine learning and AI can assist large asset allocators. Rather than producing new alpha models, it maps practical use cases: Portfolio optimization, regime detection, manager selection, and AI-driven document analysis. The biggest barriers are sparse data, long investment cycles, and governance constraints.
Key takeaway: For large allocators, AI’s immediate value lies in improving research and operational workflows rather than replacing human asset allocation decisions.
Market Microstructure
The Price Impact of Nothing: Rejected Orders as Predictors of Future Returns
(Albers, Cucuringu, Howison, and Shestopaloff)
Using granular data from the Hyperliquid BTC–USD perpetual market, the paper shows that rejected “post-only” orders, orders that never enter the order book, predict short-term price movements. Rejected orders correctly forecast the direction of the next price change about 72% of the time. These orders are not random errors but likely reflect traders attempting to position ahead of expected price moves.
Key takeaway: Even non-executed order attempts can reveal traders’ information and predict short-term price movements.
Portfolio Construction
From Black Box to Explainable Portfolio Optimization: Tracing Allocations to Views and Constraints
(Landais, Perchet, Soupe, Carvalho)
The paper opens the “black box” of portfolio construction by decomposing the final multi-asset allocation into intuitive components: A portfolio replicating the long-term benchmark, tilts from tactical views, expected manager alpha net of fees, and adjustments caused by portfolio constraints. The approach works under both classical and robust optimization.
Key takeaway: Every portfolio weight can be traced back to the initial investment views, alpha assumptions, and constraints.
Dynamic Tracking Error and the Total Portfolio Approach
(Alankar, Maymin, Maymin, Scholes, Zhang)
Using U.S. equity and bond data, the paper shows that institutional portfolio frameworks such as Strategic Asset Allocation and the Total Portfolio Approach mainly differ in how tightly tracking error is constrained. Across constraints from 0.5% to 5%, Sharpe ratios are statistically indistinguishable, while the volatility of tracking error differs by roughly 12×.
Key takeaway: The key governance choice is not the portfolio framework itself, but how much tracking-error flexibility investors allow.
Prediction Markets
A Microstructure Perspective on Prediction Markets
(Palumbo)
Using trade-level data from Kalshi’s NFL prediction markets, the paper shows that liquidity providers systematically accumulate directional exposure rather than offsetting inventory as traditional market makers do. Over the season, they earned about $29 million in aggregate, though profits were highly volatile week to week.
Key takeaway: Liquidity provision in prediction markets appears very different from traditional markets.
Regime Models
Multivariate Time Series Classification With Online Expert Advice: An Application to Market Regimes
(Guibert and Cuervo-Paloma)
Using global equity data and 567 macro and financial features, the paper develops a supervised system to detect upcoming equity stress regimes by combining logistic regression, random forest, XGBoost, and a neural network in an ensemble. The approach significantly improves prediction accuracy, while inflation-related indicators emerge as the most important predictors.
Key takeaway: Cross-asset macro signals, especially inflation surprises, help anticipate future equity stress regimes.
Retirement Planning
The 4-Percent Rule Was Never Failproof: On the Folly of Fixed Rate Withdrawals
(McQuarrie)
Using U.S. mutual fund data, the paper shows that the classic 4% retirement withdrawal rule is problematic. For retirees starting in the 1960s, portfolios often ran out of money prematurely. Small changes, such as 33 bps lower returns, slightly higher volatility, or unfavorable return sequencing, can flip success into failure.
Key takeaway: Fixed withdrawal rules are fragile; retirement spending should adapt to market conditions.
Blogs
NLP and Yield Curve Prediction From Central Bank Minutes
(CFA Institute)
Trading Equity Volatility with a Bond Market Signal
(QuantSeeker)
2-Year Notes Momentum: Extracting Term Structure Anomalies from FOMC Cycles
(Quantpedia)
Reinforcement Learning for Portfolio Optimization: From Theory to Implementation
(Jonathan Kinlay)
Macro trading signals with regression-based machine learning
(Macrosynergy)
Podcasts
When Narratives Change Faster Than Markets ft. Alan Dunne
(Top Traders Unplugged)
James Choi: Portfolio Theory in a Spreadsheet
(Rational Reminder)
Social Media & Industry Research
Capacity Discipline
(Thomas Babbedge, GreshamQuant)
Managing Investment Risk During Geopolitical Shocks
(Man Group)
The Best Defensive Strategies: Two Centuries of Evidence
(Alpha Architect)
How To Reason About A Messy Future
(SystematicLongShort)
Last Week’s Most Popular Links
Price-Path Convexity and Short-Horizon Return Predictability
(Gulen and Woeppel)
More Bets, Better Bets
(Quantitativo)
Idiosyncratic volatility
(Feldman, Kang, and Zhao)
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
4
Share

---

*由 Substack Strategy Tracker 自动抓取*
