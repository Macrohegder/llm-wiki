# Weekly Research Recap

**原文链接**: https://www.quantseeker.com/p/weekly-research-recap-c22

**发布时间**: Jul 29, 2025

**抓取时间**: 2026-04-19 22:25:03

---

## 摘要

Weekly Research Recap
Latest research on investing and trading
QuantSeeker
Jul 29, 2025
7
1
Share
Hi there. Welcome to this week’s research recap, featuring key investing insights from the past week, along with direct links to the full articles.
Equities
The “Actual Retail Price” of Equity Trades
(Schwarz, Barber, Huang, Jorion, and Odean)
Contrary to conventional wisdom, payment for order flow (PFOF) isn’t systematically linked to worse execution. This paper finds large cost differences across brokers for identical orders, not explained by PFOF or commissions. Market makers like Citadel treat each broker’s flow differently, possibly due to perceived toxicity. TD Ameritrade comes out best, with an average round-trip costs of just 7.2 bps.
How To Bet On Winners (and Losers)
(Brownlees and S...

---

## 全文

Weekly Research Recap
Latest research on investing and trading
QuantSeeker
Jul 29, 2025
7
1
Share
Hi there. Welcome to this week’s research recap, featuring key investing insights from the past week, along with direct links to the full articles.
Equities
The “Actual Retail Price” of Equity Trades
(Schwarz, Barber, Huang, Jorion, and Odean)
Contrary to conventional wisdom, payment for order flow (PFOF) isn’t systematically linked to worse execution. This paper finds large cost differences across brokers for identical orders, not explained by PFOF or commissions. Market makers like Citadel treat each broker’s flow differently, possibly due to perceived toxicity. TD Ameritrade comes out best, with an average round-trip costs of just 7.2 bps.
How To Bet On Winners (and Losers)
(Brownlees and Souza)
Previous research suggests that classifying stocks into winners and losers can lead to better risk-adjusted returns than predicting exact returns. This paper confirms that finding by using firm characteristics to estimate the probability of a stock being in the top or bottom return decile. Return classification, especially with XGBoost, is shown to outperform return prediction even after transaction costs. Hence, investors may benefit from using return classification over traditional return forecasts.
Do Investors Fully Understand the Seasonality in Accruals?
(Choy, Lobo, and Tan)
Many firms follow seasonal patterns in their financial statements, but investors seem to overlook these when evaluating quarterly numbers. This paper shows that investors underreact to predictable seasonal shifts in accruals. Firms with historically low accruals for a given quarter tend to outperform those with high accruals when the data is released. Sorting stocks monthly based on this pattern has delivered strong returns, particularly since 2001.
Systematic Investor Sentiment and Market-Anomaly Comovement
(Guo and Wu)
Market anomalies are often thought to be independent of the overall market, but this paper finds that equity long–short anomaly portfolios tend to have negative exposure to the market. This pattern is driven by investor sentiment, especially optimism, which causes speculative and high-beta stocks, often found in the short leg of anomaly portfolios, to rise with the market. The strength of this comovement predicts next-month market returns and may serve as a useful market timing signal.
Informed Trade of Earnings Announcements
(Xie)
Many investors believe that early access to earnings reports offers a major trading advantage, but this paper tells a different story. It examines a real case in which traders gained illegal access to thousands of earnings announcements by hacking newswire services. These traders selectively acted on reports with large surprises and strong sentiment, yet their performance was only slightly better than that of simple strategies based on public data. Hence, despite having perfect foresight, their returns were surprisingly modest due to frictions like price impact, risk aversion, and the difficulty of processing large volumes of earnings information each day.
Price Vs. Market-Cap-Weighted Portfolio Diversification: Does it Matter?
(Damjanovic, Drenovak, Urosevic, and Jelic)
There’s growing concern that a few firms dominate market-cap-weighted indexes like the S&P 500. This paper introduces a new diversification measure and shows that price-weighted indexes like the DJIA make more effective use of their constituents. As a result, alternative weighting methods, such as price weighting, equal weighting, or smart beta, may offer better diversification and lower risk, particularly during market shocks.
Fixed Income
Salience Theory and Cross-Sectional Corporate Bond Returns
(Chen, Wang, Wei, Wu, and Zhang)
Salience theory suggests that investors chase assets with extreme past returns, pushing prices away from fundamentals and leading to mean reversion. In stocks, this typically means chasing recent winners, which then underperform. This paper finds a similar effect in corporate bonds, but with a twist: The strongest returns come from bonds with salient downside, those that have recently lagged their peers, implying investors overreact to bad news. A long–short portfolio based on salience earns strong alpha, with most of the gains coming from the long side.
Inflation, Default, and Corporate Bond Returns
(Lu, Nozawa, and Song)
Investors may wonder how inflation affects corporate bond returns. While rising inflation generally hurts bonds, its impact varies across components. The duration portion suffers as interest rates rise, but the credit component can either benefit or decline depending on the inflation regime. In procyclical periods like the post-2000 era, inflation signals stronger growth and lower defaults, boosting credit returns. In contrast, during countercyclical periods like the 1970s, it often coincides with weak growth, hurting credit. Hence, understanding the inflation regime is key to managing credit exposure.
Machine Learning and Large Language Models
Adversarial Attacks on Machine Learning-Driven High-Frequency Trading Models
(Shimao, Saengchote, Chakraborty, Wang, and Khern-am-nuai)
This paper shows that machine learning models used in high-frequency trading are highly vulnerable to subtle manipulations. Even tiny, strategic changes to order book data can trick models into making poor predictions, leading to bad trades or missed opportunities. Ironically, the models that perform best under normal conditions are most sensitive to data manipulation.
Non-Linear Factor Investing in the Era of Machine Learning
(Chin)
Many studies argue that stock market anomalies lose their edge out of sample, especially after excluding microcaps and accounting for trading costs. This paper challenges that view. Starting with 146 standard anomalies, the author uses genetic programming to create more complex, non-linear combinations of existing signals. The result is hundreds of trading strategies that remain robust, even in recent years. These strategies are transparent, low turnover, and largely based on accounting data. The key takeaway: Thoughtfully constructed non-linear combinations of known signals can lead to more reliable and tradable stock selection models.
Predicting the Daily Return Direction of the Stock Market Using Machine Learning and Deep Learning Algorithms
(Zhang)
Many investors try to predict whether the market will go up or down the next day. This study tests different models on the EEM emerging markets ETF and finds that simple methods like logistic regression don’t work well. In contrast, machine learning models like support vector machines and random forests offer better accuracy and higher trading profits.
Your AI, Not Your View: The Bias of LLMs in Investment Analysis
(Lee, Seo, Park, Lee, Ahn, Choi, Lopez-Lira, and Lee)
As more investors use Large Language Models like ChatGPT for trading recommendations, this paper highlights that these tools can carry built-in biases. For example, the paper finds that LLMs often favor large-cap stocks and contrarian strategies, even when faced with balanced or opposing evidence. These internal preferences can override strong counterarguments, suggesting that investors should be cautious when relying on models that may distort their intended views.
Options
Option Pricing Before Black, Scholes and Merton: A Review and Assessment of the Historical Evidence
(Dotsis)
Before the Black-Scholes model, many believed option pricing lacked structure. This paper shows that 19th-century traders already used sophisticated tools like payoff diagrams, algebra, and intuitive strategies that mirror modern practices. Their prices closely matched what today’s models predict. For investors, this highlights how financial innovation often starts with market practice long before it’s formalized in academic theory.
Horizon-specific information in option implied correlation
(Oberoi, Sun, and Voukelatos)
While the implied correlation among S&P 500 stocks has been shown to predict market returns, this paper shows that splitting the signal into short- and long-term components leads to improved forecasts. The short-term component helps predict returns over days to weeks, while the long-term trend works better over several months. Hence, aligning the signal’s frequency with the investment horizon may enhance market timing.
Portfolio Management
The Power of Position Sizing in Portfolio Management
(Blotnick)
Many investors focus on picking the right stocks but overlook the importance of sizing correctly. This paper shows that poor position sizing, often driven by overconfidence or emotional bias, can hurt performance even when the stock picks are solid. It recommends using risk- or volatility-based sizing methods to manage downside risks and improve long-term returns.
Portfolio Construction: Blending Fundamental and Technical Analysis
(Blotnick)
While many investors stick to either charts or financials, this paper argues for a more integrated approach and shows how the two can work together. It demonstrates how price trends and other price signals can guide better timing, while company fundamentals provide the foundation for long-term conviction. By combining these perspectives, investors can improve decision-making, avoid costly missteps, and maintain a steady flow of trade ideas.
Blogs
Machine learning for international trading strategies
(Macrosynergy)
Weekly Research Insights - Improving Equity Momentum Strategies
(QuantSeeker)
The Equity Overnight Anomaly ETFs
(Eric Falkenstein)
GitHub
Trading Agents
- Multi-agent LLM framework
ML for Trading
- Code for Machine Learning for Algorithmic Trading, 2nd edition.
Podcasts
Kent Daniel — From Physics to Finance: Exploring Market Inefficiencies
(Value Investing with Legends)
Jason Hirschman: The +$100,000,000 Microcap Investor
(Value Bridge)
Outliers, Recovery, and the Spirit of Classic Trend
(Turtle Talk - Aussie Turtles)
Social Media
Enhancing Traditional Portfolios with a Gold Futures Stack
(Corey Hoffstein - Return Stacked)
The Case for Expected Shortfall in Tail Risk Management
(Man Group)
The elusive “illiquidity premium”
(Toby Nangle - FT)
Last Week’s Most Popular Links
AI Challenges in Mathematical Investing
(Lopez de Prado)
A Safe Haven Index
(Baur, Dimpfl, and Pena)
A Trend Factor for the Cross Section of Cryptocurrency Returns
(Fieberg, Liedtke, Poddig, Walker, and Zaremba)
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
