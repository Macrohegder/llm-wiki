# Weekly Research Recap

**原文链接**: https://www.quantseeker.com/p/weekly-research-recap-1a4

**发布时间**: Jun 17, 2025

**抓取时间**: 2026-04-19 22:24:17

---

## 摘要

Weekly Research Recap
Latest research on investing and trading
QuantSeeker
Jun 17, 2025
7
3
Share
Hi! Here’s this week’s curated roundup of top investing research and resources. Each paper is linked to its original source for easy access.
Bonds
Decoding the Bond Market
(Haghani and White)
Investors often look to bonds for clues about future interest rates and inflation. This paper explains how to extract such signals from current market yields. After adjusting for convexity and risk premia, the authors find that markets expect long-term real rates to be near 1.75% and inflation to be around 2.1%. Given the low compensation for risk, especially inflation risk, they suggest investors may prefer inflation-protected bonds like TIPS.
Crypto
Sentiment in the Cross Section of Cryptocurrency Retur...

---

## 全文

Weekly Research Recap
Latest research on investing and trading
QuantSeeker
Jun 17, 2025
7
3
Share
Hi! Here’s this week’s curated roundup of top investing research and resources. Each paper is linked to its original source for easy access.
Bonds
Decoding the Bond Market
(Haghani and White)
Investors often look to bonds for clues about future interest rates and inflation. This paper explains how to extract such signals from current market yields. After adjusting for convexity and risk premia, the authors find that markets expect long-term real rates to be near 1.75% and inflation to be around 2.1%. Given the low compensation for risk, especially inflation risk, they suggest investors may prefer inflation-protected bonds like TIPS.
Crypto
Sentiment in the Cross Section of Cryptocurrency Returns
(John, Li, and Liu)
Many investors would agree that cryptocurrencies are heavily influenced by hype and sentiment. This paper builds a broad sentiment index and finds that coins highly sensitive to sentiment shifts tend to underperform over the next month. Adding this sentiment factor improves standard models of crypto returns. Investors may benefit from avoiding coins with high sentiment exposure following periods of market euphoria.
Currencies
Dynamic Currency Mispricing and Arbitrage Profits
(Hong, Li, and Sarno)
This paper builds a dynamic model to detect short-term pricing errors in currencies using projected principal component analysis and finds that mispricing is widespread. A trading strategy based on these mispricings achieves a Sharpe ratio of around 0.8 (pre-costs), driven largely by emerging markets, and its performance cannot be explained by standard currency factors.
Equities
Factoring in the Low-Volatility Factor
(Soebhag, Baltussen, and van Vliet)
Many studies confirm that low-volatility stocks deliver better risk-adjusted returns, but puzzlingly, this factor is often left out of popular pricing models. This paper shows that when you account for practical trading issues and separate long from short positions, the low-volatility factor adds meaningful value. Hence, investors should consider adding low-risk stocks, especially on the long side, as these tend to improve portfolio efficiency even after costs.
Learning from the Wisdom of Mutual Fund Managers
(Tedongap and Tinang)
The authors introduce a method to gauge how much fund managers are overweighting individual stocks and find that these favored stocks tend to outperform. By applying machine learning to predict these preferences in real-time, they develop a practical strategy that consistently beats the market and delivers significant alpha.
How much is too much? Why 60% in US equities isn't as crazy as it might sound
(Battistella and McLoughlin)
Many investors worry that holding too much US stock is risky, especially with current high valuations. This paper compares US stocks to international markets and shows that the large US allocation seen in global indices is not unreasonable. Thanks to lower risk and stronger earnings growth, US stocks often dominate the optimal portfolio even under equal or conservative return assumptions. Hence, investors may not need to cut US exposure as much as they think.
Conditional Betas: a Non-Standard Approach
(Rodrigues, Schotman, and Schyns)
Estimating market betas with traditional regressions and fixed time windows often leads to noisy, lagging estimates. This paper introduces a neural network approach that adapts to new data and captures non-linear shifts in stock–market relationships. It delivers more accurate beta forecasts and helps investors build better hedged portfolios.
Machine Learning and Large Language Models
(Generative) AI in Financial Economics
(Mo and Ouyang)
Many aspects of financial economics are being redefined by AI. This extensive review paper explores how recent advances in generative AI are transforming tasks such as forecasting returns, analyzing financial texts, and automating investment decisions.
Exploring Microstructural Dynamics in Cryptocurrency Limit Order Books: Better Inputs Matter More Than Stacking Another Hidden Layer
(Wang)
Short-term price prediction in crypto markets can be challenging due to noisy limit order book data. This paper tests whether deeper neural networks improve accuracy or if better data preprocessing and feature design matter more. The results show that with well-prepared inputs, simpler models can match or even outperform complex ones. Investors should therefore prioritize clean data and clever feature engineering over model complexity in short-term trading.
Options
Do short-lived options reveal information asymmetry? Evidence from open interest and volume signals
(Hilliard, Hilliard, and Wu)
This paper finds that unusual activity in short-dated, out-of-the-money options, especially spikes in volume and open interest, predicts next-day stock returns and may reflect informed trading ahead of corporate events. A long-short strategy based on these signals delivers strong returns.
Option Strategies and Market Signals: Do They Add Value to Equity Portfolios?
(Blanc, Fragniere, Naya, and Tuchschmid)
Traditional equity-bond portfolios have struggled in recent market regimes, leading investors to explore alternative approaches. This study tests whether five common trading signals, momentum, historical volatility, trend, implied volatility, and skew, can enhance basic option strategies like covered calls and protective puts. It finds that trend signals improve performance the most, especially for protective puts. Investors can use these signals to make option overlays more effective without added complexity.
Sentiment and the Equity Options Market
(Warkulat, Pelster, and Weiss)
Does online sentiment affect options markets? This paper shows that firm-specific social media sentiment, measured from X posts about S&P 500 stocks, can predict short-term returns on delta-hedged call options. Surprisingly, call options tied to stocks with
less
positive sentiment tend to deliver higher returns.
Decomposing Option Anomaly Returns
(Hollstein and Wese Simen)
What drives option anomaly returns? This paper breaks down 22 anomalies into outright and delta-hedged components and finds that much of the profit stems from predictable changes in implied volatility and mispriced volatility risk premia, rather than compensation for traditional risk.
The Information in Option Strike Price Introductions
(Lee)
Do new option strike prices contain useful information? This paper finds that when exchanges introduce strikes far above or below recent levels, the underlying stocks tend to drift in the same direction over the next year. The effect is stronger when trading patterns suggest informed investor activity. Several profitable strategies are tested. Investors can potentially use these extreme listings as subtle signals of future stock moves.
Portfolio Construction
Multivariable Kelly Criterion and Leverage
(Smirnov and Dapporto)
This paper revisits the Kelly criterion and demonstrates how to calculate the optimal leverage to maximize long-term portfolio growth, for both single assets and multi-asset portfolios. For the S&P 500, it finds that the ideal historical leverage has been around 2.4. Going beyond that point reduces long-run growth, as volatility and drawdowns begin to dominate. While not discussed in the paper, it is common in practice to use a fraction of full Kelly, half Kelly being a popular choice, to manage risk.
Regime-Switching Models
Dynamic allocation: extremes, tail dependence, and regime Shifts
(Luo, Wang, Jussa, Chen, and Alvarez)
Traditional risk models often assume markets behave normally, overlooking features like volatility clustering and extreme losses. This paper introduces a more advanced approach that captures these real-world dynamics and adjusts to shifting market conditions. Specifically, the authors combine a GARCH-DCC-Copula model with a Markov switching framework to identify risk regimes. Incorporating these regimes into tactical asset allocation improves risk-adjusted returns in both multi-asset and factor-based strategies.
Blogs
Weekly Research Insights - Testing A New Signal to Avoid Momentum Crashes (QuantSeeker)
Absolute Valuation Models for the Stock Market: Are Indexes Fairly Priced?
(Quantpedia)
Generating Synthetic Equity Data with Realistic Correlation Structure
(QuantStart)
GitHub
Awesome LLM Apps
Podcasts
Cesar Alvarez - A Novel Way to Combine Trend, Reversion, ETFs, Volatility & More!
(The Algorithmic Advantage)
Trend Systems Under Strain ft. Nick Baltas
(Top Traders Unplugged)
The Hidden Risk Behind ETF Growth | Eric Balchunas and Dave Nadig Debate If We've Gone Too Far
(Excess Returns)
Alex Edmans: Finding "The Truth" in Economics, Finance, and Life
(Rational Reminder)
Social Media
Greg Coffey on risk management and more at Sohn 2024
(via Jerry Parker)
More Financial Advisers Are Outsourcing Investment Decisions
(via Andrew Beer)
Tudor Jones on Next Fed Chair, Trump Budget, Markets, AI
(Bloomberg TV)
The alpha model of Theseus
(Owen Lamont - Acadian Asset Management)
Inside a Top Quant's Playbook | Joe Gubler on the Hidden Drivers of Alpha
(via Andreas Himmelreich)
Truth or Trend: Separating Signal from Noise
(Man Group)
Are V-Shaped Recoveries Becoming More Frequent?
(Man Group)
Last Week’s Most Popular Links
Skewness Premium for Short-Term Exposure to Squared Market Returns
(Wallmeier)
Investor sentiment and stock returns: Wisdom of crowds or power of words? Evidence from Seeking Alpha and Wall Street Journal
(Lachana and Schröder)
Systematic Strategies & Quant Trading 2025
(HedgeNordic)
This Substack is reader-supported. To receive new posts and support my work, consider becoming a free or paid subscriber.
Subscribe
Disclaimer: This newsletter is for informational and educational purposes only and should not be construed as investment advice. The author does not endorse or recommend any specific securities or investments. While information is gathered from sources believed to be reliable, there is no guarantee of its accuracy, completeness, or correctness.
This content does not constitute personalized financial, legal, or investment advice and may not be suitable for your individual circumstances. Investing carries risks, and past performance does not guarantee future results. The author and affiliates may hold positions in securities discussed, and these holdings may change at any time without prior notification.
The author is not affiliated with, sponsored by, or endorsed by any of the companies, organizations, or entities mentioned in this newsletter. Any references to specific companies or entities are for informational purposes only.
The brief summaries and descriptions of research papers and articles provided in this newsletter should not be considered definitive or comprehensive representations of the original works. Readers are encouraged to refer to the original sources for complete and authoritative information.
This newsletter may contain links to external websites and resources. The inclusion of these links does not imply endorsement of the content, products, services, or views expressed on these third-party sites. The author is not responsible for the accuracy, legality, or content of external sites or for that of any subsequent links. Users access these links at their own risk.
The author assumes no liability for losses or damages arising from the use of this content. By accessing, reading, or using this newsletter, you acknowledge and agree to the terms outlined in this disclaimer.
7
3
Share

---

*由 Substack Strategy Tracker 自动抓取*
