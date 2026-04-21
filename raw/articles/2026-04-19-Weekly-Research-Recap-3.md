# Weekly Research Recap

**原文链接**: https://www.quantseeker.com/p/weekly-research-recap

**发布时间**: Mar 18, 2025

**抓取时间**: 2026-04-19 22:22:25

---

## 摘要

Weekly Research Recap
Latest research on investing and trading
QuantSeeker
Mar 18, 2025
12
1
Share
It’s time for another roundup of the latest investing research. Below is a carefully curated selection of last week’s highlights, with each title linking directly to its source for further reading.
Thank you for reading and don’t forget to hit the like button.
Crypto
Including Cryptos in Equity Portfolios: Trend or Opportunity?
(Cesarone, Figa-Talamanca, and Luciani)
Cryptocurrencies have drawn attention as a new asset class, but should investors add them to equity portfolios? This paper examines different portfolio construction techniques, Minimum Variance (MV), Risk Parity (RP), Most Diversified Portfolio (MDP), and Equally Weighted (EW), using stocks alone and in combination with cryptocur...

---

## 全文

Weekly Research Recap
Latest research on investing and trading
QuantSeeker
Mar 18, 2025
12
1
Share
It’s time for another roundup of the latest investing research. Below is a carefully curated selection of last week’s highlights, with each title linking directly to its source for further reading.
Thank you for reading and don’t forget to hit the like button.
Crypto
Including Cryptos in Equity Portfolios: Trend or Opportunity?
(Cesarone, Figa-Talamanca, and Luciani)
Cryptocurrencies have drawn attention as a new asset class, but should investors add them to equity portfolios? This paper examines different portfolio construction techniques, Minimum Variance (MV), Risk Parity (RP), Most Diversified Portfolio (MDP), and Equally Weighted (EW), using stocks alone and in combination with cryptocurrencies from 2018 to 2023. The results show that MDP and RP perform best, benefiting the most from crypto diversification with higher returns and improved risk-adjusted performance.
Equities
Volume Shocks and Overnight Returns
(Cartea, Cucuringu, Jin, and Wilson)
Periods of unusually high trading activity can indicate shifts in investor sentiment or new information entering the market. The authors find that stocks experiencing abnormal intraday trading volume, measured relative to historical averages, tend to earn higher returns overnight but not during the next trading session. Traditional explanations, such as investor attention or risk factors, don't fully account for this pattern. Therefore, investors and traders might explore overnight strategies that condition on abnormal volume patterns.
Long-Horizon Forecasts
(Balashov and Pisciotta)
Some brokerage firms encourage their analysts to make long-term earnings predictions, even though these forecasts are, on average, about 49% less accurate than shorter-term ones. The paper finds that analysts at firms prioritizing publicity over precision are more likely to issue them, as they help attract clients. However, making these forecasts can hurt an analyst’s chances of moving to top-tier firms. As a result, investors should be cautious about relying on long-term forecasts.
Moving Beyond the Mean: Explaining the Cross-Sectional Tails with Firms’ Characteristics
(Uribe, Guillen, and Vidal-Llana)
Most asset pricing models focus on explaining average stock returns, but this paper demonstrates that the same factors influence high- and low-performing stocks in distinct ways. Using quantile regressions, the authors show that size, book-to-market, momentum, and liquidity have varying effects across the return distribution. For instance, market beta boosts high-return stocks (95th percentile) but harms low-return stocks (5th percentile), while size plays a more significant role at the extremes than in the middle. Investors should therefore recognize that risk factors behave differently in bull and bear markets, impacting the estimation of tail risks.
Do Sell-side Analyst Reports Have Investment Value?
(Lv)
Markets often overreact to short-term negative news, but analyst reports may contain overlooked long-term insights. Leveraging large language models on 1.2 million reports, this study finds that strategic outlook discussions, which highlight growth potential and valuation, are the most predictive of future returns. Surprisingly, the predictive power is strongest for large, mature firms with extensive analyst coverage. Investors can benefit by focusing on stocks where analysts identify strong long-term fundamentals despite near-term setbacks, such as weak earnings.
Machine Learning and Large Language Models
Are Large Language Models Good In-context Learners for Financial Sentiment Analysis?
(Wei and Liu)
Classifying sentiment in financial news and social media can be valuable for investors and traders but challenging due to complex and ambiguous language. This paper shows that large language models (LLMs) can enhance financial sentiment analysis with well-chosen labeled examples in their prompts. The findings suggest that investors can leverage LLMs effectively for sentiment classification without expensive model retraining.
Deep Learning of Conditional Volatility and Negative Risk-Return Relation
(Ma, Wu, and Yan)
Investors commonly assume higher risk leads to higher returns, yet extensive research has shown the opposite: stocks with lower volatility often deliver higher risk-adjusted returns. This paper reinforces that relationship using deep neural networks trained on characteristics such as momentum, firm size, short-term reversal, and liquidity to simultaneously forecast stock returns and volatility over a one-month horizon. Double-sorted portfolios, going long stocks with high expected returns and low predicted volatility, and short stocks with low expected returns and high predicted volatility, generate meaningful Sharpe ratios.
The Uncertainty of Machine Learning Predictions in Asset Pricing
(Liao, Ma, Neuhierl, and Schilling)
Investors increasingly use machine learning to predict asset returns, but these forecasts typically overlook their inherent uncertainty. To address this gap, the authors develop methods to construct confidence intervals around predictions, explicitly quantifying forecast uncertainty. Using a cautious "max-min" optimization approach, investors build portfolios that consider the worst-case return scenarios from these intervals. Practically, this means investing less, or not at all, in assets whose expected returns are highly uncertain, ultimately leading to portfolios that outperform classical mean-variance strategies by reducing downside risk.
FinTSBridge: A New Evaluation Suite for Real-world Financial Prediction with Advanced Time Series Models
(Wang, Xu, Gao, Zhang, Huang, Sun, and Zhang)
Many financial forecasting models struggle with non-stationarity and noise, making them unreliable for real-world trading. This paper introduces FinTSBridge, a framework that evaluates advanced time-series models using three specialized datasets. By incorporating correlation-based evaluation metrics alongside traditional error measures, the study identifies models that not only minimize prediction errors but also capture meaningful market patterns, making them more reliable for investment decisions.
Tactical Asset Allocation with Macroeconomic Regime Detection
(Cunha Oliveira, Sandfelder, Fujita, Dong, and Cucuringu)
Markets move through different economic regimes, but identifying these shifts in real time is challenging. This research applies clustering techniques to classify macroeconomic regimes using 127 indicators from the FRED-MD database. It integrates these classifications into Black-Litterman portfolio models, using ETF data to adjust allocations based on expected regime shifts. The approach improves returns, Sharpe ratios, and downside protection compared to traditional strategies, helping investors dynamically adjust portfolios to changing market conditions.
Leveraging LLMS for Top-Down Sector Allocation In Automated Trading
(Quek, Heng, Vittori, Ong, Mao, Cambria, and Mengaldo)
Integrating macroeconomic trends and sentiment in sector allocation strategies can be challenging. This paper applies large language models to dynamically adjust sector weightings by processing macroeconomic data (inflation, employment, growth, monetary policy) and market sentiment (news-based sentiment analysis). Using a multi-agent system, including a Macro Agent, Sentiment Agent, and Ranking Agent, the framework identifies which sectors to overweight or underweight based on prevailing conditions. Backtesting results show this approach outperforms traditional momentum strategies, delivering higher Sharpe ratios.
Portfolio Management
Isotropic Correlation Models for the Cross-Section of Equity Returns
(Giller)
Traditional models assume that diversifying a portfolio eliminates individual stock risks, leaving only broad market factors. This paper challenges that idea by proposing a model where stock returns share a common correlation rather than following multi-factor structures. The study finds that real-world stock market data aligns better with this simpler correlation model than with conventional factor models.
Blogs
Macro trading signal optimization: basic statistical learning methods
(Macrosynergy)
The Impact of the Inflation on the Performance of the US Dollar
(Quantpedia)
On inflation and stock returns
(Outcastbeta)
GitHub
OpenBB LLM Agents
R&D playground to play with agents and OpenBB.
Riskfolio-Lib
Portfolio Optimization and Quantitative Strategic Asset Allocation in Python.
Finance Toolkit
Transparent and Efficient Financial Analysis.
Medium
VectorBT: The Unsung Hero of Trading Backtests
(Unicorn Day)
3 Advanced Approaches to Tackle Domain-specific Text Classification
(Kaitai Dong)
Statistical Arbitrage Copulas: Efficacy of Conditional Probability Strategies vs Cointegration
(Reid)
Podcasts
CTAs vs ETFs: The Showdown That Could Change Everything ft. Andrew Beer and Tom Wrobel
(Top Traders Unplugged)
Trend Following Trading Systems
(Michael Covel)
Last Week’s Most Popular Links
Regimes
(Mulliner, Harvey, Xia, Fang, and Van Hemert)
FinanceDatabase
A database of 300.000+ symbols containing Equities, ETFs, Funds, Indices, Currencies, Cryptocurrencies, and Money Markets.
Derivative Arbitrage Strategies in Cryptocurrency Markets
(Valery)
This Substack is reader-supported. To receive new posts and support my work, consider becoming a free or paid subscriber.
Subscribe
Disclaimer: This newsletter is for informational and educational purposes only and should not be construed as investment advice. The author does not endorse or recommend any specific securities or investments. While information is gathered from sources believed to be reliable, there is no guarantee of its accuracy, completeness, or correctness.
This content does not constitute personalized financial, legal, or investment advice and may not be suitable for your individual circumstances. Investing carries risks, and past performance does not guarantee future results. The author and affiliates may hold positions in securities discussed, and these holdings may change at any time without prior notification.
The author is not affiliated with, sponsored by, or endorsed by any of the companies, organizations, or entities mentioned in this newsletter. Any references to specific companies or entities are for informational purposes only.
The brief summaries and descriptions of research papers and articles provided in this newsletter should not be considered definitive or comprehensive representations of the original works. Readers are encouraged to refer to the original sources for complete and authoritative information.
This newsletter may contain links to external websites and resources. The inclusion of these links does not imply endorsement of the content, products, services, or views expressed on these third-party sites. The author is not responsible for the accuracy, legality, or content of external sites or for that of any subsequent links. Users access these links at their own risk.
The author assumes no liability for losses or damages arising from the use of this content. By accessing, reading, or using this newsletter, you acknowledge and agree to the terms outlined in this disclaimer.
12
1
Share

---

*由 Substack Strategy Tracker 自动抓取*
