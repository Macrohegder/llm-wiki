# Weekly Research Recap

**原文链接**: https://www.quantseeker.com/p/weekly-research-recap-0d3

**发布时间**: Apr 29, 2025

**抓取时间**: 2026-04-19 22:23:17

---

## 摘要

Weekly Research Recap
Latest research on investing and trading
QuantSeeker
Apr 29, 2025
9
2
1
Share
Time for another batch of top-tier investing research. Below is a carefully curated list of great papers from last week, each linked to the original source for easy access.
If you’re enjoying these posts, a like or subscribe is always appreciated, thank you for your support!
Asset Allocation
Global Tactical Asset Allocation: Updated Results and Real-Market Implementation Using Python and IBKR
(Zarattini)
Many investment strategies suffer from “rebalance timing luck”, where results vary depending on which day trades are made each month. By updating Meb Faber's classic tactical asset allocation strategy through 2025, the authors show that spreading trades across four staggered weeks and automa...

---

## 全文

Weekly Research Recap
Latest research on investing and trading
QuantSeeker
Apr 29, 2025
9
2
1
Share
Time for another batch of top-tier investing research. Below is a carefully curated list of great papers from last week, each linked to the original source for easy access.
If you’re enjoying these posts, a like or subscribe is always appreciated, thank you for your support!
Asset Allocation
Global Tactical Asset Allocation: Updated Results and Real-Market Implementation Using Python and IBKR
(Zarattini)
Many investment strategies suffer from “rebalance timing luck”, where results vary depending on which day trades are made each month. By updating Meb Faber's classic tactical asset allocation strategy through 2025, the authors show that spreading trades across four staggered weeks and automating execution reduces timing risk, cuts costs, and delivers more stable returns.
Commodities
Do Energy Futures add Value to Stock Portfolios?
(Forgetta, Gauthier, and Godin)
Commodities are often seen as useful diversifiers. This paper tests the impact of adding electricity, natural gas, and crude oil futures on top of a fully invested S&P 500 portfolio. The strategy significantly boosts risk-adjusted returns, especially during crises like COVID-19 and the Russia-Ukraine war, suggesting that selective energy futures exposure can improve overall portfolio performance.
Crypto
Rating Stablecoins
(Koike, Okimoto, and Sakai)
The number of stablecoins has increased in recent years and varies in how reliably they maintain their value. To help assess their quality, the authors develop a rating system that scores each stablecoin on price consistency, trading volume, market size, and stability over time. Interestingly, coins with the biggest market caps aren’t always the most stable. Hence, investors should look beyond size and consider multiple factors when allocating to stablecoins.
Currencies
Dollar Upheaval: This Time is Different
(Jiang, Krishnamurthy, Lustig, Richmond, and Xu)
Global investors usually flock to U.S. Treasurys for safety during turmoil. After new tariffs and policy changes, however, the dollar fell sharply even as U.S. interest rates climbed. The paper discusses how investors now seem less willing to pay extra for the security of dollar assets. This shift may signal rising doubts about the dollar’s special status and calls for a reassessment of its role in global portfolios.
Equities
Salience, Asymmetric Effect and Stock Returns
(Wang, Yao, and Liu)
Previous research has studied whether the salience of a stock, how much its return stands out from its peers, predicts future returns. This paper applies a quantile regression framework and finds strong predictability at the extremes: High-salience stocks that strongly underperform tend to rebound, while high-salience stocks that strongly outperform tend to decline. The mean-reversion effect is especially pronounced among small, illiquid, or volatile stocks.
Measure Mispricing with Price
(Peng and Xu)
Mispricing is difficult to measure as estimating a stock’s true value is tricky. By comparing a simple model-based fair value to the actual price and tracking short-term changes, the authors create a "price wedge shock" that flags potential mispricing. Sorting stocks by this signal each month, they find that buying the most undervalued and selling the most overvalued earns a return of 0.5 to 1.2 percent per month, potentially offering a useful trading signal.
Do Share Repurchases Increase the Value of Non-repurchasing Firms?
(Kim)
Companies often return cash to investors through buybacks, but where that money goes afterward is less obvious. This paper finds that much of it is reinvested into similar non-buyback firms, lifting their prices. Interestingly, large repurchases by growth firms have funneled money into other growth stocks, reducing demand for value stocks and helping to explain the fading value premium.
Lecture Notes
Quantitative Methods in Finance
(Vansteenberghe)
These lecture notes for Master’s students cover topics like forecasting and risk modeling, with hands-on coding exercises in Python and R.
Machine Learning and Large Language Models
From Econometrics to Machine Learning: Transforming Empirical Asset Pricing
(Shi)
Traditional asset pricing models typically rely on a few factors and often assume linear relationships, which may limit their ability to explain returns. This survey paper explores how recent advances in machine learning help empirical asset pricing move forward by capturing nonlinear patterns and using high-dimensional and alternative data.
Thematic Scoring: Quantifying Contextual Narratives using Language Models
(Lopez-Lira, Choi, Kim, Kwon, Kim, and Yun)
Analysts may struggle to gauge how companies position themselves around emerging investment themes. This paper uses large language models to extract and score theme-specific sentiment from earnings calls, showing that firms speaking positively about a theme tend to outperform those speaking negatively over the next 60 days. Hence, theme-level sentiment signals could offer distinct information compared to broad firm-level sentiment when constructing portfolios.
Predictability and Complexity Dynamics in High-Frequency Financial Machine Learning
(Buchta)
Boosted trees and neural networks predict high-frequency stock returns much better than simpler linear models. The most useful signals come from recent buy-sell imbalances and effective spreads. Frequent retraining is crucial, as even a one-day gap between training and prediction is shown to sharply reduce accuracy.
Macro
Text-based Macro Data and Asset Prices
(Klaus and Thimme)
Macroeconomic data, like GDP or consumption, is often only available at low frequencies such as annually or quarterly. This paper shows how to reconstruct monthly versions of such data by analyzing patterns in 100 years of daily New York Times articles. By linking word frequencies in news to economic indicators using machine learning, the paper shows how investors can build richer datasets that better capture economic fluctuations throughout the year.
Options
Asset Pricing Results in Option Markets: True, Spurious, or Overlooked?
(Eberbach, Molnar, Schuster, and Uhrig-Homburg)
This paper shows that option anomalies based on intraday delta hedging may be overstated. Bid-ask noise distorts both stock returns and hedge ratios, creating a bias that inflates delta-hedged returns, especially for illiquid stocks. Many findings may simply reflect microstructure noise rather than true anomalies.
Intraday Jumps and 0DTE Options: Pricing and Hedging Implications
(Božović)
The author estimates a stochastic volatility model with jump risk and finds that 0DTE options embed a sizable premium for intraday jumps, larger than for regular price moves or volatility. The paper suggests that 0DTEs can be a useful tool to hedge against or profit from sharp intraday swings.
Blogs
The Bitter Lesson
(Quantitativo)
Front-Running Seasonality in Country ETFs: An Extended Test
(Allocate Smartly)
Boosting macro trading signals
(Macrosynergy)
Short-Term Correlated Stress Reversal Trading
(Quantpedia)
Weekly Research Insights
(QuantSeeker)
FinTwit and LinkedIn
Understanding Expected Returns
(Cliff Asness - Antti Ilmanen)
Bear Market Guidebook
(Meb Faber via UBS)
On Gold’s Recent Price Surge
(Campbell Harvey)
Understanding Equity Drawdowns
(Man Group)
Market Timing
(Man Group)
GitHub
Fincept Terminal
finmarketpy
-
Backtesting with Python
fastquant
-
Python backtesting framework
Medium
Top 9 Python Quantitative Finance GitHub Repos
(Algo Insights)
Generating Trend Lines Algorithmically
(Velasquez)
The Market Isn’t Always Random — Spot It with Return Direction Tests
(Velasquez)
Podcasts
Kevin Davey II - Selecting Optimal Strategies for Peak Performance
(The Algorithmic Advantage)
Power in Fixed-Sized, Non-Compounding FX Plays
(Chat With Traders)
The Irrecoverable Error: Risk, Ruin, and the Rules of Wealth | Practical Lessons from Guy Spier
(Excess Returns)
From Chaos to Clarity: The Power of Systematic Investing ft. Nick Baltas
(Top Traders Unplugged)
Last Week’s Most Popular Links
Disaggregating VIX
(Degiannakis and Kafousaki)
Trading VIX on Volatility Forecasts: Another Volatility Puzzle?
(Degiannakis, Delis, Filis, and Giannopoulos)
Global FOMO: The Pulse of Financial Markets Worldwide
(Bonaparte)
This Substack is reader-supported. To receive new posts and support my work, consider becoming a free or paid subscriber.
Subscribe
Disclaimer: This newsletter is for informational and educational purposes only and should not be construed as investment advice. The author does not endorse or recommend any specific securities or investments. While information is gathered from sources believed to be reliable, there is no guarantee of its accuracy, completeness, or correctness.
This content does not constitute personalized financial, legal, or investment advice and may not be suitable for your individual circumstances. Investing carries risks, and past performance does not guarantee future results. The author and affiliates may hold positions in securities discussed, and these holdings may change at any time without prior notification.
The author is not affiliated with, sponsored by, or endorsed by any of the companies, organizations, or entities mentioned in this newsletter. Any references to specific companies or entities are for informational purposes only.
The brief summaries and descriptions of research papers and articles provided in this newsletter should not be considered definitive or comprehensive representations of the original works. Readers are encouraged to refer to the original sources for complete and authoritative information.
This newsletter may contain links to external websites and resources. The inclusion of these links does not imply endorsement of the content, products, services, or views expressed on these third-party sites. The author is not responsible for the accuracy, legality, or content of external sites or for that of any subsequent links. Users access these links at their own risk.
The author assumes no liability for losses or damages arising from the use of this content. By accessing, reading, or using this newsletter, you acknowledge and agree to the terms outlined in this disclaimer.
9
2
1
Share

---

*由 Substack Strategy Tracker 自动抓取*
