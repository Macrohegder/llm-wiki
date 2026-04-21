# Weekly Research Recap

**原文链接**: https://www.quantseeker.com/p/weekly-research-recap-58e

**发布时间**: Apr 22, 2025

**抓取时间**: 2026-04-19 22:23:10

---

## 摘要

Weekly Research Recap
Latest research on investing and trading
QuantSeeker
Apr 22, 2025
7
Share
It’s time for another round of great investing research. Below is a curated selection of last week’s highlights, each linked to the original source for easy reading.
If you’re enjoying these posts, a like or subscribe is always appreciated, thank you for your support!
Commodities
Factor Momentum in China's Commodity Markets
(Li, Lei, and Wu)
Past research has shown that timing equity factors can be effective. This paper studies 12 commodity factors in China and finds strong evidence that time-series factor momentum outperforms and explains cross-sectional momentum. After 2017, the authors document a shift where a market-wide component, linked to financial variables rather than macroeconomic ones...

---

## 全文

Weekly Research Recap
Latest research on investing and trading
QuantSeeker
Apr 22, 2025
7
Share
It’s time for another round of great investing research. Below is a curated selection of last week’s highlights, each linked to the original source for easy reading.
If you’re enjoying these posts, a like or subscribe is always appreciated, thank you for your support!
Commodities
Factor Momentum in China's Commodity Markets
(Li, Lei, and Wu)
Past research has shown that timing equity factors can be effective. This paper studies 12 commodity factors in China and finds strong evidence that time-series factor momentum outperforms and explains cross-sectional momentum. After 2017, the authors document a shift where a market-wide component, linked to financial variables rather than macroeconomic ones, becomes a key driver of factor momentum.
Currencies
Auctions, Announcements, and Abnormal Returns
(Krohn and Vala)
Research has shown that returns and risk premia tend to cluster around major events like macroeconomic announcements. This paper finds that foreign currencies often appreciate sharply against the U.S. dollar on days with macro news, but only when those days follow a Treasury auction. Average returns range from 6 to 19 basis points, with especially large moves after inflation, employment, and GDP reports. The authors argue that this pattern arises because dealer balance sheets are stretched after auctions, limiting their capacity to take on risk, which results in spillovers into currency markets.
Equities
Global FOMO: The Pulse of Financial Markets Worldwide
(Bonaparte)
Fear of missing out (FOMO) is a common bias that drives investors to chase hype. This paper builds a global FOMO index from Google search trends based on six speculative search terms. When FOMO is high, future stock returns tend to fall, especially in democratic countries where sentiment plays a bigger role. The findings suggest that an aggregate sentiment signal like this could potentially be useful for market timing.
Fixed Income
Pricing of Corporate Bonds: Evidence From a Century-Long Cross-Section
(Ghaderi, Plante, Roussanov, and Seo)
Corporate bond research has long struggled with limited and inconsistent data, making it difficult to pin down what drives bond returns. By building a comprehensive dataset spanning more than a century, the authors show that many risk factors dismissed in earlier work do matter. Overall, the findings suggest that corporate bonds respond to many of the same sources of risk as stocks.
Machine Learning and Large Language Models
Machine Learning in Foreign Exchange
(Yuan)
Using a rich feature set of established currency predictors, macroeconomic variables, and their interactions, the author finds that neural networks can strongly predict FX excess returns. The interaction terms between global and currency-specific factors are key to this performance. The outperformance of neural networks over linear models suggests that nonlinear effects are important drivers of expected returns in currency markets.
Time-varying predictability in the European sovereign bond market
(O´Sullivan and Papavassiliou)
The authors construct a large set of bond-specific signals for European government bonds using high-frequency trading data, including measures of yield, liquidity, credit risk, and volatility. A LASSO-based model achieves significant return predictability, especially during crisis periods, and remains effective even after accounting for up to 50% of the bid-ask spread in costs.
Do Machine Learning Models Need to Be Sector Experts?
(Hanauer, Soebhag, Stam, and Hoogteijling)
Many factor and investment strategies unintentionally make sector bets, increasing risk without boosting returns. To address this, the authors compare three machine learning approaches: one that ignores industries and normalizes inputs and target variables across all stocks; one that normalizes within each industry and fits separate models per industry group; and a third that blends both. This blended model normalizes data within industries but trains on the full sample, reducing sector biases and benefiting from a larger training set. As a result, it delivers superior out-of-sample performance.
The Memorization Problem: Can We Trust LLMs' Economic Forecasts?
(Lopez-Lira, Tang, and Zhu)
Backtesting investment strategies with large language models (LLMs) often suffers from data leakage, introducing look-ahead bias and inflated results. This paper shows that LLMs can recall past data with remarkable accuracy, even when it's anonymized and masked. The findings imply that the safest approach is to backtest only on data beyond the model’s training cutoff or train the LLM using a walk-forward approach.
The Limited Virtue of Complexity in a Noisy World
(Cartea, Jin, and Shi)
Kelly et al. (2024) suggest there is a “virtue to complexity”, showing how performance improves as the model becomes increasingly overparameterized. However, this paper shows that when factor inputs are noisy, adding more complexity can backfire, with performance starting to decline as more factors are added. The key takeaway is that the benefits of complex models depend critically on data quality, when signals are noisy, simpler models may perform better.
Dynamic Asset Allocation with Reinforcement Learning
(Broda, De Nard, and Walker)
Using a rich set of market and macro features, the authors tackle an asset allocation decision with reinforcement learning and show that their approach consistently outperforms both mean-variance optimization and equal-weighted portfolios, even after accounting for trading costs.
Can Large Language Models Trade? Testing Financial Theories with LLM Agents in Market Simulations
(Lopez-Lira)
Financial markets increasingly rely on automated systems, but it's unclear how language models would behave as traders. In a simulated market, the paper shows that LLM agents stick to their assigned roles, e.g. value investor, even when it's unprofitable. Interestingly, their interactions produce realistic dynamics such as bubbles and sharp corrections. The author notes that the widespread use of similar LLM agents in real markets could trigger destabilizing behavior.
Volatility
Disaggregating VIX
(Degiannakis and Kafousaki)
Rather than forecasting the VIX directly, this paper breaks it into simpler components in the forms of trends and cycles using six different techniques. Each part is forecasted separately, and then recombined to produce a more accurate overall VIX prediction. This method outperforms standard approaches and delivers strong returns with meaningful Sharpe ratios when used in a simple VIX futures strategy.
Trading VIX on Volatility Forecasts: Another Volatility Puzzle?
(Degiannakis, Delis, Filis, and Giannopoulos)
Many traders rely on short-term volatility forecasts to guide daily trading, but this study finds that looking further ahead can lead to better results, even for trades held just one day. VIX forecasts made over a longer horizon outperform short-term predictions when used to trade VIX futures and S&P 500 futures the next day.
Blogs
FX tail risk premia
(Macrosynergy)
Researching trading ideas in Excel
(Robot Wealth)
Tariffs, saving, and investment
(John H. Cochrane)
Building a Survivorship Bias-Free Crypto Dataset with CoinMarketCap API
(Concretum Group)
What Works Below the 200-Day Moving Average?
(QuantSeeker)
Weekly Research Insights
(QuantSeeker)
GitHub
Python for Finance (O'Reilly)
- Python code for the book by Yves Hilpisch.
PyTrendFollow
- Systematic futures trading using trend following.
statsmodels
-
Statistical modeling and econometrics in Python.
Medium
9 Modern Python Libraries You Must Know in 2025!
(Kumar)
Predicting Default Risk with the Distance-to-Default Model
(Velasquez)
Evaluating Alpha Generating Factors
(Velasquez)
Podcasts
Kevin Davey Part I - It's All About Process in Algo Trading
(The Algorithmic Advantage)
Roxton McNeal and Siddharth Sethi – Building Multi-Strategy QIS Portfolios
(Flirting with Models)
The Endowment Playbook: Balancing Long-Term Goals with Current Market Volatility
(RCM Alternatives)
Timeless Lessons Amidst Market Chaos | 50 Great Investors Share Their Most Important Lesson
(Excess Returns)
Last Week’s Most Popular Links
Market-State Dependent Momentum Strategies: An Empirical Examination of Anomalies in Asset Pricing
(Rodon Comas)
pysystemtrade
Cross-Asset Trend Spillover: A Novel Factor for Corporate Bond Returns
(Fieberg, Liedtke, Schlag, and Zaremba)
This Substack is reader-supported. To receive new posts and support my work, consider becoming a free or paid subscriber.
Subscribe
Disclaimer: This newsletter is for informational and educational purposes only and should not be construed as investment advice. The author does not endorse or recommend any specific securities or investments. While information is gathered from sources believed to be reliable, there is no guarantee of its accuracy, completeness, or correctness.
This content does not constitute personalized financial, legal, or investment advice and may not be suitable for your individual circumstances. Investing carries risks, and past performance does not guarantee future results. The author and affiliates may hold positions in securities discussed, and these holdings may change at any time without prior notification.
The author is not affiliated with, sponsored by, or endorsed by any of the companies, organizations, or entities mentioned in this newsletter. Any references to specific companies or entities are for informational purposes only.
The brief summaries and descriptions of research papers and articles provided in this newsletter should not be considered definitive or comprehensive representations of the original works. Readers are encouraged to refer to the original sources for complete and authoritative information.
This newsletter may contain links to external websites and resources. The inclusion of these links does not imply endorsement of the content, products, services, or views expressed on these third-party sites. The author is not responsible for the accuracy, legality, or content of external sites or for that of any subsequent links. Users access these links at their own risk.
The author assumes no liability for losses or damages arising from the use of this content. By accessing, reading, or using this newsletter, you acknowledge and agree to the terms outlined in this disclaimer.
7
Share

---

*由 Substack Strategy Tracker 自动抓取*
