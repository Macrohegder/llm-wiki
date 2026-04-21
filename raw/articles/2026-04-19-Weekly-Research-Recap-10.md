# Weekly Research Recap

**原文链接**: https://www.quantseeker.com/p/weekly-research-recap-1eb

**发布时间**: May 06, 2025

**抓取时间**: 2026-04-19 22:23:27

---

## 摘要

Weekly Research Recap
Latest research on investing and trading
QuantSeeker
May 06, 2025
6
1
Share
Time for another fresh set of top-tier investing papers from the past week, all carefully curated and linked for easy access.
If you’re enjoying these posts, a like or subscribe is always appreciated. Thank you for your support.
Crypto
Bitcoin Arbitrage: The Role of a Single Exchange
(Flowerday, Gandal, Halaburda, Olson, and Ardel)
Cross-exchange arbitrage has historically been common in crypto markets. This paper analyzes Bitcoin price differences across major exchanges from 2017 to 2020 and finds that Bitfinex was responsible for most discrepancies, driven by withdrawal restrictions, reliance on Tether, and regulatory uncertainty. When Bitfinex was excluded from the sample, most arbitrage op...

---

## 全文

Weekly Research Recap
Latest research on investing and trading
QuantSeeker
May 06, 2025
6
1
Share
Time for another fresh set of top-tier investing papers from the past week, all carefully curated and linked for easy access.
If you’re enjoying these posts, a like or subscribe is always appreciated. Thank you for your support.
Crypto
Bitcoin Arbitrage: The Role of a Single Exchange
(Flowerday, Gandal, Halaburda, Olson, and Ardel)
Cross-exchange arbitrage has historically been common in crypto markets. This paper analyzes Bitcoin price differences across major exchanges from 2017 to 2020 and finds that Bitfinex was responsible for most discrepancies, driven by withdrawal restrictions, reliance on Tether, and regulatory uncertainty. When Bitfinex was excluded from the sample, most arbitrage opportunities vanished. Overall, it’s a compelling case study of how structural frictions at individual exchanges can create arbitrage opportunities, many of which are difficult to exploit in practice.
Equities
How active is your (nominally) actively managed quantitative fund?
(Miguel and Chen)
Many funds claim to be actively managed, but some barely differ from basic index funds. This paper finds that half of quantitative U.S. equity mutual funds fall into that category, mimicking indexes despite being marketed as active. Even when they do try to be different, they often perform worse. For investors, the key takeaway is to be cautious: Quant funds may not offer the active edge their labels suggest.
On the Dynamics and Origins of Macroeconomic Announcement Risk Premia
(Buchta)
Prior research shows that stock returns are unusually high on macro news days, like inflation or jobs reports, but it's unclear what drives this pattern. Using detailed option data from 2016 to 2023, the author finds these returns spike during inflationary periods, when uncertainty about future interest rates is high. The paper concludes that macro announcement risk premia are largely driven by monetary policy uncertainty.
Characteristics-Based Reversals Exploiting the Gap between Predicted and Realized Returns
(Park, Yee, and Ko)
This paper develops a long-short mean-reversion strategy by finding the 200 most similar historical stock-months for each stock based on 94 firm characteristics. It predicts each stock’s return decile and compares it to its actual decile in the following month. The strategy goes long stocks that underperformed their prediction and short those that outperformed, earning an annualized return of around 20% before costs.
Small, Value, or Small/Value?
(Estrada)
Many investors try to boost returns by tilting toward small and cheap stocks, but is it better to buy separate funds for size and value or one that blends both? This paper shows that a single fund combining both traits not only simplifies the portfolio but also delivers stronger long-term performance. As a result, investors can earn higher returns and gain more exposure to proven factors without the added complexity.
Machine Learning and Large Language Models
Simplified: A Closer Look at the Virtue of Complexity in Return Prediction
(Buncic)
An influential paper by Kelly et al. (2024) showed that out-of-sample performance improves as models become increasingly complex and overparameterized. More recently, Cartea et al. (2025) argue that the benefits of such complexity depend on data quality, as complex models are prone to overfitting noise. This new paper by Buncic also challenges the value of complexity, arguing that the original strong results in favor of complexity stem from questionable modeling assumptions and design choices. Once those are corrected, simpler models outperform.
Fine-Tuning is All You Need: Compact Models Can Outperform GPT's Classification Abilities
(Lefort, Benhamou, Ohana, Saltiel, and Guez)
This study shows that smaller models like FinBERT, when fine-tuned on data labeled using next-day market returns, can outperform GPT-4 in zero-shot settings. The results suggest that compact, task-specific models may deliver faster and more affordable sentiment analysis without sacrificing accuracy.
AI Tools for Actuaries
(Wuthrich, Richman, Avanzi, Lindholm, Mayer, Schelldorfer, and Scognamiglio)
This is a comprehensive set of lecture notes covering supervised and unsupervised learning, large language models, and much more.
Model complexity and the performance of global versus regional models
(Chen, Hanauer, and Kalsbach)
Some earlier research suggests that locally focused models predict stock returns better than globally trained ones due to regional differences. However, this paper argues that such findings often rely on simple models and backward-looking analysis. Testing both basic and advanced machine learning methods across 24 countries, the authors find that while simple models perform slightly better with local data, complex models, such as neural networks, consistently deliver stronger results, especially when trained globally. The findings support using more sophisticated models for return prediction.
Macro
Navigating Economic Downturns: Insights from Survey-Based Recession Indicators
(Sun)
Spotting recessions early enough to adjust a portfolio is challenging, and official recession announcements often come too late. This paper shows that recession probabilities from the quarterly Survey of Professional Forecasters lead actual NBER recessions by at least one quarter and prove useful for market timing.
Portfolio Optimization
Portfolio Optimization for Pension Purposes: Literature Review
(Moreira, Santos, and Gonzalez)
This is a literature review focused on how investment strategies are designed for pension portfolios. It examines recent academic work and finds that many approaches still use conventional methods that overlook the unique challenges of managing retirement funds over long time horizons. The authors point to the need for more practical models that embrace newer technologies, consider environmental and social goals, and reflect real-world constraints like regulations and aging populations.
Private Equity
Building Trust in Illiquid Markets: an AI-Powered Replication of Private Equity Funds
(Benhamou, Ohana, Guez, Setrouk, and Jacquot)
Private equity has delivered strong long-term returns, but its returns are artificially smooth and come with limited liquidity and transparency, making it difficult to manage. This paper introduces a daily-traded alternative built from equity index futures, volatility hedges, and trend filters. The approach closely tracks private equity benchmarks, showing high return correlations, strong Sharpe ratios, and smaller losses during market downturns.
Real Estate
The case for listed real estate in a multi-asset portfolio
(Carvalho, Stevens, Vis, and Zakaria)
The paper suggests that many investors may avoid listed real estate because it seems too volatile and equity-like to reflect real property. Yet over longer periods, it is shown to track physical real estate closely while offering better liquidity, accessibility, and income. The authors find that adding listed real estate can improve portfolio returns and diversification without sacrificing flexibility or inflation protection.
Blogs
Macro-quantamental investment handbook
(Macrosynergy)
Can I build a scalping bot? A blogpost with numerous double digit SR
(Rob Carver)
When the Equity Premium Fades, Alpha Shines
(van Vliet)
Revisiting Pragmatic Asset Allocation: Simple Rules for Complex Times
(Quantpedia)
Weekly Research Insights
(Quantseeker)
FinTwit and LinkedIn
Prompt Engineering, via Kaggle
(@aaditsh)
Data Science and Machine Learning Book
(@swapnakpanda)
Investing Amid Trade Wars
(Kai Wu - Sparkline Capital)
What Should You Do When You Don’t Know What to Do?
(Man Group)
GitHub
FinGPT - Open-Source Financial Large Language Models
TradingAgents: Multi-Agents LLM Financial Trading Framework
StockSharp - trading platform
Podcasts
Do Index Funds Incur Adverse Selection Costs?
(Rational Reminder)
Inside the Gerber Statistic with Sander Gerber of Hudson Bay Capital
(Masters in Business)
Kenneth Rogoff on Monetary Moves, Fiscal Gambits, and Classical Chess
(Conversations with Tyler)
Is the Trend Still Your Friend? ft. Rob Carver
(Top Traders Unplugged)
Last Week’s Most Popular Links
Global Tactical Asset Allocation: Updated Results and Real-Market Implementation Using Python and IBKR
(Zarattini)
Quantitative Methods in Finance
(Vansteenberghe)
Salience, Asymmetric Effect and Stock Returns
(Wang, Yao, and Liu)
This Substack is reader-supported. To receive new posts and support my work, consider becoming a free or paid subscriber.
Subscribe
Disclaimer: This newsletter is for informational and educational purposes only and should not be construed as investment advice. The author does not endorse or recommend any specific securities or investments. While information is gathered from sources believed to be reliable, there is no guarantee of its accuracy, completeness, or correctness.
This content does not constitute personalized financial, legal, or investment advice and may not be suitable for your individual circumstances. Investing carries risks, and past performance does not guarantee future results. The author and affiliates may hold positions in securities discussed, and these holdings may change at any time without prior notification.
The author is not affiliated with, sponsored by, or endorsed by any of the companies, organizations, or entities mentioned in this newsletter. Any references to specific companies or entities are for informational purposes only.
The brief summaries and descriptions of research papers and articles provided in this newsletter should not be considered definitive or comprehensive representations of the original works. Readers are encouraged to refer to the original sources for complete and authoritative information.
This newsletter may contain links to external websites and resources. The inclusion of these links does not imply endorsement of the content, products, services, or views expressed on these third-party sites. The author is not responsible for the accuracy, legality, or content of external sites or for that of any subsequent links. Users access these links at their own risk.
The author assumes no liability for losses or damages arising from the use of this content. By accessing, reading, or using this newsletter, you acknowledge and agree to the terms outlined in this disclaimer.
6
1
Share

---

*由 Substack Strategy Tracker 自动抓取*
