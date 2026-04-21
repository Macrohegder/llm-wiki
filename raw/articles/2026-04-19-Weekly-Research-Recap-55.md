# Weekly Research Recap

**原文链接**: https://www.quantseeker.com/p/weekly-research-recap-07a

**发布时间**: Mar 17, 2026

**抓取时间**: 2026-04-19 22:29:01

---

## 摘要

Weekly Research Recap
Latest research on investing and trading
QuantSeeker
Mar 17, 2026
12
2
Share
Welcome to this week’s Tuesday roundup, your curated selection of the most actionable investing ideas from the past week, spanning academic research, industry reports, blog posts, and insightful discussions across social media, with links throughout.
Commodities
An Index of Commodity Futures Returns Since 1871
(Janardanan, Qiao, and Rouwenhorst)
Using a uniquely hand-collected dataset of 230 commodity futures contracts dating back to 1871, the paper shows that a diversified futures index has generated approximately excess returns of 5.5% with a volatility of 14% (Sharpe ratio of about 0.38), comparable to equities. It outperforms stocks 43% of the time and beats inflation by more than 6% annu...

---

## 全文

Weekly Research Recap
Latest research on investing and trading
QuantSeeker
Mar 17, 2026
12
2
Share
Welcome to this week’s Tuesday roundup, your curated selection of the most actionable investing ideas from the past week, spanning academic research, industry reports, blog posts, and insightful discussions across social media, with links throughout.
Commodities
An Index of Commodity Futures Returns Since 1871
(Janardanan, Qiao, and Rouwenhorst)
Using a uniquely hand-collected dataset of 230 commodity futures contracts dating back to 1871, the paper shows that a diversified futures index has generated approximately excess returns of 5.5% with a volatility of 14% (Sharpe ratio of about 0.38), comparable to equities. It outperforms stocks 43% of the time and beats inflation by more than 6% annually.
Key takeaway: Commodities deliver equity-like premia with low co-movement to stocks, supporting their role as a diversifier.
Equities
Save The Date: Analyst/Investor Days as a Trading Signal
(Cabrera, Kolokolova, and Zhang)
Using 1,000 U.S. Analyst/Investor Days, the paper shows that stocks rise about 3.7% from the announcement to the event, with significantly larger (7.6%) run-ups when firms actively “hype” the event, often followed by reversals. A long–short strategy (long hosts, short peers) earns 0.08 to 0.13% daily alpha (Sharpe of about 1.1 to 1.2), remaining significant after costs.
Key takeaway: Trading the pre-event run-up to Investor Days is a possible event-driven strategy.
Price Impact in Closing Auctions, Opening Auctions, and Continuous Markets: A Benchmark for Cost of Trading on Anomalies
(Goyal, Jegadeesh, and Wu)
Using U.S. equity data, the paper shows trading costs depend heavily on execution venue: Closing auctions have a lower price impact than continuous trading, while opening auctions are the least liquid. Executing in lower-cost venues reduces anomaly strategy costs to about 9–21 bps annually (ex-microcaps).
Key takeaway: Execution matters, using lower-impact venues like closing auctions can meaningfully improve net returns.
FX
Bias-Corrected Feature Selection for Short-Horizon FX Trading: Evidence from Liquid Currency Pairs
(Jukl and Lansky)
Across 14 liquid FX pairs, controlling feature-selection bias reveals a small but exploitable edge: Next-day strategies generate roughly 15 to 30% annual returns, Sharpe ratios above 1 (portfolio >2), and 55–60% win rates, even after costs. However, performance decays rapidly, and at longer horizons, Sharpe turns negative.
Key takeaway: Any edge in FX is extremely short-lived; robust performance depends more on proper feature selection than on model sophistication.
Machine Learning and Large Language Models
E-TRENDS: Enhanced LSTM Trend Forecasting for Equities
(Buchanan and Benhamou)
An LSTM model forecasting changes in equity trends improves predictive accuracy and trading performance. Across 30 S&P 500 stocks, it increases directional accuracy from 56% to 62% and lifts out-of-sample Sharpe from 0.85 to 1.10, outperforming linear and tree-based models. Gains are robust across most stocks and across different market regimes.
Key takeaway: Predicting changes in trends with nonlinear methods can improve the robustness and risk-adjusted performance of trend-following strategies.
Beyond Prompting: An Autonomous Framework for Systematic Factor Investing via Agentic AI
(Huang and Fan)
The paper proposes an agentic AI framework that replaces manual factor research with an iterative loop that proposes, tests, and refines trading signals under strict out-of-sample validation. Individual factors deliver statistically significant alphas with Sharpe ratios typically above 1, while combining them yields about 60% annual returns with a Sharpe of about 3.1 and drawdowns around 11%.
Key takeaway: Integrating a disciplined, self-improving research loop into the investment process can systematically generate robust and scalable alpha.
DatedGPT: Preventing Lookahead Bias in Large Language Models with Time-Aware Pretraining
(Yan, Tang, Gao, Jiang, and Lu)
Many LLMs suffer from look-ahead bias as they may “know the future” because training data includes events after the prediction date. This paper introduces DATEDGPT, a series of models trained separately for each year (2013–2024) using only data available up to that point. The models remain competitive, and tests show a clear performance drop on post-cutoff data, indicating no future leakage.
Key takeaway: Strictly controlling the model’s information set is essential to mitigate look-ahead bias in financial LLMs.
Macro
Stagflation Risk and Financial Markets: A Real-Time Composite Index
(Bonaparte)
The paper builds a real-time stagflation index combining macro conditions and geopolitical sentiment. Higher stagflation significantly lowers contemporaneous equity returns and raises volatility. However, it has little predictive power for future returns, while strongly and persistently forecasting higher volatility over the next 1 to 6 months.
Key takeaway: Stagflation risk is primarily priced through volatility, making the index more useful for risk management than return prediction.
Performance Evaluation
The Sharpe Stability Ratio: Temporal Consistency of Risk-Adjusted Performance
(Bajo Traver and Rodriguez Dominguez)
The paper argues that the classic Sharpe ratio hides an important dimension: How returns are earned over time. It introduces the Sharpe Stability Ratio (SSR), which penalizes strategies whose performance comes in bursts rather than steadily. Using simulations and hedge fund indices, it shows that strategies with similar Sharpe ratios can differ sharply in consistency.
Key takeaway: True skill shows up as consistency; favor strategies with stable risk-adjusted returns, not just high averages.
Blogs
War and Oil
(John H. Cochrane)
Skewness as a Time-Series Signal in Commodity Futures
(QuantSeeker)
Transformer Models for Alpha Generation: A Practical Guide
(Jonathan Kinlay)
How to write a tweet that gets over 300k views; and why diversification is probably good
(Rob Carver)
Anomaly-Based Trading Strategies in the Real Estate Sector. Can the Market Be Beaten?
(Quantpedia)
Podcasts
Annie Duke on Thinking in Bets - And Why Winners Can Be Wrong
(Odds On Open)
The World’s BEST Trader Reveals the 10 Commandments To Profitable Live Trading
(Words of Rizdom)
Managing Uncertainty: How a Major UK Pension CIO Thinks About Managing Billions
(Capital Horizons)
Social Media & Industry Research
Why Value, Quality, and Momentum Belong Together
(Research Affiliates)
An Interview with Jordan Brooks: Multi-Asset Strategies and Asset Allocation
(AQR)
Unlocking Hidden Value: How Corporate Language Reveals the Future of Intangible Investment
(Alpha Architect)
Last Week’s Most Popular Links
Quantitative Strategies For Momentum And Trend Reversal: Integrating Macroeconomic Factors, Advanced Signal Processing, And Regime Awareness
(Charlotte Sim)
Systematic Reversal and Industry Momentum
(Gao, Li, Yuan, and Zhou)
Generative AI for Finance: A New Framework
(Chai, Jiang, Meng, You, and Zhou)
This Substack is reader-supported. To receive new posts and support my work, consider becoming a free or paid subscriber.
Subscribe
Disclaimer: This newsletter is for informational and educational purposes only and should not be construed as investment advice. The author does not endorse or recommend any specific securities or investments. While information is gathered from sources believed to be reliable, there is no guarantee of its accuracy, completeness, or correctness.
This content does not constitute personalized financial, legal, or investment advice and may not be suitable for your individual circumstances. Investing carries risks, and past performance does not guarantee future results. The author and affiliates may hold positions in securities discussed, and these holdings may change at any time without prior notification.
The author is not affiliated with, sponsored by, or endorsed by any of the companies, organizations, or entities mentioned in this newsletter. Any references to specific companies or entities are for informational purposes only.
The brief summaries and descriptions of research papers and articles provided in this newsletter should not be considered definitive or comprehensive representations of the original works. Readers are encouraged to refer to the original sources for complete and authoritative information.
This newsletter may contain links to external websites and resources. The inclusion of these links does not imply endorsement of the content, products, services, or views expressed on these third-party sites. The author is not responsible for the accuracy, legality, or content of external sites or for that of any subsequent links. Users access these links at their own risk.
The author assumes no liability for losses or damages arising from the use of this content. By accessing, reading, or using this newsletter, you acknowledge and agree to the terms outlined in this disclaimer.
Paid subscriptions may not be available in all jurisdictions and may change without notice.
12
2
Share

---

*由 Substack Strategy Tracker 自动抓取*
