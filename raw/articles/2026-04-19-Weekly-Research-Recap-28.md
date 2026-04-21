# Weekly Research Recap

**原文链接**: https://www.quantseeker.com/p/weekly-research-recap-101

**发布时间**: Sep 09, 2025

**抓取时间**: 2026-04-19 22:25:49

---

## 摘要

Weekly Research Recap
Latest research on investing and trading
QuantSeeker
Sep 09, 2025
8
1
Share
Hi there! Here’s this week’s research recap, featuring key investing insights from the past week along with direct links to the full sources.
Currencies
The trade imbalance network and currency returns
(Hou, Sarno, and Ye)
While past work links a country’s trade balance to predictability of FX returns, this study shows that its position in the global network of deficits and surpluses matters too. The authors create a centrality-based measure (CBC), finding that going long highly central currencies and shorting peripheral ones delivers a Sharpe ratio of 0.65. Hence, currency risk premia seem to reflect network risk, unexplained by existing factors such as carry and momentum.
Equities
Forest thr...

---

## 全文

Weekly Research Recap
Latest research on investing and trading
QuantSeeker
Sep 09, 2025
8
1
Share
Hi there! Here’s this week’s research recap, featuring key investing insights from the past week along with direct links to the full sources.
Currencies
The trade imbalance network and currency returns
(Hou, Sarno, and Ye)
While past work links a country’s trade balance to predictability of FX returns, this study shows that its position in the global network of deficits and surpluses matters too. The authors create a centrality-based measure (CBC), finding that going long highly central currencies and shorting peripheral ones delivers a Sharpe ratio of 0.65. Hence, currency risk premia seem to reflect network risk, unexplained by existing factors such as carry and momentum.
Equities
Forest through the Trees: Building Cross-Sections of Stock Returns
(Bryzgalova, Pelger, and Zhu)
The authors introduce "Asset Pricing (AP) Trees", a method for building characteristic-sorted portfolios that capture nonlinear interactions. Compared to conventional univariate and double sorting, AP Trees deliver out-of-sample Sharpe ratios up to three times larger and alphas 20–30% higher. Importantly, these returns are not explained by standard factor models and yield a more reliable measure of expected returns.
Revaluation Alpha
(Arnott, Ehsani, Harvey, and Shakernia)
This paper decomposes factor returns into structural alpha (fundamentals-driven) and revaluation alpha (valuations-driven). Sorting factors monthly on historical structural alpha yields a 4.5% spread (t=4.0, Sharpe 0.57) versus 2.8% for sorting on past raw returns. Portfolios weighted by structural alphas earn about 1.3% excess return over equal-weighted portfolios, and with double the information ratio, providing predictive power for up to 24 months. Hence, stripping out valuation effects from returns delivers stronger, more durable factors and a superior long-horizon factor timing tool.
An Auto-Residual Factor Model
(Alkshaik)
The paper introduces a factor model that augments market and size with residual short-term reversal, residual momentum, and residual long-term reversal, with residuals extracted by regressing stock returns on the first five PCA components. Out-of-sample, residual factors consistently dominate their standard versions. For example, in the case of momentum, Sharpe ratios double in the US pre-sample, triple in APAC ex-Japan, and rise fivefold in Japan.
A New Puzzle Piece for the "Sell in May, and Go Away" Anomaly: Regulatory Disclosures
(Schroeder)
The “Sell in May” effect is a well-known anomaly, but what drives it? This paper points to seasonality in regulatory disclosure. Analyzing 10+ million SEC filings (2004–2023), it shows that summer corporate filings drop about 17%, creating an information drought that weakens returns. September, typically the worst month for equities, also records the fewest filings. Similar European patterns reinforce the point: Winter’s information flood fuels stronger performance, while summer’s information drought weakens markets.
Short Selling Index ETFs and Market Performance
(Chichernea, Petkevich, and Wang)
Several papers show that increased short selling at the stock level predicts
lower
future returns, as short-sellers are often viewed as informed traders identifying overvaluation. By contrast, this paper finds that short selling in broad market ETFs predicts
higher
future index returns, measured using short positions in standard ETFs and long positions in inverse ETFs. The predictability is strongest in bear markets, and a monthly rebalanced strategy based on ETF short exposure outperforms the market. Key lesson: Monitoring ETF short activity can potentially provide investors with a valuable market-timing signal.
A Tale of Two Anomalies: Value, Momentum, and Risk Sentiment
(Lundblad, Velikov, Yuan, and Zhdanov)
This paper constructs a risk-on/risk-off index and shows that long-short value and momentum react in opposite ways to shifts in sentiment. During risk-off episodes, value strategies lose about 0.22% per day, while momentum gains +0.35%. Retail investors withdraw from value, and short sellers add pressure, worsening losses. Momentum avoids such selling and remains resilient. Main takeaway: Value is penalized when risk aversion rises, but momentum acts as a hedge.
Machine Learning and Large Language Models
Modern Machine Learning Tools in Finance: A Critical Perspective
(Allen, Kacperczyk, and Karri)
Previous research shows that published anomalies lose about 58% of their returns after discovery, and machine learning is no exception. ML strategies often show high Sharpe ratios in sample and pre-costs, yet often underperform the market and simpler models once frictions are considered. Worse, drawdowns during regime shifts can be 2–3x deeper than backtests suggest. In short, the paper argues that machine learning speeds up discovery, but markets adapt just as quickly, making alpha difficult to sustain.
Beyond the Ellipse: The Virtue of Nonlinearity in Asset Pricing
(Huang)
Many papers have found that nonlinear models outperform linear models in predicting stock returns, but in what context do they really shine? This study shows they deliver the biggest edge for firms with skewed and lottery-like returns, growth-style uncertainty in fundamentals, and during volatile markets. In these environments, Random Forests nearly double the Sharpe of linear models (0.96 vs. 0.47).
Options
Why does options market information predict stock returns?
(Muravyev, Pearson, and Pollet)
Previous research finds that sorting stocks based on their implied volatility spread (call IV – put IV) or skew (OTM put IV – ATM call IV) produces significant alpha. This paper shows that the effect is entirely due to stock borrow fees. Before costs, long–short returns are about +0.64% per month, but after stock borrow fees, they vanish. The abnormal performance comes almost solely from the short leg, while the long side has no alpha. Thus, these signals are best used as filters to avoid or underweight costly short-leg stocks, not as standalone trading strategies.
Private Equity
The Private Equity Illusion: Revisiting Risks, Returns, and Realities
(Nocera)
The author argues that private equity’s reputation as a high-return, low-risk diversifier is largely a myth. Adjusted for leverage, valuation smoothing, and fees, average PE returns converge with public equities, while true volatility and crisis correlations approach small-cap stocks. In 2024, the State Street PE Index returned just 7.1% versus 25.0% for the S&P 500. Fees erode 400–600 bps annually, and diversification benefits vanish under stress. Overall, the paper suggests PE is leveraged beta, not true alpha, and investors should favor transparent, low-cost vehicles like ETFs.
Blogs
PCA analysis of Futures returns for fun and profit, part deux
(Rob Carver)
Bitcoin ETFs in Conventional Multi-Asset Portfolios
(Quantpedia)
Replicating an Asset Allocation Model
(QuantSeeker)
Surprisingly Profitable Pre-Holiday Drift Signal for Bitcoin
(Quantpedia)
Podcasts
What makes an Alternative Investment Truly Valuable? ft. Moritz Seibert
(Top Traders Unplugged)
Richard Thaler and Alex Imas
(Michael Covel)
Asset Allocation in Practice
(Rational Reminder)
Social Media
The Awkward Problem with Managed Futures ETFs
(Andrew Beer / Hedgenordic)
When Alt Market Trends Break
(Quantica Capital)
Last Week’s Most Popular Links
Cointegration-based pairs trading: identifying and exploiting similar exchange-traded funds
(Chen and Alexiou)
Global News Networks and Return Predictability
(Freire, Moin, Quaini, and Soebhag)
High-vol Trend Following
(Dunn Capital)
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
