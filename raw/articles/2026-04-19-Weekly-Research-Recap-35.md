# Weekly Research Recap

**原文链接**: https://www.quantseeker.com/p/weekly-research-recap-a60

**发布时间**: Oct 28, 2025

**抓取时间**: 2026-04-19 22:26:44

---

## 摘要

Weekly Research Recap
Latest research on investing and trading
QuantSeeker
Oct 28, 2025
7
2
Share
Hello! This week’s research recap highlights the most relevant investing insights from the past seven days, covering academic papers, industry research, social media, and blog posts, with direct links to every source.
Bonds
The Term Structure of Stock-Bond Covariances
(Gandhi)
After 2009, the term structure of stock–bond covariances turned downward-sloping, with long-maturity bonds providing a stronger equity hedge than short-maturity bonds. A new stock–bond factor based on these covariances predicts bond excess returns (R² > 20%) after 2010.
Key takeaway: Unconventional monetary policy post-GFC affected the stock–bond comovement, strengthening the hedging properties of long bonds.
Currencies
...

---

## 全文

Weekly Research Recap
Latest research on investing and trading
QuantSeeker
Oct 28, 2025
7
2
Share
Hello! This week’s research recap highlights the most relevant investing insights from the past seven days, covering academic papers, industry research, social media, and blog posts, with direct links to every source.
Bonds
The Term Structure of Stock-Bond Covariances
(Gandhi)
After 2009, the term structure of stock–bond covariances turned downward-sloping, with long-maturity bonds providing a stronger equity hedge than short-maturity bonds. A new stock–bond factor based on these covariances predicts bond excess returns (R² > 20%) after 2010.
Key takeaway: Unconventional monetary policy post-GFC affected the stock–bond comovement, strengthening the hedging properties of long bonds.
Currencies
Virtue or Mirage? Complexity in Exchange Rate Prediction
(Kılıç)
This paper predicts monthly FX returns using macro fundamentals, comparing standard linear regressions with a more complex ridge model employing Random Fourier Features (RFF). The RFFs apply nonlinear transformations to monetary, non-monetary, and Taylor-rule variables. Complexity yields modest gains in short samples (12-month windows) but remains unstable. In longer samples (60–120 months), linear models outperform Ridge-RFF and often surpass the random walk.
Key takeaway: In FX forecasting, simplicity proves more robust than complexity.
Equities
Optimism Everywhere: Beliefs during Stock Price Bubbles
(Greenwood and Stolborg)
Analyzing 5,300 U.S. stock-level bubbles, defined as stocks that double in price and later crash by 50%, the paper finds analysts remain euphoric at peaks, projecting 52% one-year returns and 30% long-term growth, while short interest stays low (~5%) and media rarely mention overvaluation. Greater optimism predicts higher crash probability.
Key takeaway: Bubbles stem from collective optimism, not dissent, making them hard to spot in real time.
Dark Side of the Day: Overnight Price Jumps and Short-Term Return Predictability
(Bahcivan, Dam, and Gonenc)
Analyzing 9,283 U.S. stocks, the paper finds that overnight price jumps, both positive and negative, reflect investor overreaction and are sharply reversed the next trading day. Regression coefficients show strong negative predictability (t-stats ≈ –11 for positive jumps, –4 for negative).
Key takeaway: Overnight shocks cause short-lived mispricing that is largely corrected the following trading day.
Machine Learning and Large Language Models
Aligning Multilingual News for Stock Return Prediction
(Wu, Tao, Cheng, Martineau, Nozawa, Hull, and Veneris)
This paper aligns semantically equivalent sentences across English and Japanese financial news using a novel method. Analyzing 140,000 Bloomberg articles (2012–2024) on 3,500 Tokyo stocks, the authors find that aligned cross-language content yields clearer signals, with trading portfolios achieving an annualized Sharpe of 4.36 (before costs), about twice that of unaligned news.
Key takeaway: Overlapping news coverage across languages carries the most reliable, tradable information.
Causal and Predictive Modeling of Short-Horizon Market Risk and Systematic Alpha Generation Using Hybrid Machine Learning Ensembles
(Ranjan)
The author develops a hybrid machine learning ensemble to forecast five-day SPY drawdowns using 178 cross-asset features spanning equities, bonds, FX, commodities, and volatility. The model goes long when predicted crash probability < 0.5 and short when ≥ 0.5. Over 2005–2025, it achieves a Sharpe ratio of 2.51 (before costs), an annual return of 40.8%, and a beta of 0.51.
Key takeaway: Cross-asset signals, especially short-horizon Hurst-based features, contain valuable predictive information about near-term SPY drawdowns.
Portfolio Management
Revisiting the Structure of Trend Premia: When Diversification Hides Redundancy
(Etienne, Ohana, Benhamou, Guez, Setrouk, and Jacquot)
The authors revisit multi-horizon trend-following using a Bayesian framework that dynamically reallocates weights across 20-, 60-, 125-, 250-, and 500-day signals. The widely assumed value of the 125-day “medium-term” horizon proves overstated, adding little distinct information. Excluding it modestly lifts Sharpe ratios and improves drawdowns.
Key takeaway: Meaningful diversification in trend models comes from combining short- and long-term signals while mid-range horizons add noise rather than diversification.
Thematic Investing in Total Portfolio Factor Lens
(Lee and Liu)
Investment themes are modeled as missing factors by adding narrative-based exposures, derived from RavenPack news on AI, robotics, cybersecurity, blockchain, and cloud computing, into an augmented factor model that is orthogonalized to standard risk factors. Narrative-based portfolios outperform ETFs, with information ratios of 0.97 (AI) and 0.76 (multi-theme) versus 0.70 (AIQ) and –0.06 (ARKK).
Key takeaway: Thematic factors represent “missing” risk factors and enable pure, risk-managed exposures.
Asset classes and portfolio diversification: evidence from a stochastic spanning approach
(Nguyen, Topaloglou, and Walther)
A stochastic spanning test shows that adding commodities, currencies, and real estate to traditional stock–bond portfolios consistently enhances performance. Across seven portfolio configurations, investors who omit these assets lose 0.11–0.77% per month in foregone returns. The diversification gains persist out-of-sample and strengthen during economic downturns.
Key takeaway: Alternative assets, especially commodities and FX, provide robust diversification benefits beyond conventional portfolios.
Volatility
Mind the Gap: Continuous Volatility Gaps and Option Momentum
(Gan and Nguyen)
Option momentum is strongest when the gap between realized and implied volatility (RV–IV) evolves smoothly over time, as investors underreact to gradual information. Using 564,000 delta-neutral straddles (1996–2023), monthly option momentum profits climb from 2% to 9% for continuous RV–IV patterns and persist after costs and across years. The effect is most pronounced among small, low-attention firms.
Key takeaway: Smooth, continuous RV–IV gaps foster investor inattention and amplify option momentum.
Optimal Variance Forecasting in a Trading Context
(Taylor)
The author introduces a “Risk Knowledge (RK)” loss function that makes volatility forecasts more trading-relevant by strongly penalizing underestimated risk. Applied to volatility-targeting SPY and other U.S. ETFs, standard MSE forecasts add little value, while RK-optimized ones deliver significant gains.
Key takeaway: RK-based forecasts improve vol-targeting by aligning volatility estimates with real trading performance.
Do S&P500 Options Increase Market Volatility? Evidence from 0DTEs
(Adams, Dim, Eraker, Fontaine, Ornthanalai, and Vilkov)
Contrary to popular belief, S&P 500 zero-day-to-expiration (0DTE) options reduce, not amplify, market volatility. From 2018 to 2024, market makers’ hedging needs and gamma positions dampen realized volatility, induce order-flow reversals, and weaken short-term momentum, creating mean reversion in prices.
Key takeaway: 0DTE trading stabilizes markets by enhancing liquidity and promoting mean reversion rather than amplifying shocks.
Blogs
Diversified trend following in emerging FX markets
(Macrosynergy)
Do Stop-Loss Rules Add Value in Tactical Asset Allocation?
(Quantseeker)
Podcasts
Nick Radge: Want Big Fish? You’ll Need a Bigger Rod
(The Algorithmic Advantage)
Diego Ivan Cortes Lopez - Winning Through Losing: When 30% Is Enough
(Chat With Traders)
Zero Times in History | Meb Faber on What Happens After We Cross 40 CAPE
(Excess Returns)
Engineering Alpha using Trend and Volatility on Equity Beta with Eric Leake of ALTUS Private Capital
(RCM Alternatives)
Social Media & Industry Research
Where Factors Speak Loudest: Why Size Matters in Factor Investing
(Alpha Architect)
The compromising iPad photos that dragged a London quant trader to court
(City AM, via MTZ)
Open Source Asset Pricing data - Oct 2025 Release
(Andrew Chen)
Food for Thought: Tracking Error (AQR)
What Are We Buying When We Buy Gold?
(Man Group)
Fast-Money Quants Stumble as Momentum Bust Roils Strategies
(Justina Lee, Bloomberg)
Last Week’s Most Popular Links
Enhancing global equity returns with trend-following and tail risk hedging overlays
(Schwalbach and Auret)
A little peep inside one of London’s hot new quant powerhouses
(FT Alphaville)
Equity Valuation Without DCF
(Cho, Polk, and Rogers)
This Substack is reader-supported. Subscribe to get new research insights, strategy breakdowns, and exclusive posts, and help support my work.
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
