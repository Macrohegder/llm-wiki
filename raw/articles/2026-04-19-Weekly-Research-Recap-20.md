# Weekly Research Recap

**原文链接**: https://www.quantseeker.com/p/weekly-research-recap-afc

**发布时间**: Jul 15, 2025

**抓取时间**: 2026-04-19 22:24:49

---

## 摘要

Weekly Research Recap
Latest research on investing and trading
QuantSeeker
Jul 15, 2025
6
1
1
Share
Hi there. It's time for this week’s research recap, highlighting top investing insights from the past week with direct links to the full sources.
Backtesting
In-Sample and Out-of-Sample Sharpe Ratios for Linear Predictive Models
(Jacquier, Muhle-Karbe, and Mulligan)
Combining many weak signals can raise a model’s in-sample Sharpe ratio, but this paper shows it often backfires out of sample due to overfitting. Even if the combined model looks better in backtests, it tends to perform worse in live trading than simpler models built on fewer, stronger signals. To reduce overfitting, the authors recommend keeping models simple and using the longest available backtest window.
Bonds
The Low Frequen...

---

## 全文

Weekly Research Recap
Latest research on investing and trading
QuantSeeker
Jul 15, 2025
6
1
1
Share
Hi there. It's time for this week’s research recap, highlighting top investing insights from the past week with direct links to the full sources.
Backtesting
In-Sample and Out-of-Sample Sharpe Ratios for Linear Predictive Models
(Jacquier, Muhle-Karbe, and Mulligan)
Combining many weak signals can raise a model’s in-sample Sharpe ratio, but this paper shows it often backfires out of sample due to overfitting. Even if the combined model looks better in backtests, it tends to perform worse in live trading than simpler models built on fewer, stronger signals. To reduce overfitting, the authors recommend keeping models simple and using the longest available backtest window.
Bonds
The Low Frequency Trading Arms Race: Machines Versus Delays
(Dickerson, Nozawa, and Robotti)
Several recent papers have documented anomalies in corporate bonds. However, this paper shows that once real-world frictions, such as execution delays and bid-ask spreads, are accounted for, most anomalies and predictive signals lose their profitability. Even the most sophisticated machine learning models fail to deliver positive returns after costs. Overall, the findings suggest that many active bond strategies are unlikely to live up to their backtested performance.
Crypto
Variance Decomposition and Cryptocurrency Return Prediction
(Lee and Wang)
This paper shows that cryptocurrencies with high past volatility, especially those with sudden positive price jumps, tend to underperform in the following weeks. The effect is most pronounced among smaller, less liquid coins with heavy retail trading. These findings align with the well-known lottery effect in stocks, where assets offering lottery-like payoffs attract optimistic retail investors and become overpriced, leading to lower future returns.
Arbitrage on Decentralized Exchanges
(He, Yang, and Zhou)
Crypto prices sometimes diverge between decentralized and centralized exchanges, creating potential arbitrage opportunities. This paper builds a theoretical model of how arbitrageurs decide whether to trade, factoring in expected profits and gas fees. Using ETH/USDT data from Uniswap and Binance, the authors show that arbitrage opportunities appear in about 3.4% of Ethereum blocks and typically last just 1.5 blocks. Yet in 42.7% of those cases, no arbitrageur acts. When trades do occur, 65.7% are profitable.
Currencies
Foreign Exchange Order Flow as a Risk Factor
(Burnside, Cerrato, and Zhang)
A number of papers have proposed risk factors to explain currency strategies like carry and momentum. This paper shows that trading activity, specifically, order flow from financial customers, helps explain the returns to common FX strategies. Using a proprietary dataset of FX order flow, the authors construct factors linked to carry and momentum trades and find that these factors successfully explain the alpha of standard carry and momentum portfolios.
Information Leakage and Opportunistic Trading Around the FX Fix
(Muhle-Karbe, Oomen, and Polo)
Many investors use benchmark FX rates like the 4 pm London Fix, but trading around these times can create predictable price moves. This paper shows that when dealers hedge large client orders, they may reveal information that opportunistic traders exploit by trading ahead of the fix. This raises costs for clients, but starting to hedge earlier can limit the damage.
Equities
Data-mined Anomalies and the Expected Market Return
(Li, Platanakis, Ye, and Zhou)
It is well known that many published anomalies fail to hold up out of sample. This paper shows that lesser-known, data-mined signals can forecast market returns more effectively than established ones. The authors generate 20,000 signals by combining accounting ratios and growth metrics, then select those with both strong statistical significance and signs of persistent mispricing. Timing the market portfolio with these signals leads to notably higher Sharpe ratios and improved performance compared to using standard predictors.
Thematic Investing: A Risk-based Perspective
(Candes, Hastie, Hogan, Kahn, Luo, and Spector)
Many investors chase hot themes and narratives like AI or clean energy, but it's unclear whether these represent distinct sources of risk. This paper uses Goldman Sachs’ theme baskets and shows that in 41% of cases, stocks share significant residual return correlations beyond standard factor models. These themes often exhibit short-term trends, suggesting that traditional portfolios may overlook important risks and miss opportunities tied to changing market narratives.
Factor Models
Unpriced Risks: Rethinking Cross-Sectional Asset Pricing
(Chernov, Dahlquist, and Lochstoer)
Many investment strategies use characteristics like value, momentum, or carry to build portfolios. But research shows these strategies often contain “unpriced risks” that don’t earn compensation, such as industry or geographic exposures. This paper surveys key findings showing that removing such risks can significantly improve Sharpe ratios. Hence, investors may benefit from adjusting traditional factor portfolios to strip out noise and better capture true sources of return.
Machine Learning and Large Language Models
Understanding The Virtue of Complexity
(Kelly and Malamud)
While conventional wisdom typically favors simplicity and parsimony in return forecasting, Kelly et al. (2024) challenged this view by demonstrating that large, overparameterized models can perform remarkably well out of sample, even when trained on small datasets. In response to subsequent critiques, this follow-up paper addresses those concerns and offers additional theoretical and empirical evidence in support of model complexity.
Gauging the Sentiment of Federal Open Market Committee Communications through the Eyes of the Financial Press
(Banerjee, Cordova, De Pooter, and Grishchenko)
Investors tend to closely watch Federal Reserve announcements, but market reactions can be hard to interpret. This paper studies how financial news sentiment shifts around FOMC meetings. Using natural language processing, the authors construct a sentiment index based on the tone of media coverage before and after each meeting. Surprises in this sentiment help explain asset price movements across markets, even controlling for the effects of policy rate surprises.
Multifaceted Variability in Llm-Driven Stock Recommendations
(Chon, Kim, and Kim)
A growing number of investors and firms are turning to AI tools like ChatGPT to build stock portfolios, but it's unclear how consistent these recommendations really are. This paper shows that suggested stock lists can vary widely, even when the same question is asked repeatedly, depending on how the prompt is phrased and what investment goals are specified. To improve reliability, the authors essentially recommend an ensemble approach: Repeat queries and focus on stocks that appear most often.
Options
Commodity Option Return Predictability
(Aka, Gagnon, and Power)
This paper studies the predictability of delta-hedged commodity option returns, using CME data on seven commodities. Among various linear and nonlinear models, Random Forest delivers the strongest performance. Implied volatility and other option-specific features are the most informative predictors, while macro and futures variables add less value. Agricultural options show the highest return predictability.
Blogs
Estimating emerging markets sovereign risk premia
(Macrosynergy)
The Lumber-Gold Strategy
(Allocate Smartly)
GitHub
finmarketpy
- Backtesting strategies with Python
Superalgos
- A collection of crypto algos
Podcasts
Why Trend Following Works in the Stock Market, with Cole Wilcox
(The Compound and Friends)
The Anatomy of a CTA Recovery ft. Katy Kaminski
(Top Traders Unplugged)
The Hidden Flows Behind Big Market Moves | How Options Impact the Stock Market
(Excess Returns)
Cliff Asness — Quant Origins, Value Crashes, and Market Inefficiencies
(Value Investing with Legends)
Social Media
The Highs and Lows of Allocating to Trend Following
(Alan Dunne)
On “index arb” and market impact
(Alexander Gerko)
The Performance of Listed Private Equity
(Verdad-Dan Rasmussen)
Decomposing the S&P 500 Return
(Antti Ilmanen, via Cliff Asness)
Last Week’s Most Popular Links
Revisiting factor momentum: A one-month lag perspective
(Rönkkö and Holmi)
PCA analysis of Futures returns for fun and profit
(Rob Carver)
Fundamental Growth
(Arnott, Brightman, Harvey, Nguyen, and Shakernia)
This Substack is reader-supported. To receive new posts and support my work, consider becoming a free or paid subscriber.
Subscribe
Disclaimer: This newsletter is for informational and educational purposes only and should not be construed as investment advice. The author does not endorse or recommend any specific securities or investments. While information is gathered from sources believed to be reliable, there is no guarantee of its accuracy, completeness, or correctness.
This content does not constitute personalized financial, legal, or investment advice and may not be suitable for your individual circumstances. Investing carries risks, and past performance does not guarantee future results. The author and affiliates may hold positions in securities discussed, and these holdings may change at any time without prior notification.
The author is not affiliated with, sponsored by, or endorsed by any of the companies, organizations, or entities mentioned in this newsletter. Any references to specific companies or entities are for informational purposes only.
The brief summaries and descriptions of research papers and articles provided in this newsletter should not be considered definitive or comprehensive representations of the original works. Readers are encouraged to refer to the original sources for complete and authoritative information.
This newsletter may contain links to external websites and resources. The inclusion of these links does not imply endorsement of the content, products, services, or views expressed on these third-party sites. The author is not responsible for the accuracy, legality, or content of external sites or for that of any subsequent links. Users access these links at their own risk.
The author assumes no liability for losses or damages arising from the use of this content. By accessing, reading, or using this newsletter, you acknowledge and agree to the terms outlined in this disclaimer.
6
1
1
Share

---

*由 Substack Strategy Tracker 自动抓取*
