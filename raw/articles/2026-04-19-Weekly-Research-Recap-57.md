# Weekly Research Recap

**原文链接**: https://www.quantseeker.com/p/weekly-research-recap-ee0

**发布时间**: Mar 31, 2026

**抓取时间**: 2026-04-19 22:29:12

---

## 摘要

Weekly Research Recap
Latest research on investing and trading
QuantSeeker
Mar 31, 2026
12
1
2
Share
This week’s Tuesday roundup brings together the most actionable investing ideas from recent academic work, industry research, blogs, and high-quality discussions across social media, with links throughout.
Commodities
Momentum and Reversal on the Short-Term Horizon: Evidence from Commodity Markets
(Ding, Kang, Yu, and Zhao)
Using CFTC position data, the paper shows that short-horizon returns are driven by two offsetting mechanisms: Speculators’ net trading predicts reversals, while the return component orthogonal to trading flows exhibits continuation. The latter generates about 12 bps per week (about 6.2% annualized) and, when used as a sorting signal, improves intermediate-term momentum r...

---

## 全文

Weekly Research Recap
Latest research on investing and trading
QuantSeeker
Mar 31, 2026
12
1
2
Share
This week’s Tuesday roundup brings together the most actionable investing ideas from recent academic work, industry research, blogs, and high-quality discussions across social media, with links throughout.
Commodities
Momentum and Reversal on the Short-Term Horizon: Evidence from Commodity Markets
(Ding, Kang, Yu, and Zhao)
Using CFTC position data, the paper shows that short-horizon returns are driven by two offsetting mechanisms: Speculators’ net trading predicts reversals, while the return component orthogonal to trading flows exhibits continuation. The latter generates about 12 bps per week (about 6.2% annualized) and, when used as a sorting signal, improves intermediate-term momentum returns from 5.2% to 9.9% annually.
Key takeaway: Decomposing returns into trading-flow and orthogonal components improves momentum signals.
Equities
Prediction reconditioned: Revisiting relevance
(Polakow, Flint, Turro, and van Rooyen)
Relevance-Based Prediction (RBP) focuses on observations similar to current market conditions, but this selectivity often backfires. In predicting S&P 500 returns, the paper finds that OLS achieves higher explanatory power and lower forecast error. Simulations show why: Conditioning on “relevant” data reduces bias but increases variance due to smaller samples
. Key takeaway: In noisy financial markets, using more data can outperform using “better” data.
Measuring Equity Factor Uncertainty
(Huovinen)
The paper introduces a Factor Uncertainty Index (FUI) based on a broad set of equity factors. FUI predicts future factor returns, with explanatory power rising to 30% at a 12-month horizon and out-of-sample R² around 10 to 13%. Using FUI for risk scaling improves performance, lifting Sharpe from 1.25 to 1.53.
Key takeaway: Factor uncertainty predicts returns and provides a simple, effective signal for dynamic risk scaling.
FX
One Leg at a Time: The Hidden Structure of Carry Trade Profitability
(Panayotov)
Carry trades look noisy because exchange-rate swings drown out the underlying signal. By stripping out this noise, the paper shows that carry profits arrive in distinct regimes and come from only one side of the trade at a time. Timing which leg to hold using policy-rate dynamics roughly doubles Sharpe from 0.45 to 0.87.
Key takeaway: Carry is a regime-dependent strategy and performance improves when you trade it selectively.
Machine Learning and Large Language Models
Bimodality Everywhere: International Evidence of Deep Momentum
(Han and Qin)
Momentum returns are inherently unstable: Past winners and losers both face a meaningful risk of sharp reversals. A machine learning “Deep Momentum” approach that models the full return distribution (via predicted probabilities) delivers 41% annual returns with a Sharpe of about 2.5, versus 21% and 1.0 for standard momentum, with consistent global outperformance.
Key takeaway: Modeling return distributions, not just averages, improves momentum investing.
Reviving Anomalies
(Beckmeyer, Berg, Wiedemann, and Wortmann)
Most anomalies fail after costs, but the paper shows they become profitable when conditioned on ML-based expected returns and transaction costs. By filtering each anomaly to retain only high-conviction stocks, the number of implementable anomalies rises from 10 to 100. A simple 1/N portfolio delivers 12 to 16% annual returns with Sharpe ratios up to 1.0.
Key takeaway: Alpha comes from selectively implementing existing factors, keeping only trades with strong expected returns after costs.
Options
The Changing Information Content of Options Markets: Evidence from 1996–2024
(Taheri Hosseinkhani)
Option markets still contain valuable information, but not all signals survive structural change. The implied volatility gap between calls and puts delivers 25 to 30 bps/week alpha with strong significance, while volume-based signals weaken and even reverse after 2020 as retail trading distorts flows, remaining informative mainly in hard-to-short stocks.
Key takeaway: In option markets, price-based signals are more robust, while volume-based signals become unreliable when the composition of traders shifts.
Portfolio Allocation
Geopolitical Risk and Asset Pricing Across Market Regimes
(Abou Rjaily)
Geopolitical risk is priced unevenly across assets and regimes. In a two-state framework, equities exhibit significant negative exposure, while bonds and currencies respond more to regional and bilateral shocks than to domestic risk. Safe-haven assets such as JPY and CHF benefit during stress, and responses vary widely across asset classes and market conditions.
Key takeaway: Geopolitical risk is not a single factor; its impact depends on regime, geography, and asset class.
Sports Betting
The ‘Sleeping Giant’: A Behavioral Anomaly in Prediction Markets
(Vaze)
Playoff betting markets systematically overestimate the win probability of recent “dynasty” teams when they are underdogs, by about 10 percentage points. This creates a profitable strategy, with 16% gross returns (63% win rate), while comparable non-dynasty underdogs show no bias.
Key takeaway: Even liquid markets can misprice assets when investors overweight recent success.
Trend Following
Rethinking Trend Following: Optimal Regime-Dependent Allocation
(Zakamulin)
Trend-following performance depends critically on how exposure is allocated across regimes. While most research focuses on refining signals, the paper shows that optimizing regime-dependent position sizing alone delivers large gains. A Sharpe-optimal rule lifts Sharpe from 0.41–0.57 to 0.56–0.73 in U.S. equities, from 0.05 to 0.30 internationally, and from 0.21 to 0.51 in diversified portfolios.
Key takeaway: Optimizing momentum exposures across regimes is a powerful and underexplored source of improvement.
Blogs
What Drives the Commodity Skewness Premium?
(Quantseeker)
Breaking the Rules of Intraday Trading
(Concretum Group)
Brave New Backtest
(Robot Wealth)
War and Interest Rates
(John H. Cochrane)
Why Alternatives Still Command High Fees
(CFA Institute)
Podcasts
How Billionaire Hedge Fund Managers Are Using Generative AI to Invest
(Odds on Open)
David Bush - Build a High-Performance Quant Crypto Portfolio Without Blowing Yourself Up!
(The Algorithmic Advantage)
Sports Betting and Prediction Markets—Through a Trading Lens · Stefan Stadie
(Chat with Traders)
Social Media & Industry Research
If You Can’t Beat It, Stack It: How Portable Alpha Overlays May Enhance Equity Returns
(Quantica Capital)
I Did Not Predict What is Going on in Privates
(Cliff Asness)
Unlocking Hidden Patterns: How Daily Returns Predict Future Stock Performance
(Alpha Architect)
Last Week’s Most Popular Links
Understanding the Convolutional Neural Network’s Stock Return Predictability
(Guan, Li, and Si)
Empirical Asset Pricing via Learning-to-Rank
(Lin, Su, and Zhu)
Expected Returns with Trends and Cycles
(Hillenbrand and McCarthy)
This Substack is reader-supported. To receive new posts and support my work, consider becoming a free or paid subscriber.
Subscribe
Disclaimer: This newsletter is for informational and educational purposes only and should not be construed as investment advice. The author does not endorse or recommend any specific securities or investments. While information is gathered from sources believed to be reliable, there is no guarantee of its accuracy, completeness, or correctness.
This content does not constitute personalized financial, legal, or investment advice and may not be suitable for your individual circumstances. Investing carries risks, and past performance does not guarantee future results. The author and affiliates may hold positions in securities discussed, and these holdings may change at any time without prior notification.
The author is not affiliated with, sponsored by, or endorsed by any of the companies, organizations, or entities mentioned in this newsletter. Any references to specific companies or entities are for informational purposes only.
The brief summaries and descriptions of research papers and articles provided in this newsletter should not be considered definitive or comprehensive representations of the original works. Readers are encouraged to refer to the original sources for complete and authoritative information.
This newsletter may contain links to external websites and resources. The inclusion of these links does not imply endorsement of the content, products, services, or views expressed on these third-party sites. The author is not responsible for the accuracy, legality, or content of external sites or for that of any subsequent links. Users access these links at their own risk.
The author assumes no liability for losses or damages arising from the use of this content. By accessing, reading, or using this newsletter, you acknowledge and agree to the terms outlined in this disclaimer.
Paid subscriptions may not be available in all jurisdictions and may change without notice.
12
1
2
Share

---

*由 Substack Strategy Tracker 自动抓取*
