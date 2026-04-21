# Weekly Research Recap

**原文链接**: https://www.quantseeker.com/p/weekly-research-recap-4b4

**发布时间**: Jun 03, 2025

**抓取时间**: 2026-04-19 22:23:59

---

## 摘要

Weekly Research Recap
Latest research on investing and trading
QuantSeeker
Jun 03, 2025
7
1
Share
Hi there. It’s time for another roundup of the latest investing research. Below is a carefully curated list of great papers from last week, each linked to the original source for easy access.
Anomalies and p-hacking
Anomaly Persistence and Nonstandard Errors
(Coqueret and Perignon)
Many investing anomalies seem compelling, but their performance often depends on how they're tested. This paper demonstrates that overlapping design choices, such as holding periods and weighting, create strong correlations between results, making strategies appear more robust than they actually are. The authors propose a "path-specific resampling" method to improve inference around anomaly returns. Using it, they f...

---

## 全文

Weekly Research Recap
Latest research on investing and trading
QuantSeeker
Jun 03, 2025
7
1
Share
Hi there. It’s time for another roundup of the latest investing research. Below is a carefully curated list of great papers from last week, each linked to the original source for easy access.
Anomalies and p-hacking
Anomaly Persistence and Nonstandard Errors
(Coqueret and Perignon)
Many investing anomalies seem compelling, but their performance often depends on how they're tested. This paper demonstrates that overlapping design choices, such as holding periods and weighting, create strong correlations between results, making strategies appear more robust than they actually are. The authors propose a "path-specific resampling" method to improve inference around anomaly returns. Using it, they find that 29 of 33 anomalies remain significant, with momentum and trend strategies standing out. Hence, truly robust strategies are those that hold up across a wide range of reasonable implementation choices.
A Protocol for Causal Factor Investing
(Lopez de Prado and Zoonekynd)
Many factor-based investment strategies underperform because they rely on statistical models that capture correlation, not causation. This paper shows how such models can produce misleading signals and flawed investment decisions. It introduces a structured approach for building factor strategies grounded in causal reasoning, helping investors avoid spurious patterns, reduce risk, and improve out-of-sample performance.
Commodities
Commodity Inflation Risk Premium: A Powerful Characteristic for Commodity and Stock Market Returns
(Hou, Platanakis, Ye, and Zhou)
This paper introduces a new commodity signal that outperforms traditional factors such as basis and momentum. The authors recursively estimate a three-factor term structure model for each commodity’s futures curve to derive the Commodity Inflation Risk Premium, a forward-looking measure of upside risk. The signal not only improves commodity selection but also improves stock market return forecasts, suggesting a strong link between commodities and equities.
Crypto
Crypto Contagion
(Aldridge and Du)
Cryptocurrencies often experience sudden, sharp price movements. This paper develops a framework to separate normal price changes from abrupt jumps and analyzes how these jumps vary across different coins. It finds that large coins like Bitcoin jump less often but more severely, while smaller coins jump more frequently. The authors propose a portfolio strategy based on a jump-adjusted covariance matrix, which delivers higher Sharpe ratios than standard approaches, especially during volatile markets.
Equities
Co-Jump Asymmetry in U.S. Equity Markets
(Lin and Yu)
This paper studies how likely different stocks are to experience large jumps at the same time as the market. Stocks that tend to “co-crash” with the market, rather than “co-surge”, earn about 0.5% higher returns per month, likely as compensation for bearing systematic downside risk.
Asymmetries at the core of short-term return predictability
(Breckenfelder, Buchwalter, and Tedongap)
Some models for forecasting short-term market returns focus on rare, extreme events. This paper shows that typical day-to-day price moves may contain just as much, if not more, predictive power. By splitting high-frequency returns into typical (“core”) and extreme (“tail”) segments, the authors find that the imbalance between upside and downside volatility in the core, what they call “core asymmetry”, is a strong predictive signal. Hence, investors may improve short-term forecasts by paying attention to how skewed everyday returns are, as opposed to extreme returns.
Is the Best Dividend Strategy to Avoid Them?
(Faber)
Many investors love dividend-paying stocks for their steady income, but these payouts come with a hidden cost: Taxes. This paper shows that investors can often earn better after-tax returns by skipping dividends altogether and focusing instead on cheap stocks using value-based strategies. For taxable investors especially, avoiding dividends and choosing undervalued stocks may boost long-term gains while minimizing the tax drag.
Hedge Funds
Bear factor and hedge fund performance
(Ho, Kagkadis, and Wang)
Some hedge fund styles are seen as sellers of market insurance, earning steady returns in normal times but suffering large losses during crashes. This paper examines fund performance based on exposure to downside risk. It finds that funds with low sensitivity to a downside-risk factor consistently earn higher returns, not by taking on more risk, but by better adjusting their exposure when volatility rises. Investors may improve fund selection by favoring managers with low downside-risk betas.
Investing
Passive Aggressive: The Risks of Passive Investing Dominance
(Brightman and Harvey)
As passive investing becomes dominant, the paper suggests it distorts markets by pushing prices based on flows rather than fundamentals. The authors find that this trend increases stock co-movement, reduces diversification, and weakens price discovery. Stocks with higher passive ownership become more sensitive to broad market moves and less responsive to company-specific news. Investors may benefit from rebalancing strategies that tilt toward fundamental metrics rather than chasing recent price trends.
The Bear Market in Diversification
(Faber)
Many investors followed textbook advice: Build a globally diversified portfolio, rebalance, and stay the course. Yet over the past 15 years, such portfolios have consistently lagged behind the S&P 500. The paper suggests sticking with diversification, across geographies, assets, and factors, not because it always wins, but because it's the best defense when today's market darlings eventually fall out of favor.
Expected Outcomes of 401(k) Investing: What Can History Tell Us?
(McQuarrie and Bernstein)
Many Americans rely on 401(k) plans to fund retirement, expecting regular savings and long-term market growth to do the job. But looking at history, the paper suggests that this path has only worked reliably for those who were extremely frugal or lucky with market timing. The authors find that even with steady savings, market returns have been too inconsistent for most savers to fund a full retirement confidently.
Machine Learning and Large Language Models
Historical Perspectives in Volatility Forecasting Methods with Machine Learning
(Qiu, Kownatzki, Scalzo, and Cha)
Many investors and asset managers rely on models to forecast volatility for managing risk and pricing assets. Yet forecasting volatility is hard, being influenced by a wide mix of economic data, investor behavior, and unexpected shocks. The authors compare traditional models like GARCH to newer machine learning tools like LSTM and transformers. They find that LSTM models are the most accurate overall in predicting volatility, especially when data is limited or during volatile periods.
Hybrid Models for Financial Forecasting: Combining Econometric, Machine Learning, and Deep Learning Models
(Stempien and Slepaczuk)
Predicting returns is challenging, as financial markets are noisy and non-stationary. The authors compare traditional tools like ARIMA with newer machine learning methods and combine them into hybrid models. Merging linear and nonlinear approaches, especially ARIMA with LSTM or SVM, yields strategies that outperform individual models and even beat the market. Investors may gain an edge by exploring these well-structured hybrid approaches.
Options
Media Coverage, Volatility Overreaction, and Option Returns
(Yang)
When firms receive a surge in media attention, measured using RavenPack data, their option straddles tend to deliver weak returns the following month. This appears driven by investor overreaction, where implied volatility rises more than future realized volatility justifies. A long-short straddle strategy that exploits this effect based on media coverage earns strong returns with a high Sharpe ratio.
Betting on Stocks with Options?
(d’Avernas, Schlag, Sichert, Waibel, and Wang)
Many investors believe that if they can predict a stock’s return, they should be able to earn even higher returns by trading options on that stock. However, this paper finds that using expected stock returns to guide option trades doesn’t work well. While expected stock returns predict stock prices effectively, they fail to predict option returns. Hence, the paper suggests that investors looking to benefit from return forecasts should trade stocks directly rather than using options.
Risk Management
Narrative Factors and Risk Models
(Brown, de Silva, and Lee)
Traditional risk models ignore how investor attention to various themes and narratives impacts stock prices. This paper shows that ignoring these narrative-driven factors can lead to misjudging portfolio risk. Using news analytics, the authors build a method to measure narrative exposure and adjust risk models accordingly. Overall, the findings suggest that investors can potentially improve portfolio risk estimates and allocation decisions by incorporating narrative signals into existing factor models.
Blogs
Quickies #1: Overfitting and EWMAC forecast scalars
(Rob Carver)
How Uncertain Is the Estimated Probability of a Future Recession?
(Crump and Gospodinov - New York Fed)
Can We Finally Use ChatGPT as a Quantitative Analyst?
(Quantpedia)
Weekly Research Insights
(QuantSeeker)
Stop Losses: Rethinking Conventional Wisdom
(Robot Wealth)
FinTwit and LinkedIn
Post mortem of a (almost) 1 million dollar profit HFT strategy
(@crypto_hades)
Signs of the Times: Five Indicators of Regime Change
(Man Group)
A Hundred Visions and Revisions
(Man Group)
Why Are Bond Investors Contrarian While Equity Investors Extrapolate
? (@CliffordAsness)
Is private equity becoming a money trap?
(@verdadcap)
GitHub
Nautilus Trader
-
Algo trading platform
The Data Engineering Handbook
-
Collection of useful links
Medium
Automating Alpha: How AI Agents are Forging the Future of Quantitative Trading
(ArXiv In-depth Analysis)
Podcasts
Is Trend Following Dead? (Again…) A Deep Dive with Crabel’s Grant Jaffarian
(RCM Alternatives)
This 20-Year-Old Strategy Could Quietly Beat the Market (With Less Risk)
(The Meb Faber Show)
Last Week’s Most Popular Links
Tail Risk Hedging: The Superiority of the Naïve Hedging Strategy
(Cao and Conlon)
Adaptive Momentum Investing: Leveraging Volatility Regimes for Enhanced Returns.
(Filip)
Can Dividend-Price Ratio Predict Stock Return?
(Wang)
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
