# Predicting commodity returns

**原文链接**: https://www.quantseeker.com/p/predicting-commodity-returns

**发布时间**: Aug 04, 2024

**抓取时间**: 2026-04-19 22:18:57

---

## 摘要

Predicting commodity returns
Insights from recent research on sentiment
QuantSeeker
Aug 04, 2024
12
3
Share
Introduction
Past research has identified several variables capable of predicting commodity returns, ranging from technical indicators to macro variables. This article focuses on the predictive power of sentiment, as recent studies have indicated its potential as a predictor of commodity returns. I review some of the latest research on this topic and conclude with key takeaways for investors.
Sentiment
Sentiment has been shown to predict returns across various asset classes and can be measured in multiple ways, each capturing different nuances. This article focuses on three types of sentiment that have been identified as return predictors: Business sentiment, news sentiment, and soci...

---

## 全文

Predicting commodity returns
Insights from recent research on sentiment
QuantSeeker
Aug 04, 2024
12
3
Share
Introduction
Past research has identified several variables capable of predicting commodity returns, ranging from technical indicators to macro variables. This article focuses on the predictive power of sentiment, as recent studies have indicated its potential as a predictor of commodity returns. I review some of the latest research on this topic and conclude with key takeaways for investors.
Sentiment
Sentiment has been shown to predict returns across various asset classes and can be measured in multiple ways, each capturing different nuances. This article focuses on three types of sentiment that have been identified as return predictors: Business sentiment, news sentiment, and social media sentiment.
Business Sentiment
Surveys and indicators of business confidence and manufacturing activity have demonstrated meaningful predictive power in several studies. Similarly, broad measures of economic activity and economic uncertainty have also proven useful for prediction.
For instance, Hammerschmid (2018) predicts returns on a broad basket of commodity futures using a diverse set of predictive variables. She finds that macro conditions predict returns positively, with the strongest results for the OECD business confidence index and the OECD leading indicator. This effect is more pronounced for commodities most sensitive to economic conditions, such as energy and metals.
Cotter et al. (2023) predict returns on the S&P Goldman Sachs Commodity Index using a large set of variables, identifying the OECD business confidence index and leading indicator as among the most statistically and economically significant predictors. Similarly, Dudda et al. (2024) consider a range of predictors and find measures of economic activity and economic uncertainty to predict returns out-of-sample. Consistent with the previous findings, predictability is strongest for commodities most sensitive to business cycles.
Focusing on commodity spot returns, Hollstein et al. (2021) and Delle Chiaie (2021) document a close link between economic conditions and returns, including predictability of returns. Baumeister et al. (2022) aggregate several indicators of global economic activity and economic uncertainty, finding that they predict energy markets.
For earlier contributions on the link between macroeconomic conditions and commodity returns, see for example Bailey and Chan (1993), Pagano and Pisani (2009), and Gargano and Timmermann (2014).
See also Gao and Suss (2015), who use partial least squares to construct a sentiment index based on six market variables including the VIX, SKEW indices, and IPO returns. Their findings indicate that market sentiment is a highly significant predictor of returns, with a positive sign across all commodity sectors.
Ralph Sueppel at Macrosynergy has at least two articles on business sentiment predicting commodity returns. In Sueppel (2023a), he finds that changes in the ISM and Philadelphia manufacturing surveys, along with inventory growth and economic growth, predict returns on base metals versus non-industrial commodities. He constructs a trading strategy to demonstrate this predictability. In Sueppel (2023b), he develops a global index of changes in manufacturing confidence across countries and finds the index to predict returns on industrial commodities positively. A trading strategy based on global confidence changes is shown to generate a meaningful Sharpe ratio.
Hence, there is considerable evidence showing that business sentiment and economic conditions are linked to commodity returns and possess predictive power. This evidence spans various variable definitions and time periods. The strongest results are observed for commodities most closely linked to economic conditions. When exploring predictability using economic variables, it’s recommended to use non-revised, point-in-time data to achieve realistic results. Such data can be obtained from commercial vendors or free datasets, such as the OECD database, with vintages starting in 1999, or from the ALFRED database, subject to availability. In addition, combining multiple indicators is likely to lead to improved results as well as exploring economic nowcasting indices as predictors.
News Sentiment
In addition to business sentiment, news sentiment plays an important role in predicting commodity returns. Sentiment analysis on news and text has seen substantial advancements in recent years, evolving from dictionary approaches to today’s transformer models. For those interested, recent survey papers by Cui et al. (2023), Du et al. (2024) and parts of Nie et al. (2024) provide comprehensive overviews of these developments.
Numerous research studies have demonstrated that news sentiment can predict commodity returns. A widely used dataset is the LSEG (Refinitiv) MarketPsych dataset, which covers news across asset classes from thousands of sources, including social media. For a detailed background of the dataset, see Peterson (2016). MarketPsych delivers real-time updates on news sentiment for individual commodities, facilitating the testing of cross-sectional strategies. Chi et al. (2024a) aggregate news sentiment on a weekly basis and consider a long-short strategy, going long commodities with the most positive sentiment and short those with the most negative sentiment. This strategy generates a Sharpe ratio comparable to that of other known strategies such as momentum while remaining largely unexplained by them. Moreover, they show that combining known commodity strategies with news sentiment boosts overall Sharpe ratios.
Chi et al. (2024b) differentiate between new and old news, finding that sentiment from old news has the strongest effect, likely due to investor underreaction. Chi et al. (2024c) focus on the EmotionVsFact
variable in the MarketPsych dataset, which essentially measures the emotional language versus factual reporting in a news item. The authors find that this measure has a low correlation with the standard news sentiment measures discussed above, suggesting potential diversification benefits. Sorting commodities according to the EmotionVsFact
variable and going long commodities with high emotional content and short those with low emotional content generates a significant return spread, with the strongest results for commodities with generally low media coverage. Moreover, this strategy is largely unrelated to existing commodity factors.
Other papers that have used the MarketPsych dataset are Shen et al. (2017), who find short-term predictability of returns, and Huang et al. (2018), who predict returns across asset classes, with the strongest results for commodities. Interestingly, they find that aggregating news sentiment from all asset classes further increases predictability, suggesting that it could be worthwhile to incorporate news from other assets when predicting commodities.
RavenPack news analytics is another commercial dataset that measures text sentiment from vast amounts of unstructured data and has been used extensively in research across asset classes. A recent paper by Fernandez-Perez et al. (2024) applies RavenPack data, starting with known signals such as basis, momentum, and skewness, and uses news sentiment as an overlay on those signals. For example, a commodity with an attractive momentum signal and simultaneously highly positive news sentiment will see an overall boost in its signal. The authors employ a weekly rebalanced strategy and report a substantial increase in Sharpe ratios compared to the original strategies. The gain in Sharpe ratios from news tone decreases with holding period and seems to vanish after a holding period of about 3-4 weeks, suggesting that it is a relatively fast signal. The authors compute a breakeven cost of 88 basis points on average for the weekly rebalanced news-overlay portfolios.
There is an extensive literature focusing on news sentiment and predictability in oil markets specifically. For example, Brandt and Gao (2019) find that macro news sentiment from Ravenpack has predictive power for oil returns. Lee (2022) focuses on event extraction from news on crude oil, coupled with forecasting of oil returns, and offers a rich reference list for further reading. Santos et al. (2023) provide a comprehensive survey paper on the topic.
Related literature focuses on measuring news and text sentiment on climate and weather risks to predict returns on agricultural commodities. For example, by aggregating the climate risk variables from Faccini et al. (2023), who measure the news intensity of topics related to climate risks, Ma et al. (2024) find that aggregate climate risk predicts returns on agricultural commodities. While the main results refer to spot returns, the authors also find significant predictability for the Invesco DB Agriculture ETF (DBA), which tracks the most liquid agricultural futures contracts. Hence, it is likely that the main results can be generalized to individual futures contracts.
Social Media Sentiment
While social media sources are included in many commercial datasets on news sentiment, some papers focus exclusively on social media. For example, Fan et al. (2023) retrieve millions of tweets related to commodities from the Twitter API and construct sentiment scores for individual commodities using the financial dictionary of Loughran and McDonald (2011). They implement a monthly rebalanced strategy by sorting commodities on the monthly change in their sentiment scores, going long commodities in the top ranking and short those in the bottom ranking. The strategy reportedly delivers Sharpe ratios that are double those of conventional commodity strategies while being largely unexplained by other strategies. The turnover of the strategy is about double that of other commodity strategies, yet it still allows for high breakeven transaction costs and survives when excluding the most illiquid commodities.
Related to social media sentiment, several papers use search volume data from Google Trends to measure investor attention. For instance, Fernandez-Perez et al. (2020) measure investor attention to hazards affecting commodities by tracking search volumes for words such as blizzard, storm, wildfire, drought etc. They estimate the loading of each individual commodity on changes in weekly search volumes. Subsequently, they sort commodities according to their loadings, going short commodities with large loadings and long those with small loadings. This strategy generates a higher Sharpe ratio and lower turnover compared to other commodity strategies and is reported to survive assumed transaction costs. The strategy is believed to capitalize on temporary mispricing induced by hazard-related fears.
Takeaways
Overall, the evidence suggests that sentiment possesses predictive power for commodity returns across various sentiment types, commodity sectors, and time periods. First, business sentiment and economic conditions tend to predict returns positively, with the strongest results observed for commodities sensitive to global business cycles, such as energy and industrial metals. Second, commodity-specific news and social media sentiment have been shown to predict returns across a broad cross-section of commodities. Third, weather and climate-related risks seem to contain information about future returns on agricultural commodities. Interestingly, some of the sentiment strategies above exhibit low correlations with other known commodity strategies. These findings suggest that incorporating sentiment analysis into commodity trading strategies could potentially enhance returns and diversification for investors and traders.
Thanks for reading. Consider a free or paid subscription to receive new posts and support my work.
Subscribe
References
Bailey, Warren, and K. C. Chang, 1993, Macroeconomic influences and the variability of the commodity futures basis,
Journal of Finance
48, 555-573.
Baumeister, Christiane, Dimitris Korobilis, and Thomas K. Lee, 2022, Energy markets and global economic conditions,
Review of Economics and Statistics
104, 828-844.
Brandt, Michael W., and Lin Gao, 2019, Macro fundamentals or geopolitical events? A textual analysis of news events for crude oil,
Journal of Empirical Finance
51, 64-94.
Chi, Yeguang, Lina El-Jahel, and Thanh Vu, 2024a, News sentiment and commodity futures investing, SSRN Working Paper.
Chi, Yeguang, Lina El-Jahel, and Thanh Vu, 2024b, Novel and old news sentiment in commodity futures markets, SSRN Working Paper.
Chi, Yeguang, Lina El-Jahel, and Thanh Vu, 2024c, Media emotion intensity and commodity futures pricing, SSRN Working Paper.
Cotter, John, Emmanuel Eyiah-Donkor, and Valerio Poti, 2023, Commodity futures return predictability and intertemporal asset pricing,
Journal of Commodity Markets
31, 100289.
Cui, Jingfeng, Zhaoxia Wang, Seng-Beng Ho, and Erik Cambria, 2023, Survey on sentiment analysis: evolution of research methods and topics,
Artificial Intelligence Review
56, 8469-8510.
Delle Chiaie, Simona, Laurent Ferrara, and Domenico Giannone, 2021, Common factors of commodity prices,
Journal of Applied Econometrics
37, 461-476.
Du, Kelvin, Frank Xing, Rui Mao, and Erik Cambria, 2024, Financial sentiment analysis: Techniques and applications,
ACM Computing Surveys
56, 1-42.
Dudda, Tom L., Tony Klein, Duc Khuong Nguyen, and Thomas Walther, 2024, Common drivers of commodity futures, SSRN Working Paper.
Faccini, Renato, Rastin Matin, and George Skiadopoulos, 2023, Dissecting climate risks: Are they reflected in stock prices?,
Journal of Banking & Finance
155, 106948.
Fan, John Hua, Sebastian Binnewies, and Sanuri De Silva, 2023, Wisdom of crowds and commodity pricing,
Journal of Futures Markets
43, 1040-1068.
Fernandez-Perez, Adrian, Ana-Maria Fuertes, Marcos Gonzalez-Fernandez, and Joelle Miffre, 2020, Fear of hazards in commodity futures markets,
Journal of Banking and Finance
119, 105902.
Fernandez-Perez, Adrian, Ana-Maria Fuertes, Joelle Miffre, and Nan Zhao, 2024, Newswire tone-overlay commodity portfolios, SSRN Working Paper.
Gao, Lin, and Stephan Suss, 2015, Market sentiment in commodity futures returns,
Journal of Empirical Finance
33, 84-103.
Gargano, Antonio, and Allan Timmermann, 2014, Forecasting commodity price indexes using macroeconomic and financial predictors,
International Journal of Forecasting
30, 825-843.
Hammerschmid, Regina, Commodity return predictability, 2018, SSRN Working Paper.
Hollstein, Fabian, Marcel Prokopczuk, Bjorn Tharann, and Chardin Wese Simen, 2021, Predictability in commodity markets: Evidence from more than a century,
Journal of Commodity Markets
24, 100171.
Huang, Dashan, Heikki Lehkonen, Kuntara Pukthuanthong, and Guofu Zhou, 2018, Sentiment across markets, SSRN Working Paper.
Lee, Meisin, 2022, Crude oil forecasting via events and outlook extraction from commodity news, Monash University, PhD Thesis.
Loughran, Tim, and Bill McDonald, 2011, When is a liability not a liability? Textual analysis, dictionaries, and 10-Ks,
Journal of Finance
66, 35-65.
Ma, Yong, Mingtao Zhou, and Shuaibing Li, 2024, Weathering market swings: Does climate risk matter for agricultural commodity price predictability?, SSRN Working Paper.
Nie, Yuqi, Yaxuan Kong, Xiaowen Dong, John M. Mulvey, H. Vincent Poor, Qingsong Wen, and Stefan Zohren, 2024, A survey of large language models for financial applications: Progress, prospects and challenges, arXiv Working Paper.
Pagano, Patrizio, and Massimiliano Pisani, 2009, Risk-adjusted forecasts of oil prices,
B.E. Journal of Macroeconomics
9.
Peterson, Richard L., 2016, Appendix A: Understanding the Thomson Reuters MarketPsych Indices,
Trading on Sentiment: The Power of Minds over Markets
(Wiley).
Santos, Marcus Vinicius, Fernando Morgado-Dias, and Thiago C. Silva, 2023, Oil sector and sentiment analysis-A review,
Energies
16, 4824.
Shen, Jiancheng, Mohammad Najand, Feng Dong, and Wu He, 2017, News and social media emotions in the commodity market,
Review of Behavioral Finance
9, 148-168.
Sueppel, Ralph, 2023a, Predicting base metal futures returns with economic data,
Macrosynergy
.
Sueppel, Ralph, 2023b, Business sentiment and commodity future returns,
Macrosynergy
.
Disclaimer: The author is not affiliated with, employed by, or compensated by any of the companies or data providers mentioned in this article. This article is for informational and educational purposes only and should not be construed as investment advice. The author does not endorse any specific securities or investments mentioned. While information is gathered from sources believed to be reliable, there is no guarantee of its accuracy, completeness, or correctness.
This content does not offer personalized financial, legal, or investment advice and may not be suitable for your individual circumstances. Investing carries risks, and past performance does not guarantee future results. The author and affiliates may hold positions in securities discussed without prior notification.
The brief summaries and descriptions of research papers and articles provided in this article are the author's own interpretations of the findings and content. These summaries should not be considered as definitive or comprehensive representations of the original works. Readers are encouraged to refer to the original sources for complete and authoritative information.
12
3
Share

---

*由 Substack Strategy Tracker 自动抓取*
