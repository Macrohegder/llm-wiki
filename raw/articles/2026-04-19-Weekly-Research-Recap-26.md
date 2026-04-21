# Weekly Research Recap

**原文链接**: https://www.quantseeker.com/p/weekly-research-recap-2d0

**发布时间**: Aug 26, 2025

**抓取时间**: 2026-04-19 22:25:35

---

## 摘要

Weekly Research Recap
Latest research on investing and trading
QuantSeeker
Aug 26, 2025
8
1
1
Share
Hi there! Time for this week’s recap of the latest investing research, with quick access to the full articles.
Commodities
Asymmetry and Crude Oil Returns
(Liu, Zhang, and Bouri)
This paper introduces a new distribution-based asymmetry factor (OIS) for crude oil that strongly predicts WTI futures returns. A one-standard-deviation rise in OIS, signaling right-tail clustering, forecasts a 3.15% drop in next-month returns (t≈–3.1, R²=4.1%). Out-of-sample, OIS achieves an R² of 4.2%, far exceeding standard predictors. Market timing using OIS shows a Sharpe ratio of 0.49 before costs and 0.42 after costs. Thus, when oil’s return distribution becomes more right-tailed, the next month’s returns are...

---

## 全文

Weekly Research Recap
Latest research on investing and trading
QuantSeeker
Aug 26, 2025
8
1
1
Share
Hi there! Time for this week’s recap of the latest investing research, with quick access to the full articles.
Commodities
Asymmetry and Crude Oil Returns
(Liu, Zhang, and Bouri)
This paper introduces a new distribution-based asymmetry factor (OIS) for crude oil that strongly predicts WTI futures returns. A one-standard-deviation rise in OIS, signaling right-tail clustering, forecasts a 3.15% drop in next-month returns (t≈–3.1, R²=4.1%). Out-of-sample, OIS achieves an R² of 4.2%, far exceeding standard predictors. Market timing using OIS shows a Sharpe ratio of 0.49 before costs and 0.42 after costs. Thus, when oil’s return distribution becomes more right-tailed, the next month’s returns are typically poor.
Currencies
Media tone is a priced risk factor in currency markets
(Lehkonen, Heimonen, and Pukthuanthong)
Using the Refinitiv MarketPsych Index, which distills tone from millions of news and social media articles, the paper shows that media tone is a priced risk factor in FX. A dollar-neutral long–short strategy delivers meaningful return spreads with Sharpe ratios near 0.5, outperforming benchmarks. Predictive power extends up to six months, being strongest in emerging markets. The results suggest media tone captures fundamental information overlooked by standard FX factors.
Equities
Freight Activity and Stock Returns: Evidence from Truck-Level Geolocation Data
(Li, Ruan, and Wang)
By tracking millions of truck visits to Chinese manufacturers, the authors build a freight-growth signal that captures real-time shifts in corporate activity. Firms with stronger freight momentum post higher sales, profitability, and hiring. A long–short strategy exploiting this signal earns 0.57–0.72% risk-adjusted monthly returns, unexplained by standard factors. Predictive power peaks ahead of earnings and is especially strong for firms with limited analyst coverage or no earnings guidance.
Machine Learning and Large Language Models
Variable selection for minimum-variance portfolios
(Moura, Santos, and Torrent)
Machine learning variable selection is shown to greatly enhance minimum-variance portfolio construction by parameterizing weights directly from firm characteristics rather than forecasting returns. Using 4,610 predictors, including interaction and non-linear terms, L2-boosting outperforms other methods and achieves Sharpe ratios above 1.0 net of costs. Overall, the results suggest that variable interactions overlooked by sparse models materially improve portfolio efficiency.
Textual Analysis in Financial Research and Practice: A Literature Review
(Vu, Wisniewski, and Skovoroda)
This survey paper discusses the evolution of textual analysis in finance, from early keyword counts and sentiment dictionaries to advanced transformer models like BERT, FinBERT, and GPT. It highlights both academic and practical applications, outlines challenges around data quality and interpretability, and offers readers an extensive set of references for further reading.
Options
Sizing the Risk: Kelly, VIX, and Hybrid Approaches in Put-Writing on Index Options
(Wysocki)
This paper evaluates S&P 500 short-put strategies with three sizing rules: Kelly, VIX-based (inverse to volatility levels), and a hybrid. Ultra-short maturities (0–5 days) and 5–10% OTM strikes yield the best Sharpe ratios. Kelly exceeds 3, VIX-based surpasses 6 but with high variability, while the hybrid consistently holds in the 2–4 range. The results clearly show that disciplined, dynamic sizing of short-dated put writing can significantly outperform equities while containing tail risk.
Trading TP 2 Option Violations
(Glasserman, Li, and Pirjol)
Rare mispricings in S&P 500 options, called TP2 (for calls) and RR2 (for puts) violations, where strike-maturity price ratios break theoretical monotonicity, can be systematically exploited. Long–short portfolios trading these violations earn about 4% per month, with Sharpe ratios often above 2 before costs, and remain profitable after transaction costs. Hit rates exceed 95%, and most anomalies correct within a few days.
Portfolio Construction
Cost-aware Portfolios in a Large Universe of Assets
(Fan, Medeiros, Yang, and Yang)
This paper introduces a cost-aware portfolio estimator (CAPE-S) that integrates proportional and quadratic trading costs directly into high-dimensional mean-variance optimization. In simulations, it achieves in-sample Sharpe ratios above 2.5 while cutting transaction costs by over 80% versus benchmarks. Applied to S&P 500 and Russell 2000 stocks (2017–2020), CAPE-S delivers the strongest out-of-sample Sharpe ratios (≈0.91 and ≈1.17), often the only strategy to avoid losses during downturns.
Eigen Portfolios: From Single Component Models to Ensemble Approaches
(Zhou and Luan)
The authors test PCA-based “eigen-portfolios” on DJIA stocks and find that choosing a single component by in-sample Sharpe ratio is highly unstable: The top eigen-portfolio delivered a 243% annualized return and Sharpe 1.54 in-sample, but collapsed to –85% return and Sharpe –0.56 out-of-sample. By contrast, combining the top four eigen-portfolios into an ensemble achieved 94% annualized return with Sharpe 1.05 (pre costs), beating an equal-weighted benchmark. Main takeaway: Diversifying across multiple PCA components yields more robust and investable strategies.
Systematic Trading
False Confidence in Systematic Trading: Illusion of Speed and Mirage of Performance
(Bloch)
This paper argues that short-window strategies often reflect noise rather than skill, as their signals rely on too few effective observations. At the same time, Sharpe ratios from short samples carry wide confidence intervals, making one-year performance, backtests, and ML models trained on Sharpe statistically fragile. With noise in both signals and evaluation, investors should be skeptical of short-sample Sharpe ratios without long horizons and robust validation.
Volatility
A New Star Is Born: Does the VIX1D Render Common Volatility Forecasting Models for the US Equity Market Obsolete?
(Albers)
The paper evaluates Cboe’s new VIX1D index as a tool for forecasting next-day S&P 500 volatility. It finds that VIX1D systematically overestimates realized volatility by about 36%, but adjusting it with a simple realized variance risk premium correction yields a 30% lower forecast error than HAR models and an 11% improvement over the best HAR-VIX specification. Directional accuracy is high, correctly predicting volatility up/down moves on 78% of days. That is, with a simple adjustment, VIX1D provides a fast, model-free, and highly accurate volatility forecast, making traditional short-horizon models largely redundant.
GitHub
Hands-On Large Language Models
-
Official code repo for the O'Reilly Book
Awesome-Quant-Machine-Learning-Trading
-
A collection of great resources
Podcasts
Laurens Bensdorp II - Building Strategies with Purpose
(The Algorithmic Advantage)
When Story, Fundamentals, and Technicals Align · Julian Komar
(Chat with Traders)
The Alpha Most Systems Miss ft. Yoav Git
(Top Traders Unplugged)
Social Media
On the “Virtue of Complexity” Debate
(Justina Lee, Bloomberg)
Understanding Return Expectations, Part 7
(Cliff Asness, AQR)
Last Week’s Most Popular Links
Scaled Factor Portfolio
(Jiang, Li, Ning, and Xue)
Robeco's One-Legged Vol Factor
(Eric Falkenstein)
Tracking Speculation from Expectations
(Su and Wen)
This Substack is reader-supported. To receive new posts and support my work, consider becoming a free or paid subscriber.
Subscribe
Disclaimer: This newsletter is for informational and educational purposes only and should not be construed as investment advice. The author does not endorse or recommend any specific securities or investments. While information is gathered from sources believed to be reliable, there is no guarantee of its accuracy, completeness, or correctness.
This content does not constitute personalized financial, legal, or investment advice and may not be suitable for your individual circumstances. Investing carries risks, and past performance does not guarantee future results. The author and affiliates may hold positions in securities discussed, and these holdings may change at any time without prior notification.
The author is not affiliated with, sponsored by, or endorsed by any of the companies, organizations, or entities mentioned in this newsletter. Any references to specific companies or entities are for informational purposes only.
The brief summaries and descriptions of research papers and articles provided in this newsletter should not be considered definitive or comprehensive representations of the original works. Readers are encouraged to refer to the original sources for complete and authoritative information.
This newsletter may contain links to external websites and resources. The inclusion of these links does not imply endorsement of the content, products, services, or views expressed on these third-party sites. The author is not responsible for the accuracy, legality, or content of external sites or for that of any subsequent links. Users access these links at their own risk.
The author assumes no liability for losses or damages arising from the use of this content. By accessing, reading, or using this newsletter, you acknowledge and agree to the terms outlined in this disclaimer.
8
1
1
Share

---

*由 Substack Strategy Tracker 自动抓取*
