# Weekly Research Insights

**原文链接**: https://www.quantseeker.com/p/weekly-research-insights-ba0

**发布时间**: Apr 24, 2025

**抓取时间**: 2026-04-19 22:23:14

---

## 摘要

Weekly Research Insights
Predicting Returns with Geopolitical Risk | Insider Trading Signals | Systematic or Idiosyncratic Momentum?
QuantSeeker
Apr 24, 2025
7
1
Share
In this week’s edition of Research Insights, I discuss three recent papers with actionable takeaways and ideas for investors and traders. The first finds significant predictability of stock returns using an index of geopolitical risks. The second examines return predictability based on a broad set of insider trading signals. Finally, the third paper tests whether stock momentum is driven more by firm-specific returns or factor exposures.
In This Post:
Predicting Returns with Geopolitical Risk
Insider Trading Signals
Systematic or Idiosyncratic Momentum?
Predicting Returns with Geopolitical Risk
Background
Geopolitical tensio...

---

## 全文

Weekly Research Insights
Predicting Returns with Geopolitical Risk | Insider Trading Signals | Systematic or Idiosyncratic Momentum?
QuantSeeker
Apr 24, 2025
7
1
Share
In this week’s edition of Research Insights, I discuss three recent papers with actionable takeaways and ideas for investors and traders. The first finds significant predictability of stock returns using an index of geopolitical risks. The second examines return predictability based on a broad set of insider trading signals. Finally, the third paper tests whether stock momentum is driven more by firm-specific returns or factor exposures.
In This Post:
Predicting Returns with Geopolitical Risk
Insider Trading Signals
Systematic or Idiosyncratic Momentum?
Predicting Returns with Geopolitical Risk
Background
Geopolitical tensions, such as wars, threats, or major international conflicts, are known to affect economies and markets. In recent years, several papers have examined the impact of geopolitical risk on stock returns. For example,
Sheng et al. (2025)
construct a risk index based on news articles from 1984 to 2025 and find that geopolitical risk predicts returns both in the time series and the cross-section.
A recent paper by Gonçalves et al. “
The Pricing of Geopolitical Tensions over a Century
”
addresses the same question but makes a key distinction between actual events (like wars) and the
threat
of such events. They use the Geopolitical Threats (GPT) and Geopolitical Acts (GPA) indices developed by
Caldara and Iacoviello (2022)
. GPT reflects
expectations
of future conflict (like rising military tensions), while GPA captures
realized events
(like wars or terrorist attacks).
Below, I plot the two indices, obtained from
policyuncertainty.com
. The two indices behave differently, with a monthly correlation of approximately 0.4 between them. The paper studies how each index relates differently to asset prices and return predictability.
Key Findings
Dataset & Methodology
The study uses almost 100 years of monthly data, spanning from 1927 to 2024, based on the indices developed by
Caldara and Iacoviello (2022)
.
The authors study how Geopolitical Threats (GPT) and Geopolitical Acts (GPA) relate to investor perceptions (via risk ratings and surveys), risk premia across various assets (stocks, bonds, anomaly portfolios), and real economic outcomes such as investment and consumption.
To isolate the effect of geopolitical tensions, they control for other well-known risk indices, such as policy uncertainty and market volatility.
Main Results
GPT is forward-looking and aligns more closely with investor sentiment than GPA. It rises before major conflicts, while GPA reacts after events happen.
GPT is priced and predicts stock returns:
It explains return differences across individual stocks, anomaly strategies, and international equities and bonds.
Going long risky stocks that perform poorly when GPT increases, and shorting those that hedge against geopolitical threats, yields a significant risk premium of approximately 4.2% per year.
Unlike GPA, GPT predicts market returns positively, especially over longer horizons (3-5 years). That is, a rise in geopolitical threats tends to be associated with a drop in contemporaneous returns and a rise in expected returns.
GPT also predicts real-world outcomes:
Increases in GPT are linked to future drops in firm investment and a higher likelihood of consumption disasters (e.g., prolonged economic declines).
These predictive relationships do not hold for GPA, making GPT a more meaningful and forward-looking signal.
Implications for Investors
In line with the idea that markets are forward-looking, the paper highlights that geopolitical threats, not just actual events, are critical for understanding risk premia. GPT’s ability to predict returns both in the time series and the cross-section suggests it captures priced risk and could serve as a useful factor in portfolio construction.
However, the authors point out that the premium associated with GPT is time-varying and tends to be stronger when public attention to geopolitical tensions is high, implying that timing matters. It would be interesting to study how GPT interacts with other return predictors to better capture changes in expected returns and improve return predictability.
Insider Trading Signals
Yesterday, I came across this
tweet
showing a spike in the insider buying/selling ratio, suggesting that insiders are now stepping in to buy. This reminded me of an excellent paper on insider trading signals, which could be a valuable source of ideas for those exploring return prediction strategies.
Past research in this area has proposed various indicators to identify “informed” insider trades, such as trading patterns around earnings announcements or trades by specific roles like CFOs. However, these signals have mostly been studied in isolation and focused on the U.S. market. The paper “
Synthesizing Information-Driven Insider Trade Signals
”
by Heckmann et al. takes a different approach by combining multiple well-established insider trading signals into a single composite indicator and tests whether it can predict stock returns across 34 countries.
Key Findings
Dataset & Methodology
The authors analyze over 3.7 million insider trades from 350,000 insiders across 34 countries between 2000 and 2021.
They construct 16 indicators for “buy” signals and 17 for “sell” signals based on prior academic research. These include signals such as clustered trades by multiple insiders, trades by CFOs, and trades after periods of insider silence. (See the Appendix for a detailed description of all signals.)
A simple aggregate measure for each stock is constructed: if a stock has at least two more buy signals than sell signals (or vice versa), it triggers a trade signal for the following month. The authors also explore other aggregation methods, including a data-driven model.
Main Results
Long–short portfolios based on the composite signal generate statistically significant alphas in about two-thirds of countries.
Performance is strongest in small-cap stocks, and buy signals (long positions) outperform sell signals.
The signal is effective globally, including in emerging markets, and is not heavily influenced by differences in insider trading laws or governance.
Performance fades with longer holding periods, suggesting that insiders mostly have a short-term informational edge. However, equal-weighted long–short portfolios remain statistically significant even at 12 months.
Implications for Investors
The paper shows that combining several simple insider trading signals into a single score improves return prediction and delivers stronger, more consistent performance than relying on any individual signal. The base case signal works best over a one-month holding period in equal-weighted portfolios, suggesting the alpha is concentrated in smaller firms. However, the authors also test alternative constructions that show promise in value-weighted settings, offering more scalable options. While implementation challenges like transaction costs and reporting lags remain, as discussed in the paper, the paper provides a rich toolkit of insider trading signals that could also enhance machine learning models.
Systematic or Idiosyncratic Momentum?
Background
In recent years, researchers have debated whether stock momentum is primarily driven by momentum in underlying equity factors, such as size or value, which then spill over into individual stocks. An influential paper by
Ehsani and Linnainmaa (2022)
argues that momentum in stock returns originates at the factor level and is transmitted to stocks through their exposures to these factors. However, others have suggested that momentum may instead stem from company-specific news and behaviors, pointing to a different underlying mechanism.
The paper “
Firm-specific versus systematic momentum
” by Schmid et al. directly tests these competing explanations by separating stock returns into market-driven (systematic) and firm-specific components to determine which one truly accounts for momentum profits.
Key Findings
Dataset & Methodology:
The authors analyze U.S. stock data from July 1963 to December 2019, covering returns and accounting information.
They break down each stock’s return into two parts: one that reflects its exposure to the Fama-French five-factor model (the systematic component), and another that captures firm-specific performance (the residual or idiosyncratic return).
Each month, stocks are sorted based on these two components, both for short-term (past one month) and medium-term (past 12 months excluding the most recent month), and portfolio performance is tracked accordingly.
Main Results:
When using past 12-month returns, portfolios sorted on firm-specific momentum significantly outperform those sorted on factor-driven momentum. This finding is robust across different factor models.
For short-term returns (past one month), the pattern reverses: factor-driven momentum produces positive returns, while firm-specific momentum leads to strongly negative returns, indicating mean reversion.
These results highlight a clear contrast between short-term and medium-term dynamics. Short-term momentum is more systematic, while medium-term momentum is predominantly driven by firm-specific return patterns.
Implications for Investors
The paper clearly shows that successful medium-term stock momentum strategies are primarily driven by firm-specific signals, such as earnings surprises or analyst revisions, rather than by broader market trends or factor exposures. In contrast, over shorter horizons, firm-specific returns tend to mean-revert, while factor-driven returns exhibit continuation. Hence, there is a clear distinction in the data where medium-term momentum is firm-specific and short-term momentum is more systematically driven.
This Substack is reader-supported. To receive new posts and support my work, consider becoming a free or paid subscriber.
Subscribe
The discussion above is based on the following research papers. For full details, please refer to the original sources:
References
Caldara, Dario, and Matteo Iacoviello, 2022,
Measuring geopolitical risk
,
American Economic Review
112 (4), 1194-1225.
Ehsani, Sina, and Juhani T. Linnainmaa, 2022,
Factor momentum and the momentum factor
,
Journal of Finance
77 (3), 1877-1919 (
SSRN Working Paper 3014521
).
Gonçalves, Andrei S., Alessandro Melone, and Andrea Ricciardi, 2025, The pricing of geopolitical tensions over a century,
SSRN Working Paper 5218714
.
Graef, Frank, Daniel Hoechle, and Markus Schmid, 2024, Firm-specific versus systematic momentum,
SSRN Working Paper 5053270
.
Heckmann, Jens, Heiko Jacobs, and Patrick Schwarz, 2023, Synthesizing information-driven insider trade signals,
SSRN Working Paper 4537187
.
Sheng, Jinfei, Zheng Sun, and Qiguang Wang, 2025, Geopolitical risk and stock returns,
SSRN Working Paper 5207012
.
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
