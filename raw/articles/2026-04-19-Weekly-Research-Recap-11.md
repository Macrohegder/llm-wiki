# Weekly Research Recap

**原文链接**: https://www.quantseeker.com/p/weekly-research-recap-e68

**发布时间**: May 13, 2025

**抓取时间**: 2026-04-19 22:23:34

---

## 摘要

Weekly Research Recap
Latest research on investing and trading
QuantSeeker
May 13, 2025
6
2
Share
Time for another round of the latest investing research. Below is a curated list of last week’s highlights, each linked to the original source for easy access.
Appreciate your continued support! If you’re finding value in these posts, feel free to like and subscribe if you haven’t already.
Bonds
Cross-Bond Momentum Spillovers
(Wang, Wu, and Yang)
A large body of research has studied the predictability of corporate bond returns. This paper finds that bond returns can be predicted using the recent performance of other bonds covered by the same analysts. A long-short trading strategy based on this signal earns strong returns, especially for less liquid or less widely held bonds, though returns ar...

---

## 全文

Weekly Research Recap
Latest research on investing and trading
QuantSeeker
May 13, 2025
6
2
Share
Time for another round of the latest investing research. Below is a curated list of last week’s highlights, each linked to the original source for easy access.
Appreciate your continued support! If you’re finding value in these posts, feel free to like and subscribe if you haven’t already.
Bonds
Cross-Bond Momentum Spillovers
(Wang, Wu, and Yang)
A large body of research has studied the predictability of corporate bond returns. This paper finds that bond returns can be predicted using the recent performance of other bonds covered by the same analysts. A long-short trading strategy based on this signal earns strong returns, especially for less liquid or less widely held bonds, though returns are reported before costs. However, the effect fades quickly and disappears beyond a two-month horizon. The key insight is that analyst-linked bonds share information, but markets incorporate it with a delay.
Crypto
Decentralized Finance (DeFi) and Liquidity Mining: Opportunities and Challenges
(Abraham)
Investors often question whether popular DeFi tokens have any real value or are simply speculative bubbles. This paper shows that the prices of AAVE and YFI tokens closely reflect their underlying network activity and transaction volume. It also finds that metrics like active users and token velocity help explain their returns. Overall, the paper suggests investors can use on-chain data and network models to better value these tokens and time their trades.
Currencies
Generative AI and Fundamentals-Based Exchange Rate Forecasting
(Izadyar)
Several recent studies have used ChatGPT to generate news sentiment scores for predicting stock returns. This paper uses ChatGPT to assess economic releases and assign currency strength scores. A strategy that buys strong currencies and sells weak ones delivers consistent returns, with returns not explained by standard currency factors. Hence, it seems ChatGPT can effectively connect exchange rates to underlying economic fundamentals.
Rethinking Currency Factors: The Case for Mean-Variance Optimisation
(Fan, Kearney, Li, and Liu)
The authors use a broad sample of 48 currencies and construct long-short portfolios based on carry, value, and momentum signals. Instead of equal weighting, they apply simple mean-variance optimization separately within the long and short legs to assign portfolio weights. This approach leads to meaningful improvements in both returns and Sharpe ratios.
Equities
The Intersection of Expected Returns
(Sobotka)
A small group of stocks is shown to appear repeatedly across many anomaly portfolios, driving much of their performance. These “overlap” stocks make up about 10% of stocks each month but explain about 40% of anomaly returns. Allocating only to them delivers sizeable alpha, likely driven by mispricing rather than risk.
Stock-Bond Return Correlation: Understanding the Changing Behaviour
(McMillan)
Stock-bond return correlations have shifted significantly over time, both in magnitude and sign. This paper examines how growth, inflation, and interest rates drive these changes. For example, inflation shocks often move stock and bond prices in the same direction, increasing correlations, while market stress and flight-to-safety episodes typically push them in opposite directions, reducing correlations.
Market-Dependent Momentum and Institutional Ownership
(Wu)
The classic long-short momentum strategy is known for its crash risk and negative skewness, often managed through volatility scaling. This paper shows that simply flipping the momentum signal in down markets, based on the past 12-month market return, significantly improves performance, rivaling more complex approaches. The strategy works especially well among stocks with high institutional ownership, where momentum effects appear strongest.
Machine Learning and Large Language Models
Allocation-Focused Regimes and Applications to Dynamic Factor Investing
(Yu, Mulvey, and Nie)
Identifying market regimes in a robust manner is challenging. This paper takes a novel approach by comparing pairs of standard equity factors and using a statistical Jump Model to detect periods where one consistently outperforms the other. It then trains an XGBoost model to forecast the prevailing regime and allocate accordingly. The resulting strategy improves Sharpe ratios relative to a benchmark portfolio.
Machine Learning from a "Universe" of Signals: The Role of Feature Engineering
(Li, Rossi, Yan, and Zheng)
Many machine learning papers for stock return prediction rely on carefully selected signals that weren’t available to real-time investors. For example, they often assume published signals were known before their discovery. This paper evaluates machine learning using a broader and more realistic set of 18,000 fundamental signals available in real time. While the models generate meaningful returns, they underperform those using hand-picked predictors. Surprisingly, a simple method that ranks signals by past performance beats complex models, underscoring that feature engineering often matters more than the algorithm itself.
Machine Forecast Disagreement in the Cryptocurrency Market
(Chu, Shen, and Zhu)
A rich literature shows that stocks with high investor disagreement often earn lower future returns. This paper applies that idea to cryptocurrencies by simulating a set of investors, each using a random forest model trained on a subset of crypto characteristics to forecast returns. Disagreement is measured as the standard deviation of these forecasts across simulated investors. Cryptocurrencies with higher disagreement tend to underperform, offering a signal investors can use to avoid overpriced coins.
Can LLM-based Financial Investing Strategies Outperform the Market in Long Run?
(Waylon Li, Kim, Cucuringu, and Ma)
The paper argues that most investing strategies using large language models (LLMs) are evaluated over short timeframes and a narrow set of popular stocks, which can inflate their effectiveness. Introducing a new backtesting setup, the authors show that LLM-based strategies often underperform when tested over longer periods and a wider range of stocks. Interestingly, they find that LLMs tend to be too cautious in rising markets and too aggressive during downturns.
Machine Learning: a Lecture Note
(Cho)
These lecture notes are designed for Master’s and PhD students in Data Science and provide a structured foundation in core machine learning concepts.
Options
Measuring Option Liquidity
(Götz, Riordan, Schuster, and Uhrig-Homburg)
This paper proposes a new measure of option liquidity, the “Elasticity-Adjusted Spread (EAS)”, which ties transaction costs to the size of the hedge required in the underlying stock. EAS is shown to better detect liquidity stress, align with economic fundamentals, and also work reliably across different types of options. Investors can use it to assess liquidity more accurately and better manage trading costs.
Portfolio Optimization
Robust Optimization of Strategic and Tactical Asset Allocation for Multi-Asset Portfolios
(Sepp, Ossa, and Kastenholz)
Many asset allocation methods rely on unstable return forecasts and noisy covariance estimates. This paper proposes a practical alternative that handles both liquid and illiquid assets by focusing on each asset’s contribution to portfolio risk rather than predicting returns. It builds long-term allocations through risk budgets and adds short-term tilts using signals like momentum and low volatility.
Hierarchical risk clustering versus traditional risk-based portfolios: an empirical out-of-sample comparison
(Trucios)
Traditional mean-variance portfolios may perform poorly out of sample due to unstable estimates of risk and return. This paper compares them to hierarchical risk clustering methods, which avoid matrix inversion and aim to improve diversification. While these methods don’t consistently outperform in smaller portfolios, they show promise when applied to portfolios with a large number of assets.
Volatility
Stock Return Predictability of Realized-Implied Volatility Spread and Abnormal Turnover
(Eksi and Roy)
The volatility risk premium, defined as the difference between realized and implied volatility, is a well-known predictor of stock returns. This paper shows that realized volatility can be biased for stocks with unusually high or low trading volume, weakening the signal. By correcting for this distortion using a simple mean-reverting model, the authors significantly improve the performance of portfolios sorted on the volatility risk premium.
Blogs
Beta hedging
(Quantitativo)
Equity trend-following with market and macro data
(Macrosynergy)
Weekly Research Insights
(QuantSeeker)
FinTwit and LinkedIn
Understanding Return Expectations, Part 2
(@CliffordAsness)
Evidence Based MicroCap Research
(@RTelford_invest)
Trend Following’s Tricky Tradeoffs
(@RA_Insights)
The Case for International and Emerging Small Cap Stocks
(AQR)
Market Timing
(Man Group)
GitHub
Jesse
- Crypto trading
Alphalens
-
Performance analysis
Optopsy
- Options backtesting
Podcasts
Andrea Unger - 672% Returns? Sure! Would You Like Some Risk with That?
(The Algorithmic Advantage)
The Retail Rally Trap | Volatility Trader Kris Sidial on What's Next For This Fragile Market
(Excess Returns)
Systematic Trading For A Living - Laurens Bensdorp
(Desire To Trade)
Last Week’s Most Popular Links
Can I build a scalping bot? A blogpost with numerous double digit SR
(Rob Carver)
Characteristics-Based Reversals Exploiting the Gap between Predicted and Realized Returns
(Park, Yee, and Ko)
Macro-quantamental investment handbook
(Macrosynergy)
This Substack is reader-supported. To receive new posts and support my work, consider becoming a free or paid subscriber.
Subscribe
Disclaimer: This newsletter is for informational and educational purposes only and should not be construed as investment advice. The author does not endorse or recommend any specific securities or investments. While information is gathered from sources believed to be reliable, there is no guarantee of its accuracy, completeness, or correctness.
This content does not constitute personalized financial, legal, or investment advice and may not be suitable for your individual circumstances. Investing carries risks, and past performance does not guarantee future results. The author and affiliates may hold positions in securities discussed, and these holdings may change at any time without prior notification.
The author is not affiliated with, sponsored by, or endorsed by any of the companies, organizations, or entities mentioned in this newsletter. Any references to specific companies or entities are for informational purposes only.
The brief summaries and descriptions of research papers and articles provided in this newsletter should not be considered definitive or comprehensive representations of the original works. Readers are encouraged to refer to the original sources for complete and authoritative information.
This newsletter may contain links to external websites and resources. The inclusion of these links does not imply endorsement of the content, products, services, or views expressed on these third-party sites. The author is not responsible for the accuracy, legality, or content of external sites or for that of any subsequent links. Users access these links at their own risk.
The author assumes no liability for losses or damages arising from the use of this content. By accessing, reading, or using this newsletter, you acknowledge and agree to the terms outlined in this disclaimer.
6
2
Share

---

*由 Substack Strategy Tracker 自动抓取*
