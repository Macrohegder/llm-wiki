# Weekly Research Recap

**原文链接**: https://www.quantseeker.com/p/weekly-research-recap-6d1

**发布时间**: Dec 30, 2025

**抓取时间**: 2026-04-19 22:27:45

---

## 摘要

Weekly Research Recap
Latest research on investing and trading
QuantSeeker
Dec 30, 2025
7
2
1
Share
As 2025 comes to an end, this week’s research recap is the 52nd, and final, edition of the year. As usual, it highlights the most actionable investing insights from academic research, industry reports, blogs, and social media over the past seven days, with direct links to every source.
Crypto
Bollinger Bands under Varying Market Regimes: A Comparative Study of Breakout and Mean-Reversion Strategies in BTC/USDT
(Arda)
Using 1-minute BTC/USDT data from 2017 to 2022 and long-only trades, the paper shows that Bollinger Bands are highly regime-dependent. While breakout rules tend to outperform mean reversion trades in most regimes, in strong bull trends, dip-buying can sometimes outperform. Durin...

---

## 全文

Weekly Research Recap
Latest research on investing and trading
QuantSeeker
Dec 30, 2025
7
2
1
Share
As 2025 comes to an end, this week’s research recap is the 52nd, and final, edition of the year. As usual, it highlights the most actionable investing insights from academic research, industry reports, blogs, and social media over the past seven days, with direct links to every source.
Crypto
Bollinger Bands under Varying Market Regimes: A Comparative Study of Breakout and Mean-Reversion Strategies in BTC/USDT
(Arda)
Using 1-minute BTC/USDT data from 2017 to 2022 and long-only trades, the paper shows that Bollinger Bands are highly regime-dependent. While breakout rules tend to outperform mean reversion trades in most regimes, in strong bull trends, dip-buying can sometimes outperform. During choppy phases, both approaches see performance deteriorate.
Key takeaway: In Bitcoin, trade breakouts by default, buy dips only when the broader trend is decisively bullish.
The Institutional Crypto Bet: Are Early Adopters Buying at the Wrong Time?
(Krause)
Institutional buying of Bitcoin ETFs may be mistimed from a portfolio perspective. From 2024 to 2025, the author finds that IBIT’s equity correlation increased from 0.10 to 0.49, thereby weakening diversification. Despite 39% annual returns, risk-adjusted performance lagged (Sharpe of 0.82 vs 1.86 for gold), and drawdowns were deep (−33%).
Key takeaway: Bitcoin is increasingly behaving like equity risk, calling into question its role as a diversifier.
Equities
Informed Trading and Expected Returns
(Choi, Jin, and Yan)
Using detailed ownership data from the Shanghai Stock Exchange, the paper shows that stocks with high institutional ownership volatility, measured as the average absolute weekly change in institutional ownership over the past 50 weeks, earn higher expected returns. The return spread between the top and bottom quintiles is about 10.8% annually, concentrated in mid- and large-cap stocks.
Key takeaway: Aggressive institutional trading is a proxy for information asymmetry among investors and is a strong cross-sectional return predictor.
Investor Sentiment and the Crash Risk of Anomalies
(Chue and Hu)
Across 14 equity anomalies (1965–2016), crash risk varies sharply with investor sentiment. Following low sentiment, strategies display negative skewness and severe downside tails. After high sentiment, returns are higher, and skewness turns positive, with lower crash risk. Diversifying across anomalies raises Sharpe ratios but fails to eliminate tail risk.
Key takeaway: Diversification across long–short anomalies improves risk-adjusted returns but not downside protection.
Hedge Funds and Mutual Funds
Anomalies as New Hedge Fund Factors
(Chen, Li, Tang, and Zhou)
Using adaptive LASSO on 44 candidate factors and 7,300+ hedge funds, the paper estimates a 9-factor model that outperforms standard benchmarks across hedge fund styles. Alphas shrink toward zero and lose statistical significance, while adjusted R² rises to about 85% (vs 55–70%). The factors span market, term spreads, changes in interest rates and credit spreads, ROA, asset growth, time-series momentum, low-risk, and betting-against-beta.
Key takeaway: Most hedge fund “alpha” reflects systematic factor exposure.
Country Rotation and International Mutual Fund Performance
(Jiao, Karolyi, and Ng)
Active international equity funds generate value by rotating across countries, rather than through individual stock selection. High-rotation funds earn roughly 2% annual alpha vs 0.7% for low-rotation peers. The advantage comes from cutting exposure ahead of country downturns, rather than capturing market upswings.
Key takeaway: Skilled global managers’ alpha comes mainly from country market timing rather than security selection.
Machine Learning and Large Language Models
The Nonstationarity-Complexity Tradeoff in Return Prediction
(Capponi, Huang, Sidaoui, Wang, and Zou)
The paper shows that in non-stationary markets, return predictability depends on jointly adapting model complexity and training window length. Simple linear models are often favored during regime shifts, while complex nonlinear models add value mainly in stable periods with longer histories. A joint, adaptive selection of both improves out-of-sample R² and raises cumulative returns by 31%, with the largest gains in recessions.
Key takeaway: Let market regimes determine both how complex the model is and how much data it uses.
Timing the Factor Zoo via Deep Visualization
(Jia, Li, Zhang, and Zhao)
Studying 206 equity factors, the authors transform each factor’s own return history into images and apply CNNs to detect regime shifts and patterns that simple rules miss. A long–short factor-timing portfolio earns about 14% per year with a Sharpe of 1.22. Performance survives realistic costs. Timing gains are strongest for momentum and value-style factors, whose payoffs are highly state-dependent.
Key takeaway: Factors with regime-sensitive payoffs are the easiest and most profitable to time.
Can Machines Learn from Trading Data?
(Kong, Wei, and Zhang)
Using SEC Form 4 data, the paper trains a decision-tree model that uncovers nonlinear insider-trading signals missed by standard methods. A long–short portfolio earns an annual Sharpe of about one (before costs), driven primarily by insider
purchases
. Important features are trade size as a % of shares outstanding, dollar value of trades, and recent insider trading performance.
Key takeaway: Large, economically meaningful insider buys contain exploitable alpha that ML can uncover.
Drive Smarter Quant Strategies Through the Implementation of Deep Learning (Presentation Slides)
(Rodriguez Dominguez)
The author argues that portfolio performance does not require accurate return forecasts. As long as signals point in the right direction and assets are ranked correctly, efficient frontiers remain well-behaved. Simulations deliver Sharpe ratios around 0.8–1.2 across wide model misspecification.
Key takeaway: Focus on signal direction, ranking, and robustness, not precise forecasts, to build resilient portfolios.
Market Microstructure
The Lasting Impact of Flickering Quotes
(Brogaard, Cartea, Chang, and Graumans)
Roughly 40% of limit orders are cancelled within one second, yet these “flickering” quotes are far from irrelevant. Using full Euronext Amsterdam order-book data, the paper shows that “flickering” quotes have non-zero, persistent price impact and help predict short-term price movements by inducing follow-on orders and cancellations.
Key takeaway: Fleeting quotes trigger others to reveal information in the order book.
Trend Following
On the Anatomy of Trend
(Kjaer)
This paper develops a closed-form theory of trend following, decomposing performance into directional exposure and timing. It shows trend following delivers convex, option-like payoffs and becomes profitable in deep or prolonged drawdowns, even under mean reversion. Fast signals hedge small, short-lived corrections but whipsaw; slow signals react later yet dominate major crashes.
Key takeaway: Trend following provides crisis convexity that strengthens as market drawdowns deepen.
Volatility
Return Extrapolation and Volatility Expectations
(Chordia, Lin, and Xiang)
Prior research shows investors extrapolate past returns into future return expectations. This paper shows the same bias in volatility beliefs. Recent losses lead investors to overestimate future volatility, raising implied volatility, variance risk premia, and crash-hedging demand. The effect is asymmetric and dominated by the most recent days (roughly 60% weight).
Key takeaway: Loss-driven volatility extrapolation inflates option prices and hedging costs in predictable ways.
Blogs
Daily + 15:45 OHLCV: A Database for Reliable Backtesting
(Concretum Group)
Public finance pressure as a systematic trading factor
(Macrosynergy)
What Successful Investors Read: Book Recommendations from Professionals
(CFA Institute)
Understanding Gold – Hedge, Diversifier, or Overpriced Insurance?
(Quantpedia)
Podcasts
The Truth No One Sees | 41 Great Investors Share Their Most Controversial Belief
(Excess Returns)
The Hidden Flaw in ‘Passive Investing’ — And What Wealthy Families Do Instead
(Meb Faber)
Dispersion Is the Story This Year (Group Conversation Part 1)
(Top Traders Unplugged)
Annanay Kapila – Perpetual Futures Everywhere and All the Time
(Flirting with Models)
Social Media & Industry Research
The Prison Of Financial Mediocrity
(SystematicLongShort)
The Value of Fundamental Indexing
(Clifford Asness)
Taming the Anomaly Zoo: How Macroeconomic Forces Shape Market Returns
(Alpha Architect)
Cooking up Sharpe: A Recipe for Portfolio Construction
(Man Group)
Regimes, Systematic Models and the Power of Prediction
(Man Group)
Last Week’s Most Popular Links
Nonlinear Time Series Momentum
(Moskowitz, Sabbatucci, Tamoni, and Uhl)
LLMs for Quantitative Investment Research: A Practitioner’s Guide
(Mihov, Firoozye, and Treleaven)
Options Traders, Short-Term Reversals, and Return Predictability
(Han, Huang, and Xiao)
This Substack is reader-supported. To receive new posts and support my work, consider becoming a free or paid subscriber.
Subscribe
Disclaimer: This newsletter is for informational and educational purposes only and should not be construed as investment advice. The author does not endorse or recommend any specific securities or investments. While information is gathered from sources believed to be reliable, there is no guarantee of its accuracy, completeness, or correctness.
This content does not constitute personalized financial, legal, or investment advice and may not be suitable for your individual circumstances. Investing carries risks, and past performance does not guarantee future results. The author and affiliates may hold positions in securities discussed, and these holdings may change at any time without prior notification.
The author is not affiliated with, sponsored by, or endorsed by any of the companies, organizations, or entities mentioned in this newsletter. Any references to specific companies or entities are for informational purposes only.
The brief summaries and descriptions of research papers and articles provided in this newsletter should not be considered definitive or comprehensive representations of the original works. Readers are encouraged to refer to the original sources for complete and authoritative information.
This newsletter may contain links to external websites and resources. The inclusion of these links does not imply endorsement of the content, products, services, or views expressed on these third-party sites. The author is not responsible for the accuracy, legality, or content of external sites or for that of any subsequent links. Users access these links at their own risk.
The author assumes no liability for losses or damages arising from the use of this content. By accessing, reading, or using this newsletter, you acknowledge and agree to the terms outlined in this disclaimer.
7
2
1
Share

---

*由 Substack Strategy Tracker 自动抓取*
