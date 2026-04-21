# Weekly Research Recap

**原文链接**: https://www.quantseeker.com/p/weekly-research-recap-97f

**发布时间**: Nov 04, 2025

**抓取时间**: 2026-04-19 22:26:52

---

## 摘要

Weekly Research Recap
Latest research on investing and trading
QuantSeeker
Nov 04, 2025
7
1
Share
Hello! This week’s research recap brings you the most important investing insights from the past seven days, spanning academic papers, industry reports, social media, and blogs, with direct links to every source.
Asset Allocation
Dynamic Dragon: Integrating Regime Detection into Strategic Asset Allocation
(Ni)
This paper refines the Dragon Portfolio proposed by Artemis Capital Management by replacing its static 20%-per-asset mix (equities, bonds, gold, commodity trend-following, long volatility) with regime-dependent weights identified via a Gaussian Mixture Model using cross-asset price features. Five regimes emerge: Crisis, Expansion, Tech Boom, QE, and Stagflation. In-sample (1927–2019) ret...

---

## 全文

Weekly Research Recap
Latest research on investing and trading
QuantSeeker
Nov 04, 2025
7
1
Share
Hello! This week’s research recap brings you the most important investing insights from the past seven days, spanning academic papers, industry reports, social media, and blogs, with direct links to every source.
Asset Allocation
Dynamic Dragon: Integrating Regime Detection into Strategic Asset Allocation
(Ni)
This paper refines the Dragon Portfolio proposed by Artemis Capital Management by replacing its static 20%-per-asset mix (equities, bonds, gold, commodity trend-following, long volatility) with regime-dependent weights identified via a Gaussian Mixture Model using cross-asset price features. Five regimes emerge: Crisis, Expansion, Tech Boom, QE, and Stagflation. In-sample (1927–2019) returns rise from 6.35% to 7.14% (Sharpe 1.03 to 1.13); out-of-sample (2020–2024) results remain similar.
Key takeaway: Regime-aware diversification improves risk-adjusted returns.
Commodities
When Gold Meets Copper: A Comprehensive Look at the Informative Role of the Relative Value of Gold on Global Stock Markets
(Roh, Kim, Yoon, and Yu)
Analyzing 23 developed markets (1990–2019), the paper finds that the Gold-to-Copper ratio, which rises during recessions and crisis periods, positively predicts 3- to 12-month stock returns. When gold outperforms copper, signaling economic stress and heightened risk aversion, expected returns rise and are followed by higher realized returns. The ratio forecasts one-year returns positively in 16 of 23 markets, with adjusted R² up to 15.6%.
Key takeaway: A rising Gold–Copper ratio signals bad times and a higher equity risk premium, typically followed by stronger future stock returns.
Crypto
On Risk Pricing and Arbitrage in the Cryptomarket
(Jamhamed, Martin, Rondeau, Thelissaint, and Tuffery)
The authors estimate eight systematic risk factors in the crypto market, market, momentum, volatility, macro confidence, DeFi risk-on behaviour, financial stress, equity-to-crypto reallocation, and optimism, using daily data for 29 coins (2019–2025). Betas are derived from rolling regressions and used to form high-minus-low beta portfolios to identify priced risks. Long–short portfolios with high exposure to volatility and DeFi risk-on factors deliver the strongest premia, achieving Sharpe ratios around 0.8 out-of-sample (pre-cost).
Key takeaway: Crypto assets primarily reward exposure to systemic stress and speculative DeFi exuberance.
Forecasting Cryptocurrency Markets: An Algorithmic Approach with Reddit-Based Relative Volume and Sentiment
(Noguchi, Mahadevu, Aggarwal, and Qin)
Using Reddit data from 2018–2024, the authors develop a long-only trading model driven by sentiment extracted with BERTweet. The model combines comment volume, sentiment polarity, and upvotes to generate daily allocation signals across six major cryptocurrencies. It consistently outperforms buy-and-hold, achieving gains even in down years like 2018 and 2022 (performance is before costs).
Key takeaway: When processed through BERT-based sentiment filters, Reddit discussions can generate consistent alpha in crypto markets.
Equities
Crowded spaces and anomalies
(Chincarini, Lazo-Paz, and Moneta)
Using U.S. data from 1980–2021, the paper studies how institutional crowding, measured by the
Days-ADV
ratio of institutional holdings to trading volume, affects the performance of equity anomalies. Stocks most crowded by institutions earn a Fama-French 3-factor alpha of 0.54% per month, while the least crowded lose 0.90%, yielding a 1.44% monthly spread. Across 11 anomalies, excess returns stem entirely from these crowded stocks and persist after publication. Crowding also predicts higher crash risk.
Key takeaway: Anomaly profits arise where many investors pile into the same trades, with crowding amplifying both expected returns and crash exposure.
Investors’ Quantitative Disclosure: Target Prices by Short Sellers
(Madelaine, Paugam, Stolowy, and Zhao)
Based on data from 1,237 activist short-selling campaigns, the study finds that when short sellers disclose explicit target prices, forecasting 65% declines on average, prices react faster: Attacked stocks fall 1.4% more on day 1 compared to attacks without target prices, and continue declining in the following weeks. Despite realized losses averaging only 9%, target prices still significantly predict future returns.
Key takeaway: Target prices from short sellers speed price discovery and predict returns.
Inefficiencies in the Securities Lending Market
(Daniel, Klos, and Rottke)
Borrowing costs for U.S. equities have surged, 43% of stocks now cost over 1% annually to short versus just 10% of stocks in 2003, creating persistent mispricing. A portfolio of high-borrow-cost stocks earns a −81.4% annual CAPM alpha, though this inefficiency is not directly exploitable after borrowing costs. However, long-only investors can improve performance by avoiding such stocks.
Key takeaway: Escalating short-sale frictions and intermediation bottlenecks have made equity markets less efficient.
The Lazy Man’s Momentum Strategy
(Estrada)
Using data on 23 developed-market equity indices from 1970–2024, the author introduces a 6-month momentum strategy applied to country-level portfolios and rebalanced semiannually. The long-short version earns a statistically significant 3.5% annual premium (volatility 9%), while the long-only portfolio delivers 13.1% annual returns versus 10.3% for MSCI World, with comparable risk.
Key takeaway: Even with just two rebalances a year across country ETFs, global momentum compounds wealth more effectively than a passive world portfolio.
When Buys Move Markets More than Sells: How Institutions Boost Prices without Net Buying
(Zhang)
Institutions execute buy orders far more aggressively than sells, subtly lifting prices even when net demand is unchanged. Using trade-level and 13F data, buy trades show 50–100% higher price impact, driven by incentives to enhance portfolio valuations through execution. A quarterly long–short timing strategy exploiting this pattern earns 13.2% annualized alpha (Sharpe 0.75, pre-costs).
Key takeaway: Institutional trading behavior can mechanically support prices, offering a potential short-horizon source of alpha.
Gambling with Dividends
(Klos, Muller-Dethard, Reinhardt, and Weber)
Many investors perceive dividends as “free money,” not as reductions in capital gains. Using German brokerage, experimental, and market data, the study shows that such “free” dividends often fund gambling in lottery-like stocks and options. Dividend payments boost lottery-stock purchases by 13–30 percentage points, leading to ~7% excess returns for lottery stocks during Germany’s May dividend season, with no reversal and a similar 5% effect in U.S. data.
Key takeaway: Dividend payouts create a predictable buying pressure as investors chase risky lottery trades.
Momentum Factor or Factor Momentum in REIT Market?
(Dobrynskaya, Tomtosov, and Rechmedina)
Traditional factors such as value, size, momentum, and profitability fail to generate alpha in the REIT market; most show weak or negative returns, and even the multifactor portfolio underperforms. In contrast, monthly factor momentum, going long the two best-performing factors and short the two worst, earns a 5.7% annual return, 5.9% alpha, and a Sharpe of 1.35 (pre-costs). Performance is robust across regimes, especially in bear markets.
Key takeaway: Static factor investing doesn’t work in REITs, but dynamically rotating across factors through momentum delivers significant alpha.
Machine Learning and Large Language Models
ChatGPT in Systematic Investing - Enhancing Risk-Adjusted Returns with LLMs
(Anic, Barbon, Seiz, and Zarattini)
This paper tests whether ChatGPT can enhance momentum investing by interpreting firm-specific news. Using data on S&P 500 constituents and minute-level news (2019–2025), ChatGPT 4.0 mini scores each stock’s news as supporting or contradicting momentum, guiding portfolio weights. The LLM-enhanced strategy achieves 18% vs. 15% annual returns over the full sample and Sharpe 1.06 vs. 0.79 out-of-sample (net of 2 bps costs), with gains persisting after ChatGPT’s 2023 cutoff.
Key takeaway: LLM-based news interpretation strengthens momentum signals and boosts alpha.
Can Large Language Models Predict the A-Share Market? Empirical Evidence from ChatGPT and DeepSeek
(Chen and Wei)
Using 122k Chinese financial news headlines (2023–2025), the study tests whether ChatGPT or DeepSeek can predict A-share returns. ChatGPT’s sentiment scores deliver stronger predictive power and higher directional accuracy, with sentiment emerging as the dominant feature across all models. As is often the case, ensemble approaches beat single-model forecasts.
Key takeaway: ChatGPT-based sentiment extraction significantly enhances short-term stock prediction accuracy in China’s A-share market.
Blogs
The Factor Mirage: How Quant Models Go Wrong
(CFA Institute)
R squared and Sharpe Ratio
(Rob Carver)
Value at Risk: Univariate Estimation Methods
(Portfolio Optimizer)
Sector Timing with Interest Rates
(Quantseeker)
Podcasts
The Trader Who Never Spoke...Until Now ft. David Druz
(Top Traders Unplugged)
Your Crisis Alpha: A Hidden Strategy For Market Crashes
(Meb Faber)
Turtle Talk Podcast – Episode 008: Battle of the Trends, Pyramids, and Outlier Hunting
(Aussie Turtles)
Social Media & Industry Research
Currency Valuations
(Dan Rasmussen, Verdad)
Why Hold Expensive Slow-Growing Stocks?
(Research Affiliates)
Diversifying Alternatives
(AQR)
Last Week’s Most Popular Links
Dark Side of the Day: Overnight Price Jumps and Short-Term Return Predictability
(Bahcivan, Dam, and Gonenc)
Causal and Predictive Modeling of Short-Horizon Market Risk and Systematic Alpha Generation Using Hybrid Machine Learning Ensembles
(Ranjan)
Revisiting the Structure of Trend Premia: When Diversification Hides Redundancy
(Etienne, Ohana, Benhamou, Guez, Setrouk, and Jacquot)
This Substack is reader-supported. Subscribe to get new research insights, strategy breakdowns, and exclusive posts, and help support my work.
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
