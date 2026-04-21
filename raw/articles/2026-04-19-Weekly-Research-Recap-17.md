# Weekly Research Recap

**原文链接**: https://www.quantseeker.com/p/weekly-research-recap-15a

**发布时间**: Jun 24, 2025

**抓取时间**: 2026-04-19 22:24:28

---

## 摘要

Weekly Research Recap
Latest research on investing and trading
QuantSeeker
Jun 24, 2025
7
2
Share
Hi there. Here’s this week’s handpicked selection of the latest top research and resources on investing, with direct links to the original sources for easy access.
Bonds
Genetic Mimicking Portfolios for ETF Arbitrage
(Crego, Kvaerner, Sommervoll, Sommervoll, and Stevens)
Many ETFs trade at a premium or discount to their net asset value (NAV). This paper targets corporate bond ETFs trading at a premium by shorting them and hedging the position with a portfolio of other liquid ETFs that replicate the NAV. Even after accounting for trading costs, the strategy delivers strong performance. Overall, the paper presents a practical approach for replicating ETFs that hold illiquid assets.
Crypto
Statis...

---

## 全文

Weekly Research Recap
Latest research on investing and trading
QuantSeeker
Jun 24, 2025
7
2
Share
Hi there. Here’s this week’s handpicked selection of the latest top research and resources on investing, with direct links to the original sources for easy access.
Bonds
Genetic Mimicking Portfolios for ETF Arbitrage
(Crego, Kvaerner, Sommervoll, Sommervoll, and Stevens)
Many ETFs trade at a premium or discount to their net asset value (NAV). This paper targets corporate bond ETFs trading at a premium by shorting them and hedging the position with a portfolio of other liquid ETFs that replicate the NAV. Even after accounting for trading costs, the strategy delivers strong performance. Overall, the paper presents a practical approach for replicating ETFs that hold illiquid assets.
Crypto
Statistical Arbitrage within Crypto Markets using PCA
(Jung)
Avellaneda and Lee (2008) wrote a popular paper on statistical arbitrage in US equities. This paper employs the same framework used for cryptocurrencies. It extracts market factors using PCA, computes residual returns, and models them as mean-reverting processes using an Ornstein-Uhlenbeck model. While the strategy shows strong in-sample performance, out-of-sample results are weaker, but the paper offers a thorough walkthrough of the model's mechanics.
Playing the Market: Lottery Stock and Bitcoin Comovement
(Yang and Hoang)
Bitcoin comoves more strongly with lottery-like stocks than with other types of stocks. These are typically low-priced, volatile, and positively skewed stocks. The comovement intensifies during periods of high retail investor activity.
Equities
Clinging to Beliefs in Financial Markets: Solving the Post-Earnings Announcement Drift Puzzle
(McCarthy)
The post-earnings announcement drift (PEAD) is often viewed as a fading anomaly. However, this paper finds that it remains strong and significant when earnings surprises contradict analyst sentiment. Stocks disliked by analysts that report strong earnings, and vice versa, show return drifts that are about 2 to 5 times larger than when the news aligns with expectations. So if you want to trade on earnings surprises and PEAD, focus on stocks where the news contradicts investor expectations.
The Value of Information from Sell-side Analysts
(Lv)
Many investors use analyst reports, but it's unclear how much value they add beyond the numbers. This paper shows that the written commentary in these reports explains stock price moves better than earnings forecasts or target prices. Reports are most informative just after earnings announcements. Early access to analyst reports is shown to offer investors a significant economic edge.
Cash Flow Volatility, Return Predictability and Stock Price Decompositions: Why You Should Scale Prices by Trend Cash Flows
(Hillenbrand and McCarthy)
Many investors rely on valuation ratios like price-to-earnings to forecast stock returns, but their performance is often unreliable out of sample. This paper shows that the problem lies in the short-term noise in cash flow measures, which distorts these ratios. By using a Kalman filter to separate cash flows into a trend and a transitory component, and scaling prices by the trend part, the authors achieve much stronger and more stable return predictions.
Factor Investing Lecture 10: Factor Timing and Factor Allocation (Presentation Slides)
(Shi)
Many investors try to boost returns by adjusting their exposure to investment factors like value or momentum. These lecture notes review common approaches to "factor timing," such as using past performance, valuations, volatility, sentiment, and macroeconomic indicators. Most simple timing methods don't reliably beat a basic diversified portfolio. Hence, investors may want to be wary of relying too heavily on factor timing and instead focus on more consistent and robust allocation strategies.
An Information Factor: What Are Skilled Investors Buying and Selling?
(Ma, Martin, Ringgenberg, and Zhou)
Past research finds that insider purchases, short interest, and options trading volume relative to stock volume each help predict returns. This paper combines these signals into a single information score for each stock, which significantly forecasts returns across stocks. Hedge funds with greater exposure to this score tend to outperform, suggesting it captures informed trading and skill.
FOMO in equity markets? Concentration risk in (sustainable) investing
(Brogger, Koeter, and van Dijk)
Some investors favor concentrated portfolios, echoing Warren Buffett’s view that “diversification is protection against ignorance.” However, this paper shows that concentration increases risk in two key ways. First, effective global diversification requires far more stocks than commonly believed, closer to 750. Second, just a few percent of stocks drive nearly all market wealth, so small portfolios risk missing out. Investors should consider both volatility and the chance of missing top performers when choosing how concentrated to be.
Hedge Funds
Insider Trading and the Importance of an Ivy Education
(Didisheim, Fraschini, and Somoza)
Elite universities produce many hedge fund managers, but whether this background leads to better results has been debated. This study shows that graduates of top schools often achieve similar returns, hinting at shared ideas or information channels. When a major insider trading case shook the industry in 2009, their performance noticeably fell, pointing to the possibility that informal networks had been driving their earlier success.
The Leverage of Hedge Funds and the Risk of Their Prime Brokers
(Karagiorgis, Anastasiou, Drakos, and Ongena)
Some worry that heavily leveraged hedge funds could destabilize the financial system. This study finds that when hedge funds take on more debt, the banks and brokers that finance them face a higher chance of sharp declines in their own stock prices. The relationship holds across various tests. Hence, hedge fund borrowing may signal hidden risks to key financial firms.
Machine Learning and Large Language Models
Can Machines Better Predict Insider Trading?
(Batebi and Elnahas)
Insider trading is often hard to predict because motivations behind trades vary widely and aren't always tied to private information. This paper shows that machine learning models, especially XGBoost and Random Forest, are much better than traditional models at forecasting both the likelihood and size of insider selling. Results suggest that female insiders trade more based on private information than males. Overall, investors can use machine learning to more accurately spot informative trades.
Separating Sentiment From Fundamentals Using Large Language Model: How Does Sentiment Speak to the Crowd
(Chen, Pantelous, Tang, and Xie)
This paper fine-tunes a large language model, Sentiment-GPT, to isolate sentiment from fundamentals at the article level. Using over 55,000 firm-specific articles from major financial newspapers, it finds that sentiment predicts short-term price moves, but these effects reverse within a month, consistent with noise trading. A trading strategy based on this sentiment delivers 24.4% annual returns (13.9% after costs) with a Sharpe ratio of 0.56 (0.32), outperforming word-based methods that lose money after costs.
Regime-Switching Models
Asset Allocation Under Shifting Correlations
(Ryu)
Asset correlations shift with economic conditions, making traditional portfolio mixes like 60/40 vulnerable when diversification is needed most. This paper introduces a regime-switching strategy based on DCC-GARCH and k-means clustering, combined with a Black–Litterman allocation model, that adjusts the portfolio accordingly. The approach produces higher Sharpe ratios than benchmark portfolios.
Trend Following
The Science and Practice of Trend-following Systems
(Sepp)
This is a rigorous paper studying binary and continuous trend-following systems and their return dynamics. Trend strategies are shown to generate returns when long-term return autocorrelations are positive, even if short-term behavior is noisy or mean-reverting. The paper links performance to features of the underlying return process, such as drift and autocorrelation structure, and shows that properly tuned systems behave defensively in downturns. Moreover, the paper discusses how trend-following can be combined with long-only equity exposure in return-stacked portfolios to improve diversification.
Volatility
The Volatility Edge, A Dual Approach For VIX ETNs Trading
(Zarattini, Mele, and Aziz)
This paper presents a practical volatility trading framework using VIX-linked exchange-traded notes. The strategy seeks to capture the volatility risk premium while conditioning on the slope of the VIX term structure. Through simple, rule-based signals, the authors build a series of increasingly refined models that deliver strong risk-adjusted performance from 2008 to 2025.
Blogs
Weekly Research Insights - Testing New Research on Momentum Timing
(QuantSeeker)
The Science and Practice of Trend-following Systems: paper and presentation
(Artur Sepp)
Comprehensive Comparison of Algorithmic Trading Platforms
(Jonathan Kinlay)
Why Most Markets and Styles Have Been Lagging US Equities?
(Quantpedia)
GitHub
Awesome Pinescript
HftBacktest
Podcasts
AQR's Cliff Asness on Meme Stocks, Market Timing, Private Assets & More
(Money Stuff - Bloomberg Podcasts)
Trading Earnings Volatility with Options
(Chat With Traders)
Passive Investing Is Breaking the Market — Here’s the Hidden Cost (Rob Arnott & Cam Harvey)
(Meb Faber)
Big. Chunky. Changes. with Citrini Research
(Risk of Ruin)
Social Media
How Did We Get Here? A Brief History of Expected Returns Formation
(AQR)
From Tariffs To Trends: How Time Horizon Shapes Diversification
(Quantica Capital, via Jerry Parker)
Trend Following and Drawdowns: Is This Time Different?
(Man Group)
How Can “Smart Beta” Go Horribly Right?
(Research Affiliates)
Stacking Managed Futures
(Corey Hoffstein)
Chasing Buffett: Can You Get Berkshire Returns Without the Oracle?
(Meb Faber)
Seizing Alpha in Developed Markets
(Robeco)
Fun game - Guess the Sharpe
Last Week’s Most Popular Links
Decoding the Bond Market
(Haghani and White)
Do short-lived options reveal information asymmetry? Evidence from open interest and volume signals
(Hilliard, Hilliard, and Wu)
Dynamic allocation: extremes, tail dependence, and regime Shifts
(Luo, Wang, Jussa, Chen, and Alvarez)
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
Share

---

*由 Substack Strategy Tracker 自动抓取*
