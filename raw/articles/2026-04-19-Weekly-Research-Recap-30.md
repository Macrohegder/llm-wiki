# Weekly Research Recap

**原文链接**: https://www.quantseeker.com/p/weekly-research-recap-314

**发布时间**: Sep 23, 2025

**抓取时间**: 2026-04-19 22:26:06

---

## 摘要

Weekly Research Recap
Latest research on investing and trading
QuantSeeker
Sep 23, 2025
7
1
Share
Hi there! This week’s research recap highlights the most important investing insights from the past seven days, with direct links to the full studies.
Commodities
The Term Structure of European Carbon Futures and the Predictive Power of Speculators and Hedgers
(Lautner, Dudda, and Klein)
Shifts in the carbon futures term structure are driven by hedgers, not speculators. Using ESMA Commitment of Traders data, the authors show that a 1% increase in commercial long hedging demand predicts a 0.21% rise in the curve level one month ahead. Speculator activities, despite holding most positions, provide no forecasting power. Gas–coal spreads drive levels, while oil and equity returns impact slope and ...

---

## 全文

Weekly Research Recap
Latest research on investing and trading
QuantSeeker
Sep 23, 2025
7
1
Share
Hi there! This week’s research recap highlights the most important investing insights from the past seven days, with direct links to the full studies.
Commodities
The Term Structure of European Carbon Futures and the Predictive Power of Speculators and Hedgers
(Lautner, Dudda, and Klein)
Shifts in the carbon futures term structure are driven by hedgers, not speculators. Using ESMA Commitment of Traders data, the authors show that a 1% increase in commercial long hedging demand predicts a 0.21% rise in the curve level one month ahead. Speculator activities, despite holding most positions, provide no forecasting power. Gas–coal spreads drive levels, while oil and equity returns impact slope and curvature. Overall, results suggest the EU carbon curve reflects real hedging needs, not speculative flows.
Currencies
Good Carry Trades and Market Dynamics
(Iwanaga and Sakemoto)
This paper builds on prior research introducing “good carry”, carry portfolios that exclude typical funding and investment currencies like JPY and AUD. Across G10 currencies (1980–2024), these portfolios achieve Sharpe ratios up to 0.76 before costs (vs. 0.64 for standard carry) and 0.54 after costs (vs. 0.28). Returns arise primarily from investor overconfidence, not risk premia, and remain distinct from momentum, value, and standard carry factors.
Equities
Beliefs and Stock Market Fluctuations: New Evidence from the Past Seven Decades
(Thesmar and Verner)
Using Value Line (VL) analysts’ forecasts from 1956 to 2024, the paper shows they predict market returns, explaining 60% of P/E variation and closely tracking valuation ratios such as the inverse CAPE ratio. VL forecasts are contrarian, rising after downturns and falling after rallies, unlike retail investors’ procyclical expectations. Hence, it seems this rare survey series embeds genuine predictive power, showing that sophisticated beliefs, not naive extrapolation, drive meaningful return forecasts.
The stock market impact of volatility hedging: Evidence from end-of-day trading by VIX ETPs
(Bangsgaard and Kokholm)
End-of-day VIX ETP rebalancing drives predictable movements in SPX futures. At 16:00, VIX ETP demand explains 4.6% of in-sample and 4.0% of out-of-sample variation in 16:05–16:15 SPX returns, with the strongest effects on extreme-demand days. A trading strategy exploiting this flow achieves a Sharpe ratio of 0.91 after costs (one-tick cost assumption). Hence, mechanical hedging flows, not fundamentals, temporarily move SPX futures, offering short-lived and potentially tradable opportunities.
Stocks for Inflation Shocks
(Czasonis, Li, Qiu, Song, and Turkington)
This paper develops a stock-level “inflation robustness score” that predicts which firms withstand inflation shocks best. The score measures how similar a stock looks today to the profiles of past winners or losers in inflationary periods, using Mahalanobis distance across nine firm attributes. Applied to 65 historical inflation shocks, a long–short portfolio earns +9.1% annualized during shocks while underperforming by –8.2% otherwise. Hence, investors can hedge inflation risk by dynamically tilting toward stocks statistically similar to past inflation winners.
Rethinking Measures of Sentiment: A New Approach
(Kazemi)
Traditional sentiment measures such as the AAII Sentiment Index and the University of Michigan Consumer Sentiment Index fail to predict stock returns. By contrast, newer measures, LSEG’s MarketPsych, the adjusted Baker–Wurgler index, and CBWadj, show strong significance (t-stats > 5), forecasting long-horizon returns, volatility, and credit spreads. Modern sentiment indexes thus better capture mispricing, making them superior tools for forecasting equity markets and financial stress.
Machine Learning and Large Language Models
Machine learning in the Australian equity market
(Hu, Song, and Zhong)
This study applies machine learning to Australian equities using 920 macro, firm, and industry predictors. Tree-based models and neural networks outperform, achieving out-of-sample R² up to 23% versus less than 10% for linear benchmarks. Forecast-based portfolios generate monthly long–short returns of 1.9–2.1% and alphas of 1.3–2.8% before costs, while still remaining profitable after costs. Key predictors include size, volatility, turnover, and macro shocks. Overall, machine learning effectively captures mispricing in Australian stocks.
Predicting Extreme Returns with Fundamentals: A Machine Learning Approach
(Liu and Wang)
The authors use 45 accounting and market variables in a two-stage machine learning framework to forecast extreme stock outcomes: “Rockets” (+100% returns) and “Torpedoes” (–80%). XGBoost achieves the best performance, classifying extremes with about 65% accuracy. Out-of-sample, predicted rockets gain +45% abnormal returns over 750 days, while torpedoes collapse, creating long-short spreads exceeding 100%. Hence, fundamentals combined with machine learning can reliably identify future tail winners and losers.
Simplicity versus Complexity: The Role of Historical Average in Kelly, Malamud, and Zhou's (2024) RFF Model
(Guo, Huang, and Yu)
In their “Virtue of Complexity” paper, Kelly et al. (2024) argue that random Fourier features (RFF) deliver strong market-timing, with Sharpe ratios rising alongside model complexity. Recent critiques and this paper show the effect is mechanical: With an intercept, the model collapses to the historical average. It outperformed the market pre-1975 (Sharpe 0.55 vs. 0.46, significant α) but lost all power afterwards (Sharpe 0.33 vs. 0.56, α insignificant). Main takeaway
:
RFF’s edge is illusory, offering no real predictive power.
Enhancing OHLC Data with Timing Features: A Machine Learning Evaluation
(Tepelyan)
This paper analyzes 1-minute OHLC bars for Russell 3000 stocks in 2021, predicting the next bar’s VWAP return. Incorporating timing features, the timestamps of open, high, low, and close, consistently improve forecasts. A Transformer with full features, for instance, reaches roughly 72% directional accuracy. The results suggest that simple intra-bar timing information adds a valuable dimension and contains exploitable signals beyond traditional OHLC data.
Statistics
Statistical Consequences of Fat Tails: Real World Preasymptotics, Epistemology, and Applications
(Taleb)
This is the third edition of Nassim Taleb’s book, showing that most tools in economics and finance fail under fat-tailed distributions. Sample means, variance, correlation, and even higher-order moments become unstable, often dominated by a single extreme event. Main takeaway: Investors should abandon reliance on thin-tailed models (e.g., mean-variance optimization, VaR)  and instead design strategies robust to extreme events, where survival under rare shocks, not average outcomes, determines long-term success.
Volatility
Oil price uncertainty as a predictor of stock market volatility
(Triantafyllou, Vlastakis, and Kellard)
Oil price uncertainty, measured as squared forecast errors of oil return regressions, is a powerful predictor of U.S. stock volatility. It consistently outperforms oil prices, realized volatility, and the VIX, especially over 6–12 month horizons. Its influence strengthened after the 2004 commodity financialization and is most pronounced in financial stocks. For investors, the results suggest that oil price uncertainty offers a better forward-looking, long-term, measure of volatility than the VIX.
Blogs
Stress-Testing a Tactical Allocation Model: Robustness and Improvements
(QuantSeeker)
Leveraged ETFs in Low-Volatility Environments
(Quantpedia)
Medium
Scanning Optimal Credit Spreads
(Velasquez)
What the Fear & Greed Index Tells Us About Market Returns
(Boh)
Podcasts
Vladimir Novakovski – Lighter: The Orderbook for all of Ethereum
(Flirting with Models)
Bridgewater, Botany & Breaking the 2/20 mold with Unlimited ETFs' Bob Elliott
(RCM Alternatives)
Rob Arnott: Rethinking Risk, Fear, and the Future of Asset Pricing
(Enterprising Investor)
Social Media / Industry Research
Understanding Treasury Yields
(AQR)
Interview with Jean-Philippe Bouchaud
(Robin Wigglesworth, FT)
Concentrated Portfolios
(Dan Rasmussen, Verdad Advisers)
Last Week’s Most Popular Links
Volatility Decay and Arbitrage in Leveraged ETFs: Evidence from the US and Japan
(Lin, Lin, Wang, Yeh)
Macro trading factors: dimension reduction and statistical learning
(Macrosynergy)
Measuring Volatility Mean-Reversion
(Velasquez)
This Substack is reader-supported. To receive new posts and support my work, consider becoming a free or paid subscriber.
Subscribe
Disclaimer: This newsletter is for informational and educational purposes only and should not be construed as investment advice. The author does not endorse or recommend any specific securities or investments. While information is gathered from sources believed to be reliable, there is no guarantee of its accuracy, completeness, or correctness.
This content does not constitute personalized financial, legal, or investment advice and may not be suitable for your individual circumstances. Investing carries risks, and past performance does not guarantee future results. The author and affiliates may hold positions in securities discussed, and these holdings may change at any time without prior notification.
The author is not affiliated with, sponsored by, or endorsed by any of the companies, organizations, or entities mentioned in this newsletter. Any references to specific companies or entities are for informational purposes only.
The brief summaries and descriptions of research papers and articles provided in this newsletter should not be considered definitive or comprehensive representations of the original works. Readers are encouraged to refer to the original sources for complete and authoritative information.
This newsletter may contain links to external websites and resources. The inclusion of these links does not imply endorsement of the content, products, services, or views expressed on these third-party sites. The author is not responsible for the accuracy, legality, or content of external sites or for that of any subsequent links. Users access these links at their own risk.
The author assumes no liability for losses or damages arising from the use of this content. By accessing, reading, or using this newsletter, you acknowledge and agree to the terms outlined in this disclaimer.
7
1
Share

---

*由 Substack Strategy Tracker 自动抓取*
