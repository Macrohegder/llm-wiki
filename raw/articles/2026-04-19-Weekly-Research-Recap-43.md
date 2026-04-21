# Weekly Research Recap

**原文链接**: https://www.quantseeker.com/p/weekly-research-recap-22e

**发布时间**: Dec 23, 2025

**抓取时间**: 2026-04-19 22:27:41

---

## 摘要

Weekly Research Recap
Latest research on investing and trading
QuantSeeker
Dec 23, 2025
12
Share
This week’s recap highlights the most actionable investing insights from academic research, industry reports, blogs, and social media, with direct links to every source.
Currencies
Cross-Border M&A Flows, Economic Growth, and Foreign Exchange Rates
(Riddiough and Zhang)
Unusually strong cross-border M&A inflows indicate improving macroeconomic fundamentals. Countries with high inflows tend to experience stronger future economic growth and a stronger currency. Currency portfolios built on the signal earn positive alphas and a Sharpe ratio of around 0.7 (before costs).
Key takeaway: Firms’ investment decisions contain forward-looking information that predicts both growth and FX returns, while add...

---

## 全文

Weekly Research Recap
Latest research on investing and trading
QuantSeeker
Dec 23, 2025
12
Share
This week’s recap highlights the most actionable investing insights from academic research, industry reports, blogs, and social media, with direct links to every source.
Currencies
Cross-Border M&A Flows, Economic Growth, and Foreign Exchange Rates
(Riddiough and Zhang)
Unusually strong cross-border M&A inflows indicate improving macroeconomic fundamentals. Countries with high inflows tend to experience stronger future economic growth and a stronger currency. Currency portfolios built on the signal earn positive alphas and a Sharpe ratio of around 0.7 (before costs).
Key takeaway: Firms’ investment decisions contain forward-looking information that predicts both growth and FX returns, while adding diversification.
Equities
Decile-Based Quantitative Portfolio Strategies from SEC Fundamentals: A 17-Year Backtest of Value and Momentum Factors
(Pellegrino)
Using raw SEC 10-K filings, the author builds value and price-momentum portfolios with annual rebalancing. Over 2009–2025, high-P/E growth stocks earn about 8% per year (Sharpe about 0.44), while low-P/E value stocks deliver about 2% (Sharpe about 0.05); momentum is weak and shows no robust alpha after factor controls.
Key takeaway: Annually rebalanced value and momentum strategies fail to produce any alpha.
Keeping it Simple: How Can Post-Earnings Return Drift Exist and Not Exist Simultaneously?
(Subrahmanyam)
This paper reconciles conflicting PEAD evidence by showing that post-earnings drift is economically irrelevant for nearly all stocks. Reconstructing standard PEAD factors from 2001 to 2024, the author finds weak returns (0.2–0.3% per month) and insignificant t-stats (roughly 1.4) once microcaps are excluded. The apparent strong results in recent studies may stem from microcaps or the use of non-standard methods.
Key takeaway: PEAD is not a robust, tradeable anomaly for scalable equity portfolios.
Factor Investing
Correcting the Factor Mirage: A Research Protocol for Causal Factor Investing
(Lopez de Prado and Zoonekynd)
The paper argues that factor investing’s weak performance stems from model misspecification, not necessarily fading risk premia. Standard regressions often condition on variables jointly driven by signals and returns, inflating R² and t-statistics while biasing estimates. A broad US multifactor index earned only 0.6% annual excess return with a Sharpe of 0.17 from 2007 to 2024.
Key takeaway: Without explicit causal modeling, statistically “strong” factors can systematically destroy capital.
What Threshold Should be Applied to Tests of Factor Models?
(Harvey, Sancetta, and Zhao)
Many factors appear significant only because researchers test too many signals and ignore the correlation between them. Correcting for these issues shows that the standard t-stat ≥ 2 rule greatly overstates evidence. Even clean, value-weighted factors typically need t-statistics around 3.0–3.5 to be credible.
Key takeaway: Many reported factors are not statistically reliable, and new factors should clear at least a t-stat of 3.
Machine Learning and Large Language Models
Nonlinear Time Series Momentum
(Moskowitz, Sabbatucci, Tamoni, and Uhl)
Time-series momentum is fundamentally nonlinear: Extreme trend signals should be dampened, not scaled linearly. Theory-based or ML-estimated S-shaped signals materially improve performance. With daily data and a 12-month lookback, nonlinear momentum delivers Sharpe ratios of 0.83–0.84 versus 0.70 for linear momentum, with gains concentrated in equity drawdowns.
Key takeaway: Robust trend following comes from controlling or dampening extreme signals.
LLMs for Quantitative Investment Research: A Practitioner’s Guide
(Mihov, Firoozye, and Treleaven)
This paper reviews how LLMs are used in quantitative investment research. While they don’t reliably predict returns, LLMs improve productivity by accelerating research, extracting richer signals from text, and supporting coding. Poor use introduces risks such as hallucinations and data leakage.
Key takeaway: LLMs are valuable research tools, not standalone forecasting models.
Machine Learning for Earnings Forecasting -US and International Evidence
(Chattopadhyay, Fang, and Mohanram)
The authors test whether machine learning improves earnings forecasts. A tree-based model (XGBoost) performs best, cutting one-year forecast errors by about 5% in the U.S. and 6% internationally. The gains are largest for firms that are hardest to forecast, such as small and volatile firms.
Key takeaway: Machine learning adds clear economic value by making earnings forecasts more accurate.
The Mechanical Virtue of Random Fourier Features and Model Complexity
(Cartea and Shi)
Kelly et al. (2024) argue that highly overparameterized models outperform simple models. This paper shows the pattern can be mechanical: Even with a single training observation (T = 1), random Fourier feature models deliver higher out-of-sample R² and Sharpe ratios as complexity increases. Interestingly, flipping return signs fully reverses these gains, degrading performance as complexity grows.
Key takeaway: Large models can appear successful without learning; complexity alone is not evidence of predictive power.
Machine Learning Meets Markowitz
(Wang, Gao, Harvey, Liu, and Tao)
This paper replaces the standard work flow of “predict-then-optimize” with an end-to-end ML approach that trains return forecasts to maximize portfolio utility given risk, constraints, and trading costs. In China A-shares, it lifts feasible long-only returns by about 12 percentage points per year at similar volatility.
Key takeaway: Optimize for portfolio outcome, not prediction accuracy.
Options
Options Traders, Short-Term Reversals, and Return Predictability
(Han, Huang, and Xiao)
Short-term stock reversals are most predictable when past-week price moves (adjusted for industry and earnings effects) are combined with open buy call–put ratios. Heavy call buying on recent losers signals rebounds, while heavy put buying signals continued declines. When both signals agree, subsequent stock returns earn about 10 to 15 bps per day (t-stat > 4).
Key takeaway: Call–put imbalances signal which reversals informed traders expect to materialize.
Prediction Markets
Financial Prediction Markets: A New Measure of Earnings Expectations
(Gomez Cram, Guo, Jensen, and Kung)
Prediction markets give a cleaner read of earnings expectations than analysts. The recently launched earnings contracts on Polymarket predict earnings beats with 68% accuracy a week ahead and 77% the day before, versus 62% for analysts.
Key takeaway: Markets that force investors to put money behind beliefs yield cleaner, more informative earnings expectations than analyst forecasts.
Blogs
The 6 Biggest Myths About Diversification and Non-Correlation
(IASG, Greg Taunt)
When Execution Delays Erode Short-Term Alpha
(Concretum Group)
Momentum Investing: A Stronger, More Resilient Framework for Long-Term Allocators
(CFA Institute)
Combining Bitcoin Trend Signals Across Timeframes
(Quantseeker)
Podcasts
The Alpha No Human Can Find | David Wright on Machine Learning’s Hidden Edge
(Excess Returns)
Doug Colkitt - When Crypto Markets Break: Liquidations, Leverage, and Markets Under Stress
(Chat with Traders)
Systematic Macro in a Shifting Economy: Signals Over Stories
(ReSolve Asset Management)
Social Media & Industry Research
The Speed Factor - How trend model speed has driven performance dispersion and equity downside protection since 2023
(Quantica Capital)
Market Timing: More than a mirage
(Man Group)
International Value has Outshone US Growth
(MSCI)
Round Table Discussion: Trend-following in a year without a map
(HedgeNordic)
Golden Fears
(Man Group)
Last Week’s Most Popular Links
Intraday Time Series Reversal
(Iwanaga and Sakemoto)
Alpha through equity-versus-FX trading
(Macrosynergy)
Dual Peer Effects and Cross-Stock Predictability
(Avramov, Ge, Li, and Linton)
This Substack is reader-supported. To receive new posts and support my work, consider becoming a free or paid subscriber.
Subscribe
Disclaimer: This newsletter is for informational and educational purposes only and should not be construed as investment advice. The author does not endorse or recommend any specific securities or investments. While information is gathered from sources believed to be reliable, there is no guarantee of its accuracy, completeness, or correctness.
This content does not constitute personalized financial, legal, or investment advice and may not be suitable for your individual circumstances. Investing carries risks, and past performance does not guarantee future results. The author and affiliates may hold positions in securities discussed, and these holdings may change at any time without prior notification.
The author is not affiliated with, sponsored by, or endorsed by any of the companies, organizations, or entities mentioned in this newsletter. Any references to specific companies or entities are for informational purposes only.
The brief summaries and descriptions of research papers and articles provided in this newsletter should not be considered definitive or comprehensive representations of the original works. Readers are encouraged to refer to the original sources for complete and authoritative information.
This newsletter may contain links to external websites and resources. The inclusion of these links does not imply endorsement of the content, products, services, or views expressed on these third-party sites. The author is not responsible for the accuracy, legality, or content of external sites or for that of any subsequent links. Users access these links at their own risk.
The author assumes no liability for losses or damages arising from the use of this content. By accessing, reading, or using this newsletter, you acknowledge and agree to the terms outlined in this disclaimer.
12
Share

---

*由 Substack Strategy Tracker 自动抓取*
